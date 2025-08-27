"""
Python bindings for the `XR_EXT_debug_utils` extension.

This extension provides standardized debugging and logging capabilities for OpenXR applications.
It allows developers to create debug messengers, assign human-readable names to objects, and
submit diagnostic messages to the runtime. These features are useful for validation, profiling,
and runtime introspection.

To enable debug utilities, include `"XR_EXT_debug_utils"` in your
`enabled_extension_names` when calling :func:`xr.create_instance`.

See the Khronos registry for full specification:
https://registry.khronos.org/OpenXR/specs/1.0/man/html/XR_EXT_debug_utils.html
"""

from ctypes import byref, c_void_p, cast, POINTER
import logging
from typing import Optional

import xr

xr_logger = logging.getLogger("xr")

EXTENSION_NAME = "XR_EXT_debug_utils"
SPEC_VERSION = 5
VENDOR_TAG = "EXT"

# Aliases for core types
MessageSeverityFlags = xr.DebugUtilsMessageSeverityFlagsEXT
Messenger = xr.DebugUtilsMessengerEXT
MessengerCallbackData = xr.DebugUtilsMessengerCallbackDataEXT
MessengerCreateInfo = xr.DebugUtilsMessengerCreateInfoEXT
Label = xr.DebugUtilsLabelEXT
ObjectNameInfo = xr.DebugUtilsObjectNameInfoEXT


def _default_user_callback(
    severity: int,
    _type_flags: int,
    callback_data: POINTER(MessengerCallbackData),
    _user_data: c_void_p
) -> bool:
    """
    Minimal default debug callback for `XR_EXT_debug_utils`.

    Redirects all messages into the Python `xr` logger at a level
    corresponding to the message severity. Clients should override
    this and install their own handler for structured logging,
    custom filtering, or integration with telemetry.

    :param severity: Bitmask of message severity flags.
    :param _type_flags: Bitmask of message type flags (unused here).
    :param callback_data: Pointer to a populated `MessengerCallbackData` structure.
    :param _user_data: User-data pointer passed through the create_info (unused).
    :returns: Always returns True to indicate the message was handled.

    :see: https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrCreateDebugUtilsMessengerEXT.html
    """
    data = callback_data.contents
    xr_logger.log(
        level=log_level_for_severity(MessageSeverityFlags(severity)),
        msg=f"XR.EXT.debug_utils: {data.function_name.decode()}: {data.message.decode()}"
    )
    return True


def log_level_for_severity(severity_flags: MessageSeverityFlags) -> int:
    """
    Convert OpenXR message severities to Python logging levels.

    :param severity_flags: Bitmask of message severity flags.
    :type severity_flags: xr.DebugUtilsMessageSeverityFlagsEXT
    :returns: One of logging.DEBUG, INFO, WARNING, or ERROR.
    """
    if severity_flags & MessageSeverityFlags.ERROR_BIT:
        return logging.ERROR
    if severity_flags & MessageSeverityFlags.WARNING_BIT:
        return logging.WARNING
    if severity_flags & MessageSeverityFlags.INFO_BIT:
        return logging.INFO
    return logging.DEBUG


def session_begin_label_region(
    session: xr.Session,
    label_info: Label
) -> None:
    """
    Begin a labeled debug region in the specified session.

    This marks the start of a profiling or annotation region in the runtime.

    :param instance: The OpenXR instance.
    :type instance: xr.Instance
    :param session: The OpenXR session.
    :type session: xr.Session
    :param label_info: A `DebugUtilsLabelEXT` structure describing the region.
    :type label_info: xr.DebugUtilsLabelEXT

    :raises xr.FunctionUnsupportedError: If the function is unavailable.
    :raises xr.HandleInvalidError: If `session` is not a valid handle.
    :raises xr.InstanceLostError: If the session’s instance has been lost.

    :see: https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrSessionBeginDebugUtilsLabelRegionEXT.html
    """
    pfn = cast(
        xr.get_instance_proc_addr(session.instance, "xrSessionBeginDebugUtilsLabelRegionEXT"),
        xr.PFN_xrSessionBeginDebugUtilsLabelRegionEXT
    )
    result = pfn(session, byref(label_info))
    checked = xr.check_result(xr.Result(result))
    if checked.is_exception():
        raise checked


def session_end_label_region(
    session: xr.Session
) -> None:
    """
    End the current labeled debug region in the specified session.

    :param instance: The OpenXR instance.
    :type instance: xr.Instance
    :param session: The OpenXR session.
    :type session: xr.Session

    :raises xr.FunctionUnsupportedError: If the function is unavailable.
    :raises xr.HandleInvalidError: If `session` is not a valid handle.
    :raises xr.InstanceLostError: If the session’s instance has been lost.

    :see: https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrSessionEndDebugUtilsLabelRegionEXT.html
    """
    pfn = cast(
        xr.get_instance_proc_addr(session.instance, "xrSessionEndDebugUtilsLabelRegionEXT"),
        xr.PFN_xrSessionEndDebugUtilsLabelRegionEXT
    )
    result = pfn(session)
    checked = xr.check_result(xr.Result(result))
    if checked.is_exception():
        raise checked


def session_insert_label(
    session: xr.Session,
    label_info: Label
) -> None:
    """
    Insert a single debug label into the command stream.

    Use this for point-in-time annotations rather than begin/end regions.

    :param instance: The OpenXR instance.
    :type instance: xr.Instance
    :param session: The OpenXR session.
    :type session: xr.Session
    :param label_info: A `DebugUtilsLabelEXT` structure with the label text.
    :type label_info: xr.DebugUtilsLabelEXT

    :raises xr.FunctionUnsupportedError: If the function is unavailable.
    :raises xr.HandleInvalidError: If `session` is not a valid handle.
    :raises xr.InstanceLostError: If the session’s instance has been lost.

    :see: https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrSessionInsertDebugUtilsLabelEXT.html
    """
    pfn = cast(
        xr.get_instance_proc_addr(session.instance, "xrSessionInsertDebugUtilsLabelEXT"),
        xr.PFN_xrSessionInsertDebugUtilsLabelEXT
    )
    result = pfn(session, byref(label_info))
    checked = xr.check_result(xr.Result(result))
    if checked.is_exception():
        raise checked


def create_messenger(
    instance: xr.Instance,
    create_info: Optional[MessengerCreateInfo] = None
) -> Messenger:
    """
    Create a debug messenger for the given instance.

    Thin wrapper over `xr.DebugUtilsMessengerEXT`. If `create_info` is omitted,
    defaults will enable all severities/types and route messages to the Python logger.

    :param instance: The OpenXR instance.
    :type instance: xr.Instance
    :param create_info: Optional create-info descriptor.
    :type create_info: xr.DebugUtilsMessengerCreateInfoEXT or None

    :returns: A new `DebugUtilsMessengerEXT` handle.
    :rtype: xr.DebugUtilsMessengerEXT

    :raises xr.FunctionUnsupportedError: If the extension isn’t enabled.
    :raises xr.ValidationFailureError: If parameters are rejected by the runtime.
    :raises xr.RuntimeFailureError: On internal runtime errors.
    :raises xr.OutOfMemoryError: If allocation fails.
    :raises xr.LimitReachedError: If no more messengers can be created.

    :see: https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrCreateDebugUtilsMessengerEXT.html
    """
    return Messenger(instance, create_info)


def destroy_messenger(
    messenger: Messenger
) -> None:
    """
    Destroy a debug messenger, releasing its native resources.

    :param instance: The OpenXR instance.
    :type instance: xr.Instance
    :param messenger: The messenger to destroy.
    :type messenger: xr.DebugUtilsMessengerEXT

    :raises xr.FunctionUnsupportedError: If the function is unavailable.
    :raises xr.HandleInvalidError: If `messenger` is not a valid handle.

    :see: https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrDestroyDebugUtilsMessengerEXT.html
    """
    pfn = cast(
        xr.get_instance_proc_addr(messenger.instance, "xrDestroyDebugUtilsMessengerEXT"),
        xr.PFN_xrDestroyDebugUtilsMessengerEXT
    )
    result = pfn(messenger)
    checked = xr.check_result(xr.Result(result))
    if checked.is_exception():
        raise checked


def set_object_name(
    instance: xr.Instance,
    name_info: ObjectNameInfo
) -> None:
    """
    Assign a human-readable name to an OpenXR object.

    :param instance: The OpenXR instance.
    :type instance: xr.Instance
    :param name_info: A `DebugUtilsObjectNameInfoEXT` structure.
    :type name_info: xr.DebugUtilsObjectNameInfoEXT

    :raises xr.FunctionUnsupportedError: If the function is unavailable.
    :raises xr.HandleInvalidError: If `name_info.objectHandle` is invalid.

    :see: https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrSetDebugUtilsObjectNameEXT.html
    """
    pfn = cast(
        xr.get_instance_proc_addr(instance, "xrSetDebugUtilsObjectNameEXT"),
        xr.PFN_xrSetDebugUtilsObjectNameEXT
    )
    result = pfn(instance, byref(name_info))
    checked = xr.check_result(xr.Result(result))
    if checked.is_exception():
        raise checked


def submit_message(
    instance: xr.Instance,
    message_severity: MessageSeverityFlags,
    message_type: xr.DebugUtilsMessageTypeFlagsEXT,
    callback_data: MessengerCallbackData
) -> None:
    """
    Submit a user-generated debug message to the runtime.

    :param instance: The OpenXR instance.
    :type instance: xr.Instance
    :param message_severity: Severity bitmask for this message.
    :type message_severity: xr.DebugUtilsMessageSeverityFlagsEXT
    :param message_type: Type bitmask for this message.
    :type message_type: xr.DebugUtilsMessageTypeFlagsEXT
    :param callback_data: Prepopulated callback data structure.
    :type callback_data: xr.DebugUtilsMessengerCallbackDataEXT

    :raises xr.FunctionUnsupportedError: If the function is unavailable.
    :raises xr.RuntimeFailureError: On internal runtime errors.
    :raises xr.OutOfMemoryError: If allocation fails.

    :see: https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrSubmitDebugUtilsMessageEXT.html
    """
    pfn = cast(
        xr.get_instance_proc_addr(instance, "xrSubmitDebugUtilsMessageEXT"),
        xr.PFN_xrSubmitDebugUtilsMessageEXT
    )
    result_code = pfn(instance, message_severity, message_type, callback_data)
    checked = xr.check_result(xr.Result(result_code))
    if checked.is_exception():
        raise checked


__all__ = [
    "EXTENSION_NAME",
    "SPEC_VERSION",
    "VENDOR_TAG",
    "MessageSeverityFlags",
    "Messenger",
    "MessengerCallbackData",
    "MessengerCreateInfo",
    "Label",
    "ObjectNameInfo",
    "session_begin_label_region",
    "session_end_label_region",
    "session_insert_label",
    "create_messenger",
    "destroy_messenger",
    "set_object_name",
    "submit_message",
]
