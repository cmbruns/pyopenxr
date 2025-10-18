"""
File pink_world_one_file.py

This example uses only core functions.
It is mostly only one long procedure.
The only abstraction is the SessionStateEventHandler class,
which avoids some code duplication between the core loop
and the cleanup code.
"""

import time
from contextlib import ExitStack
from ctypes import byref, cast, POINTER
import sys

if sys.platform in ["win32", "linux"]:
    from OpenGL import GL
    import glfw
    if sys.platform == "win32":
        from OpenGL import WGL
    else:
        from OpenGL import GLX
else:
    import android
    from OpenGL import GLES3 as GL
    from OpenGL import EGL

import xr


def main():
    extensions = set()
    if sys.platform in ["win32", "linux"]:
        extensions.add(xr.KHR_OPENGL_ENABLE_EXTENSION_NAME)
    else:
        assert sys.platform == "android"
        extensions.add(xr.KHR_OPENGL_ES_ENABLE_EXTENSION_NAME)
    # Initialize OpenXR loader (android only)
    instance_create_extension = None
    if sys.platform == "android":
        xr.initialize_loader_khr(xr.LoaderInitInfoAndroidKHR(
            application_vm=android.get_vm(),
            application_context=android.get_activity(),
        ))
        extensions.add(xr.KHR_ANDROID_CREATE_INSTANCE_EXTENSION_NAME)
        extensions.add(xr.FB_PASSTHROUGH_EXTENSION_NAME)
        extensions.add(xr.FB_TRIANGLE_MESH_EXTENSION_NAME)
        instance_create_extension = xr.InstanceCreateInfoAndroidKHR(
            application_vm=android.get_vm(),
            application_activity=android.get_activity(),
        )
    with ExitStack() as exit_stack:  # noqa
        # Create OpenXR instance
        instance = exit_stack.enter_context(xr.create_instance(
            create_info=xr.InstanceCreateInfo(
                next=instance_create_extension,
                enabled_extension_names=list(extensions))))
        # Create system
        system_id = xr.get_system(instance, xr.SystemGetInfo(
            form_factor=xr.FormFactor.HEAD_MOUNTED_DISPLAY))
        # Create OpenGL context
        if sys.platform in ["win32", "linux"]:
            import glfw
            if not glfw.init():
                raise RuntimeError("Failed to initialize GLFW")
            # hidden, single‐buffered context
            glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
            glfw.window_hint(glfw.DOUBLEBUFFER, glfw.FALSE)
            glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
            glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 6)
            glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
            # tiny 1×1 window just to get a context
            window = glfw.create_window(1, 1, "", None, None)
            if window is None:
                glfw.terminate()
                raise RuntimeError("Failed to create hidden GLFW window")
            glfw.make_context_current(window)
            graphics_requirements = xr.get_opengl_graphics_requirements_khr(
                instance=instance,
                system_id=system_id)
            if sys.platform == "win32":
                graphics_binding = xr.GraphicsBindingOpenGLWin32KHR(
                    h_dc=WGL.wglGetCurrentDC(),
                    h_glrc=WGL.wglGetCurrentContext(),
                )
            else:
                graphics_binding = xr.GraphicsBindingOpenGLXlibKHR(
                    x_display=GLX.glXGetCurrentDisplay(),
                    glx_context=GLX.glXGetCurrentContext(),
                    glx_drawable=GLX.glXGetCurrentDrawable(),
                )
        else:
            assert sys.platform == "android"
            display = EGL.eglGetDisplay(EGL.EGL_DEFAULT_DISPLAY)
            assert display != EGL.EGL_NO_DISPLAY
            major, minor = EGL.EGLint(), EGL.EGLint()
            assert EGL.eglInitialize(display, major, minor)
            config_attributes = [
                EGL.EGL_RENDERABLE_TYPE, EGL.EGL_OPENGL_ES3_BIT,
                EGL.EGL_SURFACE_TYPE, EGL.EGL_PBUFFER_BIT,
                EGL.EGL_RED_SIZE, 8, EGL.EGL_GREEN_SIZE, 8, EGL.EGL_BLUE_SIZE, 8,
                EGL.EGL_ALPHA_SIZE, 8, EGL.EGL_DEPTH_SIZE, 24,
                EGL.EGL_NONE]
            num_configs = EGL.EGLint()
            configs = (EGL.EGLConfig * 1)()
            assert EGL.eglChooseConfig(display, config_attributes, configs, 1, num_configs)
            assert num_configs.value > 0
            config = configs[0]
            pbuffer_attributes = [
                EGL.EGL_WIDTH, 1,
                EGL.EGL_HEIGHT, 1,
                EGL.EGL_NONE]
            surface = EGL.eglCreatePbufferSurface(display, config, pbuffer_attributes)
            assert surface != EGL.EGL_NO_SURFACE
            context_attributes = [
                EGL.EGL_CONTEXT_MAJOR_VERSION, 3,
                EGL.EGL_CONTEXT_MINOR_VERSION, 2,
                EGL.EGL_NONE
            ]
            context = EGL.eglCreateContext(display, config, EGL.EGL_NO_CONTEXT, context_attributes)
            assert context != EGL.EGL_NO_CONTEXT
            assert EGL.eglMakeCurrent(display, surface, surface, context)
            graphics_requirements = xr.get_opengl_es_graphics_requirements_khr(
                instance=instance,
                system_id=system_id)
            # Graphics binding
            graphics_binding = xr.GraphicsBindingOpenGLESAndroidKHR(
                display=display,
                context=context,
                config=config,
            )
        print(f"Graphics requirements  min: {graphics_requirements.min_api_version_supported}, "
              f"max: {graphics_requirements.max_api_version_supported}")
        # create OpenXR session
        session = exit_stack.enter_context(xr.create_session(
            instance,
            xr.SessionCreateInfo(
                system_id=system_id,
                next=graphics_binding,
            ),
        ))
        # blend mode
        blend_mode = None
        blend_modes = list(xr.enumerate_environment_blend_modes(
            instance, system_id, xr.ViewConfigurationType.PRIMARY_STEREO))
        for b in [xr.EnvironmentBlendMode.ALPHA_BLEND, xr.EnvironmentBlendMode.OPAQUE]:
            if b in blend_modes:
                blend_mode = blend_mode
                break
        if blend_mode is None:
            blend_mode = blend_modes[0]
        print(f"blend mode = {xr.EnvironmentBlendMode(blend_mode).name}")  # TODO box/unbox enum fields
        # reference space
        space = exit_stack.enter_context(xr.create_reference_space(
            session,
            xr.ReferenceSpaceCreateInfo(xr.ReferenceSpaceType.STAGE)
        ))
        # action set
        action_set = exit_stack.enter_context(xr.create_action_set(
            instance=instance,
            create_info=xr.ActionSetCreateInfo(
                action_set_name="action_set",
                localized_action_set_name="Action Set",
                priority=0,
            ),
        ))
        # swapchain format
        color_swapchain_format = None
        swapchain_formats = xr.enumerate_swapchain_formats(session)
        for sf in [GL.GL_RGBA8, GL.GL_RGBA8_SNORM, GL.GL_SRGB8_ALPHA8]:
            if sf in swapchain_formats:
                color_swapchain_format = sf
                break
        assert color_swapchain_format is not None
        # views (usually two: one for the left eye; one for the right)
        view_configuration_type = xr.ViewConfigurationType.PRIMARY_STEREO
        config_views = xr.enumerate_view_configuration_views(
            instance=instance,
            system_id=system_id,
            view_configuration_type=view_configuration_type,
        )
        assert len(config_views) > 0
        # create a swapchain for each view
        swapchains = []
        swapchain_images = []
        swapchain_sizes = []
        swapchain_image_ptr_buffers = []
        for v in config_views:
            swapchains.append(xr.create_swapchain(session, xr.SwapchainCreateInfo(
                array_size=1,
                format=color_swapchain_format,
                width=v.recommended_image_rect_width,
                height=v.recommended_image_rect_height,
                mip_count=1,
                face_count=1,
                sample_count=1,
                usage_flags=xr.SwapchainUsageFlags.SAMPLED_BIT | xr.SwapchainUsageFlags.COLOR_ATTACHMENT_BIT,
            )))
            swapchain_images.append(xr.enumerate_swapchain_images(
                swapchain=swapchains[-1], element_type=xr.SwapchainImageOpenGLESKHR))
            swapchain_sizes.append((v.recommended_image_rect_width, v.recommended_image_rect_height))
            num_images = len(swapchain_images[-1])
            swapchain_image_ptr_buffer = (POINTER(xr.SwapchainImageBaseHeader) * num_images)()
            for ix in range(num_images):
                swapchain_image_ptr_buffer[ix] = cast(
                    byref(swapchain_images[-1][ix]),
                    POINTER(xr.SwapchainImageBaseHeader))
            swapchain_image_ptr_buffers.append(swapchain_image_ptr_buffer)
        # framebuffer
        swapchain_framebuffer = GL.glGenFramebuffers(1)
        GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, swapchain_framebuffer)
        color_to_depth_map = dict()
        # action sets
        xr.attach_session_action_sets(session, attach_info=xr.SessionActionSetsAttachInfo(
            action_sets=[action_set, ],
        ))
        # begin frame/render loop
        event_handler = SessionStateEventHandler(session, view_configuration_type)
        for _ in range(500):
            # TODO: poll android events
            # Poll session state events
            while True:
                try:
                    event_buffer = xr.poll_event(instance)
                    event_handler.handle_event(event_buffer)
                except xr.EventUnavailable:
                    break
            if event_handler.exit_render_loop:
                break
            if (event_handler.session_is_running and
                    event_handler.session_state in (
                            xr.SessionState.READY,
                            xr.SessionState.SYNCHRONIZED,
                            xr.SessionState.VISIBLE,
                            xr.SessionState.FOCUSED,
                    )):
                frame_state = xr.wait_frame(session)
                xr.begin_frame(session)
                layers = []
                if frame_state.should_render:
                    assert GL.glGetError() == GL.GL_NO_ERROR
                    layer = xr.CompositionLayerProjection(space=space)
                    view_state, views = xr.locate_views(session, xr.ViewLocateInfo(
                        view_configuration_type=view_configuration_type,
                        display_time=frame_state.predicted_display_time,
                        space=space,
                    ))
                    projection_layer_views = tuple(xr.CompositionLayerProjectionView() for _ in range(len(views)))
                    vsf = view_state.view_state_flags
                    poses_are_valid = (vsf & xr.VIEW_STATE_POSITION_VALID_BIT) and (vsf & xr.VIEW_STATE_ORIENTATION_VALID_BIT)
                    assert GL.glGetError() == GL.GL_NO_ERROR
                    if poses_are_valid:
                        for view_index, view in enumerate(views):
                            assert GL.glGetError() == GL.GL_NO_ERROR
                            swapchain = swapchains[view_index]
                            swapchain_image_index = xr.acquire_swapchain_image(
                                swapchain=swapchain,
                                acquire_info=xr.SwapchainImageAcquireInfo(),
                            )
                            xr.wait_swapchain_image(
                                swapchain=swapchain,
                                wait_info=xr.SwapchainImageWaitInfo(timeout=xr.INFINITE_DURATION),
                            )
                            layer_view = projection_layer_views[view_index]
                            assert layer_view.type == xr.StructureType.COMPOSITION_LAYER_PROJECTION_VIEW
                            layer_view.pose = view.pose
                            layer_view.fov = view.fov
                            layer_view.sub_image.swapchain = swapchain
                            layer_view.sub_image.image_rect.offset[:] = [0, 0]
                            layer_view.sub_image.image_rect.extent[:] = [*swapchain_sizes[view_index]]
                            swapchain_image_ptr = swapchain_image_ptr_buffers[view_index][swapchain_image_index]
                            swapchain_image = cast(swapchain_image_ptr, POINTER(xr.SwapchainImageOpenGLESKHR)).contents
                            assert layer_view.sub_image.image_array_index == 0  # texture arrays not supported.
                            color_texture = swapchain_image.image
                            # graphics begin frame
                            GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, swapchain_framebuffer)
                            GL.glViewport(layer_view.sub_image.image_rect.offset.x,
                                          layer_view.sub_image.image_rect.offset.y,
                                          layer_view.sub_image.image_rect.extent.width,
                                          layer_view.sub_image.image_rect.extent.height)
                            if color_texture in color_to_depth_map:
                                depth_texture = color_to_depth_map[color_texture]
                            else:
                                GL.glBindTexture(GL.GL_TEXTURE_2D, color_texture)
                                width = GL.glGetTexLevelParameteriv(GL.GL_TEXTURE_2D, 0, GL.GL_TEXTURE_WIDTH)
                                height = GL.glGetTexLevelParameteriv(GL.GL_TEXTURE_2D, 0, GL.GL_TEXTURE_HEIGHT)
                                depth_texture = GL.glGenTextures(1)
                                GL.glBindTexture(GL.GL_TEXTURE_2D, depth_texture)
                                GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_NEAREST)
                                GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_NEAREST)
                                GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_CLAMP_TO_EDGE)
                                GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_CLAMP_TO_EDGE)
                                if sys.platform == "android":  # or OpenGLES really
                                    depth_component = GL.GL_DEPTH_COMPONENT24
                                else:
                                    depth_component = GL.GL_DEPTH_COMPONENT32
                                GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, depth_component, width, height, 0,
                                                GL.GL_DEPTH_COMPONENT, GL.GL_UNSIGNED_INT, None)
                                color_to_depth_map[color_texture] = depth_texture
                            GL.glFramebufferTexture2D(GL.GL_FRAMEBUFFER, GL.GL_COLOR_ATTACHMENT0, GL.GL_TEXTURE_2D,
                                                      color_texture, 0)
                            GL.glFramebufferTexture2D(GL.GL_FRAMEBUFFER, GL.GL_DEPTH_ATTACHMENT, GL.GL_TEXTURE_2D,
                                                      depth_texture, 0)

                            # render - paint the entire universe a pale pink color
                            GL.glClearColor(1, 0.7, 0.7, 1)  # pink
                            GL.glClear(GL.GL_COLOR_BUFFER_BIT)

                            # end frame
                            GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, 0)
                            xr.release_swapchain_image(
                                swapchain=swapchain,
                                release_info=xr.SwapchainImageReleaseInfo())
                        layer.views = projection_layer_views
                        layers.append(byref(layer))
                assert GL.glGetError() == GL.GL_NO_ERROR  # Prepare to avoid Linux SteamVR bug
                xr.end_frame(session, xr.FrameEndInfo(
                    display_time=frame_state.predicted_display_time,
                    environment_blend_mode=blend_mode,
                    layers=layers,
                ))
                GL.glGetError()  # Clear GL error state to avoid Linux SteamVR bug
            else:
                # throttle loop since xr.wait_frame() won't be called
                time.sleep(0.250)
        # end of frame loop
        # wind down session state
        try:
            xr.request_exit_session(session)
        except xr.SessionNotRunningError:
            pass
        for _ in range(20):
            while True:
                try:
                    event_buffer = xr.poll_event(instance)
                    event_handler.handle_event(event_buffer)
                except xr.EventUnavailable:
                    break
            if event_handler.exit_render_loop:
                break
            if (event_handler.session_is_running and
                    event_handler.session_state in (
                            xr.SessionState.READY,
                            xr.SessionState.SYNCHRONIZED,
                            xr.SessionState.VISIBLE,
                            xr.SessionState.FOCUSED,
                    )):
                frame_state = xr.wait_frame(session)
                xr.begin_frame(session)
                time.sleep(0.050)  # Yield time for other subsystems
                xr.end_frame(
                    session,
                    frame_end_info=xr.FrameEndInfo(
                        display_time=frame_state.predicted_display_time,
                        environment_blend_mode=blend_mode,
                        layers=[],
                    )
                )
        # TODO: destroy objects not destroyed by exit_stack...


class SessionStateEventHandler:
    def __init__(self, session, view_configuration_type: xr.ViewConfigurationType):
        self.session = session
        self.view_configuration_type = view_configuration_type
        self.exit_render_loop = False
        self.request_restart = False
        self.session_state = xr.SessionState.IDLE
        self.session_is_running = False

    def handle_event(self, event_buffer: xr.EventDataBuffer):
        event_type = xr.StructureType(event_buffer.type)
        if event_type == xr.StructureType.EVENT_DATA_INSTANCE_LOSS_PENDING:
            self.exit_render_loop = True
            self.request_restart = True
        elif event_type == xr.StructureType.EVENT_DATA_SESSION_STATE_CHANGED:
            event = cast(
                byref(event_buffer),
                POINTER(xr.EventDataSessionStateChanged)
            ).contents
            self.session_state = xr.SessionState(event.state)
            print(f"OpenXR session state changed to {self.session_state.name}")
            if self.session_state == xr.SessionState.READY:
                xr.begin_session(
                    session=self.session,
                    begin_info=xr.SessionBeginInfo(self.view_configuration_type)
                )
                self.session_is_running = True
            elif self.session_state == xr.SessionState.STOPPING:
                self.session_is_running = False
                xr.end_session(self.session)
            elif self.session_state in (xr.SessionState.EXITING, xr.SessionState.LOSS_PENDING):
                self.exit_render_loop = True
                self.request_restart = (self.session_state == xr.SessionState.LOSS_PENDING)


if __name__ == "__main__":
    main()
