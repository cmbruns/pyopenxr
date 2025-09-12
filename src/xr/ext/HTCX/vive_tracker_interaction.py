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

__all__ = [
    "EXTENSION_NAME",
    "EventDataConnected",
    "Paths",
    "SPEC_VERSION",
    "VENDOR_TAG",
    "enumerate_paths",
]

from ctypes import byref, cast, c_uint32
from typing import Sequence

import xr

EXTENSION_NAME = "XR_HTCX_vive_tracker_interaction"
SPEC_VERSION = 3
VENDOR_TAG = "HTCX"

# Aliases for xr core types
EventDataConnected = xr.EventDataViveTrackerConnectedHTCX
Paths = xr.ViveTrackerPathsHTCX


# TODO: generate 2-call idiom like this
def enumerate_paths(
    instance: xr.Instance,
) -> Sequence[Paths]:
    pfn = cast(
        xr.get_instance_proc_addr(instance, "xrEnumerateViveTrackerPathsHTCX"),
        xr.PFN_xrEnumerateViveTrackerPathsHTCX,
    )
    path_capacity = c_uint32(0)
    result_code = pfn(
        instance,
        0,
        byref(path_capacity),
        None,
    )
    checked = xr.check_result(xr.Result(result_code))
    if checked.is_exception():
        raise checked
    print(path_capacity.value)
    paths = (Paths * path_capacity.value)(*([Paths()] * path_capacity.value))  # noqa
    result_code = pfn(
        instance,
        path_capacity,
        byref(path_capacity),
        paths,
    )
    checked = xr.check_result(xr.Result(result_code))
    if checked.is_exception():
        raise checked
    return paths  # noqa
