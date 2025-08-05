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

from math import tan
from typing import Generic, Optional, Type, TypeVar

import numpy
import xr

from . import classes
from . import context_object
from . import graphics_context_provider
from . import matrix4x4f

from .classes import *
from .context_object import *
from .graphics_context_provider import *
from .matrix4x4f import *


SWAPCHAIN_IMAGE_TYPE = TypeVar("SWAPCHAIN_IMAGE_TYPE")


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


__all__ = [
    "projection_from_fovf",
    "projection_inverse_from_fovf",
    "rotation_from_quaternionf",
    "view_matrix_from_posef",
    "view_matrix_inverse_from_posef",
    "SwapchainInfo",
]

__all__.extend(classes.__all__)
__all__.extend(context_object.__all__)
__all__.extend(graphics_context_provider.__all__)
__all__.extend(matrix4x4f.__all__)
