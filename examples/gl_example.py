import ctypes

import glfw
from OpenGL import WGL

import xr

# TODO: finish translating example at
# https://github.com/jherico/OpenXR-Samples/blob/master/src/examples/sdl2_gl_single_file_example_c.cpp
# Next task: continue work on prepare_xr_session()


class GlExample(object):
    def __init__(self):
        self.instance = None
        self.system_id = None
        self.pxrGetOpenGLGraphicsRequirementsKHR = None
        self.graphics_requirements = None
        self.render_target_size = None
        self.window = None
        self.session = None

    def destroy(self):
        if self.instance is not None:
            xr.destroy_instance(self.instance)
        self.system_id = None
        if self.window is not None:
            glfw.terminate()  # TODO: raii

    def run(self):
        self.prepare()
        self.destroy()  # TODO: raii

    def prepare(self):
        self.prepare_xr_instance()
        self.prepare_xr_system()
        self.prepare_window()
        self.prepare_xr_session()

    def prepare_xr_instance(self):
        requested_extensions = [xr.KHR_OPENGL_ENABLE_EXTENSION_NAME]
        discovered_extensions = xr.enumerate_instance_extension_properties()
        for extension in requested_extensions:
            assert extension in discovered_extensions
        # TODO: str arguments
        app_info = xr.ApplicationInfo(b"gl_example", 0, b"pyopenxr", 0, xr.XR_CURRENT_API_VERSION)
        # TODO: buffer
        bs = [s.encode() for s in requested_extensions]
        arr_type = ctypes.c_char_p * len(bs)
        str_arr = arr_type()
        for i, s in enumerate(bs):
            str_arr[i] = s
        ici = xr.InstanceCreateInfo(0, app_info, 0, None, 1, str_arr)
        self.instance = xr.create_instance(ici)
        # TODO: pythonic wrapper
        pfn = xr.get_instance_proc_addr(
            self.instance, "xrGetOpenGLGraphicsRequirementsKHR")
        self.pxrGetOpenGLGraphicsRequirementsKHR = ctypes.cast(pfn, xr.PFN_xrGetOpenGLGraphicsRequirementsKHR)
        print(self.pxrGetOpenGLGraphicsRequirementsKHR)
        instance_properties = xr.get_instance_properties(self.instance)
        print(instance_properties)

    def prepare_xr_system(self):
        get_info = xr.SystemGetInfo(xr.FormFactor.HEAD_MOUNTED_DISPLAY.value)
        self.system_id = xr.get_system(self.instance, ctypes.pointer(get_info))  # TODO: not a pointer
        sys_props = xr.get_system_properties(self.instance, self.system_id)
        view_configs = xr.enumerate_view_configurations(self.instance, self.system_id)
        assert view_configs[0] == xr.ViewConfigurationType.PRIMARY_STEREO.value  # TODO: equality...
        view_config_views = xr.enumerate_view_configuration_views(
            self.instance, self.system_id, xr.ViewConfigurationType.PRIMARY_STEREO.value)  # TODO: pass enum
        assert len(view_config_views) == 2
        assert view_config_views[0].recommended_image_rect_height == view_config_views[1].recommended_image_rect_height
        self.render_target_size = (view_config_views[0].recommended_image_rect_width * 2, view_config_views[0].recommended_image_rect_height)
        self.graphics_requirements = xr.GraphicsRequirementsOpenGLKHR()
        result = self.pxrGetOpenGLGraphicsRequirementsKHR(
            self.instance, self.system_id, ctypes.byref(self.graphics_requirements))  # TODO: pythonic wrapper
        result = xr.exceptions.check_result(xr.Result(result))
        if result.is_exception():
            raise result

    def prepare_window(self):
        assert glfw.init()
        glfw.window_hint(glfw.DOUBLEBUFFER, False)
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        gws = [int(s / 4) for s in self.render_target_size]
        self.window = glfw.create_window(*gws, "GLFW Window", None, None)
        if self.window is None:
            glfw.terminate()  # TODO raii
            assert False
        glfw.make_context_current(self.window)
        glfw.swap_interval(0)

    def prepare_xr_session(self):
        hdc = WGL.wglGetCurrentDC()
        context = WGL.wglGetCurrentContext()
        window = glfw.get_win32_window(self.window)
        wgl_context = glfw.get_wgl_context(self.window)
        # TODO: debug this structure GraphicsBindingOpenGLWin32KHR
        # HDC type is not processed properly
        # May need to include Windows.h and enhance parser
        graphics_binding = xr.GraphicsBindingOpenGLWin32KHR(
            WGL.wglGetCurrentDC(),
            WGL.wglGetCurrentContext(),
        )
        pp = ctypes.cast(ctypes.pointer(graphics_binding), ctypes.c_void_p)
        sci = xr.SessionCreateInfo(pp, 0, self.system_id)
        self.session = xr.create_session(self.instance, sci)  # Failing here...
        reference_spaces = xr.enumerate_reference_spaces(self.session)
        rsci = xr.ReferenceSpaceCreateInfo()
        space = xr.create_reference_space(self.session, rsci)


if __name__ == "__main__":
    GlExample().run()
