# Warning: this file is auto-generated. Do not edit.

from ctypes import c_int
import enum


class DefaultEnumMeta(enum.EnumMeta):
    """
    Metaclass to allow default values in enumerations.

    https://stackoverflow.com/questions/44867597/is-there-a-way-to-specify-a-default-value-for-python-enums
    """
    default = object()

    def __call__(cls, value=default, *args, **kwargs):
        if value is DefaultEnumMeta.default:
            # Assume the first enum is default
            return next(iter(cls))
        return super().__call__(value, *args, **kwargs)


class SpaceVelocityFlagBits(enum.Flag, metaclass=DefaultEnumMeta):
    NONE = 0x00000000
    LINEAR_VALID = 0x00000001
    ANGULAR_VALID = 0x00000002


class EnumBase(enum.Enum):
    @staticmethod
    def ctype():
        return c_int


class Result(EnumBase):
    SUCCESS = 0
    TIMEOUT_EXPIRED = 1
    SESSION_LOSS_PENDING = 3
    EVENT_UNAVAILABLE = 4
    SPACE_BOUNDS_UNAVAILABLE = 7
    SESSION_NOT_FOCUSED = 8
    FRAME_DISCARDED = 9
    ERROR_VALIDATION_FAILURE = -1
    ERROR_RUNTIME_FAILURE = -2
    ERROR_OUT_OF_MEMORY = -3
    ERROR_API_VERSION_UNSUPPORTED = -4
    ERROR_INITIALIZATION_FAILED = -6
    ERROR_FUNCTION_UNSUPPORTED = -7
    ERROR_FEATURE_UNSUPPORTED = -8
    ERROR_EXTENSION_NOT_PRESENT = -9
    ERROR_LIMIT_REACHED = -10
    ERROR_SIZE_INSUFFICIENT = -11
    ERROR_HANDLE_INVALID = -12
    ERROR_INSTANCE_LOST = -13
    ERROR_SESSION_RUNNING = -14
    ERROR_SESSION_NOT_RUNNING = -16
    ERROR_SESSION_LOST = -17
    ERROR_SYSTEM_INVALID = -18
    ERROR_PATH_INVALID = -19
    ERROR_PATH_COUNT_EXCEEDED = -20
    ERROR_PATH_FORMAT_INVALID = -21
    ERROR_PATH_UNSUPPORTED = -22
    ERROR_LAYER_INVALID = -23
    ERROR_LAYER_LIMIT_EXCEEDED = -24
    ERROR_SWAPCHAIN_RECT_INVALID = -25
    ERROR_SWAPCHAIN_FORMAT_UNSUPPORTED = -26
    ERROR_ACTION_TYPE_MISMATCH = -27
    ERROR_SESSION_NOT_READY = -28
    ERROR_SESSION_NOT_STOPPING = -29
    ERROR_TIME_INVALID = -30
    ERROR_REFERENCE_SPACE_UNSUPPORTED = -31
    ERROR_FILE_ACCESS_ERROR = -32
    ERROR_FILE_CONTENTS_INVALID = -33
    ERROR_FORM_FACTOR_UNSUPPORTED = -34
    ERROR_FORM_FACTOR_UNAVAILABLE = -35
    ERROR_API_LAYER_NOT_PRESENT = -36
    ERROR_CALL_ORDER_INVALID = -37
    ERROR_GRAPHICS_DEVICE_INVALID = -38
    ERROR_POSE_INVALID = -39
    ERROR_INDEX_OUT_OF_RANGE = -40
    ERROR_VIEW_CONFIGURATION_TYPE_UNSUPPORTED = -41
    ERROR_ENVIRONMENT_BLEND_MODE_UNSUPPORTED = -42
    ERROR_NAME_DUPLICATED = -44
    ERROR_NAME_INVALID = -45
    ERROR_ACTIONSET_NOT_ATTACHED = -46
    ERROR_ACTIONSETS_ALREADY_ATTACHED = -47
    ERROR_LOCALIZED_NAME_DUPLICATED = -48
    ERROR_LOCALIZED_NAME_INVALID = -49
    ERROR_GRAPHICS_REQUIREMENTS_CALL_MISSING = -50
    ERROR_RUNTIME_UNAVAILABLE = -51
    ERROR_ANDROID_THREAD_SETTINGS_ID_INVALID_KHR = -1000003000
    ERROR_ANDROID_THREAD_SETTINGS_FAILURE_KHR = -1000003001
    ERROR_CREATE_SPATIAL_ANCHOR_FAILED_MSFT = -1000039001
    ERROR_SECONDARY_VIEW_CONFIGURATION_TYPE_NOT_ENABLED_MSFT = -1000053000
    ERROR_CONTROLLER_MODEL_KEY_INVALID_MSFT = -1000055000
    ERROR_REPROJECTION_MODE_UNSUPPORTED_MSFT = -1000066000
    ERROR_COMPUTE_NEW_SCENE_NOT_COMPLETED_MSFT = -1000097000
    ERROR_SCENE_COMPONENT_ID_INVALID_MSFT = -1000097001
    ERROR_SCENE_COMPONENT_TYPE_MISMATCH_MSFT = -1000097002
    ERROR_SCENE_MESH_BUFFER_ID_INVALID_MSFT = -1000097003
    ERROR_SCENE_COMPUTE_FEATURE_INCOMPATIBLE_MSFT = -1000097004
    ERROR_SCENE_COMPUTE_CONSISTENCY_MISMATCH_MSFT = -1000097005
    ERROR_DISPLAY_REFRESH_RATE_UNSUPPORTED_FB = -1000101000
    ERROR_COLOR_SPACE_UNSUPPORTED_FB = -1000108000
    ERROR_SPATIAL_ANCHOR_NAME_NOT_FOUND_MSFT = -1000142001
    ERROR_SPATIAL_ANCHOR_NAME_INVALID_MSFT = -1000142002


class StructureType(EnumBase):
    UNKNOWN = 0
    API_LAYER_PROPERTIES = 1
    EXTENSION_PROPERTIES = 2
    INSTANCE_CREATE_INFO = 3
    SYSTEM_GET_INFO = 4
    SYSTEM_PROPERTIES = 5
    VIEW_LOCATE_INFO = 6
    VIEW = 7
    SESSION_CREATE_INFO = 8
    SWAPCHAIN_CREATE_INFO = 9
    SESSION_BEGIN_INFO = 10
    VIEW_STATE = 11
    FRAME_END_INFO = 12
    HAPTIC_VIBRATION = 13
    EVENT_DATA_BUFFER = 16
    EVENT_DATA_INSTANCE_LOSS_PENDING = 17
    EVENT_DATA_SESSION_STATE_CHANGED = 18
    ACTION_STATE_BOOLEAN = 23
    ACTION_STATE_FLOAT = 24
    ACTION_STATE_VECTOR2F = 25
    ACTION_STATE_POSE = 27
    ACTION_SET_CREATE_INFO = 28
    ACTION_CREATE_INFO = 29
    INSTANCE_PROPERTIES = 32
    FRAME_WAIT_INFO = 33
    COMPOSITION_LAYER_PROJECTION = 35
    COMPOSITION_LAYER_QUAD = 36
    REFERENCE_SPACE_CREATE_INFO = 37
    ACTION_SPACE_CREATE_INFO = 38
    EVENT_DATA_REFERENCE_SPACE_CHANGE_PENDING = 40
    VIEW_CONFIGURATION_VIEW = 41
    SPACE_LOCATION = 42
    SPACE_VELOCITY = 43
    FRAME_STATE = 44
    VIEW_CONFIGURATION_PROPERTIES = 45
    FRAME_BEGIN_INFO = 46
    COMPOSITION_LAYER_PROJECTION_VIEW = 48
    EVENT_DATA_EVENTS_LOST = 49
    INTERACTION_PROFILE_SUGGESTED_BINDING = 51
    EVENT_DATA_INTERACTION_PROFILE_CHANGED = 52
    INTERACTION_PROFILE_STATE = 53
    SWAPCHAIN_IMAGE_ACQUIRE_INFO = 55
    SWAPCHAIN_IMAGE_WAIT_INFO = 56
    SWAPCHAIN_IMAGE_RELEASE_INFO = 57
    ACTION_STATE_GET_INFO = 58
    HAPTIC_ACTION_INFO = 59
    SESSION_ACTION_SETS_ATTACH_INFO = 60
    ACTIONS_SYNC_INFO = 61
    BOUND_SOURCES_FOR_ACTION_ENUMERATE_INFO = 62
    INPUT_SOURCE_LOCALIZED_NAME_GET_INFO = 63
    COMPOSITION_LAYER_CUBE_KHR = 1000006000
    INSTANCE_CREATE_INFO_ANDROID_KHR = 1000008000
    COMPOSITION_LAYER_DEPTH_INFO_KHR = 1000010000
    VULKAN_SWAPCHAIN_FORMAT_LIST_CREATE_INFO_KHR = 1000014000
    EVENT_DATA_PERF_SETTINGS_EXT = 1000015000
    COMPOSITION_LAYER_CYLINDER_KHR = 1000017000
    COMPOSITION_LAYER_EQUIRECT_KHR = 1000018000
    DEBUG_UTILS_OBJECT_NAME_INFO_EXT = 1000019000
    DEBUG_UTILS_MESSENGER_CALLBACK_DATA_EXT = 1000019001
    DEBUG_UTILS_MESSENGER_CREATE_INFO_EXT = 1000019002
    DEBUG_UTILS_LABEL_EXT = 1000019003
    GRAPHICS_BINDING_OPENGL_WIN32_KHR = 1000023000
    GRAPHICS_BINDING_OPENGL_XLIB_KHR = 1000023001
    GRAPHICS_BINDING_OPENGL_XCB_KHR = 1000023002
    GRAPHICS_BINDING_OPENGL_WAYLAND_KHR = 1000023003
    SWAPCHAIN_IMAGE_OPENGL_KHR = 1000023004
    GRAPHICS_REQUIREMENTS_OPENGL_KHR = 1000023005
    GRAPHICS_BINDING_OPENGL_ES_ANDROID_KHR = 1000024001
    SWAPCHAIN_IMAGE_OPENGL_ES_KHR = 1000024002
    GRAPHICS_REQUIREMENTS_OPENGL_ES_KHR = 1000024003
    GRAPHICS_BINDING_VULKAN_KHR = 1000025000
    SWAPCHAIN_IMAGE_VULKAN_KHR = 1000025001
    GRAPHICS_REQUIREMENTS_VULKAN_KHR = 1000025002
    GRAPHICS_BINDING_D3D11_KHR = 1000027000
    SWAPCHAIN_IMAGE_D3D11_KHR = 1000027001
    GRAPHICS_REQUIREMENTS_D3D11_KHR = 1000027002
    GRAPHICS_BINDING_D3D12_KHR = 1000028000
    SWAPCHAIN_IMAGE_D3D12_KHR = 1000028001
    GRAPHICS_REQUIREMENTS_D3D12_KHR = 1000028002
    SYSTEM_EYE_GAZE_INTERACTION_PROPERTIES_EXT = 1000030000
    EYE_GAZE_SAMPLE_TIME_EXT = 1000030001
    VISIBILITY_MASK_KHR = 1000031000
    EVENT_DATA_VISIBILITY_MASK_CHANGED_KHR = 1000031001
    SESSION_CREATE_INFO_OVERLAY_EXTX = 1000033000
    EVENT_DATA_MAIN_SESSION_VISIBILITY_CHANGED_EXTX = 1000033003
    COMPOSITION_LAYER_COLOR_SCALE_BIAS_KHR = 1000034000
    SPATIAL_ANCHOR_CREATE_INFO_MSFT = 1000039000
    SPATIAL_ANCHOR_SPACE_CREATE_INFO_MSFT = 1000039001
    COMPOSITION_LAYER_IMAGE_LAYOUT_FB = 1000040000
    COMPOSITION_LAYER_ALPHA_BLEND_FB = 1000041001
    VIEW_CONFIGURATION_DEPTH_RANGE_EXT = 1000046000
    GRAPHICS_BINDING_EGL_MNDX = 1000048004
    SPATIAL_GRAPH_NODE_SPACE_CREATE_INFO_MSFT = 1000049000
    SYSTEM_HAND_TRACKING_PROPERTIES_EXT = 1000051000
    HAND_TRACKER_CREATE_INFO_EXT = 1000051001
    HAND_JOINTS_LOCATE_INFO_EXT = 1000051002
    HAND_JOINT_LOCATIONS_EXT = 1000051003
    HAND_JOINT_VELOCITIES_EXT = 1000051004
    SYSTEM_HAND_TRACKING_MESH_PROPERTIES_MSFT = 1000052000
    HAND_MESH_SPACE_CREATE_INFO_MSFT = 1000052001
    HAND_MESH_UPDATE_INFO_MSFT = 1000052002
    HAND_MESH_MSFT = 1000052003
    HAND_POSE_TYPE_INFO_MSFT = 1000052004
    SECONDARY_VIEW_CONFIGURATION_SESSION_BEGIN_INFO_MSFT = 1000053000
    SECONDARY_VIEW_CONFIGURATION_STATE_MSFT = 1000053001
    SECONDARY_VIEW_CONFIGURATION_FRAME_STATE_MSFT = 1000053002
    SECONDARY_VIEW_CONFIGURATION_FRAME_END_INFO_MSFT = 1000053003
    SECONDARY_VIEW_CONFIGURATION_LAYER_INFO_MSFT = 1000053004
    SECONDARY_VIEW_CONFIGURATION_SWAPCHAIN_CREATE_INFO_MSFT = 1000053005
    CONTROLLER_MODEL_KEY_STATE_MSFT = 1000055000
    CONTROLLER_MODEL_NODE_PROPERTIES_MSFT = 1000055001
    CONTROLLER_MODEL_PROPERTIES_MSFT = 1000055002
    CONTROLLER_MODEL_NODE_STATE_MSFT = 1000055003
    CONTROLLER_MODEL_STATE_MSFT = 1000055004
    VIEW_CONFIGURATION_VIEW_FOV_EPIC = 1000059000
    HOLOGRAPHIC_WINDOW_ATTACHMENT_MSFT = 1000063000
    COMPOSITION_LAYER_REPROJECTION_INFO_MSFT = 1000066000
    COMPOSITION_LAYER_REPROJECTION_PLANE_OVERRIDE_MSFT = 1000066001
    ANDROID_SURFACE_SWAPCHAIN_CREATE_INFO_FB = 1000070000
    COMPOSITION_LAYER_SECURE_CONTENT_FB = 1000072000
    INTERACTION_PROFILE_ANALOG_THRESHOLD_VALVE = 1000079000
    HAND_JOINTS_MOTION_RANGE_INFO_EXT = 1000080000
    LOADER_INIT_INFO_ANDROID_KHR = 1000089000
    VULKAN_INSTANCE_CREATE_INFO_KHR = 1000090000
    VULKAN_DEVICE_CREATE_INFO_KHR = 1000090001
    VULKAN_GRAPHICS_DEVICE_GET_INFO_KHR = 1000090003
    COMPOSITION_LAYER_EQUIRECT2_KHR = 1000091000
    SCENE_OBSERVER_CREATE_INFO_MSFT = 1000097000
    SCENE_CREATE_INFO_MSFT = 1000097001
    NEW_SCENE_COMPUTE_INFO_MSFT = 1000097002
    VISUAL_MESH_COMPUTE_LOD_INFO_MSFT = 1000097003
    SCENE_COMPONENTS_MSFT = 1000097004
    SCENE_COMPONENTS_GET_INFO_MSFT = 1000097005
    SCENE_COMPONENT_LOCATIONS_MSFT = 1000097006
    SCENE_COMPONENTS_LOCATE_INFO_MSFT = 1000097007
    SCENE_OBJECTS_MSFT = 1000097008
    SCENE_COMPONENT_PARENT_FILTER_INFO_MSFT = 1000097009
    SCENE_OBJECT_TYPES_FILTER_INFO_MSFT = 1000097010
    SCENE_PLANES_MSFT = 1000097011
    SCENE_PLANE_ALIGNMENT_FILTER_INFO_MSFT = 1000097012
    SCENE_MESHES_MSFT = 1000097013
    SCENE_MESH_BUFFERS_GET_INFO_MSFT = 1000097014
    SCENE_MESH_BUFFERS_MSFT = 1000097015
    SCENE_MESH_VERTEX_BUFFER_MSFT = 1000097016
    SCENE_MESH_INDICES_UINT32_MSFT = 1000097017
    SCENE_MESH_INDICES_UINT16_MSFT = 1000097018
    SERIALIZED_SCENE_FRAGMENT_DATA_GET_INFO_MSFT = 1000098000
    SCENE_DESERIALIZE_INFO_MSFT = 1000098001
    EVENT_DATA_DISPLAY_REFRESH_RATE_CHANGED_FB = 1000101000
    SYSTEM_COLOR_SPACE_PROPERTIES_FB = 1000108000
    HAND_TRACKING_MESH_FB = 1000110001
    HAND_TRACKING_SCALE_FB = 1000110003
    HAND_TRACKING_AIM_STATE_FB = 1000111001
    HAND_TRACKING_CAPSULES_STATE_FB = 1000112000
    FOVEATION_PROFILE_CREATE_INFO_FB = 1000114000
    SWAPCHAIN_CREATE_INFO_FOVEATION_FB = 1000114001
    SWAPCHAIN_STATE_FOVEATION_FB = 1000114002
    FOVEATION_LEVEL_PROFILE_CREATE_INFO_FB = 1000115000
    BINDING_MODIFICATIONS_KHR = 1000120000
    VIEW_LOCATE_FOVEATED_RENDERING_VARJO = 1000121000
    FOVEATED_VIEW_CONFIGURATION_VIEW_VARJO = 1000121001
    SYSTEM_FOVEATED_RENDERING_PROPERTIES_VARJO = 1000121002
    COMPOSITION_LAYER_DEPTH_TEST_VARJO = 1000122000
    SPATIAL_ANCHOR_PERSISTENCE_INFO_MSFT = 1000142000
    SPATIAL_ANCHOR_FROM_PERSISTED_ANCHOR_CREATE_INFO_MSFT = 1000142001
    SWAPCHAIN_IMAGE_FOVEATION_VULKAN_FB = 1000160000
    SWAPCHAIN_STATE_ANDROID_SURFACE_DIMENSIONS_FB = 1000161000
    SWAPCHAIN_STATE_SAMPLER_OPENGL_ES_FB = 1000162000
    SWAPCHAIN_STATE_SAMPLER_VULKAN_FB = 1000163000
    COMPOSITION_LAYER_SPACE_WARP_INFO_FB = 1000171000
    SYSTEM_SPACE_WARP_PROPERTIES_FB = 1000171001
    GRAPHICS_BINDING_VULKAN2_KHR = 1000025000
    SWAPCHAIN_IMAGE_VULKAN2_KHR = 1000025001
    GRAPHICS_REQUIREMENTS_VULKAN2_KHR = 1000025002


class FormFactor(EnumBase):
    HEAD_MOUNTED_DISPLAY = 1
    HANDHELD_DISPLAY = 2


class ViewConfigurationType(EnumBase):
    PRIMARY_MONO = 1
    PRIMARY_STEREO = 2
    PRIMARY_QUAD_VARJO = 1000037000
    SECONDARY_MONO_FIRST_PERSON_OBSERVER_MSFT = 1000054000


class EnvironmentBlendMode(EnumBase):
    OPAQUE = 1
    ADDITIVE = 2
    ALPHA_BLEND = 3


class ReferenceSpaceType(EnumBase):
    VIEW = 1
    LOCAL = 2
    STAGE = 3
    UNBOUNDED_MSFT = 1000038000
    COMBINED_EYE_VARJO = 1000121000


class ActionType(EnumBase):
    BOOLEAN_INPUT = 1
    FLOAT_INPUT = 2
    VECTOR2F_INPUT = 3
    POSE_INPUT = 4
    VIBRATION_OUTPUT = 100


class EyeVisibility(EnumBase):
    BOTH = 0
    LEFT = 1
    RIGHT = 2


class SessionState(EnumBase):
    UNKNOWN = 0
    IDLE = 1
    READY = 2
    SYNCHRONIZED = 3
    VISIBLE = 4
    FOCUSED = 5
    STOPPING = 6
    LOSS_PENDING = 7
    EXITING = 8


class ObjectType(EnumBase):
    UNKNOWN = 0
    INSTANCE = 1
    SESSION = 2
    SWAPCHAIN = 3
    SPACE = 4
    ACTION_SET = 5
    ACTION = 6
    DEBUG_UTILS_MESSENGER_EXT = 1000019000
    SPATIAL_ANCHOR_MSFT = 1000039000
    HAND_TRACKER_EXT = 1000051000
    SCENE_OBSERVER_MSFT = 1000097000
    SCENE_MSFT = 1000097001
    FOVEATION_PROFILE_FB = 1000114000
    SPATIAL_ANCHOR_STORE_CONNECTION_MSFT = 1000142000


class VisibilityMaskTypeKHR(EnumBase):
    HIDDEN_TRIANGLE_MESH = 1
    VISIBLE_TRIANGLE_MESH = 2
    LINE_LOOP = 3


class PerfSettingsDomainEXT(EnumBase):
    CPU = 1
    GPU = 2


class PerfSettingsSubDomainEXT(EnumBase):
    COMPOSITING = 1
    RENDERING = 2
    THERMAL = 3


class PerfSettingsLevelEXT(EnumBase):
    POWER_SAVINGS = 0
    SUSTAINED_LOW = 25
    SUSTAINED_HIGH = 50
    BOOST = 75


class PerfSettingsNotificationLevelEXT(EnumBase):
    NORMAL = 0
    WARNING = 25
    IMPAIRED = 75


class BlendFactorFB(EnumBase):
    ZERO = 0
    ONE = 1
    SRC_ALPHA = 2
    ONE_MINUS_SRC_ALPHA = 3
    DST_ALPHA = 4
    ONE_MINUS_DST_ALPHA = 5


class SpatialGraphNodeTypeMSFT(EnumBase):
    STATIC = 1
    DYNAMIC = 2


class HandEXT(EnumBase):
    LEFT = 1
    RIGHT = 2


class HandJointEXT(EnumBase):
    PALM = 0
    WRIST = 1
    THUMB_METACARPAL = 2
    THUMB_PROXIMAL = 3
    THUMB_DISTAL = 4
    THUMB_TIP = 5
    INDEX_METACARPAL = 6
    INDEX_PROXIMAL = 7
    INDEX_INTERMEDIATE = 8
    INDEX_DISTAL = 9
    INDEX_TIP = 10
    MIDDLE_METACARPAL = 11
    MIDDLE_PROXIMAL = 12
    MIDDLE_INTERMEDIATE = 13
    MIDDLE_DISTAL = 14
    MIDDLE_TIP = 15
    RING_METACARPAL = 16
    RING_PROXIMAL = 17
    RING_INTERMEDIATE = 18
    RING_DISTAL = 19
    RING_TIP = 20
    LITTLE_METACARPAL = 21
    LITTLE_PROXIMAL = 22
    LITTLE_INTERMEDIATE = 23
    LITTLE_DISTAL = 24
    LITTLE_TIP = 25


class HandJointSetEXT(EnumBase):
    DEFAULT = 0


class HandPoseTypeMSFT(EnumBase):
    TRACKED = 0
    REFERENCE_OPEN_PALM = 1


class ReprojectionModeMSFT(EnumBase):
    DEPTH = 1
    PLANAR_FROM_DEPTH = 2
    PLANAR_MANUAL = 3
    ORIENTATION_ONLY = 4


class HandJointsMotionRangeEXT(EnumBase):
    UNOBSTRUCTED = 1
    CONFORMING_TO_CONTROLLER = 2


class SceneComputeFeatureMSFT(EnumBase):
    PLANE = 1
    PLANE_MESH = 2
    VISUAL_MESH = 3
    COLLIDER_MESH = 4
    SERIALIZE_SCENE = 1000098000


class SceneComputeConsistencyMSFT(EnumBase):
    SNAPSHOT_COMPLETE = 1
    SNAPSHOT_INCOMPLETE_FAST = 2
    OCCLUSION_OPTIMIZED = 3


class MeshComputeLodMSFT(EnumBase):
    COARSE = 1
    MEDIUM = 2
    FINE = 3
    UNLIMITED = 4


class SceneComponentTypeMSFT(EnumBase):
    INVALID = -1
    OBJECT = 1
    PLANE = 2
    VISUAL_MESH = 3
    COLLIDER_MESH = 4
    SERIALIZED_SCENE_FRAGMENT = 1000098000


class SceneObjectTypeMSFT(EnumBase):
    UNCATEGORIZED = -1
    BACKGROUND = 1
    WALL = 2
    FLOOR = 3
    CEILING = 4
    PLATFORM = 5
    INFERRED = 6


class ScenePlaneAlignmentTypeMSFT(EnumBase):
    NON_ORTHOGONAL = 0
    HORIZONTAL = 1
    VERTICAL = 2


class SceneComputeStateMSFT(EnumBase):
    NONE = 0
    UPDATING = 1
    COMPLETED = 2
    COMPLETED_WITH_ERROR = 3


class ColorSpaceFB(EnumBase):
    UNMANAGED = 0
    REC2020 = 1
    REC709 = 2
    RIFT_CV1 = 3
    RIFT_S = 4
    QUEST = 5
    P3 = 6
    ADOBE_RGB = 7


class FoveationLevelFB(EnumBase):
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class FoveationDynamicFB(EnumBase):
    DISABLED = 0
    LEVEL_ENABLED = 1


__all__ = [
    "SpaceVelocityFlagBits",
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
    "VisibilityMaskTypeKHR",
    "PerfSettingsDomainEXT",
    "PerfSettingsSubDomainEXT",
    "PerfSettingsLevelEXT",
    "PerfSettingsNotificationLevelEXT",
    "BlendFactorFB",
    "SpatialGraphNodeTypeMSFT",
    "HandEXT",
    "HandJointEXT",
    "HandJointSetEXT",
    "HandPoseTypeMSFT",
    "ReprojectionModeMSFT",
    "HandJointsMotionRangeEXT",
    "SceneComputeFeatureMSFT",
    "SceneComputeConsistencyMSFT",
    "MeshComputeLodMSFT",
    "SceneComponentTypeMSFT",
    "SceneObjectTypeMSFT",
    "ScenePlaneAlignmentTypeMSFT",
    "SceneComputeStateMSFT",
    "ColorSpaceFB",
    "FoveationLevelFB",
    "FoveationDynamicFB",
]
