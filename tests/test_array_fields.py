import ctypes
import unittest

import xr


class TestArrayFields(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def attempt_use_count_field(self):
        xr.InstanceCreateInfo(enabled_api_layer_count=0)

    def test_takes_a_sequence_of_strings(self):
        xr.InstanceCreateInfo(enabled_api_layer_names=["XR_APILAYER_LUNARG_api_dump", ])
        # Length field is now supported but seldom used
        # self.assertRaises(TypeError, self.attempt_missing_count_field)
        self.attempt_use_count_field()

    def test_frame_end_info(self):
        xr.FrameEndInfo(layers=[])


if __name__ == '__main__':
    unittest.main()
