import ctypes.wintypes
from ..extension.XR_KHR_win32_convert_performance_counter_time import convert_win32_performance_counter_to_time_khr
from ..typedefs import Instance, Time


kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)


def xr_time_now(instance: Instance) -> Time:
    """
    :param instance:
    :return:
    """
    performance_counter = ctypes.wintypes.LARGE_INTEGER()
    kernel32.QueryPerformanceCounter(ctypes.byref(performance_counter))
    return convert_win32_performance_counter_to_time_khr(instance, performance_counter)


__all__ = [
    "xr_time_now",
]
