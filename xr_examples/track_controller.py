"""
pyopenxr example program track_controller.py

Prints the position of your right-hand controller for 30 frames.
"""

import ctypes
import time
import xr.utils

# ContextObject is a high level pythonic class meant to keep simple cases simple.
with xr.utils.ContextObject(
    instance_create_info=xr.InstanceCreateInfo(
        enabled_extension_names=[
            # A graphics extension is mandatory (without a headless extension)
            xr.KHR_OPENGL_ENABLE_EXTENSION_NAME,
        ],
    ),
) as context:
    # Set up the controller pose action
    controller_paths = (xr.Path * 2)(
        xr.string_to_path(context.instance, "/user/hand/left"),
        xr.string_to_path(context.instance, "/user/hand/right"),
    )
    controller_pose_action = xr.create_action(
        action_set=context.default_action_set,
        create_info=xr.ActionCreateInfo(
            action_type=xr.ActionType.POSE_INPUT,
            action_name="hand_pose",
            localized_action_name="Hand Pose",
            count_subaction_paths=len(controller_paths),
            subaction_paths=controller_paths,
        ),
    )
    suggested_bindings = (xr.ActionSuggestedBinding * 2)(
        xr.ActionSuggestedBinding(
            action=controller_pose_action,
            binding=xr.string_to_path(
                instance=context.instance,
                path_string="/user/hand/left/input/grip/pose",
            ),
        ),
        xr.ActionSuggestedBinding(
            action=controller_pose_action,
            binding=xr.string_to_path(
                instance=context.instance,
                path_string="/user/hand/right/input/grip/pose",
            ),
        ),
    )
    xr.suggest_interaction_profile_bindings(
        instance=context.instance,
        suggested_bindings=xr.InteractionProfileSuggestedBinding(
            interaction_profile=xr.string_to_path(
                context.instance,
                "/interaction_profiles/khr/simple_controller",
            ),
            count_suggested_bindings=len(suggested_bindings),
            suggested_bindings=suggested_bindings,
        ),
    )
    xr.suggest_interaction_profile_bindings(
        instance=context.instance,
        suggested_bindings=xr.InteractionProfileSuggestedBinding(
            interaction_profile=xr.string_to_path(
                context.instance,
                "/interaction_profiles/htc/vive_controller",
            ),
            count_suggested_bindings=len(suggested_bindings),
            suggested_bindings=suggested_bindings,
        ),
    )

    action_spaces = [
        xr.create_action_space(
            session=context.session,
            create_info=xr.ActionSpaceCreateInfo(
                action=controller_pose_action,
                subaction_path=controller_paths[0],
            ),
        ),
        xr.create_action_space(
            session=context.session,
            create_info=xr.ActionSpaceCreateInfo(
                action=controller_pose_action,
                subaction_path=controller_paths[1],
            ),
        ),
    ]
    # Loop over the render frames
    session_was_focused = False  # Check for a common problem
    for frame_index, frame_state in enumerate(context.frame_loop()):

        if context.session_state == xr.SessionState.FOCUSED:
            session_was_focused = True
            active_action_set = xr.ActiveActionSet(
                action_set=context.default_action_set,
                subaction_path=xr.NULL_PATH,
            )
            xr.sync_actions(
                session=context.session,
                sync_info=xr.ActionsSyncInfo(
                    count_active_action_sets=1,
                    active_action_sets=ctypes.pointer(active_action_set),
                ),
            )
            found_count = 0
            for index, space in enumerate(action_spaces):
                space_location = xr.locate_space(
                    space=space,
                    base_space=context.space,
                    time=frame_state.predicted_display_time,
                )
                if space_location.location_flags & xr.SPACE_LOCATION_POSITION_VALID_BIT:
                    print(index + 1, space_location.pose)
                    found_count += 1
            if found_count == 0:
                print("no controllers active")

        # Slow things down, especially since we are not rendering anything
        time.sleep(0.5)
        # Don't run forever
        if frame_index > 30:
            break
    if not session_was_focused:
        print("This OpenXR session never entered the FOCUSED state. Did you wear the headset?")
