import unittest


class TestCtypesPointer(unittest.TestCase):
    def test_import(self):
        from ctypes import pointer  # noqa


if __name__ == '__main__':
    unittest.main()
