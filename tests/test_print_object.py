import unittest

import xr


class TestPrintObject(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_print_object(self):
        apl = xr.ApiLayerProperties()
        print(apl)


if __name__ == '__main__':
    unittest.main()
