"""
Test for bit flags types.

Based on tests at https://github.com/KhronosGroup/OpenXR-Hpp/blob/master/tests/flags.cpp
"""

import unittest

import xr


class TestFlags(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_flags(self):
        flags = xr.SpaceVelocityFlagBits.LINEAR_VALID | xr.SpaceVelocityFlagBits.ANGULAR_VALID
        self.assertEqual(xr.SpaceVelocityFlagBits.LINEAR_VALID, flags & xr.SpaceVelocityFlagBits.LINEAR_VALID)
        self.assertTrue(xr.SpaceVelocityFlagBits.LINEAR_VALID)
        self.assertEqual(xr.SpaceVelocityFlagBits.ANGULAR_VALID, flags & xr.SpaceVelocityFlagBits.ANGULAR_VALID)
        self.assertTrue(xr.SpaceVelocityFlagBits.ANGULAR_VALID)
        cflags = xr.SpaceVelocityFlags(flags.value)  # c_uint64
        self.assertEqual(
            cflags.value,
            (xr.SpaceVelocityFlagBits.LINEAR_VALID | xr.SpaceVelocityFlagBits.ANGULAR_VALID).value,
        )

        flags = xr.SpaceVelocityFlagBits.LINEAR_VALID
        self.assertEqual(flags & xr.SpaceVelocityFlagBits.LINEAR_VALID, xr.SpaceVelocityFlagBits.LINEAR_VALID)
        self.assertEqual(bool(flags & xr.SpaceVelocityFlagBits.LINEAR_VALID), True)
        self.assertEqual(flags & xr.SpaceVelocityFlagBits.ANGULAR_VALID, xr.SpaceVelocityFlagBits.NONE)
        self.assertEqual(bool(flags & xr.SpaceVelocityFlagBits.ANGULAR_VALID), False)
        cflags = xr.SpaceVelocityFlags(flags.value)  # c_uint64
        self.assertEqual(cflags.value, xr.SPACE_VELOCITY_LINEAR_VALID_BIT)

        flags = xr.SpaceVelocityFlagBits()
        self.assertEqual(flags.value, xr.SpaceVelocityFlagBits.NONE.value)
        cflags = xr.SpaceVelocityFlags(flags.value)
        self.assertEqual(0, cflags.value)


if __name__ == '__main__':
    unittest.main()
