from ctypes import byref, c_void_p, cast, POINTER, pointer

import xr
from .enums import *
from .exception import *
from .typedefs import *
from .functions import *
from .opengl_graphics import OpenGLGraphics


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
        self.frame_state = None
        self.environment_blend_mode = environment_blend_mode
        self.form_factor = form_factor
        self.graphics = None
        self.graphics_binding_pointer = None
        self.closing = False
        self.action_sets = []

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

        if self._session_create_info.next_structure is None:
            self.graphics = OpenGLGraphics(
                instance=self.instance,
                system=self.system_id,
                title=self._instance_create_info.application_info.application_name.decode()
            )
            self.graphics_binding_pointer = cast(pointer(self.graphics.graphics_binding), c_void_p)
            self._session_create_info.next_structure = self.graphics_binding_pointer
        else:
            self.graphics_binding_pointer = self._session_create_info.next_structure

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
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
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
                action_sets=(ActionSetHandle * len(self.action_sets))(
                    *self.action_sets
                )
            ),
        )
        while True:
            self.poll_xr_events()
            if self.session_state in (
                    SessionState.READY,
                    SessionState.SYNCHRONIZED,
                    SessionState.VISIBLE,
                    SessionState.FOCUSED,
            ):
                self.frame_state = wait_frame(self.session)
                begin_frame(self.session)

                yield self.frame_state

                end_frame(
                    self.session,
                    frame_end_info=FrameEndInfo(
                        display_time=self.frame_state.predicted_display_time,
                        environment_blend_mode=self.environment_blend_mode,
                        layers=(),  # TODO: what is layers?
                    )
                )

    def poll_xr_events(self):
        while True:
            try:
                event_buffer = poll_event(self.instance)
                event_type = StructureType(event_buffer.type)
                if event_type == StructureType.EVENT_DATA_INSTANCE_LOSS_PENDING:
                    # still handle rest of the events instead of immediately quitting
                    self.closing = True
                elif event_type == StructureType.EVENT_DATA_SESSION_STATE_CHANGED \
                        and self.session is not None:
                    event = cast(
                        byref(event_buffer),
                        POINTER(EventDataSessionStateChanged)).contents
                    self.session_state = SessionState(event.state)
                    if self.session_state == SessionState.READY and not self.closing:
                        begin_session(
                            session=self.session,
                            begin_info=SessionBeginInfo(
                                self.view_configuration_type,
                            ),
                        )
                    elif self.session_state == SessionState.STOPPING:
                        self.closing = True
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


__all__ = [
    "ContextObject",
]
