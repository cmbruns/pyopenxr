import os
import unittest

import xr


class TestApiLayers(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_api_layers(self):
        # make sure packaged api layers loaded
        self.assertGreaterEqual(len(xr.enumerate_api_layer_properties()), 2)
        # but not when environment is cleared
        del os.environ["XR_API_LAYER_PATH"]
        self.assertEqual(len(xr.enumerate_api_layer_properties()), 0)
        # but it can be restored
        xr.expose_packaged_api_layers()
        self.assertGreaterEqual(len(xr.enumerate_api_layer_properties()), 2)


if __name__ == '__main__':
    unittest.main()
