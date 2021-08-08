# Warning: this file is auto-generated. Do not edit.

from ctypes import CFUNCTYPE, POINTER, Structure, c_char, c_float, c_int32, c_int64, c_uint16, c_uint32, c_uint64, c_uint8, c_void_p

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

Result = c_int32

StructureType = c_int32

FormFactor = c_int32

ViewConfigurationType = c_int32

EnvironmentBlendMode = c_int32

ReferenceSpaceType = c_int32

ActionType = c_int32

EyeVisibility = c_int32

SessionState = c_int32

ObjectType = c_int32

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
        ("layerName", (c_char * 256)),
        ("specVersion", Version),
        ("layerVersion", c_uint32),
        ("description", (c_char * 256)),
    ]


class ExtensionProperties(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("extensionName", (c_char * 128)),
        ("extensionVersion", c_uint32),
    ]


class ApplicationInfo(Structure):
    _fields_ = [
        ("applicationName", (c_char * 128)),
        ("applicationVersion", c_uint32),
        ("engineName", (c_char * 128)),
        ("engineVersion", c_uint32),
        ("apiVersion", Version),
    ]


class InstanceCreateInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("createFlags", InstanceCreateFlags),
        ("applicationInfo", ApplicationInfo),
        ("enabledApiLayerCount", c_uint32),
        ("enabledApiLayerNames", POINTER(POINTER(c_char))),
        ("enabledExtensionCount", c_uint32),
        ("enabledExtensionNames", POINTER(POINTER(c_char))),
    ]


class InstanceProperties(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("runtimeVersion", Version),
        ("runtimeName", (c_char * 128)),
    ]


class EventDataBuffer(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("varying", c_uint8),
    ]


class SystemGetInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("formFactor", FormFactor),
    ]


class SystemGraphicsProperties(Structure):
    _fields_ = [
        ("maxSwapchainImageHeight", c_uint32),
        ("maxSwapchainImageWidth", c_uint32),
        ("maxLayerCount", c_uint32),
    ]


class SystemTrackingProperties(Structure):
    _fields_ = [
        ("orientationTracking", Bool32),
        ("positionTracking", Bool32),
    ]


class SystemProperties(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("systemId", SystemId),
        ("vendorId", c_uint32),
        ("systemName", (c_char * 256)),
        ("graphicsProperties", SystemGraphicsProperties),
        ("trackingProperties", SystemTrackingProperties),
    ]


class SessionCreateInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("createFlags", SessionCreateFlags),
        ("systemId", SystemId),
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
        ("velocityFlags", SpaceVelocityFlags),
        ("linearVelocity", Vector3f),
        ("angularVelocity", Vector3f),
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
        ("referenceSpaceType", ReferenceSpaceType),
        ("poseInReferenceSpace", Posef),
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
        ("subactionPath", Path),
        ("poseInActionSpace", Posef),
    ]


class SpaceLocation(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("locationFlags", SpaceLocationFlags),
        ("pose", Posef),
    ]


class ViewConfigurationProperties(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("viewConfigurationType", ViewConfigurationType),
        ("fovMutable", Bool32),
    ]


class ViewConfigurationView(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("recommendedImageRectWidth", c_uint32),
        ("maxImageRectWidth", c_uint32),
        ("recommendedImageRectHeight", c_uint32),
        ("maxImageRectHeight", c_uint32),
        ("recommendedSwapchainSampleCount", c_uint32),
        ("maxSwapchainSampleCount", c_uint32),
    ]


class SwapchainCreateInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("createFlags", SwapchainCreateFlags),
        ("usageFlags", SwapchainUsageFlags),
        ("format", c_int64),
        ("sampleCount", c_uint32),
        ("width", c_uint32),
        ("height", c_uint32),
        ("faceCount", c_uint32),
        ("arraySize", c_uint32),
        ("mipCount", c_uint32),
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
        ("primaryViewConfigurationType", ViewConfigurationType),
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
        ("predictedDisplayTime", Time),
        ("predictedDisplayPeriod", Duration),
        ("shouldRender", Bool32),
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
        ("layerFlags", CompositionLayerFlags),
        ("space", Space),
    ]


class FrameEndInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("displayTime", Time),
        ("environmentBlendMode", EnvironmentBlendMode),
        ("layerCount", c_uint32),
        ("layers", POINTER(POINTER(CompositionLayerBaseHeader))),
    ]


class ViewLocateInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("viewConfigurationType", ViewConfigurationType),
        ("displayTime", Time),
        ("space", Space),
    ]


class ViewState(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("viewStateFlags", ViewStateFlags),
    ]


class Fovf(Structure):
    _fields_ = [
        ("angleLeft", c_float),
        ("angleRight", c_float),
        ("angleUp", c_float),
        ("angleDown", c_float),
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
        ("actionSetName", (c_char * 64)),
        ("localizedActionSetName", (c_char * 128)),
        ("priority", c_uint32),
    ]


class ActionCreateInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("actionName", (c_char * 64)),
        ("actionType", ActionType),
        ("countSubactionPaths", c_uint32),
        ("subactionPaths", POINTER(Path)),
        ("localizedActionName", (c_char * 128)),
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
        ("interactionProfile", Path),
        ("countSuggestedBindings", c_uint32),
        ("suggestedBindings", POINTER(ActionSuggestedBinding)),
    ]


class SessionActionSetsAttachInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("countActionSets", c_uint32),
        ("actionSets", POINTER(ActionSet)),
    ]


class InteractionProfileState(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("interactionProfile", Path),
    ]


class ActionStateGetInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("action", Action),
        ("subactionPath", Path),
    ]


class ActionStateBoolean(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("currentState", Bool32),
        ("changedSinceLastSync", Bool32),
        ("lastChangeTime", Time),
        ("isActive", Bool32),
    ]


class ActionStateFloat(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("currentState", c_float),
        ("changedSinceLastSync", Bool32),
        ("lastChangeTime", Time),
        ("isActive", Bool32),
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
        ("currentState", Vector2f),
        ("changedSinceLastSync", Bool32),
        ("lastChangeTime", Time),
        ("isActive", Bool32),
    ]


class ActionStatePose(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("isActive", Bool32),
    ]


class ActiveActionSet(Structure):
    _fields_ = [
        ("actionSet", ActionSet),
        ("subactionPath", Path),
    ]


class ActionsSyncInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("countActiveActionSets", c_uint32),
        ("activeActionSets", POINTER(ActiveActionSet)),
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
        ("sourcePath", Path),
        ("whichComponents", InputSourceLocalizedNameFlags),
    ]


class HapticActionInfo(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("action", Action),
        ("subactionPath", Path),
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
        ("imageRect", Rect2Di),
        ("imageArrayIndex", c_uint32),
    ]


class CompositionLayerProjectionView(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("pose", Posef),
        ("fov", Fovf),
        ("subImage", SwapchainSubImage),
    ]


class CompositionLayerProjection(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("layerFlags", CompositionLayerFlags),
        ("space", Space),
        ("viewCount", c_uint32),
        ("views", POINTER(CompositionLayerProjectionView)),
    ]


class CompositionLayerQuad(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("layerFlags", CompositionLayerFlags),
        ("space", Space),
        ("eyeVisibility", EyeVisibility),
        ("subImage", SwapchainSubImage),
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
        ("lostEventCount", c_uint32),
    ]


class EventDataInstanceLossPending(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("lossTime", Time),
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
        ("referenceSpaceType", ReferenceSpaceType),
        ("changeTime", Time),
        ("poseValid", Bool32),
        ("poseInPreviousSpace", Posef),
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


PFN_xrGetInstanceProcAddr = CFUNCTYPE(Result, Instance, POINTER(c_char), POINTER(PFN_xrVoidFunction))

PFN_xrEnumerateApiLayerProperties = CFUNCTYPE(Result, c_uint32, c_uint32, POINTER(ApiLayerProperties))

PFN_xrEnumerateInstanceExtensionProperties = CFUNCTYPE(Result, POINTER(c_char), c_uint32, c_uint32, POINTER(ExtensionProperties))

PFN_xrCreateInstance = CFUNCTYPE(Result, POINTER(InstanceCreateInfo), POINTER(Instance))

PFN_xrDestroyInstance = CFUNCTYPE(Result, Instance)

PFN_xrGetInstanceProperties = CFUNCTYPE(Result, Instance, POINTER(InstanceProperties))

PFN_xrPollEvent = CFUNCTYPE(Result, Instance, POINTER(EventDataBuffer))

PFN_xrResultToString = CFUNCTYPE(Result, Instance, Result, (c_char * 64))

PFN_xrStructureTypeToString = CFUNCTYPE(Result, Instance, StructureType, (c_char * 64))

PFN_xrGetSystem = CFUNCTYPE(Result, Instance, POINTER(SystemGetInfo), POINTER(SystemId))

PFN_xrGetSystemProperties = CFUNCTYPE(Result, Instance, SystemId, POINTER(SystemProperties))

PFN_xrEnumerateEnvironmentBlendModes = CFUNCTYPE(Result, Instance, SystemId, ViewConfigurationType, c_uint32, c_uint32, POINTER(EnvironmentBlendMode))

PFN_xrCreateSession = CFUNCTYPE(Result, Instance, POINTER(SessionCreateInfo), POINTER(Session))

PFN_xrDestroySession = CFUNCTYPE(Result, Session)

PFN_xrEnumerateReferenceSpaces = CFUNCTYPE(Result, Session, c_uint32, c_uint32, POINTER(ReferenceSpaceType))

PFN_xrCreateReferenceSpace = CFUNCTYPE(Result, Session, POINTER(ReferenceSpaceCreateInfo), POINTER(Space))

PFN_xrGetReferenceSpaceBoundsRect = CFUNCTYPE(Result, Session, ReferenceSpaceType, POINTER(Extent2Df))

PFN_xrCreateActionSpace = CFUNCTYPE(Result, Session, POINTER(ActionSpaceCreateInfo), POINTER(Space))

PFN_xrLocateSpace = CFUNCTYPE(Result, Space, Space, Time, POINTER(SpaceLocation))

PFN_xrDestroySpace = CFUNCTYPE(Result, Space)

PFN_xrEnumerateViewConfigurations = CFUNCTYPE(Result, Instance, SystemId, c_uint32, c_uint32, POINTER(ViewConfigurationType))

PFN_xrGetViewConfigurationProperties = CFUNCTYPE(Result, Instance, SystemId, ViewConfigurationType, POINTER(ViewConfigurationProperties))

PFN_xrEnumerateViewConfigurationViews = CFUNCTYPE(Result, Instance, SystemId, ViewConfigurationType, c_uint32, c_uint32, POINTER(ViewConfigurationView))

PFN_xrEnumerateSwapchainFormats = CFUNCTYPE(Result, Session, c_uint32, c_uint32, c_int64)

PFN_xrCreateSwapchain = CFUNCTYPE(Result, Session, POINTER(SwapchainCreateInfo), POINTER(Swapchain))

PFN_xrDestroySwapchain = CFUNCTYPE(Result, Swapchain)

PFN_xrEnumerateSwapchainImages = CFUNCTYPE(Result, Swapchain, c_uint32, c_uint32, POINTER(SwapchainImageBaseHeader))

PFN_xrAcquireSwapchainImage = CFUNCTYPE(Result, Swapchain, POINTER(SwapchainImageAcquireInfo), c_uint32)

PFN_xrWaitSwapchainImage = CFUNCTYPE(Result, Swapchain, POINTER(SwapchainImageWaitInfo))

PFN_xrReleaseSwapchainImage = CFUNCTYPE(Result, Swapchain, POINTER(SwapchainImageReleaseInfo))

PFN_xrBeginSession = CFUNCTYPE(Result, Session, POINTER(SessionBeginInfo))

PFN_xrEndSession = CFUNCTYPE(Result, Session)

PFN_xrRequestExitSession = CFUNCTYPE(Result, Session)

PFN_xrWaitFrame = CFUNCTYPE(Result, Session, POINTER(FrameWaitInfo), POINTER(FrameState))

PFN_xrBeginFrame = CFUNCTYPE(Result, Session, POINTER(FrameBeginInfo))

PFN_xrEndFrame = CFUNCTYPE(Result, Session, POINTER(FrameEndInfo))

PFN_xrLocateViews = CFUNCTYPE(Result, Session, POINTER(ViewLocateInfo), POINTER(ViewState), c_uint32, c_uint32, POINTER(View))

PFN_xrStringToPath = CFUNCTYPE(Result, Instance, POINTER(c_char), POINTER(Path))

PFN_xrPathToString = CFUNCTYPE(Result, Instance, Path, c_uint32, c_uint32, POINTER(c_char))

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

PFN_xrEnumerateBoundSourcesForAction = CFUNCTYPE(Result, Session, POINTER(BoundSourcesForActionEnumerateInfo), c_uint32, c_uint32, POINTER(Path))

PFN_xrGetInputSourceLocalizedName = CFUNCTYPE(Result, Session, POINTER(InputSourceLocalizedNameGetInfo), c_uint32, c_uint32, POINTER(c_char))

PFN_xrApplyHapticFeedback = CFUNCTYPE(Result, Session, POINTER(HapticActionInfo), POINTER(HapticBaseHeader))

PFN_xrStopHapticFeedback = CFUNCTYPE(Result, Session, POINTER(HapticActionInfo))


class CompositionLayerCubeKHR(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("layerFlags", CompositionLayerFlags),
        ("space", Space),
        ("eyeVisibility", EyeVisibility),
        ("swapchain", Swapchain),
        ("imageArrayIndex", c_uint32),
        ("orientation", Quaternionf),
    ]


class CompositionLayerDepthInfoKHR(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("subImage", SwapchainSubImage),
        ("minDepth", c_float),
        ("maxDepth", c_float),
        ("nearZ", c_float),
        ("farZ", c_float),
    ]


class CompositionLayerCylinderKHR(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("layerFlags", CompositionLayerFlags),
        ("space", Space),
        ("eyeVisibility", EyeVisibility),
        ("subImage", SwapchainSubImage),
        ("pose", Posef),
        ("radius", c_float),
        ("centralAngle", c_float),
        ("aspectRatio", c_float),
    ]


class CompositionLayerEquirectKHR(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("layerFlags", CompositionLayerFlags),
        ("space", Space),
        ("eyeVisibility", EyeVisibility),
        ("subImage", SwapchainSubImage),
        ("pose", Posef),
        ("radius", c_float),
        ("scale", Vector2f),
        ("bias", Vector2f),
    ]


VisibilityMaskTypeKHR = c_int32


class VisibilityMaskKHR(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("vertexCapacityInput", c_uint32),
        ("vertexCountOutput", c_uint32),
        ("vertices", POINTER(Vector2f)),
        ("indexCapacityInput", c_uint32),
        ("indexCountOutput", c_uint32),
        ("indices", c_uint32),
    ]


class EventDataVisibilityMaskChangedKHR(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("session", Session),
        ("viewConfigurationType", ViewConfigurationType),
        ("viewIndex", c_uint32),
    ]


PFN_xrGetVisibilityMaskKHR = CFUNCTYPE(Result, Session, ViewConfigurationType, c_uint32, VisibilityMaskTypeKHR, POINTER(VisibilityMaskKHR))


class CompositionLayerColorScaleBiasKHR(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("colorScale", Color4f),
        ("colorBias", Color4f),
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
        ("layerFlags", CompositionLayerFlags),
        ("space", Space),
        ("eyeVisibility", EyeVisibility),
        ("subImage", SwapchainSubImage),
        ("pose", Posef),
        ("radius", c_float),
        ("centralHorizontalAngle", c_float),
        ("upperVerticalAngle", c_float),
        ("lowerVerticalAngle", c_float),
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
        ("bindingModificationCount", c_uint32),
        ("bindingModifications", POINTER(POINTER(BindingModificationBaseHeaderKHR))),
    ]


PerfSettingsDomainEXT = c_int32

PerfSettingsSubDomainEXT = c_int32

PerfSettingsLevelEXT = c_int32

PerfSettingsNotificationLevelEXT = c_int32


class EventDataPerfSettingsEXT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("domain", PerfSettingsDomainEXT),
        ("subDomain", PerfSettingsSubDomainEXT),
        ("fromLevel", PerfSettingsNotificationLevelEXT),
        ("toLevel", PerfSettingsNotificationLevelEXT),
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
        ("objectType", ObjectType),
        ("objectHandle", c_uint64),
        ("objectName", POINTER(c_char)),
    ]


class DebugUtilsLabelEXT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("labelName", POINTER(c_char)),
    ]


class DebugUtilsMessengerCallbackDataEXT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("messageId", POINTER(c_char)),
        ("functionName", POINTER(c_char)),
        ("message", POINTER(c_char)),
        ("objectCount", c_uint32),
        ("objects", POINTER(DebugUtilsObjectNameInfoEXT)),
        ("sessionLabelCount", c_uint32),
        ("sessionLabels", POINTER(DebugUtilsLabelEXT)),
    ]


PFN_xrDebugUtilsMessengerCallbackEXT = CFUNCTYPE(Bool32, DebugUtilsMessageSeverityFlagsEXT, DebugUtilsMessageTypeFlagsEXT, POINTER(DebugUtilsMessengerCallbackDataEXT), c_void_p)


class DebugUtilsMessengerCreateInfoEXT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("messageSeverities", DebugUtilsMessageSeverityFlagsEXT),
        ("messageTypes", DebugUtilsMessageTypeFlagsEXT),
        ("userCallback", PFN_xrDebugUtilsMessengerCallbackEXT),
        ("userData", c_void_p),
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
        ("supportsEyeGazeInteraction", Bool32),
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
        ("createFlags", OverlaySessionCreateFlagsEXTX),
        ("sessionLayersPlacement", c_uint32),
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
        ("poseInAnchorSpace", Posef),
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


BlendFactorFB = c_int32


class CompositionLayerAlphaBlendFB(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("srcFactorColor", BlendFactorFB),
        ("dstFactorColor", BlendFactorFB),
        ("srcFactorAlpha", BlendFactorFB),
        ("dstFactorAlpha", BlendFactorFB),
    ]


class ViewConfigurationDepthRangeEXT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("recommendedNearZ", c_float),
        ("minNearZ", c_float),
        ("recommendedFarZ", c_float),
        ("maxFarZ", c_float),
    ]


PFN_xrSetInputDeviceActiveEXT = CFUNCTYPE(Result, Session, Path, Path, Bool32)

PFN_xrSetInputDeviceStateBoolEXT = CFUNCTYPE(Result, Session, Path, Path, Bool32)

PFN_xrSetInputDeviceStateFloatEXT = CFUNCTYPE(Result, Session, Path, Path, c_float)

PFN_xrSetInputDeviceStateVector2fEXT = CFUNCTYPE(Result, Session, Path, Path, Vector2f)

PFN_xrSetInputDeviceLocationEXT = CFUNCTYPE(Result, Session, Path, Path, Space, Posef)

SpatialGraphNodeTypeMSFT = c_int32


class SpatialGraphNodeSpaceCreateInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("nodeType", SpatialGraphNodeTypeMSFT),
        ("nodeId", c_uint8),
        ("pose", Posef),
    ]


PFN_xrCreateSpatialGraphNodeSpaceMSFT = CFUNCTYPE(Result, Session, POINTER(SpatialGraphNodeSpaceCreateInfoMSFT), POINTER(Space))


class HandTrackerEXT_T(Structure):
    pass


HandTrackerEXT = POINTER(HandTrackerEXT_T)

HandEXT = c_int32

HandJointEXT = c_int32

HandJointSetEXT = c_int32


class SystemHandTrackingPropertiesEXT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("supportsHandTracking", Bool32),
    ]


class HandTrackerCreateInfoEXT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("hand", HandEXT),
        ("handJointSet", HandJointSetEXT),
    ]


class HandJointsLocateInfoEXT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("baseSpace", Space),
        ("time", Time),
    ]


class HandJointLocationEXT(Structure):
    _fields_ = [
        ("locationFlags", SpaceLocationFlags),
        ("pose", Posef),
        ("radius", c_float),
    ]


class HandJointVelocityEXT(Structure):
    _fields_ = [
        ("velocityFlags", SpaceVelocityFlags),
        ("linearVelocity", Vector3f),
        ("angularVelocity", Vector3f),
    ]


class HandJointLocationsEXT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("isActive", Bool32),
        ("jointCount", c_uint32),
        ("jointLocations", POINTER(HandJointLocationEXT)),
    ]


class HandJointVelocitiesEXT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("jointCount", c_uint32),
        ("jointVelocities", POINTER(HandJointVelocityEXT)),
    ]


PFN_xrCreateHandTrackerEXT = CFUNCTYPE(Result, Session, POINTER(HandTrackerCreateInfoEXT), POINTER(HandTrackerEXT))

PFN_xrDestroyHandTrackerEXT = CFUNCTYPE(Result, HandTrackerEXT)

PFN_xrLocateHandJointsEXT = CFUNCTYPE(Result, HandTrackerEXT, POINTER(HandJointsLocateInfoEXT), POINTER(HandJointLocationsEXT))

HandPoseTypeMSFT = c_int32


class SystemHandTrackingMeshPropertiesMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("supportsHandTrackingMesh", Bool32),
        ("maxHandMeshIndexCount", c_uint32),
        ("maxHandMeshVertexCount", c_uint32),
    ]


class HandMeshSpaceCreateInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("handPoseType", HandPoseTypeMSFT),
        ("poseInHandMeshSpace", Posef),
    ]


class HandMeshUpdateInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("time", Time),
        ("handPoseType", HandPoseTypeMSFT),
    ]


class HandMeshIndexBufferMSFT(Structure):
    _fields_ = [
        ("indexBufferKey", c_uint32),
        ("indexCapacityInput", c_uint32),
        ("indexCountOutput", c_uint32),
        ("indices", c_uint32),
    ]


class HandMeshVertexMSFT(Structure):
    _fields_ = [
        ("position", Vector3f),
        ("normal", Vector3f),
    ]


class HandMeshVertexBufferMSFT(Structure):
    _fields_ = [
        ("vertexUpdateTime", Time),
        ("vertexCapacityInput", c_uint32),
        ("vertexCountOutput", c_uint32),
        ("vertices", POINTER(HandMeshVertexMSFT)),
    ]


class HandMeshMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("isActive", Bool32),
        ("indexBufferChanged", Bool32),
        ("vertexBufferChanged", Bool32),
        ("indexBuffer", HandMeshIndexBufferMSFT),
        ("vertexBuffer", HandMeshVertexBufferMSFT),
    ]


class HandPoseTypeInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("handPoseType", HandPoseTypeMSFT),
    ]


PFN_xrCreateHandMeshSpaceMSFT = CFUNCTYPE(Result, HandTrackerEXT, POINTER(HandMeshSpaceCreateInfoMSFT), POINTER(Space))

PFN_xrUpdateHandMeshMSFT = CFUNCTYPE(Result, HandTrackerEXT, POINTER(HandMeshUpdateInfoMSFT), POINTER(HandMeshMSFT))


class SecondaryViewConfigurationSessionBeginInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("viewConfigurationCount", c_uint32),
        ("enabledViewConfigurationTypes", POINTER(ViewConfigurationType)),
    ]


class SecondaryViewConfigurationStateMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("viewConfigurationType", ViewConfigurationType),
        ("active", Bool32),
    ]


class SecondaryViewConfigurationFrameStateMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("viewConfigurationCount", c_uint32),
        ("viewConfigurationStates", POINTER(SecondaryViewConfigurationStateMSFT)),
    ]


class SecondaryViewConfigurationLayerInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("viewConfigurationType", ViewConfigurationType),
        ("environmentBlendMode", EnvironmentBlendMode),
        ("layerCount", c_uint32),
        ("layers", POINTER(POINTER(CompositionLayerBaseHeader))),
    ]


class SecondaryViewConfigurationFrameEndInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("viewConfigurationCount", c_uint32),
        ("viewConfigurationLayersInfo", POINTER(SecondaryViewConfigurationLayerInfoMSFT)),
    ]


class SecondaryViewConfigurationSwapchainCreateInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("viewConfigurationType", ViewConfigurationType),
    ]


ControllerModelKeyMSFT = c_uint64


class ControllerModelKeyStateMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("modelKey", ControllerModelKeyMSFT),
    ]


class ControllerModelNodePropertiesMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("parentNodeName", (c_char * 64)),
        ("nodeName", (c_char * 64)),
    ]


class ControllerModelPropertiesMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("nodeCapacityInput", c_uint32),
        ("nodeCountOutput", c_uint32),
        ("nodeProperties", POINTER(ControllerModelNodePropertiesMSFT)),
    ]


class ControllerModelNodeStateMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("nodePose", Posef),
    ]


class ControllerModelStateMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("nodeCapacityInput", c_uint32),
        ("nodeCountOutput", c_uint32),
        ("nodeStates", POINTER(ControllerModelNodeStateMSFT)),
    ]


PFN_xrGetControllerModelKeyMSFT = CFUNCTYPE(Result, Session, Path, POINTER(ControllerModelKeyStateMSFT))

PFN_xrLoadControllerModelMSFT = CFUNCTYPE(Result, Session, ControllerModelKeyMSFT, c_uint32, c_uint32, c_uint8)

PFN_xrGetControllerModelPropertiesMSFT = CFUNCTYPE(Result, Session, ControllerModelKeyMSFT, POINTER(ControllerModelPropertiesMSFT))

PFN_xrGetControllerModelStateMSFT = CFUNCTYPE(Result, Session, ControllerModelKeyMSFT, POINTER(ControllerModelStateMSFT))


class ViewConfigurationViewFovEPIC(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("recommendedFov", Fovf),
        ("maxMutableFov", Fovf),
    ]


ReprojectionModeMSFT = c_int32


class CompositionLayerReprojectionInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("reprojectionMode", ReprojectionModeMSFT),
    ]


class CompositionLayerReprojectionPlaneOverrideMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("position", Vector3f),
        ("normal", Vector3f),
        ("velocity", Vector3f),
    ]


PFN_xrEnumerateReprojectionModesMSFT = CFUNCTYPE(Result, Instance, SystemId, ViewConfigurationType, c_uint32, c_uint32, POINTER(ReprojectionModeMSFT))


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
        ("onThreshold", c_float),
        ("offThreshold", c_float),
        ("onHaptic", POINTER(HapticBaseHeader)),
        ("offHaptic", POINTER(HapticBaseHeader)),
    ]


HandJointsMotionRangeEXT = c_int32


class HandJointsMotionRangeInfoEXT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("handJointsMotionRange", HandJointsMotionRangeEXT),
    ]


class SceneObserverMSFT_T(Structure):
    pass


SceneObserverMSFT = POINTER(SceneObserverMSFT_T)


class SceneMSFT_T(Structure):
    pass


SceneMSFT = POINTER(SceneMSFT_T)

SceneComputeFeatureMSFT = c_int32

SceneComputeConsistencyMSFT = c_int32

MeshComputeLodMSFT = c_int32

SceneComponentTypeMSFT = c_int32

SceneObjectTypeMSFT = c_int32

ScenePlaneAlignmentTypeMSFT = c_int32

SceneComputeStateMSFT = c_int32


class UuidMSFT(Structure):
    _fields_ = [
        ("bytes", c_uint8),
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
        ("farDistance", c_float),
    ]


class SceneBoundsMSFT(Structure):
    _fields_ = [
        ("space", Space),
        ("time", Time),
        ("sphereCount", c_uint32),
        ("spheres", POINTER(SceneSphereBoundMSFT)),
        ("boxCount", c_uint32),
        ("boxes", POINTER(SceneOrientedBoxBoundMSFT)),
        ("frustumCount", c_uint32),
        ("frustums", POINTER(SceneFrustumBoundMSFT)),
    ]


class NewSceneComputeInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("requestedFeatureCount", c_uint32),
        ("requestedFeatures", POINTER(SceneComputeFeatureMSFT)),
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
        ("componentType", SceneComponentTypeMSFT),
        ("id", UuidMSFT),
        ("parentId", UuidMSFT),
        ("updateTime", Time),
    ]


class SceneComponentsMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("componentCapacityInput", c_uint32),
        ("componentCountOutput", c_uint32),
        ("components", POINTER(SceneComponentMSFT)),
    ]


class SceneComponentsGetInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("componentType", SceneComponentTypeMSFT),
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
        ("locationCount", c_uint32),
        ("locations", POINTER(SceneComponentLocationMSFT)),
    ]


class SceneComponentsLocateInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("baseSpace", Space),
        ("time", Time),
        ("componentIdCount", c_uint32),
        ("componentIds", POINTER(UuidMSFT)),
    ]


class SceneObjectMSFT(Structure):
    _fields_ = [
        ("objectType", SceneObjectTypeMSFT),
    ]


class SceneObjectsMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("sceneObjectCount", c_uint32),
        ("sceneObjects", POINTER(SceneObjectMSFT)),
    ]


class SceneComponentParentFilterInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("parentId", UuidMSFT),
    ]


class SceneObjectTypesFilterInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("objectTypeCount", c_uint32),
        ("objectTypes", POINTER(SceneObjectTypeMSFT)),
    ]


class ScenePlaneMSFT(Structure):
    _fields_ = [
        ("alignment", ScenePlaneAlignmentTypeMSFT),
        ("size", Extent2Df),
        ("meshBufferId", c_uint64),
        ("supportsIndicesUint16", Bool32),
    ]


class ScenePlanesMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("scenePlaneCount", c_uint32),
        ("scenePlanes", POINTER(ScenePlaneMSFT)),
    ]


class ScenePlaneAlignmentFilterInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("alignmentCount", c_uint32),
        ("alignments", POINTER(ScenePlaneAlignmentTypeMSFT)),
    ]


class SceneMeshMSFT(Structure):
    _fields_ = [
        ("meshBufferId", c_uint64),
        ("supportsIndicesUint16", Bool32),
    ]


class SceneMeshesMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("sceneMeshCount", c_uint32),
        ("sceneMeshes", POINTER(SceneMeshMSFT)),
    ]


class SceneMeshBuffersGetInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("meshBufferId", c_uint64),
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
        ("vertexCapacityInput", c_uint32),
        ("vertexCountOutput", c_uint32),
        ("vertices", POINTER(Vector3f)),
    ]


class SceneMeshIndicesUint32MSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("indexCapacityInput", c_uint32),
        ("indexCountOutput", c_uint32),
        ("indices", c_uint32),
    ]


class SceneMeshIndicesUint16MSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("indexCapacityInput", c_uint32),
        ("indexCountOutput", c_uint32),
        ("indices", c_uint16),
    ]


PFN_xrEnumerateSceneComputeFeaturesMSFT = CFUNCTYPE(Result, Instance, SystemId, c_uint32, c_uint32, POINTER(SceneComputeFeatureMSFT))

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
        ("sceneFragmentId", UuidMSFT),
    ]


class DeserializeSceneFragmentMSFT(Structure):
    _fields_ = [
        ("bufferSize", c_uint32),
        ("buffer", c_uint8),
    ]


class SceneDeserializeInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("fragmentCount", c_uint32),
        ("fragments", POINTER(DeserializeSceneFragmentMSFT)),
    ]


PFN_xrDeserializeSceneMSFT = CFUNCTYPE(Result, SceneObserverMSFT, POINTER(SceneDeserializeInfoMSFT))

PFN_xrGetSerializedSceneFragmentDataMSFT = CFUNCTYPE(Result, SceneMSFT, POINTER(SerializedSceneFragmentDataGetInfoMSFT), c_uint32, c_uint32, c_uint8)


class EventDataDisplayRefreshRateChangedFB(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("fromDisplayRefreshRate", c_float),
        ("toDisplayRefreshRate", c_float),
    ]


PFN_xrEnumerateDisplayRefreshRatesFB = CFUNCTYPE(Result, Session, c_uint32, c_uint32, POINTER(c_float))

PFN_xrGetDisplayRefreshRateFB = CFUNCTYPE(Result, Session, POINTER(c_float))

PFN_xrRequestDisplayRefreshRateFB = CFUNCTYPE(Result, Session, c_float)

ColorSpaceFB = c_int32


class SystemColorSpacePropertiesFB(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("colorSpace", ColorSpaceFB),
    ]


PFN_xrEnumerateColorSpacesFB = CFUNCTYPE(Result, Session, c_uint32, c_uint32, POINTER(ColorSpaceFB))

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

FoveationLevelFB = c_int32

FoveationDynamicFB = c_int32


class FoveationLevelProfileCreateInfoFB(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("level", FoveationLevelFB),
        ("verticalOffset", c_float),
        ("dynamic", FoveationDynamicFB),
    ]


class ViewLocateFoveatedRenderingVARJO(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("foveatedRenderingActive", Bool32),
    ]


class FoveatedViewConfigurationViewVARJO(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("foveatedRenderingActive", Bool32),
    ]


class SystemFoveatedRenderingPropertiesVARJO(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("supportsFoveatedRendering", Bool32),
    ]


class CompositionLayerDepthTestVARJO(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("depthTestRangeNearZ", c_float),
        ("depthTestRangeFarZ", c_float),
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
        ("spatialAnchorPersistenceName", SpatialAnchorPersistenceNameMSFT),
        ("spatialAnchor", SpatialAnchorMSFT),
    ]


class SpatialAnchorFromPersistedAnchorCreateInfoMSFT(Structure):
    _fields_ = [
        ("type", StructureType),
        ("next", c_void_p),
        ("spatialAnchorStore", SpatialAnchorStoreConnectionMSFT),
        ("spatialAnchorPersistenceName", SpatialAnchorPersistenceNameMSFT),
    ]


PFN_xrCreateSpatialAnchorStoreConnectionMSFT = CFUNCTYPE(Result, Session, POINTER(SpatialAnchorStoreConnectionMSFT))

PFN_xrDestroySpatialAnchorStoreConnectionMSFT = CFUNCTYPE(Result, SpatialAnchorStoreConnectionMSFT)

PFN_xrPersistSpatialAnchorMSFT = CFUNCTYPE(Result, SpatialAnchorStoreConnectionMSFT, POINTER(SpatialAnchorPersistenceInfoMSFT))

PFN_xrEnumeratePersistedSpatialAnchorNamesMSFT = CFUNCTYPE(Result, SpatialAnchorStoreConnectionMSFT, c_uint32, c_uint32, POINTER(SpatialAnchorPersistenceNameMSFT))

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
    "Result",
    "StructureType",
    "FormFactor",
    "ViewConfigurationType",
    "EnvironmentBlendMode",
    "ReferenceSpaceType",
    "ActionType",
    "EyeVisibility",
    "SessionState",
    "ObjectType",
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
    "VisibilityMaskTypeKHR",
    "VisibilityMaskKHR",
    "EventDataVisibilityMaskChangedKHR",
    "PFN_xrGetVisibilityMaskKHR",
    "CompositionLayerColorScaleBiasKHR",
    "LoaderInitInfoBaseHeaderKHR",
    "PFN_xrInitializeLoaderKHR",
    "CompositionLayerEquirect2KHR",
    "BindingModificationBaseHeaderKHR",
    "BindingModificationsKHR",
    "PerfSettingsDomainEXT",
    "PerfSettingsSubDomainEXT",
    "PerfSettingsLevelEXT",
    "PerfSettingsNotificationLevelEXT",
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
    "BlendFactorFB",
    "CompositionLayerAlphaBlendFB",
    "ViewConfigurationDepthRangeEXT",
    "PFN_xrSetInputDeviceActiveEXT",
    "PFN_xrSetInputDeviceStateBoolEXT",
    "PFN_xrSetInputDeviceStateFloatEXT",
    "PFN_xrSetInputDeviceStateVector2fEXT",
    "PFN_xrSetInputDeviceLocationEXT",
    "SpatialGraphNodeTypeMSFT",
    "SpatialGraphNodeSpaceCreateInfoMSFT",
    "PFN_xrCreateSpatialGraphNodeSpaceMSFT",
    "HandTrackerEXT_T",
    "HandTrackerEXT",
    "HandEXT",
    "HandJointEXT",
    "HandJointSetEXT",
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
    "HandPoseTypeMSFT",
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
    "ReprojectionModeMSFT",
    "CompositionLayerReprojectionInfoMSFT",
    "CompositionLayerReprojectionPlaneOverrideMSFT",
    "PFN_xrEnumerateReprojectionModesMSFT",
    "SwapchainStateBaseHeaderFB",
    "PFN_xrUpdateSwapchainFB",
    "PFN_xrGetSwapchainStateFB",
    "CompositionLayerSecureContentFlagsFB",
    "CompositionLayerSecureContentFB",
    "InteractionProfileAnalogThresholdVALVE",
    "HandJointsMotionRangeEXT",
    "HandJointsMotionRangeInfoEXT",
    "SceneObserverMSFT_T",
    "SceneObserverMSFT",
    "SceneMSFT_T",
    "SceneMSFT",
    "SceneComputeFeatureMSFT",
    "SceneComputeConsistencyMSFT",
    "MeshComputeLodMSFT",
    "SceneComponentTypeMSFT",
    "SceneObjectTypeMSFT",
    "ScenePlaneAlignmentTypeMSFT",
    "SceneComputeStateMSFT",
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
    "ColorSpaceFB",
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
    "FoveationLevelFB",
    "FoveationDynamicFB",
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
