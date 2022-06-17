import ctypes
import platform

import glfw
if platform.system() == "Windows":
    from OpenGL import WGL
    from .platform.windows import *
elif platform.system() == "Linux":
    from OpenGL import GLX
    from .platform.linux import *

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


__all__ = [
    "OpenGLGraphics",
]
