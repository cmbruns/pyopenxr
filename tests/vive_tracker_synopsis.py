# TODO: debug this. Maybe headless and vive tracking cannot work together?

from contextlib import ExitStack
import os
import time

import xr
from xr.ext.MND import headless
from xr.ext.HTCX import vive_tracker_interaction as vive_tracker
from xr.ext.EXT import debug_utils
from xr.utils import SessionStateManager, XrEventDispatcher

assert xr.LUNARG_core_validation_APILAYER_NAME in xr.enumerate_api_layer_properties()
os.environ["XR_API_DUMP_EXPORT_TYPE"] = "text"
os.environ["XR_LOADER_DEBUG"] = "all"
os.environ["LD_BIND_NOW"] = "1"
os.environ["XR_ENABLE_API_LAYERS"] = "XR_APILAYER_LUNARG_core_validation"

with ExitStack() as exit_stack:  # noqa
    instance = exit_stack.enter_context(xr.create_instance(
        xr.InstanceCreateInfo(
            enabled_extension_names=[
                headless.EXTENSION_NAME,
                vive_tracker.EXTENSION_NAME,
                debug_utils.EXTENSION_NAME,
            ],
            enabled_api_layer_names=[xr.LUNARG_core_validation_APILAYER_NAME],
        ),
    ))
    messenger = exit_stack.enter_context(debug_utils.create_messenger(instance))
    debug_utils.submit_message(
        instance,
        message_severity=debug_utils.MessageSeverityFlags.WARNING_BIT,
        message_types=debug_utils.MessageTypeFlags.GENERAL_BIT,
        callback_data=debug_utils.MessengerCallbackData(
            message_id="TestMessage",
            message="This is a test debug message."
        )
    )
    system_id = xr.get_system(instance)
    action_set = exit_stack.enter_context(xr.create_action_set(
        instance,
        xr.ActionSetCreateInfo(
            action_set_name="vts_action_set",
            localized_action_set_name="Action Set",
            priority=0,
        ),
    ))
    pose_action = exit_stack.enter_context(xr.create_action(
        action_set,
        xr.ActionCreateInfo(
            action_name="tracker_pose",
            localized_action_name="Tracker Pose",
            action_type=xr.ActionType.POSE_INPUT,
            subaction_paths=[xr.string_to_path(
                instance,
                "/user/vive_tracker_htcx/role/right_foot",
            )],
        ),
    ))
    session = exit_stack.enter_context(xr.create_session(
        instance,
        xr.SessionCreateInfo(system_id=system_id),
    ))
    session_state_manager = exit_stack.enter_context(SessionStateManager(
        instance,
        session,
        xr.ViewConfigurationType(),
    ))
    event_dispatcher = XrEventDispatcher(instance)
    event_dispatcher.subscribe(session_state_manager.handle_xr_event)
    xr.attach_session_action_sets(
        session,
        xr.SessionActionSetsAttachInfo(
            action_sets=[action_set],
        ),
    )
    for _ in range(10):
        event_dispatcher.poll()
        print(session_state_manager.session_state.name)
        frame_state = session_state_manager.begin_frame()
        time.sleep(0.5)
        xr.end_frame(
            session,
            frame_end_info=xr.FrameEndInfo(
                display_time=frame_state.predicted_display_time,
                environment_blend_mode=xr.EnvironmentBlendMode(),
                layers=[],
            )
        )

    paths = vive_tracker.enumerate_paths(instance)
    print(paths)
    for path in paths:
        print(path)
