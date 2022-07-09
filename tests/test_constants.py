import unittest

import xr


class TestConstants(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_constants(self):
        # Ensure presence of certain constants
        xr.NO_DURATION
        xr.MIN_HAPTIC_DURATION  # Constant missing in 1.0.2203


if __name__ == '__main__':
    unittest.main()
