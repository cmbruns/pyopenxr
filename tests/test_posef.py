import unittest

import xr


class TestVector3f(unittest.TestCase):
    def setUp(self):
        self.p = xr.Posef()

    def tearDown(self):
        pass

    def test_posef(self):
        self.assertEqual(1, self.p.orientation.w)


if __name__ == '__main__':
    unittest.main()
