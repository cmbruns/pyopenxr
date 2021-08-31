import unittest

import xr


class TestSuccessResult(unittest.TestCase):
    def setUp(self):
        self.exc = xr.Success()

    def test_docstring(self):
        self.assertEqual("Function successfully completed.", self.exc.__doc__)

    def test_construct(self):
        self.assertEqual("Function successfully completed.", str(self.exc))
        self.assertEqual("Bar", str(xr.Success("Bar")))
        xr.exception.raise_on_qualified_success = False
        self.assertFalse(self.exc.is_exception())
        xr.exception.raise_on_qualified_success = True
        self.assertFalse(self.exc.is_exception())

    def test_methods(self):
        self.assertEqual(xr.Result.SUCCESS, self.exc.get_result_enum())
        xr.exception.raise_on_qualified_success = False
        self.assertFalse(self.exc.is_exception())
        xr.exception.raise_on_qualified_success = True
        self.assertFalse(self.exc.is_exception())


class TestTimeoutExpired(unittest.TestCase):
    def setUp(self):
        self.exc = xr.TimeoutExpired()

    def test_docstring(self):
        self.assertEqual(
            "The specified timeout time occurred before the operation could complete.",
            self.exc.__doc__)

    def test_construct(self):
        self.assertEqual(
            "The specified timeout time occurred before the operation could complete.",
            str(self.exc))
        self.assertEqual("Bar", str(xr.TimeoutExpired("Bar")))

    def test_methods(self):
        self.assertEqual(xr.Result.TIMEOUT_EXPIRED, self.exc.get_result_enum())
        xr.exception.raise_on_qualified_success = False
        self.assertFalse(self.exc.is_exception())
        xr.exception.raise_on_qualified_success = True
        self.assertTrue(self.exc.is_exception())


if __name__ == '__main__':
    unittest.main()
