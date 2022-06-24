import time
from ctypes import byref, c_int32, c_void_p, cast, POINTER, pointer, Structure

import xr
from .enums import *
from .exception import *
from .typedefs import *
from .functions import *
from .opengl_graphics import OpenGLGraphics


class SwapchainStruct(Structure):
    _fields_ = [
        ("handle", Swapchain),
        ("width", c_int32),
        ("height", c_int32),
    ]


class ContextObject(object):
    def __init__(
            self,
            instance_create_info: InstanceCreateInfo = InstanceCreateInfo(),
            session_create_info: SessionCreateInfo = SessionCreateInfo(),
            reference_space_create_info: ReferenceSpaceCreateInfo = ReferenceSpaceCreateInfo(),
            view_configuration_type: ViewConfigurationType = ViewConfigurationType.PRIMARY_STEREO,
            environment_blend_mode=EnvironmentBlendMode.OPAQUE,
            form_factor=FormFactor.HEAD_MOUNTED_DISPLAY,
    ):
        self._instance_create_info = instance_create_info
        self.instance = None
        self._session_create_info = session_create_info
        self.session = None
        self.session_state = SessionState.IDLE
        self._reference_space_create_info = reference_space_create_info
        self.view_configuration_type = view_configuration_type
        self.environment_blend_mode = environment_blend_mode
        self.form_factor = form_factor
        self.graphics = None
        self.graphics_binding_pointer = None
        self.action_sets = []
        self.render_layers = []
        self.swapchains = []
        self.swapchain_image_ptr_buffers = []
        self.swapchain_image_buffers = []  # Keep alive
        self.exit_render_loop = False
        self.request_restart = False  # TODO: do like hello_xr
        self.session_is_running = False

    def __enter__(self):
        self.instance = create_instance(
            create_info=self._instance_create_info,
        )
        self.system_id = get_system(
            instance=self.instance,
            get_info=SystemGetInfo(
                form_factor=self.form_factor,
            ),
        )

        if self._session_create_info.next is None:
            self.graphics = OpenGLGraphics(
                instance=self.instance,
                system=self.system_id,
                title=self._instance_create_info.application_info.application_name.decode()
            )
            self.graphics_binding_pointer = cast(pointer(self.graphics.graphics_binding), c_void_p)
            self._session_create_info.next = self.graphics_binding_pointer
        else:
            self.graphics_binding_pointer = self._session_create_info.next

        self._session_create_info.system_id = self.system_id
        self.session = create_session(
            instance=self.instance,
            create_info=self._session_create_info,
        )
        self.space = create_reference_space(
            session=self.session,
            create_info=self._reference_space_create_info
        )
        self.default_action_set = create_action_set(
            instance=self.instance,
            create_info=ActionSetCreateInfo(
                action_set_name="default_action_set",
                localized_action_set_name="Default Action Set",
                priority=0,
            ),
        )
        self.action_sets.append(self.default_action_set)

        # Create swapchains
        config_views = xr.enumerate_view_configuration_views(
            instance=self.instance,
            system_id=self.system_id,
            view_configuration_type=self.view_configuration_type,
        )
        self.graphics.initialize_resources()
        swapchain_formats = xr.enumerate_swapchain_formats(self.session)
        color_swapchain_format = self.graphics.select_color_swapchain_format(swapchain_formats)
        # Create a swapchain for each view.
        self.swapchains.clear()
        self.swapchain_image_buffers.clear()
        self.swapchain_image_ptr_buffers.clear()
        for vp in config_views:
            # Create the swapchain.
            swapchain_create_info = xr.SwapchainCreateInfo(
                array_size=1,
                format=color_swapchain_format,
                width=vp.recommended_image_rect_width,
                height=vp.recommended_image_rect_height,
                mip_count=1,
                face_count=1,
                sample_count=vp.recommended_swapchain_sample_count,
                usage_flags=xr.SwapchainUsageFlags.SAMPLED_BIT | xr.SwapchainUsageFlags.COLOR_ATTACHMENT_BIT,
            )
            swapchain = SwapchainStruct(
                xr.create_swapchain(
                    session=self.session,
                    create_info=swapchain_create_info,
                ),
                swapchain_create_info.width,
                swapchain_create_info.height,
            )
            self.swapchains.append(swapchain)
            swapchain_image_buffer = xr.enumerate_swapchain_images(
                swapchain=swapchain.handle,
                element_type=self.graphics.swapchain_image_type,
            )
            # Keep the buffer alive by moving it into the list of buffers.
            self.swapchain_image_buffers.append(swapchain_image_buffer)
            capacity = len(swapchain_image_buffer)
            swapchain_image_ptr_buffer = (POINTER(xr.SwapchainImageBaseHeader) * capacity)()
            for ix in range(capacity):
                swapchain_image_ptr_buffer[ix] = cast(
                    byref(swapchain_image_buffer[ix]),
                    POINTER(xr.SwapchainImageBaseHeader))
            self.swapchain_image_ptr_buffers.append(swapchain_image_ptr_buffer)
        self.graphics.make_current()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.default_action_set is not None:
            destroy_action_set(self.default_action_set)
            self.default_action_set = None
        if self.space is not None:
            destroy_space(self.space)
            self.space = None
        if self.session is not None:
            destroy_session(self.session)
            self.session = None
        if self.graphics is not None:
            self.graphics.destroy()
            self.graphics = None
        if self.instance is not None:
            destroy_instance(self.instance)
            self.instance = None

    def frame_loop(self):
        attach_session_action_sets(
            session=self.session,
            attach_info=SessionActionSetsAttachInfo(
                count_action_sets=len(self.action_sets),
                action_sets=(ActionSet * len(self.action_sets))(
                    *self.action_sets
                )
            ),
        )
        while True:
            window_closed = self.graphics.poll_events()
            if window_closed:
                self.exit_render_loop = True
                break
            self.exit_render_loop = False
            self.poll_xr_events()
            if self.exit_render_loop:
                break
            if self.session_is_running:
                if self.session_state in (
                        SessionState.READY,
                        SessionState.SYNCHRONIZED,
                        SessionState.VISIBLE,
                        SessionState.FOCUSED,
                ):
                    frame_state = wait_frame(self.session)
                    begin_frame(self.session)
                    self.render_layers = []
                    self.graphics.make_current()

                    yield frame_state

                    end_frame(
                        self.session,
                        frame_end_info=FrameEndInfo(
                            display_time=frame_state.predicted_display_time,
                            environment_blend_mode=self.environment_blend_mode,
                            layers=self.render_layers,
                        )
                    )
            else:
                # Throttle loop since xrWaitFrame won't be called.
                time.sleep(0.250)

    def poll_xr_events(self):
        self.exit_render_loop = False
        self.request_restart = False
        while True:
            try:
                event_buffer = poll_event(self.instance)
                event_type = StructureType(event_buffer.type)
                if event_type == StructureType.EVENT_DATA_INSTANCE_LOSS_PENDING:
                    # still handle rest of the events instead of immediately quitting
                    self.exit_render_loop = True
                    self.request_restart = True
                elif event_type == StructureType.EVENT_DATA_SESSION_STATE_CHANGED \
                        and self.session is not None:
                    event = cast(
                        byref(event_buffer),
                        POINTER(EventDataSessionStateChanged)).contents
                    self.session_state = SessionState(event.state)
                    if self.session_state == SessionState.READY:
                        begin_session(
                            session=self.session,
                            begin_info=SessionBeginInfo(
                                self.view_configuration_type,
                            ),
                        )
                        self.session_is_running = True
                    elif self.session_state == SessionState.STOPPING:
                        self.session_is_running = False
                        xr.end_session(self.session)
                    elif self.session_state == SessionState.EXITING:
                        self.exit_render_loop = True
                        self.request_restart = False
                    elif self.session_state == SessionState.LOSS_PENDING:
                        self.exit_render_loop = True
                        self.request_restart = True
                elif event_type == StructureType.EVENT_DATA_VIVE_TRACKER_CONNECTED_HTCX:
                    vive_tracker_connected = cast(byref(event_buffer), POINTER(EventDataViveTrackerConnectedHTCX)).contents
                    paths = vive_tracker_connected.paths.contents
                    persistent_path_str = xr.path_to_string(self.instance, paths.persistent_path)
                    # print(f"Vive Tracker connected: {persistent_path_str}")
                    if paths.role_path != xr.NULL_PATH:
                        role_path_str = xr.path_to_string(self.instance, paths.role_path)
                        # print(f" New role is: {role_path_str}")
                    else:
                        # print(f" No role path.")
                        pass
                elif event_type == StructureType.EVENT_DATA_INTERACTION_PROFILE_CHANGED:
                    # print("data interaction profile changed")
                    # TODO:
                    pass
            except EventUnavailable:
                break

    def view_loop(self, frame_state):
        if frame_state.should_render:
            layer = xr.CompositionLayerProjection(space=self.space)
            projection_layer_views = (xr.CompositionLayerProjectionView * 2)(
                xr.CompositionLayerProjectionView(),
                xr.CompositionLayerProjectionView())
            view_state, views = xr.locate_views(
                session=self.session,
                view_locate_info=xr.ViewLocateInfo(
                    view_configuration_type=self.view_configuration_type,
                    display_time=frame_state.predicted_display_time,
                    space=self.space,
                )
            )
            vsf = view_state.view_state_flags
            if (vsf & xr.VIEW_STATE_POSITION_VALID_BIT == 0
                    or vsf & xr.VIEW_STATE_ORIENTATION_VALID_BIT == 0):
                return  # There are no valid tracking poses for the views.
            for view_index, view in enumerate(views):
                view_swapchain = self.swapchains[view_index]
                swapchain_image_index = xr.acquire_swapchain_image(
                    swapchain=view_swapchain.handle,
                    acquire_info=xr.SwapchainImageAcquireInfo(),
                )
                xr.wait_swapchain_image(
                    swapchain=view_swapchain.handle,
                    wait_info=xr.SwapchainImageWaitInfo(timeout=xr.INFINITE_DURATION),
                )
                layer_view = projection_layer_views[view_index]
                assert layer_view.type == xr.StructureType.COMPOSITION_LAYER_PROJECTION_VIEW
                layer_view.pose = view.pose
                layer_view.fov = view.fov
                layer_view.sub_image.swapchain = view_swapchain.handle
                layer_view.sub_image.image_rect.offset[:] = [0, 0]
                layer_view.sub_image.image_rect.extent[:] = [
                    view_swapchain.width, view_swapchain.height, ]
                swapchain_image_ptr = self.swapchain_image_ptr_buffers[view_index][swapchain_image_index]
                swapchain_image = cast(swapchain_image_ptr, POINTER(xr.SwapchainImageOpenGLKHR)).contents
                assert layer_view.sub_image.image_array_index == 0  # texture arrays not supported.
                color_texture = swapchain_image.image
                self.graphics.begin_frame(layer_view, color_texture)

                yield view

                self.graphics.end_frame()
                xr.release_swapchain_image(
                    swapchain=view_swapchain.handle,
                    release_info=xr.SwapchainImageReleaseInfo()
                )
            layer.views = projection_layer_views
            self.render_layers.append(byref(layer))


__all__ = [
    "ContextObject",
]
