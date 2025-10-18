"""
pyopenxr example program vive_tracker.py

Prints the position and orientation of your vive trackers each frame.

Helpful instructions for getting trackers working on Linux are at
https://gist.github.com/DanielArnett/c9a56c9c7cc0def20648480bca1f6772
The udev symbolic link trick was crucial in my case.
"""

import ctypes
from ctypes import cast, byref
import logging
import time
import xr
from xr.utils.gl import ContextObject
from xr.utils.gl.glfw_util import GLFWOffscreenContextProvider

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

print("Warning: trackers with role 'Handheld object' won't be detected.")

# ContextObject is a high level pythonic class meant to keep simple cases simple.
with ContextObject(
    context_provider=GLFWOffscreenContextProvider(),
    instance_create_info=xr.InstanceCreateInfo(
        enabled_extension_names=[
            # A graphics extension is mandatory (without a headless extension)
            xr.KHR_OPENGL_ENABLE_EXTENSION_NAME,
            xr.HTCX_VIVE_TRACKER_INTERACTION_EXTENSION_NAME,
        ],
    ),
) as context:
    instance = context.instance
    session = context.session

    # Create the action with subaction path
    # Role strings from
    # https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#XR_HTCX_vive_tracker_interaction
    role_strings = [
        "handheld_object",
        "left_foot",
        "right_foot",
        "left_shoulder",
        "right_shoulder",
        "left_elbow",
        "right_elbow",
        "left_knee",
        "right_knee",
        "waist",
        "chest",
        "camera",
        "keyboard",
    ]
    role_path_strings = [f"/user/vive_tracker_htcx/role/{role}"
                         for role in role_strings]
    role_paths = (xr.Path * len(role_path_strings))(  # noqa
        *[xr.string_to_path(instance, role_string) for role_string in role_path_strings],
    )
    pose_action = xr.create_action(
        action_set=context.default_action_set,
        create_info=xr.ActionCreateInfo(
            action_type=xr.ActionType.POSE_INPUT,
            action_name="tracker_pose",
            localized_action_name="Tracker Pose",
            count_subaction_paths=len(role_paths),
            subaction_paths=role_paths,
        ),
    )
    # Describe a suggested binding for that action and subaction path
    suggested_binding_paths = (xr.ActionSuggestedBinding * len(role_path_strings))(
        *[xr.ActionSuggestedBinding(
            pose_action,
            xr.string_to_path(instance, f"{role_path_string}/input/grip/pose"))
          for role_path_string in role_path_strings],
    )
    xr.suggest_interaction_profile_bindings(
        instance=instance,
        suggested_bindings=xr.InteractionProfileSuggestedBinding(
            interaction_profile=xr.string_to_path(instance, "/interaction_profiles/htc/vive_tracker_htcx"),
            count_suggested_bindings=len(suggested_binding_paths),
            suggested_bindings=suggested_binding_paths,
        )
    )
    # Create action spaces for locating trackers in each role
    tracker_action_spaces = []
    for role_index, role_path in enumerate(role_paths):
        try:
            action_space = xr.create_action_space(
                session=session,
                create_info=xr.ActionSpaceCreateInfo(
                    action=pose_action,
                    subaction_path=role_path,
                )
            )
            tracker_action_spaces.append(action_space)
        except xr.exception.PathUnsupportedError:
            log.info(f"Skipping vive tracker role {role_strings[role_index]}")

    vive_tracker_paths = xr.enumerate_vive_tracker_paths_htcx(instance)
    print(len(vive_tracker_paths))
    # print(*vive_tracker_paths)

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
                session=session,
                sync_info=xr.ActionsSyncInfo(
                    count_active_action_sets=1,
                    active_action_sets=ctypes.pointer(active_action_set),
                ),
            )

            vive_tracker_paths = xr.enumerate_vive_tracker_paths_htcx(instance)
            # print(xr.Result(result), n_paths.value)
            # print(*vive_tracker_paths)

            found_tracker_count = 0
            for index, space in enumerate(tracker_action_spaces):
                space_location = xr.locate_space(
                    space=space,
                    base_space=context.space,
                    time=frame_state.predicted_display_time,
                )
                if space_location.location_flags & xr.SPACE_LOCATION_POSITION_VALID_BIT:
                    print(f"{role_strings[index]}: {space_location.pose}")
                    found_tracker_count += 1
            if found_tracker_count == 0:
                log.info("no trackers found")
            log.info(f"{found_tracker_count} vive trackers found")

        # Slow things down, especially since we are not rendering anything
        time.sleep(0.5)
        # Don't run forever
        if frame_index > 30:
            break
    if not session_was_focused:
        print("This OpenXR session never entered the FOCUSED state. Did you wear the headset?")
