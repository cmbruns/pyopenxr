from contextlib import ExitStack
from ctypes import c_void_p
import logging

import xr
from xr.ext.EXT import debug_utils


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def debug_callback(
        severity: debug_utils.MessageSeverityFlags,
        _type_flags: debug_utils.MessageTypeFlags,
        callback_data: debug_utils.MessengerCallbackData,
        _user_data: c_void_p,
) -> bool:
    """Redirect OpenXR messages to a python logger."""
    data = callback_data.contents
    message = data.message.decode("utf-8", errors="replace")
    func_name = data.function_name.decode("utf-8", errors="replace")
    severity = xr.DebugUtilsMessageSeverityFlagsEXT(severity)
    type_flags = xr.DebugUtilsMessageTypeFlagsEXT(type_flags)
    logger.log(
        level=debug_utils.log_level_for_severity(severity),
        msg=f"{callback_data.function_name}: {callback_data.message}")
    return False


def test_debug_utils_basic():
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

        messenger = debug_utils.create_messenger(
            instance,
            messenger_create_info,
        )

        print(messenger._callback)

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
    test_debug_utils_basic()
