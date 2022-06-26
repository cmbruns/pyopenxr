"""
This is a work in progress...

The goal here is to create the simplest case to demonstrate the hang that occurs
in xr.destroy_instance() on Linux with SteamVR.

The hang does not occur on Windows; it *does* occur on linux.
The hang does not occur when calling xr.destroy_instance() without out any frame loop calls.
  it *does* occur when calling xr.destroy_instance after running a frame loop.
"""

import ctypes
from ctypes import byref, c_int32, c_void_p, cast, POINTER, pointer, Structure
import logging  # 1) Use the python logging system
import os
import platform
import time

if platform.system() == "Windows":
    from OpenGL import WGL
elif platform.system() == "Linux":
    from OpenGL import GLX
from OpenGL import GL
import xr


run_frame_loop = True


class Swapchain(Structure):
    _fields_ = [
        ("handle", xr.Swapchain),
        ("width", c_int32),
        ("height", c_int32),
    ]


# 2) Hook into the pyopenxr logger hierarchy.
logging.basicConfig()  # You might want also to study the parameters to basicConfig()...
pyopenxr_logger = logging.getLogger("pyopenxr")
# show me ALL the messages
pyopenxr_logger.setLevel(logging.INFO)  # Modify argument according to your current needs

# 3) Create a child logger for this particular program
logger = logging.getLogger("pyopenxr.where_does_it_hang")
logger.info("Hey, this logging thing works!")  # Test it out

# Use API layers for debugging
enabled_api_layers = []

# 4) Core validation adds additional messages about correct use of the OpenXR api
if xr.LUNARG_core_validation_APILAYER_NAME in xr.enumerate_api_layer_properties():
    enabled_api_layers.append(xr.LUNARG_core_validation_APILAYER_NAME)

# 5) API dump shows the details of every OpenXR call. Use this for deep debugging only.
if False and xr.LUNARG_api_dump_APILAYER_NAME in xr.enumerate_api_layer_properties():
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
enabled_extensions.append(xr.KHR_OPENGL_ENABLE_EXTENSION_NAME)
instance = xr.create_instance(
    xr.InstanceCreateInfo(
        enabled_api_layer_names=enabled_api_layers,
        enabled_extension_names=enabled_extensions,
        next=ptr_debug_messenger,
    )
)

system_id = xr.get_system(
    instance=instance,
    get_info=xr.SystemGetInfo(
        form_factor=xr.FormFactor.HEAD_MOUNTED_DISPLAY,
    ),
)

graphics = xr.OpenGLGraphics(
    instance=instance,
    system=system_id,
    title="Horatio Hornblower",
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
graphics.make_current()
GL.glDebugMessageCallback(gl_debug_message_proc, None)

graphics_binding_pointer = cast(pointer(graphics.graphics_binding), c_void_p)
session = xr.create_session(
    instance=instance,
    create_info=xr.SessionCreateInfo(
        system_id=system_id,
        next=graphics_binding_pointer,
    ),
)

space = xr.create_reference_space(
    session=session,
    create_info=xr.ReferenceSpaceCreateInfo(),
)

default_action_set = xr.create_action_set(
    instance=instance,
    create_info=xr.ActionSetCreateInfo(
        action_set_name="default_action_set",
        localized_action_set_name="Default Action Set",
        priority=0,
    ),
)

# Create swapchains
view_configuration_type = xr.ViewConfigurationType.PRIMARY_STEREO
config_views = xr.enumerate_view_configuration_views(
    instance=instance,
    system_id=system_id,
    view_configuration_type=view_configuration_type,
)
graphics.initialize_resources()
swapchain_formats = xr.enumerate_swapchain_formats(session)
color_swapchain_format = graphics.select_color_swapchain_format(swapchain_formats)
# Create a swapchain for each view.
swapchains = []
swapchain_image_buffers = []
swapchain_image_ptr_buffers = []
for vp in config_views:
    # Create the swapchain.
    swapchain_create_info = xr.SwapchainCreateInfo(
        array_size=1,
        format=color_swapchain_format,
        width=vp.recommended_image_rect_width,
        height=vp.recommended_image_rect_height,
        mip_count=1,
        face_count=1,
        sample_count=vp.recommended_swapchain_sample_count,
        usage_flags=xr.SwapchainUsageFlags.SAMPLED_BIT | xr.SwapchainUsageFlags.COLOR_ATTACHMENT_BIT,
    )
    swapchain = Swapchain(
        xr.create_swapchain(
            session=session,
            create_info=swapchain_create_info,
        ),
        swapchain_create_info.width,
        swapchain_create_info.height,
    )
    swapchains.append(swapchain)
    swapchain_image_buffer = xr.enumerate_swapchain_images(
        swapchain=swapchain.handle,
        element_type=graphics.swapchain_image_type,
    )
    # Keep the buffer alive by moving it into the list of buffers.
    swapchain_image_buffers.append(swapchain_image_buffer)
    capacity = len(swapchain_image_buffer)
    swapchain_image_ptr_buffer = (POINTER(xr.SwapchainImageBaseHeader) * capacity)()
    for ix in range(capacity):
        swapchain_image_ptr_buffer[ix] = cast(
            byref(swapchain_image_buffer[ix]),
            POINTER(xr.SwapchainImageBaseHeader))
    swapchain_image_ptr_buffers.append(swapchain_image_ptr_buffer)
graphics.make_current()
# frame_loop
action_sets = [default_action_set,]
xr.attach_session_action_sets(
    session=session,
    attach_info=xr.SessionActionSetsAttachInfo(
        count_action_sets=len(action_sets),
        action_sets=(xr.ActionSet * len(action_sets))(
            *action_sets
        )
    ),
)
session_is_running = False
frame_count = 0

if run_frame_loop:
    while True:
        frame_count += 1
        window_closed = graphics.poll_events()
        if window_closed:
            xr.request_exit_session(session)
        # poll_xr_events
        exit_render_loop = False
        while True:
            try:
                event_buffer = xr.poll_event(instance)
                event_type = xr.StructureType(event_buffer.type)
                if event_type == xr.StructureType.EVENT_DATA_INSTANCE_LOSS_PENDING:
                    # still handle rest of the events instead of immediately quitting
                    pass
                elif event_type == xr.StructureType.EVENT_DATA_SESSION_STATE_CHANGED \
                        and session is not None:
                    event = cast(
                        byref(event_buffer),
                        POINTER(xr.EventDataSessionStateChanged)).contents
                    session_state = xr.SessionState(event.state)
                    logger.info(f"Session state changed to {str(session_state)}")
                    if session_state == xr.SessionState.IDLE:
                        pass
                    elif session_state == xr.SessionState.READY:
                        xr.begin_session(
                            session=session,
                            begin_info=xr.SessionBeginInfo(
                                view_configuration_type,
                            ),
                        )
                        session_is_running = True
                    elif session_state == xr.SessionState.STOPPING:
                        session_is_running = False
                        xr.end_session(session)
                    elif session_state == xr.SessionState.EXITING:
                        exit_render_loop = True
                    elif session_state == xr.SessionState.LOSS_PENDING:
                        exit_render_loop = True
                    elif event_type == xr.StructureType.EVENT_DATA_VIVE_TRACKER_CONNECTED_HTCX:
                        vive_tracker_connected = cast(byref(event_buffer), POINTER(xr.EventDataViveTrackerConnectedHTCX)).contents
                        paths = vive_tracker_connected.paths.contents
                        persistent_path_str = xr.path_to_string(instance, paths.persistent_path)
                        # print(f"Vive Tracker connected: {persistent_path_str}")
                        if paths.role_path != xr.NULL_PATH:
                            role_path_str = xr.path_to_string(instance, paths.role_path)
                            # print(f" New role is: {role_path_str}")
                        else:
                            # print(f" No role path.")
                            pass
                    elif event_type == xr.StructureType.EVENT_DATA_INTERACTION_PROFILE_CHANGED:
                        # print("data interaction profile changed")
                        # TODO:
                        pass
            except xr.EventUnavailable:
                break
            # end of poll_xr_events
        if exit_render_loop:
            break
        if session_is_running:
            if session_state in (
                    xr.SessionState.READY,
                    xr.SessionState.SYNCHRONIZED,
                    xr.SessionState.VISIBLE,
                    xr.SessionState.FOCUSED,
            ):
                # xr.request_exit_session(session)  # Request exit here allows clean exit
                # Something about begin/wait/end_frame is making it hang at the end.
                frame_state = xr.wait_frame(session, xr.FrameWaitInfo())
                xr.begin_frame(session, xr.FrameBeginInfo())
                render_layers = []
                if frame_state.should_render:
                    graphics.make_current()
                    GL.glClearColor(1, 0.6, 0.6, 1)
                    GL.glClear(GL.GL_COLOR_BUFFER_BIT)
                    time.sleep(0.02)
                xr.end_frame(
                    session,
                    frame_end_info=xr.FrameEndInfo(
                        display_time=frame_state.predicted_display_time,
                        environment_blend_mode=xr.EnvironmentBlendMode.OPAQUE,
                        layers=render_layers,
                    )
                )
                # xr.request_exit_session(session)  # Request exit here allows clean exit but steamvr is hosed.
            if frame_count > 100:
                xr.request_exit_session(session)
        else:
            time.sleep(0.02)

# Clean up
graphics.destroy()
logger.info("About to call xr.destroy_instance()...")
xr.destroy_instance(instance)
logger.info("... called xr.destroy_instance().")
