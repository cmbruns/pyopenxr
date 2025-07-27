"""
# Copyright (c) 2017 The Khronos Group Inc.
# Copyright (c) 2016 Oculus VR, LLC.
#
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: J.M.P. van Waveren
#
"""

from ctypes import addressof, c_float, Structure
import enum
import math
import numpy
from typing import Sequence

import xr


class GraphicsAPI(enum.Enum):
    VULKAN = 0,
    OPENGL = 1,
    OPENGL_ES = 2,
    D3D = 3,


# Column-major, pre-multiplied. This type does not exist in the OpenXR API and is provided for convenience.
class Matrix4x4f_ctypes(Structure):
    _fields_ = [("m", c_float * 16), ]

    def __init__(self, matrix=None):
        super().__init__()
        self._numpy = None
        self._arr_1d = None
        self._buffer = None
        if matrix is None:
            for i in range(4):
                self.m[i * 4 + i] = 1.0
        else:
            arr = numpy.array(matrix, dtype=numpy.float32, order="F")
            if arr.shape != (4, 4):
                raise ValueError("Expected a 4x4 matrix")
            for row in range(4):
                for col in range(4):
                    self.m[col * 4 + row] = arr[row][col]

    def as_numpy(self):
        if not hasattr(self, "_numpy") or self._numpy is None:
            # Just in time construction
            self._buffer = (c_float * 16).from_address(addressof(self.m))
            self._arr_1d = numpy.frombuffer(self._buffer, dtype=numpy.float32)
            self._numpy = self._arr_1d.reshape((4, 4), order="F")
            assert self._numpy.base is self._arr_1d
        return self._numpy

    def invert_rigid_body(self) -> "Matrix4x4f_ctypes":
        """ Calculates the inverse of a rigid body transform. """
        result = Matrix4x4f_ctypes()
        result.m[0] = self.m[0]
        result.m[1] = self.m[4]
        result.m[2] = self.m[8]
        result.m[3] = 0.0
        result.m[4] = self.m[1]
        result.m[5] = self.m[5]
        result.m[6] = self.m[9]
        result.m[7] = 0.0
        result.m[8] = self.m[2]
        result.m[9] = self.m[6]
        result.m[10] = self.m[10]
        result.m[11] = 0.0
        result.m[12] = -(self.m[0] * self.m[12] + self.m[1] * self.m[13] + self.m[2] * self.m[14])
        result.m[13] = -(self.m[4] * self.m[12] + self.m[5] * self.m[13] + self.m[6] * self.m[14])
        result.m[14] = -(self.m[8] * self.m[12] + self.m[9] * self.m[13] + self.m[10] * self.m[14])
        result.m[15] = 1.0
        return result

    @staticmethod
    def create_from_quaternion(quat: xr.Quaternionf) -> "Matrix4x4f_ctypes":
        """ Creates a matrix from a quaternion. """
        quat_norm = quat.as_numpy()
        quat_norm = quat_norm / numpy.linalg.norm(quat_norm)
        x, y, z, w = quat_norm

        x2 = x + x
        y2 = y + y
        z2 = z + z

        xx2 = x * x2
        yy2 = y * y2
        zz2 = z * z2

        yz2 = y * z2
        wx2 = w * x2
        xy2 = x * y2
        wz2 = w * z2
        xz2 = x * z2
        wy2 = w * y2

        result = Matrix4x4f_ctypes()
        result.m[0] = 1.0 - yy2 - zz2
        result.m[1] = xy2 + wz2
        result.m[2] = xz2 - wy2
        result.m[3] = 0.0

        result.m[4] = xy2 - wz2
        result.m[5] = 1.0 - xx2 - zz2
        result.m[6] = yz2 + wx2
        result.m[7] = 0.0

        result.m[8] = xz2 + wy2
        result.m[9] = yz2 - wx2
        result.m[10] = 1.0 - xx2 - yy2
        result.m[11] = 0.0

        result.m[12] = 0.0
        result.m[13] = 0.0
        result.m[14] = 0.0
        result.m[15] = 1.0
        return result

    @staticmethod
    def create_projection(graphics_api: GraphicsAPI, tan_angle_left: float, tan_angle_right: float, tan_angle_up: float,
                          tan_angle_down: float, near_z: float, far_z: float) -> "Matrix4x4f_ctypes":
        """
        # Creates a projection matrix based on the specified dimensions.
        # The projection matrix transforms -Z=forward, +Y=up, +X=right to the appropriate clip space for the graphics API.
        # The far plane is placed at infinity if far_z <= near_z.
        # An infinite projection matrix is preferred for rasterization because, except for
        # things *right* up against the near plane, it always provides better precision:
        #              "Tightening the Precision of Perspective Rendering"
        #              Paul Upchurch, Mathieu Desbrun
        #              Journal of Graphics Tools, Volume 16, Issue 1, 2012
        """
        tan_angle_width = tan_angle_right - tan_angle_left
        # Set to tan_angle_down - tan_angle_up for a clip space with positive Y down (Vulkan).
        # Set to tan_angle_up - tan_angle_down for a clip space with positive Y up (OpenGL / D3D / Metal).
        tan_angle_height = (tan_angle_down - tan_angle_up) if graphics_api == GraphicsAPI.VULKAN else (tan_angle_up - tan_angle_down)
        # Set to near_z for a [-1,1] Z clip space (OpenGL / OpenGL ES).
        # Set to zero for a [0,1] Z clip space (Vulkan / D3D / Metal).
        offset_z = near_z if graphics_api == GraphicsAPI.OPENGL or graphics_api == GraphicsAPI.OPENGL_ES else 0
        result = Matrix4x4f_ctypes()

        if far_z <= near_z:
            # place the far plane at infinity
            result.m[0] = 2.0 / tan_angle_width
            result.m[4] = 0.0
            result.m[8] = (tan_angle_right + tan_angle_left) / tan_angle_width
            result.m[12] = 0.0

            result.m[1] = 0.0
            result.m[5] = 2.0 / tan_angle_height
            result.m[9] = (tan_angle_up + tan_angle_down) / tan_angle_height
            result.m[13] = 0.0

            result.m[2] = 0.0
            result.m[6] = 0.0
            result.m[10] = -1.0
            result.m[14] = -(near_z + offset_z)

            result.m[3] = 0.0
            result.m[7] = 0.0
            result.m[11] = -1.0
            result.m[15] = 0.0
        else:
            # normal projection
            result.m[0] = 2.0 / tan_angle_width
            result.m[4] = 0.0
            result.m[8] = (tan_angle_right + tan_angle_left) / tan_angle_width
            result.m[12] = 0.0

            result.m[1] = 0.0
            result.m[5] = 2.0 / tan_angle_height
            result.m[9] = (tan_angle_up + tan_angle_down) / tan_angle_height
            result.m[13] = 0.0

            result.m[2] = 0.0
            result.m[6] = 0.0
            result.m[10] = -(far_z + offset_z) / (far_z - near_z)
            result.m[14] = -(far_z * (near_z + offset_z)) / (far_z - near_z)

            result.m[3] = 0.0
            result.m[7] = 0.0
            result.m[11] = -1.0
            result.m[15] = 0.0
        return result

    @staticmethod
    def create_projection_fov(graphics_api: GraphicsAPI, fov: xr.Fovf, near_z: float, far_z: float) -> "Matrix4x4f_ctypes":
        """ Creates a projection matrix based on the specified FOV. """
        tan_left = math.tan(fov.angle_left)
        tan_right = math.tan(fov.angle_right)
        tan_down = math.tan(fov.angle_down)
        tan_up = math.tan(fov.angle_up)
        return Matrix4x4f_ctypes.create_projection(graphics_api, tan_left, tan_right, tan_up, tan_down, near_z, far_z)

    @staticmethod
    def create_scale(x: float, y: float, z: float) -> "Matrix4x4f_ctypes":
        """ Creates a scale matrix. """
        result = Matrix4x4f_ctypes()
        result.m[0] = x
        result.m[1] = 0.0
        result.m[2] = 0.0
        result.m[3] = 0.0
        result.m[4] = 0.0
        result.m[5] = y
        result.m[6] = 0.0
        result.m[7] = 0.0
        result.m[8] = 0.0
        result.m[9] = 0.0
        result.m[10] = z
        result.m[11] = 0.0
        result.m[12] = 0.0
        result.m[13] = 0.0
        result.m[14] = 0.0
        result.m[15] = 1.0
        return result

    @staticmethod
    def create_translation(x: float, y: float, z: float) -> "Matrix4x4f_ctypes":
        """ Creates a translation matrix. """
        result = Matrix4x4f_ctypes()
        result.m[0] = 1.0
        result.m[1] = 0.0
        result.m[2] = 0.0
        result.m[3] = 0.0
        result.m[4] = 0.0
        result.m[5] = 1.0
        result.m[6] = 0.0
        result.m[7] = 0.0
        result.m[8] = 0.0
        result.m[9] = 0.0
        result.m[10] = 1.0
        result.m[11] = 0.0
        result.m[12] = x
        result.m[13] = y
        result.m[14] = z
        result.m[15] = 1.0
        return result

    @staticmethod
    def create_translation_rotation_scale(translation: xr.Vector3f, rotation: xr.Quaternionf, scale: Sequence[float]) -> "Matrix4x4f_ctypes":
        """ Creates a combined translation(rotation(scale(object))) matrix. """
        scale_matrix = Matrix4x4f_ctypes.create_scale(*scale)
        rotation_matrix = Matrix4x4f_ctypes.create_from_quaternion(rotation)
        translation_matrix = Matrix4x4f_ctypes.create_translation(*translation)
        combined_matrix = rotation_matrix @ scale_matrix
        return translation_matrix @ combined_matrix

    def __getitem__(self, item):
        return self.m[item]

    def __len__(self):
        return len(self.m)

    def __matmul__(self, other) -> "Matrix4x4f_ctypes":
        return self.multiply(other)

    def multiply(self, b: "Matrix4x4f_ctypes") -> "Matrix4x4f_ctypes":
        """ Use left-multiplication to accumulate transformations. """
        result = Matrix4x4f_ctypes()
        result.m[0] = self.m[0] * b.m[0] + self.m[4] * b.m[1] + self.m[8] * b.m[2] + self.m[12] * b.m[3]
        result.m[1] = self.m[1] * b.m[0] + self.m[5] * b.m[1] + self.m[9] * b.m[2] + self.m[13] * b.m[3]
        result.m[2] = self.m[2] * b.m[0] + self.m[6] * b.m[1] + self.m[10] * b.m[2] + self.m[14] * b.m[3]
        result.m[3] = self.m[3] * b.m[0] + self.m[7] * b.m[1] + self.m[11] * b.m[2] + self.m[15] * b.m[3]

        result.m[4] = self.m[0] * b.m[4] + self.m[4] * b.m[5] + self.m[8] * b.m[6] + self.m[12] * b.m[7]
        result.m[5] = self.m[1] * b.m[4] + self.m[5] * b.m[5] + self.m[9] * b.m[6] + self.m[13] * b.m[7]
        result.m[6] = self.m[2] * b.m[4] + self.m[6] * b.m[5] + self.m[10] * b.m[6] + self.m[14] * b.m[7]
        result.m[7] = self.m[3] * b.m[4] + self.m[7] * b.m[5] + self.m[11] * b.m[6] + self.m[15] * b.m[7]

        result.m[8] = self.m[0] * b.m[8] + self.m[4] * b.m[9] + self.m[8] * b.m[10] + self.m[12] * b.m[11]
        result.m[9] = self.m[1] * b.m[8] + self.m[5] * b.m[9] + self.m[9] * b.m[10] + self.m[13] * b.m[11]
        result.m[10] = self.m[2] * b.m[8] + self.m[6] * b.m[9] + self.m[10] * b.m[10] + self.m[14] * b.m[11]
        result.m[11] = self.m[3] * b.m[8] + self.m[7] * b.m[9] + self.m[11] * b.m[10] + self.m[15] * b.m[11]

        result.m[12] = self.m[0] * b.m[12] + self.m[4] * b.m[13] + self.m[8] * b.m[14] + self.m[12] * b.m[15]
        result.m[13] = self.m[1] * b.m[12] + self.m[5] * b.m[13] + self.m[9] * b.m[14] + self.m[13] * b.m[15]
        result.m[14] = self.m[2] * b.m[12] + self.m[6] * b.m[13] + self.m[10] * b.m[14] + self.m[14] * b.m[15]
        result.m[15] = self.m[3] * b.m[12] + self.m[7] * b.m[13] + self.m[11] * b.m[14] + self.m[15] * b.m[15]
        return result

    def __repr__(self):
        return f"Matrix4x4f_ctypes({[x for x in self.m]})"

    def __str__(self):
        return str(self.as_numpy())


class Matrix4x4f:
    """
    Attempt to match Matrix4x4f_ctypes API with numpy backing July 24, 2025
    """
    def __init__(self, data=None):
        if data is None:
            self.m = numpy.eye(4, dtype=numpy.float32, order="F")
        else:
            self.m = numpy.array(data, dtype=numpy.float32).reshape((4, 4), order='F')  # column-major

    def __array__(self, dtype=None):
        return numpy.array(self.m, dtype=dtype, order="F")

    def as_numpy(self) -> numpy.ndarray:
        return self.m

    @staticmethod
    def create_from_quaternion(quat: xr.Quaternionf) -> "Matrix4x4f":
        quat_norm = quat.as_numpy()
        quat_norm = quat_norm / numpy.linalg.norm(quat_norm)
        x, y, z, w = quat_norm
        x2, y2, z2 = x + x, y + y, z + z
        xx2, yy2, zz2 = x * x2, y * y2, z * z2
        yz2, wx2 = y * z2, w * x2
        xy2, wz2 = x * y2, w * z2
        xz2, wy2 = x * z2, w * y2

        m = numpy.zeros((4, 4), dtype=numpy.float32)
        m[0, 0] = 1.0 - yy2 - zz2
        m[1, 0] = xy2 + wz2
        m[2, 0] = xz2 - wy2

        m[0, 1] = xy2 - wz2
        m[1, 1] = 1.0 - xx2 - zz2
        m[2, 1] = yz2 + wx2

        m[0, 2] = xz2 + wy2
        m[1, 2] = yz2 - wx2
        m[2, 2] = 1.0 - xx2 - yy2

        m[3, 3] = 1.0
        return Matrix4x4f(m)

    @staticmethod
    def create_projection(graphics_api: GraphicsAPI, tan_left, tan_right, tan_up, tan_down, near_z, far_z) -> "Matrix4x4f":
        w = tan_right - tan_left
        h = tan_down - tan_up if graphics_api == GraphicsAPI.VULKAN else tan_up - tan_down
        offset_z = 0 if graphics_api in [GraphicsAPI.VULKAN, GraphicsAPI.D3D] else near_z

        m = numpy.zeros((4, 4), dtype=numpy.float32, order="F")
        m[0, 0] = 2.0 / w
        m[0, 2] = (tan_right + tan_left) / w
        m[1, 1] = 2.0 / h
        m[1, 2] = (tan_up + tan_down) / h
        if far_z <= near_z:
            # Infinite projection
            m[2, 2] = -1.0
            m[2, 3] = -(near_z + offset_z)
        else:
            # Finite far plane
            m[2, 2] = -(far_z + offset_z) / (far_z - near_z)
            m[2, 3] = -(far_z * (near_z + offset_z)) / (far_z - near_z)
        m[3, 2] = -1.0
        return Matrix4x4f(m)

    @staticmethod
    def create_projection_fov(graphics_api: GraphicsAPI, fov: xr.Fovf, near_z: float, far_z: float) -> "Matrix4x4f":
        return Matrix4x4f.create_projection(
            graphics_api,
            math.tan(fov.angle_left),
            math.tan(fov.angle_right),
            math.tan(fov.angle_up),
            math.tan(fov.angle_down),
            near_z,
            far_z
        )

    @staticmethod
    def create_scale(x: float, y: float, z: float) -> "Matrix4x4f":
        m = numpy.eye(4, dtype=numpy.float32, order="F")
        m[0, 0], m[1, 1], m[2, 2] = x, y, z
        return Matrix4x4f(m)

    @staticmethod
    def create_translation(x: float, y: float, z: float) -> "Matrix4x4f":
        m = numpy.eye(4, dtype=numpy.float32, order="F")
        m[0, 3], m[1, 3], m[2, 3] = x, y, z
        return Matrix4x4f(m)

    @staticmethod
    def create_translation_rotation_scale(translation: xr.Vector3f, rotation: xr.Quaternionf, scale: Sequence[float]) -> "Matrix4x4f":
        scale_matrix = Matrix4x4f.create_scale(*scale)
        rotation_matrix = Matrix4x4f.create_from_quaternion(rotation)
        translation_matrix = Matrix4x4f.create_translation(*translation)
        return translation_matrix @ (rotation_matrix @ scale_matrix)

    def __eq__(self, other):
        return numpy.array_equal(self.m, other)

    def __getitem__(self, item):
        return self.m[item]

    def invert_rigid_body(self) -> "Matrix4x4f":
        rotation = self[:3, :3].T
        translation = self[:3, 3]
        m_inv = numpy.eye(4, dtype=numpy.float32, order="F")
        m_inv[:3, :3] = rotation
        m_inv[:3, 3] = -rotation @ translation
        return Matrix4x4f(m_inv)

    def __len__(self):
        return len(self.m)

    def __matmul__(self, other: "Matrix4x4f") -> "Matrix4x4f":
        return Matrix4x4f(numpy.matmul(self, other))

    def __repr__(self):
        return f"Matrix4x4f({repr(self.m)})"

    def __str__(self):
        return str(self.m)


__all__ = [
    "GraphicsAPI",
    # "Matrix4x4f_ctypes",
    "Matrix4x4f",
]
