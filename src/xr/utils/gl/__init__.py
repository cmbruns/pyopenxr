from abc import ABC, abstractmethod
from ctypes import byref, c_void_p, cast, pointer

from OpenGL import GL

import xr

from .. import GraphicsContextProvider


class GraphicsBinding(ABC):
    @property
    @abstractmethod
    def pointer(self):
        """Return the native pointer or ctypes handle backing this graphics binding."""
        pass


def create_graphics_binding(context_provider: GraphicsContextProvider) -> GraphicsBinding:
    try:
        from .egl_util import EGLGraphicsBinding
        return EGLGraphicsBinding(context_provider)
    except AttributeError:
        pass
    try:
        return WGLGraphicsBinding(context_provider)
    except AttributeError:
        pass
    try:
        return GLXGraphicsBinding(context_provider)
    except AttributeError:
        pass
    raise RuntimeError("No supported graphics backend found.")


class GLXGraphicsBinding(GraphicsBinding):
    def __init__(self, context_provider: GraphicsContextProvider):
        from OpenGL import GLX
        context_provider.make_current()
        drawable = GLX.glXGetCurrentDrawable()
        context = GLX.glXGetCurrentContext()
        display = GLX.glXGetCurrentDisplay()
        self.graphics_binding = xr.GraphicsBindingOpenGLXlibKHR(
            x_display=display,
            glx_drawable=drawable,
            glx_context=context,
        )
        self._pointer = cast(pointer(self.graphics_binding), c_void_p)

    @property
    def pointer(self):
        return self._pointer


class WGLGraphicsBinding(GraphicsBinding):
    def __init__(self, context_provider: GraphicsContextProvider):
        from OpenGL import WGL
        self.graphics_binding = xr.GraphicsBindingOpenGLWin32KHR()
        context_provider.make_current()
        self.graphics_binding.h_dc = WGL.wglGetCurrentDC()
        self.graphics_binding.h_glrc = WGL.wglGetCurrentContext()
        self._pointer = cast(pointer(self.graphics_binding), c_void_p)

    @property
    def pointer(self):
        return self._pointer


class OpenGLGraphics(object):
    def __init__(
            self,
            instance: xr.Instance,
            system: xr.SystemId,
            context_provider: GraphicsContextProvider,
    ) -> None:
        self.context_provider = context_provider
        self.pxrGetOpenGLGraphicsRequirementsKHR = cast(
            xr.get_instance_proc_addr(
                instance=instance,
                name="xrGetOpenGLGraphicsRequirementsKHR",
            ),
            xr.PFN_xrGetOpenGLGraphicsRequirementsKHR
        )
        self.graphics_requirements = xr.GraphicsRequirementsOpenGLKHR()
        result = self.pxrGetOpenGLGraphicsRequirementsKHR(
            instance,
            system,
            byref(self.graphics_requirements))
        result = xr.check_result(xr.Result(result))
        if result.is_exception():
            raise result
        self.context_provider.make_current()
        self.graphics_binding = create_graphics_binding(context_provider)
        self.swapchain_framebuffer = None
        self.color_to_depth_map: dict[int, int] = {}

    def __enter__(self):
        return self

    def __exit__(self, exception_type, value, traceback):
        self.destroy()

    def begin_frame(self, layer_view, color_texture):
        self.make_current()
        GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, self.swapchain_framebuffer)
        GL.glViewport(layer_view.sub_image.image_rect.offset.x,
                      layer_view.sub_image.image_rect.offset.y,
                      layer_view.sub_image.image_rect.extent.width,
                      layer_view.sub_image.image_rect.extent.height)
        depth_texture = self.get_depth_texture(color_texture)
        GL.glFramebufferTexture2D(GL.GL_FRAMEBUFFER, GL.GL_COLOR_ATTACHMENT0, GL.GL_TEXTURE_2D, color_texture, 0)
        GL.glFramebufferTexture2D(GL.GL_FRAMEBUFFER, GL.GL_DEPTH_ATTACHMENT, GL.GL_TEXTURE_2D, depth_texture, 0)

    def destroy(self):
        self.make_current()
        GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, 0)
        if self.swapchain_framebuffer is not None:
            GL.glDeleteFramebuffers(1, [self.swapchain_framebuffer, ])
            self.swapchain_framebuffer = None
        self.context_provider.destroy()

    @staticmethod
    def end_frame():
        GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, 0)

    def get_depth_texture(self, color_texture) -> int:
        # If a depth-stencil view has already been created for this back-buffer, use it.
        if color_texture in self.color_to_depth_map:
            return self.color_to_depth_map[color_texture]
        # This back-buffer has no corresponding depth-stencil texture, so create one with matching dimensions.
        GL.glBindTexture(GL.GL_TEXTURE_2D, color_texture)
        width = GL.glGetTexLevelParameteriv(GL.GL_TEXTURE_2D, 0, GL.GL_TEXTURE_WIDTH)
        height = GL.glGetTexLevelParameteriv(GL.GL_TEXTURE_2D, 0, GL.GL_TEXTURE_HEIGHT)

        depth_texture = GL.glGenTextures(1)
        GL.glBindTexture(GL.GL_TEXTURE_2D, depth_texture)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_NEAREST)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_NEAREST)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_CLAMP_TO_EDGE)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_CLAMP_TO_EDGE)
        GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_DEPTH_COMPONENT32, width, height, 0, GL.GL_DEPTH_COMPONENT, GL.GL_FLOAT, None)
        self.color_to_depth_map[color_texture] = depth_texture
        return depth_texture

    def initialize_resources(self):
        self.make_current()
        self.swapchain_framebuffer = GL.glGenFramebuffers(1)

    def make_current(self):
        self.context_provider.make_current()

    @staticmethod
    def select_color_swapchain_format(runtime_formats):
        # List of supported color swapchain formats.
        supported_color_swapchain_formats = [
            GL.GL_RGB10_A2,
            GL.GL_RGBA16F,
            # The two below should only be used as a fallback, as they are linear color formats without enough bits for color
            # depth, thus leading to banding.
            GL.GL_RGBA8,
            GL.GL_RGBA8_SNORM,
            #
            GL.GL_SRGB8,  # Linux SteamVR beta 1.24.2 has only these...
            GL.GL_SRGB8_ALPHA8,
        ]
        for rf in runtime_formats:
            for sf in supported_color_swapchain_formats:
                if rf == sf:
                    return sf
        raise RuntimeError("No runtime swapchain format supported for color swapchain")

    @property
    def swapchain_image_type(self):
        return xr.SwapchainImageOpenGLKHR


__all__ = [
    "create_graphics_binding",
    "GLXGraphicsBinding",
    "GraphicsBinding",
    "OpenGLGraphics",
    "WGLGraphicsBinding",
]

from . import context_object
from .context_object import *
__all__.extend(context_object.__all__)
