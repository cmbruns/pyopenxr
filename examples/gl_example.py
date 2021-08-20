import ctypes
import xr

# TODO: finish translating example at
# https://github.com/jherico/OpenXR-Samples/blob/master/src/examples/sdl2_gl_single_file_example_c.cpp
# Next task: prepare_window()


class GlExample(object):
    def __init__(self):
        self.instance = None
        self.system_id = None
        self.pxrGetOpenGLGraphicsRequirementsKHR = None
        self.graphics_requirements = None
        self.render_target_size = None

    def destroy(self):
        if self.instance is not None:
            xr.destroy_instance(self.instance)
        self.system_id = None

    def run(self):
        self.prepare()
        self.destroy()  # TODO: raii

    def prepare(self):
        self.prepare_xr_instance()
        self.prepare_xr_system()

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


if __name__ == "__main__":
    GlExample().run()
