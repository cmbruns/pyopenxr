"""
xr.ext.MND.headless — Headless runtime support

This module provides symbolic access to the `XR_MND_headless` extension, which
enables OpenXR runtimes to operate without presenting rendered frames to a
display. This is useful for automated testing, simulation, or server-side
applications where visual output is unnecessary.

The extension does not define any new functions or structures. Its presence is
indicated by the string `"XR_MND_headless"` in the list of enabled extensions
during instance creation.

To enable headless mode, include `"XR_MND_headless"` in the
`enabled_extension_names` list when calling :func:`xr.create_instance`.

:extension: XR_MND_headless
:seealso: https://registry.khronos.org/OpenXR/specs/1.0/html/xrspec.html#XR_MND_headless
"""
from xr.ext.instance_extension import InstanceExtension


class Headless(InstanceExtension):
    NAME = "XR_MND_headless"


__all__ = [
    "Headless",
]
