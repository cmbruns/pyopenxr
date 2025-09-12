from contextlib import ExitStack
from ctypes import c_void_p
import logging

import xr
from xr.ext.EXT import debug_utils


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def log_level_for_severity(severity_flags: debug_utils.MessageSeverityFlags) -> int:
    """
    Convert OpenXR message severities to Python logging levels.

    :param severity_flags: Bitmask of message severity flags.
    :type severity_flags: xr.DebugUtilsMessageSeverityFlagsEXT
    :returns: One of logging.DEBUG, INFO, WARNING, or ERROR.
    """
    if severity_flags & debug_utils.MessageSeverityFlags.ERROR_BIT:
        return logging.ERROR
    if severity_flags & debug_utils.MessageSeverityFlags.WARNING_BIT:
        return logging.WARNING
    if severity_flags & debug_utils.MessageSeverityFlags.INFO_BIT:
        return logging.INFO
    return logging.DEBUG


def debug_callback(
        severity: debug_utils.MessageSeverityFlags,
        _type_flags: debug_utils.MessageTypeFlags,
        callback_data: debug_utils.MessengerCallbackData,
        _user_data: c_void_p,
) -> bool:
    """Redirect OpenXR messages to a python logger."""
    logger.log(
        level=log_level_for_severity(severity),
        msg=f"{callback_data.function_name}: {callback_data.message}")
    return False


def tst_debug_utils_basic():
    with ExitStack() as exit_stack:  # noqa
        instance = exit_stack.enter_context(xr.create_instance(
            create_info=xr.InstanceCreateInfo(
                enabled_extension_names=[
                    debug_utils.EXTENSION_NAME,
                    xr.MND_HEADLESS_EXTENSION_NAME,
                ]
            )
        ))

        messenger_create_info = xr.DebugUtilsMessengerCreateInfoEXT(
            user_callback=debug_callback,
        )

        _messenger = debug_utils.create_messenger(
            instance,
            messenger_create_info,
        )

        # Trigger a message manually
        debug_utils.submit_message(
            instance,
            message_severity=debug_utils.MessageSeverityFlags.WARNING_BIT,
            message_types=debug_utils.MessageTypeFlags.GENERAL_BIT,
            callback_data=debug_utils.MessengerCallbackData(
                message_id="TestMessage",
                message="This is a test debug message."
            )
        )


if __name__ == "__main__":
    tst_debug_utils_basic()
