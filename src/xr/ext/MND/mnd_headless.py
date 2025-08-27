from xr.ext.instance_extension import InstanceExtension


class MndHeadless(InstanceExtension):
    """
    Python bindings for the `XR_MND_headless` extension.

    This extension enables OpenXR runtimes to operate without presenting rendered frames
    to a display. It is useful for automated testing, simulation, or server-side applications
    where visual output is unnecessary.

    The extension does not define any new functions or structures. Its presence is indicated
    by the string `"XR_MND_headless"` in the list of enabled extensions during instance creation.

    To enable headless mode, include `"XR_MND_headless"` in the `enabled_extension_names` list
    when calling :func:`xr.create_instance`.

    See the Khronos registry for full specification:
    https://registry.khronos.org/OpenXR/specs/1.0/html/xrspec.html#XR_MND_headless
    """

    NAME = "XR_MND_headless"
    SPEC_VERSION = 2
    VENDOR_TAG = "MND"


MND_headless = MndHeadless


__all__ = [
    "MND_headless",
    "MndHeadless",
]
