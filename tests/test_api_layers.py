import os
import unittest

import xr


class TestApiLayers(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_api_layers(self):
        # clear dynamic api layer folders
        previous = os.environ.pop("XR_API_LAYER_PATH", None)
        if len(xr.enumerate_api_layer_properties()) == 0:  # No layers are available
            xr.expose_packaged_api_layers()
            # self.assertGreaterEqual(len(xr.enumerate_api_layer_properties()), 2)
        # restore environment
        if previous is not None:
            os.environ["XR_API_LAYER_PATH"] = previous


if __name__ == '__main__':
    unittest.main()
