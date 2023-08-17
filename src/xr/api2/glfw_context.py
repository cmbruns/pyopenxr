"""
OpenGL context using glfw.
This is sufficient for non-rendering uses of pyopenxr.
For example pseudo-headless use when the MND_headless extension is unavailable.
See GLSwapchain for when graphics display is required.
"""

import abc
import glfw
import xr


class IGLContext(abc.ABC):
    @abc.abstractmethod
    def make_current(self) -> None:
        pass

    @abc.abstractmethod
    def done_current(self) -> None:
        pass


class GLFWContext(IGLContext):
    @staticmethod
    def required_extensions():
        return [xr.KHR_OPENGL_ENABLE_EXTENSION_NAME]

    def __init__(self) -> None:
        if not glfw.init():
            raise xr.XrException("GLFW initialization failed")
        self.window_size = (64, 64)
        glfw.window_hint(glfw.VISIBLE, False)
        glfw.window_hint(glfw.DOUBLEBUFFER, False)
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 5)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        self.window = glfw.create_window(*self.window_size, "pyopenxr glfw OpenGL", None, None)
        if self.window is None:
            raise xr.XrException("Failed to create GLFW window")
        # Attempt to disable vsync on the desktop window, or
        # it will interfere with the OpenXR frame loop timing
        self.make_current()
        glfw.swap_interval(0)
        self.done_current()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.destroy()

    def destroy(self) -> None:
        self.make_current()
        glfw.destroy_window(self.window)
        self.window = None
        glfw.terminate()

    def done_current(self) -> None:
        glfw.make_context_current(None)

    def make_current(self) -> None:
        glfw.make_context_current(self.window)


__all__ = [
    "GLFWContext",
    "IGLContext",
]
