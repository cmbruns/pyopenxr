from ctypes import byref, c_void_p, cast, pointer
import platform

import glfw
if platform.system() == "Windows":
    from OpenGL import WGL
elif platform.system() == "Linux":
    from OpenGL import GLX
import xr


class GLFWContext(object):
    @staticmethod
    def required_extensions():
        return [xr.KHR_OPENGL_ENABLE_EXTENSION_NAME]

    def __init__(self, instance: xr.Instance, system_id: xr.SystemId) -> None:
        if not glfw.init():
            raise xr.XrException("GLFW initialization failed")
        self.window_size = (64, 64)
        glfw.window_hint(glfw.VISIBLE, False)
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
            system_id,
            byref(self.graphics_requirements))
        result = xr.check_result(xr.Result(result))
        if result.is_exception():
            raise result
        glfw.window_hint(glfw.DOUBLEBUFFER, False)
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 5)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        self.window = glfw.create_window(*self.window_size, "pyopenxr glfw OpenGL", None, None)
        if self.window is None:
            raise xr.XrException("Failed to create GLFW window")
        self.make_current()
        # Attempt to disable vsync on the desktop window, or
        # it will interfere with the OpenXR frame loop timing
        glfw.swap_interval(0)
        self.graphics_binding = None
        if platform.system() == "Windows":
            self.graphics_binding = xr.GraphicsBindingOpenGLWin32KHR()
            self.graphics_binding.h_dc = WGL.wglGetCurrentDC()
            self.graphics_binding.h_glrc = WGL.wglGetCurrentContext()
        elif platform.system() == "Linux":
            drawable = GLX.glXGetCurrentDrawable()
            context = GLX.glXGetCurrentContext()
            display = GLX.glXGetCurrentDisplay()
            self.graphics_binding = xr.GraphicsBindingOpenGLXlibKHR(
                x_display=display,
                glx_drawable=drawable,
                glx_context=context,
            )
        else:
            raise NotImplementedError
        self.graphics_binding_pointer = cast(
            pointer(self.graphics_binding),
            c_void_p,
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.destroy()

    def destroy(self):
        self.make_current()
        glfw.destroy_window(self.window)
        self.window = None
        glfw.terminate()

    def make_current(self):
        glfw.make_context_current(self.window)


__all__ = [
    "GLFWContext",
]
