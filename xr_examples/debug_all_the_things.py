"""
debug_all_the_things.py

This example program demonstrates several logging aids for debugging pyopenxr programs.
Ordinarily you would not do all these things at once.
"""

import ctypes
import logging  # 1) Use the python logging system
import os

import glfw
from OpenGL import GL  # OpenGL can report debug messages too
import xr

# 2) Hook into the pyopenxr logger hierarchy.
logging.basicConfig()  # You might want also to study the parameters to basicConfig()...
pyopenxr_logger = logging.getLogger("pyopenxr")
# show me ALL the messages
pyopenxr_logger.setLevel(logging.DEBUG)  # Modify argument according to your current needs

# 3) Create a child logger for this particular program
logger = logging.getLogger("pyopenxr.debug_all_the_things")
logger.info("Hey, this logging thing works!")  # Test it out

# Use API layers for debugging
enabled_api_layers = []

# 4) Core validation adds additional messages about correct use of the OpenXR api
if xr.LUNARG_core_validation_APILAYER_NAME in xr.enumerate_api_layer_properties():
    enabled_api_layers.append(xr.LUNARG_core_validation_APILAYER_NAME)

# 5) API dump shows the details of every OpenXR call. Use this for deep debugging only.
if xr.LUNARG_api_dump_APILAYER_NAME in xr.enumerate_api_layer_properties():
    enabled_api_layers.append(xr.LUNARG_api_dump_APILAYER_NAME)
    os.environ["XR_API_DUMP_EXPORT_TYPE"] = "text"  # or "html"
    # os.environ["XR_API_DUMP_FILE_NAME"] = "/some/file/name"

# Use extensions for debugging
enabled_extensions = []
# 6) XR_EXT_debug_utils can be used to redirect pyopenxr debugging messages to our logger,
#    among other things.
if xr.EXT_DEBUG_UTILS_EXTENSION_NAME in xr.enumerate_instance_extension_properties():
    enabled_extensions.append(xr.EXT_DEBUG_UTILS_EXTENSION_NAME)


# Define helper function for our logging callback
def openxr_log_level(severity_flags: xr.DebugUtilsMessageSeverityFlagsEXT) -> int:
    """Convert OpenXR message severities to python logging severities."""
    if severity_flags & xr.DEBUG_UTILS_MESSAGE_SEVERITY_ERROR_BIT_EXT:
        return logging.ERROR
    elif severity_flags & xr.DEBUG_UTILS_MESSAGE_SEVERITY_WARNING_BIT_EXT:
        return logging.WARNING
    elif severity_flags & xr.DEBUG_UTILS_MESSAGE_SEVERITY_INFO_BIT_EXT:
        return logging.INFO
    else:
        return logging.DEBUG


def xr_debug_callback(
            severity: xr.DebugUtilsMessageSeverityFlagsEXT,
            _type: xr.DebugUtilsMessageTypeFlagsEXT,
            data: ctypes.POINTER(xr.DebugUtilsMessengerCallbackDataEXT),
            _user_data: ctypes.c_void_p) -> bool:
    """Redirect OpenXR messages to our python logger."""
    d = data.contents
    pyopenxr_logger.log(
        level=openxr_log_level(severity),
        msg=f"OpenXR: {d.function_name.decode()}: {d.message.decode()}")
    return True


# Prepare to create a debug utils messenger
pfn_xr_debug_callback = xr.PFN_xrDebugUtilsMessengerCallbackEXT(xr_debug_callback)
debug_utils_messenger_create_info = xr.DebugUtilsMessengerCreateInfoEXT(
    message_severities=(
            xr.DEBUG_UTILS_MESSAGE_SEVERITY_VERBOSE_BIT_EXT
            | xr.DEBUG_UTILS_MESSAGE_SEVERITY_INFO_BIT_EXT
            | xr.DEBUG_UTILS_MESSAGE_SEVERITY_WARNING_BIT_EXT
            | xr.DEBUG_UTILS_MESSAGE_SEVERITY_ERROR_BIT_EXT
    ),
    message_types=(
                xr.DEBUG_UTILS_MESSAGE_TYPE_GENERAL_BIT_EXT
                | xr.DEBUG_UTILS_MESSAGE_TYPE_VALIDATION_BIT_EXT
                | xr.DEBUG_UTILS_MESSAGE_TYPE_PERFORMANCE_BIT_EXT
                | xr.DEBUG_UTILS_MESSAGE_TYPE_CONFORMANCE_BIT_EXT
    ),
    user_callback=pfn_xr_debug_callback,
)

ptr_debug_messenger = None
if xr.EXT_DEBUG_UTILS_EXTENSION_NAME in xr.enumerate_instance_extension_properties():
    # Insert our debug_utils_messenger create_info
    ptr_debug_messenger = ctypes.cast(
        ctypes.pointer(debug_utils_messenger_create_info), ctypes.c_void_p)

# 7) Turn on extra debugging messages in the OpenXR Loader
os.environ["XR_LOADER_DEBUG"] = "all"
os.environ["LD_BIND_NOW"] = "1"


# Create OpenXR instance with attached layers, extensions, and debug messenger.
instance = xr.create_instance(
    xr.InstanceCreateInfo(
        enabled_api_layer_names=enabled_api_layers,
        enabled_extension_names=enabled_extensions,
        next=ptr_debug_messenger,
    )
)

# OpenGL can report debug messages too
# Create a sub-logger for messages from OpenGL
gl_logger = logging.getLogger("pyopenxr.opengl")


def gl_debug_message_callback(_source, _msg_type, _msg_id, severity, length, raw, _user):
    """Redirect OpenGL debug messages"""
    log_level = {
        GL.GL_DEBUG_SEVERITY_HIGH: logging.ERROR,
        GL.GL_DEBUG_SEVERITY_MEDIUM: logging.WARNING,
        GL.GL_DEBUG_SEVERITY_LOW: logging.INFO,
        GL.GL_DEBUG_SEVERITY_NOTIFICATION: logging.DEBUG,
    }[severity]
    gl_logger.log(log_level, f"OpenGL Message: {raw[0:length].decode()}")


gl_debug_message_proc = GL.GLDEBUGPROC(gl_debug_message_callback)
# We need an active OpenGL context before calling glDebugMessageCallback
glfw.init()
window = glfw.create_window(16, 16, "glfw window", None, None)
glfw.make_context_current(window)
GL.glDebugMessageCallback(gl_debug_message_proc, None)


# Clean up
glfw.terminate()
xr.destroy_instance(instance)
