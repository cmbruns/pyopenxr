import time
import xr

# Once XR_KHR_headless extension is ratified and adopted, we
# should be able to avoid the Window and frame stuff here.
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
                        time.sleep(0.5)
                        session.end_frame()
