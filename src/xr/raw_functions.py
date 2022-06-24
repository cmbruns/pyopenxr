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
xrGetInstanceProcAddr.restype = Result
xrGetInstanceProcAddr.argtypes = [
    Instance,  # instance
    c_char_p,  # name
    POINTER(PFN_xrVoidFunction),  # function
]

xrEnumerateApiLayerProperties = openxr_loader_library.xrEnumerateApiLayerProperties
xrEnumerateApiLayerProperties.restype = Result
xrEnumerateApiLayerProperties.argtypes = [
    c_uint32,  # property_capacity_input
    POINTER(c_uint32),  # property_count_output
    POINTER(ApiLayerProperties),  # properties
]

xrEnumerateInstanceExtensionProperties = openxr_loader_library.xrEnumerateInstanceExtensionProperties
xrEnumerateInstanceExtensionProperties.restype = Result
xrEnumerateInstanceExtensionProperties.argtypes = [
    c_char_p,  # layer_name
    c_uint32,  # property_capacity_input
    POINTER(c_uint32),  # property_count_output
    POINTER(ExtensionProperties),  # properties
]

xrCreateInstance = openxr_loader_library.xrCreateInstance
xrCreateInstance.restype = Result
xrCreateInstance.argtypes = [
    POINTER(InstanceCreateInfo),  # create_info
    POINTER(Instance),  # instance
]

xrDestroyInstance = openxr_loader_library.xrDestroyInstance
xrDestroyInstance.restype = Result
xrDestroyInstance.argtypes = [
    Instance,  # instance
]

xrGetInstanceProperties = openxr_loader_library.xrGetInstanceProperties
xrGetInstanceProperties.restype = Result
xrGetInstanceProperties.argtypes = [
    Instance,  # instance
    POINTER(InstanceProperties),  # instance_properties
]

xrPollEvent = openxr_loader_library.xrPollEvent
xrPollEvent.restype = Result
xrPollEvent.argtypes = [
    Instance,  # instance
    POINTER(EventDataBuffer),  # event_data
]

xrResultToString = openxr_loader_library.xrResultToString
xrResultToString.restype = Result
xrResultToString.argtypes = [
    Instance,  # instance
    Result.ctype(),  # value
    (c_char * 64),  # buffer
]

xrStructureTypeToString = openxr_loader_library.xrStructureTypeToString
xrStructureTypeToString.restype = Result
xrStructureTypeToString.argtypes = [
    Instance,  # instance
    StructureType.ctype(),  # value
    (c_char * 64),  # buffer
]

xrGetSystem = openxr_loader_library.xrGetSystem
xrGetSystem.restype = Result
xrGetSystem.argtypes = [
    Instance,  # instance
    POINTER(SystemGetInfo),  # get_info
    POINTER(SystemId),  # system_id
]

xrGetSystemProperties = openxr_loader_library.xrGetSystemProperties
xrGetSystemProperties.restype = Result
xrGetSystemProperties.argtypes = [
    Instance,  # instance
    SystemId,  # system_id
    POINTER(SystemProperties),  # properties
]

xrEnumerateEnvironmentBlendModes = openxr_loader_library.xrEnumerateEnvironmentBlendModes
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
xrCreateSession.restype = Result
xrCreateSession.argtypes = [
    Instance,  # instance
    POINTER(SessionCreateInfo),  # create_info
    POINTER(Session),  # session
]

xrDestroySession = openxr_loader_library.xrDestroySession
xrDestroySession.restype = Result
xrDestroySession.argtypes = [
    Session,  # session
]

xrEnumerateReferenceSpaces = openxr_loader_library.xrEnumerateReferenceSpaces
xrEnumerateReferenceSpaces.restype = Result
xrEnumerateReferenceSpaces.argtypes = [
    Session,  # session
    c_uint32,  # space_capacity_input
    POINTER(c_uint32),  # space_count_output
    POINTER(ReferenceSpaceType.ctype()),  # spaces
]

xrCreateReferenceSpace = openxr_loader_library.xrCreateReferenceSpace
xrCreateReferenceSpace.restype = Result
xrCreateReferenceSpace.argtypes = [
    Session,  # session
    POINTER(ReferenceSpaceCreateInfo),  # create_info
    POINTER(Space),  # space
]

xrGetReferenceSpaceBoundsRect = openxr_loader_library.xrGetReferenceSpaceBoundsRect
xrGetReferenceSpaceBoundsRect.restype = Result
xrGetReferenceSpaceBoundsRect.argtypes = [
    Session,  # session
    ReferenceSpaceType.ctype(),  # reference_space_type
    POINTER(Extent2Df),  # bounds
]

xrCreateActionSpace = openxr_loader_library.xrCreateActionSpace
xrCreateActionSpace.restype = Result
xrCreateActionSpace.argtypes = [
    Session,  # session
    POINTER(ActionSpaceCreateInfo),  # create_info
    POINTER(Space),  # space
]

xrLocateSpace = openxr_loader_library.xrLocateSpace
xrLocateSpace.restype = Result
xrLocateSpace.argtypes = [
    Space,  # space
    Space,  # base_space
    Time,  # time
    POINTER(SpaceLocation),  # location
]

xrDestroySpace = openxr_loader_library.xrDestroySpace
xrDestroySpace.restype = Result
xrDestroySpace.argtypes = [
    Space,  # space
]

xrEnumerateViewConfigurations = openxr_loader_library.xrEnumerateViewConfigurations
xrEnumerateViewConfigurations.restype = Result
xrEnumerateViewConfigurations.argtypes = [
    Instance,  # instance
    SystemId,  # system_id
    c_uint32,  # view_configuration_type_capacity_input
    POINTER(c_uint32),  # view_configuration_type_count_output
    POINTER(ViewConfigurationType.ctype()),  # view_configuration_types
]

xrGetViewConfigurationProperties = openxr_loader_library.xrGetViewConfigurationProperties
xrGetViewConfigurationProperties.restype = Result
xrGetViewConfigurationProperties.argtypes = [
    Instance,  # instance
    SystemId,  # system_id
    ViewConfigurationType.ctype(),  # view_configuration_type
    POINTER(ViewConfigurationProperties),  # configuration_properties
]

xrEnumerateViewConfigurationViews = openxr_loader_library.xrEnumerateViewConfigurationViews
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
xrEnumerateSwapchainFormats.restype = Result
xrEnumerateSwapchainFormats.argtypes = [
    Session,  # session
    c_uint32,  # format_capacity_input
    POINTER(c_uint32),  # format_count_output
    POINTER(c_int64),  # formats
]

xrCreateSwapchain = openxr_loader_library.xrCreateSwapchain
xrCreateSwapchain.restype = Result
xrCreateSwapchain.argtypes = [
    Session,  # session
    POINTER(SwapchainCreateInfo),  # create_info
    POINTER(Swapchain),  # swapchain
]

xrDestroySwapchain = openxr_loader_library.xrDestroySwapchain
xrDestroySwapchain.restype = Result
xrDestroySwapchain.argtypes = [
    Swapchain,  # swapchain
]

xrEnumerateSwapchainImages = openxr_loader_library.xrEnumerateSwapchainImages
xrEnumerateSwapchainImages.restype = Result
xrEnumerateSwapchainImages.argtypes = [
    Swapchain,  # swapchain
    c_uint32,  # image_capacity_input
    POINTER(c_uint32),  # image_count_output
    POINTER(SwapchainImageBaseHeader),  # images
]

xrAcquireSwapchainImage = openxr_loader_library.xrAcquireSwapchainImage
xrAcquireSwapchainImage.restype = Result
xrAcquireSwapchainImage.argtypes = [
    Swapchain,  # swapchain
    POINTER(SwapchainImageAcquireInfo),  # acquire_info
    POINTER(c_uint32),  # index
]

xrWaitSwapchainImage = openxr_loader_library.xrWaitSwapchainImage
xrWaitSwapchainImage.restype = Result
xrWaitSwapchainImage.argtypes = [
    Swapchain,  # swapchain
    POINTER(SwapchainImageWaitInfo),  # wait_info
]

xrReleaseSwapchainImage = openxr_loader_library.xrReleaseSwapchainImage
xrReleaseSwapchainImage.restype = Result
xrReleaseSwapchainImage.argtypes = [
    Swapchain,  # swapchain
    POINTER(SwapchainImageReleaseInfo),  # release_info
]

xrBeginSession = openxr_loader_library.xrBeginSession
xrBeginSession.restype = Result
xrBeginSession.argtypes = [
    Session,  # session
    POINTER(SessionBeginInfo),  # begin_info
]

xrEndSession = openxr_loader_library.xrEndSession
xrEndSession.restype = Result
xrEndSession.argtypes = [
    Session,  # session
]

xrRequestExitSession = openxr_loader_library.xrRequestExitSession
xrRequestExitSession.restype = Result
xrRequestExitSession.argtypes = [
    Session,  # session
]

xrWaitFrame = openxr_loader_library.xrWaitFrame
xrWaitFrame.restype = Result
xrWaitFrame.argtypes = [
    Session,  # session
    POINTER(FrameWaitInfo),  # frame_wait_info
    POINTER(FrameState),  # frame_state
]

xrBeginFrame = openxr_loader_library.xrBeginFrame
xrBeginFrame.restype = Result
xrBeginFrame.argtypes = [
    Session,  # session
    POINTER(FrameBeginInfo),  # frame_begin_info
]

xrEndFrame = openxr_loader_library.xrEndFrame
xrEndFrame.restype = Result
xrEndFrame.argtypes = [
    Session,  # session
    POINTER(FrameEndInfo),  # frame_end_info
]

xrLocateViews = openxr_loader_library.xrLocateViews
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
xrStringToPath.restype = Result
xrStringToPath.argtypes = [
    Instance,  # instance
    c_char_p,  # path_string
    POINTER(Path),  # path
]

xrPathToString = openxr_loader_library.xrPathToString
xrPathToString.restype = Result
xrPathToString.argtypes = [
    Instance,  # instance
    Path,  # path
    c_uint32,  # buffer_capacity_input
    POINTER(c_uint32),  # buffer_count_output
    c_char_p,  # buffer
]

xrCreateActionSet = openxr_loader_library.xrCreateActionSet
xrCreateActionSet.restype = Result
xrCreateActionSet.argtypes = [
    Instance,  # instance
    POINTER(ActionSetCreateInfo),  # create_info
    POINTER(ActionSet),  # action_set
]

xrDestroyActionSet = openxr_loader_library.xrDestroyActionSet
xrDestroyActionSet.restype = Result
xrDestroyActionSet.argtypes = [
    ActionSet,  # action_set
]

xrCreateAction = openxr_loader_library.xrCreateAction
xrCreateAction.restype = Result
xrCreateAction.argtypes = [
    ActionSet,  # action_set
    POINTER(ActionCreateInfo),  # create_info
    POINTER(Action),  # action
]

xrDestroyAction = openxr_loader_library.xrDestroyAction
xrDestroyAction.restype = Result
xrDestroyAction.argtypes = [
    Action,  # action
]

xrSuggestInteractionProfileBindings = openxr_loader_library.xrSuggestInteractionProfileBindings
xrSuggestInteractionProfileBindings.restype = Result
xrSuggestInteractionProfileBindings.argtypes = [
    Instance,  # instance
    POINTER(InteractionProfileSuggestedBinding),  # suggested_bindings
]

xrAttachSessionActionSets = openxr_loader_library.xrAttachSessionActionSets
xrAttachSessionActionSets.restype = Result
xrAttachSessionActionSets.argtypes = [
    Session,  # session
    POINTER(SessionActionSetsAttachInfo),  # attach_info
]

xrGetCurrentInteractionProfile = openxr_loader_library.xrGetCurrentInteractionProfile
xrGetCurrentInteractionProfile.restype = Result
xrGetCurrentInteractionProfile.argtypes = [
    Session,  # session
    Path,  # top_level_user_path
    POINTER(InteractionProfileState),  # interaction_profile
]

xrGetActionStateBoolean = openxr_loader_library.xrGetActionStateBoolean
xrGetActionStateBoolean.restype = Result
xrGetActionStateBoolean.argtypes = [
    Session,  # session
    POINTER(ActionStateGetInfo),  # get_info
    POINTER(ActionStateBoolean),  # state
]

xrGetActionStateFloat = openxr_loader_library.xrGetActionStateFloat
xrGetActionStateFloat.restype = Result
xrGetActionStateFloat.argtypes = [
    Session,  # session
    POINTER(ActionStateGetInfo),  # get_info
    POINTER(ActionStateFloat),  # state
]

xrGetActionStateVector2f = openxr_loader_library.xrGetActionStateVector2f
xrGetActionStateVector2f.restype = Result
xrGetActionStateVector2f.argtypes = [
    Session,  # session
    POINTER(ActionStateGetInfo),  # get_info
    POINTER(ActionStateVector2f),  # state
]

xrGetActionStatePose = openxr_loader_library.xrGetActionStatePose
xrGetActionStatePose.restype = Result
xrGetActionStatePose.argtypes = [
    Session,  # session
    POINTER(ActionStateGetInfo),  # get_info
    POINTER(ActionStatePose),  # state
]

xrSyncActions = openxr_loader_library.xrSyncActions
xrSyncActions.restype = Result
xrSyncActions.argtypes = [
    Session,  # session
    POINTER(ActionsSyncInfo),  # sync_info
]

xrEnumerateBoundSourcesForAction = openxr_loader_library.xrEnumerateBoundSourcesForAction
xrEnumerateBoundSourcesForAction.restype = Result
xrEnumerateBoundSourcesForAction.argtypes = [
    Session,  # session
    POINTER(BoundSourcesForActionEnumerateInfo),  # enumerate_info
    c_uint32,  # source_capacity_input
    POINTER(c_uint32),  # source_count_output
    POINTER(Path),  # sources
]

xrGetInputSourceLocalizedName = openxr_loader_library.xrGetInputSourceLocalizedName
xrGetInputSourceLocalizedName.restype = Result
xrGetInputSourceLocalizedName.argtypes = [
    Session,  # session
    POINTER(InputSourceLocalizedNameGetInfo),  # get_info
    c_uint32,  # buffer_capacity_input
    POINTER(c_uint32),  # buffer_count_output
    c_char_p,  # buffer
]

xrApplyHapticFeedback = openxr_loader_library.xrApplyHapticFeedback
xrApplyHapticFeedback.restype = Result
xrApplyHapticFeedback.argtypes = [
    Session,  # session
    POINTER(HapticActionInfo),  # haptic_action_info
    POINTER(HapticBaseHeader),  # haptic_feedback
]

xrStopHapticFeedback = openxr_loader_library.xrStopHapticFeedback
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
