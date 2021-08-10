# Warning: this file is auto-generated. Do not edit.

from ctypes import CFUNCTYPE, POINTER, Structure, c_char, c_char_p, c_float, c_int, c_int32, c_int64, c_uint16, c_uint32, c_uint64, c_uint8, c_void_p

# Enum aliases (not exposed in __all__)
Result = c_int
StructureType = c_int
FormFactor = c_int
ViewConfigurationType = c_int
EnvironmentBlendMode = c_int
ReferenceSpaceType = c_int
ActionType = c_int
EyeVisibility = c_int
SessionState = c_int
ObjectType = c_int
VisibilityMaskTypeKHR = c_int
PerfSettingsDomainEXT = c_int
PerfSettingsSubDomainEXT = c_int
PerfSettingsLevelEXT = c_int
PerfSettingsNotificationLevelEXT = c_int
BlendFactorFB = c_int
SpatialGraphNodeTypeMSFT = c_int
HandEXT = c_int
HandJointEXT = c_int
HandJointSetEXT = c_int
HandPoseTypeMSFT = c_int
ReprojectionModeMSFT = c_int
HandJointsMotionRangeEXT = c_int
SceneComputeFeatureMSFT = c_int
SceneComputeConsistencyMSFT = c_int
MeshComputeLodMSFT = c_int
SceneComponentTypeMSFT = c_int
SceneObjectTypeMSFT = c_int
ScenePlaneAlignmentTypeMSFT = c_int
SceneComputeStateMSFT = c_int
ColorSpaceFB = c_int
FoveationLevelFB = c_int
FoveationDynamicFB = c_int

Version = c_uint64

Flags64 = c_uint64

SystemId = c_uint64

Bool32 = c_uint32

Path = c_uint64

Time = c_int64

Duration = c_int64


class Instance_T(Structure):
    pass


Instance = POINTER(Instance_T)


class Session_T(Structure):
    pass


Session = POINTER(Session_T)


class Space_T(Structure):
    pass


Space = POINTER(Space_T)


class Action_T(Structure):
    pass


Action = POINTER(Action_T)


class Swapchain_T(Structure):
    pass


Swapchain = POINTER(Swapchain_T)


class ActionSet_T(Structure):
    pass


ActionSet = POINTER(ActionSet_T)

InstanceCreateFlags = Flags64

SessionCreateFlags = Flags64

SpaceVelocityFlags = Flags64

SpaceLocationFlags = Flags64

SwapchainCreateFlags = Flags64

SwapchainUsageFlags = Flags64

CompositionLayerFlags = Flags64

ViewStateFlags = Flags64

InputSourceLocalizedNameFlags = Flags64

PFN_xrVoidFunction = CFUNCTYPE(None)


class ApiLayerProperties(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("layer_name", (c_char * 256)),
        ("spec_version", Version),
        ("layer_version", c_uint32),
        ("description", (c_char * 256)),
    ]


class ExtensionProperties(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("extension_name", (c_char * 128)),
        ("extension_version", c_uint32),
    ]


class ApplicationInfo(Structure):
    _fields_ = [
        ("application_name", (c_char * 128)),
        ("application_version", c_uint32),
        ("engine_name", (c_char * 128)),
        ("engine_version", c_uint32),
        ("api_version", Version),
    ]


class InstanceCreateInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("create_flags", InstanceCreateFlags),
        ("application_info", ApplicationInfo),
        ("enabled_api_layer_count", c_uint32),
        ("enabled_api_layer_names", POINTER(c_char_p)),
        ("enabled_extension_count", c_uint32),
        ("enabled_extension_names", POINTER(c_char_p)),
    ]


class InstanceProperties(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("runtime_version", Version),
        ("runtime_name", (c_char * 128)),
    ]


class EventDataBuffer(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("varying", (c_uint8 * 4000)),
    ]


class SystemGetInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("form_factor", FormFactor),
    ]


class SystemGraphicsProperties(Structure):
    _fields_ = [
        ("max_swapchain_image_height", c_uint32),
        ("max_swapchain_image_width", c_uint32),
        ("max_layer_count", c_uint32),
    ]


class SystemTrackingProperties(Structure):
    _fields_ = [
        ("orientation_tracking", Bool32),
        ("position_tracking", Bool32),
    ]


class SystemProperties(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("system_id", SystemId),
        ("vendor_id", c_uint32),
        ("system_name", (c_char * 256)),
        ("graphics_properties", SystemGraphicsProperties),
        ("tracking_properties", SystemTrackingProperties),
    ]


class SessionCreateInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("create_flags", SessionCreateFlags),
        ("system_id", SystemId),
    ]


class Vector3f(Structure):
    _fields_ = [
        ("x", c_float),
        ("y", c_float),
        ("z", c_float),
    ]


class SpaceVelocity(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("velocity_flags", SpaceVelocityFlags),
        ("linear_velocity", Vector3f),
        ("angular_velocity", Vector3f),
    ]


class Quaternionf(Structure):
    _fields_ = [
        ("x", c_float),
        ("y", c_float),
        ("z", c_float),
        ("w", c_float),
    ]


class Posef(Structure):
    _fields_ = [
        ("orientation", Quaternionf),
        ("position", Vector3f),
    ]


class ReferenceSpaceCreateInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("reference_space_type", ReferenceSpaceType),
        ("pose_in_reference_space", Posef),
    ]


class Extent2Df(Structure):
    _fields_ = [
        ("width", c_float),
        ("height", c_float),
    ]


class ActionSpaceCreateInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("action", Action),
        ("subaction_path", Path),
        ("pose_in_action_space", Posef),
    ]


class SpaceLocation(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("location_flags", SpaceLocationFlags),
        ("pose", Posef),
    ]


class ViewConfigurationProperties(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("view_configuration_type", ViewConfigurationType),
        ("fov_mutable", Bool32),
    ]


class ViewConfigurationView(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("recommended_image_rect_width", c_uint32),
        ("max_image_rect_width", c_uint32),
        ("recommended_image_rect_height", c_uint32),
        ("max_image_rect_height", c_uint32),
        ("recommended_swapchain_sample_count", c_uint32),
        ("max_swapchain_sample_count", c_uint32),
    ]


class SwapchainCreateInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("create_flags", SwapchainCreateFlags),
        ("usage_flags", SwapchainUsageFlags),
        ("format", c_int64),
        ("sample_count", c_uint32),
        ("width", c_uint32),
        ("height", c_uint32),
        ("face_count", c_uint32),
        ("array_size", c_uint32),
        ("mip_count", c_uint32),
    ]


class SwapchainImageBaseHeader(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
    ]


class SwapchainImageAcquireInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
    ]


class SwapchainImageWaitInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("timeout", Duration),
    ]


class SwapchainImageReleaseInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
    ]


class SessionBeginInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("primary_view_configuration_type", ViewConfigurationType),
    ]


class FrameWaitInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
    ]


class FrameState(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("predicted_display_time", Time),
        ("predicted_display_period", Duration),
        ("should_render", Bool32),
    ]


class FrameBeginInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
    ]


class CompositionLayerBaseHeader(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlags),
        ("space", Space),
    ]


class FrameEndInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("display_time", Time),
        ("environment_blend_mode", EnvironmentBlendMode),
        ("layer_count", c_uint32),
        ("layers", POINTER(POINTER(CompositionLayerBaseHeader))),
    ]


class ViewLocateInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("view_configuration_type", ViewConfigurationType),
        ("display_time", Time),
        ("space", Space),
    ]


class ViewState(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("view_state_flags", ViewStateFlags),
    ]


class Fovf(Structure):
    _fields_ = [
        ("angle_left", c_float),
        ("angle_right", c_float),
        ("angle_up", c_float),
        ("angle_down", c_float),
    ]


class View(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("pose", Posef),
        ("fov", Fovf),
    ]


class ActionSetCreateInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("action_set_name", (c_char * 64)),
        ("localized_action_set_name", (c_char * 128)),
        ("priority", c_uint32),
    ]


class ActionCreateInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("action_name", (c_char * 64)),
        ("action_type", ActionType),
        ("count_subaction_paths", c_uint32),
        ("subaction_paths", POINTER(Path)),
        ("localized_action_name", (c_char * 128)),
    ]


class ActionSuggestedBinding(Structure):
    _fields_ = [
        ("action", Action),
        ("binding", Path),
    ]


class InteractionProfileSuggestedBinding(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("interaction_profile", Path),
        ("count_suggested_bindings", c_uint32),
        ("suggested_bindings", POINTER(ActionSuggestedBinding)),
    ]


class SessionActionSetsAttachInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("count_action_sets", c_uint32),
        ("action_sets", POINTER(ActionSet)),
    ]


class InteractionProfileState(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("interaction_profile", Path),
    ]


class ActionStateGetInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("action", Action),
        ("subaction_path", Path),
    ]


class ActionStateBoolean(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("current_state", Bool32),
        ("changed_since_last_sync", Bool32),
        ("last_change_time", Time),
        ("is_active", Bool32),
    ]


class ActionStateFloat(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("current_state", c_float),
        ("changed_since_last_sync", Bool32),
        ("last_change_time", Time),
        ("is_active", Bool32),
    ]


class Vector2f(Structure):
    _fields_ = [
        ("x", c_float),
        ("y", c_float),
    ]


class ActionStateVector2f(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("current_state", Vector2f),
        ("changed_since_last_sync", Bool32),
        ("last_change_time", Time),
        ("is_active", Bool32),
    ]


class ActionStatePose(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("is_active", Bool32),
    ]


class ActiveActionSet(Structure):
    _fields_ = [
        ("action_set", ActionSet),
        ("subaction_path", Path),
    ]


class ActionsSyncInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("count_active_action_sets", c_uint32),
        ("active_action_sets", POINTER(ActiveActionSet)),
    ]


class BoundSourcesForActionEnumerateInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("action", Action),
    ]


class InputSourceLocalizedNameGetInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("source_path", Path),
        ("which_components", InputSourceLocalizedNameFlags),
    ]


class HapticActionInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("action", Action),
        ("subaction_path", Path),
    ]


class HapticBaseHeader(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
    ]


class BaseInStructure(Structure):
    pass


BaseInStructure._fields_ = [
        ("type", StructureType),
        ("next", POINTER(BaseInStructure)),
    ]


class BaseOutStructure(Structure):
    pass


BaseOutStructure._fields_ = [
        ("type", StructureType),
        ("next", POINTER(BaseOutStructure)),
    ]


class Offset2Di(Structure):
    _fields_ = [
        ("x", c_int32),
        ("y", c_int32),
    ]


class Extent2Di(Structure):
    _fields_ = [
        ("width", c_int32),
        ("height", c_int32),
    ]


class Rect2Di(Structure):
    _fields_ = [
        ("offset", Offset2Di),
        ("extent", Extent2Di),
    ]


class SwapchainSubImage(Structure):
    _fields_ = [
        ("swapchain", Swapchain),
        ("image_rect", Rect2Di),
        ("image_array_index", c_uint32),
    ]


class CompositionLayerProjectionView(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("pose", Posef),
        ("fov", Fovf),
        ("sub_image", SwapchainSubImage),
    ]


class CompositionLayerProjection(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlags),
        ("space", Space),
        ("view_count", c_uint32),
        ("views", POINTER(CompositionLayerProjectionView)),
    ]


class CompositionLayerQuad(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlags),
        ("space", Space),
        ("eye_visibility", EyeVisibility),
        ("sub_image", SwapchainSubImage),
        ("pose", Posef),
        ("size", Extent2Df),
    ]


class EventDataBaseHeader(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
    ]


class EventDataEventsLost(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("lost_event_count", c_uint32),
    ]


class EventDataInstanceLossPending(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("loss_time", Time),
    ]


class EventDataSessionStateChanged(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("session", Session),
        ("state", SessionState),
        ("time", Time),
    ]


class EventDataReferenceSpaceChangePending(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("session", Session),
        ("reference_space_type", ReferenceSpaceType),
        ("change_time", Time),
        ("pose_valid", Bool32),
        ("pose_in_previous_space", Posef),
    ]


class EventDataInteractionProfileChanged(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("session", Session),
    ]


class HapticVibration(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("duration", Duration),
        ("frequency", c_float),
        ("amplitude", c_float),
    ]


class Offset2Df(Structure):
    _fields_ = [
        ("x", c_float),
        ("y", c_float),
    ]


class Rect2Df(Structure):
    _fields_ = [
        ("offset", Offset2Df),
        ("extent", Extent2Df),
    ]


class Vector4f(Structure):
    _fields_ = [
        ("x", c_float),
        ("y", c_float),
        ("z", c_float),
        ("w", c_float),
    ]


class Color4f(Structure):
    _fields_ = [
        ("r", c_float),
        ("g", c_float),
        ("b", c_float),
        ("a", c_float),
    ]


PFN_xrGetInstanceProcAddr = CFUNCTYPE(Result, Instance, c_char_p, POINTER(PFN_xrVoidFunction))

PFN_xrEnumerateApiLayerProperties = CFUNCTYPE(Result, c_uint32, POINTER(c_uint32), POINTER(ApiLayerProperties))

PFN_xrEnumerateInstanceExtensionProperties = CFUNCTYPE(Result, c_char_p, c_uint32, POINTER(c_uint32), POINTER(ExtensionProperties))

PFN_xrCreateInstance = CFUNCTYPE(Result, POINTER(InstanceCreateInfo), POINTER(Instance))

PFN_xrDestroyInstance = CFUNCTYPE(Result, Instance)

PFN_xrGetInstanceProperties = CFUNCTYPE(Result, Instance, POINTER(InstanceProperties))

PFN_xrPollEvent = CFUNCTYPE(Result, Instance, POINTER(EventDataBuffer))

PFN_xrResultToString = CFUNCTYPE(Result, Instance, Result, (c_char * 64))

PFN_xrStructureTypeToString = CFUNCTYPE(Result, Instance, StructureType, (c_char * 64))

PFN_xrGetSystem = CFUNCTYPE(Result, Instance, POINTER(SystemGetInfo), POINTER(SystemId))

PFN_xrGetSystemProperties = CFUNCTYPE(Result, Instance, SystemId, POINTER(SystemProperties))

PFN_xrEnumerateEnvironmentBlendModes = CFUNCTYPE(Result, Instance, SystemId, ViewConfigurationType, c_uint32, POINTER(c_uint32), POINTER(EnvironmentBlendMode))

PFN_xrCreateSession = CFUNCTYPE(Result, Instance, POINTER(SessionCreateInfo), POINTER(Session))

PFN_xrDestroySession = CFUNCTYPE(Result, Session)

PFN_xrEnumerateReferenceSpaces = CFUNCTYPE(Result, Session, c_uint32, POINTER(c_uint32), POINTER(ReferenceSpaceType))

PFN_xrCreateReferenceSpace = CFUNCTYPE(Result, Session, POINTER(ReferenceSpaceCreateInfo), POINTER(Space))

PFN_xrGetReferenceSpaceBoundsRect = CFUNCTYPE(Result, Session, ReferenceSpaceType, POINTER(Extent2Df))

PFN_xrCreateActionSpace = CFUNCTYPE(Result, Session, POINTER(ActionSpaceCreateInfo), POINTER(Space))

PFN_xrLocateSpace = CFUNCTYPE(Result, Space, Space, Time, POINTER(SpaceLocation))

PFN_xrDestroySpace = CFUNCTYPE(Result, Space)

PFN_xrEnumerateViewConfigurations = CFUNCTYPE(Result, Instance, SystemId, c_uint32, POINTER(c_uint32), POINTER(ViewConfigurationType))

PFN_xrGetViewConfigurationProperties = CFUNCTYPE(Result, Instance, SystemId, ViewConfigurationType, POINTER(ViewConfigurationProperties))

PFN_xrEnumerateViewConfigurationViews = CFUNCTYPE(Result, Instance, SystemId, ViewConfigurationType, c_uint32, POINTER(c_uint32), POINTER(ViewConfigurationView))

PFN_xrEnumerateSwapchainFormats = CFUNCTYPE(Result, Session, c_uint32, POINTER(c_uint32), POINTER(c_int64))

PFN_xrCreateSwapchain = CFUNCTYPE(Result, Session, POINTER(SwapchainCreateInfo), POINTER(Swapchain))

PFN_xrDestroySwapchain = CFUNCTYPE(Result, Swapchain)

PFN_xrEnumerateSwapchainImages = CFUNCTYPE(Result, Swapchain, c_uint32, POINTER(c_uint32), POINTER(SwapchainImageBaseHeader))

PFN_xrAcquireSwapchainImage = CFUNCTYPE(Result, Swapchain, POINTER(SwapchainImageAcquireInfo), POINTER(c_uint32))

PFN_xrWaitSwapchainImage = CFUNCTYPE(Result, Swapchain, POINTER(SwapchainImageWaitInfo))

PFN_xrReleaseSwapchainImage = CFUNCTYPE(Result, Swapchain, POINTER(SwapchainImageReleaseInfo))

PFN_xrBeginSession = CFUNCTYPE(Result, Session, POINTER(SessionBeginInfo))

PFN_xrEndSession = CFUNCTYPE(Result, Session)

PFN_xrRequestExitSession = CFUNCTYPE(Result, Session)

PFN_xrWaitFrame = CFUNCTYPE(Result, Session, POINTER(FrameWaitInfo), POINTER(FrameState))

PFN_xrBeginFrame = CFUNCTYPE(Result, Session, POINTER(FrameBeginInfo))

PFN_xrEndFrame = CFUNCTYPE(Result, Session, POINTER(FrameEndInfo))

PFN_xrLocateViews = CFUNCTYPE(Result, Session, POINTER(ViewLocateInfo), POINTER(ViewState), c_uint32, POINTER(c_uint32), POINTER(View))

PFN_xrStringToPath = CFUNCTYPE(Result, Instance, c_char_p, POINTER(Path))

PFN_xrPathToString = CFUNCTYPE(Result, Instance, Path, c_uint32, POINTER(c_uint32), c_char_p)

PFN_xrCreateActionSet = CFUNCTYPE(Result, Instance, POINTER(ActionSetCreateInfo), POINTER(ActionSet))

PFN_xrDestroyActionSet = CFUNCTYPE(Result, ActionSet)

PFN_xrCreateAction = CFUNCTYPE(Result, ActionSet, POINTER(ActionCreateInfo), POINTER(Action))

PFN_xrDestroyAction = CFUNCTYPE(Result, Action)

PFN_xrSuggestInteractionProfileBindings = CFUNCTYPE(Result, Instance, POINTER(InteractionProfileSuggestedBinding))

PFN_xrAttachSessionActionSets = CFUNCTYPE(Result, Session, POINTER(SessionActionSetsAttachInfo))

PFN_xrGetCurrentInteractionProfile = CFUNCTYPE(Result, Session, Path, POINTER(InteractionProfileState))

PFN_xrGetActionStateBoolean = CFUNCTYPE(Result, Session, POINTER(ActionStateGetInfo), POINTER(ActionStateBoolean))

PFN_xrGetActionStateFloat = CFUNCTYPE(Result, Session, POINTER(ActionStateGetInfo), POINTER(ActionStateFloat))

PFN_xrGetActionStateVector2f = CFUNCTYPE(Result, Session, POINTER(ActionStateGetInfo), POINTER(ActionStateVector2f))

PFN_xrGetActionStatePose = CFUNCTYPE(Result, Session, POINTER(ActionStateGetInfo), POINTER(ActionStatePose))

PFN_xrSyncActions = CFUNCTYPE(Result, Session, POINTER(ActionsSyncInfo))

PFN_xrEnumerateBoundSourcesForAction = CFUNCTYPE(Result, Session, POINTER(BoundSourcesForActionEnumerateInfo), c_uint32, POINTER(c_uint32), POINTER(Path))

PFN_xrGetInputSourceLocalizedName = CFUNCTYPE(Result, Session, POINTER(InputSourceLocalizedNameGetInfo), c_uint32, POINTER(c_uint32), c_char_p)

PFN_xrApplyHapticFeedback = CFUNCTYPE(Result, Session, POINTER(HapticActionInfo), POINTER(HapticBaseHeader))

PFN_xrStopHapticFeedback = CFUNCTYPE(Result, Session, POINTER(HapticActionInfo))


class CompositionLayerCubeKHR(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlags),
        ("space", Space),
        ("eye_visibility", EyeVisibility),
        ("swapchain", Swapchain),
        ("image_array_index", c_uint32),
        ("orientation", Quaternionf),
    ]


class CompositionLayerDepthInfoKHR(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("sub_image", SwapchainSubImage),
        ("min_depth", c_float),
        ("max_depth", c_float),
        ("near_z", c_float),
        ("far_z", c_float),
    ]


class CompositionLayerCylinderKHR(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlags),
        ("space", Space),
        ("eye_visibility", EyeVisibility),
        ("sub_image", SwapchainSubImage),
        ("pose", Posef),
        ("radius", c_float),
        ("central_angle", c_float),
        ("aspect_ratio", c_float),
    ]


class CompositionLayerEquirectKHR(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlags),
        ("space", Space),
        ("eye_visibility", EyeVisibility),
        ("sub_image", SwapchainSubImage),
        ("pose", Posef),
        ("radius", c_float),
        ("scale", Vector2f),
        ("bias", Vector2f),
    ]


class VisibilityMaskKHR(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("vertex_capacity_input", c_uint32),
        ("vertex_count_output", c_uint32),
        ("vertices", POINTER(Vector2f)),
        ("index_capacity_input", c_uint32),
        ("index_count_output", c_uint32),
        ("indices", POINTER(c_uint32)),
    ]


class EventDataVisibilityMaskChangedKHR(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("session", Session),
        ("view_configuration_type", ViewConfigurationType),
        ("view_index", c_uint32),
    ]


PFN_xrGetVisibilityMaskKHR = CFUNCTYPE(Result, Session, ViewConfigurationType, c_uint32, VisibilityMaskTypeKHR, POINTER(VisibilityMaskKHR))


class CompositionLayerColorScaleBiasKHR(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("color_scale", Color4f),
        ("color_bias", Color4f),
    ]


class LoaderInitInfoBaseHeaderKHR(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
    ]


PFN_xrInitializeLoaderKHR = CFUNCTYPE(Result, POINTER(LoaderInitInfoBaseHeaderKHR))


class CompositionLayerEquirect2KHR(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlags),
        ("space", Space),
        ("eye_visibility", EyeVisibility),
        ("sub_image", SwapchainSubImage),
        ("pose", Posef),
        ("radius", c_float),
        ("central_horizontal_angle", c_float),
        ("upper_vertical_angle", c_float),
        ("lower_vertical_angle", c_float),
    ]


class BindingModificationBaseHeaderKHR(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
    ]


class BindingModificationsKHR(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("binding_modification_count", c_uint32),
        ("binding_modifications", POINTER(POINTER(BindingModificationBaseHeaderKHR))),
    ]


class EventDataPerfSettingsEXT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("domain", PerfSettingsDomainEXT),
        ("sub_domain", PerfSettingsSubDomainEXT),
        ("from_level", PerfSettingsNotificationLevelEXT),
        ("to_level", PerfSettingsNotificationLevelEXT),
    ]


PFN_xrPerfSettingsSetPerformanceLevelEXT = CFUNCTYPE(Result, Session, PerfSettingsDomainEXT, PerfSettingsLevelEXT)

PFN_xrThermalGetTemperatureTrendEXT = CFUNCTYPE(Result, Session, PerfSettingsDomainEXT, POINTER(PerfSettingsNotificationLevelEXT), POINTER(c_float), POINTER(c_float))


class DebugUtilsMessengerEXT_T(Structure):
    pass


DebugUtilsMessengerEXT = POINTER(DebugUtilsMessengerEXT_T)

DebugUtilsMessageSeverityFlagsEXT = Flags64

DebugUtilsMessageTypeFlagsEXT = Flags64


class DebugUtilsObjectNameInfoEXT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("object_type", ObjectType),
        ("object_handle", c_uint64),
        ("object_name", c_char_p),
    ]


class DebugUtilsLabelEXT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("label_name", c_char_p),
    ]


class DebugUtilsMessengerCallbackDataEXT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("message_id", c_char_p),
        ("function_name", c_char_p),
        ("message", c_char_p),
        ("object_count", c_uint32),
        ("objects", POINTER(DebugUtilsObjectNameInfoEXT)),
        ("session_label_count", c_uint32),
        ("session_labels", POINTER(DebugUtilsLabelEXT)),
    ]


PFN_xrDebugUtilsMessengerCallbackEXT = CFUNCTYPE(Bool32, DebugUtilsMessageSeverityFlagsEXT, DebugUtilsMessageTypeFlagsEXT, POINTER(DebugUtilsMessengerCallbackDataEXT), c_void_p)


class DebugUtilsMessengerCreateInfoEXT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("message_severities", DebugUtilsMessageSeverityFlagsEXT),
        ("message_types", DebugUtilsMessageTypeFlagsEXT),
        ("user_callback", PFN_xrDebugUtilsMessengerCallbackEXT),
        ("user_data", c_void_p),
    ]


PFN_xrSetDebugUtilsObjectNameEXT = CFUNCTYPE(Result, Instance, POINTER(DebugUtilsObjectNameInfoEXT))

PFN_xrCreateDebugUtilsMessengerEXT = CFUNCTYPE(Result, Instance, POINTER(DebugUtilsMessengerCreateInfoEXT), POINTER(DebugUtilsMessengerEXT))

PFN_xrDestroyDebugUtilsMessengerEXT = CFUNCTYPE(Result, DebugUtilsMessengerEXT)

PFN_xrSubmitDebugUtilsMessageEXT = CFUNCTYPE(Result, Instance, DebugUtilsMessageSeverityFlagsEXT, DebugUtilsMessageTypeFlagsEXT, POINTER(DebugUtilsMessengerCallbackDataEXT))

PFN_xrSessionBeginDebugUtilsLabelRegionEXT = CFUNCTYPE(Result, Session, POINTER(DebugUtilsLabelEXT))

PFN_xrSessionEndDebugUtilsLabelRegionEXT = CFUNCTYPE(Result, Session)

PFN_xrSessionInsertDebugUtilsLabelEXT = CFUNCTYPE(Result, Session, POINTER(DebugUtilsLabelEXT))


class SystemEyeGazeInteractionPropertiesEXT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("supports_eye_gaze_interaction", Bool32),
    ]


class EyeGazeSampleTimeEXT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("time", Time),
    ]


OverlaySessionCreateFlagsEXTX = Flags64

OverlayMainSessionFlagsEXTX = Flags64


class SessionCreateInfoOverlayEXTX(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("create_flags", OverlaySessionCreateFlagsEXTX),
        ("session_layers_placement", c_uint32),
    ]


class EventDataMainSessionVisibilityChangedEXTX(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("visible", Bool32),
        ("flags", OverlayMainSessionFlagsEXTX),
    ]


class SpatialAnchorMSFT_T(Structure):
    pass


SpatialAnchorMSFT = POINTER(SpatialAnchorMSFT_T)


class SpatialAnchorCreateInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("space", Space),
        ("pose", Posef),
        ("time", Time),
    ]


class SpatialAnchorSpaceCreateInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("anchor", SpatialAnchorMSFT),
        ("pose_in_anchor_space", Posef),
    ]


PFN_xrCreateSpatialAnchorMSFT = CFUNCTYPE(Result, Session, POINTER(SpatialAnchorCreateInfoMSFT), POINTER(SpatialAnchorMSFT))

PFN_xrCreateSpatialAnchorSpaceMSFT = CFUNCTYPE(Result, Session, POINTER(SpatialAnchorSpaceCreateInfoMSFT), POINTER(Space))

PFN_xrDestroySpatialAnchorMSFT = CFUNCTYPE(Result, SpatialAnchorMSFT)

CompositionLayerImageLayoutFlagsFB = Flags64


class CompositionLayerImageLayoutFB(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("flags", CompositionLayerImageLayoutFlagsFB),
    ]


class CompositionLayerAlphaBlendFB(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("src_factor_color", BlendFactorFB),
        ("dst_factor_color", BlendFactorFB),
        ("src_factor_alpha", BlendFactorFB),
        ("dst_factor_alpha", BlendFactorFB),
    ]


class ViewConfigurationDepthRangeEXT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("recommended_near_z", c_float),
        ("min_near_z", c_float),
        ("recommended_far_z", c_float),
        ("max_far_z", c_float),
    ]


PFN_xrSetInputDeviceActiveEXT = CFUNCTYPE(Result, Session, Path, Path, Bool32)

PFN_xrSetInputDeviceStateBoolEXT = CFUNCTYPE(Result, Session, Path, Path, Bool32)

PFN_xrSetInputDeviceStateFloatEXT = CFUNCTYPE(Result, Session, Path, Path, c_float)

PFN_xrSetInputDeviceStateVector2fEXT = CFUNCTYPE(Result, Session, Path, Path, Vector2f)

PFN_xrSetInputDeviceLocationEXT = CFUNCTYPE(Result, Session, Path, Path, Space, Posef)


class SpatialGraphNodeSpaceCreateInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("node_type", SpatialGraphNodeTypeMSFT),
        ("node_id", (c_uint8 * 16)),
        ("pose", Posef),
    ]


PFN_xrCreateSpatialGraphNodeSpaceMSFT = CFUNCTYPE(Result, Session, POINTER(SpatialGraphNodeSpaceCreateInfoMSFT), POINTER(Space))


class HandTrackerEXT_T(Structure):
    pass


HandTrackerEXT = POINTER(HandTrackerEXT_T)


class SystemHandTrackingPropertiesEXT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("supports_hand_tracking", Bool32),
    ]


class HandTrackerCreateInfoEXT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("hand", HandEXT),
        ("hand_joint_set", HandJointSetEXT),
    ]


class HandJointsLocateInfoEXT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("base_space", Space),
        ("time", Time),
    ]


class HandJointLocationEXT(Structure):
    _fields_ = [
        ("location_flags", SpaceLocationFlags),
        ("pose", Posef),
        ("radius", c_float),
    ]


class HandJointVelocityEXT(Structure):
    _fields_ = [
        ("velocity_flags", SpaceVelocityFlags),
        ("linear_velocity", Vector3f),
        ("angular_velocity", Vector3f),
    ]


class HandJointLocationsEXT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("is_active", Bool32),
        ("joint_count", c_uint32),
        ("joint_locations", POINTER(HandJointLocationEXT)),
    ]


class HandJointVelocitiesEXT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("joint_count", c_uint32),
        ("joint_velocities", POINTER(HandJointVelocityEXT)),
    ]


PFN_xrCreateHandTrackerEXT = CFUNCTYPE(Result, Session, POINTER(HandTrackerCreateInfoEXT), POINTER(HandTrackerEXT))

PFN_xrDestroyHandTrackerEXT = CFUNCTYPE(Result, HandTrackerEXT)

PFN_xrLocateHandJointsEXT = CFUNCTYPE(Result, HandTrackerEXT, POINTER(HandJointsLocateInfoEXT), POINTER(HandJointLocationsEXT))


class SystemHandTrackingMeshPropertiesMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("supports_hand_tracking_mesh", Bool32),
        ("max_hand_mesh_index_count", c_uint32),
        ("max_hand_mesh_vertex_count", c_uint32),
    ]


class HandMeshSpaceCreateInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("hand_pose_type", HandPoseTypeMSFT),
        ("pose_in_hand_mesh_space", Posef),
    ]


class HandMeshUpdateInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("time", Time),
        ("hand_pose_type", HandPoseTypeMSFT),
    ]


class HandMeshIndexBufferMSFT(Structure):
    _fields_ = [
        ("index_buffer_key", c_uint32),
        ("index_capacity_input", c_uint32),
        ("index_count_output", c_uint32),
        ("indices", POINTER(c_uint32)),
    ]


class HandMeshVertexMSFT(Structure):
    _fields_ = [
        ("position", Vector3f),
        ("normal", Vector3f),
    ]


class HandMeshVertexBufferMSFT(Structure):
    _fields_ = [
        ("vertex_update_time", Time),
        ("vertex_capacity_input", c_uint32),
        ("vertex_count_output", c_uint32),
        ("vertices", POINTER(HandMeshVertexMSFT)),
    ]


class HandMeshMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("is_active", Bool32),
        ("index_buffer_changed", Bool32),
        ("vertex_buffer_changed", Bool32),
        ("index_buffer", HandMeshIndexBufferMSFT),
        ("vertex_buffer", HandMeshVertexBufferMSFT),
    ]


class HandPoseTypeInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("hand_pose_type", HandPoseTypeMSFT),
    ]


PFN_xrCreateHandMeshSpaceMSFT = CFUNCTYPE(Result, HandTrackerEXT, POINTER(HandMeshSpaceCreateInfoMSFT), POINTER(Space))

PFN_xrUpdateHandMeshMSFT = CFUNCTYPE(Result, HandTrackerEXT, POINTER(HandMeshUpdateInfoMSFT), POINTER(HandMeshMSFT))


class SecondaryViewConfigurationSessionBeginInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("view_configuration_count", c_uint32),
        ("enabled_view_configuration_types", POINTER(ViewConfigurationType)),
    ]


class SecondaryViewConfigurationStateMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("view_configuration_type", ViewConfigurationType),
        ("active", Bool32),
    ]


class SecondaryViewConfigurationFrameStateMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("view_configuration_count", c_uint32),
        ("view_configuration_states", POINTER(SecondaryViewConfigurationStateMSFT)),
    ]


class SecondaryViewConfigurationLayerInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("view_configuration_type", ViewConfigurationType),
        ("environment_blend_mode", EnvironmentBlendMode),
        ("layer_count", c_uint32),
        ("layers", POINTER(POINTER(CompositionLayerBaseHeader))),
    ]


class SecondaryViewConfigurationFrameEndInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("view_configuration_count", c_uint32),
        ("view_configuration_layers_info", POINTER(SecondaryViewConfigurationLayerInfoMSFT)),
    ]


class SecondaryViewConfigurationSwapchainCreateInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("view_configuration_type", ViewConfigurationType),
    ]


ControllerModelKeyMSFT = c_uint64


class ControllerModelKeyStateMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("model_key", ControllerModelKeyMSFT),
    ]


class ControllerModelNodePropertiesMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("parent_node_name", (c_char * 64)),
        ("node_name", (c_char * 64)),
    ]


class ControllerModelPropertiesMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("node_capacity_input", c_uint32),
        ("node_count_output", c_uint32),
        ("node_properties", POINTER(ControllerModelNodePropertiesMSFT)),
    ]


class ControllerModelNodeStateMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("node_pose", Posef),
    ]


class ControllerModelStateMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("node_capacity_input", c_uint32),
        ("node_count_output", c_uint32),
        ("node_states", POINTER(ControllerModelNodeStateMSFT)),
    ]


PFN_xrGetControllerModelKeyMSFT = CFUNCTYPE(Result, Session, Path, POINTER(ControllerModelKeyStateMSFT))

PFN_xrLoadControllerModelMSFT = CFUNCTYPE(Result, Session, ControllerModelKeyMSFT, c_uint32, POINTER(c_uint32), POINTER(c_uint8))

PFN_xrGetControllerModelPropertiesMSFT = CFUNCTYPE(Result, Session, ControllerModelKeyMSFT, POINTER(ControllerModelPropertiesMSFT))

PFN_xrGetControllerModelStateMSFT = CFUNCTYPE(Result, Session, ControllerModelKeyMSFT, POINTER(ControllerModelStateMSFT))


class ViewConfigurationViewFovEPIC(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("recommended_fov", Fovf),
        ("max_mutable_fov", Fovf),
    ]


class CompositionLayerReprojectionInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("reprojection_mode", ReprojectionModeMSFT),
    ]


class CompositionLayerReprojectionPlaneOverrideMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("position", Vector3f),
        ("normal", Vector3f),
        ("velocity", Vector3f),
    ]


PFN_xrEnumerateReprojectionModesMSFT = CFUNCTYPE(Result, Instance, SystemId, ViewConfigurationType, c_uint32, POINTER(c_uint32), POINTER(ReprojectionModeMSFT))


class SwapchainStateBaseHeaderFB(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
    ]


PFN_xrUpdateSwapchainFB = CFUNCTYPE(Result, Swapchain, POINTER(SwapchainStateBaseHeaderFB))

PFN_xrGetSwapchainStateFB = CFUNCTYPE(Result, Swapchain, POINTER(SwapchainStateBaseHeaderFB))

CompositionLayerSecureContentFlagsFB = Flags64


class CompositionLayerSecureContentFB(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("flags", CompositionLayerSecureContentFlagsFB),
    ]


class InteractionProfileAnalogThresholdVALVE(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("action", Action),
        ("binding", Path),
        ("on_threshold", c_float),
        ("off_threshold", c_float),
        ("on_haptic", POINTER(HapticBaseHeader)),
        ("off_haptic", POINTER(HapticBaseHeader)),
    ]


class HandJointsMotionRangeInfoEXT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("hand_joints_motion_range", HandJointsMotionRangeEXT),
    ]


class SceneObserverMSFT_T(Structure):
    pass


SceneObserverMSFT = POINTER(SceneObserverMSFT_T)


class SceneMSFT_T(Structure):
    pass


SceneMSFT = POINTER(SceneMSFT_T)


class UuidMSFT(Structure):
    _fields_ = [
        ("bytes", (c_uint8 * 16)),
    ]


class SceneObserverCreateInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
    ]


class SceneCreateInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
    ]


class SceneSphereBoundMSFT(Structure):
    _fields_ = [
        ("center", Vector3f),
        ("radius", c_float),
    ]


class SceneOrientedBoxBoundMSFT(Structure):
    _fields_ = [
        ("pose", Posef),
        ("extents", Vector3f),
    ]


class SceneFrustumBoundMSFT(Structure):
    _fields_ = [
        ("pose", Posef),
        ("fov", Fovf),
        ("far_distance", c_float),
    ]


class SceneBoundsMSFT(Structure):
    _fields_ = [
        ("space", Space),
        ("time", Time),
        ("sphere_count", c_uint32),
        ("spheres", POINTER(SceneSphereBoundMSFT)),
        ("box_count", c_uint32),
        ("boxes", POINTER(SceneOrientedBoxBoundMSFT)),
        ("frustum_count", c_uint32),
        ("frustums", POINTER(SceneFrustumBoundMSFT)),
    ]


class NewSceneComputeInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("requested_feature_count", c_uint32),
        ("requested_features", POINTER(SceneComputeFeatureMSFT)),
        ("consistency", SceneComputeConsistencyMSFT),
        ("bounds", SceneBoundsMSFT),
    ]


class VisualMeshComputeLodInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("lod", MeshComputeLodMSFT),
    ]


class SceneComponentMSFT(Structure):
    _fields_ = [
        ("component_type", SceneComponentTypeMSFT),
        ("id", UuidMSFT),
        ("parent_id", UuidMSFT),
        ("update_time", Time),
    ]


class SceneComponentsMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("component_capacity_input", c_uint32),
        ("component_count_output", c_uint32),
        ("components", POINTER(SceneComponentMSFT)),
    ]


class SceneComponentsGetInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("component_type", SceneComponentTypeMSFT),
    ]


class SceneComponentLocationMSFT(Structure):
    _fields_ = [
        ("flags", SpaceLocationFlags),
        ("pose", Posef),
    ]


class SceneComponentLocationsMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("location_count", c_uint32),
        ("locations", POINTER(SceneComponentLocationMSFT)),
    ]


class SceneComponentsLocateInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("base_space", Space),
        ("time", Time),
        ("component_id_count", c_uint32),
        ("component_ids", POINTER(UuidMSFT)),
    ]


class SceneObjectMSFT(Structure):
    _fields_ = [
        ("object_type", SceneObjectTypeMSFT),
    ]


class SceneObjectsMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("scene_object_count", c_uint32),
        ("scene_objects", POINTER(SceneObjectMSFT)),
    ]


class SceneComponentParentFilterInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("parent_id", UuidMSFT),
    ]


class SceneObjectTypesFilterInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("object_type_count", c_uint32),
        ("object_types", POINTER(SceneObjectTypeMSFT)),
    ]


class ScenePlaneMSFT(Structure):
    _fields_ = [
        ("alignment", ScenePlaneAlignmentTypeMSFT),
        ("size", Extent2Df),
        ("mesh_buffer_id", c_uint64),
        ("supports_indices_uint16", Bool32),
    ]


class ScenePlanesMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("scene_plane_count", c_uint32),
        ("scene_planes", POINTER(ScenePlaneMSFT)),
    ]


class ScenePlaneAlignmentFilterInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("alignment_count", c_uint32),
        ("alignments", POINTER(ScenePlaneAlignmentTypeMSFT)),
    ]


class SceneMeshMSFT(Structure):
    _fields_ = [
        ("mesh_buffer_id", c_uint64),
        ("supports_indices_uint16", Bool32),
    ]


class SceneMeshesMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("scene_mesh_count", c_uint32),
        ("scene_meshes", POINTER(SceneMeshMSFT)),
    ]


class SceneMeshBuffersGetInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("mesh_buffer_id", c_uint64),
    ]


class SceneMeshBuffersMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
    ]


class SceneMeshVertexBufferMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("vertex_capacity_input", c_uint32),
        ("vertex_count_output", c_uint32),
        ("vertices", POINTER(Vector3f)),
    ]


class SceneMeshIndicesUint32MSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("index_capacity_input", c_uint32),
        ("index_count_output", c_uint32),
        ("indices", POINTER(c_uint32)),
    ]


class SceneMeshIndicesUint16MSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("index_capacity_input", c_uint32),
        ("index_count_output", c_uint32),
        ("indices", POINTER(c_uint16)),
    ]


PFN_xrEnumerateSceneComputeFeaturesMSFT = CFUNCTYPE(Result, Instance, SystemId, c_uint32, POINTER(c_uint32), POINTER(SceneComputeFeatureMSFT))

PFN_xrCreateSceneObserverMSFT = CFUNCTYPE(Result, Session, POINTER(SceneObserverCreateInfoMSFT), POINTER(SceneObserverMSFT))

PFN_xrDestroySceneObserverMSFT = CFUNCTYPE(Result, SceneObserverMSFT)

PFN_xrCreateSceneMSFT = CFUNCTYPE(Result, SceneObserverMSFT, POINTER(SceneCreateInfoMSFT), POINTER(SceneMSFT))

PFN_xrDestroySceneMSFT = CFUNCTYPE(Result, SceneMSFT)

PFN_xrComputeNewSceneMSFT = CFUNCTYPE(Result, SceneObserverMSFT, POINTER(NewSceneComputeInfoMSFT))

PFN_xrGetSceneComputeStateMSFT = CFUNCTYPE(Result, SceneObserverMSFT, POINTER(SceneComputeStateMSFT))

PFN_xrGetSceneComponentsMSFT = CFUNCTYPE(Result, SceneMSFT, POINTER(SceneComponentsGetInfoMSFT), POINTER(SceneComponentsMSFT))

PFN_xrLocateSceneComponentsMSFT = CFUNCTYPE(Result, SceneMSFT, POINTER(SceneComponentsLocateInfoMSFT), POINTER(SceneComponentLocationsMSFT))

PFN_xrGetSceneMeshBuffersMSFT = CFUNCTYPE(Result, SceneMSFT, POINTER(SceneMeshBuffersGetInfoMSFT), POINTER(SceneMeshBuffersMSFT))


class SerializedSceneFragmentDataGetInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("scene_fragment_id", UuidMSFT),
    ]


class DeserializeSceneFragmentMSFT(Structure):
    _fields_ = [
        ("buffer_size", c_uint32),
        ("buffer", POINTER(c_uint8)),
    ]


class SceneDeserializeInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("fragment_count", c_uint32),
        ("fragments", POINTER(DeserializeSceneFragmentMSFT)),
    ]


PFN_xrDeserializeSceneMSFT = CFUNCTYPE(Result, SceneObserverMSFT, POINTER(SceneDeserializeInfoMSFT))

PFN_xrGetSerializedSceneFragmentDataMSFT = CFUNCTYPE(Result, SceneMSFT, POINTER(SerializedSceneFragmentDataGetInfoMSFT), c_uint32, POINTER(c_uint32), POINTER(c_uint8))


class EventDataDisplayRefreshRateChangedFB(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("from_display_refresh_rate", c_float),
        ("to_display_refresh_rate", c_float),
    ]


PFN_xrEnumerateDisplayRefreshRatesFB = CFUNCTYPE(Result, Session, c_uint32, POINTER(c_uint32), POINTER(c_float))

PFN_xrGetDisplayRefreshRateFB = CFUNCTYPE(Result, Session, POINTER(c_float))

PFN_xrRequestDisplayRefreshRateFB = CFUNCTYPE(Result, Session, c_float)


class SystemColorSpacePropertiesFB(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("color_space", ColorSpaceFB),
    ]


PFN_xrEnumerateColorSpacesFB = CFUNCTYPE(Result, Session, c_uint32, POINTER(c_uint32), POINTER(ColorSpaceFB))

PFN_xrSetColorSpaceFB = CFUNCTYPE(Result, Session, ColorSpaceFB)


class FoveationProfileFB_T(Structure):
    pass


FoveationProfileFB = POINTER(FoveationProfileFB_T)

SwapchainCreateFoveationFlagsFB = Flags64

SwapchainStateFoveationFlagsFB = Flags64


class FoveationProfileCreateInfoFB(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
    ]


class SwapchainCreateInfoFoveationFB(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("flags", SwapchainCreateFoveationFlagsFB),
    ]


class SwapchainStateFoveationFB(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("flags", SwapchainStateFoveationFlagsFB),
        ("profile", FoveationProfileFB),
    ]


PFN_xrCreateFoveationProfileFB = CFUNCTYPE(Result, Session, POINTER(FoveationProfileCreateInfoFB), POINTER(FoveationProfileFB))

PFN_xrDestroyFoveationProfileFB = CFUNCTYPE(Result, FoveationProfileFB)


class FoveationLevelProfileCreateInfoFB(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("level", FoveationLevelFB),
        ("vertical_offset", c_float),
        ("dynamic", FoveationDynamicFB),
    ]


class ViewLocateFoveatedRenderingVARJO(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("foveated_rendering_active", Bool32),
    ]


class FoveatedViewConfigurationViewVARJO(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("foveated_rendering_active", Bool32),
    ]


class SystemFoveatedRenderingPropertiesVARJO(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("supports_foveated_rendering", Bool32),
    ]


class CompositionLayerDepthTestVARJO(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("depth_test_range_near_z", c_float),
        ("depth_test_range_far_z", c_float),
    ]


PFN_xrSetEnvironmentDepthEstimationVARJO = CFUNCTYPE(Result, Session, Bool32)


class SpatialAnchorStoreConnectionMSFT_T(Structure):
    pass


SpatialAnchorStoreConnectionMSFT = POINTER(SpatialAnchorStoreConnectionMSFT_T)


class SpatialAnchorPersistenceNameMSFT(Structure):
    _fields_ = [
        ("name", (c_char * 256)),
    ]


class SpatialAnchorPersistenceInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("spatial_anchor_persistence_name", SpatialAnchorPersistenceNameMSFT),
        ("spatial_anchor", SpatialAnchorMSFT),
    ]


class SpatialAnchorFromPersistedAnchorCreateInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("spatial_anchor_store", SpatialAnchorStoreConnectionMSFT),
        ("spatial_anchor_persistence_name", SpatialAnchorPersistenceNameMSFT),
    ]


PFN_xrCreateSpatialAnchorStoreConnectionMSFT = CFUNCTYPE(Result, Session, POINTER(SpatialAnchorStoreConnectionMSFT))

PFN_xrDestroySpatialAnchorStoreConnectionMSFT = CFUNCTYPE(Result, SpatialAnchorStoreConnectionMSFT)

PFN_xrPersistSpatialAnchorMSFT = CFUNCTYPE(Result, SpatialAnchorStoreConnectionMSFT, POINTER(SpatialAnchorPersistenceInfoMSFT))

PFN_xrEnumeratePersistedSpatialAnchorNamesMSFT = CFUNCTYPE(Result, SpatialAnchorStoreConnectionMSFT, c_uint32, POINTER(c_uint32), POINTER(SpatialAnchorPersistenceNameMSFT))

PFN_xrCreateSpatialAnchorFromPersistedNameMSFT = CFUNCTYPE(Result, Session, POINTER(SpatialAnchorFromPersistedAnchorCreateInfoMSFT), POINTER(SpatialAnchorMSFT))

PFN_xrUnpersistSpatialAnchorMSFT = CFUNCTYPE(Result, SpatialAnchorStoreConnectionMSFT, POINTER(SpatialAnchorPersistenceNameMSFT))

PFN_xrClearSpatialAnchorStoreMSFT = CFUNCTYPE(Result, SpatialAnchorStoreConnectionMSFT)


__all__ = [
    "Version",
    "Flags64",
    "SystemId",
    "Bool32",
    "Path",
    "Time",
    "Duration",
    "Instance_T",
    "Instance",
    "Session_T",
    "Session",
    "Space_T",
    "Space",
    "Action_T",
    "Action",
    "Swapchain_T",
    "Swapchain",
    "ActionSet_T",
    "ActionSet",
    "InstanceCreateFlags",
    "SessionCreateFlags",
    "SpaceVelocityFlags",
    "SpaceLocationFlags",
    "SwapchainCreateFlags",
    "SwapchainUsageFlags",
    "CompositionLayerFlags",
    "ViewStateFlags",
    "InputSourceLocalizedNameFlags",
    "PFN_xrVoidFunction",
    "ApiLayerProperties",
    "ExtensionProperties",
    "ApplicationInfo",
    "InstanceCreateInfo",
    "InstanceProperties",
    "EventDataBuffer",
    "SystemGetInfo",
    "SystemGraphicsProperties",
    "SystemTrackingProperties",
    "SystemProperties",
    "SessionCreateInfo",
    "Vector3f",
    "SpaceVelocity",
    "Quaternionf",
    "Posef",
    "ReferenceSpaceCreateInfo",
    "Extent2Df",
    "ActionSpaceCreateInfo",
    "SpaceLocation",
    "ViewConfigurationProperties",
    "ViewConfigurationView",
    "SwapchainCreateInfo",
    "SwapchainImageBaseHeader",
    "SwapchainImageAcquireInfo",
    "SwapchainImageWaitInfo",
    "SwapchainImageReleaseInfo",
    "SessionBeginInfo",
    "FrameWaitInfo",
    "FrameState",
    "FrameBeginInfo",
    "CompositionLayerBaseHeader",
    "FrameEndInfo",
    "ViewLocateInfo",
    "ViewState",
    "Fovf",
    "View",
    "ActionSetCreateInfo",
    "ActionCreateInfo",
    "ActionSuggestedBinding",
    "InteractionProfileSuggestedBinding",
    "SessionActionSetsAttachInfo",
    "InteractionProfileState",
    "ActionStateGetInfo",
    "ActionStateBoolean",
    "ActionStateFloat",
    "Vector2f",
    "ActionStateVector2f",
    "ActionStatePose",
    "ActiveActionSet",
    "ActionsSyncInfo",
    "BoundSourcesForActionEnumerateInfo",
    "InputSourceLocalizedNameGetInfo",
    "HapticActionInfo",
    "HapticBaseHeader",
    "BaseInStructure",
    "BaseOutStructure",
    "Offset2Di",
    "Extent2Di",
    "Rect2Di",
    "SwapchainSubImage",
    "CompositionLayerProjectionView",
    "CompositionLayerProjection",
    "CompositionLayerQuad",
    "EventDataBaseHeader",
    "EventDataEventsLost",
    "EventDataInstanceLossPending",
    "EventDataSessionStateChanged",
    "EventDataReferenceSpaceChangePending",
    "EventDataInteractionProfileChanged",
    "HapticVibration",
    "Offset2Df",
    "Rect2Df",
    "Vector4f",
    "Color4f",
    "PFN_xrGetInstanceProcAddr",
    "PFN_xrEnumerateApiLayerProperties",
    "PFN_xrEnumerateInstanceExtensionProperties",
    "PFN_xrCreateInstance",
    "PFN_xrDestroyInstance",
    "PFN_xrGetInstanceProperties",
    "PFN_xrPollEvent",
    "PFN_xrResultToString",
    "PFN_xrStructureTypeToString",
    "PFN_xrGetSystem",
    "PFN_xrGetSystemProperties",
    "PFN_xrEnumerateEnvironmentBlendModes",
    "PFN_xrCreateSession",
    "PFN_xrDestroySession",
    "PFN_xrEnumerateReferenceSpaces",
    "PFN_xrCreateReferenceSpace",
    "PFN_xrGetReferenceSpaceBoundsRect",
    "PFN_xrCreateActionSpace",
    "PFN_xrLocateSpace",
    "PFN_xrDestroySpace",
    "PFN_xrEnumerateViewConfigurations",
    "PFN_xrGetViewConfigurationProperties",
    "PFN_xrEnumerateViewConfigurationViews",
    "PFN_xrEnumerateSwapchainFormats",
    "PFN_xrCreateSwapchain",
    "PFN_xrDestroySwapchain",
    "PFN_xrEnumerateSwapchainImages",
    "PFN_xrAcquireSwapchainImage",
    "PFN_xrWaitSwapchainImage",
    "PFN_xrReleaseSwapchainImage",
    "PFN_xrBeginSession",
    "PFN_xrEndSession",
    "PFN_xrRequestExitSession",
    "PFN_xrWaitFrame",
    "PFN_xrBeginFrame",
    "PFN_xrEndFrame",
    "PFN_xrLocateViews",
    "PFN_xrStringToPath",
    "PFN_xrPathToString",
    "PFN_xrCreateActionSet",
    "PFN_xrDestroyActionSet",
    "PFN_xrCreateAction",
    "PFN_xrDestroyAction",
    "PFN_xrSuggestInteractionProfileBindings",
    "PFN_xrAttachSessionActionSets",
    "PFN_xrGetCurrentInteractionProfile",
    "PFN_xrGetActionStateBoolean",
    "PFN_xrGetActionStateFloat",
    "PFN_xrGetActionStateVector2f",
    "PFN_xrGetActionStatePose",
    "PFN_xrSyncActions",
    "PFN_xrEnumerateBoundSourcesForAction",
    "PFN_xrGetInputSourceLocalizedName",
    "PFN_xrApplyHapticFeedback",
    "PFN_xrStopHapticFeedback",
    "CompositionLayerCubeKHR",
    "CompositionLayerDepthInfoKHR",
    "CompositionLayerCylinderKHR",
    "CompositionLayerEquirectKHR",
    "VisibilityMaskKHR",
    "EventDataVisibilityMaskChangedKHR",
    "PFN_xrGetVisibilityMaskKHR",
    "CompositionLayerColorScaleBiasKHR",
    "LoaderInitInfoBaseHeaderKHR",
    "PFN_xrInitializeLoaderKHR",
    "CompositionLayerEquirect2KHR",
    "BindingModificationBaseHeaderKHR",
    "BindingModificationsKHR",
    "EventDataPerfSettingsEXT",
    "PFN_xrPerfSettingsSetPerformanceLevelEXT",
    "PFN_xrThermalGetTemperatureTrendEXT",
    "DebugUtilsMessengerEXT_T",
    "DebugUtilsMessengerEXT",
    "DebugUtilsMessageSeverityFlagsEXT",
    "DebugUtilsMessageTypeFlagsEXT",
    "DebugUtilsObjectNameInfoEXT",
    "DebugUtilsLabelEXT",
    "DebugUtilsMessengerCallbackDataEXT",
    "PFN_xrDebugUtilsMessengerCallbackEXT",
    "DebugUtilsMessengerCreateInfoEXT",
    "PFN_xrSetDebugUtilsObjectNameEXT",
    "PFN_xrCreateDebugUtilsMessengerEXT",
    "PFN_xrDestroyDebugUtilsMessengerEXT",
    "PFN_xrSubmitDebugUtilsMessageEXT",
    "PFN_xrSessionBeginDebugUtilsLabelRegionEXT",
    "PFN_xrSessionEndDebugUtilsLabelRegionEXT",
    "PFN_xrSessionInsertDebugUtilsLabelEXT",
    "SystemEyeGazeInteractionPropertiesEXT",
    "EyeGazeSampleTimeEXT",
    "OverlaySessionCreateFlagsEXTX",
    "OverlayMainSessionFlagsEXTX",
    "SessionCreateInfoOverlayEXTX",
    "EventDataMainSessionVisibilityChangedEXTX",
    "SpatialAnchorMSFT_T",
    "SpatialAnchorMSFT",
    "SpatialAnchorCreateInfoMSFT",
    "SpatialAnchorSpaceCreateInfoMSFT",
    "PFN_xrCreateSpatialAnchorMSFT",
    "PFN_xrCreateSpatialAnchorSpaceMSFT",
    "PFN_xrDestroySpatialAnchorMSFT",
    "CompositionLayerImageLayoutFlagsFB",
    "CompositionLayerImageLayoutFB",
    "CompositionLayerAlphaBlendFB",
    "ViewConfigurationDepthRangeEXT",
    "PFN_xrSetInputDeviceActiveEXT",
    "PFN_xrSetInputDeviceStateBoolEXT",
    "PFN_xrSetInputDeviceStateFloatEXT",
    "PFN_xrSetInputDeviceStateVector2fEXT",
    "PFN_xrSetInputDeviceLocationEXT",
    "SpatialGraphNodeSpaceCreateInfoMSFT",
    "PFN_xrCreateSpatialGraphNodeSpaceMSFT",
    "HandTrackerEXT_T",
    "HandTrackerEXT",
    "SystemHandTrackingPropertiesEXT",
    "HandTrackerCreateInfoEXT",
    "HandJointsLocateInfoEXT",
    "HandJointLocationEXT",
    "HandJointVelocityEXT",
    "HandJointLocationsEXT",
    "HandJointVelocitiesEXT",
    "PFN_xrCreateHandTrackerEXT",
    "PFN_xrDestroyHandTrackerEXT",
    "PFN_xrLocateHandJointsEXT",
    "SystemHandTrackingMeshPropertiesMSFT",
    "HandMeshSpaceCreateInfoMSFT",
    "HandMeshUpdateInfoMSFT",
    "HandMeshIndexBufferMSFT",
    "HandMeshVertexMSFT",
    "HandMeshVertexBufferMSFT",
    "HandMeshMSFT",
    "HandPoseTypeInfoMSFT",
    "PFN_xrCreateHandMeshSpaceMSFT",
    "PFN_xrUpdateHandMeshMSFT",
    "SecondaryViewConfigurationSessionBeginInfoMSFT",
    "SecondaryViewConfigurationStateMSFT",
    "SecondaryViewConfigurationFrameStateMSFT",
    "SecondaryViewConfigurationLayerInfoMSFT",
    "SecondaryViewConfigurationFrameEndInfoMSFT",
    "SecondaryViewConfigurationSwapchainCreateInfoMSFT",
    "ControllerModelKeyMSFT",
    "ControllerModelKeyStateMSFT",
    "ControllerModelNodePropertiesMSFT",
    "ControllerModelPropertiesMSFT",
    "ControllerModelNodeStateMSFT",
    "ControllerModelStateMSFT",
    "PFN_xrGetControllerModelKeyMSFT",
    "PFN_xrLoadControllerModelMSFT",
    "PFN_xrGetControllerModelPropertiesMSFT",
    "PFN_xrGetControllerModelStateMSFT",
    "ViewConfigurationViewFovEPIC",
    "CompositionLayerReprojectionInfoMSFT",
    "CompositionLayerReprojectionPlaneOverrideMSFT",
    "PFN_xrEnumerateReprojectionModesMSFT",
    "SwapchainStateBaseHeaderFB",
    "PFN_xrUpdateSwapchainFB",
    "PFN_xrGetSwapchainStateFB",
    "CompositionLayerSecureContentFlagsFB",
    "CompositionLayerSecureContentFB",
    "InteractionProfileAnalogThresholdVALVE",
    "HandJointsMotionRangeInfoEXT",
    "SceneObserverMSFT_T",
    "SceneObserverMSFT",
    "SceneMSFT_T",
    "SceneMSFT",
    "UuidMSFT",
    "SceneObserverCreateInfoMSFT",
    "SceneCreateInfoMSFT",
    "SceneSphereBoundMSFT",
    "SceneOrientedBoxBoundMSFT",
    "SceneFrustumBoundMSFT",
    "SceneBoundsMSFT",
    "NewSceneComputeInfoMSFT",
    "VisualMeshComputeLodInfoMSFT",
    "SceneComponentMSFT",
    "SceneComponentsMSFT",
    "SceneComponentsGetInfoMSFT",
    "SceneComponentLocationMSFT",
    "SceneComponentLocationsMSFT",
    "SceneComponentsLocateInfoMSFT",
    "SceneObjectMSFT",
    "SceneObjectsMSFT",
    "SceneComponentParentFilterInfoMSFT",
    "SceneObjectTypesFilterInfoMSFT",
    "ScenePlaneMSFT",
    "ScenePlanesMSFT",
    "ScenePlaneAlignmentFilterInfoMSFT",
    "SceneMeshMSFT",
    "SceneMeshesMSFT",
    "SceneMeshBuffersGetInfoMSFT",
    "SceneMeshBuffersMSFT",
    "SceneMeshVertexBufferMSFT",
    "SceneMeshIndicesUint32MSFT",
    "SceneMeshIndicesUint16MSFT",
    "PFN_xrEnumerateSceneComputeFeaturesMSFT",
    "PFN_xrCreateSceneObserverMSFT",
    "PFN_xrDestroySceneObserverMSFT",
    "PFN_xrCreateSceneMSFT",
    "PFN_xrDestroySceneMSFT",
    "PFN_xrComputeNewSceneMSFT",
    "PFN_xrGetSceneComputeStateMSFT",
    "PFN_xrGetSceneComponentsMSFT",
    "PFN_xrLocateSceneComponentsMSFT",
    "PFN_xrGetSceneMeshBuffersMSFT",
    "SerializedSceneFragmentDataGetInfoMSFT",
    "DeserializeSceneFragmentMSFT",
    "SceneDeserializeInfoMSFT",
    "PFN_xrDeserializeSceneMSFT",
    "PFN_xrGetSerializedSceneFragmentDataMSFT",
    "EventDataDisplayRefreshRateChangedFB",
    "PFN_xrEnumerateDisplayRefreshRatesFB",
    "PFN_xrGetDisplayRefreshRateFB",
    "PFN_xrRequestDisplayRefreshRateFB",
    "SystemColorSpacePropertiesFB",
    "PFN_xrEnumerateColorSpacesFB",
    "PFN_xrSetColorSpaceFB",
    "FoveationProfileFB_T",
    "FoveationProfileFB",
    "SwapchainCreateFoveationFlagsFB",
    "SwapchainStateFoveationFlagsFB",
    "FoveationProfileCreateInfoFB",
    "SwapchainCreateInfoFoveationFB",
    "SwapchainStateFoveationFB",
    "PFN_xrCreateFoveationProfileFB",
    "PFN_xrDestroyFoveationProfileFB",
    "FoveationLevelProfileCreateInfoFB",
    "ViewLocateFoveatedRenderingVARJO",
    "FoveatedViewConfigurationViewVARJO",
    "SystemFoveatedRenderingPropertiesVARJO",
    "CompositionLayerDepthTestVARJO",
    "PFN_xrSetEnvironmentDepthEstimationVARJO",
    "SpatialAnchorStoreConnectionMSFT_T",
    "SpatialAnchorStoreConnectionMSFT",
    "SpatialAnchorPersistenceNameMSFT",
    "SpatialAnchorPersistenceInfoMSFT",
    "SpatialAnchorFromPersistedAnchorCreateInfoMSFT",
    "PFN_xrCreateSpatialAnchorStoreConnectionMSFT",
    "PFN_xrDestroySpatialAnchorStoreConnectionMSFT",
    "PFN_xrPersistSpatialAnchorMSFT",
    "PFN_xrEnumeratePersistedSpatialAnchorNamesMSFT",
    "PFN_xrCreateSpatialAnchorFromPersistedNameMSFT",
    "PFN_xrUnpersistSpatialAnchorMSFT",
    "PFN_xrClearSpatialAnchorStoreMSFT",
]
