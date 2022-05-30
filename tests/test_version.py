"""
Tests for version numbers

Based on tests at https://github.com/KhronosGroup/OpenXR-Hpp/blob/master/tests/version.cpp
"""

import unittest

import xr


class TestFlags(unittest.TestCase):
    def setUp(self):
        self.version_123 = 0x0001000200000003
        self.version_321 = 0x0003000200000001

    def tearDown(self):
        pass

    def test_version(self):
        v = xr.Version()
        self.assertEqual(0, v.major)
        self.assertEqual(0, v.minor)
        self.assertEqual(0, v.patch)
        #
        v = xr.Version(self.version_123)
        self.assertEqual(1, v.major)
        self.assertEqual(2, v.minor)
        self.assertEqual(3, v.patch)
        #
        v = xr.Version(self.version_321)
        self.assertEqual(3, v.major)
        self.assertEqual(2, v.minor)
        self.assertEqual(1, v.patch)
        self.assertEqual(self.version_123, xr.Version(1, 2, 3).number())


if __name__ == '__main__':
    unittest.main()
