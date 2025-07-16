import glfw


class GLFWContextProvider(object):
    def __init__(self):
        if not glfw.init():
            raise RuntimeError("GLFW initialization failed")
        glfw.window_hint(glfw.VISIBLE, False)
        glfw.window_hint(glfw.DOUBLEBUFFER, False)
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 5)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        self.window = glfw.create_window(
            64, 64,
            "glfw OpenGL window",
            None, None)
        if self.window is None:
            raise RuntimeError("Failed to create GLFW window")
        # Attempt to disable vsync on the desktop window, or
        # it will interfere with the OpenXR frame loop timing
        glfw.swap_interval(0)

    def destroy(self):
        glfw.destroy_window(self.window)
        self.window = None
        glfw.terminate()

    def make_current(self):
        glfw.make_context_current(self.window)

    def poll_events(self) -> bool:
        glfw.poll_events()
        return glfw.window_should_close(self.window)
