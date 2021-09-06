import unittest

import xr


class TestExtensionProperties(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_construct(self):
        _ = xr.ExtensionProperties()
        self.assertTrue(True)

    def test_string_equality(self):
        # Extension properties is nearly equivalent to a string
        ep = xr.ExtensionProperties()
        ep.extension_name = b"Some String"
        self.assertEqual(bytes(ep), b"Some String")
        self.assertNotEqual(bytes(ep), b"Some Other String")
        # Sorry equality is not transitive here...
        self.assertNotEqual("Some String", b"Some String")
        self.assertEqual(ep, "Some String")

    def test_type_value(self):
        # The type field must always be StructureType.EXTENSION_PROPERTIES
        # Default construction
        ep = xr.ExtensionProperties()
        self.assertEqual(ep.type, xr.StructureType.EXTENSION_PROPERTIES.value)
        # Array construction
        # Warning: array construction without template values would fail.
        # (That's a bug I suppose)
        arr = (xr.ExtensionProperties * 5)(*([xr.ExtensionProperties()] * 5))
        for p in arr:
            self.assertEqual(p.type, xr.StructureType.EXTENSION_PROPERTIES.value)

    def test_to_string(self):
        ep = xr.ExtensionProperties()
        ep.extension_name = b"Some String"
        self.assertEqual(str(ep), "Some String")


if __name__ == '__main__':
    unittest.main()
