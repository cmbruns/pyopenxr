from __future__ import annotations  # To support python 3.9+ style array type annotations
# Warning: this file is auto-generated. Do not edit.

from ctypes import Array, POINTER, byref, c_char, c_int64, c_uint32, cast, create_string_buffer

"""
File xr.functions.py

Defines high-level pythonic function definitions for pyopenxr.
"""

from . import raw_functions
from .enums import *
from .exception import check_result
from .typedefs import *


def get_instance_proc_addr(
    instance: Instance,
    name: str,
) -> PFN_xrVoidFunction:
    """"""
    if name is not None:
        name = name.encode()
    function = PFN_xrVoidFunction()
    fxn = raw_functions.xrGetInstanceProcAddr
    result = check_result(fxn(
        instance,
        name,
        byref(function),
    ))
    if result.is_exception():
        raise result
    return function


def enumerate_api_layer_properties(
) -> Array[ApiLayerProperties]:
    """"""
    property_capacity_input = c_uint32(0)
    fxn = raw_functions.xrEnumerateApiLayerProperties
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        0,
        byref(property_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    properties = (ApiLayerProperties * property_capacity_input.value)(*([ApiLayerProperties()] * property_capacity_input.value))
    result = check_result(fxn(
        property_capacity_input,
        byref(property_capacity_input),
        properties,
    ))
    if result.is_exception():
        raise result
    return properties


def enumerate_instance_extension_properties(
    layer_name: str = None,
) -> Array[ExtensionProperties]:
    """"""
    if layer_name is not None:
        layer_name = layer_name.encode()
    property_capacity_input = c_uint32(0)
    fxn = raw_functions.xrEnumerateInstanceExtensionProperties
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        layer_name,
        0,
        byref(property_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    properties = (ExtensionProperties * property_capacity_input.value)(*([ExtensionProperties()] * property_capacity_input.value))
    result = check_result(fxn(
        layer_name,
        property_capacity_input,
        byref(property_capacity_input),
        properties,
    ))
    if result.is_exception():
        raise result
    return properties


def create_instance(
    create_info: InstanceCreateInfo = None,
) -> Instance:
    """"""
    if create_info is None:
        create_info = InstanceCreateInfo()
    instance = Instance()
    fxn = raw_functions.xrCreateInstance
    result = check_result(fxn(
        create_info,
        byref(instance),
    ))
    if result.is_exception():
        raise result
    return instance


def destroy_instance(
    instance: Instance,
) -> None:
    """"""
    fxn = raw_functions.xrDestroyInstance
    result = check_result(fxn(
        instance,
    ))
    if result.is_exception():
        raise result


def get_instance_properties(
    instance: Instance,
) -> InstanceProperties:
    """"""
    instance_properties = InstanceProperties()
    fxn = raw_functions.xrGetInstanceProperties
    result = check_result(fxn(
        instance,
        byref(instance_properties),
    ))
    if result.is_exception():
        raise result
    return instance_properties


def poll_event(
    instance: Instance,
) -> EventDataBuffer:
    """"""
    event_data = EventDataBuffer()
    fxn = raw_functions.xrPollEvent
    result = check_result(fxn(
        instance,
        byref(event_data),
    ))
    if result.is_exception():
        raise result
    return event_data


def result_to_string(
    instance: Instance,
    value: Result,
    buffer: (c_char * 64),
) -> None:
    """"""
    fxn = raw_functions.xrResultToString
    result = check_result(fxn(
        instance,
        value.value,
        buffer,
    ))
    if result.is_exception():
        raise result


def structure_type_to_string(
    instance: Instance,
    value: StructureType,
    buffer: (c_char * 64),
) -> None:
    """"""
    fxn = raw_functions.xrStructureTypeToString
    result = check_result(fxn(
        instance,
        value.value,
        buffer,
    ))
    if result.is_exception():
        raise result


def get_system(
    instance: Instance,
    get_info: SystemGetInfo,
) -> SystemId:
    """"""
    system_id = SystemId()
    fxn = raw_functions.xrGetSystem
    result = check_result(fxn(
        instance,
        get_info,
        byref(system_id),
    ))
    if result.is_exception():
        raise result
    return system_id


def get_system_properties(
    instance: Instance,
    system_id: SystemId,
) -> SystemProperties:
    """"""
    properties = SystemProperties()
    fxn = raw_functions.xrGetSystemProperties
    result = check_result(fxn(
        instance,
        system_id,
        byref(properties),
    ))
    if result.is_exception():
        raise result
    return properties


def enumerate_environment_blend_modes(
    instance: Instance,
    system_id: SystemId,
    view_configuration_type: ViewConfigurationType,
) -> Array[EnvironmentBlendMode.ctype()]:
    """"""
    environment_blend_mode_capacity_input = c_uint32(0)
    fxn = raw_functions.xrEnumerateEnvironmentBlendModes
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        instance,
        system_id,
        view_configuration_type.value,
        0,
        byref(environment_blend_mode_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    environment_blend_modes = (EnvironmentBlendMode.ctype() * environment_blend_mode_capacity_input.value)(*([EnvironmentBlendMode.ctype()()] * environment_blend_mode_capacity_input.value))
    result = check_result(fxn(
        instance,
        system_id,
        view_configuration_type.value,
        environment_blend_mode_capacity_input,
        byref(environment_blend_mode_capacity_input),
        environment_blend_modes,
    ))
    if result.is_exception():
        raise result
    return environment_blend_modes


def create_session(
    instance: Instance,
    create_info: SessionCreateInfo = None,
) -> Session:
    """"""
    if create_info is None:
        create_info = SessionCreateInfo()
    session = Session()
    fxn = raw_functions.xrCreateSession
    result = check_result(fxn(
        instance,
        create_info,
        byref(session),
    ))
    if result.is_exception():
        raise result
    return session


def destroy_session(
    session: Session,
) -> None:
    """"""
    fxn = raw_functions.xrDestroySession
    result = check_result(fxn(
        session,
    ))
    if result.is_exception():
        raise result


def enumerate_reference_spaces(
    session: Session,
) -> Array[ReferenceSpaceType.ctype()]:
    """"""
    space_capacity_input = c_uint32(0)
    fxn = raw_functions.xrEnumerateReferenceSpaces
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        session,
        0,
        byref(space_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    spaces = (ReferenceSpaceType.ctype() * space_capacity_input.value)(*([ReferenceSpaceType.ctype()()] * space_capacity_input.value))
    result = check_result(fxn(
        session,
        space_capacity_input,
        byref(space_capacity_input),
        spaces,
    ))
    if result.is_exception():
        raise result
    return spaces


def create_reference_space(
    session: Session,
    create_info: ReferenceSpaceCreateInfo = None,
) -> Space:
    """"""
    if create_info is None:
        create_info = ReferenceSpaceCreateInfo()
    space = Space()
    fxn = raw_functions.xrCreateReferenceSpace
    result = check_result(fxn(
        session,
        create_info,
        byref(space),
    ))
    if result.is_exception():
        raise result
    return space


def get_reference_space_bounds_rect(
    session: Session,
    reference_space_type: ReferenceSpaceType,
) -> Extent2Df:
    """"""
    bounds = Extent2Df()
    fxn = raw_functions.xrGetReferenceSpaceBoundsRect
    result = check_result(fxn(
        session,
        reference_space_type.value,
        byref(bounds),
    ))
    if result.is_exception():
        raise result
    return bounds


def create_action_space(
    session: Session,
    create_info: ActionSpaceCreateInfo = None,
) -> Space:
    """"""
    if create_info is None:
        create_info = ActionSpaceCreateInfo()
    space = Space()
    fxn = raw_functions.xrCreateActionSpace
    result = check_result(fxn(
        session,
        create_info,
        byref(space),
    ))
    if result.is_exception():
        raise result
    return space


def locate_space(
    space: Space,
    base_space: Space,
    time: Time,
) -> SpaceLocation:
    """"""
    location = SpaceLocation()
    fxn = raw_functions.xrLocateSpace
    result = check_result(fxn(
        space,
        base_space,
        time,
        byref(location),
    ))
    if result.is_exception():
        raise result
    return location


def destroy_space(
    space: Space,
) -> None:
    """"""
    fxn = raw_functions.xrDestroySpace
    result = check_result(fxn(
        space,
    ))
    if result.is_exception():
        raise result


def enumerate_view_configurations(
    instance: Instance,
    system_id: SystemId,
) -> Array[ViewConfigurationType.ctype()]:
    """"""
    view_configuration_type_capacity_input = c_uint32(0)
    fxn = raw_functions.xrEnumerateViewConfigurations
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        instance,
        system_id,
        0,
        byref(view_configuration_type_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    view_configuration_types = (ViewConfigurationType.ctype() * view_configuration_type_capacity_input.value)(*([ViewConfigurationType.ctype()()] * view_configuration_type_capacity_input.value))
    result = check_result(fxn(
        instance,
        system_id,
        view_configuration_type_capacity_input,
        byref(view_configuration_type_capacity_input),
        view_configuration_types,
    ))
    if result.is_exception():
        raise result
    return view_configuration_types


def get_view_configuration_properties(
    instance: Instance,
    system_id: SystemId,
    view_configuration_type: ViewConfigurationType,
) -> ViewConfigurationProperties:
    """"""
    configuration_properties = ViewConfigurationProperties()
    fxn = raw_functions.xrGetViewConfigurationProperties
    result = check_result(fxn(
        instance,
        system_id,
        view_configuration_type.value,
        byref(configuration_properties),
    ))
    if result.is_exception():
        raise result
    return configuration_properties


def enumerate_view_configuration_views(
    instance: Instance,
    system_id: SystemId,
    view_configuration_type: ViewConfigurationType,
) -> Array[ViewConfigurationView]:
    """"""
    view_capacity_input = c_uint32(0)
    fxn = raw_functions.xrEnumerateViewConfigurationViews
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        instance,
        system_id,
        view_configuration_type.value,
        0,
        byref(view_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    views = (ViewConfigurationView * view_capacity_input.value)(*([ViewConfigurationView()] * view_capacity_input.value))
    result = check_result(fxn(
        instance,
        system_id,
        view_configuration_type.value,
        view_capacity_input,
        byref(view_capacity_input),
        views,
    ))
    if result.is_exception():
        raise result
    return views


def enumerate_swapchain_formats(
    session: Session,
) -> Array[c_int64]:
    """"""
    format_capacity_input = c_uint32(0)
    fxn = raw_functions.xrEnumerateSwapchainFormats
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        session,
        0,
        byref(format_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    formats = (c_int64 * format_capacity_input.value)(*([c_int64()] * format_capacity_input.value))
    result = check_result(fxn(
        session,
        format_capacity_input,
        byref(format_capacity_input),
        formats,
    ))
    if result.is_exception():
        raise result
    return formats


def create_swapchain(
    session: Session,
    create_info: SwapchainCreateInfo = None,
) -> Swapchain:
    """"""
    if create_info is None:
        create_info = SwapchainCreateInfo()
    swapchain = Swapchain()
    fxn = raw_functions.xrCreateSwapchain
    result = check_result(fxn(
        session,
        create_info,
        byref(swapchain),
    ))
    if result.is_exception():
        raise result
    return swapchain


def destroy_swapchain(
    swapchain: Swapchain,
) -> None:
    """"""
    fxn = raw_functions.xrDestroySwapchain
    result = check_result(fxn(
        swapchain,
    ))
    if result.is_exception():
        raise result


def enumerate_swapchain_images(
    swapchain: Swapchain,
    element_type: type,
) -> Array[SwapchainImageBaseHeader]:
    """"""
    image_capacity_input = c_uint32(0)
    fxn = raw_functions.xrEnumerateSwapchainImages
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        swapchain,
        0,
        byref(image_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    images = (element_type * image_capacity_input.value)(*([element_type()] * image_capacity_input.value))
    result = check_result(fxn(
        swapchain,
        image_capacity_input,
        byref(image_capacity_input),
        cast(images, POINTER(SwapchainImageBaseHeader)),
    ))
    if result.is_exception():
        raise result
    return images


def acquire_swapchain_image(
    swapchain: Swapchain,
    acquire_info: SwapchainImageAcquireInfo = None,
) -> int:
    """"""
    index = c_uint32()
    fxn = raw_functions.xrAcquireSwapchainImage
    result = check_result(fxn(
        swapchain,
        acquire_info,
        byref(index),
    ))
    if result.is_exception():
        raise result
    return index.value


def wait_swapchain_image(
    swapchain: Swapchain,
    wait_info: SwapchainImageWaitInfo,
) -> None:
    """"""
    fxn = raw_functions.xrWaitSwapchainImage
    result = check_result(fxn(
        swapchain,
        wait_info,
    ))
    if result.is_exception():
        raise result


def release_swapchain_image(
    swapchain: Swapchain,
    release_info: SwapchainImageReleaseInfo = None,
) -> None:
    """"""
    fxn = raw_functions.xrReleaseSwapchainImage
    result = check_result(fxn(
        swapchain,
        release_info,
    ))
    if result.is_exception():
        raise result


def begin_session(
    session: Session,
    begin_info: SessionBeginInfo,
) -> None:
    """"""
    fxn = raw_functions.xrBeginSession
    result = check_result(fxn(
        session,
        begin_info,
    ))
    if result.is_exception():
        raise result


def end_session(
    session: Session,
) -> None:
    """"""
    fxn = raw_functions.xrEndSession
    result = check_result(fxn(
        session,
    ))
    if result.is_exception():
        raise result


def request_exit_session(
    session: Session,
) -> None:
    """"""
    fxn = raw_functions.xrRequestExitSession
    result = check_result(fxn(
        session,
    ))
    if result.is_exception():
        raise result


def wait_frame(
    session: Session,
    frame_wait_info: FrameWaitInfo = None,
) -> FrameState:
    """"""
    frame_state = FrameState()
    fxn = raw_functions.xrWaitFrame
    result = check_result(fxn(
        session,
        frame_wait_info,
        byref(frame_state),
    ))
    if result.is_exception():
        raise result
    return frame_state


def begin_frame(
    session: Session,
    frame_begin_info: FrameBeginInfo = None,
) -> None:
    """"""
    fxn = raw_functions.xrBeginFrame
    result = check_result(fxn(
        session,
        frame_begin_info,
    ))
    if result.is_exception():
        raise result


def end_frame(
    session: Session,
    frame_end_info: FrameEndInfo,
) -> None:
    """"""
    fxn = raw_functions.xrEndFrame
    result = check_result(fxn(
        session,
        frame_end_info,
    ))
    if result.is_exception():
        raise result


def locate_views(
    session: Session,
    view_locate_info: ViewLocateInfo,
) -> (ViewState, Array[View]):
    """"""
    view_state = ViewState()
    view_capacity_input = c_uint32(0)
    fxn = raw_functions.xrLocateViews
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        session,
        view_locate_info,
        byref(view_state),
        0,
        byref(view_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    views = (View * view_capacity_input.value)(*([View()] * view_capacity_input.value))
    result = check_result(fxn(
        session,
        view_locate_info,
        byref(view_state),
        view_capacity_input,
        byref(view_capacity_input),
        views,
    ))
    if result.is_exception():
        raise result
    return view_state, views


def string_to_path(
    instance: Instance,
    path_string: str,
) -> Path:
    """"""
    if path_string is not None:
        path_string = path_string.encode()
    path = Path()
    fxn = raw_functions.xrStringToPath
    result = check_result(fxn(
        instance,
        path_string,
        byref(path),
    ))
    if result.is_exception():
        raise result
    return path


def path_to_string(
    instance: Instance,
    path: Path,
) -> str:
    """"""
    buffer_capacity_input = c_uint32(0)
    fxn = raw_functions.xrPathToString
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        instance,
        path,
        0,
        byref(buffer_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    buffer = create_string_buffer(buffer_capacity_input.value)
    result = check_result(fxn(
        instance,
        path,
        buffer_capacity_input,
        byref(buffer_capacity_input),
        buffer,
    ))
    if result.is_exception():
        raise result
    return buffer.value.decode()


def create_action_set(
    instance: Instance,
    create_info: ActionSetCreateInfo = None,
) -> ActionSet:
    """"""
    if create_info is None:
        create_info = ActionSetCreateInfo()
    action_set = ActionSet()
    fxn = raw_functions.xrCreateActionSet
    result = check_result(fxn(
        instance,
        create_info,
        byref(action_set),
    ))
    if result.is_exception():
        raise result
    return action_set


def destroy_action_set(
    action_set: ActionSet,
) -> None:
    """"""
    fxn = raw_functions.xrDestroyActionSet
    result = check_result(fxn(
        action_set,
    ))
    if result.is_exception():
        raise result


def create_action(
    action_set: ActionSet,
    create_info: ActionCreateInfo = None,
) -> Action:
    """"""
    if create_info is None:
        create_info = ActionCreateInfo()
    action = Action()
    fxn = raw_functions.xrCreateAction
    result = check_result(fxn(
        action_set,
        create_info,
        byref(action),
    ))
    if result.is_exception():
        raise result
    return action


def destroy_action(
    action: Action,
) -> None:
    """"""
    fxn = raw_functions.xrDestroyAction
    result = check_result(fxn(
        action,
    ))
    if result.is_exception():
        raise result


def suggest_interaction_profile_bindings(
    instance: Instance,
    suggested_bindings: InteractionProfileSuggestedBinding,
) -> None:
    """"""
    fxn = raw_functions.xrSuggestInteractionProfileBindings
    result = check_result(fxn(
        instance,
        suggested_bindings,
    ))
    if result.is_exception():
        raise result


def attach_session_action_sets(
    session: Session,
    attach_info: SessionActionSetsAttachInfo,
) -> None:
    """"""
    fxn = raw_functions.xrAttachSessionActionSets
    result = check_result(fxn(
        session,
        attach_info,
    ))
    if result.is_exception():
        raise result


def get_current_interaction_profile(
    session: Session,
    top_level_user_path: Path,
) -> InteractionProfileState:
    """"""
    interaction_profile = InteractionProfileState()
    fxn = raw_functions.xrGetCurrentInteractionProfile
    result = check_result(fxn(
        session,
        top_level_user_path,
        byref(interaction_profile),
    ))
    if result.is_exception():
        raise result
    return interaction_profile


def get_action_state_boolean(
    session: Session,
    get_info: ActionStateGetInfo,
) -> ActionStateBoolean:
    """"""
    state = ActionStateBoolean()
    fxn = raw_functions.xrGetActionStateBoolean
    result = check_result(fxn(
        session,
        get_info,
        byref(state),
    ))
    if result.is_exception():
        raise result
    return state


def get_action_state_float(
    session: Session,
    get_info: ActionStateGetInfo,
) -> ActionStateFloat:
    """"""
    state = ActionStateFloat()
    fxn = raw_functions.xrGetActionStateFloat
    result = check_result(fxn(
        session,
        get_info,
        byref(state),
    ))
    if result.is_exception():
        raise result
    return state


def get_action_state_vector2f(
    session: Session,
    get_info: ActionStateGetInfo,
) -> ActionStateVector2f:
    """"""
    state = ActionStateVector2f()
    fxn = raw_functions.xrGetActionStateVector2f
    result = check_result(fxn(
        session,
        get_info,
        byref(state),
    ))
    if result.is_exception():
        raise result
    return state


def get_action_state_pose(
    session: Session,
    get_info: ActionStateGetInfo,
) -> ActionStatePose:
    """"""
    state = ActionStatePose()
    fxn = raw_functions.xrGetActionStatePose
    result = check_result(fxn(
        session,
        get_info,
        byref(state),
    ))
    if result.is_exception():
        raise result
    return state


def sync_actions(
    session: Session,
    sync_info: ActionsSyncInfo,
) -> None:
    """"""
    fxn = raw_functions.xrSyncActions
    result = check_result(fxn(
        session,
        sync_info,
    ))
    if result.is_exception():
        raise result


def enumerate_bound_sources_for_action(
    session: Session,
    enumerate_info: BoundSourcesForActionEnumerateInfo,
) -> Array[Path]:
    """"""
    source_capacity_input = c_uint32(0)
    fxn = raw_functions.xrEnumerateBoundSourcesForAction
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        session,
        enumerate_info,
        0,
        byref(source_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    sources = (Path * source_capacity_input.value)(*([Path()] * source_capacity_input.value))
    result = check_result(fxn(
        session,
        enumerate_info,
        source_capacity_input,
        byref(source_capacity_input),
        sources,
    ))
    if result.is_exception():
        raise result
    return sources


def get_input_source_localized_name(
    session: Session,
    get_info: InputSourceLocalizedNameGetInfo,
) -> str:
    """"""
    buffer_capacity_input = c_uint32(0)
    fxn = raw_functions.xrGetInputSourceLocalizedName
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        session,
        get_info,
        0,
        byref(buffer_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    buffer = create_string_buffer(buffer_capacity_input.value)
    result = check_result(fxn(
        session,
        get_info,
        buffer_capacity_input,
        byref(buffer_capacity_input),
        buffer,
    ))
    if result.is_exception():
        raise result
    return buffer.value.decode()


def apply_haptic_feedback(
    session: Session,
    haptic_action_info: HapticActionInfo,
    haptic_feedback: HapticBaseHeader,
) -> None:
    """"""
    fxn = raw_functions.xrApplyHapticFeedback
    result = check_result(fxn(
        session,
        haptic_action_info,
        haptic_feedback,
    ))
    if result.is_exception():
        raise result


def stop_haptic_feedback(
    session: Session,
    haptic_action_info: HapticActionInfo,
) -> None:
    """"""
    fxn = raw_functions.xrStopHapticFeedback
    result = check_result(fxn(
        session,
        haptic_action_info,
    ))
    if result.is_exception():
        raise result


__all__ = [
    "acquire_swapchain_image",
    "apply_haptic_feedback",
    "attach_session_action_sets",
    "begin_frame",
    "begin_session",
    "create_action",
    "create_action_set",
    "create_action_space",
    "create_instance",
    "create_reference_space",
    "create_session",
    "create_swapchain",
    "destroy_action",
    "destroy_action_set",
    "destroy_instance",
    "destroy_session",
    "destroy_space",
    "destroy_swapchain",
    "end_frame",
    "end_session",
    "enumerate_api_layer_properties",
    "enumerate_bound_sources_for_action",
    "enumerate_environment_blend_modes",
    "enumerate_instance_extension_properties",
    "enumerate_reference_spaces",
    "enumerate_swapchain_formats",
    "enumerate_swapchain_images",
    "enumerate_view_configuration_views",
    "enumerate_view_configurations",
    "get_action_state_boolean",
    "get_action_state_float",
    "get_action_state_pose",
    "get_action_state_vector2f",
    "get_current_interaction_profile",
    "get_input_source_localized_name",
    "get_instance_proc_addr",
    "get_instance_properties",
    "get_reference_space_bounds_rect",
    "get_system",
    "get_system_properties",
    "get_view_configuration_properties",
    "locate_space",
    "locate_views",
    "path_to_string",
    "poll_event",
    "release_swapchain_image",
    "request_exit_session",
    "result_to_string",
    "stop_haptic_feedback",
    "string_to_path",
    "structure_type_to_string",
    "suggest_interaction_profile_bindings",
    "sync_actions",
    "wait_frame",
    "wait_swapchain_image",
]
