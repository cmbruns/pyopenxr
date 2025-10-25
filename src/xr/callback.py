from ctypes import (
    CFUNCTYPE,
    c_uint32,
    c_uint64,
    c_void_p,
    POINTER,
    Structure,
)
from typing import Any, Callable

from .enums import DebugUtilsMessageSeverityFlagsEXT
from .enums import DebugUtilsMessageTypeFlagsEXT

__all__ = [
    "DebugCallbackType",
    "stdout_debug_callback",
    "wrap_debug_callback",
]


# Forward declaration
class DebugUtilsMessengerCallbackDataEXT(Structure):
    pass


Bool32 = c_uint32
Flags64 = c_uint64
DebugUtilsMessageSeverityFlagsEXTCInt = Flags64
DebugUtilsMessageTypeFlagsEXTCInt = Flags64
PFN_xrDebugUtilsMessengerCallbackEXT = CFUNCTYPE(Bool32, DebugUtilsMessageSeverityFlagsEXTCInt, DebugUtilsMessageTypeFlagsEXTCInt, POINTER(DebugUtilsMessengerCallbackDataEXT), c_void_p)


DebugCallbackType = Callable[[
    DebugUtilsMessageSeverityFlagsEXT,
    DebugUtilsMessageTypeFlagsEXT,
    DebugUtilsMessengerCallbackDataEXT,
    c_void_p,
], bool]


def wrap_debug_callback(user_callback: DebugCallbackType, user_data: Any):
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
