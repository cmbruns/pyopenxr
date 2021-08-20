import ctypes

import glfw
from OpenGL import GL, WGL

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
        self.projection_layer_views = (xr.CompositionLayerProjectionView * 2)(*([xr.CompositionLayerProjectionView()] * 2))
        self.projection_layer = xr.CompositionLayerProjection(None, 0, None, 2, self.projection_layer_views)
        self.swapchain_create_info = xr.SwapchainCreateInfo(None)
        self.swapchain = None
        self.swapchain_images = None
        self.fbo_id = None
        self.fbo_depth_buffer = None

    def run(self):
        self.prepare()
        while not glfw.window_should_close(self.window):
            self.frame()
        self.destroy()  # TODO: raii

    def prepare(self):
        self.prepare_xr_instance()
        self.prepare_xr_system()
        self.prepare_window()
        self.prepare_xr_session()
        self.prepare_xr_swapchain()
        self.prepare_xr_composition_layers()
        self.prepare_gl_framebuffer()

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
        ici = xr.InstanceCreateInfo(None, 0, app_info, 0, None, 1, str_arr)
        self.instance = xr.create_instance(ici)
        # TODO: pythonic wrapper
        pfn = xr.get_instance_proc_addr(
            self.instance, "xrGetOpenGLGraphicsRequirementsKHR")
        self.pxrGetOpenGLGraphicsRequirementsKHR = ctypes.cast(pfn, xr.PFN_xrGetOpenGLGraphicsRequirementsKHR)
        print(self.pxrGetOpenGLGraphicsRequirementsKHR)
        instance_properties = xr.get_instance_properties(self.instance)
        print(instance_properties)

    def prepare_xr_system(self):
        get_info = xr.SystemGetInfo(None, xr.FormFactor.HEAD_MOUNTED_DISPLAY.value)
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
            None,
            WGL.wglGetCurrentDC(),
            WGL.wglGetCurrentContext(),
        )
        pp = ctypes.cast(ctypes.pointer(graphics_binding), ctypes.c_void_p)
        sci = xr.SessionCreateInfo(pp, 0, self.system_id)
        self.session = xr.create_session(self.instance, sci)  # Failing here...
        reference_spaces = xr.enumerate_reference_spaces(self.session)
        for rs in reference_spaces:
            print(rs)
        # TODO: default constructors for Quaternion, Vector3f, Posef, ReferenceSpaceCreateInfo
        rsci = xr.ReferenceSpaceCreateInfo(None, 3, xr.Posef(xr.Quaternionf(0, 0, 0, 1), xr.Vector3f(0, 0, 0)))
        self.projection_layer.space = xr.create_reference_space(self.session, rsci)
        swapchain_formats = xr.enumerate_swapchain_formats(self.session)
        for scf in swapchain_formats:
            print(scf)

    def prepare_xr_swapchain(self):
        self.swapchain_create_info.usage_flags = xr.SWAPCHAIN_USAGE_TRANSFER_DST_BIT
        self.swapchain_create_info.format = GL.GL_SRGB8_ALPHA8
        self.swapchain_create_info.sample_count = 1
        self.swapchain_create_info.array_size = 1
        self.swapchain_create_info.face_count = 1
        self.swapchain_create_info.mip_count = 1
        self.swapchain_create_info.width = self.render_target_size[0]
        self.swapchain_create_info.height = self.render_target_size[1]
        self.swapchain = xr.create_swapchain(self.session, self.swapchain_create_info)
        self.swapchain_images = xr.enumerate_swapchain_images(self.swapchain)
        for si in self.swapchain_images:
            print(si)

    def prepare_xr_composition_layers(self):
        self.projection_layer.view_count = 2
        self.projection_layer.views = self.projection_layer_views
        for eye_index in range(2):
            layer_view = self.projection_layer_views[eye_index]
            layer_view.sub_image.swapchain = self.swapchain
            layer_view.sub_image.image_rect.extent.width = self.render_target_size[0] // 2
            layer_view.sub_image.image_rect.extent.width = self.render_target_size[1]
            if eye_index == 1:
                layer_view.sub_image.image_rect.offset.x = layer_view.sub_image.image_rect.extent.width

    def prepare_gl_framebuffer(self):
        self.fbo_depth_buffer = GL.glGenRenderbuffers(1)
        GL.glBindRenderbuffer(GL.GL_RENDERBUFFER, self.fbo_depth_buffer)
        if self.swapchain_create_info.sample_count == 1:
            GL.glRenderbufferStorage(
                GL.GL_RENDERBUFFER,
                GL.GL_DEPTH24_STENCIL8,
                self.swapchain_create_info.width,
                self.swapchain_create_info.height,
            )
        else:
            GL.glRenderbufferStorageMultisample(
                GL.GL_RENDERBUFFER,
                self.swapchain_create_info.sample_count,
                GL.GL_DEPTH24_STENCIL8,
                self.swapchain_create_info.width,
                self.swapchain_create_info.height,
            )
        self.fbo_id = GL.glGenFramebuffers(1)
        GL.glBindFramebuffer(GL.GL_DRAW_FRAMEBUFFER, self.fbo_id)
        GL.glFramebufferRenderbuffer(
            GL.GL_DRAW_FRAMEBUFFER,
            GL.GL_DEPTH_STENCIL_ATTACHMENT,
            GL.GL_RENDERBUFFER,
            self.fbo_depth_buffer,
        )
        GL.glBindFramebuffer(GL.GL_DRAW_FRAMEBUFFER, 0)

    def frame(self):
        glfw.poll_events()
        self.poll_xr_events()
        glfw.swap_buffers(self.window)

    def poll_xr_events(self):
        while True:
            try:
                event_buffer = xr.poll_event(self.instance)
            except xr.EventUnavailable as exc:
                break


    def destroy(self):
        if self.fbo_id is not None:
            GL.glDeleteFramebuffers(1, [self.fbo_id])
            self.fbo_id = None
        if self.fbo_depth_buffer is not None:
            GL.glDeleteRenderbuffers(1, [self.fbo_depth_buffer])
            self.fbo_depth_buffer = None
        if self.swapchain is not None:
            xr.destroy_swapchain(self.swapchain)
            self.swapchain = None
        if self.session is not None:
            xr.destroy_session(self.session)
            self.session = None
        if self.window is not None:
            glfw.terminate()  # TODO: raii
            self.window = None
        self.system_id = None
        if self.instance is not None:
            xr.destroy_instance(self.instance)
            self.instance = None


if __name__ == "__main__":
    GlExample().run()
