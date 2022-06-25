import unittest

import xr


class TestCreateInfo(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_default_constructible(self):
        xr.ActionCreateInfo()
        xr.ActionSetCreateInfo()
        xr.ActionSpaceCreateInfo()
        xr.InstanceCreateInfo()
        xr.ReferenceSpaceCreateInfo()
        xr.SessionCreateInfo()
        xr.SwapchainCreateInfo()

    def test_default_constructible2(self):
        xr.create_instance()  # But *not* TypeError


if __name__ == '__main__':
    unittest.main()
