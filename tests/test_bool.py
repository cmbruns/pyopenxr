import unittest

import xr


class TestBool(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_bool(self):
        self.assertTrue(True)
        self.assertFalse(False)
        self.assertTrue(xr.TRUE)
        self.assertFalse(xr.FALSE)
        self.assertTrue(xr.Bool32(True))
        self.assertFalse(xr.Bool32(False))


if __name__ == '__main__':
    unittest.main()
