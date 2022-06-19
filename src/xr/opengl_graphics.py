import ctypes
import platform

import glfw
if platform.system() == "Windows":
    from OpenGL import WGL
    from .platform.windows import *
elif platform.system() == "Linux":
    from OpenGL import GLX
    from .platform.linux import *
from OpenGL import GL

from .enums import *
from .exception import *
from .typedefs import *
from .functions import *


class OpenGLGraphics(object):
    def __init__(
            self,
            instance: InstanceHandle,
            system: SystemId,
            title: str = "glfw OpenGL window",
    ) -> None:
        if not glfw.init():
            raise XrException("GLFW initialization failed")
        self.window_size = (64, 64)
        glfw.window_hint(glfw.VISIBLE, False)
        self.pxrGetOpenGLGraphicsRequirementsKHR = ctypes.cast(
            get_instance_proc_addr(
                instance=instance,
                name="xrGetOpenGLGraphicsRequirementsKHR",
            ),
            PFN_xrGetOpenGLGraphicsRequirementsKHR
        )
        self.graphics_requirements = GraphicsRequirementsOpenGLKHR()
        result = self.pxrGetOpenGLGraphicsRequirementsKHR(
            instance,
            system,
            ctypes.byref(self.graphics_requirements))
        result = check_result(Result(result))
        if result.is_exception():
            raise result
        glfw.window_hint(glfw.DOUBLEBUFFER, False)
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 5)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        self.window = glfw.create_window(*self.window_size, title, None, None)
        if self.window is None:
            raise XrException("Failed to create GLFW window")
        glfw.make_context_current(self.window)
        # Attempt to disable vsync on the desktop window, or
        # it will interfere with the OpenXR frame loop timing
        glfw.swap_interval(0)
        self.graphics_binding = None
        if platform.system() == "Windows":
            self.graphics_binding = GraphicsBindingOpenGLWin32KHR()
            self.graphics_binding.h_dc = WGL.wglGetCurrentDC()
            self.graphics_binding.h_glrc = WGL.wglGetCurrentContext()
        elif platform.system() == "Linux":
            drawable = GLX.glXGetCurrentDrawable()
            context = GLX.glXGetCurrentContext()
            display = GLX.glXGetCurrentDisplay()
            self.graphics_binding = GraphicsBindingOpenGLXlibKHR(
                x_display=display,
                glx_drawable=drawable,
                glx_context=context,
            )
        else:
            raise NotImplementedError

    def __enter__(self):
        return self

    def __exit__(self, exception_type, value, traceback):
        self.destroy()

    @staticmethod
    def destroy():
        glfw.terminate()

    def make_current(self):
        glfw.make_context_current(self.window)

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
        ]
        for rf in runtime_formats:
            for sf in supported_color_swapchain_formats:
                if rf == sf:
                    return sf
        raise RuntimeError("No runtime swapchain format supported for color swapchain")

    @property
    def swapchain_image_type(self):
        return SwapchainImageOpenGLKHR


__all__ = [
    "OpenGLGraphics",
]
