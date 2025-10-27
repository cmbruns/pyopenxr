from ctypes import (
    c_void_p,
    POINTER,
    Structure,
)
import logging
from typing import Any, Callable

from .enums import DebugUtilsMessageSeverityFlagsEXT, DebugUtilsMessageTypeFlagsEXT

__all__ = [
    "DebugCallbackType",
    "logging_debug_callback",
    "stdout_debug_callback",
    "wrap_debug_callback",
]


# Forward declaration
class DebugUtilsMessengerCallbackDataEXT(Structure):
    pass


DebugCallbackType = Callable[[
    DebugUtilsMessageSeverityFlagsEXT,
    DebugUtilsMessageTypeFlagsEXT,
    DebugUtilsMessengerCallbackDataEXT,
    Any,
], bool]


def log_level_for_severity(severity_flags: DebugUtilsMessageSeverityFlagsEXT) -> int:
    """
    Convert OpenXR message severities to Python logging levels.

    :param severity_flags: Bitmask of message severity flags.
    :type severity_flags: xr.DebugUtilsMessageSeverityFlagsEXT
    :returns: One of logging.DEBUG, INFO, WARNING, or ERROR.
    """
    if severity_flags & DebugUtilsMessageSeverityFlagsEXT.ERROR_BIT:
        return logging.ERROR
    if severity_flags & DebugUtilsMessageSeverityFlagsEXT.WARNING_BIT:
        return logging.WARNING
    if severity_flags & DebugUtilsMessageSeverityFlagsEXT.INFO_BIT:
        return logging.INFO
    return logging.DEBUG


def logging_debug_callback(
        severity: DebugUtilsMessageSeverityFlagsEXT,
        _type_flags: DebugUtilsMessageTypeFlagsEXT,
        callback_data: DebugUtilsMessengerCallbackDataEXT,
        logger: logging.Logger,
) -> bool:
    """Redirect OpenXR messages to a python logger."""
    logger.log(
        level=log_level_for_severity(severity),
        msg=f"{callback_data.function_name}: {callback_data.message}")
    return False


def stdout_debug_callback(
        severity: DebugUtilsMessageSeverityFlagsEXT,
        type_flags: DebugUtilsMessageTypeFlagsEXT,
        callback_data: DebugUtilsMessengerCallbackDataEXT,
        _user_data: c_void_p,
) -> bool:
    """
    Default diagnostic callback for `XR_EXT_debug_utils`.

    This function is invoked by the OpenXR runtime when a debug message is emitted.
    It prints the message to standard output, including severity, type, and function name.

    This is a minimal implementation intended primarily as a reference or starting point
    for client applications. Users are encouraged to implement their own callback to
    integrate with logging frameworks, telemetry systems, or custom filtering logic.

    :param severity: Bitmask of message severity flags.
    :type severity: xr.DebugUtilsMessageSeverityFlagsEXT
    :param type_flags: Bitmask of message type flags.
    :type type_flags: xr.DebugUtilsMessageTypeFlagsEXT
    :param callback_data: Pointer to a populated `DebugUtilsMessengerCallbackDataEXT` structure.
    :type callback_data: ctypes.POINTER(xr.DebugUtilsMessengerCallbackDataEXT)
    :param _user_data: Optional user data passed during messenger creation. Unused by default.
    :type _user_data: ctypes.c_void_p

    :seealso: :class:`xr.DebugUtilsMessengerCreateInfoEXT`, :class:`xr.DebugUtilsMessengerEXT`
    """

    message = callback_data.message
    func_name = callback_data.function_name
    print(f"[XR DEBUG] Severity={severity} Type={type_flags} Message={message} Function={func_name}")
    return False  # important!


def wrap_debug_callback(
        user_callback: DebugCallbackType,
        user_data: Any,
) -> "PFN_xrDebugUtilsMessengerCallbackEXT":
    # Just-in-time import to avoid circular import
    from .typedefs import PFN_xrDebugUtilsMessengerCallbackEXT, DebugUtilsMessengerCallbackDataEXT

    def _shim(
            severity: int,
            type_flags: int,
            callback_data_ptr: POINTER(DebugUtilsMessengerCallbackDataEXT),
            _user_data_ptr: c_void_p,
    ):
        try:
            severity_enum = DebugUtilsMessageSeverityFlagsEXT(severity)
            type_enum = DebugUtilsMessageTypeFlagsEXT(type_flags)
            callback_data = callback_data_ptr.contents
            return user_callback(severity_enum, type_enum, callback_data, user_data)
        except Exception as e:
            print(f"Exception in debug callback: {e}")
            return False
    return PFN_xrDebugUtilsMessengerCallbackEXT(_shim)
