import unittest

import xr


# TODO:
#  * string comparison
#  * __str__ and __repr__
#  * field values
#  * array construction

class TestExtensionProperties(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_construct(self):
        ep = xr.ExtensionProperties()
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
