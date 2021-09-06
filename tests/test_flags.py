import unittest

import xr


class TestFlags(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_bool(self):
        flags = xr.SPACE_VELOCITY_LINEAR_VALID_BIT  # TODO


if __name__ == '__main__':
    unittest.main()
