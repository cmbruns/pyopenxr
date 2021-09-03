import unittest

import xr


class TestVector3f(unittest.TestCase):
    def setUp(self):
        self.q = xr.Quaternionf()

    def tearDown(self):
        pass

    def test_container(self):
        self.assertEqual(4, len(self.q))
        self.assertEqual(0, self.q[2])
        self.assertEqual("(0.000, 0.000, 0.000, 1.000)", str(self.q))
        self.assertEqual(
            "xr.Quaternionf(0.0, 0.0, 0.0, 1.0)",
            repr(self.q))
        count = 0
        for f in self.q:
            count += 1
        self.assertEqual(4, count)
        self.assertTrue(self.q.y in self.q)
        self.assertTrue(0 in self.q)
        self.assertTrue(1 in self.q)


if __name__ == '__main__':
    unittest.main()
