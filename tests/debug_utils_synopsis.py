from contextlib import ExitStack
from ctypes import POINTER, c_void_p
import logging

import xr
from xr.ext import DebugUtils


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def debug_callback(
        severity: xr.DebugUtilsMessageSeverityFlagsEXT,
        _type: xr.DebugUtilsMessageTypeFlagsEXT,
        data: POINTER(xr.DebugUtilsMessengerCallbackDataEXT),
        _user_data: c_void_p
) -> bool:
    """Redirect OpenXR messages to our python logger."""
    d = data.contents
    logger.log(
        level=DebugUtils.log_level_for_severity(severity),
        msg=f"{d.function_name.decode()}: {d.message.decode()}")
    return True


def test_debug_utils_basic():
    with ExitStack() as exit_stack:  # noqa
        messenger_create_info = xr.DebugUtilsMessengerCreateInfoEXT(
            message_severities=xr.DebugUtilsMessageSeverityFlagsEXT.WARNING_BIT |
            xr.DebugUtilsMessageSeverityFlagsEXT.ERROR_BIT,
            message_types=xr.DebugUtilsMessageTypeFlagsEXT.GENERAL_BIT |
            xr.DebugUtilsMessageTypeFlagsEXT.VALIDATION_BIT,
            user_callback=xr.PFN_xrDebugUtilsMessengerCallbackEXT(
                debug_callback),
        )

        instance = exit_stack.enter_context(xr.Instance(
            create_info=xr.InstanceCreateInfo(
                enabled_extension_names=[
                    DebugUtils.NAME,
                    xr.MND_HEADLESS_EXTENSION_NAME,
                ]
            )
        ))

        debug_utils = DebugUtils(instance)
        messenger = debug_utils.create_messenger(messenger_create_info)

        # Trigger a message manually
        debug_utils.submit_message(
            message_severity=xr.DebugUtilsMessageSeverityFlagsEXT.WARNING_BIT,
            message_type=xr.DebugUtilsMessageTypeFlagsEXT.GENERAL_BIT,
            callback_data=xr.DebugUtilsMessengerCallbackDataEXT(
                message_id="TestMessage",
                message="This is a test debug message."
            )
        )

        debug_utils.destroy_messenger(messenger)


if __name__ == "__main__":
    test_debug_utils_basic()
