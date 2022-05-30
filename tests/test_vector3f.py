from ctypes import c_float
import unittest

import xr


class TestVector3f(unittest.TestCase):
    def setUp(self):
        self.v = xr.Vector3f(1.34, -9.6, 17.44444444442)

    def tearDown(self):
        pass

    def test_container(self):
        self.assertEqual(3, len(self.v))
        self.assertAlmostEqual(17.44444444442, self.v[2], 5)
        self.assertEqual("(x=1.340, y=-9.600, z=17.444)", str(self.v))
        self.assertEqual(
            "xr.Vector3f(x=1.340000033378601, y=-9.600000381469727, z=17.44444465637207)",
            repr(self.v))
        count = 0
        for _ in self.v:
            count += 1
        self.assertEqual(3, count)
        self.assertTrue(self.v.y in self.v)
        self.assertTrue(c_float(1.340).value in self.v)

    def test_constructor(self):
        v = xr.Vector3f()
        self.assertTrue(v.x == v.y == v.z == 0)

    def test_sequence(self):
        self.assertEqual(3, len(self.v))

    def test_setter(self):
        v2 = xr.Vector3f(3, 2, 1)
        v2[:] = [9, 8, 7]
        self.assertEqual(v2.z, 7)


if __name__ == '__main__':
    unittest.main()
