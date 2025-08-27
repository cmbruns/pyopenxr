"""
Python bindings for the `XR_HTCX_vive_tracker_interaction` extension.

This extension enables interaction with VIVE Tracker devices via OpenXR.
It defines symbolic paths and event structures for tracker identification and role assignment,
but does not currently expose any functions or structures for direct use in Python.

This stub provides metadata and symbolic access to the extension name for use during
instance creation. Future versions may wrap `xrEnumerateViveTrackerPathsHTCX` or related
functionality if deemed useful.

See the Khronos registry for full specification:
https://registry.khronos.org/OpenXR/specs/1.1/man/html/XR_HTCX_vive_tracker_interaction.html
"""

EXTENSION_NAME = "XR_HTCX_vive_tracker_interaction"
SPEC_VERSION = 3
VENDOR_TAG = "HTCX"


__all__ = [
    "EXTENSION_NAME",
    "SPEC_VERSION",
    "VENDOR_TAG",
]
