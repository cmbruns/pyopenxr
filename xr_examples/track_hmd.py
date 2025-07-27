import time
import xr.utils

# Once XR_KHR_headless extension is ratified and adopted, we
# should be able to avoid the Window and frame stuff here.
with xr.utils.InstanceObject(application_name="track_hmd") as instance, \
      xr.utils.SystemObject(instance) as system, \
      xr.utils.GlfwWindow(system) as window, \
      xr.utils.SessionObject(system, graphics_binding=window.graphics_binding) as session:
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
            print(views[xr.utils.Eye.LEFT.value].pose, flush=True)
            time.sleep(0.5)
            session.end_frame()
