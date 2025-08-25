from ctypes import byref, c_void_p, cast, pointer, POINTER
import logging
from typing import Callable

import xr
from .instance_extension import InstanceExtension

xr_logger = logging.getLogger("xr")


def default_user_callback(
        severity: xr.DebugUtilsMessageSeverityFlagsEXT,
        _type: xr.DebugUtilsMessageTypeFlagsEXT,
        data: POINTER(xr.DebugUtilsMessengerCallbackDataEXT),
        _user_data: c_void_p
) -> bool:
    """Redirect OpenXR messages to our python logger."""
    d = data.contents
    xr_logger.log(
        level=log_level_for_severity(severity),
        msg=f"XR.EXT.debug_utils: {d.function_name.decode()}: {d.message.decode()}")
    return True


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


class ExtDebugUtils(InstanceExtension):
    """
    Python bindings for the `XR_EXT_debug_utils` extension.

    This extension provides standardized debugging and logging capabilities for OpenXR applications.
    It allows developers to create debug messengers, assign human-readable names to objects, and
    submit diagnostic messages to the runtime. These features are useful for validation, profiling,
    and runtime introspection.

    The current implementation includes basic support for messenger creation, message submission,
    and object naming. Additional functionality such as label regions and context managers is
    planned but not yet implemented.

    To enable debug utilities, include `"XR_EXT_debug_utils"` in the `enabled_extension_names` list
    when calling :func:`xr.create_instance`.

    See the Khronos registry for full specification:
    https://registry.khronos.org/OpenXR/specs/1.0/man/html/XR_EXT_debug_utils.html
    """

    NAME = "XR_EXT_debug_utils"
    SPEC_VERSION = 5
    VENDOR_TAG = "EXT"

    # TODO: context manager for label regions
    def begin_label_region(self):
        pass

    def create_messenger(
            self,
            # TODO: transform callback in xr.DebugUtilsMessengerCreateInfoEXT constructor
            create_info: xr.DebugUtilsMessengerCreateInfoEXT = xr.DebugUtilsMessengerCreateInfoEXT(
                message_severities=(
                        xr.DebugUtilsMessageSeverityFlagsEXT.VERBOSE_BIT
                        | xr.DebugUtilsMessageSeverityFlagsEXT.INFO_BIT
                        | xr.DebugUtilsMessageSeverityFlagsEXT.WARNING_BIT
                        | xr.DebugUtilsMessageSeverityFlagsEXT.ERROR_BIT
                ),
                message_types=(
                        xr.DebugUtilsMessageTypeFlagsEXT.GENERAL_BIT
                        | xr.DebugUtilsMessageTypeFlagsEXT.VALIDATION_BIT
                        | xr.DebugUtilsMessageTypeFlagsEXT.PERFORMANCE_BIT
                        | xr.DebugUtilsMessageTypeFlagsEXT.CONFORMANCE_BIT
                ),
                user_callback=xr.PFN_xrDebugUtilsMessengerCallbackEXT(default_user_callback),
            )
    ) -> xr.DebugUtilsMessengerEXT:
        # TODO: context manager for messenger
        messenger = xr.DebugUtilsMessengerEXT()
        self._call_raw(
            "xrCreateDebugUtilsMessengerEXT",
            self.instance,
            create_info,
            byref(messenger),
        )
        return messenger

    def destroy_messenger(self, messenger: xr.DebugUtilsMessengerEXT) -> None:
        self._call_raw("xrDestroyDebugUtilsMessengerEXT", messenger)

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

    def set_object_name(self, name_info: xr.DebugUtilsObjectNameInfoEXT) -> None:
        self._call_raw(
            "xrSetDebugUtilsObjectNameEXT",
            self.instance,
            name_info,
        )

    def submit_message(
            self,
            message_severity: xr.DebugUtilsMessageSeverityFlagsEXT,
            message_type: xr.DebugUtilsMessageTypeFlagsEXT,
            callback_data: xr.DebugUtilsMessengerCallbackDataEXT,
    ) -> None:
        self._call_raw(
            "xrSubmitDebugUtilsMessageEXT",
            self.instance,
            message_severity,
            message_type,
            callback_data,
        )


EXT_debug_utils = ExtDebugUtils


__all__ = [
    "EXT_debug_utils",
    "ExtDebugUtils",
]
