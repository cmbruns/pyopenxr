from math import tan
from typing import Optional

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


__all__ = [
    "projection_from_fovf",
    "projection_inverse_from_fovf",
    "rotation_from_quaternionf",
]

__all__.extend(classes.__all__)
__all__.extend(context_object.__all__)
__all__.extend(graphics_context_provider.__all__)
__all__.extend(matrix4x4f.__all__)
