import unittest


class TestEgl(unittest.TestCase):
    def test_basic_synopsis(self):
        try:
            from OpenGL import EGL
        except AttributeError:
            return  # Windows does not have EGL
        from xr.utils.gl import egl_util
        context_provider = egl_util.EGLOffscreenContextProvider()
        with context_provider.scope():
            _binding = egl_util.EGLGraphicsBinding(context_provider)


if __name__ == '__main__':
    unittest.main()
