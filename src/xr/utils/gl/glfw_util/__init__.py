from typing import Tuple

import glfw

from .. import GraphicsContextProvider

from . import classes

from .classes import *


class GLFWSharedOffscreenContextProvider(GraphicsContextProvider):
    def __init__(self, window) -> None:
        glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
        glfw.window_hint(glfw.DOUBLEBUFFER, glfw.FALSE)
        # tiny 1×1 window just to get a context
        self._window = glfw.create_window(1, 1, "", None, window)
        if self._window is None:
            raise RuntimeError("Failed to create hidden GLFW window")
        # make it current so swap_interval takes effect on this context
        glfw.make_context_current(self._window)
        glfw.swap_interval(0)

    def __enter__(self) -> "GLFWOffscreenContextProvider":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.destroy()

    def destroy(self) -> None:
        """Tear down the hidden window and terminate GLFW."""
        glfw.destroy_window(self._window)
        self._window = None

    def make_current(self) -> None:
        """Activate this OpenGL context for subsequent GL calls."""
        glfw.make_context_current(self._window)

    def done_current(self) -> None:
        """Unbind this context from the current thread."""
        glfw.make_context_current(None)


class GLFWOffscreenContextProvider(GraphicsContextProvider):
    """
    Create a hidden OpenGL context (offscreen) for use with the OpenXR render loop.
    Only make_current() and destroy() are exposed.
    """
    def __init__(self, gl_version: Tuple[int, int] = (4, 1)) -> None:
        if not glfw.init():
            raise RuntimeError("Failed to initialize GLFW")
        # hidden, single‐buffered context
        glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
        glfw.window_hint(glfw.DOUBLEBUFFER, glfw.FALSE)
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, gl_version[0])
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, gl_version[1])
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        # tiny 1×1 window just to get a context
        self._window = glfw.create_window(1, 1, "", None, None)
        if self._window is None:
            glfw.terminate()
            raise RuntimeError("Failed to create hidden GLFW window")
        # make it current so swap_interval takes effect on this context
        glfw.make_context_current(self._window)
        glfw.swap_interval(0)

    def __enter__(self) -> "GLFWOffscreenContextProvider":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.destroy()

    def destroy(self) -> None:
        """Tear down the hidden window and terminate GLFW."""
        glfw.destroy_window(self._window)
        glfw.terminate()
        self._window = None

    def make_current(self) -> None:
        """Activate this OpenGL context for subsequent GL calls."""
        glfw.make_context_current(self._window)

    def done_current(self) -> None:
        """Unbind this context from the current thread."""
        glfw.make_context_current(None)


__all__ = [
    "GLFWOffscreenContextProvider",
    "GLFWSharedOffscreenContextProvider",
]

__all__.extend(classes.__all__)
