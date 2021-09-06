import ctypes
import logging

import glfw
import platform
from OpenGL import GL
if platform.system() == "Windows":
    from OpenGL import WGL
elif platform.system() == "Linux":
    from OpenGL import GLX

import xr


ALL_SEVERITIES = (
    xr.DEBUG_UTILS_MESSAGE_SEVERITY_VERBOSE_BIT_EXT
    | xr.DEBUG_UTILS_MESSAGE_SEVERITY_INFO_BIT_EXT
    | xr.DEBUG_UTILS_MESSAGE_SEVERITY_WARNING_BIT_EXT
    | xr.DEBUG_UTILS_MESSAGE_SEVERITY_ERROR_BIT_EXT
)

ALL_TYPES = (
    xr.DEBUG_UTILS_MESSAGE_TYPE_GENERAL_BIT_EXT
    | xr.DEBUG_UTILS_MESSAGE_TYPE_VALIDATION_BIT_EXT
    | xr.DEBUG_UTILS_MESSAGE_TYPE_PERFORMANCE_BIT_EXT
    | xr.DEBUG_UTILS_MESSAGE_TYPE_CONFORMANCE_BIT_EXT
)


def py_log_level(severity_flags: int):
    if severity_flags & 0x0001:  # VERBOSE
        return logging.DEBUG
    if severity_flags & 0x0010:  # INFO
        return logging.INFO
    if severity_flags & 0x0100:  # WARNING
        return logging.WARNING
    if severity_flags & 0x1000:  # ERROR
        return logging.ERROR
    return logging.CRITICAL


stringForFormat = {
    GL.GL_COMPRESSED_R11_EAC: "COMPRESSED_R11_EAC",
    GL.GL_COMPRESSED_RED_RGTC1: "COMPRESSED_RED_RGTC1",
    GL.GL_COMPRESSED_RG_RGTC2: "COMPRESSED_RG_RGTC2",
    GL.GL_COMPRESSED_RG11_EAC: "COMPRESSED_RG11_EAC",
    GL.GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT: "COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT",
    GL.GL_COMPRESSED_RGB8_ETC2: "COMPRESSED_RGB8_ETC2",
    GL.GL_COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2: "COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2",
    GL.GL_COMPRESSED_RGBA8_ETC2_EAC: "COMPRESSED_RGBA8_ETC2_EAC",
    GL.GL_COMPRESSED_SIGNED_R11_EAC: "COMPRESSED_SIGNED_R11_EAC",
    GL.GL_COMPRESSED_SIGNED_RG11_EAC: "COMPRESSED_SIGNED_RG11_EAC",
    GL.GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM: "COMPRESSED_SRGB_ALPHA_BPTC_UNORM",
    GL.GL_COMPRESSED_SRGB8_ALPHA8_ETC2_EAC: "COMPRESSED_SRGB8_ALPHA8_ETC2_EAC",
    GL.GL_COMPRESSED_SRGB8_ETC2: "COMPRESSED_SRGB8_ETC2",
    GL.GL_COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2: "COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2",
    GL.GL_DEPTH_COMPONENT16: "DEPTH_COMPONENT16",
    GL.GL_DEPTH_COMPONENT24: "DEPTH_COMPONENT24",
    GL.GL_DEPTH_COMPONENT32: "DEPTH_COMPONENT32",
    GL.GL_DEPTH_COMPONENT32F: "DEPTH_COMPONENT32F",
    GL.GL_DEPTH24_STENCIL8: "DEPTH24_STENCIL8",
    GL.GL_R11F_G11F_B10F: "R11F_G11F_B10F",
    GL.GL_R16_SNORM: "R16_SNORM",
    GL.GL_R16: "R16",
    GL.GL_R16F: "R16F",
    GL.GL_R16I: "R16I",
    GL.GL_R16UI: "R16UI",
    GL.GL_R32F: "R32F",
    GL.GL_R32I: "R32I",
    GL.GL_R32UI: "R32UI",
    GL.GL_R8_SNORM: "R8_SNORM",
    GL.GL_R8: "R8",
    GL.GL_R8I: "R8I",
    GL.GL_R8UI: "R8UI",
    GL.GL_RG16_SNORM: "RG16_SNORM",
    GL.GL_RG16: "RG16",
    GL.GL_RG16F: "RG16F",
    GL.GL_RG16I: "RG16I",
    GL.GL_RG16UI: "RG16UI",
    GL.GL_RG32F: "RG32F",
    GL.GL_RG32I: "RG32I",
    GL.GL_RG32UI: "RG32UI",
    GL.GL_RG8_SNORM: "RG8_SNORM",
    GL.GL_RG8: "RG8",
    GL.GL_RG8I: "RG8I",
    GL.GL_RG8UI: "RG8UI",
    GL.GL_RGB10_A2: "RGB10_A2",
    GL.GL_RGB8: "RGB8",
    GL.GL_RGB9_E5: "RGB9_E5",
    GL.GL_RGBA16_SNORM: "RGBA16_SNORM",
    GL.GL_RGBA16: "RGBA16",
    GL.GL_RGBA16F: "RGBA16F",
    GL.GL_RGBA16I: "RGBA16I",
    GL.GL_RGBA16UI: "RGBA16UI",
    GL.GL_RGBA2: "RGBA2",
    GL.GL_RGBA32F: "RGBA32F",
    GL.GL_RGBA32I: "RGBA32I",
    GL.GL_RGBA32UI: "RGBA32UI",
    GL.GL_RGBA8_SNORM: "RGBA8_SNORM",
    GL.GL_RGBA8: "RGBA8",
    GL.GL_RGBA8I: "RGBA8I",
    GL.GL_RGBA8UI: "RGBA8UI",
    GL.GL_SRGB8_ALPHA8: "SRGB8_ALPHA8",
    GL.GL_SRGB8: "SRGB8",
    GL.GL_RGB16F: "RGB16F",
    GL.GL_DEPTH32F_STENCIL8: "DEPTH32F_STENCIL8",
    GL.GL_BGR: "BGR (Out of spec)",
    GL.GL_BGRA: "BGRA (Out of spec)",
}


class OpenXrExample(object):
    def __init__(self, log_level=logging.WARNING):
        logging.basicConfig()
        self.logger = logging.getLogger("gl_example")
        self.logger.setLevel(log_level)
        self.debug_callback = xr.PFN_xrDebugUtilsMessengerCallbackEXT(self.debug_callback_py)
        self.mirror_window = False
        self.instance = None
        self.system_id = None
        self.pxrCreateDebugUtilsMessengerEXT = None
        self.pxrDestroyDebugUtilsMessengerEXT = None
        self.pxrGetOpenGLGraphicsRequirementsKHR = None
        self.graphics_requirements = xr.GraphicsRequirementsOpenGLKHR()
        if platform.system() == 'Windows':
            self.graphics_binding = xr.GraphicsBindingOpenGLWin32KHR()
        elif platform.system() == 'Linux':
            self.graphics_binding = xr.GraphicsBindingOpenGLXlibKHR()
        else:
            raise NotImplementedError('Unsupported platform')
        self.render_target_size = None
        self.window = None
        self.session = None
        self.projection_layer_views = (xr.CompositionLayerProjectionView * 2)(
            *([xr.CompositionLayerProjectionView()] * 2))
        self.projection_layer = xr.CompositionLayerProjection(0, None, 2, self.projection_layer_views)
        self.swapchain_create_info = xr.SwapchainCreateInfo()
        self.swapchain = None
        self.swapchain_images = None
        self.fbo_id = None
        self.fbo_depth_buffer = None
        self.quit = False
        self.session_state = xr.SessionState.IDLE
        self.frame_state = xr.FrameState()
        self.eye_view_states = None
        self.window_size = None
        self.enable_debug = True

    def debug_callback_py(
            self,
            severity: xr.DebugUtilsMessageSeverityFlagsEXT,
            _type: xr.DebugUtilsMessageTypeFlagsEXT,
            data: ctypes.POINTER(xr.DebugUtilsMessengerCallbackDataEXT),
            _user_data: ctypes.c_void_p,
    ) -> bool:
        d = data.contents
        # TODO structure properties to return unicode strings
        self.logger.log(py_log_level(severity), f"{d.function_name.decode()}: {d.message.decode()}")
        return True

    def run(self):
        while not self.quit:
            if glfw.window_should_close(self.window):
                self.quit = True
            else:
                self.frame()

    def __enter__(self):
        self.prepare_xr_instance()
        self.prepare_xr_system()
        self.prepare_window()
        self.prepare_xr_session()
        self.prepare_xr_swapchain()
        self.prepare_xr_composition_layers()
        self.prepare_gl_framebuffer()
        return self

    def prepare_xr_instance(self):
        discovered_extensions = xr.enumerate_instance_extension_properties()
        if xr.EXT_DEBUG_UTILS_EXTENSION_NAME not in discovered_extensions:
            self.enable_debug = False
        requested_extensions = [xr.KHR_OPENGL_ENABLE_EXTENSION_NAME]
        if self.enable_debug:
            requested_extensions.append(xr.EXT_DEBUG_UTILS_EXTENSION_NAME)
        for extension in requested_extensions:
            assert extension in discovered_extensions
        app_info = xr.ApplicationInfo("gl_example", 0, "pyopenxr", 0, xr.XR_CURRENT_API_VERSION)
        # TODO: buffer
        bs = [s.encode() for s in requested_extensions]
        arr_type = ctypes.c_char_p * len(bs)
        str_arr = arr_type()
        for i, s in enumerate(bs):
            str_arr[i] = s
        ici = xr.InstanceCreateInfo(0, app_info, 0, None, 1, str_arr)
        dumci = xr.DebugUtilsMessengerCreateInfoEXT()
        if self.enable_debug:
            dumci.message_severities = ALL_SEVERITIES
            dumci.message_types = ALL_TYPES
            dumci.user_data = None  # TODO
            dumci.user_callback = self.debug_callback
            ici.next = ctypes.cast(ctypes.pointer(dumci), ctypes.c_void_p)  # TODO: yuck
        self.instance = xr.create_instance(ici)
        # TODO: pythonic wrapper
        self.pxrGetOpenGLGraphicsRequirementsKHR = ctypes.cast(
            xr.get_instance_proc_addr(
                self.instance,
                "xrGetOpenGLGraphicsRequirementsKHR",
            ),
            xr.PFN_xrGetOpenGLGraphicsRequirementsKHR
        )

    def prepare_xr_system(self):
        get_info = xr.SystemGetInfo(xr.FormFactor.HEAD_MOUNTED_DISPLAY)
        self.system_id = xr.get_system(self.instance, get_info)  # TODO: not a pointer
        view_configs = xr.enumerate_view_configurations(self.instance, self.system_id)
        assert view_configs[0] == xr.ViewConfigurationType.PRIMARY_STEREO.value  # TODO: equality...
        view_config_views = xr.enumerate_view_configuration_views(
            self.instance, self.system_id, xr.ViewConfigurationType.PRIMARY_STEREO)
        assert len(view_config_views) == 2
        assert view_config_views[0].recommended_image_rect_height == view_config_views[1].recommended_image_rect_height
        self.render_target_size = (
            view_config_views[0].recommended_image_rect_width * 2,
            view_config_views[0].recommended_image_rect_height)
        result = self.pxrGetOpenGLGraphicsRequirementsKHR(
            self.instance, self.system_id, ctypes.byref(self.graphics_requirements))  # TODO: pythonic wrapper
        result = xr.exception.check_result(xr.Result(result))
        if result.is_exception():
            raise result

    def prepare_window(self):
        if not glfw.init():
            raise RuntimeError("GLFW initialization failed")
        if not self.mirror_window:
            glfw.window_hint(glfw.VISIBLE, False)
        glfw.window_hint(glfw.DOUBLEBUFFER, False)
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 5)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        self.window_size = [s // 4 for s in self.render_target_size]
        self.window = glfw.create_window(*self.window_size, "gl_example", None, None)
        if self.window is None:
            raise RuntimeError("Failed to create GLFW window")
        glfw.make_context_current(self.window)
        # Attempt to disable vsync on the desktop window or
        # it will interfere with the OpenXR frame loop timing
        glfw.swap_interval(0)

    def prepare_xr_session(self):
        if platform.system() == 'Windows':
            self.graphics_binding.h_dc = WGL.wglGetCurrentDC()
            self.graphics_binding.h_glrc = WGL.wglGetCurrentContext()
        else:
            self.graphics_binding.x_display = GLX.glXGetCurrentDisplay()
            self.graphics_binding.glx_context = GLX.glXGetCurrentContext()
            self.graphics_binding.glx_drawable = GLX.glXGetCurrentDrawable()
        pp = ctypes.cast(ctypes.pointer(self.graphics_binding), ctypes.c_void_p)
        sci = xr.SessionCreateInfo(0, self.system_id, next_structure=pp)
        self.session = xr.create_session(self.instance, sci)
        reference_spaces = xr.enumerate_reference_spaces(self.session)
        for rs in reference_spaces:
            self.logger.debug(f"Session supports reference space {xr.ReferenceSpaceType(rs)}")
        # TODO: default constructors for Quaternion, Vector3f, Posef, ReferenceSpaceCreateInfo
        rsci = xr.ReferenceSpaceCreateInfo(
            xr.ReferenceSpaceType.STAGE,
            xr.Posef(xr.Quaternionf(0, 0, 0, 1), xr.Vector3f(0, 0, 0))
        )
        self.projection_layer.space = xr.create_reference_space(self.session, rsci)
        swapchain_formats = xr.enumerate_swapchain_formats(self.session)
        for scf in swapchain_formats:
            self.logger.debug(f"Session supports swapchain format {stringForFormat[scf]}")

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
        self.swapchain_images = xr.enumerate_swapchain_images(self.swapchain, xr.SwapchainImageOpenGLKHR)
        for i, si in enumerate(self.swapchain_images):
            self.logger.debug(f"Swapchain image {i} type = {xr.StructureType(si.type)}")

    def prepare_xr_composition_layers(self):
        self.projection_layer.view_count = 2
        self.projection_layer.views = self.projection_layer_views
        for eye_index in range(2):
            layer_view = self.projection_layer_views[eye_index]
            layer_view.sub_image.swapchain = self.swapchain
            layer_view.sub_image.image_rect.extent = xr.Extent2Di(
                self.render_target_size[0] // 2,
                self.render_target_size[1],
            )
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
        if self.quit:
            return
        if self.start_xr_frame():
            self.update_xr_views()
            if self.frame_state.should_render:
                self.render()
            self.end_xr_frame()

    def poll_xr_events(self):
        while True:
            try:
                event_buffer = xr.poll_event(self.instance)
                event_type = xr.StructureType(event_buffer.type)
                if event_type == xr.StructureType.EVENT_DATA_SESSION_STATE_CHANGED:
                    self.on_session_state_changed(event_buffer)
            except xr.EventUnavailable:
                break

    def on_session_state_changed(self, session_state_changed_event):
        # TODO: it would be nice to avoid this horrible cast...
        event = ctypes.cast(
            ctypes.byref(session_state_changed_event),
            ctypes.POINTER(xr.EventDataSessionStateChanged)).contents
        # TODO: enum property
        self.session_state = xr.SessionState(event.state)
        if self.session_state == xr.SessionState.READY:
            if not self.quit:
                sbi = xr.SessionBeginInfo(xr.ViewConfigurationType.PRIMARY_STEREO)
                xr.begin_session(self.session, sbi)
        elif self.session_state == xr.SessionState.STOPPING:
            xr.end_session(self.session)
            self.session = None
            self.quit = True

    def start_xr_frame(self) -> bool:
        if self.session_state in [
            xr.SessionState.READY,
            xr.SessionState.FOCUSED,
            xr.SessionState.SYNCHRONIZED,
            xr.SessionState.VISIBLE,
        ]:
            frame_wait_info = xr.FrameWaitInfo(None)
            try:
                self.frame_state = xr.wait_frame(self.session, frame_wait_info)
                xr.begin_frame(self.session, None)
                return True
            except xr.ResultException:
                return False
        return False

    def end_xr_frame(self):
        frame_end_info = xr.FrameEndInfo(
            self.frame_state.predicted_display_time,
            xr.EnvironmentBlendMode.OPAQUE
        )
        if self.frame_state.should_render:
            for eye_index in range(2):
                layer_view = self.projection_layer_views[eye_index]
                eye_view = self.eye_view_states[eye_index]
                layer_view.fov = eye_view.fov
                layer_view.pose = eye_view.pose
            frame_end_info.layer_count = 1  # len(self.layer_pointers)
            p_layer_projection = ctypes.cast(
                ctypes.byref(self.projection_layer),
                ctypes.POINTER(xr.CompositionLayerBaseHeader))
            frame_end_info.layers = ctypes.pointer(p_layer_projection)
        xr.end_frame(self.session, frame_end_info)

    def update_xr_views(self):
        vi = xr.ViewLocateInfo(
            xr.ViewConfigurationType.PRIMARY_STEREO,
            self.frame_state.predicted_display_time,
            self.projection_layer.space,
        )
        vs, self.eye_view_states = xr.locate_views(self.session, vi)
        for eye_index, view_state in enumerate(self.eye_view_states):
            # These aren't actually used in this simple example...
            # self.eye_projections[eye_index] = something(view_state.fov)  # TODO:
            # print(view_state.pose)
            pass

    def render(self):
        ai = xr.SwapchainImageAcquireInfo(None)
        swapchain_index = xr.acquire_swapchain_image(self.swapchain, ai)
        wi = xr.SwapchainImageWaitInfo(xr.INFINITE_DURATION)
        xr.wait_swapchain_image(self.swapchain, wi)
        GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, self.fbo_id)
        sw_image = self.swapchain_images[swapchain_index]
        GL.glFramebufferTexture(
            GL.GL_FRAMEBUFFER,
            GL.GL_COLOR_ATTACHMENT0,
            sw_image.image,
            0,
        )
        # "render" to the swapchain image
        w, h = self.render_target_size
        GL.glEnable(GL.GL_SCISSOR_TEST)
        GL.glScissor(0, 0, w // 2, h)
        GL.glClearColor(0, 1, 0, 1)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glScissor(w // 2, 0, w // 2, h)
        GL.glClearColor(0, 0, 1, 1)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

        if self.mirror_window:
            # fast blit from the fbo to the window surface
            GL.glDisable(GL.GL_SCISSOR_TEST)
            GL.glBindFramebuffer(GL.GL_DRAW_FRAMEBUFFER, 0)
            GL.glBlitFramebuffer(
                0, 0, w, h, 0, 0,
                *self.window_size,
                GL.GL_COLOR_BUFFER_BIT,
                GL.GL_NEAREST
            )
            GL.glFramebufferTexture(GL.GL_READ_FRAMEBUFFER, GL.GL_COLOR_ATTACHMENT0, 0, 0)
            GL.glBindFramebuffer(GL.GL_READ_FRAMEBUFFER, 0)
        ri = xr.SwapchainImageReleaseInfo()
        xr.release_swapchain_image(self.swapchain, ri)
        # If we're mirror make sure to do the potentially blocking command
        # AFTER we've released the swapchain image
        if self.mirror_window:
            glfw.swap_buffers(self.window)

    def __exit__(self, exc_type, exc_value, traceback):
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
        glfw.terminate()


if __name__ == "__main__":
    with OpenXrExample(logging.DEBUG) as ex:
        ex.run()
