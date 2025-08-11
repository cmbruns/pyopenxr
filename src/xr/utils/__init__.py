"""
High-level utilities and abstractions for OpenXR integration.

The :mod:`xr.utils` module provides ergonomic helpers, glue code, and convenience
constructs that complement the low-level OpenXR API exposed in :mod:`xr`. While
:mod:`xr` aims to mirror the native OpenXR specification as closely as possible,
:mod:`xr.utils` offers higher-level patterns that simplify common workflows,
such as view matrix construction, swapchain management, and pose utilities.

This module is intended for rapid iteration and may evolve more quickly than
the stable :mod:`xr` namespace. Developers should treat its API as provisional
and subject to refinement as best practices emerge.

Contents may include:
- Matrix and pose utilities for rendering and simulation
- Swapchain wrappers for per-view resource management
- Threading or lifecycle helpers for session orchestration
- Experimental constructs for bridging OpenXR with graphics APIs

:seealso: :mod:`xr`
"""
import enum
from abc import ABC, abstractmethod
from contextlib import ExitStack
from ctypes import cast, byref, POINTER
import logging
from math import tan
import time
from typing import Callable, Generic, List, Optional, Type, TypeVar

import numpy
import xr

from . import matrix4x4f
from .matrix4x4f import *

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())  # To avoid complaints about missing handler

SWAPCHAIN_IMAGE_TYPE = TypeVar("SWAPCHAIN_IMAGE_TYPE")


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


def projection_from_fovf(fov: xr.Fovf, near: float = 0.05, far: Optional[float] = None) -> numpy.ndarray:
    """
    Constructs a transposed forward projection matrix from OpenXR FOV angles.

    Produces a column-major matrix that maps eye-space to clip-space, suitable for VR rendering.
    Uses infinite reverse-Z projection by default. If `far` is specified, constructs a finite-depth variant.

    Parameters:
        fov  (xr.Fovf): Field-of-view angles (radians) with left, right, up, and down.
        near (float):   Near clipping plane distance; must be positive. Default is 0.05.
        far  (float | None): Far clipping plane. If None, assumes infinity.

    Returns:
        numpy.ndarray: Transposed forward projection matrix (4x4) in column-major format (float32).
    """
    left = tan(fov.angle_left) * near
    right = tan(fov.angle_right) * near
    bottom = tan(fov.angle_down) * near
    top = tan(fov.angle_up) * near
    if far is None:
        # Infinite reverse-Z projection
        proj = numpy.array([
            [2 * near / (right - left), 0, 0, 0],
            [0, 2 * near / (top - bottom), 0, 0],
            [0, 0, 0, -1],
            [(right + left) / (right - left), (top + bottom) / (top - bottom), -0.5, 0.5],
        ], dtype=numpy.float32, order="F")
    else:
        # Finite reverse-Z projection
        clip_range = far - near
        proj = numpy.array([
            [2 * near / (right - left), 0, 0, 0],
            [0, 2 * near / (top - bottom), 0, 0],
            [0, 0, far / clip_range, -1],
            [(right + left) / (right - left), (top + bottom) / (top - bottom), (far * near) / clip_range, 0],
        ], dtype=numpy.float32, order="F")
    return proj


def projection_inverse_from_fovf(fov: xr.Fovf, near: float = 0.05, far: Optional[float] = None) -> numpy.ndarray:
    """
    Constructs a transposed inverse projection matrix from OpenXR FOV angles.

    Produces a column-major inverse matrix suitable for reversing clip-to-eye-space transformations in VR.
    Defaults to infinite reverse-Z depth unless `far` is provided.

    Parameters:
        fov  (xr.Fovf): Field-of-view angles (radians) with left, right, up, and down.
        near (float):   Near clipping plane distance; must be positive. Default is 0.05.
        far  (float | None): Far clipping plane. If None, assumes infinity.

    Returns:
        numpy.ndarray: Transposed inverse projection matrix (4x4) in column-major format (float32).
    """
    left = tan(fov.angle_left) * near
    right = tan(fov.angle_right) * near
    bottom = tan(fov.angle_down) * near
    top = tan(fov.angle_up) * near
    if far is None:
        # Infinite reverse-Z projection
        inv_proj = numpy.array([
            [(right - left) / (2 * near), 0, 0, 0],
            [0, (top - bottom) / (2 * near), 0, 0],
            [0, 0, 0, -0.5 / near],
            [(right + left) / (2 * near), (top + bottom) / (2 * near), -1, 0.5],
        ], dtype=numpy.float32, order="F")
    else:
        # Finite reverse-Z projection
        clip_range = far - near
        inv_proj = numpy.array([
            [(right - left) / (2 * near), 0, 0, 0],
            [0, (top - bottom) / (2 * near), 0, 0],
            [0, 0, 0, (near * far) / clip_range],
            [(right + left) / (2 * near), (top + bottom) / (2 * near), -1, near / clip_range],
        ], dtype=numpy.float32, order="F")
    return inv_proj


def rotation_from_quaternionf(quat: xr.Quaternionf) -> numpy.ndarray:
    """
    Constructs a transposed 3×3 rotation matrix from an OpenXR-style quaternion.

    Converts a unit quaternion (w, x, y, z) into a right-handed rotation matrix suitable for transforming
    vectors from local to world space or vice versa. Output is in column-major order to align with OpenGL-style usage,
    and assumes the quaternion is normalized (unit length). No scale or shear is applied.

    Parameters:
        quat (xr.Quaternionf): Quaternion representing rotation, with components (x, y, z, w).
                               Expected to be normalized.

    Returns:
        numpy.ndarray: 3×3 rotation matrix (float32), transposed for column-major layout.
    """
    x2 = quat.x + quat.x
    y2 = quat.y + quat.y
    z2 = quat.z + quat.z

    xx2 = quat.x * x2
    yy2 = quat.y * y2
    zz2 = quat.z * z2

    yz2 = quat.y * z2
    wx2 = quat.w * x2
    xy2 = quat.x * y2
    wz2 = quat.w * z2
    xz2 = quat.x * z2
    wy2 = quat.w * y2

    return numpy.array([
        [1.0 - yy2 - zz2, xy2 + wz2, xz2 - wy2],
        [xy2 - wz2, 1.0 - xx2 - zz2, yz2 + wx2],
        [xz2 + wy2, yz2 - wx2, 1.0 - xx2 - yy2],
    ], dtype=numpy.float32, order="F")


def view_matrix_from_posef(pose: xr.Posef) -> numpy.ndarray:
    """
    Construct a view matrix from an OpenXR pose.

    This function computes a 4×4 view matrix from a given :class:`xr.Posef`, which
    includes orientation (as a quaternion) and position (as a 3D vector). The resulting
    matrix transforms world-space coordinates into view-space, suitable for rendering
    from the perspective of the pose.

    The view matrix is computed as the inverse of the world transform:
    :math:`V = R^T \\cdot T^{-1}`, where `R` is the rotation matrix and `T` is the
    translation matrix. The result is returned in column-major (Fortran-style) order
    to match OpenXR and graphics API conventions.

    :param pose: The pose representing the viewer's position and orientation in world space.
    :type pose: xr.Posef
    :return: A 4×4 view matrix in column-major order.
    :rtype: numpy.ndarray
    :seealso: :func:`xr.utils.rotation_from_quaternionf`, :class:`xr.Posef`
    """
    rotation3 = rotation_from_quaternionf(pose.orientation)
    translation = numpy.identity(4, dtype=numpy.float32)
    translation[:3, 3] = -pose.position.x, -pose.position.y, -pose.position.z

    rotation4 = numpy.identity(4, dtype=numpy.float32)
    rotation4[:3, :3] = rotation3.T

    view = rotation4 @ translation
    return numpy.array(view, dtype=numpy.float32, order='F')


def view_matrix_inverse_from_posef(pose: xr.Posef) -> numpy.ndarray:
    """
    Construct an inverse view matrix from an OpenXR pose.

    Computes a 4×4 world transform matrix from the given :class:`xr.Posef`. This
    matrix applies the pose’s position and orientation in world-space coordinates
    and is commonly used for camera-relative rendering, physics simulations, or
    head-to-world transformations.

    The matrix is assembled from a rotation (derived from the pose’s quaternion)
    and translation (from the pose’s 3D position), in the form:
    :math:`M = R \\cdot T`.

    The result is returned in column-major (Fortran-style) order, matching
    OpenXR and graphics API conventions.

    :param pose: The pose describing orientation and position in world space.
    :type pose: xr.Posef
    :return: A 4×4 transformation matrix in column-major order.
    :rtype: numpy.ndarray
    :seealso: :func:`xr.utils.rotation_from_quaternionf`, :class:`xr.Posef`
    """
    rotation3 = rotation_from_quaternionf(pose.orientation)
    transform = numpy.identity(4, dtype=numpy.float32)
    transform[:3, :3] = rotation3
    transform[:3, 3] = pose.position.x, pose.position.y, pose.position.z
    return numpy.array(transform, dtype=numpy.float32, order='F')


class SessionStateManager:
    """
    Handles OpenXR session state transitions, lifecycle control, and frame loop integration.

    This class manages the transition between session states, receives runtime events,
    and coordinates rendering activity. It also gracefully winds down the session
    during context exit or shutdown.

    Raises:
        ExitRenderLoop: When the session transitions into an exit state.
    """

    class ExitRenderLoop(BaseException):
        """Signal raised to indicate the frame loop should exit immediately."""
        pass

    def __init__(
        self,
        instance: xr.Instance,
        session: xr.Session,
        view_configuration_type: xr.ViewConfigurationType,
    ) -> None:
        self.instance = instance
        self.session = session
        self.view_configuration_type = view_configuration_type

        self.session_state = xr.SessionState.IDLE
        self.session_is_running = False
        self.request_restart = False
        self.exit_render_loop = False

    def begin_frame(self) -> Optional[xr.FrameState]:
        """
        Poll OpenXR events and start a frame if the session is running.

        Returns:
            FrameState if the frame is started, None otherwise.
        """
        if self.exit_render_loop:
            raise self.ExitRenderLoop()

        if self.session_is_running and self.session_state in (
            xr.SessionState.READY,
            xr.SessionState.SYNCHRONIZED,
            xr.SessionState.VISIBLE,
            xr.SessionState.FOCUSED,
        ):
            frame_state = xr.wait_frame(self.session)
            xr.begin_frame(self.session)
            return frame_state

        return None

    def _simple_end_frame(self, frame_state: xr.FrameState) -> None:
        """
        End a frame without rendering any layers.

        Used for wind-down behavior or minimal rendering.

        Args:
            frame_state: The frame state returned by `wait_frame()`.
        """
        xr.end_frame(
            self.session,
            frame_end_info=xr.FrameEndInfo(
                display_time=frame_state.predicted_display_time,
                environment_blend_mode=xr.EnvironmentBlendMode.OPAQUE,
                layers=[],
            )
        )

    def __enter__(self) -> "SessionStateManager":
        return self

    def __exit__(self, _exc_type, _exc_val, _exc_tb) -> None:
        """
        Gracefully unwind the session lifecycle during context exit.

        This attempts to exit the session, processes events, and runs several
        no-op frames to help the runtime shut down cleanly.
        """
        try:
            xr.request_exit_session(self.session)
        except xr.exception.SessionNotRunningError:
            pass  # Session already exited or never started
        for _ in range(20):
            while True:
                try:
                    event = xr.poll_event(self.instance)
                    self.handle_xr_event(event)
                except xr.EventUnavailable:
                    break
            if self.exit_render_loop:
                break
            if self.session_is_running:
                frame_state = self.begin_frame()
                time.sleep(0.050)  # Yield time for other subsystems
                if frame_state:
                    self._simple_end_frame(frame_state)

    def handle_xr_event(self, event_buffer: xr.EventDataBuffer) -> None:
        """
        Dispatch and handle runtime OpenXR events relevant to the session.

        Args:
            event_buffer: A buffer containing one OpenXR event.
        """
        event_type = xr.StructureType(event_buffer.type)

        if event_type == xr.StructureType.EVENT_DATA_INSTANCE_LOSS_PENDING:
            self.exit_render_loop = True
            self.request_restart = True

        elif event_type == xr.StructureType.EVENT_DATA_SESSION_STATE_CHANGED and self.session:
            event = cast(
                byref(event_buffer),
                POINTER(xr.EventDataSessionStateChanged)
            ).contents
            self.session_state = xr.SessionState(event.state)
            logger.info(f"OpenXR session state changed to {self.session_state.name}")

            if self.session_state == xr.SessionState.READY:
                xr.begin_session(
                    session=self.session,
                    begin_info=xr.SessionBeginInfo(self.view_configuration_type)
                )
                self.session_is_running = True

            elif self.session_state == xr.SessionState.STOPPING:
                self.session_is_running = False
                xr.end_session(self.session)

            elif self.session_state in (xr.SessionState.EXITING, xr.SessionState.LOSS_PENDING):
                self.exit_render_loop = True
                self.request_restart = (self.session_state == xr.SessionState.LOSS_PENDING)


class SwapchainInfo(Generic[SWAPCHAIN_IMAGE_TYPE]):
    """
    Encapsulates rendering resources for a single OpenXR view.

    This class manages the creation and lifecycle of an OpenXR swapchain associated
    with a single :class:`xr.ViewConfigurationView`, typically corresponding to one eye.
    It handles swapchain allocation, image enumeration, and cleanup, and provides
    metadata useful for framebuffer setup.

    :param view: Configuration metadata for the current view, including recommended image size and sample count.
    :type view: xr.ViewConfigurationView
    :param session: Active OpenXR session used to create the swapchain.
    :type session: xr.Session
    :param color_texture_format: OpenGL-compatible format constant (e.g., :data:`GL_RGBA8`).
    :type color_texture_format: int
    :param swapchain_image_type: ctypes structure type representing swapchain image buffers.
    :type swapchain_image_type: Type[SWAPCHAIN_IMAGE_TYPE]

    :ivar swapchain: Handle to the OpenXR swapchain object.
    :vartype swapchain: xr.Swapchain
    :ivar size: Tuple of (width, height) from the view configuration.
    :vartype size: Tuple[int, int]
    :ivar images: List of swapchain image buffers suitable for GPU binding.
    :vartype images: List[SWAPCHAIN_IMAGE_TYPE]

    :seealso: :func:`xr.create_swapchain`, :func:`xr.enumerate_swapchain_images`, :class:`xr.SwapchainCreateInfo`
    """

    def __init__(
            self,
            view: xr.ViewConfigurationView,
            session: xr.Session,
            color_texture_format: int,
            swapchain_image_type: Type[SWAPCHAIN_IMAGE_TYPE],
    ):
        # Set up swapchain creation parameters based on recommended view config
        create_info = xr.SwapchainCreateInfo(
            array_size=1,
            format=color_texture_format,
            width=view.recommended_image_rect_width,
            height=view.recommended_image_rect_height,
            mip_count=1,
            face_count=1,
            sample_count=view.recommended_swapchain_sample_count,
            usage_flags=xr.SwapchainUsageFlags.SAMPLED_BIT | xr.SwapchainUsageFlags.COLOR_ATTACHMENT_BIT,
        )
        # Create swapchain for rendering
        self.swapchain: xr.Swapchain = xr.create_swapchain(
            session=session, create_info=create_info)
        # Cache size info for FBO or framebuffer attachment
        self.size: tuple[int, int] = create_info.width, create_info.height
        # Enumerate swapchain image buffers; usually ctypes-wrapped GL texture pointers
        self.images = xr.enumerate_swapchain_images(
            swapchain=self.swapchain,
            element_type=swapchain_image_type,
        )

    def __enter__(self) -> "SwapchainInfo":
        """Allow usage with `with` statements."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Destroy the swapchain on exit, releasing GPU resources."""
        xr.destroy_swapchain(self.swapchain)


class SwapchainSet(Generic[SWAPCHAIN_IMAGE_TYPE]):
    """
    Aggregates swapchains for multiple OpenXR views.

    This class creates and manages a collection of per-view :class:`xr.Swapchain` instances,
    typically one for each eye in a stereo configuration. It uses an internal :class:`contextlib.ExitStack`
    to ensure lifecycle safety and deterministic resource cleanup.

    Swapchains are initialized using the recommended parameters from the runtime, as reported
    by :func:`xr.enumerate_view_configuration_views`.

    :param instance: The OpenXR runtime instance.
    :type instance: xr.Instance
    :param system_id: The headset or rendering system providing view capabilities.
    :type system_id: xr.SystemId
    :param session: The active OpenXR session used to create swapchains.
    :type session: xr.Session
    :param color_texture_format: OpenGL format used for swapchain images (e.g., :data:`GL_RGBA8`).
    :type color_texture_format: int
    :param swapchain_image_type: ctypes structure representing each swapchain image.
    :type swapchain_image_type: Type[SWAPCHAIN_IMAGE_TYPE]
    :param view_configuration_type: The view configuration, such as stereo or mono.
    :type view_configuration_type: xr.ViewConfigurationType

    :ivar views: List of view-specific swapchain resources.
    :vartype views: List[SwapchainInfo]
    :ivar exit_stack: Internal context manager for cleanup logic.
    :vartype exit_stack: contextlib.ExitStack

    :seealso: :class:`SwapchainInfo`, :class:`xr.ViewConfigurationView`
    """
    def __init__(
            self,
            instance: xr.Instance,
            system_id: xr.SystemId,
            session: xr.Session,
            color_texture_format: int,
            swapchain_image_type: Type[SWAPCHAIN_IMAGE_TYPE],
            view_configuration_type: xr.ViewConfigurationType = xr.ViewConfigurationType.PRIMARY_STEREO,
    ):
        self.exit_stack = ExitStack()  # noqa
        self.views: list[SwapchainInfo] = []
        # Enumerate views (typically left/right eyes), and create a swapchain for each
        config_views = xr.enumerate_view_configuration_views(
            instance=instance,
            system_id=system_id,
            view_configuration_type=view_configuration_type,
        )
        for view_index, view in enumerate(config_views):
            view_data = self.exit_stack.enter_context(
                SwapchainInfo(
                    view=view,
                    session=session,
                    color_texture_format=color_texture_format,
                    swapchain_image_type=swapchain_image_type,
                )
            )
            self.views.append(view_data)

    def __enter__(self) -> "SwapchainSet":
        """Support usage with `with` statements for lifecycle safety."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Destroy all managed swapchains in reverse creation order."""
        self.exit_stack.__exit__(exc_type, exc_val, exc_tb)


class XrEventDispatcher:
    """
    Polls OpenXR events and dispatches them to subscribed handlers.

    Subscribers must be callables that accept a single event argument.
    """

    def __init__(self, instance):
        self.instance = instance
        self.subscribers: List[Callable[[xr.EventDataBuffer], None]] = []

    def subscribe(self, callback: Callable[[xr.EventDataBuffer], None]):
        """
        Register a callback to receive OpenXR events.

        Args:
            callback: A callable that takes one event argument.
        """
        self.subscribers.append(callback)

    def poll(self):
        """
        Polls events from the OpenXR runtime and dispatches them to all subscribers.
        """
        while True:
            try:
                event = xr.poll_event(self.instance)
                for subscriber in self.subscribers:
                    subscriber(event)
            except xr.EventUnavailable:
                break


__all__ = [
    "GraphicsContextProvider",
    "projection_from_fovf",
    "projection_inverse_from_fovf",
    "rotation_from_quaternionf",
    "view_matrix_from_posef",
    "view_matrix_inverse_from_posef",
    "SessionStateManager",
    "SwapchainInfo",
    "SwapchainSet",
    "XrEventDispatcher",
]

__all__.extend(matrix4x4f.__all__)


class Eye(enum.IntEnum):
    LEFT = 0
    RIGHT = 1
