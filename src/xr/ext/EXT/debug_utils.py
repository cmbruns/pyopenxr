from ctypes import byref, c_void_p, cast, pointer, POINTER
from functools import wraps
import logging
from typing import Callable

import xr

xr_logger = logging.getLogger("xr")



def xr_entrypoint(name: str, output=None):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            result_int = func(self, *args, **kwargs)
            result_obj = xr.check_result(xr.Result(result_int))
            if result_obj.is_exception():
                raise result_obj
            return kwargs.get(output)
        return wrapper
    return decorator


class DebugUtilsExtension:
    NAME = "XR_EXT_debug_utils"

    def __init__(self, instance):
        self.instance = instance

    # TODO: context manager for label regions
    def begin_label_region(self):
        pass

    def _call_raw(self, func_name, *args, **kwargs):
        pfn = cast(
            xr.get_instance_proc_addr(self.instance, func_name),
            getattr(xr, f"PFN_{func_name}")
        )
        result_int = pfn(*args, **kwargs)
        result_obj = xr.check_result(xr.Result(result_int))
        if result_obj.is_exception():
            raise result_obj

    # @xr_entrypoint("xrCreateDebugUtilsMessengerEXT", output="messenger")
    def create_messenger(
            self,
            create_info: xr.DebugUtilsMessengerCreateInfoEXT,
    ) -> xr.DebugUtilsMessengerEXT:
        pfn = cast(
            xr.get_instance_proc_addr(self.instance, "xrCreateDebugUtilsMessengerEXT"),
            xr.PFN_xrCreateDebugUtilsMessengerEXT,
        )
        messenger = xr.DebugUtilsMessengerEXT()  # TODO: context manager
        result_int = pfn(
            self.instance,
            create_info,
            byref(messenger),
        )
        result_obj = xr.check_result(xr.Result(result_int))
        if result_obj.is_exception():
            raise result_obj
        return messenger

    def default_user_callback(
            self,
            severity: xr.DebugUtilsMessageSeverityFlagsEXT,
            _type: xr.DebugUtilsMessageTypeFlagsEXT,
            data: POINTER(xr.DebugUtilsMessengerCallbackDataEXT),
            _user_data: c_void_p
    ) -> bool:
        """Redirect OpenXR messages to our python logger."""
        d = data.contents
        xr_logger.log(
            level=self.log_level_for_severity(severity),
            msg=f"XR.EXT.debug_utils: {d.function_name.decode()}: {d.message.decode()}")
        return True

    def destroy_messenger(self, messenger: xr.DebugUtilsMessengerEXT) -> None:
        pfn = cast(
            xr.get_instance_proc_addr(
                instance=self.instance,
                name="xrDestroyDebugUtilsMessengerEXT",
            ),
            xr.PFN_xrDestroyDebugUtilsMessengerEXT
        )
        result_int = pfn(
            messenger,
        )
        result_object = xr.check_result(xr.Result(result_int))
        if result_object.is_exception():
            raise result_object

    def foo(
            self,
            message_severities: xr.DebugUtilsMessageSeverityFlagsEXT = (
                    xr.DebugUtilsMessageSeverityFlagsEXT.VERBOSE_BIT
                    | xr.DebugUtilsMessageSeverityFlagsEXT.INFO_BIT
                    | xr.DebugUtilsMessageSeverityFlagsEXT.WARNING_BIT
                    | xr.DebugUtilsMessageSeverityFlagsEXT.ERROR_BIT
            ),
            message_types: xr.DebugUtilsMessageTypeFlagsEXT = (
                xr.DebugUtilsMessageTypeFlagsEXT.GENERAL_BIT
                | xr.DebugUtilsMessageTypeFlagsEXT.VALIDATION_BIT
                | xr.DebugUtilsMessageTypeFlagsEXT.PERFORMANCE_BIT
                | xr.DebugUtilsMessageTypeFlagsEXT.CONFORMANCE_BIT
            ),
            user_callback: Callable[[
                xr.DebugUtilsMessageSeverityFlagsEXT,
                xr.DebugUtilsMessageTypeFlagsEXT,
                POINTER(xr.DebugUtilsMessengerCallbackDataEXT),
                c_void_p,
            ], bool] = default_user_callback,
    ) -> c_void_p:
        create_info = xr.DebugUtilsMessengerCreateInfoEXT(
            message_severities=message_severities,
            message_types=message_types,
            user_callback=xr.PFN_xrDebugUtilsMessengerCallbackEXT(user_callback),
        )
        return cast(pointer(create_info), c_void_p)

    def end_label_region(self):
        pass

    def insert_label(self):
        pass

    @staticmethod
    def log_level_for_severity(severity_flags: xr.DebugUtilsMessageSeverityFlagsEXT) -> int:
        """Convert OpenXR message severities to python logging severities."""
        if severity_flags & xr.DebugUtilsMessageSeverityFlagsEXT.ERROR_BIT:
            return logging.ERROR
        elif severity_flags & xr.DebugUtilsMessageSeverityFlagsEXT.WARNING_BIT:
            return logging.WARNING
        elif severity_flags & xr.DebugUtilsMessageSeverityFlagsEXT.INFO_BIT:
            return logging.INFO
        else:
            return logging.DEBUG

    def set_object_name(self,):
        pass

    def submit_message(
            self,
            message_severity: xr.DebugUtilsMessageSeverityFlagsEXT,
            message_type: xr.DebugUtilsMessageTypeFlagsEXT,
            callback_data: xr.DebugUtilsMessengerCallbackDataEXT,
    ) -> None:
        pfn = cast(
            xr.get_instance_proc_addr(
                instance=self.instance,
                name="xrSubmitDebugUtilsMessageEXT",
            ),
            xr.PFN_xrSubmitDebugUtilsMessageEXT,
        )
        result_int = pfn(
            self.instance,
            message_severity,
            message_type,
            callback_data,
        )
        result_object = xr.check_result(xr.Result(result_int))
        if result_object.is_exception():
            raise result_object


__all__ = [
    "DebugUtilsExtension",
]
