"""
Python bindings for the `XR_EXT_debug_utils` instance extension.

This module provides Python wrappers for OpenXR functions defined in the
`XR_EXT_debug_utils` specification. These wrappers expose runtime diagnostics,
object naming, and other extension-specific features.

To enable this extension, include `"XR_EXT_debug_utils"` in your
`enabled_extension_names` when calling :func:`xr.create_instance`.

See the Khronos registry for full specification:
https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_debug_utils
"""

__all__ = [
    "EXTENSION_NAME",
    "Label",
    "MessageSeverityFlags",
    "MessageTypeFlags",
    "Messenger",
    "MessengerCallbackData",
    "MessengerCreateInfo",
    "ObjectNameInfo",
    "SPEC_VERSION",
    "VENDOR_TAG",
    "create_messenger",
    "destroy_messenger",
    "session_begin_label_region",
    "session_end_label_region",
    "session_insert_label",
    "set_object_name",
    "submit_message",
]

from ctypes import byref, cast

import xr

EXTENSION_NAME = "XR_EXT_debug_utils"
SPEC_VERSION = 5
VENDOR_TAG = "EXT"

# Aliases for xr core types
Label = xr.DebugUtilsLabelEXT
MessageSeverityFlags = xr.DebugUtilsMessageSeverityFlagsEXT
MessageTypeFlags = xr.DebugUtilsMessageTypeFlagsEXT
Messenger = xr.DebugUtilsMessengerEXT
MessengerCallbackData = xr.DebugUtilsMessengerCallbackDataEXT
MessengerCreateInfo = xr.DebugUtilsMessengerCreateInfoEXT
ObjectNameInfo = xr.DebugUtilsObjectNameInfoEXT


def create_messenger(
    instance: xr.Instance,
    create_info: MessengerCreateInfo = MessengerCreateInfo(),
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
    pfn = cast(
        xr.get_instance_proc_addr(instance, "xrCreateDebugUtilsMessengerEXT"),
        xr.PFN_xrCreateDebugUtilsMessengerEXT,
    )        
    messenger = Messenger()
    messenger.instance = instance
    messenger._callback = create_info.user_callback  # Tie lifetime to messenger object
    result_code = pfn(
        instance,
        byref(create_info),
        byref(messenger),
    )
    checked = xr.check_result(xr.Result(result_code))
    if checked.is_exception():
        raise checked
    return messenger


def destroy_messenger(
    messenger: Messenger,
) -> None:
    """
    Destroy a debug messenger, releasing its native resources.

    :param messenger: The messenger to destroy.
    :type messenger: xr.DebugUtilsMessengerEXT

    :raises xr.FunctionUnsupportedError: If the function is unavailable.
    :raises xr.HandleInvalidError: If `messenger` is not a valid handle.

    :see: https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrDestroyDebugUtilsMessengerEXT.html
    """
    pfn = cast(
        xr.get_instance_proc_addr(messenger.instance, "xrDestroyDebugUtilsMessengerEXT"),
        xr.PFN_xrDestroyDebugUtilsMessengerEXT,
    )        
    result_code = pfn(
        messenger,
    )
    checked = xr.check_result(xr.Result(result_code))
    if checked.is_exception():
        raise checked


def session_begin_label_region(
    session: xr.Session,
    label_info: Label = Label(),
) -> None:
    """
    Begin a labeled debug region in the specified session.

    This marks the start of a profiling or annotation region in the runtime.

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
        xr.PFN_xrSessionBeginDebugUtilsLabelRegionEXT,
    )        
    result_code = pfn(
        session,
        byref(label_info),
    )
    checked = xr.check_result(xr.Result(result_code))
    if checked.is_exception():
        raise checked


def session_end_label_region(
    session: xr.Session,
) -> None:
    """
    End the current labeled debug region in the specified session.

    :param session: The OpenXR session.
    :type session: xr.Session

    :raises xr.FunctionUnsupportedError: If the function is unavailable.
    :raises xr.HandleInvalidError: If `session` is not a valid handle.
    :raises xr.InstanceLostError: If the session’s instance has been lost.

    :see: https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrSessionEndDebugUtilsLabelRegionEXT.html
    """
    pfn = cast(
        xr.get_instance_proc_addr(session.instance, "xrSessionEndDebugUtilsLabelRegionEXT"),
        xr.PFN_xrSessionEndDebugUtilsLabelRegionEXT,
    )        
    result_code = pfn(
        session,
    )
    checked = xr.check_result(xr.Result(result_code))
    if checked.is_exception():
        raise checked


def session_insert_label(
    session: xr.Session,
    label_info: Label = Label(),
) -> None:
    """
    Insert a single debug label into the command stream.

    Use this for point-in-time annotations rather than begin/end regions.

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
        xr.PFN_xrSessionInsertDebugUtilsLabelEXT,
    )        
    result_code = pfn(
        session,
        byref(label_info),
    )
    checked = xr.check_result(xr.Result(result_code))
    if checked.is_exception():
        raise checked


def set_object_name(
    instance: xr.Instance,
    name_info: ObjectNameInfo = ObjectNameInfo(),
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
        xr.PFN_xrSetDebugUtilsObjectNameEXT,
    )        
    result_code = pfn(
        instance,
        byref(name_info),
    )
    checked = xr.check_result(xr.Result(result_code))
    if checked.is_exception():
        raise checked


def submit_message(
    instance: xr.Instance,
    message_severity: MessageSeverityFlags,
    message_types: MessageTypeFlags,
    callback_data: MessengerCallbackData = MessengerCallbackData(),
) -> None:
    """
    Submit a user-generated debug message to the runtime.

    :param instance: The OpenXR instance.
    :type instance: xr.Instance
    :param message_severity: Severity bitmask for this message.
    :type message_severity: xr.DebugUtilsMessageSeverityFlagsEXT
    :param message_types: Type bitmask for this message.
    :type message_types: xr.DebugUtilsMessageTypeFlagsEXT
    :param callback_data: Prepopulated callback data structure.
    :type callback_data: xr.DebugUtilsMessengerCallbackDataEXT

    :raises xr.FunctionUnsupportedError: If the function is unavailable.
    :raises xr.RuntimeFailureError: On internal runtime errors.
    :raises xr.OutOfMemoryError: If allocation fails.

    :see: https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrSubmitDebugUtilsMessageEXT.html
    """
    pfn = cast(
        xr.get_instance_proc_addr(instance, "xrSubmitDebugUtilsMessageEXT"),
        xr.PFN_xrSubmitDebugUtilsMessageEXT,
    )        
    result_code = pfn(
        instance,
        message_severity,
        message_types,
        byref(callback_data),
    )
    checked = xr.check_result(xr.Result(result_code))
    if checked.is_exception():
        raise checked
