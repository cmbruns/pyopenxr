from abc import ABC, abstractmethod
from ctypes import byref, c_void_p, cast, pointer

import xr
from ..graphics_context_provider import GraphicsContextProvider


def create_graphics_binding(context_provider: GraphicsContextProvider):
    try:
        from OpenGL import EGL
        return EGLGraphicsBinding(context_provider)
    except ImportError:
        pass
    try:
        from OpenGL import WGL
        return WGLGraphicsBinding(context_provider)
    except ImportError:
        pass
    try:
        from OpenGL import GLX
        return GLXGraphicsBinding(context_provider)
    except ImportError:
        pass
    raise RuntimeError("No supported graphics backend found.")


class GraphicsBinding(ABC):
    @property
    @abstractmethod
    def pointer(self):
        """Return the native pointer or ctypes handle backing this graphics binding."""
        pass


class EGLGraphicsBinding(GraphicsBinding):
    def __init__(self, context_provider: GraphicsContextProvider):
        from OpenGL import EGL
        self.graphics_binding = xr.GraphicsBindingEGLMNDX()
        display = context_provider.egl_display()
        context = context_provider.egl_context()
        self.graphics_binding.display = display
        self.graphics_binding.context = context
        self.graphics_binding.get_proc_address = cast(
            EGL.eglGetProcAddress.load(), xr.PFN_xrEglGetProcAddressMNDX)
        config = c_void_p()
        num_configs = EGL.EGLint()
        config_attribs = [
            EGL.EGL_RENDERABLE_TYPE, EGL.EGL_OPENGL_BIT,
            EGL.EGL_SURFACE_TYPE, EGL.EGL_PBUFFER_BIT,
            EGL.EGL_RED_SIZE, 8,
            EGL.EGL_GREEN_SIZE, 8,
            EGL.EGL_BLUE_SIZE, 8,
            EGL.EGL_ALPHA_SIZE, 8,
            EGL.EGL_NONE
        ]
        attribs_list = (EGL.EGLint * len(config_attribs))(*config_attribs)
        EGL.eglChooseConfig(display, attribs_list, byref(config), 1, byref(num_configs))
        self.graphics_binding.config = config
        self._pointer = cast(pointer(self.graphics_binding), c_void_p)

    @property
    def pointer(self):
        return self._pointer


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
