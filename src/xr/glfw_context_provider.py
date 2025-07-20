from abc import ABC, abstractmethod
from typing import Tuple

import glfw


class OffscreenContextProvider(ABC):
    """
    Abstract interface for activating an OpenGL rendering context on a given surface.

    Implementations are responsible for managing context binding and unbinding—
    typically using framework-specific mechanisms like Qt or GLFW. This interface
    supports both manual activation and scoped usage via `GLContextScope`.

    Implementors must ensure thread-safe behavior and appropriate sharing semantics
    for offscreen contexts.

    Typical usage:

        provider.make_current()
        # Perform rendering...
        provider.done_current()

        # or using a scoped context:
        with provider.scope():
            GL.glDrawArrays(...)
    """

    @abstractmethod
    def make_current(self) -> None:
        """Bind this context and surface to the current thread."""
        pass

    @abstractmethod
    def done_current(self) -> None:
        """Unbind this context from the current thread."""
        pass

    def scope(self):
        """Return a scoped context activator for use with `with` or manual control."""
        return self.GLContextScope(self)

    class GLContextScope:
        """
        Scoped activator for an OpenGL rendering context.

        This class wraps an `OffscreenContextProvider`, allowing safe and reversible
        context activation via either manual calls or Python's `with` statement.

        It does not create or destroy the context—it simply manages when it is bound
        and unbound on the current thread.

        Parameters:
            provider (OffscreenContextProvider): The context provider to activate.

        Typical usage:

            # Manual lifecycle
            scope = provider.scope()
            scope.make_current()
            GL.glDrawArrays(...)
            scope.done_current()

            # Scoped lifecycle
            with provider.scope():
                GL.glClear(GL.GL_COLOR_BUFFER_BIT)

        Notes:
            - Designed for cross-backend compatibility (e.g., Qt, GLFW).
            - May be extended to support context validation, debugging, or profiling.
        """

        def __init__(self, provider: "OffscreenContextProvider"):
            self.provider = provider

        def make_current(self):
            """Activate the provider's context."""
            self.provider.make_current()

        def done_current(self):
            """Deactivate the provider's context."""
            self.provider.done_current()

        def __enter__(self):
            self.make_current()
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.done_current()


class GLFWOffscreenContextProvider(OffscreenContextProvider):
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
