from ctypes import byref, cast, POINTER
import logging
import time
from typing import Optional

import xr

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())  # To avoid complaints about missing handler


class SessionStateManager:
    """
    Handles OpenXR session state transitions, lifecycle control, and frame loop integration.

    This class manages the transition between session states, receives runtime events,
    and coordinates rendering activity. It also gracefully winds down the session
    during context exit or shutdown.

    Raises:
        ExitRenderLoop: When the session transitions into an exit state.
    """

    class ExitRenderLoop(BaseException):
        """Signal raised to indicate the frame loop should exit immediately."""
        pass

    def __init__(
        self,
        instance: xr.Instance,
        session: xr.Session,
        view_configuration_type: xr.ViewConfigurationType,
    ) -> None:
        self.instance = instance
        self.session = session
        self.view_configuration_type = view_configuration_type

        self.session_state = xr.SessionState.IDLE
        self.session_is_running = False
        self.request_restart = False
        self.exit_render_loop = False

    def begin_frame(self) -> Optional[xr.FrameState]:
        """
        Poll OpenXR events and start a frame if the session is running.

        Returns:
            FrameState if the frame is started, None otherwise.
        """
        if self.exit_render_loop:
            raise self.ExitRenderLoop()

        if self.session_is_running and self.session_state in (
            xr.SessionState.READY,
            xr.SessionState.SYNCHRONIZED,
            xr.SessionState.VISIBLE,
            xr.SessionState.FOCUSED,
        ):
            frame_state = xr.wait_frame(self.session)
            xr.begin_frame(self.session)
            return frame_state

        return None

    def _simple_end_frame(self, frame_state: xr.FrameState) -> None:
        """
        End a frame without rendering any layers.

        Used for wind-down behavior or minimal rendering.

        Args:
            frame_state: The frame state returned by `wait_frame()`.
        """
        xr.end_frame(
            self.session,
            frame_end_info=xr.FrameEndInfo(
                display_time=frame_state.predicted_display_time,
                environment_blend_mode=xr.EnvironmentBlendMode.OPAQUE,
                layers=[],
            )
        )

    def __enter__(self) -> "SessionStateManager":
        return self

    def __exit__(self, _exc_type, _exc_val, _exc_tb) -> None:
        """
        Gracefully unwind the session lifecycle during context exit.

        This attempts to exit the session, processes events, and runs several
        no-op frames to help the runtime shut down cleanly.
        """
        try:
            xr.request_exit_session(self.session)
        except xr.exception.SessionNotRunningError:
            pass  # Session already exited or never started
        for _ in range(20):
            while True:
                try:
                    event = xr.poll_event(self.instance)
                    self.handle_xr_event(event)
                except xr.EventUnavailable:
                    break
            if self.exit_render_loop:
                break
            if self.session_is_running:
                frame_state = self.begin_frame()
                time.sleep(0.050)  # Yield time for other subsystems
                if frame_state:
                    self._simple_end_frame(frame_state)

    def handle_xr_event(self, event_buffer: xr.EventDataBuffer) -> None:
        """
        Dispatch and handle runtime OpenXR events relevant to the session.

        Args:
            event_buffer: A buffer containing one OpenXR event.
        """
        event_type = xr.StructureType(event_buffer.type)

        if event_type == xr.StructureType.EVENT_DATA_INSTANCE_LOSS_PENDING:
            self.exit_render_loop = True
            self.request_restart = True

        elif event_type == xr.StructureType.EVENT_DATA_SESSION_STATE_CHANGED and self.session:
            event = cast(
                byref(event_buffer),
                POINTER(xr.EventDataSessionStateChanged)
            ).contents
            self.session_state = xr.SessionState(event.state)
            logger.info(f"OpenXR session state changed to {self.session_state.name}")

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
