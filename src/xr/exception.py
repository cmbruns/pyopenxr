from typing import Optional
from .enums import Result

# raise_on_qualified_success is a module setting to control whether positive non-SUCCESS result
# trigger exceptions.
raise_on_qualified_success = True


class XrException(Exception):
    """Base class for all OpenXR exceptions."""

    @staticmethod
    def is_exception() -> bool:
        return True


class ResultException(XrException):
    """Exception related to return value of and OpenXR function."""

    @staticmethod
    def get_result_enum() -> Optional[Result]:
        return None

    @staticmethod
    def is_exception() -> bool:
        return False


class ErrorResult(ResultException):
    """Error during OpenXR function call."""

    @staticmethod
    def is_exception() -> bool:
        return True


class QualifiedSuccessResult(ResultException):
    """An OpenXR function returned a non-error status other than SUCCESS"""

    @staticmethod
    def is_exception() -> bool:
        return raise_on_qualified_success


class Success(ResultException):
    """Function successfully completed."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "Function successfully completed."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.SUCCESS


class TimeoutExpired(QualifiedSuccessResult):
    """The specified timeout time occurred before the operation could complete."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The specified timeout time occurred before the operation could complete."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.TIMEOUT_EXPIRED


class SessionLossPending(QualifiedSuccessResult):
    """The session will be lost soon."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The session will be lost soon."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.SESSION_LOSS_PENDING


class EventUnavailable(QualifiedSuccessResult):
    """No event was available."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "No event was available."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.EVENT_UNAVAILABLE


class SpaceBoundsUnavailable(QualifiedSuccessResult):
    """The space's bounds are not known at the moment."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The space's bounds are not known at the moment."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.SPACE_BOUNDS_UNAVAILABLE


class SessionNotFocused(QualifiedSuccessResult):
    """The session is not in the focused state."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The session is not in the focused state."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.SESSION_NOT_FOCUSED


class FrameDiscarded(QualifiedSuccessResult):
    """A frame has been discarded from composition."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "A frame has been discarded from composition."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.FRAME_DISCARDED


class ValidationFailureError(ErrorResult):
    """The function usage was invalid in some way."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The function usage was invalid in some way."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_VALIDATION_FAILURE


class RuntimeFailureError(ErrorResult):
    """The runtime failed to handle the function in an unexpected way that is not covered by another error result. """

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The runtime failed to handle the function in an unexpected way that is not covered by another error result. "
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_RUNTIME_FAILURE


class OutOfMemoryError(ErrorResult):
    """A memory allocation has failed."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "A memory allocation has failed."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_OUT_OF_MEMORY


class ApiVersionUnsupportedError(ErrorResult):
    """The runtime does not support the requested API version."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The runtime does not support the requested API version."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_API_VERSION_UNSUPPORTED


class InitializationFailedError(ErrorResult):
    """Initialization of object could not be completed."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "Initialization of object could not be completed."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_INITIALIZATION_FAILED


class FunctionUnsupportedError(ErrorResult):
    """The requested function was not found or is otherwise unsupported."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The requested function was not found or is otherwise unsupported."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_FUNCTION_UNSUPPORTED


class FeatureUnsupportedError(ErrorResult):
    """The requested feature is not supported."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The requested feature is not supported."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_FEATURE_UNSUPPORTED


class ExtensionNotPresentError(ErrorResult):
    """A requested extension is not supported."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "A requested extension is not supported."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_EXTENSION_NOT_PRESENT


class LimitReachedError(ErrorResult):
    """The runtime supports no more of the requested resource."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The runtime supports no more of the requested resource."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_LIMIT_REACHED


class SizeInsufficientError(ErrorResult):
    """The supplied size was smaller than required."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The supplied size was smaller than required."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_SIZE_INSUFFICIENT


class HandleInvalidError(ErrorResult):
    """A supplied object handle was invalid."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "A supplied object handle was invalid."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_HANDLE_INVALID


class InstanceLostError(ErrorResult):
    """The slink:XrInstance was lost or could not be found. It will need to be destroyed and optionally recreated."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The slink:XrInstance was lost or could not be found. It will need to be destroyed and optionally recreated."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_INSTANCE_LOST


class SessionRunningError(ErrorResult):
    """The session <<session_running, is already running>>."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The session <<session_running, is already running>>."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_SESSION_RUNNING


class SessionNotRunningError(ErrorResult):
    """The session <<session_not_running, is not yet running>>."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The session <<session_not_running, is not yet running>>."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_SESSION_NOT_RUNNING


class SessionLostError(ErrorResult):
    """The slink:XrSession was lost. It will need to be destroyed and optionally recreated."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The slink:XrSession was lost. It will need to be destroyed and optionally recreated."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_SESSION_LOST


class SystemInvalidError(ErrorResult):
    """The provided basetype:XrSystemId was invalid."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The provided basetype:XrSystemId was invalid."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_SYSTEM_INVALID


class PathInvalidError(ErrorResult):
    """The provided basetype:XrPath was not valid."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The provided basetype:XrPath was not valid."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_PATH_INVALID


class PathCountExceededError(ErrorResult):
    """The maximum number of supported semantic paths has been reached."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The maximum number of supported semantic paths has been reached."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_PATH_COUNT_EXCEEDED


class PathFormatInvalidError(ErrorResult):
    """The semantic path character format is invalid."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The semantic path character format is invalid."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_PATH_FORMAT_INVALID


class PathUnsupportedError(ErrorResult):
    """The semantic path is unsupported."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The semantic path is unsupported."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_PATH_UNSUPPORTED


class LayerInvalidError(ErrorResult):
    """The layer was NULL or otherwise invalid."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The layer was NULL or otherwise invalid."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_LAYER_INVALID


class LayerLimitExceededError(ErrorResult):
    """The number of specified layers is greater than the supported number."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The number of specified layers is greater than the supported number."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_LAYER_LIMIT_EXCEEDED


class SwapchainRectInvalidError(ErrorResult):
    """The image rect was negatively sized or otherwise invalid."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The image rect was negatively sized or otherwise invalid."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_SWAPCHAIN_RECT_INVALID


class SwapchainFormatUnsupportedError(ErrorResult):
    """The image format is not supported by the runtime or platform."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The image format is not supported by the runtime or platform."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_SWAPCHAIN_FORMAT_UNSUPPORTED


class ActionTypeMismatchError(ErrorResult):
    """The API used to retrieve an action's state does not match the action's type."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The API used to retrieve an action's state does not match the action's type."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_ACTION_TYPE_MISMATCH


class SessionNotReadyError(ErrorResult):
    """The session is not in the ready state."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The session is not in the ready state."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_SESSION_NOT_READY


class SessionNotStoppingError(ErrorResult):
    """The session is not in the stopping state."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The session is not in the stopping state."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_SESSION_NOT_STOPPING


class TimeInvalidError(ErrorResult):
    """The provided basetype:XrTime was zero, negative, or out of range."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The provided basetype:XrTime was zero, negative, or out of range."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_TIME_INVALID


class ReferenceSpaceUnsupportedError(ErrorResult):
    """The specified reference space is not supported by the runtime or system."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The specified reference space is not supported by the runtime or system."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_REFERENCE_SPACE_UNSUPPORTED


class FileAccessErrorError(ErrorResult):
    """The file could not be accessed."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The file could not be accessed."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_FILE_ACCESS_ERROR


class FileContentsInvalidError(ErrorResult):
    """The file's contents were invalid."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The file's contents were invalid."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_FILE_CONTENTS_INVALID


class FormFactorUnsupportedError(ErrorResult):
    """The specified form factor is not supported by the current runtime or platform."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The specified form factor is not supported by the current runtime or platform."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_FORM_FACTOR_UNSUPPORTED


class FormFactorUnavailableError(ErrorResult):
    """The specified form factor is supported, but the device is currently not available, e.g. not plugged in or powered off."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The specified form factor is supported, but the device is currently not available, e.g. not plugged in or powered off."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_FORM_FACTOR_UNAVAILABLE


class ApiLayerNotPresentError(ErrorResult):
    """A requested API layer is not present or could not be loaded."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "A requested API layer is not present or could not be loaded."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_API_LAYER_NOT_PRESENT


class CallOrderInvalidError(ErrorResult):
    """The call was made without having made a previously required call."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The call was made without having made a previously required call."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_CALL_ORDER_INVALID


class GraphicsDeviceInvalidError(ErrorResult):
    """The given graphics device is not in a valid state. The graphics device could be lost or initialized without meeting graphics requirements."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The given graphics device is not in a valid state. The graphics device could be lost or initialized without meeting graphics requirements."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_GRAPHICS_DEVICE_INVALID


class PoseInvalidError(ErrorResult):
    """The supplied pose was invalid with respect to the requirements."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The supplied pose was invalid with respect to the requirements."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_POSE_INVALID


class IndexOutOfRangeError(ErrorResult):
    """The supplied index was outside the range of valid indices."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The supplied index was outside the range of valid indices."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_INDEX_OUT_OF_RANGE


class ViewConfigurationTypeUnsupportedError(ErrorResult):
    """The specified view configuration type is not supported by the runtime or platform."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The specified view configuration type is not supported by the runtime or platform."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_VIEW_CONFIGURATION_TYPE_UNSUPPORTED


class EnvironmentBlendModeUnsupportedError(ErrorResult):
    """The specified environment blend mode is not supported by the runtime or platform."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The specified environment blend mode is not supported by the runtime or platform."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_ENVIRONMENT_BLEND_MODE_UNSUPPORTED


class NameDuplicatedError(ErrorResult):
    """The name provided was a duplicate of an already-existing resource."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The name provided was a duplicate of an already-existing resource."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_NAME_DUPLICATED


class NameInvalidError(ErrorResult):
    """The name provided was invalid."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The name provided was invalid."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_NAME_INVALID


class ActionsetNotAttachedError(ErrorResult):
    """A referenced action set is not attached to the session."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "A referenced action set is not attached to the session."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_ACTIONSET_NOT_ATTACHED


class ActionsetsAlreadyAttachedError(ErrorResult):
    """The session already has attached action sets."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The session already has attached action sets."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_ACTIONSETS_ALREADY_ATTACHED


class LocalizedNameDuplicatedError(ErrorResult):
    """The localized name provided was a duplicate of an already-existing resource."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The localized name provided was a duplicate of an already-existing resource."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_LOCALIZED_NAME_DUPLICATED


class LocalizedNameInvalidError(ErrorResult):
    """The localized name provided was invalid."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The localized name provided was invalid."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_LOCALIZED_NAME_INVALID


class GraphicsRequirementsCallMissingError(ErrorResult):
    """The fname:xrGetGraphicsRequirements* call was not made before calling fname:xrCreateSession."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The fname:xrGetGraphicsRequirements* call was not made before calling fname:xrCreateSession."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_GRAPHICS_REQUIREMENTS_CALL_MISSING


class RuntimeUnavailableError(ErrorResult):
    """The loader was unable to find or load a runtime."""

    def __init__(self, message=None):
        if message is None:
            super().__init__(
                "The loader was unable to find or load a runtime."
            )
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_RUNTIME_UNAVAILABLE


class AndroidThreadSettingsIdInvalidKHRError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_ANDROID_THREAD_SETTINGS_ID_INVALID_KHR


class AndroidThreadSettingsFailureKHRError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_ANDROID_THREAD_SETTINGS_FAILURE_KHR


class CreateSpatialAnchorFailedMSFTError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_CREATE_SPATIAL_ANCHOR_FAILED_MSFT


class SecondaryViewConfigurationTypeNotEnabledMSFTError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_SECONDARY_VIEW_CONFIGURATION_TYPE_NOT_ENABLED_MSFT


class ControllerModelKeyInvalidMSFTError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_CONTROLLER_MODEL_KEY_INVALID_MSFT


class ReprojectionModeUnsupportedMSFTError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_REPROJECTION_MODE_UNSUPPORTED_MSFT


class ComputeNewSceneNotCompletedMSFTError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_COMPUTE_NEW_SCENE_NOT_COMPLETED_MSFT


class SceneComponentIdInvalidMSFTError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_SCENE_COMPONENT_ID_INVALID_MSFT


class SceneComponentTypeMismatchMSFTError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_SCENE_COMPONENT_TYPE_MISMATCH_MSFT


class SceneMeshBufferIdInvalidMSFTError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_SCENE_MESH_BUFFER_ID_INVALID_MSFT


class SceneComputeFeatureIncompatibleMSFTError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_SCENE_COMPUTE_FEATURE_INCOMPATIBLE_MSFT


class SceneComputeConsistencyMismatchMSFTError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_SCENE_COMPUTE_CONSISTENCY_MISMATCH_MSFT


class DisplayRefreshRateUnsupportedFBError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_DISPLAY_REFRESH_RATE_UNSUPPORTED_FB


class ColorSpaceUnsupportedFBError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_COLOR_SPACE_UNSUPPORTED_FB


class UnexpectedStatePassthroughFBError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_UNEXPECTED_STATE_PASSTHROUGH_FB


class FeatureAlreadyCreatedPassthroughFBError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_FEATURE_ALREADY_CREATED_PASSTHROUGH_FB


class FeatureRequiredPassthroughFBError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_FEATURE_REQUIRED_PASSTHROUGH_FB


class NotPermittedPassthroughFBError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_NOT_PERMITTED_PASSTHROUGH_FB


class InsufficientResourcesPassthroughFBError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_INSUFFICIENT_RESOURCES_PASSTHROUGH_FB


class UnknownPassthroughFBError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_UNKNOWN_PASSTHROUGH_FB


class RenderModelKeyInvalidFBError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_RENDER_MODEL_KEY_INVALID_FB


class RenderModelUnavailableFB(QualifiedSuccessResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.RENDER_MODEL_UNAVAILABLE_FB


class MarkerNotTrackedVarjoError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_MARKER_NOT_TRACKED_VARJO


class MarkerIdInvalidVarjoError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_MARKER_ID_INVALID_VARJO


class SpatialAnchorNameNotFoundMSFTError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_SPATIAL_ANCHOR_NAME_NOT_FOUND_MSFT


class SpatialAnchorNameInvalidMSFTError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_SPATIAL_ANCHOR_NAME_INVALID_MSFT


_exception_map = {
    Result.SUCCESS: Success,
    Result.TIMEOUT_EXPIRED: TimeoutExpired,
    Result.SESSION_LOSS_PENDING: SessionLossPending,
    Result.EVENT_UNAVAILABLE: EventUnavailable,
    Result.SPACE_BOUNDS_UNAVAILABLE: SpaceBoundsUnavailable,
    Result.SESSION_NOT_FOCUSED: SessionNotFocused,
    Result.FRAME_DISCARDED: FrameDiscarded,
    Result.ERROR_VALIDATION_FAILURE: ValidationFailureError,
    Result.ERROR_RUNTIME_FAILURE: RuntimeFailureError,
    Result.ERROR_OUT_OF_MEMORY: OutOfMemoryError,
    Result.ERROR_API_VERSION_UNSUPPORTED: ApiVersionUnsupportedError,
    Result.ERROR_INITIALIZATION_FAILED: InitializationFailedError,
    Result.ERROR_FUNCTION_UNSUPPORTED: FunctionUnsupportedError,
    Result.ERROR_FEATURE_UNSUPPORTED: FeatureUnsupportedError,
    Result.ERROR_EXTENSION_NOT_PRESENT: ExtensionNotPresentError,
    Result.ERROR_LIMIT_REACHED: LimitReachedError,
    Result.ERROR_SIZE_INSUFFICIENT: SizeInsufficientError,
    Result.ERROR_HANDLE_INVALID: HandleInvalidError,
    Result.ERROR_INSTANCE_LOST: InstanceLostError,
    Result.ERROR_SESSION_RUNNING: SessionRunningError,
    Result.ERROR_SESSION_NOT_RUNNING: SessionNotRunningError,
    Result.ERROR_SESSION_LOST: SessionLostError,
    Result.ERROR_SYSTEM_INVALID: SystemInvalidError,
    Result.ERROR_PATH_INVALID: PathInvalidError,
    Result.ERROR_PATH_COUNT_EXCEEDED: PathCountExceededError,
    Result.ERROR_PATH_FORMAT_INVALID: PathFormatInvalidError,
    Result.ERROR_PATH_UNSUPPORTED: PathUnsupportedError,
    Result.ERROR_LAYER_INVALID: LayerInvalidError,
    Result.ERROR_LAYER_LIMIT_EXCEEDED: LayerLimitExceededError,
    Result.ERROR_SWAPCHAIN_RECT_INVALID: SwapchainRectInvalidError,
    Result.ERROR_SWAPCHAIN_FORMAT_UNSUPPORTED: SwapchainFormatUnsupportedError,
    Result.ERROR_ACTION_TYPE_MISMATCH: ActionTypeMismatchError,
    Result.ERROR_SESSION_NOT_READY: SessionNotReadyError,
    Result.ERROR_SESSION_NOT_STOPPING: SessionNotStoppingError,
    Result.ERROR_TIME_INVALID: TimeInvalidError,
    Result.ERROR_REFERENCE_SPACE_UNSUPPORTED: ReferenceSpaceUnsupportedError,
    Result.ERROR_FILE_ACCESS_ERROR: FileAccessErrorError,
    Result.ERROR_FILE_CONTENTS_INVALID: FileContentsInvalidError,
    Result.ERROR_FORM_FACTOR_UNSUPPORTED: FormFactorUnsupportedError,
    Result.ERROR_FORM_FACTOR_UNAVAILABLE: FormFactorUnavailableError,
    Result.ERROR_API_LAYER_NOT_PRESENT: ApiLayerNotPresentError,
    Result.ERROR_CALL_ORDER_INVALID: CallOrderInvalidError,
    Result.ERROR_GRAPHICS_DEVICE_INVALID: GraphicsDeviceInvalidError,
    Result.ERROR_POSE_INVALID: PoseInvalidError,
    Result.ERROR_INDEX_OUT_OF_RANGE: IndexOutOfRangeError,
    Result.ERROR_VIEW_CONFIGURATION_TYPE_UNSUPPORTED: ViewConfigurationTypeUnsupportedError,
    Result.ERROR_ENVIRONMENT_BLEND_MODE_UNSUPPORTED: EnvironmentBlendModeUnsupportedError,
    Result.ERROR_NAME_DUPLICATED: NameDuplicatedError,
    Result.ERROR_NAME_INVALID: NameInvalidError,
    Result.ERROR_ACTIONSET_NOT_ATTACHED: ActionsetNotAttachedError,
    Result.ERROR_ACTIONSETS_ALREADY_ATTACHED: ActionsetsAlreadyAttachedError,
    Result.ERROR_LOCALIZED_NAME_DUPLICATED: LocalizedNameDuplicatedError,
    Result.ERROR_LOCALIZED_NAME_INVALID: LocalizedNameInvalidError,
    Result.ERROR_GRAPHICS_REQUIREMENTS_CALL_MISSING: GraphicsRequirementsCallMissingError,
    Result.ERROR_RUNTIME_UNAVAILABLE: RuntimeUnavailableError,
    Result.ERROR_ANDROID_THREAD_SETTINGS_ID_INVALID_KHR: AndroidThreadSettingsIdInvalidKHRError,
    Result.ERROR_ANDROID_THREAD_SETTINGS_FAILURE_KHR: AndroidThreadSettingsFailureKHRError,
    Result.ERROR_CREATE_SPATIAL_ANCHOR_FAILED_MSFT: CreateSpatialAnchorFailedMSFTError,
    Result.ERROR_SECONDARY_VIEW_CONFIGURATION_TYPE_NOT_ENABLED_MSFT: SecondaryViewConfigurationTypeNotEnabledMSFTError,
    Result.ERROR_CONTROLLER_MODEL_KEY_INVALID_MSFT: ControllerModelKeyInvalidMSFTError,
    Result.ERROR_REPROJECTION_MODE_UNSUPPORTED_MSFT: ReprojectionModeUnsupportedMSFTError,
    Result.ERROR_COMPUTE_NEW_SCENE_NOT_COMPLETED_MSFT: ComputeNewSceneNotCompletedMSFTError,
    Result.ERROR_SCENE_COMPONENT_ID_INVALID_MSFT: SceneComponentIdInvalidMSFTError,
    Result.ERROR_SCENE_COMPONENT_TYPE_MISMATCH_MSFT: SceneComponentTypeMismatchMSFTError,
    Result.ERROR_SCENE_MESH_BUFFER_ID_INVALID_MSFT: SceneMeshBufferIdInvalidMSFTError,
    Result.ERROR_SCENE_COMPUTE_FEATURE_INCOMPATIBLE_MSFT: SceneComputeFeatureIncompatibleMSFTError,
    Result.ERROR_SCENE_COMPUTE_CONSISTENCY_MISMATCH_MSFT: SceneComputeConsistencyMismatchMSFTError,
    Result.ERROR_DISPLAY_REFRESH_RATE_UNSUPPORTED_FB: DisplayRefreshRateUnsupportedFBError,
    Result.ERROR_COLOR_SPACE_UNSUPPORTED_FB: ColorSpaceUnsupportedFBError,
    Result.ERROR_UNEXPECTED_STATE_PASSTHROUGH_FB: UnexpectedStatePassthroughFBError,
    Result.ERROR_FEATURE_ALREADY_CREATED_PASSTHROUGH_FB: FeatureAlreadyCreatedPassthroughFBError,
    Result.ERROR_FEATURE_REQUIRED_PASSTHROUGH_FB: FeatureRequiredPassthroughFBError,
    Result.ERROR_NOT_PERMITTED_PASSTHROUGH_FB: NotPermittedPassthroughFBError,
    Result.ERROR_INSUFFICIENT_RESOURCES_PASSTHROUGH_FB: InsufficientResourcesPassthroughFBError,
    Result.ERROR_UNKNOWN_PASSTHROUGH_FB: UnknownPassthroughFBError,
    Result.ERROR_RENDER_MODEL_KEY_INVALID_FB: RenderModelKeyInvalidFBError,
    Result.RENDER_MODEL_UNAVAILABLE_FB: RenderModelUnavailableFB,
    Result.ERROR_MARKER_NOT_TRACKED_VARJO: MarkerNotTrackedVarjoError,
    Result.ERROR_MARKER_ID_INVALID_VARJO: MarkerIdInvalidVarjoError,
    Result.ERROR_SPATIAL_ANCHOR_NAME_NOT_FOUND_MSFT: SpatialAnchorNameNotFoundMSFTError,
    Result.ERROR_SPATIAL_ANCHOR_NAME_INVALID_MSFT: SpatialAnchorNameInvalidMSFTError,
}


def check_result(
    xr_result: Result, message: str = None
) -> XrException:
    if xr_result in _exception_map:
        xr_result_exception = _exception_map[xr_result]
    else:
        if xr_result.value < 0:
            xr_result_exception = ErrorResult
        elif xr_result.value > 1:
            xr_result_exception = QualifiedSuccessResult
        else:
            xr_result_exception = Success
    if message is None:
        # TODO: I see a message in the logging...
        return xr_result_exception()
    else:
        return xr_result_exception(message)


__all__ = [
    "ActionTypeMismatchError",
    "ActionsetNotAttachedError",
    "ActionsetsAlreadyAttachedError",
    "AndroidThreadSettingsFailureKHRError",
    "AndroidThreadSettingsIdInvalidKHRError",
    "ApiLayerNotPresentError",
    "ApiVersionUnsupportedError",
    "CallOrderInvalidError",
    "ColorSpaceUnsupportedFBError",
    "ComputeNewSceneNotCompletedMSFTError",
    "ControllerModelKeyInvalidMSFTError",
    "CreateSpatialAnchorFailedMSFTError",
    "DisplayRefreshRateUnsupportedFBError",
    "EnvironmentBlendModeUnsupportedError",
    "ErrorResult",
    "EventUnavailable",
    "ExtensionNotPresentError",
    "FeatureAlreadyCreatedPassthroughFBError",
    "FeatureRequiredPassthroughFBError",
    "FeatureUnsupportedError",
    "FileAccessErrorError",
    "FileContentsInvalidError",
    "FormFactorUnavailableError",
    "FormFactorUnsupportedError",
    "FrameDiscarded",
    "FunctionUnsupportedError",
    "GraphicsDeviceInvalidError",
    "GraphicsRequirementsCallMissingError",
    "HandleInvalidError",
    "IndexOutOfRangeError",
    "InitializationFailedError",
    "InstanceLostError",
    "InsufficientResourcesPassthroughFBError",
    "LayerInvalidError",
    "LayerLimitExceededError",
    "LimitReachedError",
    "LocalizedNameDuplicatedError",
    "LocalizedNameInvalidError",
    "MarkerIdInvalidVarjoError",
    "MarkerNotTrackedVarjoError",
    "NameDuplicatedError",
    "NameInvalidError",
    "NotPermittedPassthroughFBError",
    "OutOfMemoryError",
    "PathCountExceededError",
    "PathFormatInvalidError",
    "PathInvalidError",
    "PathUnsupportedError",
    "PoseInvalidError",
    "QualifiedSuccessResult",
    "ReferenceSpaceUnsupportedError",
    "RenderModelKeyInvalidFBError",
    "RenderModelUnavailableFB",
    "ReprojectionModeUnsupportedMSFTError",
    "ResultException",
    "RuntimeFailureError",
    "RuntimeUnavailableError",
    "SceneComponentIdInvalidMSFTError",
    "SceneComponentTypeMismatchMSFTError",
    "SceneComputeConsistencyMismatchMSFTError",
    "SceneComputeFeatureIncompatibleMSFTError",
    "SceneMeshBufferIdInvalidMSFTError",
    "SecondaryViewConfigurationTypeNotEnabledMSFTError",
    "SessionLossPending",
    "SessionLostError",
    "SessionNotFocused",
    "SessionNotReadyError",
    "SessionNotRunningError",
    "SessionNotStoppingError",
    "SessionRunningError",
    "SizeInsufficientError",
    "SpaceBoundsUnavailable",
    "SpatialAnchorNameInvalidMSFTError",
    "SpatialAnchorNameNotFoundMSFTError",
    "Success",
    "SwapchainFormatUnsupportedError",
    "SwapchainRectInvalidError",
    "SystemInvalidError",
    "TimeInvalidError",
    "TimeoutExpired",
    "UnexpectedStatePassthroughFBError",
    "UnknownPassthroughFBError",
    "ValidationFailureError",
    "ViewConfigurationTypeUnsupportedError",
    "XrException",
    "check_result",
]
