import ctypes
import platform
import time
import xr


class TimeFetcher(object):
    """
    Allows cross-platform access to the current time as XrTime
    """
    @staticmethod
    def required_extensions():
        if platform.system() == "Windows":
            return [xr.KHR_WIN32_CONVERT_PERFORMANCE_COUNTER_TIME_EXTENSION_NAME]
        else:
            return [xr.KHR_CONVERT_TIMESPEC_TIME_EXTENSION_NAME]

    def __init__(self, instance: xr.Instance):
        self.instance = instance
        self._pc_time = None
        self._kernel32 = None
        self._pxrConvertWin32PerformanceCounterToTimeKHR = None
        self._timespecTime = None
        if platform.system() == "Windows":
            self._setup_windows()
        else:
            self._setup_linux()

    def _setup_linux(self):
        self._timespecTime = xr.timespec()
        self._pxrConvertTimespecTimeToTimeKHR = ctypes.cast(
            xr.get_instance_proc_addr(
                instance=self.instance,
                name="xrConvertTimespecTimeToTimeKHR",
            ),
            xr.PFN_xrConvertTimespecTimeToTimeKHR,
        )
        self.time_now = self._time_now_linux

    def _setup_windows(self):
        import ctypes.wintypes
        self._pc_time = ctypes.wintypes.LARGE_INTEGER()
        self._kernel32 = ctypes.WinDLL("kernel32")
        self._pxrConvertWin32PerformanceCounterToTimeKHR = ctypes.cast(
            xr.get_instance_proc_addr(
                instance=self.instance,
                name="xrConvertWin32PerformanceCounterToTimeKHR",
            ),
            xr.PFN_xrConvertWin32PerformanceCounterToTimeKHR,
        )
        self.time_now = self._time_now_windows

    def _time_now_linux(self) -> xr.Time:
        time_float = time.clock_gettime(time.CLOCK_MONOTONIC)
        self._timespecTime.tv_sec = int(time_float)
        self._timespecTime.tv_nsec = int((time_float % 1) * 1e9)
        xr_time = xr.Time()
        result = self._pxrConvertTimespecTimeToTimeKHR(
            self.instance,
            ctypes.pointer(self._timespecTime),
            ctypes.byref(xr_time),
        )
        result = xr.check_result(result)
        if result.is_exception():
            raise result
        return xr_time

    def _time_now_windows(self) -> xr.Time:
        xr_time = xr.Time()
        self._kernel32.QueryPerformanceCounter(ctypes.byref(self._pc_time))
        result = self._pxrConvertWin32PerformanceCounterToTimeKHR(
            self.instance,
            ctypes.pointer(self._pc_time),
            ctypes.byref(xr_time),
        )
        result = xr.check_result(result)
        if result.is_exception():
            raise result
        return xr_time

    def time_now(self) -> xr.Time:
        # We should not get here.
        # This method should be automatically overwritten
        raise NotImplementedError


__all__ = [
    "TimeFetcher",
]
