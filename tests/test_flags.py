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
        flags = xr.SpaceVelocityFlags.LINEAR_VALID_BIT | xr.SpaceVelocityFlags.ANGULAR_VALID_BIT
        self.assertEqual(xr.SpaceVelocityFlags.LINEAR_VALID_BIT, flags & xr.SpaceVelocityFlags.LINEAR_VALID_BIT)
        self.assertTrue(xr.SpaceVelocityFlags.LINEAR_VALID_BIT)
        self.assertEqual(xr.SpaceVelocityFlags.ANGULAR_VALID_BIT, flags & xr.SpaceVelocityFlags.ANGULAR_VALID_BIT)
        self.assertTrue(xr.SpaceVelocityFlags.ANGULAR_VALID_BIT)
        cflags = xr.SpaceVelocityFlagsCInt(flags.value)  # c_uint64
        self.assertEqual(
            cflags.value,
            (xr.SpaceVelocityFlags.LINEAR_VALID_BIT | xr.SpaceVelocityFlags.ANGULAR_VALID_BIT).value,
        )

        flags = xr.SpaceVelocityFlags.LINEAR_VALID_BIT
        self.assertEqual(flags & xr.SpaceVelocityFlags.LINEAR_VALID_BIT, xr.SpaceVelocityFlags.LINEAR_VALID_BIT)
        self.assertEqual(bool(flags & xr.SpaceVelocityFlags.LINEAR_VALID_BIT), True)
        self.assertEqual(flags & xr.SpaceVelocityFlags.ANGULAR_VALID_BIT, xr.SpaceVelocityFlags.NONE)
        self.assertEqual(bool(flags & xr.SpaceVelocityFlags.ANGULAR_VALID_BIT), False)
        cflags = xr.SpaceVelocityFlagsCInt(flags.value)  # c_uint64
        self.assertEqual(cflags.value, xr.SPACE_VELOCITY_LINEAR_VALID_BIT)

        flags = xr.SpaceVelocityFlags()
        self.assertEqual(flags.value, xr.SpaceVelocityFlags.NONE.value)
        cflags = xr.SpaceVelocityFlagsCInt(flags.value)
        self.assertEqual(0, cflags.value)


if __name__ == '__main__':
    unittest.main()
