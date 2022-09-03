# Warning: this file is auto-generated. Do not edit.

from ctypes import POINTER, c_char, c_char_p, c_int64, c_uint32

"""
File xr.raw_functions.py

Defines low-level ctypes function definitions for use by
higher-level pythonic functions in pyopenxr.
"""

from .library import openxr_loader_library
from .enums import *
from .typedefs import *


# ctypes Function definitions

xrGetInstanceProcAddr = openxr_loader_library.xrGetInstanceProcAddr
xrGetInstanceProcAddr.__doc__ = """
    Gets a function pointer for an OpenXR function.
"""
xrGetInstanceProcAddr.restype = Result
xrGetInstanceProcAddr.argtypes = [
    Instance,  # instance
    c_char_p,  # name
    POINTER(PFN_xrVoidFunction),  # function
]

xrEnumerateApiLayerProperties = openxr_loader_library.xrEnumerateApiLayerProperties
xrEnumerateApiLayerProperties.__doc__ = """
    Returns up to requested number of global layer properties.
"""
xrEnumerateApiLayerProperties.restype = Result
xrEnumerateApiLayerProperties.argtypes = [
    c_uint32,  # property_capacity_input
    POINTER(c_uint32),  # property_count_output
    POINTER(ApiLayerProperties),  # properties
]

xrEnumerateInstanceExtensionProperties = openxr_loader_library.xrEnumerateInstanceExtensionProperties
xrEnumerateInstanceExtensionProperties.__doc__ = """
    Returns properties of available instance extensions.
"""
xrEnumerateInstanceExtensionProperties.restype = Result
xrEnumerateInstanceExtensionProperties.argtypes = [
    c_char_p,  # layer_name
    c_uint32,  # property_capacity_input
    POINTER(c_uint32),  # property_count_output
    POINTER(ExtensionProperties),  # properties
]

xrCreateInstance = openxr_loader_library.xrCreateInstance
xrCreateInstance.__doc__ = """
    Creates an OpenXR Instance.
"""
xrCreateInstance.restype = Result
xrCreateInstance.argtypes = [
    POINTER(InstanceCreateInfo),  # create_info
    POINTER(Instance),  # instance
]

xrDestroyInstance = openxr_loader_library.xrDestroyInstance
xrDestroyInstance.__doc__ = """
    Destroy an instance of OpenXR.
"""
xrDestroyInstance.restype = Result
xrDestroyInstance.argtypes = [
    Instance,  # instance
]

xrGetInstanceProperties = openxr_loader_library.xrGetInstanceProperties
xrGetInstanceProperties.__doc__ = """
    Gets information about the instance.
"""
xrGetInstanceProperties.restype = Result
xrGetInstanceProperties.argtypes = [
    Instance,  # instance
    POINTER(InstanceProperties),  # instance_properties
]

xrPollEvent = openxr_loader_library.xrPollEvent
xrPollEvent.__doc__ = """
    Polls for events.
"""
xrPollEvent.restype = Result
xrPollEvent.argtypes = [
    Instance,  # instance
    POINTER(EventDataBuffer),  # event_data
]

xrResultToString = openxr_loader_library.xrResultToString
xrResultToString.__doc__ = """
    Converts an XrResult to a UTF-8 string.
"""
xrResultToString.restype = Result
xrResultToString.argtypes = [
    Instance,  # instance
    Result.ctype(),  # value
    (c_char * 64),  # buffer
]

xrStructureTypeToString = openxr_loader_library.xrStructureTypeToString
xrStructureTypeToString.__doc__ = """
    Converts an XrStructureType to a UTF-8 string.
"""
xrStructureTypeToString.restype = Result
xrStructureTypeToString.argtypes = [
    Instance,  # instance
    StructureType.ctype(),  # value
    (c_char * 64),  # buffer
]

xrGetSystem = openxr_loader_library.xrGetSystem
xrGetSystem.__doc__ = """
    Gets a system identifier.
"""
xrGetSystem.restype = Result
xrGetSystem.argtypes = [
    Instance,  # instance
    POINTER(SystemGetInfo),  # get_info
    POINTER(SystemId),  # system_id
]

xrGetSystemProperties = openxr_loader_library.xrGetSystemProperties
xrGetSystemProperties.__doc__ = """
    Gets the properties of a particular system.
"""
xrGetSystemProperties.restype = Result
xrGetSystemProperties.argtypes = [
    Instance,  # instance
    SystemId,  # system_id
    POINTER(SystemProperties),  # properties
]

xrEnumerateEnvironmentBlendModes = openxr_loader_library.xrEnumerateEnvironmentBlendModes
xrEnumerateEnvironmentBlendModes.__doc__ = """
    Lists environment blend modes.
"""
xrEnumerateEnvironmentBlendModes.restype = Result
xrEnumerateEnvironmentBlendModes.argtypes = [
    Instance,  # instance
    SystemId,  # system_id
    ViewConfigurationType.ctype(),  # view_configuration_type
    c_uint32,  # environment_blend_mode_capacity_input
    POINTER(c_uint32),  # environment_blend_mode_count_output
    POINTER(EnvironmentBlendMode.ctype()),  # environment_blend_modes
]

xrCreateSession = openxr_loader_library.xrCreateSession
xrCreateSession.__doc__ = """
    Creates an XrSession.
"""
xrCreateSession.restype = Result
xrCreateSession.argtypes = [
    Instance,  # instance
    POINTER(SessionCreateInfo),  # create_info
    POINTER(Session),  # session
]

xrDestroySession = openxr_loader_library.xrDestroySession
xrDestroySession.__doc__ = """
    Destroys an XrSession.
"""
xrDestroySession.restype = Result
xrDestroySession.argtypes = [
    Session,  # session
]

xrEnumerateReferenceSpaces = openxr_loader_library.xrEnumerateReferenceSpaces
xrEnumerateReferenceSpaces.__doc__ = """
    Enumerate available reference spaces.
"""
xrEnumerateReferenceSpaces.restype = Result
xrEnumerateReferenceSpaces.argtypes = [
    Session,  # session
    c_uint32,  # space_capacity_input
    POINTER(c_uint32),  # space_count_output
    POINTER(ReferenceSpaceType.ctype()),  # spaces
]

xrCreateReferenceSpace = openxr_loader_library.xrCreateReferenceSpace
xrCreateReferenceSpace.__doc__ = """
    Creates a reference space.
"""
xrCreateReferenceSpace.restype = Result
xrCreateReferenceSpace.argtypes = [
    Session,  # session
    POINTER(ReferenceSpaceCreateInfo),  # create_info
    POINTER(Space),  # space
]

xrGetReferenceSpaceBoundsRect = openxr_loader_library.xrGetReferenceSpaceBoundsRect
xrGetReferenceSpaceBoundsRect.__doc__ = """
    Gets the bounds rectangle of a reference space.
"""
xrGetReferenceSpaceBoundsRect.restype = Result
xrGetReferenceSpaceBoundsRect.argtypes = [
    Session,  # session
    ReferenceSpaceType.ctype(),  # reference_space_type
    POINTER(Extent2Df),  # bounds
]

xrCreateActionSpace = openxr_loader_library.xrCreateActionSpace
xrCreateActionSpace.__doc__ = """
    Creates a space based on a pose action.
"""
xrCreateActionSpace.restype = Result
xrCreateActionSpace.argtypes = [
    Session,  # session
    POINTER(ActionSpaceCreateInfo),  # create_info
    POINTER(Space),  # space
]

xrLocateSpace = openxr_loader_library.xrLocateSpace
xrLocateSpace.__doc__ = """
    Locates a space with reference to another space.
"""
xrLocateSpace.restype = Result
xrLocateSpace.argtypes = [
    Space,  # space
    Space,  # base_space
    Time,  # time
    POINTER(SpaceLocation),  # location
]

xrDestroySpace = openxr_loader_library.xrDestroySpace
xrDestroySpace.__doc__ = """
    Creates a space based on a pose action.
"""
xrDestroySpace.restype = Result
xrDestroySpace.argtypes = [
    Space,  # space
]

xrEnumerateViewConfigurations = openxr_loader_library.xrEnumerateViewConfigurations
xrEnumerateViewConfigurations.__doc__ = """
    Enumerates supported view configurations.
"""
xrEnumerateViewConfigurations.restype = Result
xrEnumerateViewConfigurations.argtypes = [
    Instance,  # instance
    SystemId,  # system_id
    c_uint32,  # view_configuration_type_capacity_input
    POINTER(c_uint32),  # view_configuration_type_count_output
    POINTER(ViewConfigurationType.ctype()),  # view_configuration_types
]

xrGetViewConfigurationProperties = openxr_loader_library.xrGetViewConfigurationProperties
xrGetViewConfigurationProperties.__doc__ = """
    Gets information for a view configuration.
"""
xrGetViewConfigurationProperties.restype = Result
xrGetViewConfigurationProperties.argtypes = [
    Instance,  # instance
    SystemId,  # system_id
    ViewConfigurationType.ctype(),  # view_configuration_type
    POINTER(ViewConfigurationProperties),  # configuration_properties
]

xrEnumerateViewConfigurationViews = openxr_loader_library.xrEnumerateViewConfigurationViews
xrEnumerateViewConfigurationViews.__doc__ = """
    Gets view configuration views.
"""
xrEnumerateViewConfigurationViews.restype = Result
xrEnumerateViewConfigurationViews.argtypes = [
    Instance,  # instance
    SystemId,  # system_id
    ViewConfigurationType.ctype(),  # view_configuration_type
    c_uint32,  # view_capacity_input
    POINTER(c_uint32),  # view_count_output
    POINTER(ViewConfigurationView),  # views
]

xrEnumerateSwapchainFormats = openxr_loader_library.xrEnumerateSwapchainFormats
xrEnumerateSwapchainFormats.__doc__ = """
    Enumerates swapchain formats.
"""
xrEnumerateSwapchainFormats.restype = Result
xrEnumerateSwapchainFormats.argtypes = [
    Session,  # session
    c_uint32,  # format_capacity_input
    POINTER(c_uint32),  # format_count_output
    POINTER(c_int64),  # formats
]

xrCreateSwapchain = openxr_loader_library.xrCreateSwapchain
xrCreateSwapchain.__doc__ = """
    Creates an XrSwapchain.
"""
xrCreateSwapchain.restype = Result
xrCreateSwapchain.argtypes = [
    Session,  # session
    POINTER(SwapchainCreateInfo),  # create_info
    POINTER(Swapchain),  # swapchain
]

xrDestroySwapchain = openxr_loader_library.xrDestroySwapchain
xrDestroySwapchain.__doc__ = """
    Destroys an XrSwapchain.
"""
xrDestroySwapchain.restype = Result
xrDestroySwapchain.argtypes = [
    Swapchain,  # swapchain
]

xrEnumerateSwapchainImages = openxr_loader_library.xrEnumerateSwapchainImages
xrEnumerateSwapchainImages.__doc__ = """
    Gets images from an XrSwapchain.
"""
xrEnumerateSwapchainImages.restype = Result
xrEnumerateSwapchainImages.argtypes = [
    Swapchain,  # swapchain
    c_uint32,  # image_capacity_input
    POINTER(c_uint32),  # image_count_output
    POINTER(SwapchainImageBaseHeader),  # images
]

xrAcquireSwapchainImage = openxr_loader_library.xrAcquireSwapchainImage
xrAcquireSwapchainImage.__doc__ = """
    Acquire a swapchain image.
"""
xrAcquireSwapchainImage.restype = Result
xrAcquireSwapchainImage.argtypes = [
    Swapchain,  # swapchain
    POINTER(SwapchainImageAcquireInfo),  # acquire_info
    POINTER(c_uint32),  # index
]

xrWaitSwapchainImage = openxr_loader_library.xrWaitSwapchainImage
xrWaitSwapchainImage.__doc__ = """
    Wait for a swapchain image to be available.
"""
xrWaitSwapchainImage.restype = Result
xrWaitSwapchainImage.argtypes = [
    Swapchain,  # swapchain
    POINTER(SwapchainImageWaitInfo),  # wait_info
]

xrReleaseSwapchainImage = openxr_loader_library.xrReleaseSwapchainImage
xrReleaseSwapchainImage.__doc__ = """
    Release a swapchain image.
"""
xrReleaseSwapchainImage.restype = Result
xrReleaseSwapchainImage.argtypes = [
    Swapchain,  # swapchain
    POINTER(SwapchainImageReleaseInfo),  # release_info
]

xrBeginSession = openxr_loader_library.xrBeginSession
xrBeginSession.__doc__ = """
    Begins an XrSession.
"""
xrBeginSession.restype = Result
xrBeginSession.argtypes = [
    Session,  # session
    POINTER(SessionBeginInfo),  # begin_info
]

xrEndSession = openxr_loader_library.xrEndSession
xrEndSession.__doc__ = """
    Ends an XrSession.
"""
xrEndSession.restype = Result
xrEndSession.argtypes = [
    Session,  # session
]

xrRequestExitSession = openxr_loader_library.xrRequestExitSession
xrRequestExitSession.__doc__ = """
    Request to exit a running session.
"""
xrRequestExitSession.restype = Result
xrRequestExitSession.argtypes = [
    Session,  # session
]

xrWaitFrame = openxr_loader_library.xrWaitFrame
xrWaitFrame.__doc__ = """
    Frame timing function.
"""
xrWaitFrame.restype = Result
xrWaitFrame.argtypes = [
    Session,  # session
    POINTER(FrameWaitInfo),  # frame_wait_info
    POINTER(FrameState),  # frame_state
]

xrBeginFrame = openxr_loader_library.xrBeginFrame
xrBeginFrame.__doc__ = """
    Marks a frame.
"""
xrBeginFrame.restype = Result
xrBeginFrame.argtypes = [
    Session,  # session
    POINTER(FrameBeginInfo),  # frame_begin_info
]

xrEndFrame = openxr_loader_library.xrEndFrame
xrEndFrame.__doc__ = """
    Marks a frame.
"""
xrEndFrame.restype = Result
xrEndFrame.argtypes = [
    Session,  # session
    POINTER(FrameEndInfo),  # frame_end_info
]

xrLocateViews = openxr_loader_library.xrLocateViews
xrLocateViews.__doc__ = """
    Gets view and projection info.
"""
xrLocateViews.restype = Result
xrLocateViews.argtypes = [
    Session,  # session
    POINTER(ViewLocateInfo),  # view_locate_info
    POINTER(ViewState),  # view_state
    c_uint32,  # view_capacity_input
    POINTER(c_uint32),  # view_count_output
    POINTER(View),  # views
]

xrStringToPath = openxr_loader_library.xrStringToPath
xrStringToPath.__doc__ = """
    Converts a string to a semantic path.
"""
xrStringToPath.restype = Result
xrStringToPath.argtypes = [
    Instance,  # instance
    c_char_p,  # path_string
    POINTER(Path),  # path
]

xrPathToString = openxr_loader_library.xrPathToString
xrPathToString.__doc__ = """
    Converts a semantic path to a string.
"""
xrPathToString.restype = Result
xrPathToString.argtypes = [
    Instance,  # instance
    Path,  # path
    c_uint32,  # buffer_capacity_input
    POINTER(c_uint32),  # buffer_count_output
    c_char_p,  # buffer
]

xrCreateActionSet = openxr_loader_library.xrCreateActionSet
xrCreateActionSet.__doc__ = """
    Creates an XrActionSet.
"""
xrCreateActionSet.restype = Result
xrCreateActionSet.argtypes = [
    Instance,  # instance
    POINTER(ActionSetCreateInfo),  # create_info
    POINTER(ActionSet),  # action_set
]

xrDestroyActionSet = openxr_loader_library.xrDestroyActionSet
xrDestroyActionSet.__doc__ = """
    Destroys an XrActionSet.
"""
xrDestroyActionSet.restype = Result
xrDestroyActionSet.argtypes = [
    ActionSet,  # action_set
]

xrCreateAction = openxr_loader_library.xrCreateAction
xrCreateAction.__doc__ = """
    Creates an XrAction.
"""
xrCreateAction.restype = Result
xrCreateAction.argtypes = [
    ActionSet,  # action_set
    POINTER(ActionCreateInfo),  # create_info
    POINTER(Action),  # action
]

xrDestroyAction = openxr_loader_library.xrDestroyAction
xrDestroyAction.__doc__ = """
    Destroys an XrAction.
"""
xrDestroyAction.restype = Result
xrDestroyAction.argtypes = [
    Action,  # action
]

xrSuggestInteractionProfileBindings = openxr_loader_library.xrSuggestInteractionProfileBindings
xrSuggestInteractionProfileBindings.__doc__ = """
    Sets the application-suggested bindings for the interaction
    profile.
"""
xrSuggestInteractionProfileBindings.restype = Result
xrSuggestInteractionProfileBindings.argtypes = [
    Instance,  # instance
    POINTER(InteractionProfileSuggestedBinding),  # suggested_bindings
]

xrAttachSessionActionSets = openxr_loader_library.xrAttachSessionActionSets
xrAttachSessionActionSets.__doc__ = """
    Attaches action sets to a given session.
"""
xrAttachSessionActionSets.restype = Result
xrAttachSessionActionSets.argtypes = [
    Session,  # session
    POINTER(SessionActionSetsAttachInfo),  # attach_info
]

xrGetCurrentInteractionProfile = openxr_loader_library.xrGetCurrentInteractionProfile
xrGetCurrentInteractionProfile.__doc__ = """
    Gets the current interaction profile for a top level user paths.
"""
xrGetCurrentInteractionProfile.restype = Result
xrGetCurrentInteractionProfile.argtypes = [
    Session,  # session
    Path,  # top_level_user_path
    POINTER(InteractionProfileState),  # interaction_profile
]

xrGetActionStateBoolean = openxr_loader_library.xrGetActionStateBoolean
xrGetActionStateBoolean.__doc__ = """
    Gets boolean action state.
"""
xrGetActionStateBoolean.restype = Result
xrGetActionStateBoolean.argtypes = [
    Session,  # session
    POINTER(ActionStateGetInfo),  # get_info
    POINTER(ActionStateBoolean),  # state
]

xrGetActionStateFloat = openxr_loader_library.xrGetActionStateFloat
xrGetActionStateFloat.__doc__ = """
    Gets a floating point action state.
"""
xrGetActionStateFloat.restype = Result
xrGetActionStateFloat.argtypes = [
    Session,  # session
    POINTER(ActionStateGetInfo),  # get_info
    POINTER(ActionStateFloat),  # state
]

xrGetActionStateVector2f = openxr_loader_library.xrGetActionStateVector2f
xrGetActionStateVector2f.__doc__ = """
    Gets 2D float vector action state.
"""
xrGetActionStateVector2f.restype = Result
xrGetActionStateVector2f.argtypes = [
    Session,  # session
    POINTER(ActionStateGetInfo),  # get_info
    POINTER(ActionStateVector2f),  # state
]

xrGetActionStatePose = openxr_loader_library.xrGetActionStatePose
xrGetActionStatePose.__doc__ = """
    Gets metadata from a pose action.
"""
xrGetActionStatePose.restype = Result
xrGetActionStatePose.argtypes = [
    Session,  # session
    POINTER(ActionStateGetInfo),  # get_info
    POINTER(ActionStatePose),  # state
]

xrSyncActions = openxr_loader_library.xrSyncActions
xrSyncActions.__doc__ = """
    Updates the current state of input actions.
"""
xrSyncActions.restype = Result
xrSyncActions.argtypes = [
    Session,  # session
    POINTER(ActionsSyncInfo),  # sync_info
]

xrEnumerateBoundSourcesForAction = openxr_loader_library.xrEnumerateBoundSourcesForAction
xrEnumerateBoundSourcesForAction.__doc__ = """
    Queries the bound input sources for an action.
"""
xrEnumerateBoundSourcesForAction.restype = Result
xrEnumerateBoundSourcesForAction.argtypes = [
    Session,  # session
    POINTER(BoundSourcesForActionEnumerateInfo),  # enumerate_info
    c_uint32,  # source_capacity_input
    POINTER(c_uint32),  # source_count_output
    POINTER(Path),  # sources
]

xrGetInputSourceLocalizedName = openxr_loader_library.xrGetInputSourceLocalizedName
xrGetInputSourceLocalizedName.__doc__ = """
    Gets a localized source name.
"""
xrGetInputSourceLocalizedName.restype = Result
xrGetInputSourceLocalizedName.argtypes = [
    Session,  # session
    POINTER(InputSourceLocalizedNameGetInfo),  # get_info
    c_uint32,  # buffer_capacity_input
    POINTER(c_uint32),  # buffer_count_output
    c_char_p,  # buffer
]

xrApplyHapticFeedback = openxr_loader_library.xrApplyHapticFeedback
xrApplyHapticFeedback.__doc__ = """
    Apply haptic feedback.
"""
xrApplyHapticFeedback.restype = Result
xrApplyHapticFeedback.argtypes = [
    Session,  # session
    POINTER(HapticActionInfo),  # haptic_action_info
    POINTER(HapticBaseHeader),  # haptic_feedback
]

xrStopHapticFeedback = openxr_loader_library.xrStopHapticFeedback
xrStopHapticFeedback.__doc__ = """
    Stop haptic feedback.
"""
xrStopHapticFeedback.restype = Result
xrStopHapticFeedback.argtypes = [
    Session,  # session
    POINTER(HapticActionInfo),  # haptic_action_info
]


__all__ = [
    "xrAcquireSwapchainImage",
    "xrApplyHapticFeedback",
    "xrAttachSessionActionSets",
    "xrBeginFrame",
    "xrBeginSession",
    "xrCreateAction",
    "xrCreateActionSet",
    "xrCreateActionSpace",
    "xrCreateInstance",
    "xrCreateReferenceSpace",
    "xrCreateSession",
    "xrCreateSwapchain",
    "xrDestroyAction",
    "xrDestroyActionSet",
    "xrDestroyInstance",
    "xrDestroySession",
    "xrDestroySpace",
    "xrDestroySwapchain",
    "xrEndFrame",
    "xrEndSession",
    "xrEnumerateApiLayerProperties",
    "xrEnumerateBoundSourcesForAction",
    "xrEnumerateEnvironmentBlendModes",
    "xrEnumerateInstanceExtensionProperties",
    "xrEnumerateReferenceSpaces",
    "xrEnumerateSwapchainFormats",
    "xrEnumerateSwapchainImages",
    "xrEnumerateViewConfigurationViews",
    "xrEnumerateViewConfigurations",
    "xrGetActionStateBoolean",
    "xrGetActionStateFloat",
    "xrGetActionStatePose",
    "xrGetActionStateVector2f",
    "xrGetCurrentInteractionProfile",
    "xrGetInputSourceLocalizedName",
    "xrGetInstanceProcAddr",
    "xrGetInstanceProperties",
    "xrGetReferenceSpaceBoundsRect",
    "xrGetSystem",
    "xrGetSystemProperties",
    "xrGetViewConfigurationProperties",
    "xrLocateSpace",
    "xrLocateViews",
    "xrPathToString",
    "xrPollEvent",
    "xrReleaseSwapchainImage",
    "xrRequestExitSession",
    "xrResultToString",
    "xrStopHapticFeedback",
    "xrStringToPath",
    "xrStructureTypeToString",
    "xrSuggestInteractionProfileBindings",
    "xrSyncActions",
    "xrWaitFrame",
    "xrWaitSwapchainImage",
]
