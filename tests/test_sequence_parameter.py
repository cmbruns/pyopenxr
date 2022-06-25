from ctypes import byref, pointer
import unittest

import xr


class TestSequenceParameter(unittest.TestCase):
    """
    Ways to construct a sequence parameter:
      * None: (default value) results in an empty sequence
      * Pointer with count (like in C)
      * ctypes array
      * other python sequence
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sizes(self):
        # Default construction
        self.assertEqual(0, len(xr.CompositionLayerProjection().views))
        self.assertEqual(0, xr.CompositionLayerProjection().view_count)
        # construct from None (should be same as default)
        self.assertEqual(0, len(xr.CompositionLayerProjection(views=None).views))
        self.assertEqual(0, xr.CompositionLayerProjection(views=None).view_count)
        # construct from pointer
        cpv = xr.CompositionLayerProjectionView()  # Element
        cpv.pose.orientation.w = 3  # Unusual value
        clp = xr.CompositionLayerProjection(
            view_count=1,
            views=pointer(cpv),
        )
        self.assertEqual(1, len(clp.views))
        self.assertEqual(1, clp.view_count)
        self.assertEqual(3, clp.views[0].pose.orientation.w)
        # construct from single element
        clp = xr.CompositionLayerProjection(
            views=cpv,
        )
        self.assertEqual(1, len(clp.views))
        self.assertEqual(1, clp.view_count)
        self.assertEqual(3, clp.views[0].pose.orientation.w)
        # construct from ctypes array
        clp = xr.CompositionLayerProjection(
            views=(xr.CompositionLayerProjectionView * 5)())
        self.assertEqual(5, len(clp.views))
        self.assertEqual(5, clp.view_count)
        # construct from a python sequence
        clp = xr.CompositionLayerProjection(
            views=[
                xr.CompositionLayerProjectionView(),
                xr.CompositionLayerProjectionView(),
            ]
        )
        self.assertEqual(2, len(clp.views))
        self.assertEqual(2, clp.view_count)
