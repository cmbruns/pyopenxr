# Warning: this file is auto-generated. Do not edit.

from ctypes import (
    POINTER, byref, c_char, c_float, c_int, c_int64, c_uint16, c_uint32,
    c_uint64, c_uint8, cast, create_string_buffer,
)
from typing import Sequence, TypeVar, Type

"""
File xr.functions.py

Defines high-level pythonic function definitions for pyopenxr.
"""

from . import raw_functions
from .enums import *
from .exception import check_result
from .typedefs import *
from .constants import NULL_HANDLE

SWAPCHAIN_IMAGE_TYPE = TypeVar("SWAPCHAIN_IMAGE_TYPE")


def get_instance_proc_addr(
    instance: Instance,
    name: str,
) -> PFN_xrVoidFunction:
    """
    Retrieve a function pointer for an OpenXR core or extension function.
    
    This function wraps the native `xrGetInstanceProcAddr` call, allowing dynamic access
    to OpenXR API functions. It returns a raw function pointer that must be cast to the
    appropriate callable type before use.
    
    If `instance` is `None`, only a limited set of functions may be queried:
    - `xrEnumerateInstanceExtensionProperties`
    - `xrEnumerateApiLayerProperties`
    - `xrCreateInstance`
    
    For extension functions, the corresponding extension must have been enabled during
    instance creation via `enabled_extension_names`.
    
    :param instance: The OpenXR instance handle, or `None` for pre-instance functions.
    :type instance: xr.Instance
    :param name: The name of the function to query (e.g. "xrCreateSession").
    :type name: str
    :return: A raw function pointer (`PFN_xrVoidFunction`) to the requested API function.
    :rtype: xr.PFN_xrVoidFunction
    :raises xr.FunctionUnsupportedError: If the function name is not recognized or not supported.
    :raises xr.HandleInvalidError: If the provided instance handle is invalid.
    :raises xr.InstanceLossPendingError: If the instance is in a loss-pending state.
    :raises xr.InitializationFailedError: If the runtime failed to initialize the query.
    :raises xr.RuntimeFailureError: For general runtime failure not covered by other error codes.
    :seealso: :class:`xr.PFN_xrVoidFunction`
    """
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
) -> Sequence[ApiLayerProperties]:
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
    properties = (ApiLayerProperties * property_capacity_input.value)(*([ApiLayerProperties()] * property_capacity_input.value))  # noqa
    result = check_result(fxn(
        property_capacity_input,
        byref(property_capacity_input),
        properties,
    ))
    if result.is_exception():
        raise result
    return properties  # noqa


def enumerate_instance_extension_properties(
    layer_name: str = None,
) -> Sequence[ExtensionProperties]:
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
    properties = (ExtensionProperties * property_capacity_input.value)(*([ExtensionProperties()] * property_capacity_input.value))  # noqa
    result = check_result(fxn(
        layer_name,
        property_capacity_input,
        byref(property_capacity_input),
        properties,
    ))
    if result.is_exception():
        raise result
    return properties  # noqa


def create_instance(
    create_info: InstanceCreateInfo = None,
) -> Instance:
    """
    Create a new OpenXR instance.
    
    This function wraps the native :func:`xrCreateInstance` call, establishing a connection
    between the application and the OpenXR runtime. It enables requested API layers and
    extensions, and returns an opaque handle to the newly created instance.
    
    If `create_info` is not provided, a default :class:`xr.InstanceCreateInfo` will be used.
    
    :param create_info: Optional descriptor specifying application info, enabled extensions,
                        and platform-specific parameters.
    :type create_info: xr.InstanceCreateInfo or None
    :return: A newly created OpenXR instance handle.
    :rtype: xr.Instance
    :raises xr.ValidationFailureError: If validation layers reject the configuration.
    :raises xr.RuntimeFailureError: If the runtime fails to initialize.
    :raises xr.OutOfMemoryError: If memory allocation fails.
    :raises xr.LimitReachedError: If the runtime cannot support additional instances.
    :raises xr.RuntimeUnavailableError: If no runtime is available.
    :raises xr.NameInvalidError: If the application name is empty.
    :raises xr.InitializationFailedError: If platform-specific initialization fails.
    :raises xr.ExtensionNotPresentError: If a requested extension is missing.
    :raises xr.ExtensionDependencyNotEnabledError: If an extension dependency is missing.
    :raises xr.ApiVersionUnsupportedError: If the requested API version is not supported.
    :raises xr.ApiLayerNotPresentError: If a requested API layer is missing.
    :seealso: :class:`xr.Instance`, :class:`xr.InstanceCreateInfo`
    """
    if create_info is None:
        create_info = InstanceCreateInfo()
    instance = Instance()
    instance.instance = instance
    instance._create_info = create_info
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
    fxn = raw_functions.xrDestroyInstance
    result = check_result(fxn(
        instance,
    ))
    if result.is_exception():
        raise result


def get_instance_properties(
    instance: Instance,
) -> InstanceProperties:
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
    get_info: SystemGetInfo = SystemGetInfo(),
) -> SystemId:
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
) -> Sequence[EnvironmentBlendMode]:
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
    environment_blend_modes = (EnvironmentBlendMode.ctype() * environment_blend_mode_capacity_input.value)(*([EnvironmentBlendMode.ctype()()] * environment_blend_mode_capacity_input.value))  # noqa
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
    return environment_blend_modes  # noqa


def create_session(
    instance: Instance,
    create_info: SessionCreateInfo = None,
) -> Session:
    if create_info is None:
        create_info = SessionCreateInfo()
    session = Session()
    session.instance = instance
    session._create_info = create_info
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
    fxn = raw_functions.xrDestroySession
    result = check_result(fxn(
        session,
    ))
    if result.is_exception():
        raise result


def enumerate_reference_spaces(
    session: Session,
) -> Sequence[ReferenceSpaceType]:
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
    spaces = (ReferenceSpaceType.ctype() * space_capacity_input.value)(*([ReferenceSpaceType.ctype()()] * space_capacity_input.value))  # noqa
    result = check_result(fxn(
        session,
        space_capacity_input,
        byref(space_capacity_input),
        spaces,
    ))
    if result.is_exception():
        raise result
    return spaces  # noqa


def create_reference_space(
    session: Session,
    create_info: ReferenceSpaceCreateInfo = None,
) -> Space:
    if create_info is None:
        create_info = ReferenceSpaceCreateInfo()
    space = Space()
    space.instance = session.instance
    space._create_info = create_info
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
    if create_info is None:
        create_info = ActionSpaceCreateInfo()
    space = Space()
    space.instance = session.instance
    space._create_info = create_info
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
    fxn = raw_functions.xrDestroySpace
    result = check_result(fxn(
        space,
    ))
    if result.is_exception():
        raise result


def enumerate_view_configurations(
    instance: Instance,
    system_id: SystemId,
) -> Sequence[ViewConfigurationType]:
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
    view_configuration_types = (ViewConfigurationType.ctype() * view_configuration_type_capacity_input.value)(*([ViewConfigurationType.ctype()()] * view_configuration_type_capacity_input.value))  # noqa
    result = check_result(fxn(
        instance,
        system_id,
        view_configuration_type_capacity_input,
        byref(view_configuration_type_capacity_input),
        view_configuration_types,
    ))
    if result.is_exception():
        raise result
    return view_configuration_types  # noqa


def get_view_configuration_properties(
    instance: Instance,
    system_id: SystemId,
    view_configuration_type: ViewConfigurationType,
) -> ViewConfigurationProperties:
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
) -> Sequence[ViewConfigurationView]:
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
    views = (ViewConfigurationView * view_capacity_input.value)(*([ViewConfigurationView()] * view_capacity_input.value))  # noqa
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
    return views  # noqa


def enumerate_swapchain_formats(
    session: Session,
) -> Sequence[int]:
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
    formats = (c_int64 * format_capacity_input.value)(*([c_int64()] * format_capacity_input.value))  # noqa
    result = check_result(fxn(
        session,
        format_capacity_input,
        byref(format_capacity_input),
        formats,
    ))
    if result.is_exception():
        raise result
    return formats  # noqa


def create_swapchain(
    session: Session,
    create_info: SwapchainCreateInfo = None,
) -> Swapchain:
    if create_info is None:
        create_info = SwapchainCreateInfo()
    swapchain = Swapchain()
    swapchain.instance = session.instance
    swapchain._create_info = create_info
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
    fxn = raw_functions.xrDestroySwapchain
    result = check_result(fxn(
        swapchain,
    ))
    if result.is_exception():
        raise result


def enumerate_swapchain_images(
    swapchain: Swapchain,
    element_type: Type[SWAPCHAIN_IMAGE_TYPE],
) -> Sequence[SwapchainImageBaseHeader]:
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
    images = (element_type * image_capacity_input.value)(*([element_type()] * image_capacity_input.value))  # noqa
    result = check_result(fxn(
        swapchain,
        image_capacity_input,
        byref(image_capacity_input),
        cast(images, POINTER(SwapchainImageBaseHeader)),
    ))
    if result.is_exception():
        raise result
    return images  # noqa


def acquire_swapchain_image(
    swapchain: Swapchain,
    acquire_info: SwapchainImageAcquireInfo = None,
) -> int:
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
    fxn = raw_functions.xrEndSession
    result = check_result(fxn(
        session,
    ))
    if result.is_exception():
        raise result


def request_exit_session(
    session: Session,
) -> None:
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
) -> (ViewState, Sequence[View]):
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
    views = (View * view_capacity_input.value)(*([View()] * view_capacity_input.value))  # noqa
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
    return view_state, views  # noqa


def string_to_path(
    instance: Instance,
    path_string: str,
) -> Path:
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
    if create_info is None:
        create_info = ActionSetCreateInfo()
    action_set = ActionSet()
    action_set.instance = instance
    action_set._create_info = create_info
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
    if create_info is None:
        create_info = ActionCreateInfo()
    action = Action()
    action.instance = action_set.instance
    action._create_info = create_info
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
) -> Sequence[Path]:
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
    sources = (Path * source_capacity_input.value)(*([Path()] * source_capacity_input.value))  # noqa
    result = check_result(fxn(
        session,
        enumerate_info,
        source_capacity_input,
        byref(source_capacity_input),
        sources,
    ))
    if result.is_exception():
        raise result
    return sources  # noqa


def get_input_source_localized_name(
    session: Session,
    get_info: InputSourceLocalizedNameGetInfo,
) -> str:
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
    fxn = raw_functions.xrApplyHapticFeedback
    result = check_result(fxn(
        session,
        haptic_action_info,
        cast(byref(haptic_feedback), POINTER(HapticBaseHeader)),
    ))
    if result.is_exception():
        raise result


def stop_haptic_feedback(
    session: Session,
    haptic_action_info: HapticActionInfo,
) -> None:
    fxn = raw_functions.xrStopHapticFeedback
    result = check_result(fxn(
        session,
        haptic_action_info,
    ))
    if result.is_exception():
        raise result


def locate_spaces(
    session: Session,
    locate_info: SpacesLocateInfo,
) -> SpaceLocations:
    space_locations = SpaceLocations()
    fxn = raw_functions.xrLocateSpaces
    result = check_result(fxn(
        session,
        locate_info,
        byref(space_locations),
    ))
    if result.is_exception():
        raise result
    return space_locations


def get_visibility_mask_khr(
    session: Session,
    view_configuration_type: ViewConfigurationType,
    view_index: int,
    visibility_mask_type: VisibilityMaskTypeKHR,
) -> VisibilityMaskKHR:
    visibility_mask = VisibilityMaskKHR()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrGetVisibilityMaskKHR"),
        PFN_xrGetVisibilityMaskKHR,
    )
    result = check_result(fxn(
        session,
        view_configuration_type.value,
        view_index,
        visibility_mask_type.value,
        byref(visibility_mask),
    ))
    if result.is_exception():
        raise result
    return visibility_mask


def initialize_loader_khr(
    loader_init_info: LoaderInitInfoBaseHeaderKHR,
) -> None:
    fxn = cast(
        get_instance_proc_addr(NULL_HANDLE, "xrInitializeLoaderKHR"),
        PFN_xrInitializeLoaderKHR,
    )
    result = check_result(fxn(
        cast(byref(loader_init_info), POINTER(LoaderInitInfoBaseHeaderKHR)),
    ))
    if result.is_exception():
        raise result


def structure_type_to_string2_khr(
    instance: Instance,
    value: StructureType,
    buffer: (c_char * 256),
) -> None:
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrStructureTypeToString2KHR"),
        PFN_xrStructureTypeToString2KHR,
    )
    result = check_result(fxn(
        instance,
        value.value,
        buffer,
    ))
    if result.is_exception():
        raise result


def perf_settings_set_performance_level_ext(
    session: Session,
    domain: PerfSettingsDomainEXT,
    level: PerfSettingsLevelEXT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrPerfSettingsSetPerformanceLevelEXT"),
        PFN_xrPerfSettingsSetPerformanceLevelEXT,
    )
    result = check_result(fxn(
        session,
        domain.value,
        level.value,
    ))
    if result.is_exception():
        raise result


def thermal_get_temperature_trend_ext(
    session: Session,
    domain: PerfSettingsDomainEXT,
) -> (PerfSettingsNotificationLevelEXT, float, float):
    notification_level = PerfSettingsNotificationLevelEXT.ctype()()
    temp_headroom = c_float()
    temp_slope = c_float()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrThermalGetTemperatureTrendEXT"),
        PFN_xrThermalGetTemperatureTrendEXT,
    )
    result = check_result(fxn(
        session,
        domain.value,
        byref(notification_level),
        byref(temp_headroom),
        byref(temp_slope),
    ))
    if result.is_exception():
        raise result
    return notification_level, temp_headroom, temp_slope


def set_debug_utils_object_name_ext(
    instance: Instance,
    name_info: DebugUtilsObjectNameInfoEXT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrSetDebugUtilsObjectNameEXT"),
        PFN_xrSetDebugUtilsObjectNameEXT,
    )
    result = check_result(fxn(
        instance,
        name_info,
    ))
    if result.is_exception():
        raise result


def create_debug_utils_messenger_ext(
    instance: Instance,
    create_info: DebugUtilsMessengerCreateInfoEXT = None,
) -> DebugUtilsMessengerEXT:
    if create_info is None:
        create_info = DebugUtilsMessengerCreateInfoEXT()
    messenger = DebugUtilsMessengerEXT()
    messenger.instance = instance
    messenger._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrCreateDebugUtilsMessengerEXT"),
        PFN_xrCreateDebugUtilsMessengerEXT,
    )
    result = check_result(fxn(
        instance,
        create_info,
        byref(messenger),
    ))
    if result.is_exception():
        raise result
    return messenger


def destroy_debug_utils_messenger_ext(
    messenger: DebugUtilsMessengerEXT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(messenger.instance, "xrDestroyDebugUtilsMessengerEXT"),
        PFN_xrDestroyDebugUtilsMessengerEXT,
    )
    result = check_result(fxn(
        messenger,
    ))
    if result.is_exception():
        raise result


def submit_debug_utils_message_ext(
    instance: Instance,
    message_severity: DebugUtilsMessageSeverityFlagsEXT,
    message_types: DebugUtilsMessageTypeFlagsEXT,
    callback_data: DebugUtilsMessengerCallbackDataEXT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrSubmitDebugUtilsMessageEXT"),
        PFN_xrSubmitDebugUtilsMessageEXT,
    )
    result = check_result(fxn(
        instance,
        message_severity,
        message_types,
        callback_data,
    ))
    if result.is_exception():
        raise result


def session_begin_debug_utils_label_region_ext(
    session: Session,
    label_info: DebugUtilsLabelEXT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrSessionBeginDebugUtilsLabelRegionEXT"),
        PFN_xrSessionBeginDebugUtilsLabelRegionEXT,
    )
    result = check_result(fxn(
        session,
        label_info,
    ))
    if result.is_exception():
        raise result


def session_end_debug_utils_label_region_ext(
    session: Session,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrSessionEndDebugUtilsLabelRegionEXT"),
        PFN_xrSessionEndDebugUtilsLabelRegionEXT,
    )
    result = check_result(fxn(
        session,
    ))
    if result.is_exception():
        raise result


def session_insert_debug_utils_label_ext(
    session: Session,
    label_info: DebugUtilsLabelEXT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrSessionInsertDebugUtilsLabelEXT"),
        PFN_xrSessionInsertDebugUtilsLabelEXT,
    )
    result = check_result(fxn(
        session,
        label_info,
    ))
    if result.is_exception():
        raise result


def create_spatial_anchor_msft(
    session: Session,
    create_info: SpatialAnchorCreateInfoMSFT = None,
) -> SpatialAnchorMSFT:
    if create_info is None:
        create_info = SpatialAnchorCreateInfoMSFT()
    anchor = SpatialAnchorMSFT()
    anchor.instance = session.instance
    anchor._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateSpatialAnchorMSFT"),
        PFN_xrCreateSpatialAnchorMSFT,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(anchor),
    ))
    if result.is_exception():
        raise result
    return anchor


def create_spatial_anchor_space_msft(
    session: Session,
    create_info: SpatialAnchorSpaceCreateInfoMSFT = None,
) -> Space:
    if create_info is None:
        create_info = SpatialAnchorSpaceCreateInfoMSFT()
    space = Space()
    space.instance = session.instance
    space._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateSpatialAnchorSpaceMSFT"),
        PFN_xrCreateSpatialAnchorSpaceMSFT,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(space),
    ))
    if result.is_exception():
        raise result
    return space


def destroy_spatial_anchor_msft(
    anchor: SpatialAnchorMSFT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(anchor.instance, "xrDestroySpatialAnchorMSFT"),
        PFN_xrDestroySpatialAnchorMSFT,
    )
    result = check_result(fxn(
        anchor,
    ))
    if result.is_exception():
        raise result


def set_input_device_active_ext(
    session: Session,
    interaction_profile: Path,
    top_level_path: Path,
    is_active: Bool32,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrSetInputDeviceActiveEXT"),
        PFN_xrSetInputDeviceActiveEXT,
    )
    result = check_result(fxn(
        session,
        interaction_profile,
        top_level_path,
        is_active,
    ))
    if result.is_exception():
        raise result


def set_input_device_state_bool_ext(
    session: Session,
    top_level_path: Path,
    input_source_path: Path,
    state: Bool32,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrSetInputDeviceStateBoolEXT"),
        PFN_xrSetInputDeviceStateBoolEXT,
    )
    result = check_result(fxn(
        session,
        top_level_path,
        input_source_path,
        state,
    ))
    if result.is_exception():
        raise result


def set_input_device_state_float_ext(
    session: Session,
    top_level_path: Path,
    input_source_path: Path,
    state: float,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrSetInputDeviceStateFloatEXT"),
        PFN_xrSetInputDeviceStateFloatEXT,
    )
    result = check_result(fxn(
        session,
        top_level_path,
        input_source_path,
        state,
    ))
    if result.is_exception():
        raise result


def set_input_device_state_vector2f_ext(
    session: Session,
    top_level_path: Path,
    input_source_path: Path,
    state: Vector2f,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrSetInputDeviceStateVector2fEXT"),
        PFN_xrSetInputDeviceStateVector2fEXT,
    )
    result = check_result(fxn(
        session,
        top_level_path,
        input_source_path,
        state.value,
    ))
    if result.is_exception():
        raise result


def set_input_device_location_ext(
    session: Session,
    top_level_path: Path,
    input_source_path: Path,
    space: Space,
    pose: Posef,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrSetInputDeviceLocationEXT"),
        PFN_xrSetInputDeviceLocationEXT,
    )
    result = check_result(fxn(
        session,
        top_level_path,
        input_source_path,
        space,
        pose.value,
    ))
    if result.is_exception():
        raise result


def create_spatial_graph_node_space_msft(
    session: Session,
    create_info: SpatialGraphNodeSpaceCreateInfoMSFT = None,
) -> Space:
    if create_info is None:
        create_info = SpatialGraphNodeSpaceCreateInfoMSFT()
    space = Space()
    space.instance = session.instance
    space._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateSpatialGraphNodeSpaceMSFT"),
        PFN_xrCreateSpatialGraphNodeSpaceMSFT,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(space),
    ))
    if result.is_exception():
        raise result
    return space


def try_create_spatial_graph_static_node_binding_msft(
    session: Session,
    create_info: SpatialGraphStaticNodeBindingCreateInfoMSFT = None,
) -> SpatialGraphNodeBindingMSFT:
    if create_info is None:
        create_info = SpatialGraphStaticNodeBindingCreateInfoMSFT()
    node_binding = SpatialGraphNodeBindingMSFT()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrTryCreateSpatialGraphStaticNodeBindingMSFT"),
        PFN_xrTryCreateSpatialGraphStaticNodeBindingMSFT,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(node_binding),
    ))
    if result.is_exception():
        raise result
    return node_binding


def destroy_spatial_graph_node_binding_msft(
    node_binding: SpatialGraphNodeBindingMSFT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(node_binding.instance, "xrDestroySpatialGraphNodeBindingMSFT"),
        PFN_xrDestroySpatialGraphNodeBindingMSFT,
    )
    result = check_result(fxn(
        node_binding,
    ))
    if result.is_exception():
        raise result


def get_spatial_graph_node_binding_properties_msft(
    node_binding: SpatialGraphNodeBindingMSFT,
    get_info: SpatialGraphNodeBindingPropertiesGetInfoMSFT = None,
) -> SpatialGraphNodeBindingPropertiesMSFT:
    properties = SpatialGraphNodeBindingPropertiesMSFT()
    fxn = cast(
        get_instance_proc_addr(node_binding.instance, "xrGetSpatialGraphNodeBindingPropertiesMSFT"),
        PFN_xrGetSpatialGraphNodeBindingPropertiesMSFT,
    )
    result = check_result(fxn(
        node_binding,
        get_info,
        byref(properties),
    ))
    if result.is_exception():
        raise result
    return properties


def create_hand_tracker_ext(
    session: Session,
    create_info: HandTrackerCreateInfoEXT = None,
) -> HandTrackerEXT:
    if create_info is None:
        create_info = HandTrackerCreateInfoEXT()
    hand_tracker = HandTrackerEXT()
    hand_tracker.instance = session.instance
    hand_tracker._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateHandTrackerEXT"),
        PFN_xrCreateHandTrackerEXT,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(hand_tracker),
    ))
    if result.is_exception():
        raise result
    return hand_tracker


def destroy_hand_tracker_ext(
    hand_tracker: HandTrackerEXT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(hand_tracker.instance, "xrDestroyHandTrackerEXT"),
        PFN_xrDestroyHandTrackerEXT,
    )
    result = check_result(fxn(
        hand_tracker,
    ))
    if result.is_exception():
        raise result


def locate_hand_joints_ext(
    hand_tracker: HandTrackerEXT,
    locate_info: HandJointsLocateInfoEXT,
) -> HandJointLocationsEXT:
    locations = HandJointLocationsEXT()
    fxn = cast(
        get_instance_proc_addr(hand_tracker.instance, "xrLocateHandJointsEXT"),
        PFN_xrLocateHandJointsEXT,
    )
    result = check_result(fxn(
        hand_tracker,
        locate_info,
        byref(locations),
    ))
    if result.is_exception():
        raise result
    return locations


def create_hand_mesh_space_msft(
    hand_tracker: HandTrackerEXT,
    create_info: HandMeshSpaceCreateInfoMSFT = None,
) -> Space:
    if create_info is None:
        create_info = HandMeshSpaceCreateInfoMSFT()
    space = Space()
    space.instance = hand_tracker.instance
    space._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(hand_tracker.instance, "xrCreateHandMeshSpaceMSFT"),
        PFN_xrCreateHandMeshSpaceMSFT,
    )
    result = check_result(fxn(
        hand_tracker,
        create_info,
        byref(space),
    ))
    if result.is_exception():
        raise result
    return space


def update_hand_mesh_msft(
    hand_tracker: HandTrackerEXT,
    update_info: HandMeshUpdateInfoMSFT,
) -> HandMeshMSFT:
    hand_mesh = HandMeshMSFT()
    fxn = cast(
        get_instance_proc_addr(hand_tracker.instance, "xrUpdateHandMeshMSFT"),
        PFN_xrUpdateHandMeshMSFT,
    )
    result = check_result(fxn(
        hand_tracker,
        update_info,
        byref(hand_mesh),
    ))
    if result.is_exception():
        raise result
    return hand_mesh


def get_controller_model_key_msft(
    session: Session,
    top_level_user_path: Path,
) -> ControllerModelKeyStateMSFT:
    controller_model_key_state = ControllerModelKeyStateMSFT()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrGetControllerModelKeyMSFT"),
        PFN_xrGetControllerModelKeyMSFT,
    )
    result = check_result(fxn(
        session,
        top_level_user_path,
        byref(controller_model_key_state),
    ))
    if result.is_exception():
        raise result
    return controller_model_key_state


def load_controller_model_msft(
    session: Session,
    model_key: ControllerModelKeyMSFT,
) -> Sequence[int]:
    buffer_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrLoadControllerModelMSFT"),
        PFN_xrLoadControllerModelMSFT,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        session,
        model_key,
        0,
        byref(buffer_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    buffer = (c_uint8 * buffer_capacity_input.value)(*([c_uint8()] * buffer_capacity_input.value))  # noqa
    result = check_result(fxn(
        session,
        model_key,
        buffer_capacity_input,
        byref(buffer_capacity_input),
        buffer,
    ))
    if result.is_exception():
        raise result
    return buffer  # noqa


def get_controller_model_properties_msft(
    session: Session,
    model_key: ControllerModelKeyMSFT,
) -> ControllerModelPropertiesMSFT:
    properties = ControllerModelPropertiesMSFT()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrGetControllerModelPropertiesMSFT"),
        PFN_xrGetControllerModelPropertiesMSFT,
    )
    result = check_result(fxn(
        session,
        model_key,
        byref(properties),
    ))
    if result.is_exception():
        raise result
    return properties


def get_controller_model_state_msft(
    session: Session,
    model_key: ControllerModelKeyMSFT,
) -> ControllerModelStateMSFT:
    state = ControllerModelStateMSFT()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrGetControllerModelStateMSFT"),
        PFN_xrGetControllerModelStateMSFT,
    )
    result = check_result(fxn(
        session,
        model_key,
        byref(state),
    ))
    if result.is_exception():
        raise result
    return state


def enumerate_reprojection_modes_msft(
    instance: Instance,
    system_id: SystemId,
    view_configuration_type: ViewConfigurationType,
) -> Sequence[ReprojectionModeMSFT]:
    mode_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrEnumerateReprojectionModesMSFT"),
        PFN_xrEnumerateReprojectionModesMSFT,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        instance,
        system_id,
        view_configuration_type.value,
        0,
        byref(mode_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    modes = (ReprojectionModeMSFT.ctype() * mode_capacity_input.value)(*([ReprojectionModeMSFT.ctype()()] * mode_capacity_input.value))  # noqa
    result = check_result(fxn(
        instance,
        system_id,
        view_configuration_type.value,
        mode_capacity_input,
        byref(mode_capacity_input),
        modes,
    ))
    if result.is_exception():
        raise result
    return modes  # noqa


def update_swapchain_fb(
    swapchain: Swapchain,
    state: SwapchainStateBaseHeaderFB,
) -> None:
    fxn = cast(
        get_instance_proc_addr(swapchain.instance, "xrUpdateSwapchainFB"),
        PFN_xrUpdateSwapchainFB,
    )
    result = check_result(fxn(
        swapchain,
        cast(byref(state), POINTER(SwapchainStateBaseHeaderFB)),
    ))
    if result.is_exception():
        raise result


def get_swapchain_state_fb(
    swapchain: Swapchain,
) -> SwapchainStateBaseHeaderFB:
    state = SwapchainStateBaseHeaderFB()
    fxn = cast(
        get_instance_proc_addr(swapchain.instance, "xrGetSwapchainStateFB"),
        PFN_xrGetSwapchainStateFB,
    )
    result = check_result(fxn(
        swapchain,
        cast(byref(state), POINTER(SwapchainStateBaseHeaderFB)),
    ))
    if result.is_exception():
        raise result
    return state


def create_body_tracker_fb(
    session: Session,
    create_info: BodyTrackerCreateInfoFB = None,
) -> BodyTrackerFB:
    if create_info is None:
        create_info = BodyTrackerCreateInfoFB()
    body_tracker = BodyTrackerFB()
    body_tracker.instance = session.instance
    body_tracker._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateBodyTrackerFB"),
        PFN_xrCreateBodyTrackerFB,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(body_tracker),
    ))
    if result.is_exception():
        raise result
    return body_tracker


def destroy_body_tracker_fb(
    body_tracker: BodyTrackerFB,
) -> None:
    fxn = cast(
        get_instance_proc_addr(body_tracker.instance, "xrDestroyBodyTrackerFB"),
        PFN_xrDestroyBodyTrackerFB,
    )
    result = check_result(fxn(
        body_tracker,
    ))
    if result.is_exception():
        raise result


def locate_body_joints_fb(
    body_tracker: BodyTrackerFB,
    locate_info: BodyJointsLocateInfoFB,
) -> BodyJointLocationsFB:
    locations = BodyJointLocationsFB()
    fxn = cast(
        get_instance_proc_addr(body_tracker.instance, "xrLocateBodyJointsFB"),
        PFN_xrLocateBodyJointsFB,
    )
    result = check_result(fxn(
        body_tracker,
        locate_info,
        byref(locations),
    ))
    if result.is_exception():
        raise result
    return locations


def get_body_skeleton_fb(
    body_tracker: BodyTrackerFB,
) -> BodySkeletonFB:
    skeleton = BodySkeletonFB()
    fxn = cast(
        get_instance_proc_addr(body_tracker.instance, "xrGetBodySkeletonFB"),
        PFN_xrGetBodySkeletonFB,
    )
    result = check_result(fxn(
        body_tracker,
        byref(skeleton),
    ))
    if result.is_exception():
        raise result
    return skeleton


def enumerate_scene_compute_features_msft(
    instance: Instance,
    system_id: SystemId,
) -> Sequence[SceneComputeFeatureMSFT]:
    feature_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrEnumerateSceneComputeFeaturesMSFT"),
        PFN_xrEnumerateSceneComputeFeaturesMSFT,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        instance,
        system_id,
        0,
        byref(feature_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    features = (SceneComputeFeatureMSFT.ctype() * feature_capacity_input.value)(*([SceneComputeFeatureMSFT.ctype()()] * feature_capacity_input.value))  # noqa
    result = check_result(fxn(
        instance,
        system_id,
        feature_capacity_input,
        byref(feature_capacity_input),
        features,
    ))
    if result.is_exception():
        raise result
    return features  # noqa


def create_scene_observer_msft(
    session: Session,
    create_info: SceneObserverCreateInfoMSFT = None,
) -> SceneObserverMSFT:
    if create_info is None:
        create_info = SceneObserverCreateInfoMSFT()
    scene_observer = SceneObserverMSFT()
    scene_observer.instance = session.instance
    scene_observer._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateSceneObserverMSFT"),
        PFN_xrCreateSceneObserverMSFT,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(scene_observer),
    ))
    if result.is_exception():
        raise result
    return scene_observer


def destroy_scene_observer_msft(
    scene_observer: SceneObserverMSFT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(scene_observer.instance, "xrDestroySceneObserverMSFT"),
        PFN_xrDestroySceneObserverMSFT,
    )
    result = check_result(fxn(
        scene_observer,
    ))
    if result.is_exception():
        raise result


def create_scene_msft(
    scene_observer: SceneObserverMSFT,
    create_info: SceneCreateInfoMSFT = None,
) -> SceneMSFT:
    if create_info is None:
        create_info = SceneCreateInfoMSFT()
    scene = SceneMSFT()
    scene.instance = scene_observer.instance
    scene._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(scene_observer.instance, "xrCreateSceneMSFT"),
        PFN_xrCreateSceneMSFT,
    )
    result = check_result(fxn(
        scene_observer,
        create_info,
        byref(scene),
    ))
    if result.is_exception():
        raise result
    return scene


def destroy_scene_msft(
    scene: SceneMSFT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(scene.instance, "xrDestroySceneMSFT"),
        PFN_xrDestroySceneMSFT,
    )
    result = check_result(fxn(
        scene,
    ))
    if result.is_exception():
        raise result


def compute_new_scene_msft(
    scene_observer: SceneObserverMSFT,
    compute_info: NewSceneComputeInfoMSFT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(scene_observer.instance, "xrComputeNewSceneMSFT"),
        PFN_xrComputeNewSceneMSFT,
    )
    result = check_result(fxn(
        scene_observer,
        compute_info,
    ))
    if result.is_exception():
        raise result


def get_scene_compute_state_msft(
    scene_observer: SceneObserverMSFT,
) -> SceneComputeStateMSFT:
    state = SceneComputeStateMSFT.ctype()()
    fxn = cast(
        get_instance_proc_addr(scene_observer.instance, "xrGetSceneComputeStateMSFT"),
        PFN_xrGetSceneComputeStateMSFT,
    )
    result = check_result(fxn(
        scene_observer,
        byref(state),
    ))
    if result.is_exception():
        raise result
    return state


def get_scene_components_msft(
    scene: SceneMSFT,
    get_info: SceneComponentsGetInfoMSFT,
) -> SceneComponentsMSFT:
    components = SceneComponentsMSFT()
    fxn = cast(
        get_instance_proc_addr(scene.instance, "xrGetSceneComponentsMSFT"),
        PFN_xrGetSceneComponentsMSFT,
    )
    result = check_result(fxn(
        scene,
        get_info,
        byref(components),
    ))
    if result.is_exception():
        raise result
    return components


def locate_scene_components_msft(
    scene: SceneMSFT,
    locate_info: SceneComponentsLocateInfoMSFT,
) -> SceneComponentLocationsMSFT:
    locations = SceneComponentLocationsMSFT()
    fxn = cast(
        get_instance_proc_addr(scene.instance, "xrLocateSceneComponentsMSFT"),
        PFN_xrLocateSceneComponentsMSFT,
    )
    result = check_result(fxn(
        scene,
        locate_info,
        byref(locations),
    ))
    if result.is_exception():
        raise result
    return locations


def get_scene_mesh_buffers_msft(
    scene: SceneMSFT,
    get_info: SceneMeshBuffersGetInfoMSFT,
) -> SceneMeshBuffersMSFT:
    buffers = SceneMeshBuffersMSFT()
    fxn = cast(
        get_instance_proc_addr(scene.instance, "xrGetSceneMeshBuffersMSFT"),
        PFN_xrGetSceneMeshBuffersMSFT,
    )
    result = check_result(fxn(
        scene,
        get_info,
        byref(buffers),
    ))
    if result.is_exception():
        raise result
    return buffers


def deserialize_scene_msft(
    scene_observer: SceneObserverMSFT,
    deserialize_info: SceneDeserializeInfoMSFT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(scene_observer.instance, "xrDeserializeSceneMSFT"),
        PFN_xrDeserializeSceneMSFT,
    )
    result = check_result(fxn(
        scene_observer,
        deserialize_info,
    ))
    if result.is_exception():
        raise result


def get_serialized_scene_fragment_data_msft(
    scene: SceneMSFT,
    get_info: SerializedSceneFragmentDataGetInfoMSFT,
    count_input: int = None,
) -> (int, int):
    read_output = c_uint32()
    buffer = c_uint8()
    fxn = cast(
        get_instance_proc_addr(scene.instance, "xrGetSerializedSceneFragmentDataMSFT"),
        PFN_xrGetSerializedSceneFragmentDataMSFT,
    )
    result = check_result(fxn(
        scene,
        get_info,
        count_input,
        byref(read_output),
        byref(buffer),
    ))
    if result.is_exception():
        raise result
    return read_output.value, buffer.value


def enumerate_display_refresh_rates_fb(
    session: Session,
) -> Sequence[float]:
    display_refresh_rate_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrEnumerateDisplayRefreshRatesFB"),
        PFN_xrEnumerateDisplayRefreshRatesFB,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        session,
        0,
        byref(display_refresh_rate_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    display_refresh_rates = (c_float * display_refresh_rate_capacity_input.value)(*([c_float()] * display_refresh_rate_capacity_input.value))  # noqa
    result = check_result(fxn(
        session,
        display_refresh_rate_capacity_input,
        byref(display_refresh_rate_capacity_input),
        display_refresh_rates,
    ))
    if result.is_exception():
        raise result
    return display_refresh_rates  # noqa


def get_display_refresh_rate_fb(
    session: Session,
) -> float:
    display_refresh_rate = c_float()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrGetDisplayRefreshRateFB"),
        PFN_xrGetDisplayRefreshRateFB,
    )
    result = check_result(fxn(
        session,
        byref(display_refresh_rate),
    ))
    if result.is_exception():
        raise result
    return display_refresh_rate


def request_display_refresh_rate_fb(
    session: Session,
    display_refresh_rate: float,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrRequestDisplayRefreshRateFB"),
        PFN_xrRequestDisplayRefreshRateFB,
    )
    result = check_result(fxn(
        session,
        display_refresh_rate,
    ))
    if result.is_exception():
        raise result


def enumerate_vive_tracker_paths_htcx(
    instance: Instance,
) -> Sequence[ViveTrackerPathsHTCX]:
    path_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrEnumerateViveTrackerPathsHTCX"),
        PFN_xrEnumerateViveTrackerPathsHTCX,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        instance,
        0,
        byref(path_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    paths = (ViveTrackerPathsHTCX * path_capacity_input.value)(*([ViveTrackerPathsHTCX()] * path_capacity_input.value))  # noqa
    result = check_result(fxn(
        instance,
        path_capacity_input,
        byref(path_capacity_input),
        paths,
    ))
    if result.is_exception():
        raise result
    return paths  # noqa


def create_facial_tracker_htc(
    session: Session,
    create_info: FacialTrackerCreateInfoHTC = None,
) -> FacialTrackerHTC:
    if create_info is None:
        create_info = FacialTrackerCreateInfoHTC()
    facial_tracker = FacialTrackerHTC()
    facial_tracker.instance = session.instance
    facial_tracker._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateFacialTrackerHTC"),
        PFN_xrCreateFacialTrackerHTC,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(facial_tracker),
    ))
    if result.is_exception():
        raise result
    return facial_tracker


def destroy_facial_tracker_htc(
    facial_tracker: FacialTrackerHTC,
) -> None:
    fxn = cast(
        get_instance_proc_addr(facial_tracker.instance, "xrDestroyFacialTrackerHTC"),
        PFN_xrDestroyFacialTrackerHTC,
    )
    result = check_result(fxn(
        facial_tracker,
    ))
    if result.is_exception():
        raise result


def get_facial_expressions_htc(
    facial_tracker: FacialTrackerHTC,
) -> FacialExpressionsHTC:
    facial_expressions = FacialExpressionsHTC()
    fxn = cast(
        get_instance_proc_addr(facial_tracker.instance, "xrGetFacialExpressionsHTC"),
        PFN_xrGetFacialExpressionsHTC,
    )
    result = check_result(fxn(
        facial_tracker,
        byref(facial_expressions),
    ))
    if result.is_exception():
        raise result
    return facial_expressions


def enumerate_color_spaces_fb(
    session: Session,
) -> Sequence[ColorSpaceFB]:
    color_space_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrEnumerateColorSpacesFB"),
        PFN_xrEnumerateColorSpacesFB,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        session,
        0,
        byref(color_space_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    color_spaces = (ColorSpaceFB.ctype() * color_space_capacity_input.value)(*([ColorSpaceFB.ctype()()] * color_space_capacity_input.value))  # noqa
    result = check_result(fxn(
        session,
        color_space_capacity_input,
        byref(color_space_capacity_input),
        color_spaces,
    ))
    if result.is_exception():
        raise result
    return color_spaces  # noqa


def set_color_space_fb(
    session: Session,
    color_space: c_int,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrSetColorSpaceFB"),
        PFN_xrSetColorSpaceFB,
    )
    result = check_result(fxn(
        session,
        color_space,
    ))
    if result.is_exception():
        raise result


def get_hand_mesh_fb(
    hand_tracker: HandTrackerEXT,
) -> HandTrackingMeshFB:
    mesh = HandTrackingMeshFB()
    fxn = cast(
        get_instance_proc_addr(hand_tracker.instance, "xrGetHandMeshFB"),
        PFN_xrGetHandMeshFB,
    )
    result = check_result(fxn(
        hand_tracker,
        byref(mesh),
    ))
    if result.is_exception():
        raise result
    return mesh


def create_spatial_anchor_fb(
    session: Session,
    info: SpatialAnchorCreateInfoFB,
) -> AsyncRequestIdFB:
    request_id = AsyncRequestIdFB()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateSpatialAnchorFB"),
        PFN_xrCreateSpatialAnchorFB,
    )
    result = check_result(fxn(
        session,
        info,
        byref(request_id),
    ))
    if result.is_exception():
        raise result
    return request_id


def get_space_uuid_fb(
    space: Space,
) -> UuidEXT:
    uuid = UuidEXT()
    fxn = cast(
        get_instance_proc_addr(space.instance, "xrGetSpaceUuidFB"),
        PFN_xrGetSpaceUuidFB,
    )
    result = check_result(fxn(
        space,
        byref(uuid),
    ))
    if result.is_exception():
        raise result
    return uuid


def enumerate_space_supported_components_fb(
    space: Space,
) -> Sequence[SpaceComponentTypeFB]:
    component_type_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(space.instance, "xrEnumerateSpaceSupportedComponentsFB"),
        PFN_xrEnumerateSpaceSupportedComponentsFB,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        space,
        0,
        byref(component_type_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    component_types = (SpaceComponentTypeFB.ctype() * component_type_capacity_input.value)(*([SpaceComponentTypeFB.ctype()()] * component_type_capacity_input.value))  # noqa
    result = check_result(fxn(
        space,
        component_type_capacity_input,
        byref(component_type_capacity_input),
        component_types,
    ))
    if result.is_exception():
        raise result
    return component_types  # noqa


def set_space_component_status_fb(
    space: Space,
    info: SpaceComponentStatusSetInfoFB,
) -> AsyncRequestIdFB:
    request_id = AsyncRequestIdFB()
    fxn = cast(
        get_instance_proc_addr(space.instance, "xrSetSpaceComponentStatusFB"),
        PFN_xrSetSpaceComponentStatusFB,
    )
    result = check_result(fxn(
        space,
        info,
        byref(request_id),
    ))
    if result.is_exception():
        raise result
    return request_id


def get_space_component_status_fb(
    space: Space,
    component_type: SpaceComponentTypeFB,
) -> SpaceComponentStatusFB:
    status = SpaceComponentStatusFB()
    fxn = cast(
        get_instance_proc_addr(space.instance, "xrGetSpaceComponentStatusFB"),
        PFN_xrGetSpaceComponentStatusFB,
    )
    result = check_result(fxn(
        space,
        component_type.value,
        byref(status),
    ))
    if result.is_exception():
        raise result
    return status


def create_foveation_profile_fb(
    session: Session,
    create_info: FoveationProfileCreateInfoFB = None,
) -> FoveationProfileFB:
    if create_info is None:
        create_info = FoveationProfileCreateInfoFB()
    profile = FoveationProfileFB()
    profile.instance = session.instance
    profile._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateFoveationProfileFB"),
        PFN_xrCreateFoveationProfileFB,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(profile),
    ))
    if result.is_exception():
        raise result
    return profile


def destroy_foveation_profile_fb(
    profile: FoveationProfileFB,
) -> None:
    fxn = cast(
        get_instance_proc_addr(profile.instance, "xrDestroyFoveationProfileFB"),
        PFN_xrDestroyFoveationProfileFB,
    )
    result = check_result(fxn(
        profile,
    ))
    if result.is_exception():
        raise result


def query_system_tracked_keyboard_fb(
    session: Session,
    query_info: KeyboardTrackingQueryFB,
) -> KeyboardTrackingDescriptionFB:
    keyboard = KeyboardTrackingDescriptionFB()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrQuerySystemTrackedKeyboardFB"),
        PFN_xrQuerySystemTrackedKeyboardFB,
    )
    result = check_result(fxn(
        session,
        query_info,
        byref(keyboard),
    ))
    if result.is_exception():
        raise result
    return keyboard


def create_keyboard_space_fb(
    session: Session,
    create_info: KeyboardSpaceCreateInfoFB = None,
) -> Space:
    if create_info is None:
        create_info = KeyboardSpaceCreateInfoFB()
    keyboard_space = Space()
    keyboard_space.instance = session.instance
    keyboard_space._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateKeyboardSpaceFB"),
        PFN_xrCreateKeyboardSpaceFB,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(keyboard_space),
    ))
    if result.is_exception():
        raise result
    return keyboard_space


def create_triangle_mesh_fb(
    session: Session,
    create_info: TriangleMeshCreateInfoFB = None,
) -> TriangleMeshFB:
    if create_info is None:
        create_info = TriangleMeshCreateInfoFB()
    out_triangle_mesh = TriangleMeshFB()
    out_triangle_mesh.instance = session.instance
    out_triangle_mesh._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateTriangleMeshFB"),
        PFN_xrCreateTriangleMeshFB,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(out_triangle_mesh),
    ))
    if result.is_exception():
        raise result
    return out_triangle_mesh


def destroy_triangle_mesh_fb(
    mesh: TriangleMeshFB,
) -> None:
    fxn = cast(
        get_instance_proc_addr(mesh.instance, "xrDestroyTriangleMeshFB"),
        PFN_xrDestroyTriangleMeshFB,
    )
    result = check_result(fxn(
        mesh,
    ))
    if result.is_exception():
        raise result


def triangle_mesh_get_vertex_buffer_fb(
    mesh: TriangleMeshFB,
) -> POINTER(Vector3f):
    out_vertex_buffer = POINTER(Vector3f)()
    fxn = cast(
        get_instance_proc_addr(mesh.instance, "xrTriangleMeshGetVertexBufferFB"),
        PFN_xrTriangleMeshGetVertexBufferFB,
    )
    result = check_result(fxn(
        mesh,
        byref(out_vertex_buffer),
    ))
    if result.is_exception():
        raise result
    return out_vertex_buffer


def triangle_mesh_get_index_buffer_fb(
    mesh: TriangleMeshFB,
) -> POINTER(c_uint32):
    out_index_buffer = POINTER(c_uint32)()
    fxn = cast(
        get_instance_proc_addr(mesh.instance, "xrTriangleMeshGetIndexBufferFB"),
        PFN_xrTriangleMeshGetIndexBufferFB,
    )
    result = check_result(fxn(
        mesh,
        byref(out_index_buffer),
    ))
    if result.is_exception():
        raise result
    return out_index_buffer


def triangle_mesh_begin_update_fb(
    mesh: TriangleMeshFB,
) -> None:
    fxn = cast(
        get_instance_proc_addr(mesh.instance, "xrTriangleMeshBeginUpdateFB"),
        PFN_xrTriangleMeshBeginUpdateFB,
    )
    result = check_result(fxn(
        mesh,
    ))
    if result.is_exception():
        raise result


def triangle_mesh_end_update_fb(
    mesh: TriangleMeshFB,
    vertex_count: int,
    triangle_count: int,
) -> None:
    fxn = cast(
        get_instance_proc_addr(mesh.instance, "xrTriangleMeshEndUpdateFB"),
        PFN_xrTriangleMeshEndUpdateFB,
    )
    result = check_result(fxn(
        mesh,
        vertex_count,
        triangle_count,
    ))
    if result.is_exception():
        raise result


def triangle_mesh_begin_vertex_buffer_update_fb(
    mesh: TriangleMeshFB,
) -> int:
    out_vertex_count = c_uint32()
    fxn = cast(
        get_instance_proc_addr(mesh.instance, "xrTriangleMeshBeginVertexBufferUpdateFB"),
        PFN_xrTriangleMeshBeginVertexBufferUpdateFB,
    )
    result = check_result(fxn(
        mesh,
        byref(out_vertex_count),
    ))
    if result.is_exception():
        raise result
    return out_vertex_count.value


def triangle_mesh_end_vertex_buffer_update_fb(
    mesh: TriangleMeshFB,
) -> None:
    fxn = cast(
        get_instance_proc_addr(mesh.instance, "xrTriangleMeshEndVertexBufferUpdateFB"),
        PFN_xrTriangleMeshEndVertexBufferUpdateFB,
    )
    result = check_result(fxn(
        mesh,
    ))
    if result.is_exception():
        raise result


def create_passthrough_fb(
    session: Session,
    create_info: PassthroughCreateInfoFB = None,
) -> PassthroughFB:
    if create_info is None:
        create_info = PassthroughCreateInfoFB()
    out_passthrough = PassthroughFB()
    out_passthrough.instance = session.instance
    out_passthrough._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreatePassthroughFB"),
        PFN_xrCreatePassthroughFB,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(out_passthrough),
    ))
    if result.is_exception():
        raise result
    return out_passthrough


def destroy_passthrough_fb(
    passthrough: PassthroughFB,
) -> None:
    fxn = cast(
        get_instance_proc_addr(passthrough.instance, "xrDestroyPassthroughFB"),
        PFN_xrDestroyPassthroughFB,
    )
    result = check_result(fxn(
        passthrough,
    ))
    if result.is_exception():
        raise result


def passthrough_start_fb(
    passthrough: PassthroughFB,
) -> None:
    fxn = cast(
        get_instance_proc_addr(passthrough.instance, "xrPassthroughStartFB"),
        PFN_xrPassthroughStartFB,
    )
    result = check_result(fxn(
        passthrough,
    ))
    if result.is_exception():
        raise result


def passthrough_pause_fb(
    passthrough: PassthroughFB,
) -> None:
    fxn = cast(
        get_instance_proc_addr(passthrough.instance, "xrPassthroughPauseFB"),
        PFN_xrPassthroughPauseFB,
    )
    result = check_result(fxn(
        passthrough,
    ))
    if result.is_exception():
        raise result


def create_passthrough_layer_fb(
    session: Session,
    create_info: PassthroughLayerCreateInfoFB = None,
) -> PassthroughLayerFB:
    if create_info is None:
        create_info = PassthroughLayerCreateInfoFB()
    out_layer = PassthroughLayerFB()
    out_layer.instance = session.instance
    out_layer._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreatePassthroughLayerFB"),
        PFN_xrCreatePassthroughLayerFB,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(out_layer),
    ))
    if result.is_exception():
        raise result
    return out_layer


def destroy_passthrough_layer_fb(
    layer: PassthroughLayerFB,
) -> None:
    fxn = cast(
        get_instance_proc_addr(layer.instance, "xrDestroyPassthroughLayerFB"),
        PFN_xrDestroyPassthroughLayerFB,
    )
    result = check_result(fxn(
        layer,
    ))
    if result.is_exception():
        raise result


def passthrough_layer_pause_fb(
    layer: PassthroughLayerFB,
) -> None:
    fxn = cast(
        get_instance_proc_addr(layer.instance, "xrPassthroughLayerPauseFB"),
        PFN_xrPassthroughLayerPauseFB,
    )
    result = check_result(fxn(
        layer,
    ))
    if result.is_exception():
        raise result


def passthrough_layer_resume_fb(
    layer: PassthroughLayerFB,
) -> None:
    fxn = cast(
        get_instance_proc_addr(layer.instance, "xrPassthroughLayerResumeFB"),
        PFN_xrPassthroughLayerResumeFB,
    )
    result = check_result(fxn(
        layer,
    ))
    if result.is_exception():
        raise result


def passthrough_layer_set_style_fb(
    layer: PassthroughLayerFB,
    style: PassthroughStyleFB,
) -> None:
    fxn = cast(
        get_instance_proc_addr(layer.instance, "xrPassthroughLayerSetStyleFB"),
        PFN_xrPassthroughLayerSetStyleFB,
    )
    result = check_result(fxn(
        layer,
        style,
    ))
    if result.is_exception():
        raise result


def create_geometry_instance_fb(
    session: Session,
    create_info: GeometryInstanceCreateInfoFB = None,
) -> GeometryInstanceFB:
    if create_info is None:
        create_info = GeometryInstanceCreateInfoFB()
    out_geometry_instance = GeometryInstanceFB()
    out_geometry_instance.instance = session.instance
    out_geometry_instance._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateGeometryInstanceFB"),
        PFN_xrCreateGeometryInstanceFB,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(out_geometry_instance),
    ))
    if result.is_exception():
        raise result
    return out_geometry_instance


def destroy_geometry_instance_fb(
    instance: GeometryInstanceFB,
) -> None:
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrDestroyGeometryInstanceFB"),
        PFN_xrDestroyGeometryInstanceFB,
    )
    result = check_result(fxn(
        instance,
    ))
    if result.is_exception():
        raise result


def geometry_instance_set_transform_fb(
    instance: GeometryInstanceFB,
    transformation: GeometryInstanceTransformFB,
) -> None:
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrGeometryInstanceSetTransformFB"),
        PFN_xrGeometryInstanceSetTransformFB,
    )
    result = check_result(fxn(
        instance,
        transformation,
    ))
    if result.is_exception():
        raise result


def enumerate_render_model_paths_fb(
    session: Session,
) -> Sequence[RenderModelPathInfoFB]:
    path_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrEnumerateRenderModelPathsFB"),
        PFN_xrEnumerateRenderModelPathsFB,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        session,
        0,
        byref(path_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    paths = (RenderModelPathInfoFB * path_capacity_input.value)(*([RenderModelPathInfoFB()] * path_capacity_input.value))  # noqa
    result = check_result(fxn(
        session,
        path_capacity_input,
        byref(path_capacity_input),
        paths,
    ))
    if result.is_exception():
        raise result
    return paths  # noqa


def get_render_model_properties_fb(
    session: Session,
    path: Path,
) -> RenderModelPropertiesFB:
    properties = RenderModelPropertiesFB()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrGetRenderModelPropertiesFB"),
        PFN_xrGetRenderModelPropertiesFB,
    )
    result = check_result(fxn(
        session,
        path,
        byref(properties),
    ))
    if result.is_exception():
        raise result
    return properties


def load_render_model_fb(
    session: Session,
    info: RenderModelLoadInfoFB,
) -> RenderModelBufferFB:
    buffer = RenderModelBufferFB()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrLoadRenderModelFB"),
        PFN_xrLoadRenderModelFB,
    )
    result = check_result(fxn(
        session,
        info,
        byref(buffer),
    ))
    if result.is_exception():
        raise result
    return buffer


def set_environment_depth_estimation_varjo(
    session: Session,
    enabled: Bool32,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrSetEnvironmentDepthEstimationVARJO"),
        PFN_xrSetEnvironmentDepthEstimationVARJO,
    )
    result = check_result(fxn(
        session,
        enabled,
    ))
    if result.is_exception():
        raise result


def set_marker_tracking_varjo(
    session: Session,
    enabled: Bool32,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrSetMarkerTrackingVARJO"),
        PFN_xrSetMarkerTrackingVARJO,
    )
    result = check_result(fxn(
        session,
        enabled,
    ))
    if result.is_exception():
        raise result


def set_marker_tracking_timeout_varjo(
    session: Session,
    marker_id: int,
    timeout: Duration,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrSetMarkerTrackingTimeoutVARJO"),
        PFN_xrSetMarkerTrackingTimeoutVARJO,
    )
    result = check_result(fxn(
        session,
        marker_id,
        timeout,
    ))
    if result.is_exception():
        raise result


def set_marker_tracking_prediction_varjo(
    session: Session,
    marker_id: int,
    enable: Bool32,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrSetMarkerTrackingPredictionVARJO"),
        PFN_xrSetMarkerTrackingPredictionVARJO,
    )
    result = check_result(fxn(
        session,
        marker_id,
        enable,
    ))
    if result.is_exception():
        raise result


def get_marker_size_varjo(
    session: Session,
    marker_id: int,
) -> Extent2Df:
    size = Extent2Df()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrGetMarkerSizeVARJO"),
        PFN_xrGetMarkerSizeVARJO,
    )
    result = check_result(fxn(
        session,
        marker_id,
        byref(size),
    ))
    if result.is_exception():
        raise result
    return size


def create_marker_space_varjo(
    session: Session,
    create_info: MarkerSpaceCreateInfoVARJO = None,
) -> Space:
    if create_info is None:
        create_info = MarkerSpaceCreateInfoVARJO()
    space = Space()
    space.instance = session.instance
    space._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateMarkerSpaceVARJO"),
        PFN_xrCreateMarkerSpaceVARJO,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(space),
    ))
    if result.is_exception():
        raise result
    return space


def set_view_offset_varjo(
    session: Session,
    offset: float,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrSetViewOffsetVARJO"),
        PFN_xrSetViewOffsetVARJO,
    )
    result = check_result(fxn(
        session,
        offset,
    ))
    if result.is_exception():
        raise result


def create_marker_detector_ml(
    session: Session,
    create_info: MarkerDetectorCreateInfoML = None,
) -> MarkerDetectorML:
    if create_info is None:
        create_info = MarkerDetectorCreateInfoML()
    marker_detector = MarkerDetectorML()
    marker_detector.instance = session.instance
    marker_detector._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateMarkerDetectorML"),
        PFN_xrCreateMarkerDetectorML,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(marker_detector),
    ))
    if result.is_exception():
        raise result
    return marker_detector


def destroy_marker_detector_ml(
    marker_detector: MarkerDetectorML,
) -> None:
    fxn = cast(
        get_instance_proc_addr(marker_detector.instance, "xrDestroyMarkerDetectorML"),
        PFN_xrDestroyMarkerDetectorML,
    )
    result = check_result(fxn(
        marker_detector,
    ))
    if result.is_exception():
        raise result


def snapshot_marker_detector_ml(
    marker_detector: MarkerDetectorML,
) -> MarkerDetectorSnapshotInfoML:
    snapshot_info = MarkerDetectorSnapshotInfoML()
    fxn = cast(
        get_instance_proc_addr(marker_detector.instance, "xrSnapshotMarkerDetectorML"),
        PFN_xrSnapshotMarkerDetectorML,
    )
    result = check_result(fxn(
        marker_detector,
        byref(snapshot_info),
    ))
    if result.is_exception():
        raise result
    return snapshot_info


def get_marker_detector_state_ml(
    marker_detector: MarkerDetectorML,
) -> MarkerDetectorStateML:
    state = MarkerDetectorStateML()
    fxn = cast(
        get_instance_proc_addr(marker_detector.instance, "xrGetMarkerDetectorStateML"),
        PFN_xrGetMarkerDetectorStateML,
    )
    result = check_result(fxn(
        marker_detector,
        byref(state),
    ))
    if result.is_exception():
        raise result
    return state


def get_markers_ml(
    marker_detector: MarkerDetectorML,
) -> Sequence[MarkerML]:
    marker_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(marker_detector.instance, "xrGetMarkersML"),
        PFN_xrGetMarkersML,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        marker_detector,
        0,
        byref(marker_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    markers = (MarkerML * marker_capacity_input.value)(*([MarkerML()] * marker_capacity_input.value))  # noqa
    result = check_result(fxn(
        marker_detector,
        marker_capacity_input,
        byref(marker_capacity_input),
        markers,
    ))
    if result.is_exception():
        raise result
    return markers  # noqa


def get_marker_reprojection_error_ml(
    marker_detector: MarkerDetectorML,
    marker: MarkerML,
) -> float:
    reprojection_error_meters = c_float()
    fxn = cast(
        get_instance_proc_addr(marker_detector.instance, "xrGetMarkerReprojectionErrorML"),
        PFN_xrGetMarkerReprojectionErrorML,
    )
    result = check_result(fxn(
        marker_detector,
        marker,
        byref(reprojection_error_meters),
    ))
    if result.is_exception():
        raise result
    return reprojection_error_meters


def get_marker_length_ml(
    marker_detector: MarkerDetectorML,
    marker: MarkerML,
) -> float:
    meters = c_float()
    fxn = cast(
        get_instance_proc_addr(marker_detector.instance, "xrGetMarkerLengthML"),
        PFN_xrGetMarkerLengthML,
    )
    result = check_result(fxn(
        marker_detector,
        marker,
        byref(meters),
    ))
    if result.is_exception():
        raise result
    return meters


def get_marker_number_ml(
    marker_detector: MarkerDetectorML,
    marker: MarkerML,
) -> int:
    number = c_uint64()
    fxn = cast(
        get_instance_proc_addr(marker_detector.instance, "xrGetMarkerNumberML"),
        PFN_xrGetMarkerNumberML,
    )
    result = check_result(fxn(
        marker_detector,
        marker,
        byref(number),
    ))
    if result.is_exception():
        raise result
    return number.value


def get_marker_string_ml(
    marker_detector: MarkerDetectorML,
    marker: MarkerML,
) -> str:
    buffer_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(marker_detector.instance, "xrGetMarkerStringML"),
        PFN_xrGetMarkerStringML,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        marker_detector,
        marker,
        0,
        byref(buffer_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    buffer = create_string_buffer(buffer_capacity_input.value)
    result = check_result(fxn(
        marker_detector,
        marker,
        buffer_capacity_input,
        byref(buffer_capacity_input),
        buffer,
    ))
    if result.is_exception():
        raise result
    return buffer.value.decode()


def create_marker_space_ml(
    session: Session,
    create_info: MarkerSpaceCreateInfoML = None,
) -> Space:
    if create_info is None:
        create_info = MarkerSpaceCreateInfoML()
    space = Space()
    space.instance = session.instance
    space._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateMarkerSpaceML"),
        PFN_xrCreateMarkerSpaceML,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(space),
    ))
    if result.is_exception():
        raise result
    return space


def enable_localization_events_ml(
    session: Session,
    info: LocalizationEnableEventsInfoML,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrEnableLocalizationEventsML"),
        PFN_xrEnableLocalizationEventsML,
    )
    result = check_result(fxn(
        session,
        info,
    ))
    if result.is_exception():
        raise result


def query_localization_maps_ml(
    session: Session,
    query_info: LocalizationMapQueryInfoBaseHeaderML = None,
) -> Sequence[LocalizationMapML]:
    map_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrQueryLocalizationMapsML"),
        PFN_xrQueryLocalizationMapsML,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        session,
        query_info,
        0,
        byref(map_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    maps = (LocalizationMapML * map_capacity_input.value)(*([LocalizationMapML()] * map_capacity_input.value))  # noqa
    result = check_result(fxn(
        session,
        cast(byref(query_info), POINTER(LocalizationMapQueryInfoBaseHeaderML)),
        map_capacity_input,
        byref(map_capacity_input),
        maps,
    ))
    if result.is_exception():
        raise result
    return maps  # noqa


def request_map_localization_ml(
    session: Session,
    request_info: MapLocalizationRequestInfoML,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrRequestMapLocalizationML"),
        PFN_xrRequestMapLocalizationML,
    )
    result = check_result(fxn(
        session,
        request_info,
    ))
    if result.is_exception():
        raise result


def import_localization_map_ml(
    session: Session,
    import_info: LocalizationMapImportInfoML,
) -> UuidEXT:
    map_uuid = UuidEXT()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrImportLocalizationMapML"),
        PFN_xrImportLocalizationMapML,
    )
    result = check_result(fxn(
        session,
        import_info,
        byref(map_uuid),
    ))
    if result.is_exception():
        raise result
    return map_uuid


def create_exported_localization_map_ml(
    session: Session,
    map_uuid: POINTER(Uuid),
) -> ExportedLocalizationMapML:
    map = ExportedLocalizationMapML()
    map.instance = session.instance
    map._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateExportedLocalizationMapML"),
        PFN_xrCreateExportedLocalizationMapML,
    )
    result = check_result(fxn(
        session,
        map_uuid,
        byref(map),
    ))
    if result.is_exception():
        raise result
    return map


def destroy_exported_localization_map_ml(
    map: ExportedLocalizationMapML,
) -> None:
    fxn = cast(
        get_instance_proc_addr(map.instance, "xrDestroyExportedLocalizationMapML"),
        PFN_xrDestroyExportedLocalizationMapML,
    )
    result = check_result(fxn(
        map,
    ))
    if result.is_exception():
        raise result


def get_exported_localization_map_data_ml(
    map: ExportedLocalizationMapML,
) -> str:
    buffer_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(map.instance, "xrGetExportedLocalizationMapDataML"),
        PFN_xrGetExportedLocalizationMapDataML,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        map,
        0,
        byref(buffer_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    buffer = create_string_buffer(buffer_capacity_input.value)
    result = check_result(fxn(
        map,
        buffer_capacity_input,
        byref(buffer_capacity_input),
        buffer,
    ))
    if result.is_exception():
        raise result
    return buffer.value.decode()


def create_spatial_anchors_async_ml(
    session: Session,
    create_info: SpatialAnchorsCreateInfoBaseHeaderML = None,
) -> FutureEXT:
    if create_info is None:
        create_info = SpatialAnchorsCreateInfoBaseHeaderML()
    future = FutureEXT()
    future.instance = session.instance
    future._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateSpatialAnchorsAsyncML"),
        PFN_xrCreateSpatialAnchorsAsyncML,
    )
    result = check_result(fxn(
        session,
        cast(byref(create_info), POINTER(SpatialAnchorsCreateInfoBaseHeaderML)),
        byref(future),
    ))
    if result.is_exception():
        raise result
    return future


def create_spatial_anchors_complete_ml(
    session: Session,
    future: FutureEXT,
) -> CreateSpatialAnchorsCompletionML:
    completion = CreateSpatialAnchorsCompletionML()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateSpatialAnchorsCompleteML"),
        PFN_xrCreateSpatialAnchorsCompleteML,
    )
    result = check_result(fxn(
        session,
        future,
        byref(completion),
    ))
    if result.is_exception():
        raise result
    return completion


def get_spatial_anchor_state_ml(
    anchor: Space,
) -> SpatialAnchorStateML:
    state = SpatialAnchorStateML()
    fxn = cast(
        get_instance_proc_addr(anchor.instance, "xrGetSpatialAnchorStateML"),
        PFN_xrGetSpatialAnchorStateML,
    )
    result = check_result(fxn(
        anchor,
        byref(state),
    ))
    if result.is_exception():
        raise result
    return state


def create_spatial_anchors_storage_ml(
    session: Session,
    create_info: SpatialAnchorsCreateStorageInfoML = None,
) -> SpatialAnchorsStorageML:
    if create_info is None:
        create_info = SpatialAnchorsCreateStorageInfoML()
    storage = SpatialAnchorsStorageML()
    storage.instance = session.instance
    storage._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateSpatialAnchorsStorageML"),
        PFN_xrCreateSpatialAnchorsStorageML,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(storage),
    ))
    if result.is_exception():
        raise result
    return storage


def destroy_spatial_anchors_storage_ml(
    storage: SpatialAnchorsStorageML,
) -> None:
    fxn = cast(
        get_instance_proc_addr(storage.instance, "xrDestroySpatialAnchorsStorageML"),
        PFN_xrDestroySpatialAnchorsStorageML,
    )
    result = check_result(fxn(
        storage,
    ))
    if result.is_exception():
        raise result


def query_spatial_anchors_async_ml(
    storage: SpatialAnchorsStorageML,
    query_info: SpatialAnchorsQueryInfoBaseHeaderML,
) -> FutureEXT:
    future = FutureEXT()
    fxn = cast(
        get_instance_proc_addr(storage.instance, "xrQuerySpatialAnchorsAsyncML"),
        PFN_xrQuerySpatialAnchorsAsyncML,
    )
    result = check_result(fxn(
        storage,
        cast(byref(query_info), POINTER(SpatialAnchorsQueryInfoBaseHeaderML)),
        byref(future),
    ))
    if result.is_exception():
        raise result
    return future


def query_spatial_anchors_complete_ml(
    storage: SpatialAnchorsStorageML,
    future: FutureEXT,
) -> SpatialAnchorsQueryCompletionML:
    completion = SpatialAnchorsQueryCompletionML()
    fxn = cast(
        get_instance_proc_addr(storage.instance, "xrQuerySpatialAnchorsCompleteML"),
        PFN_xrQuerySpatialAnchorsCompleteML,
    )
    result = check_result(fxn(
        storage,
        future,
        byref(completion),
    ))
    if result.is_exception():
        raise result
    return completion


def publish_spatial_anchors_async_ml(
    storage: SpatialAnchorsStorageML,
    publish_info: SpatialAnchorsPublishInfoML,
) -> FutureEXT:
    future = FutureEXT()
    fxn = cast(
        get_instance_proc_addr(storage.instance, "xrPublishSpatialAnchorsAsyncML"),
        PFN_xrPublishSpatialAnchorsAsyncML,
    )
    result = check_result(fxn(
        storage,
        publish_info,
        byref(future),
    ))
    if result.is_exception():
        raise result
    return future


def publish_spatial_anchors_complete_ml(
    storage: SpatialAnchorsStorageML,
    future: FutureEXT,
) -> SpatialAnchorsPublishCompletionML:
    completion = SpatialAnchorsPublishCompletionML()
    fxn = cast(
        get_instance_proc_addr(storage.instance, "xrPublishSpatialAnchorsCompleteML"),
        PFN_xrPublishSpatialAnchorsCompleteML,
    )
    result = check_result(fxn(
        storage,
        future,
        byref(completion),
    ))
    if result.is_exception():
        raise result
    return completion


def delete_spatial_anchors_async_ml(
    storage: SpatialAnchorsStorageML,
    delete_info: SpatialAnchorsDeleteInfoML,
) -> FutureEXT:
    future = FutureEXT()
    fxn = cast(
        get_instance_proc_addr(storage.instance, "xrDeleteSpatialAnchorsAsyncML"),
        PFN_xrDeleteSpatialAnchorsAsyncML,
    )
    result = check_result(fxn(
        storage,
        delete_info,
        byref(future),
    ))
    if result.is_exception():
        raise result
    return future


def delete_spatial_anchors_complete_ml(
    storage: SpatialAnchorsStorageML,
    future: FutureEXT,
) -> SpatialAnchorsDeleteCompletionML:
    completion = SpatialAnchorsDeleteCompletionML()
    fxn = cast(
        get_instance_proc_addr(storage.instance, "xrDeleteSpatialAnchorsCompleteML"),
        PFN_xrDeleteSpatialAnchorsCompleteML,
    )
    result = check_result(fxn(
        storage,
        future,
        byref(completion),
    ))
    if result.is_exception():
        raise result
    return completion


def update_spatial_anchors_expiration_async_ml(
    storage: SpatialAnchorsStorageML,
    update_info: SpatialAnchorsUpdateExpirationInfoML,
) -> FutureEXT:
    future = FutureEXT()
    fxn = cast(
        get_instance_proc_addr(storage.instance, "xrUpdateSpatialAnchorsExpirationAsyncML"),
        PFN_xrUpdateSpatialAnchorsExpirationAsyncML,
    )
    result = check_result(fxn(
        storage,
        update_info,
        byref(future),
    ))
    if result.is_exception():
        raise result
    return future


def update_spatial_anchors_expiration_complete_ml(
    storage: SpatialAnchorsStorageML,
    future: FutureEXT,
) -> SpatialAnchorsUpdateExpirationCompletionML:
    completion = SpatialAnchorsUpdateExpirationCompletionML()
    fxn = cast(
        get_instance_proc_addr(storage.instance, "xrUpdateSpatialAnchorsExpirationCompleteML"),
        PFN_xrUpdateSpatialAnchorsExpirationCompleteML,
    )
    result = check_result(fxn(
        storage,
        future,
        byref(completion),
    ))
    if result.is_exception():
        raise result
    return completion


def create_spatial_anchor_store_connection_msft(
    session: Session,
) -> SpatialAnchorStoreConnectionMSFT:
    spatial_anchor_store = SpatialAnchorStoreConnectionMSFT()
    spatial_anchor_store.instance = session.instance
    spatial_anchor_store._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateSpatialAnchorStoreConnectionMSFT"),
        PFN_xrCreateSpatialAnchorStoreConnectionMSFT,
    )
    result = check_result(fxn(
        session,
        byref(spatial_anchor_store),
    ))
    if result.is_exception():
        raise result
    return spatial_anchor_store


def destroy_spatial_anchor_store_connection_msft(
    spatial_anchor_store: SpatialAnchorStoreConnectionMSFT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(spatial_anchor_store.instance, "xrDestroySpatialAnchorStoreConnectionMSFT"),
        PFN_xrDestroySpatialAnchorStoreConnectionMSFT,
    )
    result = check_result(fxn(
        spatial_anchor_store,
    ))
    if result.is_exception():
        raise result


def persist_spatial_anchor_msft(
    spatial_anchor_store: SpatialAnchorStoreConnectionMSFT,
    spatial_anchor_persistence_info: SpatialAnchorPersistenceInfoMSFT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(spatial_anchor_store.instance, "xrPersistSpatialAnchorMSFT"),
        PFN_xrPersistSpatialAnchorMSFT,
    )
    result = check_result(fxn(
        spatial_anchor_store,
        spatial_anchor_persistence_info,
    ))
    if result.is_exception():
        raise result


def enumerate_persisted_spatial_anchor_names_msft(
    spatial_anchor_store: SpatialAnchorStoreConnectionMSFT,
) -> Sequence[SpatialAnchorPersistenceNameMSFT]:
    spatial_anchor_name_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(spatial_anchor_store.instance, "xrEnumeratePersistedSpatialAnchorNamesMSFT"),
        PFN_xrEnumeratePersistedSpatialAnchorNamesMSFT,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        spatial_anchor_store,
        0,
        byref(spatial_anchor_name_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    spatial_anchor_names = (SpatialAnchorPersistenceNameMSFT * spatial_anchor_name_capacity_input.value)(*([SpatialAnchorPersistenceNameMSFT()] * spatial_anchor_name_capacity_input.value))  # noqa
    result = check_result(fxn(
        spatial_anchor_store,
        spatial_anchor_name_capacity_input,
        byref(spatial_anchor_name_capacity_input),
        spatial_anchor_names,
    ))
    if result.is_exception():
        raise result
    return spatial_anchor_names  # noqa


def create_spatial_anchor_from_persisted_name_msft(
    session: Session,
    spatial_anchor_create_info: SpatialAnchorFromPersistedAnchorCreateInfoMSFT,
) -> SpatialAnchorMSFT:
    spatial_anchor = SpatialAnchorMSFT()
    spatial_anchor.instance = session.instance
    spatial_anchor._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateSpatialAnchorFromPersistedNameMSFT"),
        PFN_xrCreateSpatialAnchorFromPersistedNameMSFT,
    )
    result = check_result(fxn(
        session,
        spatial_anchor_create_info,
        byref(spatial_anchor),
    ))
    if result.is_exception():
        raise result
    return spatial_anchor


def unpersist_spatial_anchor_msft(
    spatial_anchor_store: SpatialAnchorStoreConnectionMSFT,
    spatial_anchor_persistence_name: SpatialAnchorPersistenceNameMSFT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(spatial_anchor_store.instance, "xrUnpersistSpatialAnchorMSFT"),
        PFN_xrUnpersistSpatialAnchorMSFT,
    )
    result = check_result(fxn(
        spatial_anchor_store,
        spatial_anchor_persistence_name,
    ))
    if result.is_exception():
        raise result


def clear_spatial_anchor_store_msft(
    spatial_anchor_store: SpatialAnchorStoreConnectionMSFT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(spatial_anchor_store.instance, "xrClearSpatialAnchorStoreMSFT"),
        PFN_xrClearSpatialAnchorStoreMSFT,
    )
    result = check_result(fxn(
        spatial_anchor_store,
    ))
    if result.is_exception():
        raise result


def get_scene_marker_raw_data_msft(
    scene: SceneMSFT,
    marker_id: UuidMSFT,
) -> Sequence[int]:
    buffer_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(scene.instance, "xrGetSceneMarkerRawDataMSFT"),
        PFN_xrGetSceneMarkerRawDataMSFT,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        scene,
        marker_id,
        0,
        byref(buffer_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    buffer = (c_uint8 * buffer_capacity_input.value)(*([c_uint8()] * buffer_capacity_input.value))  # noqa
    result = check_result(fxn(
        scene,
        marker_id,
        buffer_capacity_input,
        byref(buffer_capacity_input),
        buffer,
    ))
    if result.is_exception():
        raise result
    return buffer  # noqa


def get_scene_marker_decoded_string_msft(
    scene: SceneMSFT,
    marker_id: UuidMSFT,
) -> str:
    buffer_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(scene.instance, "xrGetSceneMarkerDecodedStringMSFT"),
        PFN_xrGetSceneMarkerDecodedStringMSFT,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        scene,
        marker_id,
        0,
        byref(buffer_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    buffer = create_string_buffer(buffer_capacity_input.value)
    result = check_result(fxn(
        scene,
        marker_id,
        buffer_capacity_input,
        byref(buffer_capacity_input),
        buffer,
    ))
    if result.is_exception():
        raise result
    return buffer.value.decode()


def query_spaces_fb(
    session: Session,
    info: SpaceQueryInfoBaseHeaderFB,
) -> AsyncRequestIdFB:
    request_id = AsyncRequestIdFB()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrQuerySpacesFB"),
        PFN_xrQuerySpacesFB,
    )
    result = check_result(fxn(
        session,
        cast(byref(info), POINTER(SpaceQueryInfoBaseHeaderFB)),
        byref(request_id),
    ))
    if result.is_exception():
        raise result
    return request_id


def retrieve_space_query_results_fb(
    session: Session,
    request_id: AsyncRequestIdFB,
) -> SpaceQueryResultsFB:
    results = SpaceQueryResultsFB()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrRetrieveSpaceQueryResultsFB"),
        PFN_xrRetrieveSpaceQueryResultsFB,
    )
    result = check_result(fxn(
        session,
        request_id,
        byref(results),
    ))
    if result.is_exception():
        raise result
    return results


def save_space_fb(
    session: Session,
    info: SpaceSaveInfoFB,
) -> AsyncRequestIdFB:
    request_id = AsyncRequestIdFB()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrSaveSpaceFB"),
        PFN_xrSaveSpaceFB,
    )
    result = check_result(fxn(
        session,
        info,
        byref(request_id),
    ))
    if result.is_exception():
        raise result
    return request_id


def erase_space_fb(
    session: Session,
    info: SpaceEraseInfoFB,
) -> AsyncRequestIdFB:
    request_id = AsyncRequestIdFB()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrEraseSpaceFB"),
        PFN_xrEraseSpaceFB,
    )
    result = check_result(fxn(
        session,
        info,
        byref(request_id),
    ))
    if result.is_exception():
        raise result
    return request_id


def share_spaces_fb(
    session: Session,
    info: SpaceShareInfoFB,
) -> AsyncRequestIdFB:
    request_id = AsyncRequestIdFB()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrShareSpacesFB"),
        PFN_xrShareSpacesFB,
    )
    result = check_result(fxn(
        session,
        info,
        byref(request_id),
    ))
    if result.is_exception():
        raise result
    return request_id


def get_space_bounding_box_2d_fb(
    session: Session,
    space: Space,
) -> Rect2Df:
    bounding_box_2d_output = Rect2Df()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrGetSpaceBoundingBox2DFB"),
        PFN_xrGetSpaceBoundingBox2DFB,
    )
    result = check_result(fxn(
        session,
        space,
        byref(bounding_box_2d_output),
    ))
    if result.is_exception():
        raise result
    return bounding_box_2d_output


def get_space_bounding_box_3d_fb(
    session: Session,
    space: Space,
) -> Rect3DfFB:
    bounding_box_3d_output = Rect3DfFB()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrGetSpaceBoundingBox3DFB"),
        PFN_xrGetSpaceBoundingBox3DFB,
    )
    result = check_result(fxn(
        session,
        space,
        byref(bounding_box_3d_output),
    ))
    if result.is_exception():
        raise result
    return bounding_box_3d_output


def get_space_semantic_labels_fb(
    session: Session,
    space: Space,
) -> SemanticLabelsFB:
    semantic_labels_output = SemanticLabelsFB()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrGetSpaceSemanticLabelsFB"),
        PFN_xrGetSpaceSemanticLabelsFB,
    )
    result = check_result(fxn(
        session,
        space,
        byref(semantic_labels_output),
    ))
    if result.is_exception():
        raise result
    return semantic_labels_output


def get_space_boundary_2d_fb(
    session: Session,
    space: Space,
) -> Boundary2DFB:
    boundary_2d_output = Boundary2DFB()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrGetSpaceBoundary2DFB"),
        PFN_xrGetSpaceBoundary2DFB,
    )
    result = check_result(fxn(
        session,
        space,
        byref(boundary_2d_output),
    ))
    if result.is_exception():
        raise result
    return boundary_2d_output


def get_space_room_layout_fb(
    session: Session,
    space: Space,
) -> RoomLayoutFB:
    room_layout_output = RoomLayoutFB()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrGetSpaceRoomLayoutFB"),
        PFN_xrGetSpaceRoomLayoutFB,
    )
    result = check_result(fxn(
        session,
        space,
        byref(room_layout_output),
    ))
    if result.is_exception():
        raise result
    return room_layout_output


def set_digital_lens_control_almalence(
    session: Session,
    digital_lens_control: DigitalLensControlALMALENCE,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrSetDigitalLensControlALMALENCE"),
        PFN_xrSetDigitalLensControlALMALENCE,
    )
    result = check_result(fxn(
        session,
        digital_lens_control,
    ))
    if result.is_exception():
        raise result


def request_scene_capture_fb(
    session: Session,
    info: SceneCaptureRequestInfoFB,
) -> AsyncRequestIdFB:
    request_id = AsyncRequestIdFB()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrRequestSceneCaptureFB"),
        PFN_xrRequestSceneCaptureFB,
    )
    result = check_result(fxn(
        session,
        info,
        byref(request_id),
    ))
    if result.is_exception():
        raise result
    return request_id


def get_space_container_fb(
    session: Session,
    space: Space,
) -> SpaceContainerFB:
    space_container_output = SpaceContainerFB()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrGetSpaceContainerFB"),
        PFN_xrGetSpaceContainerFB,
    )
    result = check_result(fxn(
        session,
        space,
        byref(space_container_output),
    ))
    if result.is_exception():
        raise result
    return space_container_output


def get_foveation_eye_tracked_state_meta(
    session: Session,
) -> FoveationEyeTrackedStateMETA:
    foveation_state = FoveationEyeTrackedStateMETA()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrGetFoveationEyeTrackedStateMETA"),
        PFN_xrGetFoveationEyeTrackedStateMETA,
    )
    result = check_result(fxn(
        session,
        byref(foveation_state),
    ))
    if result.is_exception():
        raise result
    return foveation_state


def create_face_tracker_fb(
    session: Session,
    create_info: FaceTrackerCreateInfoFB = None,
) -> FaceTrackerFB:
    if create_info is None:
        create_info = FaceTrackerCreateInfoFB()
    face_tracker = FaceTrackerFB()
    face_tracker.instance = session.instance
    face_tracker._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateFaceTrackerFB"),
        PFN_xrCreateFaceTrackerFB,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(face_tracker),
    ))
    if result.is_exception():
        raise result
    return face_tracker


def destroy_face_tracker_fb(
    face_tracker: FaceTrackerFB,
) -> None:
    fxn = cast(
        get_instance_proc_addr(face_tracker.instance, "xrDestroyFaceTrackerFB"),
        PFN_xrDestroyFaceTrackerFB,
    )
    result = check_result(fxn(
        face_tracker,
    ))
    if result.is_exception():
        raise result


def get_face_expression_weights_fb(
    face_tracker: FaceTrackerFB,
    expression_info: FaceExpressionInfoFB,
) -> FaceExpressionWeightsFB:
    expression_weights = FaceExpressionWeightsFB()
    fxn = cast(
        get_instance_proc_addr(face_tracker.instance, "xrGetFaceExpressionWeightsFB"),
        PFN_xrGetFaceExpressionWeightsFB,
    )
    result = check_result(fxn(
        face_tracker,
        expression_info,
        byref(expression_weights),
    ))
    if result.is_exception():
        raise result
    return expression_weights


def create_eye_tracker_fb(
    session: Session,
    create_info: EyeTrackerCreateInfoFB = None,
) -> EyeTrackerFB:
    if create_info is None:
        create_info = EyeTrackerCreateInfoFB()
    eye_tracker = EyeTrackerFB()
    eye_tracker.instance = session.instance
    eye_tracker._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateEyeTrackerFB"),
        PFN_xrCreateEyeTrackerFB,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(eye_tracker),
    ))
    if result.is_exception():
        raise result
    return eye_tracker


def destroy_eye_tracker_fb(
    eye_tracker: EyeTrackerFB,
) -> None:
    fxn = cast(
        get_instance_proc_addr(eye_tracker.instance, "xrDestroyEyeTrackerFB"),
        PFN_xrDestroyEyeTrackerFB,
    )
    result = check_result(fxn(
        eye_tracker,
    ))
    if result.is_exception():
        raise result


def get_eye_gazes_fb(
    eye_tracker: EyeTrackerFB,
    gaze_info: EyeGazesInfoFB,
) -> EyeGazesFB:
    eye_gazes = EyeGazesFB()
    fxn = cast(
        get_instance_proc_addr(eye_tracker.instance, "xrGetEyeGazesFB"),
        PFN_xrGetEyeGazesFB,
    )
    result = check_result(fxn(
        eye_tracker,
        gaze_info,
        byref(eye_gazes),
    ))
    if result.is_exception():
        raise result
    return eye_gazes


def passthrough_layer_set_keyboard_hands_intensity_fb(
    layer: PassthroughLayerFB,
    intensity: PassthroughKeyboardHandsIntensityFB,
) -> None:
    fxn = cast(
        get_instance_proc_addr(layer.instance, "xrPassthroughLayerSetKeyboardHandsIntensityFB"),
        PFN_xrPassthroughLayerSetKeyboardHandsIntensityFB,
    )
    result = check_result(fxn(
        layer,
        intensity,
    ))
    if result.is_exception():
        raise result


def get_device_sample_rate_fb(
    session: Session,
    haptic_action_info: HapticActionInfo,
) -> DevicePcmSampleRateGetInfoFB:
    device_sample_rate = DevicePcmSampleRateGetInfoFB()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrGetDeviceSampleRateFB"),
        PFN_xrGetDeviceSampleRateFB,
    )
    result = check_result(fxn(
        session,
        haptic_action_info,
        byref(device_sample_rate),
    ))
    if result.is_exception():
        raise result
    return device_sample_rate


def get_passthrough_preferences_meta(
    session: Session,
) -> PassthroughPreferencesMETA:
    preferences = PassthroughPreferencesMETA()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrGetPassthroughPreferencesMETA"),
        PFN_xrGetPassthroughPreferencesMETA,
    )
    result = check_result(fxn(
        session,
        byref(preferences),
    ))
    if result.is_exception():
        raise result
    return preferences


def create_virtual_keyboard_meta(
    session: Session,
    create_info: VirtualKeyboardCreateInfoMETA = None,
) -> VirtualKeyboardMETA:
    if create_info is None:
        create_info = VirtualKeyboardCreateInfoMETA()
    keyboard = VirtualKeyboardMETA()
    keyboard.instance = session.instance
    keyboard._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateVirtualKeyboardMETA"),
        PFN_xrCreateVirtualKeyboardMETA,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(keyboard),
    ))
    if result.is_exception():
        raise result
    return keyboard


def destroy_virtual_keyboard_meta(
    keyboard: VirtualKeyboardMETA,
) -> None:
    fxn = cast(
        get_instance_proc_addr(keyboard.instance, "xrDestroyVirtualKeyboardMETA"),
        PFN_xrDestroyVirtualKeyboardMETA,
    )
    result = check_result(fxn(
        keyboard,
    ))
    if result.is_exception():
        raise result


def create_virtual_keyboard_space_meta(
    session: Session,
    keyboard: VirtualKeyboardMETA,
    create_info: VirtualKeyboardSpaceCreateInfoMETA = None,
) -> Space:
    if create_info is None:
        create_info = VirtualKeyboardSpaceCreateInfoMETA()
    keyboard_space = Space()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateVirtualKeyboardSpaceMETA"),
        PFN_xrCreateVirtualKeyboardSpaceMETA,
    )
    result = check_result(fxn(
        session,
        keyboard,
        create_info,
        byref(keyboard_space),
    ))
    if result.is_exception():
        raise result
    return keyboard_space


def suggest_virtual_keyboard_location_meta(
    keyboard: VirtualKeyboardMETA,
    location_info: VirtualKeyboardLocationInfoMETA,
) -> None:
    fxn = cast(
        get_instance_proc_addr(keyboard.instance, "xrSuggestVirtualKeyboardLocationMETA"),
        PFN_xrSuggestVirtualKeyboardLocationMETA,
    )
    result = check_result(fxn(
        keyboard,
        location_info,
    ))
    if result.is_exception():
        raise result


def get_virtual_keyboard_scale_meta(
    keyboard: VirtualKeyboardMETA,
) -> float:
    scale = c_float()
    fxn = cast(
        get_instance_proc_addr(keyboard.instance, "xrGetVirtualKeyboardScaleMETA"),
        PFN_xrGetVirtualKeyboardScaleMETA,
    )
    result = check_result(fxn(
        keyboard,
        byref(scale),
    ))
    if result.is_exception():
        raise result
    return scale


def set_virtual_keyboard_model_visibility_meta(
    keyboard: VirtualKeyboardMETA,
    model_visibility: VirtualKeyboardModelVisibilitySetInfoMETA,
) -> None:
    fxn = cast(
        get_instance_proc_addr(keyboard.instance, "xrSetVirtualKeyboardModelVisibilityMETA"),
        PFN_xrSetVirtualKeyboardModelVisibilityMETA,
    )
    result = check_result(fxn(
        keyboard,
        model_visibility,
    ))
    if result.is_exception():
        raise result


def get_virtual_keyboard_model_animation_states_meta(
    keyboard: VirtualKeyboardMETA,
) -> VirtualKeyboardModelAnimationStatesMETA:
    animation_states = VirtualKeyboardModelAnimationStatesMETA()
    fxn = cast(
        get_instance_proc_addr(keyboard.instance, "xrGetVirtualKeyboardModelAnimationStatesMETA"),
        PFN_xrGetVirtualKeyboardModelAnimationStatesMETA,
    )
    result = check_result(fxn(
        keyboard,
        byref(animation_states),
    ))
    if result.is_exception():
        raise result
    return animation_states


def get_virtual_keyboard_dirty_textures_meta(
    keyboard: VirtualKeyboardMETA,
) -> Sequence[int]:
    texture_id_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(keyboard.instance, "xrGetVirtualKeyboardDirtyTexturesMETA"),
        PFN_xrGetVirtualKeyboardDirtyTexturesMETA,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        keyboard,
        0,
        byref(texture_id_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    texture_ids = (c_uint64 * texture_id_capacity_input.value)(*([c_uint64()] * texture_id_capacity_input.value))  # noqa
    result = check_result(fxn(
        keyboard,
        texture_id_capacity_input,
        byref(texture_id_capacity_input),
        texture_ids,
    ))
    if result.is_exception():
        raise result
    return texture_ids  # noqa


def get_virtual_keyboard_texture_data_meta(
    keyboard: VirtualKeyboardMETA,
    texture_id: int,
) -> VirtualKeyboardTextureDataMETA:
    texture_data = VirtualKeyboardTextureDataMETA()
    fxn = cast(
        get_instance_proc_addr(keyboard.instance, "xrGetVirtualKeyboardTextureDataMETA"),
        PFN_xrGetVirtualKeyboardTextureDataMETA,
    )
    result = check_result(fxn(
        keyboard,
        texture_id,
        byref(texture_data),
    ))
    if result.is_exception():
        raise result
    return texture_data


def send_virtual_keyboard_input_meta(
    keyboard: VirtualKeyboardMETA,
    info: VirtualKeyboardInputInfoMETA,
) -> Posef:
    interactor_root_pose = Posef()
    fxn = cast(
        get_instance_proc_addr(keyboard.instance, "xrSendVirtualKeyboardInputMETA"),
        PFN_xrSendVirtualKeyboardInputMETA,
    )
    result = check_result(fxn(
        keyboard,
        info,
        byref(interactor_root_pose),
    ))
    if result.is_exception():
        raise result
    return interactor_root_pose


def change_virtual_keyboard_text_context_meta(
    keyboard: VirtualKeyboardMETA,
    change_info: VirtualKeyboardTextContextChangeInfoMETA,
) -> None:
    fxn = cast(
        get_instance_proc_addr(keyboard.instance, "xrChangeVirtualKeyboardTextContextMETA"),
        PFN_xrChangeVirtualKeyboardTextContextMETA,
    )
    result = check_result(fxn(
        keyboard,
        change_info,
    ))
    if result.is_exception():
        raise result


def enumerate_external_cameras_oculus(
    session: Session,
) -> Sequence[ExternalCameraOCULUS]:
    camera_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrEnumerateExternalCamerasOCULUS"),
        PFN_xrEnumerateExternalCamerasOCULUS,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        session,
        0,
        byref(camera_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    cameras = (ExternalCameraOCULUS * camera_capacity_input.value)(*([ExternalCameraOCULUS()] * camera_capacity_input.value))  # noqa
    result = check_result(fxn(
        session,
        camera_capacity_input,
        byref(camera_capacity_input),
        cameras,
    ))
    if result.is_exception():
        raise result
    return cameras  # noqa


def enumerate_performance_metrics_counter_paths_meta(
    instance: Instance,
) -> Sequence[Path]:
    counter_path_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrEnumeratePerformanceMetricsCounterPathsMETA"),
        PFN_xrEnumeratePerformanceMetricsCounterPathsMETA,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        instance,
        0,
        byref(counter_path_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    counter_paths = (Path * counter_path_capacity_input.value)(*([Path()] * counter_path_capacity_input.value))  # noqa
    result = check_result(fxn(
        instance,
        counter_path_capacity_input,
        byref(counter_path_capacity_input),
        counter_paths,
    ))
    if result.is_exception():
        raise result
    return counter_paths  # noqa


def set_performance_metrics_state_meta(
    session: Session,
    state: PerformanceMetricsStateMETA,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrSetPerformanceMetricsStateMETA"),
        PFN_xrSetPerformanceMetricsStateMETA,
    )
    result = check_result(fxn(
        session,
        state,
    ))
    if result.is_exception():
        raise result


def get_performance_metrics_state_meta(
    session: Session,
) -> PerformanceMetricsStateMETA:
    state = PerformanceMetricsStateMETA()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrGetPerformanceMetricsStateMETA"),
        PFN_xrGetPerformanceMetricsStateMETA,
    )
    result = check_result(fxn(
        session,
        byref(state),
    ))
    if result.is_exception():
        raise result
    return state


def query_performance_metrics_counter_meta(
    session: Session,
    counter_path: Path,
) -> PerformanceMetricsCounterMETA:
    counter = PerformanceMetricsCounterMETA()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrQueryPerformanceMetricsCounterMETA"),
        PFN_xrQueryPerformanceMetricsCounterMETA,
    )
    result = check_result(fxn(
        session,
        counter_path,
        byref(counter),
    ))
    if result.is_exception():
        raise result
    return counter


def save_space_list_fb(
    session: Session,
    info: SpaceListSaveInfoFB,
) -> AsyncRequestIdFB:
    request_id = AsyncRequestIdFB()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrSaveSpaceListFB"),
        PFN_xrSaveSpaceListFB,
    )
    result = check_result(fxn(
        session,
        info,
        byref(request_id),
    ))
    if result.is_exception():
        raise result
    return request_id


def create_space_user_fb(
    session: Session,
    info: SpaceUserCreateInfoFB,
) -> SpaceUserFB:
    user = SpaceUserFB()
    user.instance = session.instance
    user._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateSpaceUserFB"),
        PFN_xrCreateSpaceUserFB,
    )
    result = check_result(fxn(
        session,
        info,
        byref(user),
    ))
    if result.is_exception():
        raise result
    return user


def get_space_user_id_fb(
    user: SpaceUserFB,
) -> SpaceUserIdFB:
    user_id = SpaceUserIdFB()
    fxn = cast(
        get_instance_proc_addr(user.instance, "xrGetSpaceUserIdFB"),
        PFN_xrGetSpaceUserIdFB,
    )
    result = check_result(fxn(
        user,
        byref(user_id),
    ))
    if result.is_exception():
        raise result
    return user_id


def destroy_space_user_fb(
    user: SpaceUserFB,
) -> None:
    fxn = cast(
        get_instance_proc_addr(user.instance, "xrDestroySpaceUserFB"),
        PFN_xrDestroySpaceUserFB,
    )
    result = check_result(fxn(
        user,
    ))
    if result.is_exception():
        raise result


def discover_spaces_meta(
    session: Session,
    info: SpaceDiscoveryInfoMETA,
) -> AsyncRequestIdFB:
    request_id = AsyncRequestIdFB()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrDiscoverSpacesMETA"),
        PFN_xrDiscoverSpacesMETA,
    )
    result = check_result(fxn(
        session,
        info,
        byref(request_id),
    ))
    if result.is_exception():
        raise result
    return request_id


def retrieve_space_discovery_results_meta(
    session: Session,
    request_id: AsyncRequestIdFB,
) -> SpaceDiscoveryResultsMETA:
    results = SpaceDiscoveryResultsMETA()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrRetrieveSpaceDiscoveryResultsMETA"),
        PFN_xrRetrieveSpaceDiscoveryResultsMETA,
    )
    result = check_result(fxn(
        session,
        request_id,
        byref(results),
    ))
    if result.is_exception():
        raise result
    return results


def get_recommended_layer_resolution_meta(
    session: Session,
    info: RecommendedLayerResolutionGetInfoMETA,
) -> RecommendedLayerResolutionMETA:
    resolution = RecommendedLayerResolutionMETA()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrGetRecommendedLayerResolutionMETA"),
        PFN_xrGetRecommendedLayerResolutionMETA,
    )
    result = check_result(fxn(
        session,
        info,
        byref(resolution),
    ))
    if result.is_exception():
        raise result
    return resolution


def save_spaces_meta(
    session: Session,
    info: SpacesSaveInfoMETA,
) -> AsyncRequestIdFB:
    request_id = AsyncRequestIdFB()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrSaveSpacesMETA"),
        PFN_xrSaveSpacesMETA,
    )
    result = check_result(fxn(
        session,
        info,
        byref(request_id),
    ))
    if result.is_exception():
        raise result
    return request_id


def erase_spaces_meta(
    session: Session,
    info: SpacesEraseInfoMETA,
) -> AsyncRequestIdFB:
    request_id = AsyncRequestIdFB()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrEraseSpacesMETA"),
        PFN_xrEraseSpacesMETA,
    )
    result = check_result(fxn(
        session,
        info,
        byref(request_id),
    ))
    if result.is_exception():
        raise result
    return request_id


def create_passthrough_color_lut_meta(
    passthrough: PassthroughFB,
    create_info: PassthroughColorLutCreateInfoMETA = None,
) -> PassthroughColorLutMETA:
    if create_info is None:
        create_info = PassthroughColorLutCreateInfoMETA()
    color_lut = PassthroughColorLutMETA()
    color_lut.instance = passthrough.instance
    color_lut._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(passthrough.instance, "xrCreatePassthroughColorLutMETA"),
        PFN_xrCreatePassthroughColorLutMETA,
    )
    result = check_result(fxn(
        passthrough,
        create_info,
        byref(color_lut),
    ))
    if result.is_exception():
        raise result
    return color_lut


def destroy_passthrough_color_lut_meta(
    color_lut: PassthroughColorLutMETA,
) -> None:
    fxn = cast(
        get_instance_proc_addr(color_lut.instance, "xrDestroyPassthroughColorLutMETA"),
        PFN_xrDestroyPassthroughColorLutMETA,
    )
    result = check_result(fxn(
        color_lut,
    ))
    if result.is_exception():
        raise result


def update_passthrough_color_lut_meta(
    color_lut: PassthroughColorLutMETA,
    update_info: PassthroughColorLutUpdateInfoMETA,
) -> None:
    fxn = cast(
        get_instance_proc_addr(color_lut.instance, "xrUpdatePassthroughColorLutMETA"),
        PFN_xrUpdatePassthroughColorLutMETA,
    )
    result = check_result(fxn(
        color_lut,
        update_info,
    ))
    if result.is_exception():
        raise result


def get_space_triangle_mesh_meta(
    space: Space,
    get_info: SpaceTriangleMeshGetInfoMETA,
) -> SpaceTriangleMeshMETA:
    triangle_mesh_output = SpaceTriangleMeshMETA()
    fxn = cast(
        get_instance_proc_addr(space.instance, "xrGetSpaceTriangleMeshMETA"),
        PFN_xrGetSpaceTriangleMeshMETA,
    )
    result = check_result(fxn(
        space,
        get_info,
        byref(triangle_mesh_output),
    ))
    if result.is_exception():
        raise result
    return triangle_mesh_output


def suggest_body_tracking_calibration_override_meta(
    body_tracker: BodyTrackerFB,
    calibration_info: BodyTrackingCalibrationInfoMETA,
) -> None:
    fxn = cast(
        get_instance_proc_addr(body_tracker.instance, "xrSuggestBodyTrackingCalibrationOverrideMETA"),
        PFN_xrSuggestBodyTrackingCalibrationOverrideMETA,
    )
    result = check_result(fxn(
        body_tracker,
        calibration_info,
    ))
    if result.is_exception():
        raise result


def reset_body_tracking_calibration_meta(
    body_tracker: BodyTrackerFB,
) -> None:
    fxn = cast(
        get_instance_proc_addr(body_tracker.instance, "xrResetBodyTrackingCalibrationMETA"),
        PFN_xrResetBodyTrackingCalibrationMETA,
    )
    result = check_result(fxn(
        body_tracker,
    ))
    if result.is_exception():
        raise result


def create_face_tracker2_fb(
    session: Session,
    create_info: FaceTrackerCreateInfo2FB = None,
) -> FaceTracker2FB:
    if create_info is None:
        create_info = FaceTrackerCreateInfo2FB()
    face_tracker = FaceTracker2FB()
    face_tracker.instance = session.instance
    face_tracker._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateFaceTracker2FB"),
        PFN_xrCreateFaceTracker2FB,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(face_tracker),
    ))
    if result.is_exception():
        raise result
    return face_tracker


def destroy_face_tracker2_fb(
    face_tracker: FaceTracker2FB,
) -> None:
    fxn = cast(
        get_instance_proc_addr(face_tracker.instance, "xrDestroyFaceTracker2FB"),
        PFN_xrDestroyFaceTracker2FB,
    )
    result = check_result(fxn(
        face_tracker,
    ))
    if result.is_exception():
        raise result


def get_face_expression_weights2_fb(
    face_tracker: FaceTracker2FB,
    expression_info: FaceExpressionInfo2FB,
) -> FaceExpressionWeights2FB:
    expression_weights = FaceExpressionWeights2FB()
    fxn = cast(
        get_instance_proc_addr(face_tracker.instance, "xrGetFaceExpressionWeights2FB"),
        PFN_xrGetFaceExpressionWeights2FB,
    )
    result = check_result(fxn(
        face_tracker,
        expression_info,
        byref(expression_weights),
    ))
    if result.is_exception():
        raise result
    return expression_weights


def share_spaces_meta(
    session: Session,
    info: ShareSpacesInfoMETA,
) -> AsyncRequestIdFB:
    request_id = AsyncRequestIdFB()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrShareSpacesMETA"),
        PFN_xrShareSpacesMETA,
    )
    result = check_result(fxn(
        session,
        info,
        byref(request_id),
    ))
    if result.is_exception():
        raise result
    return request_id


def create_environment_depth_provider_meta(
    session: Session,
    create_info: EnvironmentDepthProviderCreateInfoMETA = None,
) -> EnvironmentDepthProviderMETA:
    if create_info is None:
        create_info = EnvironmentDepthProviderCreateInfoMETA()
    environment_depth_provider = EnvironmentDepthProviderMETA()
    environment_depth_provider.instance = session.instance
    environment_depth_provider._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateEnvironmentDepthProviderMETA"),
        PFN_xrCreateEnvironmentDepthProviderMETA,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(environment_depth_provider),
    ))
    if result.is_exception():
        raise result
    return environment_depth_provider


def destroy_environment_depth_provider_meta(
    environment_depth_provider: EnvironmentDepthProviderMETA,
) -> None:
    fxn = cast(
        get_instance_proc_addr(environment_depth_provider.instance, "xrDestroyEnvironmentDepthProviderMETA"),
        PFN_xrDestroyEnvironmentDepthProviderMETA,
    )
    result = check_result(fxn(
        environment_depth_provider,
    ))
    if result.is_exception():
        raise result


def start_environment_depth_provider_meta(
    environment_depth_provider: EnvironmentDepthProviderMETA,
) -> None:
    fxn = cast(
        get_instance_proc_addr(environment_depth_provider.instance, "xrStartEnvironmentDepthProviderMETA"),
        PFN_xrStartEnvironmentDepthProviderMETA,
    )
    result = check_result(fxn(
        environment_depth_provider,
    ))
    if result.is_exception():
        raise result


def stop_environment_depth_provider_meta(
    environment_depth_provider: EnvironmentDepthProviderMETA,
) -> None:
    fxn = cast(
        get_instance_proc_addr(environment_depth_provider.instance, "xrStopEnvironmentDepthProviderMETA"),
        PFN_xrStopEnvironmentDepthProviderMETA,
    )
    result = check_result(fxn(
        environment_depth_provider,
    ))
    if result.is_exception():
        raise result


def create_environment_depth_swapchain_meta(
    environment_depth_provider: EnvironmentDepthProviderMETA,
    create_info: EnvironmentDepthSwapchainCreateInfoMETA = None,
) -> EnvironmentDepthSwapchainMETA:
    if create_info is None:
        create_info = EnvironmentDepthSwapchainCreateInfoMETA()
    swapchain = EnvironmentDepthSwapchainMETA()
    swapchain.instance = environment_depth_provider.instance
    swapchain._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(environment_depth_provider.instance, "xrCreateEnvironmentDepthSwapchainMETA"),
        PFN_xrCreateEnvironmentDepthSwapchainMETA,
    )
    result = check_result(fxn(
        environment_depth_provider,
        create_info,
        byref(swapchain),
    ))
    if result.is_exception():
        raise result
    return swapchain


def destroy_environment_depth_swapchain_meta(
    swapchain: EnvironmentDepthSwapchainMETA,
) -> None:
    fxn = cast(
        get_instance_proc_addr(swapchain.instance, "xrDestroyEnvironmentDepthSwapchainMETA"),
        PFN_xrDestroyEnvironmentDepthSwapchainMETA,
    )
    result = check_result(fxn(
        swapchain,
    ))
    if result.is_exception():
        raise result


def enumerate_environment_depth_swapchain_images_meta(
    swapchain: EnvironmentDepthSwapchainMETA,
) -> Sequence[SwapchainImageBaseHeader]:
    image_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(swapchain.instance, "xrEnumerateEnvironmentDepthSwapchainImagesMETA"),
        PFN_xrEnumerateEnvironmentDepthSwapchainImagesMETA,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        swapchain,
        0,
        byref(image_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    images = (SwapchainImageBaseHeader * image_capacity_input.value)(*([SwapchainImageBaseHeader()] * image_capacity_input.value))  # noqa
    result = check_result(fxn(
        swapchain,
        image_capacity_input,
        byref(image_capacity_input),
        images,
    ))
    if result.is_exception():
        raise result
    return images  # noqa


def get_environment_depth_swapchain_state_meta(
    swapchain: EnvironmentDepthSwapchainMETA,
) -> EnvironmentDepthSwapchainStateMETA:
    state = EnvironmentDepthSwapchainStateMETA()
    fxn = cast(
        get_instance_proc_addr(swapchain.instance, "xrGetEnvironmentDepthSwapchainStateMETA"),
        PFN_xrGetEnvironmentDepthSwapchainStateMETA,
    )
    result = check_result(fxn(
        swapchain,
        byref(state),
    ))
    if result.is_exception():
        raise result
    return state


def acquire_environment_depth_image_meta(
    environment_depth_provider: EnvironmentDepthProviderMETA,
    acquire_info: EnvironmentDepthImageAcquireInfoMETA,
) -> EnvironmentDepthImageMETA:
    environment_depth_image = EnvironmentDepthImageMETA()
    fxn = cast(
        get_instance_proc_addr(environment_depth_provider.instance, "xrAcquireEnvironmentDepthImageMETA"),
        PFN_xrAcquireEnvironmentDepthImageMETA,
    )
    result = check_result(fxn(
        environment_depth_provider,
        acquire_info,
        byref(environment_depth_image),
    ))
    if result.is_exception():
        raise result
    return environment_depth_image


def set_environment_depth_hand_removal_meta(
    environment_depth_provider: EnvironmentDepthProviderMETA,
    set_info: EnvironmentDepthHandRemovalSetInfoMETA,
) -> None:
    fxn = cast(
        get_instance_proc_addr(environment_depth_provider.instance, "xrSetEnvironmentDepthHandRemovalMETA"),
        PFN_xrSetEnvironmentDepthHandRemovalMETA,
    )
    result = check_result(fxn(
        environment_depth_provider,
        set_info,
    ))
    if result.is_exception():
        raise result


def create_render_model_ext(
    session: Session,
    create_info: RenderModelCreateInfoEXT = None,
) -> RenderModelEXT:
    if create_info is None:
        create_info = RenderModelCreateInfoEXT()
    render_model = RenderModelEXT()
    render_model.instance = session.instance
    render_model._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateRenderModelEXT"),
        PFN_xrCreateRenderModelEXT,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(render_model),
    ))
    if result.is_exception():
        raise result
    return render_model


def destroy_render_model_ext(
    render_model: RenderModelEXT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(render_model.instance, "xrDestroyRenderModelEXT"),
        PFN_xrDestroyRenderModelEXT,
    )
    result = check_result(fxn(
        render_model,
    ))
    if result.is_exception():
        raise result


def get_render_model_properties_ext(
    render_model: RenderModelEXT,
    get_info: RenderModelPropertiesGetInfoEXT = None,
) -> RenderModelPropertiesEXT:
    properties = RenderModelPropertiesEXT()
    fxn = cast(
        get_instance_proc_addr(render_model.instance, "xrGetRenderModelPropertiesEXT"),
        PFN_xrGetRenderModelPropertiesEXT,
    )
    result = check_result(fxn(
        render_model,
        get_info,
        byref(properties),
    ))
    if result.is_exception():
        raise result
    return properties


def create_render_model_space_ext(
    session: Session,
    create_info: RenderModelSpaceCreateInfoEXT = None,
) -> Space:
    if create_info is None:
        create_info = RenderModelSpaceCreateInfoEXT()
    space = Space()
    space.instance = session.instance
    space._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateRenderModelSpaceEXT"),
        PFN_xrCreateRenderModelSpaceEXT,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(space),
    ))
    if result.is_exception():
        raise result
    return space


def create_render_model_asset_ext(
    session: Session,
    create_info: RenderModelAssetCreateInfoEXT = None,
) -> RenderModelAssetEXT:
    if create_info is None:
        create_info = RenderModelAssetCreateInfoEXT()
    asset = RenderModelAssetEXT()
    asset.instance = session.instance
    asset._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateRenderModelAssetEXT"),
        PFN_xrCreateRenderModelAssetEXT,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(asset),
    ))
    if result.is_exception():
        raise result
    return asset


def destroy_render_model_asset_ext(
    asset: RenderModelAssetEXT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(asset.instance, "xrDestroyRenderModelAssetEXT"),
        PFN_xrDestroyRenderModelAssetEXT,
    )
    result = check_result(fxn(
        asset,
    ))
    if result.is_exception():
        raise result


def get_render_model_asset_data_ext(
    asset: RenderModelAssetEXT,
    get_info: RenderModelAssetDataGetInfoEXT = None,
) -> RenderModelAssetDataEXT:
    buffer = RenderModelAssetDataEXT()
    fxn = cast(
        get_instance_proc_addr(asset.instance, "xrGetRenderModelAssetDataEXT"),
        PFN_xrGetRenderModelAssetDataEXT,
    )
    result = check_result(fxn(
        asset,
        get_info,
        byref(buffer),
    ))
    if result.is_exception():
        raise result
    return buffer


def get_render_model_asset_properties_ext(
    asset: RenderModelAssetEXT,
    get_info: RenderModelAssetPropertiesGetInfoEXT = None,
) -> RenderModelAssetPropertiesEXT:
    properties = RenderModelAssetPropertiesEXT()
    fxn = cast(
        get_instance_proc_addr(asset.instance, "xrGetRenderModelAssetPropertiesEXT"),
        PFN_xrGetRenderModelAssetPropertiesEXT,
    )
    result = check_result(fxn(
        asset,
        get_info,
        byref(properties),
    ))
    if result.is_exception():
        raise result
    return properties


def get_render_model_state_ext(
    render_model: RenderModelEXT,
    get_info: RenderModelStateGetInfoEXT,
) -> RenderModelStateEXT:
    state = RenderModelStateEXT()
    fxn = cast(
        get_instance_proc_addr(render_model.instance, "xrGetRenderModelStateEXT"),
        PFN_xrGetRenderModelStateEXT,
    )
    result = check_result(fxn(
        render_model,
        get_info,
        byref(state),
    ))
    if result.is_exception():
        raise result
    return state


def enumerate_interaction_render_model_ids_ext(
    session: Session,
    get_info: InteractionRenderModelIdsEnumerateInfoEXT,
) -> Sequence[RenderModelIdEXT]:
    render_model_id_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrEnumerateInteractionRenderModelIdsEXT"),
        PFN_xrEnumerateInteractionRenderModelIdsEXT,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        session,
        get_info,
        0,
        byref(render_model_id_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    render_model_ids = (RenderModelIdEXT * render_model_id_capacity_input.value)(*([RenderModelIdEXT()] * render_model_id_capacity_input.value))  # noqa
    result = check_result(fxn(
        session,
        get_info,
        render_model_id_capacity_input,
        byref(render_model_id_capacity_input),
        render_model_ids,
    ))
    if result.is_exception():
        raise result
    return render_model_ids  # noqa


def enumerate_render_model_subaction_paths_ext(
    render_model: RenderModelEXT,
    info: InteractionRenderModelSubactionPathInfoEXT = None,
) -> Sequence[Path]:
    path_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(render_model.instance, "xrEnumerateRenderModelSubactionPathsEXT"),
        PFN_xrEnumerateRenderModelSubactionPathsEXT,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        render_model,
        info,
        0,
        byref(path_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    paths = (Path * path_capacity_input.value)(*([Path()] * path_capacity_input.value))  # noqa
    result = check_result(fxn(
        render_model,
        info,
        path_capacity_input,
        byref(path_capacity_input),
        paths,
    ))
    if result.is_exception():
        raise result
    return paths  # noqa


def get_render_model_pose_top_level_user_path_ext(
    render_model: RenderModelEXT,
    info: InteractionRenderModelTopLevelUserPathGetInfoEXT,
) -> Path:
    top_level_user_path = Path()
    fxn = cast(
        get_instance_proc_addr(render_model.instance, "xrGetRenderModelPoseTopLevelUserPathEXT"),
        PFN_xrGetRenderModelPoseTopLevelUserPathEXT,
    )
    result = check_result(fxn(
        render_model,
        info,
        byref(top_level_user_path),
    ))
    if result.is_exception():
        raise result
    return top_level_user_path


def set_tracking_optimization_settings_hint_qcom(
    session: Session,
    domain: TrackingOptimizationSettingsDomainQCOM,
    hint: TrackingOptimizationSettingsHintQCOM,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrSetTrackingOptimizationSettingsHintQCOM"),
        PFN_xrSetTrackingOptimizationSettingsHintQCOM,
    )
    result = check_result(fxn(
        session,
        domain.value,
        hint.value,
    ))
    if result.is_exception():
        raise result


def create_passthrough_htc(
    session: Session,
    create_info: PassthroughCreateInfoHTC = None,
) -> PassthroughHTC:
    if create_info is None:
        create_info = PassthroughCreateInfoHTC()
    passthrough = PassthroughHTC()
    passthrough.instance = session.instance
    passthrough._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreatePassthroughHTC"),
        PFN_xrCreatePassthroughHTC,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(passthrough),
    ))
    if result.is_exception():
        raise result
    return passthrough


def destroy_passthrough_htc(
    passthrough: PassthroughHTC,
) -> None:
    fxn = cast(
        get_instance_proc_addr(passthrough.instance, "xrDestroyPassthroughHTC"),
        PFN_xrDestroyPassthroughHTC,
    )
    result = check_result(fxn(
        passthrough,
    ))
    if result.is_exception():
        raise result


def apply_foveation_htc(
    session: Session,
    apply_info: FoveationApplyInfoHTC,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrApplyFoveationHTC"),
        PFN_xrApplyFoveationHTC,
    )
    result = check_result(fxn(
        session,
        apply_info,
    ))
    if result.is_exception():
        raise result


def create_spatial_anchor_htc(
    session: Session,
    create_info: SpatialAnchorCreateInfoHTC = None,
) -> Space:
    if create_info is None:
        create_info = SpatialAnchorCreateInfoHTC()
    anchor = Space()
    anchor.instance = session.instance
    anchor._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateSpatialAnchorHTC"),
        PFN_xrCreateSpatialAnchorHTC,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(anchor),
    ))
    if result.is_exception():
        raise result
    return anchor


def get_spatial_anchor_name_htc(
    anchor: Space,
) -> SpatialAnchorNameHTC:
    name = SpatialAnchorNameHTC()
    fxn = cast(
        get_instance_proc_addr(anchor.instance, "xrGetSpatialAnchorNameHTC"),
        PFN_xrGetSpatialAnchorNameHTC,
    )
    result = check_result(fxn(
        anchor,
        byref(name),
    ))
    if result.is_exception():
        raise result
    return name


def create_body_tracker_htc(
    session: Session,
    create_info: BodyTrackerCreateInfoHTC = None,
) -> BodyTrackerHTC:
    if create_info is None:
        create_info = BodyTrackerCreateInfoHTC()
    body_tracker = BodyTrackerHTC()
    body_tracker.instance = session.instance
    body_tracker._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateBodyTrackerHTC"),
        PFN_xrCreateBodyTrackerHTC,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(body_tracker),
    ))
    if result.is_exception():
        raise result
    return body_tracker


def destroy_body_tracker_htc(
    body_tracker: BodyTrackerHTC,
) -> None:
    fxn = cast(
        get_instance_proc_addr(body_tracker.instance, "xrDestroyBodyTrackerHTC"),
        PFN_xrDestroyBodyTrackerHTC,
    )
    result = check_result(fxn(
        body_tracker,
    ))
    if result.is_exception():
        raise result


def locate_body_joints_htc(
    body_tracker: BodyTrackerHTC,
    locate_info: BodyJointsLocateInfoHTC,
) -> BodyJointLocationsHTC:
    locations = BodyJointLocationsHTC()
    fxn = cast(
        get_instance_proc_addr(body_tracker.instance, "xrLocateBodyJointsHTC"),
        PFN_xrLocateBodyJointsHTC,
    )
    result = check_result(fxn(
        body_tracker,
        locate_info,
        byref(locations),
    ))
    if result.is_exception():
        raise result
    return locations


def get_body_skeleton_htc(
    body_tracker: BodyTrackerHTC,
    base_space: Space,
    skeleton_generation_id: int,
) -> BodySkeletonHTC:
    skeleton = BodySkeletonHTC()
    fxn = cast(
        get_instance_proc_addr(body_tracker.instance, "xrGetBodySkeletonHTC"),
        PFN_xrGetBodySkeletonHTC,
    )
    result = check_result(fxn(
        body_tracker,
        base_space,
        skeleton_generation_id,
        byref(skeleton),
    ))
    if result.is_exception():
        raise result
    return skeleton


def apply_force_feedback_curl_mndx(
    hand_tracker: HandTrackerEXT,
    locations: ForceFeedbackCurlApplyLocationsMNDX,
) -> None:
    fxn = cast(
        get_instance_proc_addr(hand_tracker.instance, "xrApplyForceFeedbackCurlMNDX"),
        PFN_xrApplyForceFeedbackCurlMNDX,
    )
    result = check_result(fxn(
        hand_tracker,
        locations,
    ))
    if result.is_exception():
        raise result


def create_body_tracker_bd(
    session: Session,
    create_info: BodyTrackerCreateInfoBD = None,
) -> BodyTrackerBD:
    if create_info is None:
        create_info = BodyTrackerCreateInfoBD()
    body_tracker = BodyTrackerBD()
    body_tracker.instance = session.instance
    body_tracker._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateBodyTrackerBD"),
        PFN_xrCreateBodyTrackerBD,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(body_tracker),
    ))
    if result.is_exception():
        raise result
    return body_tracker


def destroy_body_tracker_bd(
    body_tracker: BodyTrackerBD,
) -> None:
    fxn = cast(
        get_instance_proc_addr(body_tracker.instance, "xrDestroyBodyTrackerBD"),
        PFN_xrDestroyBodyTrackerBD,
    )
    result = check_result(fxn(
        body_tracker,
    ))
    if result.is_exception():
        raise result


def locate_body_joints_bd(
    body_tracker: BodyTrackerBD,
    locate_info: BodyJointsLocateInfoBD,
) -> BodyJointLocationsBD:
    locations = BodyJointLocationsBD()
    fxn = cast(
        get_instance_proc_addr(body_tracker.instance, "xrLocateBodyJointsBD"),
        PFN_xrLocateBodyJointsBD,
    )
    result = check_result(fxn(
        body_tracker,
        locate_info,
        byref(locations),
    ))
    if result.is_exception():
        raise result
    return locations


def enumerate_facial_simulation_modes_bd(
    session: Session,
) -> Sequence[FacialSimulationModeBD]:
    mode_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrEnumerateFacialSimulationModesBD"),
        PFN_xrEnumerateFacialSimulationModesBD,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        session,
        0,
        byref(mode_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    modes = (FacialSimulationModeBD.ctype() * mode_capacity_input.value)(*([FacialSimulationModeBD.ctype()()] * mode_capacity_input.value))  # noqa
    result = check_result(fxn(
        session,
        mode_capacity_input,
        byref(mode_capacity_input),
        modes,
    ))
    if result.is_exception():
        raise result
    return modes  # noqa


def create_face_tracker_bd(
    session: Session,
    create_info: FaceTrackerCreateInfoBD = None,
) -> FaceTrackerBD:
    if create_info is None:
        create_info = FaceTrackerCreateInfoBD()
    tracker = FaceTrackerBD()
    tracker.instance = session.instance
    tracker._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateFaceTrackerBD"),
        PFN_xrCreateFaceTrackerBD,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(tracker),
    ))
    if result.is_exception():
        raise result
    return tracker


def destroy_face_tracker_bd(
    tracker: FaceTrackerBD,
) -> None:
    fxn = cast(
        get_instance_proc_addr(tracker.instance, "xrDestroyFaceTrackerBD"),
        PFN_xrDestroyFaceTrackerBD,
    )
    result = check_result(fxn(
        tracker,
    ))
    if result.is_exception():
        raise result


def get_facial_simulation_data_bd(
    tracker: FaceTrackerBD,
    info: FacialSimulationDataGetInfoBD,
) -> FacialSimulationDataBD:
    facial_data = FacialSimulationDataBD()
    fxn = cast(
        get_instance_proc_addr(tracker.instance, "xrGetFacialSimulationDataBD"),
        PFN_xrGetFacialSimulationDataBD,
    )
    result = check_result(fxn(
        tracker,
        info,
        byref(facial_data),
    ))
    if result.is_exception():
        raise result
    return facial_data


def set_facial_simulation_mode_bd(
    tracker: FaceTrackerBD,
    mode: FacialSimulationModeBD,
) -> None:
    fxn = cast(
        get_instance_proc_addr(tracker.instance, "xrSetFacialSimulationModeBD"),
        PFN_xrSetFacialSimulationModeBD,
    )
    result = check_result(fxn(
        tracker,
        mode.value,
    ))
    if result.is_exception():
        raise result


def get_facial_simulation_mode_bd(
    tracker: FaceTrackerBD,
) -> FacialSimulationModeBD:
    mode = FacialSimulationModeBD.ctype()()
    fxn = cast(
        get_instance_proc_addr(tracker.instance, "xrGetFacialSimulationModeBD"),
        PFN_xrGetFacialSimulationModeBD,
    )
    result = check_result(fxn(
        tracker,
        byref(mode),
    ))
    if result.is_exception():
        raise result
    return mode


def enumerate_spatial_entity_component_types_bd(
    snapshot: SenseDataSnapshotBD,
    entity_id: SpatialEntityIdBD,
) -> Sequence[SpatialEntityComponentTypeBD]:
    component_type_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(snapshot.instance, "xrEnumerateSpatialEntityComponentTypesBD"),
        PFN_xrEnumerateSpatialEntityComponentTypesBD,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        snapshot,
        entity_id,
        0,
        byref(component_type_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    component_types = (SpatialEntityComponentTypeBD.ctype() * component_type_capacity_input.value)(*([SpatialEntityComponentTypeBD.ctype()()] * component_type_capacity_input.value))  # noqa
    result = check_result(fxn(
        snapshot,
        entity_id,
        component_type_capacity_input,
        byref(component_type_capacity_input),
        component_types,
    ))
    if result.is_exception():
        raise result
    return component_types  # noqa


def get_spatial_entity_uuid_bd(
    snapshot: SenseDataSnapshotBD,
    entity_id: SpatialEntityIdBD,
) -> UuidEXT:
    uuid = UuidEXT()
    fxn = cast(
        get_instance_proc_addr(snapshot.instance, "xrGetSpatialEntityUuidBD"),
        PFN_xrGetSpatialEntityUuidBD,
    )
    result = check_result(fxn(
        snapshot,
        entity_id,
        byref(uuid),
    ))
    if result.is_exception():
        raise result
    return uuid


def get_spatial_entity_component_data_bd(
    snapshot: SenseDataSnapshotBD,
    get_info: SpatialEntityComponentGetInfoBD,
) -> SpatialEntityComponentDataBaseHeaderBD:
    component_data = SpatialEntityComponentDataBaseHeaderBD()
    fxn = cast(
        get_instance_proc_addr(snapshot.instance, "xrGetSpatialEntityComponentDataBD"),
        PFN_xrGetSpatialEntityComponentDataBD,
    )
    result = check_result(fxn(
        snapshot,
        get_info,
        cast(byref(component_data), POINTER(SpatialEntityComponentDataBaseHeaderBD)),
    ))
    if result.is_exception():
        raise result
    return component_data


def create_sense_data_provider_bd(
    session: Session,
    create_info: SenseDataProviderCreateInfoBD = None,
) -> SenseDataProviderBD:
    if create_info is None:
        create_info = SenseDataProviderCreateInfoBD()
    provider = SenseDataProviderBD()
    provider.instance = session.instance
    provider._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateSenseDataProviderBD"),
        PFN_xrCreateSenseDataProviderBD,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(provider),
    ))
    if result.is_exception():
        raise result
    return provider


def start_sense_data_provider_async_bd(
    provider: SenseDataProviderBD,
    start_info: SenseDataProviderStartInfoBD,
) -> FutureEXT:
    future = FutureEXT()
    fxn = cast(
        get_instance_proc_addr(provider.instance, "xrStartSenseDataProviderAsyncBD"),
        PFN_xrStartSenseDataProviderAsyncBD,
    )
    result = check_result(fxn(
        provider,
        start_info,
        byref(future),
    ))
    if result.is_exception():
        raise result
    return future


def start_sense_data_provider_complete_bd(
    session: Session,
    future: FutureEXT,
) -> FutureCompletionEXT:
    completion = FutureCompletionEXT()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrStartSenseDataProviderCompleteBD"),
        PFN_xrStartSenseDataProviderCompleteBD,
    )
    result = check_result(fxn(
        session,
        future,
        byref(completion),
    ))
    if result.is_exception():
        raise result
    return completion


def get_sense_data_provider_state_bd(
    provider: SenseDataProviderBD,
) -> SenseDataProviderStateBD:
    state = SenseDataProviderStateBD.ctype()()
    fxn = cast(
        get_instance_proc_addr(provider.instance, "xrGetSenseDataProviderStateBD"),
        PFN_xrGetSenseDataProviderStateBD,
    )
    result = check_result(fxn(
        provider,
        byref(state),
    ))
    if result.is_exception():
        raise result
    return state


def query_sense_data_async_bd(
    provider: SenseDataProviderBD,
    query_info: SenseDataQueryInfoBD,
) -> FutureEXT:
    future = FutureEXT()
    fxn = cast(
        get_instance_proc_addr(provider.instance, "xrQuerySenseDataAsyncBD"),
        PFN_xrQuerySenseDataAsyncBD,
    )
    result = check_result(fxn(
        provider,
        query_info,
        byref(future),
    ))
    if result.is_exception():
        raise result
    return future


def query_sense_data_complete_bd(
    provider: SenseDataProviderBD,
    future: FutureEXT,
) -> SenseDataQueryCompletionBD:
    completion = SenseDataQueryCompletionBD()
    fxn = cast(
        get_instance_proc_addr(provider.instance, "xrQuerySenseDataCompleteBD"),
        PFN_xrQuerySenseDataCompleteBD,
    )
    result = check_result(fxn(
        provider,
        future,
        byref(completion),
    ))
    if result.is_exception():
        raise result
    return completion


def destroy_sense_data_snapshot_bd(
    snapshot: SenseDataSnapshotBD,
) -> None:
    fxn = cast(
        get_instance_proc_addr(snapshot.instance, "xrDestroySenseDataSnapshotBD"),
        PFN_xrDestroySenseDataSnapshotBD,
    )
    result = check_result(fxn(
        snapshot,
    ))
    if result.is_exception():
        raise result


def get_queried_sense_data_bd(
    snapshot: SenseDataSnapshotBD,
) -> (QueriedSenseDataGetInfoBD, QueriedSenseDataBD):
    get_info = QueriedSenseDataGetInfoBD()
    queried_sense_data = QueriedSenseDataBD()
    fxn = cast(
        get_instance_proc_addr(snapshot.instance, "xrGetQueriedSenseDataBD"),
        PFN_xrGetQueriedSenseDataBD,
    )
    result = check_result(fxn(
        snapshot,
        byref(get_info),
        byref(queried_sense_data),
    ))
    if result.is_exception():
        raise result
    return get_info, queried_sense_data


def stop_sense_data_provider_bd(
    provider: SenseDataProviderBD,
) -> None:
    fxn = cast(
        get_instance_proc_addr(provider.instance, "xrStopSenseDataProviderBD"),
        PFN_xrStopSenseDataProviderBD,
    )
    result = check_result(fxn(
        provider,
    ))
    if result.is_exception():
        raise result


def destroy_sense_data_provider_bd(
    provider: SenseDataProviderBD,
) -> None:
    fxn = cast(
        get_instance_proc_addr(provider.instance, "xrDestroySenseDataProviderBD"),
        PFN_xrDestroySenseDataProviderBD,
    )
    result = check_result(fxn(
        provider,
    ))
    if result.is_exception():
        raise result


def create_spatial_entity_anchor_bd(
    provider: SenseDataProviderBD,
    create_info: SpatialEntityAnchorCreateInfoBD = None,
) -> AnchorBD:
    if create_info is None:
        create_info = SpatialEntityAnchorCreateInfoBD()
    anchor = AnchorBD()
    anchor.instance = provider.instance
    anchor._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(provider.instance, "xrCreateSpatialEntityAnchorBD"),
        PFN_xrCreateSpatialEntityAnchorBD,
    )
    result = check_result(fxn(
        provider,
        create_info,
        byref(anchor),
    ))
    if result.is_exception():
        raise result
    return anchor


def destroy_anchor_bd(
    anchor: AnchorBD,
) -> None:
    fxn = cast(
        get_instance_proc_addr(anchor.instance, "xrDestroyAnchorBD"),
        PFN_xrDestroyAnchorBD,
    )
    result = check_result(fxn(
        anchor,
    ))
    if result.is_exception():
        raise result


def get_anchor_uuid_bd(
    anchor: AnchorBD,
) -> UuidEXT:
    uuid = UuidEXT()
    fxn = cast(
        get_instance_proc_addr(anchor.instance, "xrGetAnchorUuidBD"),
        PFN_xrGetAnchorUuidBD,
    )
    result = check_result(fxn(
        anchor,
        byref(uuid),
    ))
    if result.is_exception():
        raise result
    return uuid


def create_anchor_space_bd(
    session: Session,
    create_info: AnchorSpaceCreateInfoBD = None,
) -> Space:
    if create_info is None:
        create_info = AnchorSpaceCreateInfoBD()
    space = Space()
    space.instance = session.instance
    space._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateAnchorSpaceBD"),
        PFN_xrCreateAnchorSpaceBD,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(space),
    ))
    if result.is_exception():
        raise result
    return space


def create_spatial_anchor_async_bd(
    provider: SenseDataProviderBD,
    info: SpatialAnchorCreateInfoBD,
) -> FutureEXT:
    future = FutureEXT()
    future.instance = provider.instance
    future._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(provider.instance, "xrCreateSpatialAnchorAsyncBD"),
        PFN_xrCreateSpatialAnchorAsyncBD,
    )
    result = check_result(fxn(
        provider,
        info,
        byref(future),
    ))
    if result.is_exception():
        raise result
    return future


def create_spatial_anchor_complete_bd(
    provider: SenseDataProviderBD,
    future: FutureEXT,
) -> SpatialAnchorCreateCompletionBD:
    completion = SpatialAnchorCreateCompletionBD()
    fxn = cast(
        get_instance_proc_addr(provider.instance, "xrCreateSpatialAnchorCompleteBD"),
        PFN_xrCreateSpatialAnchorCompleteBD,
    )
    result = check_result(fxn(
        provider,
        future,
        byref(completion),
    ))
    if result.is_exception():
        raise result
    return completion


def persist_spatial_anchor_async_bd(
    provider: SenseDataProviderBD,
    info: SpatialAnchorPersistInfoBD,
) -> FutureEXT:
    future = FutureEXT()
    fxn = cast(
        get_instance_proc_addr(provider.instance, "xrPersistSpatialAnchorAsyncBD"),
        PFN_xrPersistSpatialAnchorAsyncBD,
    )
    result = check_result(fxn(
        provider,
        info,
        byref(future),
    ))
    if result.is_exception():
        raise result
    return future


def persist_spatial_anchor_complete_bd(
    provider: SenseDataProviderBD,
    future: FutureEXT,
) -> FutureCompletionEXT:
    completion = FutureCompletionEXT()
    fxn = cast(
        get_instance_proc_addr(provider.instance, "xrPersistSpatialAnchorCompleteBD"),
        PFN_xrPersistSpatialAnchorCompleteBD,
    )
    result = check_result(fxn(
        provider,
        future,
        byref(completion),
    ))
    if result.is_exception():
        raise result
    return completion


def unpersist_spatial_anchor_async_bd(
    provider: SenseDataProviderBD,
    info: SpatialAnchorUnpersistInfoBD,
) -> FutureEXT:
    future = FutureEXT()
    fxn = cast(
        get_instance_proc_addr(provider.instance, "xrUnpersistSpatialAnchorAsyncBD"),
        PFN_xrUnpersistSpatialAnchorAsyncBD,
    )
    result = check_result(fxn(
        provider,
        info,
        byref(future),
    ))
    if result.is_exception():
        raise result
    return future


def unpersist_spatial_anchor_complete_bd(
    provider: SenseDataProviderBD,
    future: FutureEXT,
) -> FutureCompletionEXT:
    completion = FutureCompletionEXT()
    fxn = cast(
        get_instance_proc_addr(provider.instance, "xrUnpersistSpatialAnchorCompleteBD"),
        PFN_xrUnpersistSpatialAnchorCompleteBD,
    )
    result = check_result(fxn(
        provider,
        future,
        byref(completion),
    ))
    if result.is_exception():
        raise result
    return completion


def share_spatial_anchor_async_bd(
    provider: SenseDataProviderBD,
    info: SpatialAnchorShareInfoBD,
) -> FutureEXT:
    future = FutureEXT()
    fxn = cast(
        get_instance_proc_addr(provider.instance, "xrShareSpatialAnchorAsyncBD"),
        PFN_xrShareSpatialAnchorAsyncBD,
    )
    result = check_result(fxn(
        provider,
        info,
        byref(future),
    ))
    if result.is_exception():
        raise result
    return future


def share_spatial_anchor_complete_bd(
    provider: SenseDataProviderBD,
    future: FutureEXT,
) -> FutureCompletionEXT:
    completion = FutureCompletionEXT()
    fxn = cast(
        get_instance_proc_addr(provider.instance, "xrShareSpatialAnchorCompleteBD"),
        PFN_xrShareSpatialAnchorCompleteBD,
    )
    result = check_result(fxn(
        provider,
        future,
        byref(completion),
    ))
    if result.is_exception():
        raise result
    return completion


def download_shared_spatial_anchor_async_bd(
    provider: SenseDataProviderBD,
    info: SharedSpatialAnchorDownloadInfoBD,
) -> FutureEXT:
    future = FutureEXT()
    fxn = cast(
        get_instance_proc_addr(provider.instance, "xrDownloadSharedSpatialAnchorAsyncBD"),
        PFN_xrDownloadSharedSpatialAnchorAsyncBD,
    )
    result = check_result(fxn(
        provider,
        info,
        byref(future),
    ))
    if result.is_exception():
        raise result
    return future


def download_shared_spatial_anchor_complete_bd(
    provider: SenseDataProviderBD,
    future: FutureEXT,
) -> FutureCompletionEXT:
    completion = FutureCompletionEXT()
    fxn = cast(
        get_instance_proc_addr(provider.instance, "xrDownloadSharedSpatialAnchorCompleteBD"),
        PFN_xrDownloadSharedSpatialAnchorCompleteBD,
    )
    result = check_result(fxn(
        provider,
        future,
        byref(completion),
    ))
    if result.is_exception():
        raise result
    return completion


def capture_scene_async_bd(
    provider: SenseDataProviderBD,
    info: SceneCaptureInfoBD,
) -> FutureEXT:
    future = FutureEXT()
    fxn = cast(
        get_instance_proc_addr(provider.instance, "xrCaptureSceneAsyncBD"),
        PFN_xrCaptureSceneAsyncBD,
    )
    result = check_result(fxn(
        provider,
        info,
        byref(future),
    ))
    if result.is_exception():
        raise result
    return future


def capture_scene_complete_bd(
    provider: SenseDataProviderBD,
    future: FutureEXT,
) -> FutureCompletionEXT:
    completion = FutureCompletionEXT()
    fxn = cast(
        get_instance_proc_addr(provider.instance, "xrCaptureSceneCompleteBD"),
        PFN_xrCaptureSceneCompleteBD,
    )
    result = check_result(fxn(
        provider,
        future,
        byref(completion),
    ))
    if result.is_exception():
        raise result
    return completion


def create_plane_detector_ext(
    session: Session,
    create_info: PlaneDetectorCreateInfoEXT = None,
) -> PlaneDetectorEXT:
    if create_info is None:
        create_info = PlaneDetectorCreateInfoEXT()
    plane_detector = PlaneDetectorEXT()
    plane_detector.instance = session.instance
    plane_detector._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreatePlaneDetectorEXT"),
        PFN_xrCreatePlaneDetectorEXT,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(plane_detector),
    ))
    if result.is_exception():
        raise result
    return plane_detector


def destroy_plane_detector_ext(
    plane_detector: PlaneDetectorEXT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(plane_detector.instance, "xrDestroyPlaneDetectorEXT"),
        PFN_xrDestroyPlaneDetectorEXT,
    )
    result = check_result(fxn(
        plane_detector,
    ))
    if result.is_exception():
        raise result


def begin_plane_detection_ext(
    plane_detector: PlaneDetectorEXT,
    begin_info: PlaneDetectorBeginInfoEXT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(plane_detector.instance, "xrBeginPlaneDetectionEXT"),
        PFN_xrBeginPlaneDetectionEXT,
    )
    result = check_result(fxn(
        plane_detector,
        begin_info,
    ))
    if result.is_exception():
        raise result


def get_plane_detection_state_ext(
    plane_detector: PlaneDetectorEXT,
) -> PlaneDetectionStateEXT:
    state = PlaneDetectionStateEXT.ctype()()
    fxn = cast(
        get_instance_proc_addr(plane_detector.instance, "xrGetPlaneDetectionStateEXT"),
        PFN_xrGetPlaneDetectionStateEXT,
    )
    result = check_result(fxn(
        plane_detector,
        byref(state),
    ))
    if result.is_exception():
        raise result
    return state


def get_plane_detections_ext(
    plane_detector: PlaneDetectorEXT,
    info: PlaneDetectorGetInfoEXT,
) -> PlaneDetectorLocationsEXT:
    locations = PlaneDetectorLocationsEXT()
    fxn = cast(
        get_instance_proc_addr(plane_detector.instance, "xrGetPlaneDetectionsEXT"),
        PFN_xrGetPlaneDetectionsEXT,
    )
    result = check_result(fxn(
        plane_detector,
        info,
        byref(locations),
    ))
    if result.is_exception():
        raise result
    return locations


def get_plane_polygon_buffer_ext(
    plane_detector: PlaneDetectorEXT,
    plane_id: int,
    polygon_buffer_index: int,
) -> PlaneDetectorPolygonBufferEXT:
    polygon_buffer = PlaneDetectorPolygonBufferEXT()
    fxn = cast(
        get_instance_proc_addr(plane_detector.instance, "xrGetPlanePolygonBufferEXT"),
        PFN_xrGetPlanePolygonBufferEXT,
    )
    result = check_result(fxn(
        plane_detector,
        plane_id,
        polygon_buffer_index,
        byref(polygon_buffer),
    ))
    if result.is_exception():
        raise result
    return polygon_buffer


def enumerate_supported_trackable_types_android(
    instance: Instance,
    system_id: SystemId,
) -> Sequence[TrackableTypeANDROID]:
    trackable_type_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrEnumerateSupportedTrackableTypesANDROID"),
        PFN_xrEnumerateSupportedTrackableTypesANDROID,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        instance,
        system_id,
        0,
        byref(trackable_type_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    trackable_types = (TrackableTypeANDROID.ctype() * trackable_type_capacity_input.value)(*([TrackableTypeANDROID.ctype()()] * trackable_type_capacity_input.value))  # noqa
    result = check_result(fxn(
        instance,
        system_id,
        trackable_type_capacity_input,
        byref(trackable_type_capacity_input),
        trackable_types,
    ))
    if result.is_exception():
        raise result
    return trackable_types  # noqa


def enumerate_supported_anchor_trackable_types_android(
    instance: Instance,
    system_id: SystemId,
) -> Sequence[TrackableTypeANDROID]:
    trackable_type_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrEnumerateSupportedAnchorTrackableTypesANDROID"),
        PFN_xrEnumerateSupportedAnchorTrackableTypesANDROID,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        instance,
        system_id,
        0,
        byref(trackable_type_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    trackable_types = (TrackableTypeANDROID.ctype() * trackable_type_capacity_input.value)(*([TrackableTypeANDROID.ctype()()] * trackable_type_capacity_input.value))  # noqa
    result = check_result(fxn(
        instance,
        system_id,
        trackable_type_capacity_input,
        byref(trackable_type_capacity_input),
        trackable_types,
    ))
    if result.is_exception():
        raise result
    return trackable_types  # noqa


def create_trackable_tracker_android(
    session: Session,
    create_info: TrackableTrackerCreateInfoANDROID = None,
) -> TrackableTrackerANDROID:
    if create_info is None:
        create_info = TrackableTrackerCreateInfoANDROID()
    trackable_tracker = TrackableTrackerANDROID()
    trackable_tracker.instance = session.instance
    trackable_tracker._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateTrackableTrackerANDROID"),
        PFN_xrCreateTrackableTrackerANDROID,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(trackable_tracker),
    ))
    if result.is_exception():
        raise result
    return trackable_tracker


def destroy_trackable_tracker_android(
    trackable_tracker: TrackableTrackerANDROID,
) -> None:
    fxn = cast(
        get_instance_proc_addr(trackable_tracker.instance, "xrDestroyTrackableTrackerANDROID"),
        PFN_xrDestroyTrackableTrackerANDROID,
    )
    result = check_result(fxn(
        trackable_tracker,
    ))
    if result.is_exception():
        raise result


def get_all_trackables_android(
    trackable_tracker: TrackableTrackerANDROID,
) -> Sequence[TrackableANDROID]:
    trackable_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(trackable_tracker.instance, "xrGetAllTrackablesANDROID"),
        PFN_xrGetAllTrackablesANDROID,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        trackable_tracker,
        0,
        byref(trackable_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    trackables = (TrackableANDROID * trackable_capacity_input.value)(*([TrackableANDROID()] * trackable_capacity_input.value))  # noqa
    result = check_result(fxn(
        trackable_tracker,
        trackable_capacity_input,
        byref(trackable_capacity_input),
        trackables,
    ))
    if result.is_exception():
        raise result
    return trackables  # noqa


def get_trackable_plane_android(
    trackable_tracker: TrackableTrackerANDROID,
    get_info: TrackableGetInfoANDROID,
) -> TrackablePlaneANDROID:
    plane_output = TrackablePlaneANDROID()
    fxn = cast(
        get_instance_proc_addr(trackable_tracker.instance, "xrGetTrackablePlaneANDROID"),
        PFN_xrGetTrackablePlaneANDROID,
    )
    result = check_result(fxn(
        trackable_tracker,
        get_info,
        byref(plane_output),
    ))
    if result.is_exception():
        raise result
    return plane_output


def create_anchor_space_android(
    session: Session,
    create_info: AnchorSpaceCreateInfoANDROID = None,
) -> Space:
    if create_info is None:
        create_info = AnchorSpaceCreateInfoANDROID()
    anchor_output = Space()
    anchor_output.instance = session.instance
    anchor_output._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateAnchorSpaceANDROID"),
        PFN_xrCreateAnchorSpaceANDROID,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(anchor_output),
    ))
    if result.is_exception():
        raise result
    return anchor_output


def enumerate_supported_persistence_anchor_types_android(
    instance: Instance,
    system_id: SystemId,
) -> Sequence[TrackableTypeANDROID]:
    trackable_type_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrEnumerateSupportedPersistenceAnchorTypesANDROID"),
        PFN_xrEnumerateSupportedPersistenceAnchorTypesANDROID,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        instance,
        system_id,
        0,
        byref(trackable_type_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    trackable_types = (TrackableTypeANDROID.ctype() * trackable_type_capacity_input.value)(*([TrackableTypeANDROID.ctype()()] * trackable_type_capacity_input.value))  # noqa
    result = check_result(fxn(
        instance,
        system_id,
        trackable_type_capacity_input,
        byref(trackable_type_capacity_input),
        trackable_types,
    ))
    if result.is_exception():
        raise result
    return trackable_types  # noqa


def create_device_anchor_persistence_android(
    session: Session,
    create_info: DeviceAnchorPersistenceCreateInfoANDROID = None,
) -> DeviceAnchorPersistenceANDROID:
    if create_info is None:
        create_info = DeviceAnchorPersistenceCreateInfoANDROID()
    out_handle = DeviceAnchorPersistenceANDROID()
    out_handle.instance = session.instance
    out_handle._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateDeviceAnchorPersistenceANDROID"),
        PFN_xrCreateDeviceAnchorPersistenceANDROID,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(out_handle),
    ))
    if result.is_exception():
        raise result
    return out_handle


def destroy_device_anchor_persistence_android(
    handle: DeviceAnchorPersistenceANDROID,
) -> None:
    fxn = cast(
        get_instance_proc_addr(handle.instance, "xrDestroyDeviceAnchorPersistenceANDROID"),
        PFN_xrDestroyDeviceAnchorPersistenceANDROID,
    )
    result = check_result(fxn(
        handle,
    ))
    if result.is_exception():
        raise result


def persist_anchor_android(
    handle: DeviceAnchorPersistenceANDROID,
    persisted_info: PersistedAnchorSpaceInfoANDROID,
) -> UuidEXT:
    anchor_id_output = UuidEXT()
    fxn = cast(
        get_instance_proc_addr(handle.instance, "xrPersistAnchorANDROID"),
        PFN_xrPersistAnchorANDROID,
    )
    result = check_result(fxn(
        handle,
        persisted_info,
        byref(anchor_id_output),
    ))
    if result.is_exception():
        raise result
    return anchor_id_output


def get_anchor_persist_state_android(
    handle: DeviceAnchorPersistenceANDROID,
    anchor_id: POINTER(Uuid),
) -> AnchorPersistStateANDROID:
    persist_state = AnchorPersistStateANDROID.ctype()()
    fxn = cast(
        get_instance_proc_addr(handle.instance, "xrGetAnchorPersistStateANDROID"),
        PFN_xrGetAnchorPersistStateANDROID,
    )
    result = check_result(fxn(
        handle,
        anchor_id,
        byref(persist_state),
    ))
    if result.is_exception():
        raise result
    return persist_state


def create_persisted_anchor_space_android(
    handle: DeviceAnchorPersistenceANDROID,
    create_info: PersistedAnchorSpaceCreateInfoANDROID = None,
) -> Space:
    if create_info is None:
        create_info = PersistedAnchorSpaceCreateInfoANDROID()
    anchor_output = Space()
    anchor_output.instance = handle.instance
    anchor_output._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(handle.instance, "xrCreatePersistedAnchorSpaceANDROID"),
        PFN_xrCreatePersistedAnchorSpaceANDROID,
    )
    result = check_result(fxn(
        handle,
        create_info,
        byref(anchor_output),
    ))
    if result.is_exception():
        raise result
    return anchor_output


def enumerate_persisted_anchors_android(
    handle: DeviceAnchorPersistenceANDROID,
) -> Sequence[UuidEXT]:
    anchor_id_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(handle.instance, "xrEnumeratePersistedAnchorsANDROID"),
        PFN_xrEnumeratePersistedAnchorsANDROID,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        handle,
        0,
        byref(anchor_id_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    anchor_ids = (UuidEXT * anchor_id_capacity_input.value)(*([UuidEXT()] * anchor_id_capacity_input.value))  # noqa
    result = check_result(fxn(
        handle,
        anchor_id_capacity_input,
        byref(anchor_id_capacity_input),
        anchor_ids,
    ))
    if result.is_exception():
        raise result
    return anchor_ids  # noqa


def unpersist_anchor_android(
    handle: DeviceAnchorPersistenceANDROID,
    anchor_id: POINTER(Uuid),
) -> None:
    fxn = cast(
        get_instance_proc_addr(handle.instance, "xrUnpersistAnchorANDROID"),
        PFN_xrUnpersistAnchorANDROID,
    )
    result = check_result(fxn(
        handle,
        anchor_id,
    ))
    if result.is_exception():
        raise result


def create_face_tracker_android(
    session: Session,
    create_info: FaceTrackerCreateInfoANDROID = None,
) -> FaceTrackerANDROID:
    if create_info is None:
        create_info = FaceTrackerCreateInfoANDROID()
    face_tracker = FaceTrackerANDROID()
    face_tracker.instance = session.instance
    face_tracker._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateFaceTrackerANDROID"),
        PFN_xrCreateFaceTrackerANDROID,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(face_tracker),
    ))
    if result.is_exception():
        raise result
    return face_tracker


def destroy_face_tracker_android(
    face_tracker: FaceTrackerANDROID,
) -> None:
    fxn = cast(
        get_instance_proc_addr(face_tracker.instance, "xrDestroyFaceTrackerANDROID"),
        PFN_xrDestroyFaceTrackerANDROID,
    )
    result = check_result(fxn(
        face_tracker,
    ))
    if result.is_exception():
        raise result


def get_face_state_android(
    face_tracker: FaceTrackerANDROID,
    get_info: FaceStateGetInfoANDROID,
) -> FaceStateANDROID:
    face_state_output = FaceStateANDROID()
    fxn = cast(
        get_instance_proc_addr(face_tracker.instance, "xrGetFaceStateANDROID"),
        PFN_xrGetFaceStateANDROID,
    )
    result = check_result(fxn(
        face_tracker,
        get_info,
        byref(face_state_output),
    ))
    if result.is_exception():
        raise result
    return face_state_output


def get_face_calibration_state_android(
    face_tracker: FaceTrackerANDROID,
) -> Bool32:
    face_is_calibrated_output = Bool32()
    fxn = cast(
        get_instance_proc_addr(face_tracker.instance, "xrGetFaceCalibrationStateANDROID"),
        PFN_xrGetFaceCalibrationStateANDROID,
    )
    result = check_result(fxn(
        face_tracker,
        byref(face_is_calibrated_output),
    ))
    if result.is_exception():
        raise result
    return face_is_calibrated_output


def get_passthrough_camera_state_android(
    session: Session,
    get_info: PassthroughCameraStateGetInfoANDROID,
) -> PassthroughCameraStateANDROID:
    camera_state_output = PassthroughCameraStateANDROID.ctype()()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrGetPassthroughCameraStateANDROID"),
        PFN_xrGetPassthroughCameraStateANDROID,
    )
    result = check_result(fxn(
        session,
        get_info,
        byref(camera_state_output),
    ))
    if result.is_exception():
        raise result
    return camera_state_output


def enumerate_raycast_supported_trackable_types_android(
    instance: Instance,
    system_id: SystemId,
) -> Sequence[TrackableTypeANDROID]:
    trackable_type_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrEnumerateRaycastSupportedTrackableTypesANDROID"),
        PFN_xrEnumerateRaycastSupportedTrackableTypesANDROID,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        instance,
        system_id,
        0,
        byref(trackable_type_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    trackable_types = (TrackableTypeANDROID.ctype() * trackable_type_capacity_input.value)(*([TrackableTypeANDROID.ctype()()] * trackable_type_capacity_input.value))  # noqa
    result = check_result(fxn(
        instance,
        system_id,
        trackable_type_capacity_input,
        byref(trackable_type_capacity_input),
        trackable_types,
    ))
    if result.is_exception():
        raise result
    return trackable_types  # noqa


def raycast_android(
    session: Session,
    ray_info: RaycastInfoANDROID,
) -> RaycastHitResultsANDROID:
    results = RaycastHitResultsANDROID()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrRaycastANDROID"),
        PFN_xrRaycastANDROID,
    )
    result = check_result(fxn(
        session,
        ray_info,
        byref(results),
    ))
    if result.is_exception():
        raise result
    return results


def get_trackable_object_android(
    tracker: TrackableTrackerANDROID,
    get_info: TrackableGetInfoANDROID,
) -> TrackableObjectANDROID:
    object_output = TrackableObjectANDROID()
    fxn = cast(
        get_instance_proc_addr(tracker.instance, "xrGetTrackableObjectANDROID"),
        PFN_xrGetTrackableObjectANDROID,
    )
    result = check_result(fxn(
        tracker,
        get_info,
        byref(object_output),
    ))
    if result.is_exception():
        raise result
    return object_output


def poll_future_ext(
    instance: Instance,
    poll_info: FuturePollInfoEXT,
) -> FuturePollResultEXT:
    poll_result = FuturePollResultEXT()
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrPollFutureEXT"),
        PFN_xrPollFutureEXT,
    )
    result = check_result(fxn(
        instance,
        poll_info,
        byref(poll_result),
    ))
    if result.is_exception():
        raise result
    return poll_result


def cancel_future_ext(
    instance: Instance,
    cancel_info: FutureCancelInfoEXT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrCancelFutureEXT"),
        PFN_xrCancelFutureEXT,
    )
    result = check_result(fxn(
        instance,
        cancel_info,
    ))
    if result.is_exception():
        raise result


def enable_user_calibration_events_ml(
    instance: Instance,
    enable_info: UserCalibrationEnableEventsInfoML,
) -> None:
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrEnableUserCalibrationEventsML"),
        PFN_xrEnableUserCalibrationEventsML,
    )
    result = check_result(fxn(
        instance,
        enable_info,
    ))
    if result.is_exception():
        raise result


def set_system_notifications_ml(
    instance: Instance,
    info: SystemNotificationsSetInfoML,
) -> None:
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrSetSystemNotificationsML"),
        PFN_xrSetSystemNotificationsML,
    )
    result = check_result(fxn(
        instance,
        info,
    ))
    if result.is_exception():
        raise result


def create_world_mesh_detector_ml(
    session: Session,
    create_info: WorldMeshDetectorCreateInfoML = None,
) -> WorldMeshDetectorML:
    if create_info is None:
        create_info = WorldMeshDetectorCreateInfoML()
    detector = WorldMeshDetectorML()
    detector.instance = session.instance
    detector._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateWorldMeshDetectorML"),
        PFN_xrCreateWorldMeshDetectorML,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(detector),
    ))
    if result.is_exception():
        raise result
    return detector


def destroy_world_mesh_detector_ml(
    detector: WorldMeshDetectorML,
) -> None:
    fxn = cast(
        get_instance_proc_addr(detector.instance, "xrDestroyWorldMeshDetectorML"),
        PFN_xrDestroyWorldMeshDetectorML,
    )
    result = check_result(fxn(
        detector,
    ))
    if result.is_exception():
        raise result


def request_world_mesh_state_async_ml(
    detector: WorldMeshDetectorML,
    state_request: WorldMeshStateRequestInfoML,
) -> FutureEXT:
    future = FutureEXT()
    fxn = cast(
        get_instance_proc_addr(detector.instance, "xrRequestWorldMeshStateAsyncML"),
        PFN_xrRequestWorldMeshStateAsyncML,
    )
    result = check_result(fxn(
        detector,
        state_request,
        byref(future),
    ))
    if result.is_exception():
        raise result
    return future


def request_world_mesh_state_complete_ml(
    detector: WorldMeshDetectorML,
    future: FutureEXT,
) -> WorldMeshStateRequestCompletionML:
    completion = WorldMeshStateRequestCompletionML()
    fxn = cast(
        get_instance_proc_addr(detector.instance, "xrRequestWorldMeshStateCompleteML"),
        PFN_xrRequestWorldMeshStateCompleteML,
    )
    result = check_result(fxn(
        detector,
        future,
        byref(completion),
    ))
    if result.is_exception():
        raise result
    return completion


def get_world_mesh_buffer_recommend_size_ml(
    detector: WorldMeshDetectorML,
    size_info: WorldMeshBufferRecommendedSizeInfoML,
) -> WorldMeshBufferSizeML:
    size = WorldMeshBufferSizeML()
    fxn = cast(
        get_instance_proc_addr(detector.instance, "xrGetWorldMeshBufferRecommendSizeML"),
        PFN_xrGetWorldMeshBufferRecommendSizeML,
    )
    result = check_result(fxn(
        detector,
        size_info,
        byref(size),
    ))
    if result.is_exception():
        raise result
    return size


def allocate_world_mesh_buffer_ml(
    detector: WorldMeshDetectorML,
    size: WorldMeshBufferSizeML,
) -> WorldMeshBufferML:
    buffer = WorldMeshBufferML()
    fxn = cast(
        get_instance_proc_addr(detector.instance, "xrAllocateWorldMeshBufferML"),
        PFN_xrAllocateWorldMeshBufferML,
    )
    result = check_result(fxn(
        detector,
        size,
        byref(buffer),
    ))
    if result.is_exception():
        raise result
    return buffer


def free_world_mesh_buffer_ml(
    detector: WorldMeshDetectorML,
    buffer: WorldMeshBufferML,
) -> None:
    fxn = cast(
        get_instance_proc_addr(detector.instance, "xrFreeWorldMeshBufferML"),
        PFN_xrFreeWorldMeshBufferML,
    )
    result = check_result(fxn(
        detector,
        buffer,
    ))
    if result.is_exception():
        raise result


def request_world_mesh_async_ml(
    detector: WorldMeshDetectorML,
    get_info: WorldMeshGetInfoML,
) -> (WorldMeshBufferML, FutureEXT):
    buffer = WorldMeshBufferML()
    future = FutureEXT()
    fxn = cast(
        get_instance_proc_addr(detector.instance, "xrRequestWorldMeshAsyncML"),
        PFN_xrRequestWorldMeshAsyncML,
    )
    result = check_result(fxn(
        detector,
        get_info,
        byref(buffer),
        byref(future),
    ))
    if result.is_exception():
        raise result
    return buffer, future


def request_world_mesh_complete_ml(
    detector: WorldMeshDetectorML,
    completion_info: WorldMeshRequestCompletionInfoML,
    future: FutureEXT,
) -> WorldMeshRequestCompletionML:
    completion = WorldMeshRequestCompletionML()
    fxn = cast(
        get_instance_proc_addr(detector.instance, "xrRequestWorldMeshCompleteML"),
        PFN_xrRequestWorldMeshCompleteML,
    )
    result = check_result(fxn(
        detector,
        completion_info,
        future,
        byref(completion),
    ))
    if result.is_exception():
        raise result
    return completion


def create_facial_expression_client_ml(
    session: Session,
    create_info: FacialExpressionClientCreateInfoML = None,
) -> FacialExpressionClientML:
    if create_info is None:
        create_info = FacialExpressionClientCreateInfoML()
    facial_expression_client = FacialExpressionClientML()
    facial_expression_client.instance = session.instance
    facial_expression_client._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateFacialExpressionClientML"),
        PFN_xrCreateFacialExpressionClientML,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(facial_expression_client),
    ))
    if result.is_exception():
        raise result
    return facial_expression_client


def destroy_facial_expression_client_ml(
    facial_expression_client: FacialExpressionClientML,
) -> None:
    fxn = cast(
        get_instance_proc_addr(facial_expression_client.instance, "xrDestroyFacialExpressionClientML"),
        PFN_xrDestroyFacialExpressionClientML,
    )
    result = check_result(fxn(
        facial_expression_client,
    ))
    if result.is_exception():
        raise result


def get_facial_expression_blend_shape_properties_ml(
    facial_expression_client: FacialExpressionClientML,
    blend_shape_get_info: FacialExpressionBlendShapeGetInfoML,
    blend_shape_count: int,
) -> FacialExpressionBlendShapePropertiesML:
    blend_shapes = FacialExpressionBlendShapePropertiesML()
    fxn = cast(
        get_instance_proc_addr(facial_expression_client.instance, "xrGetFacialExpressionBlendShapePropertiesML"),
        PFN_xrGetFacialExpressionBlendShapePropertiesML,
    )
    result = check_result(fxn(
        facial_expression_client,
        blend_shape_get_info,
        blend_shape_count,
        byref(blend_shapes),
    ))
    if result.is_exception():
        raise result
    return blend_shapes


def resume_simultaneous_hands_and_controllers_tracking_meta(
    session: Session,
    resume_info: SimultaneousHandsAndControllersTrackingResumeInfoMETA,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrResumeSimultaneousHandsAndControllersTrackingMETA"),
        PFN_xrResumeSimultaneousHandsAndControllersTrackingMETA,
    )
    result = check_result(fxn(
        session,
        resume_info,
    ))
    if result.is_exception():
        raise result


def pause_simultaneous_hands_and_controllers_tracking_meta(
    session: Session,
    pause_info: SimultaneousHandsAndControllersTrackingPauseInfoMETA,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrPauseSimultaneousHandsAndControllersTrackingMETA"),
        PFN_xrPauseSimultaneousHandsAndControllersTrackingMETA,
    )
    result = check_result(fxn(
        session,
        pause_info,
    ))
    if result.is_exception():
        raise result


def start_colocation_discovery_meta(
    session: Session,
    info: ColocationDiscoveryStartInfoMETA,
) -> AsyncRequestIdFB:
    discovery_request_id = AsyncRequestIdFB()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrStartColocationDiscoveryMETA"),
        PFN_xrStartColocationDiscoveryMETA,
    )
    result = check_result(fxn(
        session,
        info,
        byref(discovery_request_id),
    ))
    if result.is_exception():
        raise result
    return discovery_request_id


def stop_colocation_discovery_meta(
    session: Session,
    info: ColocationDiscoveryStopInfoMETA,
) -> AsyncRequestIdFB:
    request_id = AsyncRequestIdFB()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrStopColocationDiscoveryMETA"),
        PFN_xrStopColocationDiscoveryMETA,
    )
    result = check_result(fxn(
        session,
        info,
        byref(request_id),
    ))
    if result.is_exception():
        raise result
    return request_id


def start_colocation_advertisement_meta(
    session: Session,
    info: ColocationAdvertisementStartInfoMETA,
) -> AsyncRequestIdFB:
    advertisement_request_id = AsyncRequestIdFB()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrStartColocationAdvertisementMETA"),
        PFN_xrStartColocationAdvertisementMETA,
    )
    result = check_result(fxn(
        session,
        info,
        byref(advertisement_request_id),
    ))
    if result.is_exception():
        raise result
    return advertisement_request_id


def stop_colocation_advertisement_meta(
    session: Session,
    info: ColocationAdvertisementStopInfoMETA,
) -> AsyncRequestIdFB:
    request_id = AsyncRequestIdFB()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrStopColocationAdvertisementMETA"),
        PFN_xrStopColocationAdvertisementMETA,
    )
    result = check_result(fxn(
        session,
        info,
        byref(request_id),
    ))
    if result.is_exception():
        raise result
    return request_id


def get_trackable_marker_android(
    tracker: TrackableTrackerANDROID,
    get_info: TrackableGetInfoANDROID,
) -> TrackableMarkerANDROID:
    marker_output = TrackableMarkerANDROID()
    fxn = cast(
        get_instance_proc_addr(tracker.instance, "xrGetTrackableMarkerANDROID"),
        PFN_xrGetTrackableMarkerANDROID,
    )
    result = check_result(fxn(
        tracker,
        get_info,
        byref(marker_output),
    ))
    if result.is_exception():
        raise result
    return marker_output


def enumerate_spatial_capabilities_ext(
    instance: Instance,
    system_id: SystemId,
) -> Sequence[SpatialCapabilityEXT]:
    capability_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrEnumerateSpatialCapabilitiesEXT"),
        PFN_xrEnumerateSpatialCapabilitiesEXT,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        instance,
        system_id,
        0,
        byref(capability_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    capabilities = (SpatialCapabilityEXT.ctype() * capability_capacity_input.value)(*([SpatialCapabilityEXT.ctype()()] * capability_capacity_input.value))  # noqa
    result = check_result(fxn(
        instance,
        system_id,
        capability_capacity_input,
        byref(capability_capacity_input),
        capabilities,
    ))
    if result.is_exception():
        raise result
    return capabilities  # noqa


def enumerate_spatial_capability_component_types_ext(
    instance: Instance,
    system_id: SystemId,
    capability: SpatialCapabilityEXT,
) -> SpatialCapabilityComponentTypesEXT:
    capability_components = SpatialCapabilityComponentTypesEXT()
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrEnumerateSpatialCapabilityComponentTypesEXT"),
        PFN_xrEnumerateSpatialCapabilityComponentTypesEXT,
    )
    result = check_result(fxn(
        instance,
        system_id,
        capability.value,
        byref(capability_components),
    ))
    if result.is_exception():
        raise result
    return capability_components


def enumerate_spatial_capability_features_ext(
    instance: Instance,
    system_id: SystemId,
    capability: SpatialCapabilityEXT,
) -> Sequence[SpatialCapabilityFeatureEXT]:
    capability_feature_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrEnumerateSpatialCapabilityFeaturesEXT"),
        PFN_xrEnumerateSpatialCapabilityFeaturesEXT,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        instance,
        system_id,
        capability.value,
        0,
        byref(capability_feature_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    capability_features = (SpatialCapabilityFeatureEXT.ctype() * capability_feature_capacity_input.value)(*([SpatialCapabilityFeatureEXT.ctype()()] * capability_feature_capacity_input.value))  # noqa
    result = check_result(fxn(
        instance,
        system_id,
        capability.value,
        capability_feature_capacity_input,
        byref(capability_feature_capacity_input),
        capability_features,
    ))
    if result.is_exception():
        raise result
    return capability_features  # noqa


def create_spatial_context_async_ext(
    session: Session,
    create_info: SpatialContextCreateInfoEXT = None,
) -> FutureEXT:
    if create_info is None:
        create_info = SpatialContextCreateInfoEXT()
    future = FutureEXT()
    future.instance = session.instance
    future._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateSpatialContextAsyncEXT"),
        PFN_xrCreateSpatialContextAsyncEXT,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(future),
    ))
    if result.is_exception():
        raise result
    return future


def create_spatial_context_complete_ext(
    session: Session,
    future: FutureEXT,
) -> CreateSpatialContextCompletionEXT:
    completion = CreateSpatialContextCompletionEXT()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateSpatialContextCompleteEXT"),
        PFN_xrCreateSpatialContextCompleteEXT,
    )
    result = check_result(fxn(
        session,
        future,
        byref(completion),
    ))
    if result.is_exception():
        raise result
    return completion


def destroy_spatial_context_ext(
    spatial_context: SpatialContextEXT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(spatial_context.instance, "xrDestroySpatialContextEXT"),
        PFN_xrDestroySpatialContextEXT,
    )
    result = check_result(fxn(
        spatial_context,
    ))
    if result.is_exception():
        raise result


def create_spatial_discovery_snapshot_async_ext(
    spatial_context: SpatialContextEXT,
    create_info: SpatialDiscoverySnapshotCreateInfoEXT = None,
) -> FutureEXT:
    if create_info is None:
        create_info = SpatialDiscoverySnapshotCreateInfoEXT()
    future = FutureEXT()
    future.instance = spatial_context.instance
    future._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(spatial_context.instance, "xrCreateSpatialDiscoverySnapshotAsyncEXT"),
        PFN_xrCreateSpatialDiscoverySnapshotAsyncEXT,
    )
    result = check_result(fxn(
        spatial_context,
        create_info,
        byref(future),
    ))
    if result.is_exception():
        raise result
    return future


def create_spatial_discovery_snapshot_complete_ext(
    spatial_context: SpatialContextEXT,
    create_snapshot_completion_info: CreateSpatialDiscoverySnapshotCompletionInfoEXT,
) -> CreateSpatialDiscoverySnapshotCompletionEXT:
    completion = CreateSpatialDiscoverySnapshotCompletionEXT()
    fxn = cast(
        get_instance_proc_addr(spatial_context.instance, "xrCreateSpatialDiscoverySnapshotCompleteEXT"),
        PFN_xrCreateSpatialDiscoverySnapshotCompleteEXT,
    )
    result = check_result(fxn(
        spatial_context,
        create_snapshot_completion_info,
        byref(completion),
    ))
    if result.is_exception():
        raise result
    return completion


def query_spatial_component_data_ext(
    snapshot: SpatialSnapshotEXT,
    query_condition: SpatialComponentDataQueryConditionEXT,
) -> SpatialComponentDataQueryResultEXT:
    query_result = SpatialComponentDataQueryResultEXT()
    fxn = cast(
        get_instance_proc_addr(snapshot.instance, "xrQuerySpatialComponentDataEXT"),
        PFN_xrQuerySpatialComponentDataEXT,
    )
    result = check_result(fxn(
        snapshot,
        query_condition,
        byref(query_result),
    ))
    if result.is_exception():
        raise result
    return query_result


def destroy_spatial_snapshot_ext(
    snapshot: SpatialSnapshotEXT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(snapshot.instance, "xrDestroySpatialSnapshotEXT"),
        PFN_xrDestroySpatialSnapshotEXT,
    )
    result = check_result(fxn(
        snapshot,
    ))
    if result.is_exception():
        raise result


def create_spatial_entity_from_id_ext(
    spatial_context: SpatialContextEXT,
    create_info: SpatialEntityFromIdCreateInfoEXT = None,
) -> SpatialEntityEXT:
    if create_info is None:
        create_info = SpatialEntityFromIdCreateInfoEXT()
    spatial_entity = SpatialEntityEXT()
    spatial_entity.instance = spatial_context.instance
    spatial_entity._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(spatial_context.instance, "xrCreateSpatialEntityFromIdEXT"),
        PFN_xrCreateSpatialEntityFromIdEXT,
    )
    result = check_result(fxn(
        spatial_context,
        create_info,
        byref(spatial_entity),
    ))
    if result.is_exception():
        raise result
    return spatial_entity


def destroy_spatial_entity_ext(
    spatial_entity: SpatialEntityEXT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(spatial_entity.instance, "xrDestroySpatialEntityEXT"),
        PFN_xrDestroySpatialEntityEXT,
    )
    result = check_result(fxn(
        spatial_entity,
    ))
    if result.is_exception():
        raise result


def create_spatial_update_snapshot_ext(
    spatial_context: SpatialContextEXT,
    create_info: SpatialUpdateSnapshotCreateInfoEXT = None,
) -> SpatialSnapshotEXT:
    if create_info is None:
        create_info = SpatialUpdateSnapshotCreateInfoEXT()
    snapshot = SpatialSnapshotEXT()
    snapshot.instance = spatial_context.instance
    snapshot._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(spatial_context.instance, "xrCreateSpatialUpdateSnapshotEXT"),
        PFN_xrCreateSpatialUpdateSnapshotEXT,
    )
    result = check_result(fxn(
        spatial_context,
        create_info,
        byref(snapshot),
    ))
    if result.is_exception():
        raise result
    return snapshot


def get_spatial_buffer_string_ext(
    snapshot: SpatialSnapshotEXT,
    info: SpatialBufferGetInfoEXT,
) -> str:
    buffer_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(snapshot.instance, "xrGetSpatialBufferStringEXT"),
        PFN_xrGetSpatialBufferStringEXT,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        snapshot,
        info,
        0,
        byref(buffer_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    buffer = create_string_buffer(buffer_capacity_input.value)
    result = check_result(fxn(
        snapshot,
        info,
        buffer_capacity_input,
        byref(buffer_capacity_input),
        buffer,
    ))
    if result.is_exception():
        raise result
    return buffer.value.decode()


def get_spatial_buffer_uint8_ext(
    snapshot: SpatialSnapshotEXT,
    info: SpatialBufferGetInfoEXT,
) -> Sequence[int]:
    buffer_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(snapshot.instance, "xrGetSpatialBufferUint8EXT"),
        PFN_xrGetSpatialBufferUint8EXT,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        snapshot,
        info,
        0,
        byref(buffer_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    buffer = (c_uint8 * buffer_capacity_input.value)(*([c_uint8()] * buffer_capacity_input.value))  # noqa
    result = check_result(fxn(
        snapshot,
        info,
        buffer_capacity_input,
        byref(buffer_capacity_input),
        buffer,
    ))
    if result.is_exception():
        raise result
    return buffer  # noqa


def get_spatial_buffer_uint16_ext(
    snapshot: SpatialSnapshotEXT,
    info: SpatialBufferGetInfoEXT,
) -> Sequence[int]:
    buffer_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(snapshot.instance, "xrGetSpatialBufferUint16EXT"),
        PFN_xrGetSpatialBufferUint16EXT,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        snapshot,
        info,
        0,
        byref(buffer_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    buffer = (c_uint16 * buffer_capacity_input.value)(*([c_uint16()] * buffer_capacity_input.value))  # noqa
    result = check_result(fxn(
        snapshot,
        info,
        buffer_capacity_input,
        byref(buffer_capacity_input),
        buffer,
    ))
    if result.is_exception():
        raise result
    return buffer  # noqa


def get_spatial_buffer_uint32_ext(
    snapshot: SpatialSnapshotEXT,
    info: SpatialBufferGetInfoEXT,
) -> Sequence[int]:
    buffer_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(snapshot.instance, "xrGetSpatialBufferUint32EXT"),
        PFN_xrGetSpatialBufferUint32EXT,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        snapshot,
        info,
        0,
        byref(buffer_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    buffer = (c_uint32 * buffer_capacity_input.value)(*([c_uint32()] * buffer_capacity_input.value))  # noqa
    result = check_result(fxn(
        snapshot,
        info,
        buffer_capacity_input,
        byref(buffer_capacity_input),
        buffer,
    ))
    if result.is_exception():
        raise result
    return buffer  # noqa


def get_spatial_buffer_float_ext(
    snapshot: SpatialSnapshotEXT,
    info: SpatialBufferGetInfoEXT,
) -> Sequence[float]:
    buffer_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(snapshot.instance, "xrGetSpatialBufferFloatEXT"),
        PFN_xrGetSpatialBufferFloatEXT,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        snapshot,
        info,
        0,
        byref(buffer_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    buffer = (c_float * buffer_capacity_input.value)(*([c_float()] * buffer_capacity_input.value))  # noqa
    result = check_result(fxn(
        snapshot,
        info,
        buffer_capacity_input,
        byref(buffer_capacity_input),
        buffer,
    ))
    if result.is_exception():
        raise result
    return buffer  # noqa


def get_spatial_buffer_vector2f_ext(
    snapshot: SpatialSnapshotEXT,
    info: SpatialBufferGetInfoEXT,
) -> Sequence[Vector2f]:
    buffer_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(snapshot.instance, "xrGetSpatialBufferVector2fEXT"),
        PFN_xrGetSpatialBufferVector2fEXT,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        snapshot,
        info,
        0,
        byref(buffer_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    buffer = (Vector2f * buffer_capacity_input.value)(*([Vector2f()] * buffer_capacity_input.value))  # noqa
    result = check_result(fxn(
        snapshot,
        info,
        buffer_capacity_input,
        byref(buffer_capacity_input),
        buffer,
    ))
    if result.is_exception():
        raise result
    return buffer  # noqa


def get_spatial_buffer_vector3f_ext(
    snapshot: SpatialSnapshotEXT,
    info: SpatialBufferGetInfoEXT,
) -> Sequence[Vector3f]:
    buffer_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(snapshot.instance, "xrGetSpatialBufferVector3fEXT"),
        PFN_xrGetSpatialBufferVector3fEXT,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        snapshot,
        info,
        0,
        byref(buffer_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    buffer = (Vector3f * buffer_capacity_input.value)(*([Vector3f()] * buffer_capacity_input.value))  # noqa
    result = check_result(fxn(
        snapshot,
        info,
        buffer_capacity_input,
        byref(buffer_capacity_input),
        buffer,
    ))
    if result.is_exception():
        raise result
    return buffer  # noqa


def create_spatial_anchor_ext(
    spatial_context: SpatialContextEXT,
    create_info: SpatialAnchorCreateInfoEXT = None,
) -> (SpatialEntityIdEXT, SpatialEntityEXT):
    if create_info is None:
        create_info = SpatialAnchorCreateInfoEXT()
    anchor_entity_id = SpatialEntityIdEXT()
    anchor_entity = SpatialEntityEXT()
    fxn = cast(
        get_instance_proc_addr(spatial_context.instance, "xrCreateSpatialAnchorEXT"),
        PFN_xrCreateSpatialAnchorEXT,
    )
    result = check_result(fxn(
        spatial_context,
        create_info,
        byref(anchor_entity_id),
        byref(anchor_entity),
    ))
    if result.is_exception():
        raise result
    return anchor_entity_id, anchor_entity


def enumerate_spatial_persistence_scopes_ext(
    instance: Instance,
    system_id: SystemId,
) -> Sequence[SpatialPersistenceScopeEXT]:
    persistence_scope_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrEnumerateSpatialPersistenceScopesEXT"),
        PFN_xrEnumerateSpatialPersistenceScopesEXT,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        instance,
        system_id,
        0,
        byref(persistence_scope_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    persistence_scopes = (SpatialPersistenceScopeEXT.ctype() * persistence_scope_capacity_input.value)(*([SpatialPersistenceScopeEXT.ctype()()] * persistence_scope_capacity_input.value))  # noqa
    result = check_result(fxn(
        instance,
        system_id,
        persistence_scope_capacity_input,
        byref(persistence_scope_capacity_input),
        persistence_scopes,
    ))
    if result.is_exception():
        raise result
    return persistence_scopes  # noqa


def create_spatial_persistence_context_async_ext(
    session: Session,
    create_info: SpatialPersistenceContextCreateInfoEXT = None,
) -> FutureEXT:
    if create_info is None:
        create_info = SpatialPersistenceContextCreateInfoEXT()
    future = FutureEXT()
    future.instance = session.instance
    future._create_info = create_info
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateSpatialPersistenceContextAsyncEXT"),
        PFN_xrCreateSpatialPersistenceContextAsyncEXT,
    )
    result = check_result(fxn(
        session,
        create_info,
        byref(future),
    ))
    if result.is_exception():
        raise result
    return future


def create_spatial_persistence_context_complete_ext(
    session: Session,
    future: FutureEXT,
) -> CreateSpatialPersistenceContextCompletionEXT:
    completion = CreateSpatialPersistenceContextCompletionEXT()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateSpatialPersistenceContextCompleteEXT"),
        PFN_xrCreateSpatialPersistenceContextCompleteEXT,
    )
    result = check_result(fxn(
        session,
        future,
        byref(completion),
    ))
    if result.is_exception():
        raise result
    return completion


def destroy_spatial_persistence_context_ext(
    persistence_context: SpatialPersistenceContextEXT,
) -> None:
    fxn = cast(
        get_instance_proc_addr(persistence_context.instance, "xrDestroySpatialPersistenceContextEXT"),
        PFN_xrDestroySpatialPersistenceContextEXT,
    )
    result = check_result(fxn(
        persistence_context,
    ))
    if result.is_exception():
        raise result


def persist_spatial_entity_async_ext(
    persistence_context: SpatialPersistenceContextEXT,
    persist_info: SpatialEntityPersistInfoEXT,
) -> FutureEXT:
    future = FutureEXT()
    fxn = cast(
        get_instance_proc_addr(persistence_context.instance, "xrPersistSpatialEntityAsyncEXT"),
        PFN_xrPersistSpatialEntityAsyncEXT,
    )
    result = check_result(fxn(
        persistence_context,
        persist_info,
        byref(future),
    ))
    if result.is_exception():
        raise result
    return future


def persist_spatial_entity_complete_ext(
    persistence_context: SpatialPersistenceContextEXT,
    future: FutureEXT,
) -> PersistSpatialEntityCompletionEXT:
    completion = PersistSpatialEntityCompletionEXT()
    fxn = cast(
        get_instance_proc_addr(persistence_context.instance, "xrPersistSpatialEntityCompleteEXT"),
        PFN_xrPersistSpatialEntityCompleteEXT,
    )
    result = check_result(fxn(
        persistence_context,
        future,
        byref(completion),
    ))
    if result.is_exception():
        raise result
    return completion


def unpersist_spatial_entity_async_ext(
    persistence_context: SpatialPersistenceContextEXT,
    unpersist_info: SpatialEntityUnpersistInfoEXT,
) -> FutureEXT:
    future = FutureEXT()
    fxn = cast(
        get_instance_proc_addr(persistence_context.instance, "xrUnpersistSpatialEntityAsyncEXT"),
        PFN_xrUnpersistSpatialEntityAsyncEXT,
    )
    result = check_result(fxn(
        persistence_context,
        unpersist_info,
        byref(future),
    ))
    if result.is_exception():
        raise result
    return future


def unpersist_spatial_entity_complete_ext(
    persistence_context: SpatialPersistenceContextEXT,
    future: FutureEXT,
) -> UnpersistSpatialEntityCompletionEXT:
    completion = UnpersistSpatialEntityCompletionEXT()
    fxn = cast(
        get_instance_proc_addr(persistence_context.instance, "xrUnpersistSpatialEntityCompleteEXT"),
        PFN_xrUnpersistSpatialEntityCompleteEXT,
    )
    result = check_result(fxn(
        persistence_context,
        future,
        byref(completion),
    ))
    if result.is_exception():
        raise result
    return completion


__all__ = [
    "acquire_environment_depth_image_meta",
    "acquire_swapchain_image",
    "allocate_world_mesh_buffer_ml",
    "apply_force_feedback_curl_mndx",
    "apply_foveation_htc",
    "apply_haptic_feedback",
    "attach_session_action_sets",
    "begin_frame",
    "begin_plane_detection_ext",
    "begin_session",
    "cancel_future_ext",
    "capture_scene_async_bd",
    "capture_scene_complete_bd",
    "change_virtual_keyboard_text_context_meta",
    "clear_spatial_anchor_store_msft",
    "compute_new_scene_msft",
    "create_action",
    "create_action_set",
    "create_action_space",
    "create_anchor_space_android",
    "create_anchor_space_bd",
    "create_body_tracker_bd",
    "create_body_tracker_fb",
    "create_body_tracker_htc",
    "create_debug_utils_messenger_ext",
    "create_device_anchor_persistence_android",
    "create_environment_depth_provider_meta",
    "create_environment_depth_swapchain_meta",
    "create_exported_localization_map_ml",
    "create_eye_tracker_fb",
    "create_face_tracker2_fb",
    "create_face_tracker_android",
    "create_face_tracker_bd",
    "create_face_tracker_fb",
    "create_facial_expression_client_ml",
    "create_facial_tracker_htc",
    "create_foveation_profile_fb",
    "create_geometry_instance_fb",
    "create_hand_mesh_space_msft",
    "create_hand_tracker_ext",
    "create_instance",
    "create_keyboard_space_fb",
    "create_marker_detector_ml",
    "create_marker_space_ml",
    "create_marker_space_varjo",
    "create_passthrough_color_lut_meta",
    "create_passthrough_fb",
    "create_passthrough_htc",
    "create_passthrough_layer_fb",
    "create_persisted_anchor_space_android",
    "create_plane_detector_ext",
    "create_reference_space",
    "create_render_model_asset_ext",
    "create_render_model_ext",
    "create_render_model_space_ext",
    "create_scene_msft",
    "create_scene_observer_msft",
    "create_sense_data_provider_bd",
    "create_session",
    "create_space_user_fb",
    "create_spatial_anchor_async_bd",
    "create_spatial_anchor_complete_bd",
    "create_spatial_anchor_ext",
    "create_spatial_anchor_fb",
    "create_spatial_anchor_from_persisted_name_msft",
    "create_spatial_anchor_htc",
    "create_spatial_anchor_msft",
    "create_spatial_anchor_space_msft",
    "create_spatial_anchor_store_connection_msft",
    "create_spatial_anchors_async_ml",
    "create_spatial_anchors_complete_ml",
    "create_spatial_anchors_storage_ml",
    "create_spatial_context_async_ext",
    "create_spatial_context_complete_ext",
    "create_spatial_discovery_snapshot_async_ext",
    "create_spatial_discovery_snapshot_complete_ext",
    "create_spatial_entity_anchor_bd",
    "create_spatial_entity_from_id_ext",
    "create_spatial_graph_node_space_msft",
    "create_spatial_persistence_context_async_ext",
    "create_spatial_persistence_context_complete_ext",
    "create_spatial_update_snapshot_ext",
    "create_swapchain",
    "create_trackable_tracker_android",
    "create_triangle_mesh_fb",
    "create_virtual_keyboard_meta",
    "create_virtual_keyboard_space_meta",
    "create_world_mesh_detector_ml",
    "delete_spatial_anchors_async_ml",
    "delete_spatial_anchors_complete_ml",
    "deserialize_scene_msft",
    "destroy_action",
    "destroy_action_set",
    "destroy_anchor_bd",
    "destroy_body_tracker_bd",
    "destroy_body_tracker_fb",
    "destroy_body_tracker_htc",
    "destroy_debug_utils_messenger_ext",
    "destroy_device_anchor_persistence_android",
    "destroy_environment_depth_provider_meta",
    "destroy_environment_depth_swapchain_meta",
    "destroy_exported_localization_map_ml",
    "destroy_eye_tracker_fb",
    "destroy_face_tracker2_fb",
    "destroy_face_tracker_android",
    "destroy_face_tracker_bd",
    "destroy_face_tracker_fb",
    "destroy_facial_expression_client_ml",
    "destroy_facial_tracker_htc",
    "destroy_foveation_profile_fb",
    "destroy_geometry_instance_fb",
    "destroy_hand_tracker_ext",
    "destroy_instance",
    "destroy_marker_detector_ml",
    "destroy_passthrough_color_lut_meta",
    "destroy_passthrough_fb",
    "destroy_passthrough_htc",
    "destroy_passthrough_layer_fb",
    "destroy_plane_detector_ext",
    "destroy_render_model_asset_ext",
    "destroy_render_model_ext",
    "destroy_scene_msft",
    "destroy_scene_observer_msft",
    "destroy_sense_data_provider_bd",
    "destroy_sense_data_snapshot_bd",
    "destroy_session",
    "destroy_space",
    "destroy_space_user_fb",
    "destroy_spatial_anchor_msft",
    "destroy_spatial_anchor_store_connection_msft",
    "destroy_spatial_anchors_storage_ml",
    "destroy_spatial_context_ext",
    "destroy_spatial_entity_ext",
    "destroy_spatial_graph_node_binding_msft",
    "destroy_spatial_persistence_context_ext",
    "destroy_spatial_snapshot_ext",
    "destroy_swapchain",
    "destroy_trackable_tracker_android",
    "destroy_triangle_mesh_fb",
    "destroy_virtual_keyboard_meta",
    "destroy_world_mesh_detector_ml",
    "discover_spaces_meta",
    "download_shared_spatial_anchor_async_bd",
    "download_shared_spatial_anchor_complete_bd",
    "enable_localization_events_ml",
    "enable_user_calibration_events_ml",
    "end_frame",
    "end_session",
    "enumerate_api_layer_properties",
    "enumerate_bound_sources_for_action",
    "enumerate_color_spaces_fb",
    "enumerate_display_refresh_rates_fb",
    "enumerate_environment_blend_modes",
    "enumerate_environment_depth_swapchain_images_meta",
    "enumerate_external_cameras_oculus",
    "enumerate_facial_simulation_modes_bd",
    "enumerate_instance_extension_properties",
    "enumerate_interaction_render_model_ids_ext",
    "enumerate_performance_metrics_counter_paths_meta",
    "enumerate_persisted_anchors_android",
    "enumerate_persisted_spatial_anchor_names_msft",
    "enumerate_raycast_supported_trackable_types_android",
    "enumerate_reference_spaces",
    "enumerate_render_model_paths_fb",
    "enumerate_render_model_subaction_paths_ext",
    "enumerate_reprojection_modes_msft",
    "enumerate_scene_compute_features_msft",
    "enumerate_space_supported_components_fb",
    "enumerate_spatial_capabilities_ext",
    "enumerate_spatial_capability_component_types_ext",
    "enumerate_spatial_capability_features_ext",
    "enumerate_spatial_entity_component_types_bd",
    "enumerate_spatial_persistence_scopes_ext",
    "enumerate_supported_anchor_trackable_types_android",
    "enumerate_supported_persistence_anchor_types_android",
    "enumerate_supported_trackable_types_android",
    "enumerate_swapchain_formats",
    "enumerate_swapchain_images",
    "enumerate_view_configuration_views",
    "enumerate_view_configurations",
    "enumerate_vive_tracker_paths_htcx",
    "erase_space_fb",
    "erase_spaces_meta",
    "free_world_mesh_buffer_ml",
    "geometry_instance_set_transform_fb",
    "get_action_state_boolean",
    "get_action_state_float",
    "get_action_state_pose",
    "get_action_state_vector2f",
    "get_all_trackables_android",
    "get_anchor_persist_state_android",
    "get_anchor_uuid_bd",
    "get_body_skeleton_fb",
    "get_body_skeleton_htc",
    "get_controller_model_key_msft",
    "get_controller_model_properties_msft",
    "get_controller_model_state_msft",
    "get_current_interaction_profile",
    "get_device_sample_rate_fb",
    "get_display_refresh_rate_fb",
    "get_environment_depth_swapchain_state_meta",
    "get_exported_localization_map_data_ml",
    "get_eye_gazes_fb",
    "get_face_calibration_state_android",
    "get_face_expression_weights2_fb",
    "get_face_expression_weights_fb",
    "get_face_state_android",
    "get_facial_expression_blend_shape_properties_ml",
    "get_facial_expressions_htc",
    "get_facial_simulation_data_bd",
    "get_facial_simulation_mode_bd",
    "get_foveation_eye_tracked_state_meta",
    "get_hand_mesh_fb",
    "get_input_source_localized_name",
    "get_instance_proc_addr",
    "get_instance_properties",
    "get_marker_detector_state_ml",
    "get_marker_length_ml",
    "get_marker_number_ml",
    "get_marker_reprojection_error_ml",
    "get_marker_size_varjo",
    "get_marker_string_ml",
    "get_markers_ml",
    "get_passthrough_camera_state_android",
    "get_passthrough_preferences_meta",
    "get_performance_metrics_state_meta",
    "get_plane_detection_state_ext",
    "get_plane_detections_ext",
    "get_plane_polygon_buffer_ext",
    "get_queried_sense_data_bd",
    "get_recommended_layer_resolution_meta",
    "get_reference_space_bounds_rect",
    "get_render_model_asset_data_ext",
    "get_render_model_asset_properties_ext",
    "get_render_model_pose_top_level_user_path_ext",
    "get_render_model_properties_ext",
    "get_render_model_properties_fb",
    "get_render_model_state_ext",
    "get_scene_components_msft",
    "get_scene_compute_state_msft",
    "get_scene_marker_decoded_string_msft",
    "get_scene_marker_raw_data_msft",
    "get_scene_mesh_buffers_msft",
    "get_sense_data_provider_state_bd",
    "get_serialized_scene_fragment_data_msft",
    "get_space_boundary_2d_fb",
    "get_space_bounding_box_2d_fb",
    "get_space_bounding_box_3d_fb",
    "get_space_component_status_fb",
    "get_space_container_fb",
    "get_space_room_layout_fb",
    "get_space_semantic_labels_fb",
    "get_space_triangle_mesh_meta",
    "get_space_user_id_fb",
    "get_space_uuid_fb",
    "get_spatial_anchor_name_htc",
    "get_spatial_anchor_state_ml",
    "get_spatial_buffer_float_ext",
    "get_spatial_buffer_string_ext",
    "get_spatial_buffer_uint16_ext",
    "get_spatial_buffer_uint32_ext",
    "get_spatial_buffer_uint8_ext",
    "get_spatial_buffer_vector2f_ext",
    "get_spatial_buffer_vector3f_ext",
    "get_spatial_entity_component_data_bd",
    "get_spatial_entity_uuid_bd",
    "get_spatial_graph_node_binding_properties_msft",
    "get_swapchain_state_fb",
    "get_system",
    "get_system_properties",
    "get_trackable_marker_android",
    "get_trackable_object_android",
    "get_trackable_plane_android",
    "get_view_configuration_properties",
    "get_virtual_keyboard_dirty_textures_meta",
    "get_virtual_keyboard_model_animation_states_meta",
    "get_virtual_keyboard_scale_meta",
    "get_virtual_keyboard_texture_data_meta",
    "get_visibility_mask_khr",
    "get_world_mesh_buffer_recommend_size_ml",
    "import_localization_map_ml",
    "initialize_loader_khr",
    "load_controller_model_msft",
    "load_render_model_fb",
    "locate_body_joints_bd",
    "locate_body_joints_fb",
    "locate_body_joints_htc",
    "locate_hand_joints_ext",
    "locate_scene_components_msft",
    "locate_space",
    "locate_spaces",
    "locate_views",
    "passthrough_layer_pause_fb",
    "passthrough_layer_resume_fb",
    "passthrough_layer_set_keyboard_hands_intensity_fb",
    "passthrough_layer_set_style_fb",
    "passthrough_pause_fb",
    "passthrough_start_fb",
    "path_to_string",
    "pause_simultaneous_hands_and_controllers_tracking_meta",
    "perf_settings_set_performance_level_ext",
    "persist_anchor_android",
    "persist_spatial_anchor_async_bd",
    "persist_spatial_anchor_complete_bd",
    "persist_spatial_anchor_msft",
    "persist_spatial_entity_async_ext",
    "persist_spatial_entity_complete_ext",
    "poll_event",
    "poll_future_ext",
    "publish_spatial_anchors_async_ml",
    "publish_spatial_anchors_complete_ml",
    "query_localization_maps_ml",
    "query_performance_metrics_counter_meta",
    "query_sense_data_async_bd",
    "query_sense_data_complete_bd",
    "query_spaces_fb",
    "query_spatial_anchors_async_ml",
    "query_spatial_anchors_complete_ml",
    "query_spatial_component_data_ext",
    "query_system_tracked_keyboard_fb",
    "raycast_android",
    "release_swapchain_image",
    "request_display_refresh_rate_fb",
    "request_exit_session",
    "request_map_localization_ml",
    "request_scene_capture_fb",
    "request_world_mesh_async_ml",
    "request_world_mesh_complete_ml",
    "request_world_mesh_state_async_ml",
    "request_world_mesh_state_complete_ml",
    "reset_body_tracking_calibration_meta",
    "result_to_string",
    "resume_simultaneous_hands_and_controllers_tracking_meta",
    "retrieve_space_discovery_results_meta",
    "retrieve_space_query_results_fb",
    "save_space_fb",
    "save_space_list_fb",
    "save_spaces_meta",
    "send_virtual_keyboard_input_meta",
    "session_begin_debug_utils_label_region_ext",
    "session_end_debug_utils_label_region_ext",
    "session_insert_debug_utils_label_ext",
    "set_color_space_fb",
    "set_debug_utils_object_name_ext",
    "set_digital_lens_control_almalence",
    "set_environment_depth_estimation_varjo",
    "set_environment_depth_hand_removal_meta",
    "set_facial_simulation_mode_bd",
    "set_input_device_active_ext",
    "set_input_device_location_ext",
    "set_input_device_state_bool_ext",
    "set_input_device_state_float_ext",
    "set_input_device_state_vector2f_ext",
    "set_marker_tracking_prediction_varjo",
    "set_marker_tracking_timeout_varjo",
    "set_marker_tracking_varjo",
    "set_performance_metrics_state_meta",
    "set_space_component_status_fb",
    "set_system_notifications_ml",
    "set_tracking_optimization_settings_hint_qcom",
    "set_view_offset_varjo",
    "set_virtual_keyboard_model_visibility_meta",
    "share_spaces_fb",
    "share_spaces_meta",
    "share_spatial_anchor_async_bd",
    "share_spatial_anchor_complete_bd",
    "snapshot_marker_detector_ml",
    "start_colocation_advertisement_meta",
    "start_colocation_discovery_meta",
    "start_environment_depth_provider_meta",
    "start_sense_data_provider_async_bd",
    "start_sense_data_provider_complete_bd",
    "stop_colocation_advertisement_meta",
    "stop_colocation_discovery_meta",
    "stop_environment_depth_provider_meta",
    "stop_haptic_feedback",
    "stop_sense_data_provider_bd",
    "string_to_path",
    "structure_type_to_string",
    "structure_type_to_string2_khr",
    "submit_debug_utils_message_ext",
    "suggest_body_tracking_calibration_override_meta",
    "suggest_interaction_profile_bindings",
    "suggest_virtual_keyboard_location_meta",
    "sync_actions",
    "thermal_get_temperature_trend_ext",
    "triangle_mesh_begin_update_fb",
    "triangle_mesh_begin_vertex_buffer_update_fb",
    "triangle_mesh_end_update_fb",
    "triangle_mesh_end_vertex_buffer_update_fb",
    "triangle_mesh_get_index_buffer_fb",
    "triangle_mesh_get_vertex_buffer_fb",
    "try_create_spatial_graph_static_node_binding_msft",
    "unpersist_anchor_android",
    "unpersist_spatial_anchor_async_bd",
    "unpersist_spatial_anchor_complete_bd",
    "unpersist_spatial_anchor_msft",
    "unpersist_spatial_entity_async_ext",
    "unpersist_spatial_entity_complete_ext",
    "update_hand_mesh_msft",
    "update_passthrough_color_lut_meta",
    "update_spatial_anchors_expiration_async_ml",
    "update_spatial_anchors_expiration_complete_ml",
    "update_swapchain_fb",
    "wait_frame",
    "wait_swapchain_image",
]
