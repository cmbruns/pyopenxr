import time
import xr.utils.gl.glfw_util

# Once XR_KHR_headless extension is ratified and adopted, we
# should be able to avoid the Window and frame stuff here.
with xr.utils.gl.glfw_util.InstanceObject(application_name="track_hmd") as instance, \
      xr.utils.gl.glfw_util.SystemObject(instance) as system, \
      xr.utils.gl.glfw_util.GlfwWindow(system) as window, \
      xr.utils.gl.glfw_util.SessionObject(system, graphics_binding=window.graphics_binding) as session:
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
