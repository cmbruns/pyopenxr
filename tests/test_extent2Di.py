from ctypes import c_float
import unittest

import xr


class TestExtent2Di(unittest.TestCase):
    def setUp(self):
        self.e = xr.Extent2Di(3, 9)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
