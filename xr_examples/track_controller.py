"""
pyopenxr example program track_controller.py

Prints the position of your right-hand controller for 30 frames.
"""

import ctypes
import time
import xr

# ContextObject is a high level pythonic class meant to keep simple cases simple.
with xr.ContextObject(
    instance_create_info=xr.InstanceCreateInfo(
        enabled_extension_names=[
            # A graphics extension is mandatory (without a headless extension)
            xr.KHR_OPENGL_ENABLE_EXTENSION_NAME,
        ],
    ),
) as context:
    # Set up the controller pose action
    action_set = xr.create_action_set(
        instance=context.instance_handle,
        create_info=xr.ActionSetCreateInfo(
            action_set_name="device_tracking",
            localized_action_set_name="Device Tracking",
            priority=0,
        ),
    )
    right_controller_path = xr.string_to_path(
        instance=context.instance_handle,
        path_string="/user/hand/right",
    )
    right_controller_pose_action = xr.create_action(
        action_set=action_set,
        create_info=xr.ActionCreateInfo(
            action_type=xr.ActionType.POSE_INPUT,
            action_name="right_controller_pose",
            localized_action_name="Right Controller Pose",
            count_subaction_paths=1,
            subaction_paths=ctypes.pointer(right_controller_path),
        ),
    )
    suggested_binding = xr.ActionSuggestedBinding(
        action=right_controller_pose_action,
        binding=xr.string_to_path(
            instance=context.instance_handle,
            path_string="/user/hand/right/input/grip/pose",
        ),
    )
    xr.suggest_interaction_profile_bindings(
        instance=context.instance_handle,
        suggested_bindings=xr.InteractionProfileSuggestedBinding(
            interaction_profile=xr.string_to_path(
                context.instance_handle,
                "/interaction_profiles/khr/simple_controller",
            ),
            count_suggested_bindings=1,
            suggested_bindings=ctypes.pointer(suggested_binding),
        ),
    )
    right_controller_action_space = xr.create_action_space(
        session=context.session_handle,
        create_info=xr.ActionSpaceCreateInfo(
            action=right_controller_pose_action,
            subaction_path=right_controller_path,
        ),
    )
    xr.attach_session_action_sets(
        session=context.session_handle,
        attach_info=xr.SessionActionSetsAttachInfo(
            count_action_sets=1,
            action_sets=ctypes.pointer(action_set),
        ),
    )
    # Loop over the render frames
    for frame_index, frame_state in enumerate(context.frame_loop()):

        if context.session_state == xr.SessionState.FOCUSED:
            active_action_set = xr.ActiveActionSet(
                action_set=action_set,
                subaction_path=xr.NULL_PATH,
            )
            xr.sync_actions(
                session=context.session_handle,
                sync_info=xr.ActionsSyncInfo(
                    count_active_action_sets=1,
                    active_action_sets=ctypes.pointer(active_action_set),
                ),
            )
            space_location = xr.locate_space(
                space=right_controller_action_space,
                base_space=context.space_handle,
                time=frame_state.predicted_display_time,
            )
            if space_location.location_flags & xr.SPACE_LOCATION_POSITION_VALID_BIT:
                print(space_location.pose)
            else:
                print("controller not active")

        # Slow things down, especially since we are not rendering anything
        time.sleep(0.5)
        # Don't run forever
        if frame_index > 30:
            break
