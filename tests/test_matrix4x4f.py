import unittest
import numpy

from xr.typedefs import Quaternionf, Fovf, Vector3f
from xr.utils.matrix4x4f import Matrix4x4f, GraphicsAPI  # new NumPy-based version
from xr.utils.matrix4x4f import Matrix4x4f_ctypes       # original ctypes version


class TestMatrix4x4fConsistency(unittest.TestCase):
    @staticmethod
    def assertMatricesEqual(a: numpy.ndarray, b: numpy.ndarray, tol=1e-5):
        numpy.testing.assert_allclose(a, b, rtol=tol, atol=tol)

    def test_create_from_quaternion(self):
        q = Quaternionf(0.1, 0.2, 0.3, 0.9)
        m_new = Matrix4x4f.create_from_quaternion(q)
        m_old = Matrix4x4f_ctypes.create_from_quaternion(q)
        self.assertMatricesEqual(m_new.as_numpy(), m_old.as_numpy())

    def test_create_projection(self):
        args = (GraphicsAPI.OPENGL, -0.8, 0.8, 0.9, -0.9, 0.1, 10.0)
        m_new = Matrix4x4f.create_projection(*args)
        m_old = Matrix4x4f_ctypes.create_projection(*args)
        self.assertMatricesEqual(m_new.as_numpy(), m_old.as_numpy())

    def test_create_projection_infinite(self):
        args = (GraphicsAPI.OPENGL, -0.8, 0.8, 0.9, -0.9, 0.1, 0.05)  # far_z < near_z triggers infinite
        m_new = Matrix4x4f.create_projection(*args)
        m_old = Matrix4x4f_ctypes.create_projection(*args)
        self.assertMatricesEqual(m_new.as_numpy(), m_old.as_numpy())

    def test_create_scale(self):
        m_new = Matrix4x4f.create_scale(1.5, 2.0, 0.5)
        m_old = Matrix4x4f_ctypes.create_scale(1.5, 2.0, 0.5)
        self.assertMatricesEqual(m_new.as_numpy(), m_old.as_numpy())

    def test_create_translation(self):
        m_new = Matrix4x4f.create_translation(3.0, -2.0, 5.0)
        m_old = Matrix4x4f_ctypes.create_translation(3.0, -2.0, 5.0)
        self.assertMatricesEqual(m_new.as_numpy(), m_old.as_numpy())

    def test_create_projection_fov(self):
        fov = Fovf(angle_left=-0.6, angle_right=0.6, angle_up=0.7, angle_down=-0.7)
        m_new = Matrix4x4f.create_projection_fov(GraphicsAPI.OPENGL, fov, 0.1, 100.0)
        m_old = Matrix4x4f_ctypes.create_projection_fov(GraphicsAPI.OPENGL, fov, 0.1, 100.0)
        self.assertMatricesEqual(m_new.as_numpy(), m_old.as_numpy())

    def test_create_translation_rotation_scale(self):
        translation = Vector3f(1.0, 2.0, 3.0)
        rotation = Quaternionf(0.1, 0.2, 0.3, 0.9)
        scale = (1.0, 2.0, 0.5)
        m_new = Matrix4x4f.create_translation_rotation_scale(translation, rotation, scale)
        m_old = Matrix4x4f_ctypes.create_translation_rotation_scale(translation, rotation, scale)
        self.assertMatricesEqual(m_new.as_numpy(), m_old.as_numpy())

    def test_matrix_multiplication(self):
        a = Matrix4x4f.create_scale(2, 2, 2)
        b = Matrix4x4f.create_translation(1, 2, 3)
        m_new = (a @ b)
        a_old = Matrix4x4f_ctypes.create_scale(2, 2, 2)
        b_old = Matrix4x4f_ctypes.create_translation(1, 2, 3)
        m_old = a_old @ b_old
        self.assertMatricesEqual(m_new, m_old.as_numpy())

    def test_invert_rigid_body(self):
        t = Matrix4x4f.create_translation(2.0, 3.0, 4.0)
        r = Matrix4x4f.create_from_quaternion(Quaternionf(0.2, -0.3, 0.1, 0.9))
        m = t @ r
        m_new = m.invert_rigid_body()
        # self.assertMatricesEqual(m @ m_new, numpy.identity(4))
        temp = Matrix4x4f_ctypes(m.as_numpy())
        m_old = temp.invert_rigid_body()
        id_old = temp @ m_old
        self.assertMatricesEqual(id_old.as_numpy(), numpy.identity(4))
        self.assertMatricesEqual((m @ m_new).as_numpy(), numpy.identity(4))
        self.assertMatricesEqual(m_new.as_numpy(), m_old.as_numpy())


if __name__ == '__main__':
    unittest.main()
