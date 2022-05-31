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

import xr


class GraphicsAPI(enum.Enum):
    VULKAN = 0,
    OPENGL = 1,
    OPENGL_ES = 2,
    D3D = 3,


# Column-major, pre-multiplied. This type does not exist in the OpenXR API and is provided for convenience.
class Matrix4x4f(Structure):
    _fields_ = [("m", c_float * 16), ]

    def __init__(self):
        super().__init__()
        self._numpy = None

    def __matmul__(self, other) -> "Matrix4x4f":
        return self.multiply(other)

    def as_numpy(self):
        if not hasattr(self, "_numpy") or self._numpy is None:
            # Just in time construction
            buffer = (c_float * 16).from_address(addressof(self))
            buffer._wrapper = self  # To link lifetime of buffer to self
            self._numpy = numpy.ctypeslib.as_array(buffer)
        return self._numpy

    @staticmethod
    def create_from_quaternion(quat: xr.Quaternionf) -> "Matrix4x4f":
        """ Creates a matrix from a quaternion. """
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

        result = Matrix4x4f()
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
                          tan_angle_down: float, near_z: float, far_z: float) -> "Matrix4x4f":
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
        result = Matrix4x4f()
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
    def create_projection_fov(graphics_api: GraphicsAPI, fov: xr.Fovf, near_z: float, far_z: float) -> "Matrix4x4f":
        """ Creates a projection matrix based on the specified FOV. """
        tan_left = math.tan(fov.angle_left)
        tan_right = math.tan(fov.angle_right)
        tan_down = math.tan(fov.angle_down)
        tan_up = math.tan(fov.angle_up)
        return Matrix4x4f.create_projection(graphics_api, tan_left, tan_right, tan_up, tan_down, near_z, far_z)

    @staticmethod
    def create_scale(x: float, y: float, z: float) -> "Matrix4x4f":
        """ Creates a scale matrix. """
        result = Matrix4x4f()
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
    def create_translation(x: float, y: float, z: float) -> "Matrix4x4f":
        """ Creates a translation matrix. """
        result = Matrix4x4f()
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
    def create_translation_rotation_scale(translation: xr.Vector3f, rotation: xr.Quaternionf, scale: xr.Vector3f) -> "Matrix4x4f":
        """ Creates a combined translation(rotation(scale(object))) matrix. """
        scale_matrix = Matrix4x4f.create_scale(*scale)
        rotation_matrix = Matrix4x4f.create_from_quaternion(rotation)
        translation_matrix = Matrix4x4f.create_translation(*translation)
        combined_matrix = rotation_matrix @ scale_matrix
        return translation_matrix @ combined_matrix

    def multiply(self, b: "Matrix4x4f") -> "Matrix4x4f":
        """ Use left-multiplication to accumulate transformations. """
        result = Matrix4x4f()
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

    """ Calculates the inverse of a rigid body transform. """
    def invert_rigid_body(self) -> "Matrix4x4f":
        result = Matrix4x4f()
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
