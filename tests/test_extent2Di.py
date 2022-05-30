from ctypes import c_float
import unittest

import xr


class TestExtent2Di(unittest.TestCase):
    def setUp(self):
        self.e = xr.Extent2Di(3, 9)

    def tearDown(self):
        pass

    def test_setter(self):
        e = xr.Extent2Di(2, 1)
        e[:] = [100, 99]
        self.assertEqual(e.height, 99)


if __name__ == '__main__':
    unittest.main()
