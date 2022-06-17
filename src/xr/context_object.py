from ctypes import byref, c_void_p, cast, POINTER, pointer
import time

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
        self.instance_handle = None
        self._session_create_info = session_create_info
        self.session_handle = None
        self.session_state = SessionState.IDLE
        self._reference_space_create_info = reference_space_create_info
        self.view_configuration_type = view_configuration_type
        self.frame_state = None
        self.environment_blend_mode = environment_blend_mode
        self.form_factor = form_factor
        self.graphics = None
        self.graphics_binding_pointer = None

    def __enter__(self):
        self.instance_handle = create_instance(
            create_info=self._instance_create_info,
        )
        self.system_id = get_system(
            instance=self.instance_handle,
            get_info=SystemGetInfo(
                form_factor=self.form_factor,
            ),
        )

        if self._session_create_info.next_structure is None:
            self.graphics = OpenGLGraphics(
                instance=self.instance_handle,
                system=self.system_id,
                title=self._instance_create_info.application_info.application_name.decode()
            )
            self.graphics_binding_pointer = cast(pointer(self.graphics.graphics_binding), c_void_p)
            self._session_create_info.next_structure = self.graphics_binding_pointer
        else:
            self.graphics_binding_pointer = self._session_create_info.next_structure

        self._session_create_info.system_id = self.system_id
        self.session_handle = create_session(
            instance=self.instance_handle,
            create_info=self._session_create_info,
        )
        self.space_handle = create_reference_space(
            session=self.session_handle,
            create_info=self._reference_space_create_info
        )

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.space_handle is not None:
            destroy_space(self.space_handle)
            self.space_handle = None
        if self.session_handle is not None:
            destroy_session(self.session_handle)
            self.session_handle = None
        if self.graphics is not None:
            self.graphics.destroy()
            self.graphics = None
        if self.instance_handle is not None:
            destroy_instance(self.instance_handle)
            self.instance_handle = None

    def frame_loop(self):
        while True:
            self.poll_xr_events()
            if self.session_state in (
                    SessionState.READY,
                    SessionState.SYNCHRONIZED,
                    SessionState.VISIBLE,
                    SessionState.FOCUSED,
            ):
                self.frame_state = wait_frame(self.session_handle)
                begin_frame(self.session_handle)

                yield self.frame_state

                end_frame(
                    self.session_handle,
                    frame_end_info=FrameEndInfo(
                        display_time=self.frame_state.predicted_display_time,
                        environment_blend_mode=self.environment_blend_mode,
                        layers=(),  # TODO: what is layers?
                    )
                )

    def poll_xr_events(self):
        while True:
            try:
                event_buffer = poll_event(self.instance_handle)
                event_type = StructureType(event_buffer.type)
                if event_type == StructureType.EVENT_DATA_SESSION_STATE_CHANGED \
                        and self.session_handle is not None:
                    event = cast(
                        byref(event_buffer),
                        POINTER(EventDataSessionStateChanged)).contents
                    self.session_state = SessionState(event.state)
                    if self.session_state == SessionState.READY:
                        begin_session(
                            session=self.session_handle,
                            begin_info=SessionBeginInfo(
                                self.view_configuration_type,
                            ),
                        )
                    elif self.session_state == SessionState.STOPPING:
                        destroy_session(self.session_handle)
                        self.session_handle = None
            except EventUnavailable:
                break


__all__ = [
    "ContextObject",
]
