import numpy
import unittest

import xr


class TestQuaternionf(unittest.TestCase):
    def setUp(self):
        self.q = xr.Quaternionf()

    def tearDown(self):
        pass

    def test_container(self):
        self.assertEqual(4, len(self.q))
        self.assertEqual(0, self.q[2])
        self.assertEqual("(x=0.000, y=0.000, z=0.000, w=1.000)", str(self.q))
        self.assertEqual(
            "xr.Quaternionf(x=0.0, y=0.0, z=0.0, w=1.0)",
            repr(self.q))
        count = 0
        for _ in self.q:
            count += 1
        self.assertEqual(4, count)
        self.assertTrue(self.q.y in self.q)
        self.assertTrue(0 in self.q)
        self.assertTrue(1 in self.q)

    def test_numpy(self):
        nq = self.q.as_numpy()
        self.assertEqual(1.0, numpy.linalg.norm(nq))
        self.assertEqual(1.0, numpy.sum(nq))
        self.assertEqual(numpy.float32, nq.dtype)
        # Prove that the numpy array references the internal ctypes data
        self.assertEqual(1, nq[3])
        self.assertEqual(0, nq[0])
        self.q.x = 1
        self.q.w = 0
        self.assertEqual(0, nq[3])
        self.assertEqual(1, nq[0])


if __name__ == '__main__':
    unittest.main()
