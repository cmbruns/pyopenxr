import ctypes
import unittest

import xr


class TestInstanceCreateInfo(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_takes_a_sequence_of_strings(self):
        enabled_api_layer_strings = [
            "XR_APILAYER_LUNARG_api_dump",
        ]
        xr.InstanceCreateInfo(
            enabled_api_layer_names=enabled_api_layer_strings,
        )


if __name__ == '__main__':
    unittest.main()
