"""
graphics_context_provider.py

Provides an abstract interface for activating an OpenGL rendering context
on a target surface or window system. Implementations must ensure safe thread
affinity and correct context sharing for offscreen rendering.

Supports manual activation and scoped context usage via `GLContextScope`.

Typical usage:

    provider.make_current()
    # Perform rendering...
    provider.done_current()

    # or using a scoped context:
    with provider.scope():
        GL.glDrawArrays(...)
"""

from abc import ABC, abstractmethod


class GraphicsContextProvider(ABC):
    """
    Abstract base class for activating an OpenGL rendering context.

    Concrete implementations should manage context binding/unbinding
    using framework-specific mechanisms (e.g., Qt, GLFW). Supports both
    manual and scoped activation models.

    Thread safety and proper context sharing must be enforced for offscreen usage.
    """

    def __enter__(self):
        """
        Enter the context manager.

        :return: self
        :rtype: GraphicsContextProvider
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the context manager, releasing any held resources.

        :param exc_type: Exception type, if any
        :param exc_val: Exception value, if any
        :param exc_tb: Exception traceback, if any
        """
        self.destroy()

    def destroy(self):
        """
        Optional cleanup method invoked during `__exit__`.
        Override to release platform-specific resources.
        """
        pass

    @abstractmethod
    def make_current(self) -> None:
        """
        Bind this context and surface to the current thread.
        Must be thread-safe and idempotent.
        """
        pass

    @abstractmethod
    def done_current(self) -> None:
        """
        Unbind the context from the current thread.
        Typically used after rendering operations.
        """
        pass

    def scope(self):
        """
        Create a scoped context activator compatible with `with` statement usage.

        :return: A new scoped context manager
        :rtype: GraphicsContextProvider.GLContextScope
        """
        return self.GLContextScope(self)

    class GLContextScope:
        """
        Scoped context activator for OpenGL rendering.

        Wraps a `GraphicsContextProvider` and ensures safe and reversible context
        activation, either manually or using the `with` statement.

        This does not create or destroy the context—it only manages bindings on
        the current thread.

        :param provider: The context provider instance
        :type provider: GraphicsContextProvider

        **Example (manual usage):**

            scope = provider.scope()
            scope.make_current()
            GL.glDrawArrays(...)
            scope.done_current()

        **Example (scoped usage):**

            with provider.scope():
                GL.glClear(GL.GL_COLOR_BUFFER_BIT)

        .. note::
            Designed for cross-backend compatibility (e.g., Qt, GLFW).
            May be extended to support profiling, validation, or debugging.
        """

        def __init__(self, provider: "GraphicsContextProvider"):
            """
            Initialize scoped context activator.

            :param provider: The context provider to activate
            :type provider: GraphicsContextProvider
            """
            self.provider = provider

        def make_current(self):
            """
            Activate the OpenGL context via the provider.
            """
            self.provider.make_current()

        def done_current(self):
            """
            Deactivate the OpenGL context via the provider.
            """
            self.provider.done_current()

        def __enter__(self):
            """
            Enter the scoped context.

            :return: self
            :rtype: GraphicsContextProvider.GLContextScope
            """
            self.make_current()
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            """
            Exit the scoped context.

            :param exc_type: Exception type
            :param exc_val: Exception value
            :param exc_tb: Exception traceback
            """
            self.done_current()


__all__ = [
    "GraphicsContextProvider",
]
