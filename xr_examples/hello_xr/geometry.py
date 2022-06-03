"""
Copyright (c) 2017-2022, The Khronos Group Inc.
SPDX-License-Identifier: Apache-2.0
"""

import ctypes
import numpy
import xr


class Vertex(ctypes.Structure):
    _fields_ = [
        ("position", xr.Vector3f),
        ("color", xr.Vector3f),
    ]


Red = numpy.array([1, 0, 0], dtype=numpy.float32)
DarkRed = numpy.array([0.25, 0, 0], dtype=numpy.float32)
Green = numpy.array([0, 1, 0], dtype=numpy.float32)
DarkGreen = numpy.array([0, 0.25, 0], dtype=numpy.float32)
Blue = numpy.array([0, 0, 1], dtype=numpy.float32)
DarkBlue = numpy.array([0, 0, 0.25], dtype=numpy.float32)

# Vertices for a 1x1x1 meter cube. (Left/Right, Top/Bottom, Front/Back)
LBB = numpy.array([-0.5, -0.5, -0.5], dtype=numpy.float32)
LBF = numpy.array([-0.5, -0.5, 0.5], dtype=numpy.float32)
LTB = numpy.array([-0.5, 0.5, -0.5], dtype=numpy.float32)
LTF = numpy.array([-0.5, 0.5, 0.5], dtype=numpy.float32)
RBB = numpy.array([0.5, -0.5, -0.5], dtype=numpy.float32)
RBF = numpy.array([0.5, -0.5, 0.5], dtype=numpy.float32)
RTB = numpy.array([0.5, 0.5, -0.5], dtype=numpy.float32)
RTF = numpy.array([0.5, 0.5, 0.5], dtype=numpy.float32)


def cube_side(v1, v2, v3, v4, v5, v6, color):
    return numpy.array([
        [v1, color], [v2, color], [v3, color], [v4, color], [v5, color], [v6, color],
        ], dtype=numpy.float32)


c_cubeVertices = numpy.array([
    cube_side(LTB, LBF, LBB, LTB, LTF, LBF, DarkRed),    # -X
    cube_side(RTB, RBB, RBF, RTB, RBF, RTF, Red),        # +X
    cube_side(LBB, LBF, RBF, LBB, RBF, RBB, DarkGreen),  # -Y
    cube_side(LTB, RTB, RTF, LTB, RTF, LTF, Green),      # +Y
    cube_side(LBB, RBB, RTB, LBB, RTB, LTB, DarkBlue),   # -Z
    cube_side(LBF, LTF, RTF, LBF, RTF, RBF, Blue),       # +Z
], dtype=numpy.float32)

# Winding order is clockwise. Each side uses a different color.
c_cubeIndices = numpy.array([
    0,  1,  2,  3,  4,  5,   # -X
    6,  7,  8,  9,  10, 11,  # +X
    12, 13, 14, 15, 16, 17,  # -Y
    18, 19, 20, 21, 22, 23,  # +Y
    24, 25, 26, 27, 28, 29,  # -Z
    30, 31, 32, 33, 34, 35,  # +Z
], dtype=numpy.uint16)
