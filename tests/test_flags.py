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
        c_flags = xr.SpaceVelocityFlagsCInt(flags.value)  # c_uint64  # noqa
        self.assertEqual(
            c_flags.value,
            (xr.SpaceVelocityFlags.LINEAR_VALID_BIT | xr.SpaceVelocityFlags.ANGULAR_VALID_BIT).value,
        )
        # Using integer constants like xr.SPACE_VELOCITY_LINEAR_VALID_BIT
        self.assertEqual(xr.SpaceVelocityFlags.LINEAR_VALID_BIT, flags & xr.SPACE_VELOCITY_LINEAR_VALID_BIT)
        self.assertEqual(xr.SpaceVelocityFlags.LINEAR_VALID_BIT, xr.SPACE_VELOCITY_LINEAR_VALID_BIT & flags)
        self.assertNotEqual(xr.SpaceVelocityFlags.LINEAR_VALID_BIT, xr.SPACE_VELOCITY_ANGULAR_VALID_BIT & flags)
        self.assertTrue(xr.SPACE_VELOCITY_LINEAR_VALID_BIT)
        self.assertEqual(xr.SpaceVelocityFlags.ANGULAR_VALID_BIT, flags & xr.SPACE_VELOCITY_ANGULAR_VALID_BIT)
        self.assertTrue(xr.SPACE_VELOCITY_ANGULAR_VALID_BIT)
        c_flags = xr.SpaceVelocityFlagsCInt(flags.value)  # c_uint64  # noqa

        flags = xr.SpaceVelocityFlags.LINEAR_VALID_BIT
        self.assertEqual(flags & xr.SpaceVelocityFlags.LINEAR_VALID_BIT, xr.SpaceVelocityFlags.LINEAR_VALID_BIT)
        self.assertEqual(bool(flags & xr.SpaceVelocityFlags.LINEAR_VALID_BIT), True)
        self.assertEqual(flags & xr.SpaceVelocityFlags.ANGULAR_VALID_BIT, xr.SpaceVelocityFlags.NONE)
        self.assertEqual(bool(flags & xr.SpaceVelocityFlags.ANGULAR_VALID_BIT), False)
        c_flags = xr.SpaceVelocityFlagsCInt(flags.value)  # c_uint64  # noqa
        self.assertEqual(c_flags.value, xr.SPACE_VELOCITY_LINEAR_VALID_BIT)

        flags = xr.SpaceVelocityFlags()  # noqa
        self.assertEqual(flags.value, xr.SpaceVelocityFlags.NONE.value)
        c_flags = xr.SpaceVelocityFlagsCInt(flags.value)  # noqa
        self.assertEqual(0, c_flags.value)


if __name__ == '__main__':
    unittest.main()
