from typing import Generator, Tuple
import xr


class TwoControllers(object):
    def __init__(
            self,
            instance: xr.Instance,
            session: xr.Session,
    ):
        self.instance = instance
        self.session = session
        self.action_set = xr.create_action_set(
            instance=instance,
            create_info=xr.ActionSetCreateInfo(
                action_set_name="two_controllers_action_set",
                localized_action_set_name="TwoControllers Action Set",
                priority=0,
            ),
        )
        self.controller_paths = (xr.Path * 2)(
            xr.string_to_path(instance, "/user/hand/left"),
            xr.string_to_path(instance, "/user/hand/right"),
        )
        self.controller_pose_action = xr.create_action(
            action_set=self.action_set,
            create_info=xr.ActionCreateInfo(
                action_type=xr.ActionType.POSE_INPUT,
                action_name="controller_pose",
                localized_action_name="Controller pose",
                count_subaction_paths=len(self.controller_paths),
                subaction_paths=self.controller_paths,
            ),
        )
        # TODO: more bindings like in C++ hello_xr
        self.suggested_bindings = (xr.ActionSuggestedBinding * 2)(
            xr.ActionSuggestedBinding(
                action=self.controller_pose_action,
                binding=xr.string_to_path(
                    instance=instance,
                    path_string="/user/hand/left/input/grip/pose",
                ),
            ),
            xr.ActionSuggestedBinding(
                action=self.controller_pose_action,
                binding=xr.string_to_path(
                    instance=instance,
                    path_string="/user/hand/right/input/grip/pose",
                ),
            ),
        )
        xr.suggest_interaction_profile_bindings(
            instance=instance,
            suggested_bindings=xr.InteractionProfileSuggestedBinding(
                interaction_profile=xr.string_to_path(
                    instance,
                    "/interaction_profiles/khr/simple_controller",
                ),
                count_suggested_bindings=len(self.suggested_bindings),
                suggested_bindings=self.suggested_bindings,
            ),
        )
        xr.suggest_interaction_profile_bindings(
            instance=instance,
            suggested_bindings=xr.InteractionProfileSuggestedBinding(
                interaction_profile=xr.string_to_path(
                    instance,
                    "/interaction_profiles/htc/vive_controller",
                ),
                count_suggested_bindings=len(self.suggested_bindings),
                suggested_bindings=self.suggested_bindings,
            ),
        )
        self.action_spaces = [
            xr.create_action_space(
                session=session,
                create_info=xr.ActionSpaceCreateInfo(
                    action=self.controller_pose_action,
                    subaction_path=self.controller_paths[0],
                ),
            ),
            xr.create_action_space(
                session=session,
                create_info=xr.ActionSpaceCreateInfo(
                    action=self.controller_pose_action,
                    subaction_path=self.controller_paths[1],
                ),
            ),
        ]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.action_set is not None:
            xr.destroy_action_set(self.action_set)
            self.action_set = None

    def enumerate_active_controllers(
            self,
            time: xr.Time,
            reference_space: xr.Space,
    ) -> Generator[Tuple[int, xr.SpaceLocation], None, None]:
        try:
            active_action_set = xr.ActiveActionSet(
                action_set=self.action_set,
                subaction_path=xr.NULL_PATH,
            )
            xr.sync_actions(
                session=self.session,
                sync_info=xr.ActionsSyncInfo(
                    active_action_sets=[active_action_set],
                ),
            )
            for index, space in enumerate(self.action_spaces):
                space_location = xr.locate_space(
                    space=space,
                    base_space=reference_space,
                    time=time,
                )
                yield index, space_location
        except xr.exception.SessionNotFocused:
            # Sometimes (due to race condition?) the session is no longer focused when we get here
            yield from []


__all__ = [
    "TwoControllers"
]
