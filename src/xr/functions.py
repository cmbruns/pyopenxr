# Warning: this file is auto-generated. Do not edit.

from ctypes import POINTER, c_char, c_int64, c_uint32

"""
File xr.functions.py

Defines high-level pythonic function definitions for pyopenxr.
"""

from ctypes import Array, byref, create_string_buffer

from . import raw_functions
from .enums import *
from .exceptions import check_result
from .typedefs import *


def get_instance_proc_addr(
    instance: Instance,
    name: str,
    function: POINTER(PFN_xrVoidFunction),
) -> None:
    """"""
    if name is not None:
        name = name.encode()
    fxn = raw_functions.xrGetInstanceProcAddr
    result = check_result(fxn(
        instance,
        name,
        function,
    ))
    if result.is_exception():
        raise result


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
    properties = ApiLayerProperties.make_array(property_capacity_input.value)
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
    properties = ExtensionProperties.make_array(property_capacity_input.value)
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
    create_info: POINTER(InstanceCreateInfo),
    instance: POINTER(Instance),
) -> None:
    """"""
    fxn = raw_functions.xrCreateInstance
    result = check_result(fxn(
        create_info,
        instance,
    ))
    if result.is_exception():
        raise result


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
    instance_properties: POINTER(InstanceProperties),
) -> None:
    """"""
    fxn = raw_functions.xrGetInstanceProperties
    result = check_result(fxn(
        instance,
        instance_properties,
    ))
    if result.is_exception():
        raise result


def poll_event(
    instance: Instance,
    event_data: POINTER(EventDataBuffer),
) -> None:
    """"""
    fxn = raw_functions.xrPollEvent
    result = check_result(fxn(
        instance,
        event_data,
    ))
    if result.is_exception():
        raise result


def result_to_string(
    instance: Instance,
    value: Result,
    buffer: (c_char * 64),
) -> None:
    """"""
    fxn = raw_functions.xrResultToString
    result = check_result(fxn(
        instance,
        value,
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
        value,
        buffer,
    ))
    if result.is_exception():
        raise result


def get_system(
    instance: Instance,
    get_info: POINTER(SystemGetInfo),
    system_id: POINTER(SystemId),
) -> None:
    """"""
    fxn = raw_functions.xrGetSystem
    result = check_result(fxn(
        instance,
        get_info,
        system_id,
    ))
    if result.is_exception():
        raise result


def get_system_properties(
    instance: Instance,
    system_id: SystemId,
    properties: POINTER(SystemProperties),
) -> None:
    """"""
    fxn = raw_functions.xrGetSystemProperties
    result = check_result(fxn(
        instance,
        system_id,
        properties,
    ))
    if result.is_exception():
        raise result


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
        view_configuration_type,
        0,
        byref(environment_blend_mode_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    environment_blend_modes = EnvironmentBlendMode.ctype().make_array(environment_blend_mode_capacity_input.value)
    result = check_result(fxn(
        instance,
        system_id,
        view_configuration_type,
        environment_blend_mode_capacity_input,
        byref(environment_blend_mode_capacity_input),
        environment_blend_modes,
    ))
    if result.is_exception():
        raise result
    return environment_blend_modes


def create_session(
    instance: Instance,
    create_info: POINTER(SessionCreateInfo),
    session: POINTER(Session),
) -> None:
    """"""
    fxn = raw_functions.xrCreateSession
    result = check_result(fxn(
        instance,
        create_info,
        session,
    ))
    if result.is_exception():
        raise result


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
    spaces = ReferenceSpaceType.ctype().make_array(space_capacity_input.value)
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
    create_info: POINTER(ReferenceSpaceCreateInfo),
    space: POINTER(Space),
) -> None:
    """"""
    fxn = raw_functions.xrCreateReferenceSpace
    result = check_result(fxn(
        session,
        create_info,
        space,
    ))
    if result.is_exception():
        raise result


def get_reference_space_bounds_rect(
    session: Session,
    reference_space_type: ReferenceSpaceType,
    bounds: POINTER(Extent2Df),
) -> None:
    """"""
    fxn = raw_functions.xrGetReferenceSpaceBoundsRect
    result = check_result(fxn(
        session,
        reference_space_type,
        bounds,
    ))
    if result.is_exception():
        raise result


def create_action_space(
    session: Session,
    create_info: POINTER(ActionSpaceCreateInfo),
    space: POINTER(Space),
) -> None:
    """"""
    fxn = raw_functions.xrCreateActionSpace
    result = check_result(fxn(
        session,
        create_info,
        space,
    ))
    if result.is_exception():
        raise result


def locate_space(
    space: Space,
    base_space: Space,
    time: Time,
    location: POINTER(SpaceLocation),
) -> None:
    """"""
    fxn = raw_functions.xrLocateSpace
    result = check_result(fxn(
        space,
        base_space,
        time,
        location,
    ))
    if result.is_exception():
        raise result


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
    view_configuration_types = ViewConfigurationType.ctype().make_array(view_configuration_type_capacity_input.value)
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
    configuration_properties: POINTER(ViewConfigurationProperties),
) -> None:
    """"""
    fxn = raw_functions.xrGetViewConfigurationProperties
    result = check_result(fxn(
        instance,
        system_id,
        view_configuration_type,
        configuration_properties,
    ))
    if result.is_exception():
        raise result


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
        view_configuration_type,
        0,
        byref(view_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    views = ViewConfigurationView.make_array(view_capacity_input.value)
    result = check_result(fxn(
        instance,
        system_id,
        view_configuration_type,
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
    formats = (c_int64 * format_capacity_input.value)()
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
    create_info: POINTER(SwapchainCreateInfo),
    swapchain: POINTER(Swapchain),
) -> None:
    """"""
    fxn = raw_functions.xrCreateSwapchain
    result = check_result(fxn(
        session,
        create_info,
        swapchain,
    ))
    if result.is_exception():
        raise result


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
    images = SwapchainImageBaseHeader.make_array(image_capacity_input.value)
    result = check_result(fxn(
        swapchain,
        image_capacity_input,
        byref(image_capacity_input),
        images,
    ))
    if result.is_exception():
        raise result
    return images


def acquire_swapchain_image(
    swapchain: Swapchain,
    acquire_info: POINTER(SwapchainImageAcquireInfo),
    index: POINTER(c_uint32),
) -> None:
    """"""
    fxn = raw_functions.xrAcquireSwapchainImage
    result = check_result(fxn(
        swapchain,
        acquire_info,
        index,
    ))
    if result.is_exception():
        raise result


def wait_swapchain_image(
    swapchain: Swapchain,
    wait_info: POINTER(SwapchainImageWaitInfo),
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
    release_info: POINTER(SwapchainImageReleaseInfo) = None,
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
    begin_info: POINTER(SessionBeginInfo),
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
    frame_wait_info: POINTER(FrameWaitInfo),
    frame_state: POINTER(FrameState),
) -> None:
    """"""
    fxn = raw_functions.xrWaitFrame
    result = check_result(fxn(
        session,
        frame_wait_info,
        frame_state,
    ))
    if result.is_exception():
        raise result


def begin_frame(
    session: Session,
    frame_begin_info: POINTER(FrameBeginInfo) = None,
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
    frame_end_info: POINTER(FrameEndInfo),
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
    view_locate_info: POINTER(ViewLocateInfo),
    view_state: POINTER(ViewState),
) -> Array[View]:
    """"""
    view_capacity_input = c_uint32(0)
    fxn = raw_functions.xrLocateViews
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        session,
        view_locate_info,
        view_state,
        0,
        byref(view_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    views = View.make_array(view_capacity_input.value)
    result = check_result(fxn(
        session,
        view_locate_info,
        view_state,
        view_capacity_input,
        byref(view_capacity_input),
        views,
    ))
    if result.is_exception():
        raise result
    return views


def string_to_path(
    instance: Instance,
    path_string: str,
    path: POINTER(Path),
) -> None:
    """"""
    if path_string is not None:
        path_string = path_string.encode()
    fxn = raw_functions.xrStringToPath
    result = check_result(fxn(
        instance,
        path_string,
        path,
    ))
    if result.is_exception():
        raise result


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
    create_info: POINTER(ActionSetCreateInfo),
    action_set: POINTER(ActionSet),
) -> None:
    """"""
    fxn = raw_functions.xrCreateActionSet
    result = check_result(fxn(
        instance,
        create_info,
        action_set,
    ))
    if result.is_exception():
        raise result


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
    create_info: POINTER(ActionCreateInfo),
    action: POINTER(Action),
) -> None:
    """"""
    fxn = raw_functions.xrCreateAction
    result = check_result(fxn(
        action_set,
        create_info,
        action,
    ))
    if result.is_exception():
        raise result


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
    suggested_bindings: POINTER(InteractionProfileSuggestedBinding),
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
    attach_info: POINTER(SessionActionSetsAttachInfo),
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
    interaction_profile: POINTER(InteractionProfileState),
) -> None:
    """"""
    fxn = raw_functions.xrGetCurrentInteractionProfile
    result = check_result(fxn(
        session,
        top_level_user_path,
        interaction_profile,
    ))
    if result.is_exception():
        raise result


def get_action_state_boolean(
    session: Session,
    get_info: POINTER(ActionStateGetInfo),
    state: POINTER(ActionStateBoolean),
) -> None:
    """"""
    fxn = raw_functions.xrGetActionStateBoolean
    result = check_result(fxn(
        session,
        get_info,
        state,
    ))
    if result.is_exception():
        raise result


def get_action_state_float(
    session: Session,
    get_info: POINTER(ActionStateGetInfo),
    state: POINTER(ActionStateFloat),
) -> None:
    """"""
    fxn = raw_functions.xrGetActionStateFloat
    result = check_result(fxn(
        session,
        get_info,
        state,
    ))
    if result.is_exception():
        raise result


def get_action_state_vector2f(
    session: Session,
    get_info: POINTER(ActionStateGetInfo),
    state: POINTER(ActionStateVector2f),
) -> None:
    """"""
    fxn = raw_functions.xrGetActionStateVector2f
    result = check_result(fxn(
        session,
        get_info,
        state,
    ))
    if result.is_exception():
        raise result


def get_action_state_pose(
    session: Session,
    get_info: POINTER(ActionStateGetInfo),
    state: POINTER(ActionStatePose),
) -> None:
    """"""
    fxn = raw_functions.xrGetActionStatePose
    result = check_result(fxn(
        session,
        get_info,
        state,
    ))
    if result.is_exception():
        raise result


def sync_actions(
    session: Session,
    sync_info: POINTER(ActionsSyncInfo),
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
    enumerate_info: POINTER(BoundSourcesForActionEnumerateInfo),
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
    sources = Path.make_array(source_capacity_input.value)
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
    get_info: POINTER(InputSourceLocalizedNameGetInfo),
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
    haptic_action_info: POINTER(HapticActionInfo),
    haptic_feedback: POINTER(HapticBaseHeader),
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
    haptic_action_info: POINTER(HapticActionInfo),
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
    "get_instance_proc_addr",
    "enumerate_api_layer_properties",
    "enumerate_instance_extension_properties",
    "create_instance",
    "destroy_instance",
    "get_instance_properties",
    "poll_event",
    "result_to_string",
    "structure_type_to_string",
    "get_system",
    "get_system_properties",
    "enumerate_environment_blend_modes",
    "create_session",
    "destroy_session",
    "enumerate_reference_spaces",
    "create_reference_space",
    "get_reference_space_bounds_rect",
    "create_action_space",
    "locate_space",
    "destroy_space",
    "enumerate_view_configurations",
    "get_view_configuration_properties",
    "enumerate_view_configuration_views",
    "enumerate_swapchain_formats",
    "create_swapchain",
    "destroy_swapchain",
    "enumerate_swapchain_images",
    "acquire_swapchain_image",
    "wait_swapchain_image",
    "release_swapchain_image",
    "begin_session",
    "end_session",
    "request_exit_session",
    "wait_frame",
    "begin_frame",
    "end_frame",
    "locate_views",
    "string_to_path",
    "path_to_string",
    "create_action_set",
    "destroy_action_set",
    "create_action",
    "destroy_action",
    "suggest_interaction_profile_bindings",
    "attach_session_action_sets",
    "get_current_interaction_profile",
    "get_action_state_boolean",
    "get_action_state_float",
    "get_action_state_vector2f",
    "get_action_state_pose",
    "sync_actions",
    "enumerate_bound_sources_for_action",
    "get_input_source_localized_name",
    "apply_haptic_feedback",
    "stop_haptic_feedback",
]
