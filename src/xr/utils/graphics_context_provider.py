from abc import ABC, abstractmethod


class GraphicsContextProvider(ABC):
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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.destroy()

    def destroy(self):
        pass

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
            provider (GraphicsContextProvider): The context provider to activate.

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

        def __init__(self, provider: "GraphicsContextProvider"):
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

__all__ = [
    "GraphicsContextProvider",
]
