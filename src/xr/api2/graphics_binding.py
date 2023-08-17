import platform
from ctypes import cast, byref, pointer, c_void_p

import xr
from xr.api2 import IGLContext


class GraphicsBinding(object):
    def __init__(self, instance: xr.Instance, system_id: xr.SystemId):
        self.instance = instance
        self.system_id = system_id

    def get_graphics_requirements(self):
        # 1 - get graphics requirements from OpenXR
        pxr_get_open_gl_graphics_requirements_khr = cast(
            xr.get_instance_proc_addr(
                instance=self.instance,
                name="xrGetOpenGLGraphicsRequirementsKHR",
            ),
            xr.PFN_xrGetOpenGLGraphicsRequirementsKHR
        )
        graphics_requirements = xr.GraphicsRequirementsOpenGLKHR()
        result = pxr_get_open_gl_graphics_requirements_khr(
            self.instance,
            self.system_id,
            byref(graphics_requirements))
        result = xr.check_result(xr.Result(result))
        if result.is_exception():
            raise result
        return graphics_requirements

    def pointer(self, graphics_context: IGLContext):
        self.get_graphics_requirements()  # Unused but must-run
        graphics_context.make_current()
        if platform.system() == "Windows":
            from OpenGL import WGL
            graphics_binding = xr.GraphicsBindingOpenGLWin32KHR()
            graphics_binding.h_dc = WGL.wglGetCurrentDC()
            graphics_binding.h_glrc = WGL.wglGetCurrentContext()
        elif platform.system() == "Linux":
            from OpenGL import GLX
            drawable = GLX.glXGetCurrentDrawable()
            context = GLX.glXGetCurrentContext()
            display = GLX.glXGetCurrentDisplay()
            graphics_binding = xr.GraphicsBindingOpenGLXlibKHR(
                x_display=display,
                glx_drawable=drawable,
                glx_context=context,
            )
        else:
            raise NotImplementedError
        graphics_context.done_current()
        return cast(pointer(graphics_binding), c_void_p)


__all__ = [
    "GraphicsBinding",
]
