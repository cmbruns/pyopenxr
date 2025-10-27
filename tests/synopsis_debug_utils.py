from contextlib import ExitStack
import inspect
import logging
import xr
from xr.callback import logging_debug_callback, stdout_debug_callback

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def tst_debug_utils_basic():
    # This example creates two different debug messengers.
    with ExitStack() as exit_stack:  # noqa
        EC = exit_stack.enter_context
        # First messenger writes to stdout and is passed in xr.InstanceCreateInfo
        # NOTE: we need to keep this create_info alive to avoid premature garbage
        # collection of the callback closure.
        messenger_create_info1 = xr.DebugUtilsMessengerCreateInfoEXT(
            user_callback=stdout_debug_callback)
        instance = EC(xr.create_instance(
            create_info=xr.InstanceCreateInfo(
                enabled_extension_names=[xr.EXT_DEBUG_UTILS_EXTENSION_NAME],
                next=messenger_create_info1)))
        # Second messenger writes to python logging, and is created normally
        # NOTE: keep this messenger alive; it holds a reference to the callback closure.
        _messenger2 = EC(xr.create_debug_utils_messenger_ext(
            instance=instance,
            create_info=xr.DebugUtilsMessengerCreateInfoEXT(
                user_callback=logging_debug_callback,
                user_data=logger)))
        # Trigger a message manually
        xr.submit_debug_utils_message_ext(
            instance=instance,
            message_severity=xr.DebugUtilsMessageSeverityFlagsEXT.WARNING_BIT,
            message_types=xr.DebugUtilsMessageTypeFlagsEXT.GENERAL_BIT,
            callback_data=xr.DebugUtilsMessengerCallbackDataEXT(
                message_id="TestMessage",
                message="This is a test debug message.",
                function_name=inspect.currentframe().f_code.co_name))


if __name__ == "__main__":
    tst_debug_utils_basic()
