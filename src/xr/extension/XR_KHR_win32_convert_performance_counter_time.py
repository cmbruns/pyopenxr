"""
Level 3 API for pyopenxr instance extension XR_KHR_win32_convert_performance_counter_time
https://registry.khronos.org/OpenXR/specs/1.0/man/html/XR_KHR_win32_convert_performance_counter_time.html
"""

import ctypes.wintypes
from ctypes import CFUNCTYPE, POINTER
from ..enums import Result
from ..exception import check_result, FunctionUnsupportedError
from ..functions import get_instance_proc_addr
from ..typedefs import Instance, Time


_extension_name = "XR_KHR_win32_convert_performance_counter_time"
_PFN_xrConvertWin32PerformanceCounterToTimeKHR = CFUNCTYPE(Result.ctype(), Instance, POINTER(ctypes.wintypes.LARGE_INTEGER), POINTER(Time))
_PFN_xrConvertTimeToWin32PerformanceCounterKHR = CFUNCTYPE(Result.ctype(), Instance, Time, POINTER(ctypes.wintypes.LARGE_INTEGER))


def convert_time_to_win32_performance_counter_khr(instance: Instance, xr_time: Time) -> ctypes.wintypes.LARGE_INTEGER:
    perf_counter = ctypes.wintypes.LARGE_INTEGER()
    try:
        pfn = get_instance_proc_addr(
            instance,
            "xrConvertTimeToWin32PerformanceCounterKHR",
        )
    except FunctionUnsupportedError as exc:
        raise FunctionUnsupportedError(f"Instance extension {_extension_name} must be enabled to use this function") from exc
    _pxrConvertTimeToWin32PerformanceCounterKHR = ctypes.cast(
        pfn,
        _PFN_xrConvertTimeToWin32PerformanceCounterKHR,
    )
    result = _pxrConvertTimeToWin32PerformanceCounterKHR(
        instance,
        xr_time,
        ctypes.byref(perf_counter),
    )
    result = check_result(result)
    if result.is_exception():
        raise result
    return perf_counter


def convert_win32_performance_counter_to_time_khr(
        instance: Instance,
        performance_counter: ctypes.wintypes.LARGE_INTEGER,
) -> Time:
    xr_time = Time()
    try:
        pfn = get_instance_proc_addr(
            instance,
            "xrConvertWin32PerformanceCounterToTimeKHR",
        )
    except FunctionUnsupportedError as exc:
        raise FunctionUnsupportedError(f"Instance extension {_extension_name} must be enabled to use this function") from exc
    _pxrConvertWin32PerformanceCounterToTimeKHR = ctypes.cast(
        pfn,
        _PFN_xrConvertWin32PerformanceCounterToTimeKHR,
    )
    result = _pxrConvertWin32PerformanceCounterToTimeKHR(
        instance,
        ctypes.pointer(performance_counter),
        ctypes.byref(xr_time),
    )
    result = check_result(result)
    if result.is_exception():
        raise result
    return xr_time


__all__ = [
    "convert_time_to_win32_performance_counter_khr",
    "convert_win32_performance_counter_to_time_khr",
]
