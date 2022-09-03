import unittest

import xr


class TestDocstring(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_docstring(self):
        doc = xr.raw_functions.xrGetInstanceProcAddr.__doc__
        assert "Gets a function pointer for an OpenXR function" in doc


if __name__ == '__main__':
    unittest.main()
