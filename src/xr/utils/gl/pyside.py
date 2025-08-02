from typing import Optional

from PySide6.QtGui import QOffscreenSurface, QOpenGLContext, QSurfaceFormat
from xr.utils import GraphicsContextProvider


class PySide6OffscreenContextProvider(GraphicsContextProvider):
    """
    Provides an offscreen OpenGL context using PySide6's QOffscreenSurface and QOpenGLContext.

    This implementation enables rendering outside the visible window system, which is
    critical for integrating with OpenXR runtimes while preserving Qt's context-sharing semantics.

    Parameters:
        shared_context (Optional[QOpenGLContext]): An existing context to share resources with.
            If None, a default context format will be used.

    Attributes:
        surface (QOffscreenSurface): The offscreen surface used for rendering.
        context (QOpenGLContext): The OpenGL context bound to the surface.
    """

    def __init__(self, shared_context: Optional[QOpenGLContext] = None):
        # Decide on GL format: inherit from shared context or use default
        fmt = shared_context.format() if shared_context else self._default_format()

        # Create surface with the selected format
        self.surface = QOffscreenSurface()
        self.surface.setFormat(fmt)
        self.surface.create()

        # Create the context and optionally share with another
        self.context = QOpenGLContext()
        self.context.setFormat(fmt)
        if shared_context:
            self.context.setShareContext(shared_context)
        self.context.create()

    @staticmethod
    def _default_format() -> QSurfaceFormat:
        """
        Define a reasonable default OpenGL format for offscreen rendering.

        Returns:
            QSurfaceFormat: The chosen default format.
        """
        fmt = QSurfaceFormat()
        fmt.setDepthBufferSize(24)
        fmt.setStencilBufferSize(8)
        fmt.setVersion(4, 1)  # Ensures compatibility with modern OpenXR bindings
        fmt.setProfile(QSurfaceFormat.CoreProfile)  # Use core profile for headless rendering # noqa
        return fmt

    def make_current(self) -> None:
        """
        Bind this provider's OpenGL context to the current thread.
        """
        self.context.makeCurrent(self.surface)

    def done_current(self) -> None:
        """
        Unbind the OpenGL context from the current thread.
        """
        self.context.doneCurrent()
