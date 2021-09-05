import time
import xr

with xr.Instance(application_name="track_hmd") as instance:
    with xr.System(instance) as system:
        with xr.GlfwWindow(system) as window:
            with xr.Session(system) as session:
                for _ in range(50):
                    session.poll_xr_events()
                    if session.state in (
                        xr.SessionState.READY,
                        xr.SessionState.SYNCHRONIZED,
                        xr.SessionState.VISIBLE,
                        xr.SessionState.FOCUSED,
                    ):
                        session.wait_frame()
                        session.begin_frame()
                        view_state, views = session.locate_views()
                        print(views[xr.Eye.LEFT.value].pose, flush=True)
                        time.sleep(0.2)
                        session.end_frame()
