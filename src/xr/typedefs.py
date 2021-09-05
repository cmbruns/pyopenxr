# Warning: this file is auto-generated. Do not edit.

from typing import Generator

from ctypes import CFUNCTYPE, POINTER, Structure, addressof, c_char, c_char_p, c_float, c_int, c_int16, c_int32, c_int64, c_uint16, c_uint32, c_uint64, c_uint8, c_void_p
import numpy
from .enums import *

VersionNumber = c_uint64

Flags64 = c_uint64

SystemId = c_uint64

Bool32 = c_uint32

Path = c_uint64

Time = c_int64

Duration = c_int64


class Instance_T(Structure):
    pass


InstanceHandle = POINTER(Instance_T)


class Session_T(Structure):
    pass


SessionHandle = POINTER(Session_T)


class Space_T(Structure):
    pass


SpaceHandle = POINTER(Space_T)


class Action_T(Structure):
    pass


ActionHandle = POINTER(Action_T)


class Swapchain_T(Structure):
    pass


SwapchainHandle = POINTER(Swapchain_T)


class ActionSet_T(Structure):
    pass


ActionSetHandle = POINTER(ActionSet_T)

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
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.API_LAYER_PROPERTIES.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_name", (c_char * 256)),
        ("spec_version", VersionNumber),
        ("layer_version", c_uint32),
        ("description", (c_char * 256)),
    ]


class ExtensionProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.EXTENSION_PROPERTIES.value,
            *args, **kwargs,
        )            

    def __bytes__(self):
        return self.extension_name

    def __eq__(self, other):
        try:
            if other.type != self.type:
                return False
        except AttributeError:
            pass  # That's OK, objects without those attributes can use string comparison
        return str(other) == str(self)

    def __str__(self):
        return self.extension_name.decode()                

    _fields_ = [
        ("type", StructureType.ctype()),
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
        ("api_version", VersionNumber),
    ]


class InstanceCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.INSTANCE_CREATE_INFO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("create_flags", InstanceCreateFlags),
        ("application_info", ApplicationInfo),
        ("enabled_api_layer_count", c_uint32),
        ("enabled_api_layer_names", POINTER(c_char_p)),
        ("enabled_extension_count", c_uint32),
        ("enabled_extension_names", POINTER(c_char_p)),
    ]


class InstanceProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.INSTANCE_PROPERTIES.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("runtime_version", VersionNumber),
        ("runtime_name", (c_char * 128)),
    ]


class EventDataBuffer(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.EVENT_DATA_BUFFER.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("varying", (c_uint8 * 4000)),
    ]


class SystemGetInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SYSTEM_GET_INFO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("form_factor", FormFactor.ctype()),
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
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SYSTEM_PROPERTIES.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("system_id", SystemId),
        ("vendor_id", c_uint32),
        ("system_name", (c_char * 256)),
        ("graphics_properties", SystemGraphicsProperties),
        ("tracking_properties", SystemTrackingProperties),
    ]


class SessionCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SESSION_CREATE_INFO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
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

    def __iter__(self) -> Generator[float, None, None]:
        yield self.x
        yield self.y
        yield self.z

    def __getitem__(self, key):
        return tuple(self)[key]

    def __len__(self) -> int:
        return 3

    def __repr__(self) -> str:
        return f"xr.{self.__class__.__name__}({', '.join([repr(v) for v in self])})"

    def __str__(self) -> str:
        return f"({', '.join([f'{v:.3f}' for v in self])})"


class SpaceVelocity(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SPACE_VELOCITY.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
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

    def __init__(self, x=0, y=0, z=0, w=1):
        super().__init__(x=x, y=y, z=z, w=w)
        self._numpy = None  # self.as_numpy will construct it just-in-time

    def __iter__(self) -> Generator[float, None, None]:
        yield self.x
        yield self.y
        yield self.z
        yield self.w

    def __getitem__(self, key):
        return tuple(self)[key]

    def __len__(self) -> int:
        return 4

    def __repr__(self) -> str:
        return f"xr.{self.__class__.__name__}({', '.join([repr(v) for v in self])})"

    def __str__(self) -> str:
        return f"({', '.join([f'{v:.3f}' for v in self])})"

    def as_numpy(self):
        if self._numpy is None:
            # Just in time construction
            buffer = (c_float * len(self)).from_address(addressof(self))
            buffer._wrapper = self  # To link lifetime of buffer to self
            self._numpy = numpy.ctypeslib.as_array(buffer)
        return self._numpy


class Posef(Structure):
    _fields_ = [
        ("orientation", Quaternionf),
        ("position", Vector3f),
    ]

    def __init__(self, orientation: Quaternionf = None, position: Vector3f = None):
        if orientation is None:
            orientation = Quaternionf()
        if position is None:
            position = Vector3f()
        super().__init__(orientation=orientation, position=position)

    def __repr__(self) -> str:
        return f"xr.{self.__class__.__name__}({repr(self.orientation)}, {repr(self.position)})"

    def __str__(self) -> str:
        return f"xr.{self.__class__.__name__}({self.orientation}, {self.position})"


class ReferenceSpaceCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.REFERENCE_SPACE_CREATE_INFO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("reference_space_type", ReferenceSpaceType.ctype()),
        ("pose_in_reference_space", Posef),
    ]


class Extent2Df(Structure):
    _fields_ = [
        ("width", c_float),
        ("height", c_float),
    ]


class ActionSpaceCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.ACTION_SPACE_CREATE_INFO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("action", ActionHandle),
        ("subaction_path", Path),
        ("pose_in_action_space", Posef),
    ]


class SpaceLocation(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SPACE_LOCATION.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("location_flags", SpaceLocationFlags),
        ("pose", Posef),
    ]


class ViewConfigurationProperties(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.VIEW_CONFIGURATION_PROPERTIES.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_configuration_type", ViewConfigurationType.ctype()),
        ("fov_mutable", Bool32),
    ]


class ViewConfigurationView(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.VIEW_CONFIGURATION_VIEW.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("recommended_image_rect_width", c_uint32),
        ("max_image_rect_width", c_uint32),
        ("recommended_image_rect_height", c_uint32),
        ("max_image_rect_height", c_uint32),
        ("recommended_swapchain_sample_count", c_uint32),
        ("max_swapchain_sample_count", c_uint32),
    ]


class SwapchainCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SWAPCHAIN_CREATE_INFO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
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
    def __init__(self, *args, **kwargs):
        super().__init__(
            0,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SwapchainImageAcquireInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SWAPCHAIN_IMAGE_ACQUIRE_INFO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SwapchainImageWaitInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SWAPCHAIN_IMAGE_WAIT_INFO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("timeout", Duration),
    ]


class SwapchainImageReleaseInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SWAPCHAIN_IMAGE_RELEASE_INFO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SessionBeginInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SESSION_BEGIN_INFO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("primary_view_configuration_type", ViewConfigurationType.ctype()),
    ]


class FrameWaitInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.FRAME_WAIT_INFO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class FrameState(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.FRAME_STATE.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("predicted_display_time", Time),
        ("predicted_display_period", Duration),
        ("should_render", Bool32),
    ]


class FrameBeginInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.FRAME_BEGIN_INFO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class CompositionLayerBaseHeader(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.COMPOSITION_LAYER_BASE_HEADER.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlags),
        ("space", SpaceHandle),
    ]


class FrameEndInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.FRAME_END_INFO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("display_time", Time),
        ("environment_blend_mode", EnvironmentBlendMode.ctype()),
        ("layer_count", c_uint32),
        ("layers", POINTER(POINTER(CompositionLayerBaseHeader))),
    ]


class ViewLocateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.VIEW_LOCATE_INFO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_configuration_type", ViewConfigurationType.ctype()),
        ("display_time", Time),
        ("space", SpaceHandle),
    ]


class ViewState(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.VIEW_STATE.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
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
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.VIEW.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("pose", Posef),
        ("fov", Fovf),
    ]


class ActionSetCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.ACTION_SET_CREATE_INFO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("action_set_name", (c_char * 64)),
        ("localized_action_set_name", (c_char * 128)),
        ("priority", c_uint32),
    ]


class ActionCreateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.ACTION_CREATE_INFO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("action_name", (c_char * 64)),
        ("action_type", ActionType.ctype()),
        ("count_subaction_paths", c_uint32),
        ("subaction_paths", POINTER(c_uint64)),
        ("localized_action_name", (c_char * 128)),
    ]


class ActionSuggestedBinding(Structure):
    _fields_ = [
        ("action", ActionHandle),
        ("binding", Path),
    ]


class InteractionProfileSuggestedBinding(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.INTERACTION_PROFILE_SUGGESTED_BINDING.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("interaction_profile", Path),
        ("count_suggested_bindings", c_uint32),
        ("suggested_bindings", POINTER(ActionSuggestedBinding)),
    ]


class SessionActionSetsAttachInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SESSION_ACTION_SETS_ATTACH_INFO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("count_action_sets", c_uint32),
        ("action_sets", POINTER(POINTER(ActionSet_T))),
    ]


class InteractionProfileState(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.INTERACTION_PROFILE_STATE.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("interaction_profile", Path),
    ]


class ActionStateGetInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.ACTION_STATE_GET_INFO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("action", ActionHandle),
        ("subaction_path", Path),
    ]


class ActionStateBoolean(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.ACTION_STATE_BOOLEAN.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("current_state", Bool32),
        ("changed_since_last_sync", Bool32),
        ("last_change_time", Time),
        ("is_active", Bool32),
    ]


class ActionStateFloat(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.ACTION_STATE_FLOAT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
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
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.ACTION_STATE_VECTOR2F.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("current_state", Vector2f),
        ("changed_since_last_sync", Bool32),
        ("last_change_time", Time),
        ("is_active", Bool32),
    ]


class ActionStatePose(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.ACTION_STATE_POSE.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("is_active", Bool32),
    ]


class ActiveActionSet(Structure):
    _fields_ = [
        ("action_set", ActionSetHandle),
        ("subaction_path", Path),
    ]


class ActionsSyncInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.ACTIONS_SYNC_INFO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("count_active_action_sets", c_uint32),
        ("active_action_sets", POINTER(ActiveActionSet)),
    ]


class BoundSourcesForActionEnumerateInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.BOUND_SOURCES_FOR_ACTION_ENUMERATE_INFO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("action", ActionHandle),
    ]


class InputSourceLocalizedNameGetInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.INPUT_SOURCE_LOCALIZED_NAME_GET_INFO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("source_path", Path),
        ("which_components", InputSourceLocalizedNameFlags),
    ]


class HapticActionInfo(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.HAPTIC_ACTION_INFO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("action", ActionHandle),
        ("subaction_path", Path),
    ]


class HapticBaseHeader(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.HAPTIC_BASE_HEADER.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class BaseInStructure(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.BASE_IN_STRUCTURE.value,
            *args, **kwargs,
        )            

    pass


BaseInStructure._fields_ = [
        ("type", StructureType.ctype()),
        ("next", POINTER(BaseInStructure)),
    ]


class BaseOutStructure(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.BASE_OUT_STRUCTURE.value,
            *args, **kwargs,
        )            

    pass


BaseOutStructure._fields_ = [
        ("type", StructureType.ctype()),
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
        ("swapchain", SwapchainHandle),
        ("image_rect", Rect2Di),
        ("image_array_index", c_uint32),
    ]


class CompositionLayerProjectionView(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.COMPOSITION_LAYER_PROJECTION_VIEW.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("pose", Posef),
        ("fov", Fovf),
        ("sub_image", SwapchainSubImage),
    ]


class CompositionLayerProjection(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.COMPOSITION_LAYER_PROJECTION.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlags),
        ("space", SpaceHandle),
        ("view_count", c_uint32),
        ("views", POINTER(CompositionLayerProjectionView)),
    ]


class CompositionLayerQuad(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.COMPOSITION_LAYER_QUAD.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlags),
        ("space", SpaceHandle),
        ("eye_visibility", EyeVisibility.ctype()),
        ("sub_image", SwapchainSubImage),
        ("pose", Posef),
        ("size", Extent2Df),
    ]


class EventDataBaseHeader(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.EVENT_DATA_BASE_HEADER.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class EventDataEventsLost(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.EVENT_DATA_EVENTS_LOST.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("lost_event_count", c_uint32),
    ]


class EventDataInstanceLossPending(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.EVENT_DATA_INSTANCE_LOSS_PENDING.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("loss_time", Time),
    ]


class EventDataSessionStateChanged(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.EVENT_DATA_SESSION_STATE_CHANGED.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("session", SessionHandle),
        ("state", SessionState.ctype()),
        ("time", Time),
    ]


class EventDataReferenceSpaceChangePending(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.EVENT_DATA_REFERENCE_SPACE_CHANGE_PENDING.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("session", SessionHandle),
        ("reference_space_type", ReferenceSpaceType.ctype()),
        ("change_time", Time),
        ("pose_valid", Bool32),
        ("pose_in_previous_space", Posef),
    ]


class EventDataInteractionProfileChanged(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.EVENT_DATA_INTERACTION_PROFILE_CHANGED.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("session", SessionHandle),
    ]


class HapticVibration(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.HAPTIC_VIBRATION.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
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


PFN_xrGetInstanceProcAddr = CFUNCTYPE(Result.ctype(), InstanceHandle, c_char_p, POINTER(PFN_xrVoidFunction))

PFN_xrEnumerateApiLayerProperties = CFUNCTYPE(Result.ctype(), c_uint32, POINTER(c_uint32), POINTER(ApiLayerProperties))

PFN_xrEnumerateInstanceExtensionProperties = CFUNCTYPE(Result.ctype(), c_char_p, c_uint32, POINTER(c_uint32), POINTER(ExtensionProperties))

PFN_xrCreateInstance = CFUNCTYPE(Result.ctype(), POINTER(InstanceCreateInfo), POINTER(InstanceHandle))

PFN_xrDestroyInstance = CFUNCTYPE(Result.ctype(), InstanceHandle)

PFN_xrGetInstanceProperties = CFUNCTYPE(Result.ctype(), InstanceHandle, POINTER(InstanceProperties))

PFN_xrPollEvent = CFUNCTYPE(Result.ctype(), InstanceHandle, POINTER(EventDataBuffer))

PFN_xrResultToString = CFUNCTYPE(Result.ctype(), InstanceHandle, Result.ctype(), (c_char * 64))

PFN_xrStructureTypeToString = CFUNCTYPE(Result.ctype(), InstanceHandle, StructureType.ctype(), (c_char * 64))

PFN_xrGetSystem = CFUNCTYPE(Result.ctype(), InstanceHandle, POINTER(SystemGetInfo), POINTER(SystemId))

PFN_xrGetSystemProperties = CFUNCTYPE(Result.ctype(), InstanceHandle, SystemId, POINTER(SystemProperties))

PFN_xrEnumerateEnvironmentBlendModes = CFUNCTYPE(Result.ctype(), InstanceHandle, SystemId, ViewConfigurationType.ctype(), c_uint32, POINTER(c_uint32), POINTER(EnvironmentBlendMode.ctype()))

PFN_xrCreateSession = CFUNCTYPE(Result.ctype(), InstanceHandle, POINTER(SessionCreateInfo), POINTER(SessionHandle))

PFN_xrDestroySession = CFUNCTYPE(Result.ctype(), SessionHandle)

PFN_xrEnumerateReferenceSpaces = CFUNCTYPE(Result.ctype(), SessionHandle, c_uint32, POINTER(c_uint32), POINTER(ReferenceSpaceType.ctype()))

PFN_xrCreateReferenceSpace = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(ReferenceSpaceCreateInfo), POINTER(SpaceHandle))

PFN_xrGetReferenceSpaceBoundsRect = CFUNCTYPE(Result.ctype(), SessionHandle, ReferenceSpaceType.ctype(), POINTER(Extent2Df))

PFN_xrCreateActionSpace = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(ActionSpaceCreateInfo), POINTER(SpaceHandle))

PFN_xrLocateSpace = CFUNCTYPE(Result.ctype(), SpaceHandle, SpaceHandle, Time, POINTER(SpaceLocation))

PFN_xrDestroySpace = CFUNCTYPE(Result.ctype(), SpaceHandle)

PFN_xrEnumerateViewConfigurations = CFUNCTYPE(Result.ctype(), InstanceHandle, SystemId, c_uint32, POINTER(c_uint32), POINTER(ViewConfigurationType.ctype()))

PFN_xrGetViewConfigurationProperties = CFUNCTYPE(Result.ctype(), InstanceHandle, SystemId, ViewConfigurationType.ctype(), POINTER(ViewConfigurationProperties))

PFN_xrEnumerateViewConfigurationViews = CFUNCTYPE(Result.ctype(), InstanceHandle, SystemId, ViewConfigurationType.ctype(), c_uint32, POINTER(c_uint32), POINTER(ViewConfigurationView))

PFN_xrEnumerateSwapchainFormats = CFUNCTYPE(Result.ctype(), SessionHandle, c_uint32, POINTER(c_uint32), POINTER(c_int64))

PFN_xrCreateSwapchain = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(SwapchainCreateInfo), POINTER(SwapchainHandle))

PFN_xrDestroySwapchain = CFUNCTYPE(Result.ctype(), SwapchainHandle)

PFN_xrEnumerateSwapchainImages = CFUNCTYPE(Result.ctype(), SwapchainHandle, c_uint32, POINTER(c_uint32), POINTER(SwapchainImageBaseHeader))

PFN_xrAcquireSwapchainImage = CFUNCTYPE(Result.ctype(), SwapchainHandle, POINTER(SwapchainImageAcquireInfo), POINTER(c_uint32))

PFN_xrWaitSwapchainImage = CFUNCTYPE(Result.ctype(), SwapchainHandle, POINTER(SwapchainImageWaitInfo))

PFN_xrReleaseSwapchainImage = CFUNCTYPE(Result.ctype(), SwapchainHandle, POINTER(SwapchainImageReleaseInfo))

PFN_xrBeginSession = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(SessionBeginInfo))

PFN_xrEndSession = CFUNCTYPE(Result.ctype(), SessionHandle)

PFN_xrRequestExitSession = CFUNCTYPE(Result.ctype(), SessionHandle)

PFN_xrWaitFrame = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(FrameWaitInfo), POINTER(FrameState))

PFN_xrBeginFrame = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(FrameBeginInfo))

PFN_xrEndFrame = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(FrameEndInfo))

PFN_xrLocateViews = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(ViewLocateInfo), POINTER(ViewState), c_uint32, POINTER(c_uint32), POINTER(View))

PFN_xrStringToPath = CFUNCTYPE(Result.ctype(), InstanceHandle, c_char_p, POINTER(Path))

PFN_xrPathToString = CFUNCTYPE(Result.ctype(), InstanceHandle, Path, c_uint32, POINTER(c_uint32), c_char_p)

PFN_xrCreateActionSet = CFUNCTYPE(Result.ctype(), InstanceHandle, POINTER(ActionSetCreateInfo), POINTER(ActionSetHandle))

PFN_xrDestroyActionSet = CFUNCTYPE(Result.ctype(), ActionSetHandle)

PFN_xrCreateAction = CFUNCTYPE(Result.ctype(), ActionSetHandle, POINTER(ActionCreateInfo), POINTER(ActionHandle))

PFN_xrDestroyAction = CFUNCTYPE(Result.ctype(), ActionHandle)

PFN_xrSuggestInteractionProfileBindings = CFUNCTYPE(Result.ctype(), InstanceHandle, POINTER(InteractionProfileSuggestedBinding))

PFN_xrAttachSessionActionSets = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(SessionActionSetsAttachInfo))

PFN_xrGetCurrentInteractionProfile = CFUNCTYPE(Result.ctype(), SessionHandle, Path, POINTER(InteractionProfileState))

PFN_xrGetActionStateBoolean = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(ActionStateGetInfo), POINTER(ActionStateBoolean))

PFN_xrGetActionStateFloat = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(ActionStateGetInfo), POINTER(ActionStateFloat))

PFN_xrGetActionStateVector2f = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(ActionStateGetInfo), POINTER(ActionStateVector2f))

PFN_xrGetActionStatePose = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(ActionStateGetInfo), POINTER(ActionStatePose))

PFN_xrSyncActions = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(ActionsSyncInfo))

PFN_xrEnumerateBoundSourcesForAction = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(BoundSourcesForActionEnumerateInfo), c_uint32, POINTER(c_uint32), POINTER(Path))

PFN_xrGetInputSourceLocalizedName = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(InputSourceLocalizedNameGetInfo), c_uint32, POINTER(c_uint32), c_char_p)

PFN_xrApplyHapticFeedback = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(HapticActionInfo), POINTER(HapticBaseHeader))

PFN_xrStopHapticFeedback = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(HapticActionInfo))


class CompositionLayerCubeKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.COMPOSITION_LAYER_CUBE_KHR.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlags),
        ("space", SpaceHandle),
        ("eye_visibility", EyeVisibility.ctype()),
        ("swapchain", SwapchainHandle),
        ("image_array_index", c_uint32),
        ("orientation", Quaternionf),
    ]


class CompositionLayerDepthInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.COMPOSITION_LAYER_DEPTH_INFO_KHR.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("sub_image", SwapchainSubImage),
        ("min_depth", c_float),
        ("max_depth", c_float),
        ("near_z", c_float),
        ("far_z", c_float),
    ]


class CompositionLayerCylinderKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.COMPOSITION_LAYER_CYLINDER_KHR.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlags),
        ("space", SpaceHandle),
        ("eye_visibility", EyeVisibility.ctype()),
        ("sub_image", SwapchainSubImage),
        ("pose", Posef),
        ("radius", c_float),
        ("central_angle", c_float),
        ("aspect_ratio", c_float),
    ]


class CompositionLayerEquirectKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.COMPOSITION_LAYER_EQUIRECT_KHR.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlags),
        ("space", SpaceHandle),
        ("eye_visibility", EyeVisibility.ctype()),
        ("sub_image", SwapchainSubImage),
        ("pose", Posef),
        ("radius", c_float),
        ("scale", Vector2f),
        ("bias", Vector2f),
    ]


class VisibilityMaskKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.VISIBILITY_MASK_KHR.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("vertex_capacity_input", c_uint32),
        ("vertex_count_output", c_uint32),
        ("vertices", POINTER(Vector2f)),
        ("index_capacity_input", c_uint32),
        ("index_count_output", c_uint32),
        ("indices", POINTER(c_uint32)),
    ]


class EventDataVisibilityMaskChangedKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.EVENT_DATA_VISIBILITY_MASK_CHANGED_KHR.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("session", SessionHandle),
        ("view_configuration_type", ViewConfigurationType.ctype()),
        ("view_index", c_uint32),
    ]


PFN_xrGetVisibilityMaskKHR = CFUNCTYPE(Result.ctype(), SessionHandle, ViewConfigurationType.ctype(), c_uint32, VisibilityMaskTypeKHR.ctype(), POINTER(VisibilityMaskKHR))


class CompositionLayerColorScaleBiasKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.COMPOSITION_LAYER_COLOR_SCALE_BIAS_KHR.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("color_scale", Color4f),
        ("color_bias", Color4f),
    ]


class LoaderInitInfoBaseHeaderKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.LOADER_INIT_INFO_BASE_HEADER_KHR.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


PFN_xrInitializeLoaderKHR = CFUNCTYPE(Result.ctype(), POINTER(LoaderInitInfoBaseHeaderKHR))


class CompositionLayerEquirect2KHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.COMPOSITION_LAYER_EQUIRECT2_KHR.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlags),
        ("space", SpaceHandle),
        ("eye_visibility", EyeVisibility.ctype()),
        ("sub_image", SwapchainSubImage),
        ("pose", Posef),
        ("radius", c_float),
        ("central_horizontal_angle", c_float),
        ("upper_vertical_angle", c_float),
        ("lower_vertical_angle", c_float),
    ]


class BindingModificationBaseHeaderKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.BINDING_MODIFICATION_BASE_HEADER_KHR.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class BindingModificationsKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.BINDING_MODIFICATIONS_KHR.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("binding_modification_count", c_uint32),
        ("binding_modifications", POINTER(POINTER(BindingModificationBaseHeaderKHR))),
    ]


class EventDataPerfSettingsEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.EVENT_DATA_PERF_SETTINGS_EXT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("domain", PerfSettingsDomainEXT.ctype()),
        ("sub_domain", PerfSettingsSubDomainEXT.ctype()),
        ("from_level", PerfSettingsNotificationLevelEXT.ctype()),
        ("to_level", PerfSettingsNotificationLevelEXT.ctype()),
    ]


PFN_xrPerfSettingsSetPerformanceLevelEXT = CFUNCTYPE(Result.ctype(), SessionHandle, PerfSettingsDomainEXT.ctype(), PerfSettingsLevelEXT.ctype())

PFN_xrThermalGetTemperatureTrendEXT = CFUNCTYPE(Result.ctype(), SessionHandle, PerfSettingsDomainEXT.ctype(), POINTER(PerfSettingsNotificationLevelEXT.ctype()), POINTER(c_float), POINTER(c_float))


class DebugUtilsMessengerEXT_T(Structure):
    pass


DebugUtilsMessengerEXTHandle = POINTER(DebugUtilsMessengerEXT_T)

DebugUtilsMessageSeverityFlagsEXT = Flags64

DebugUtilsMessageTypeFlagsEXT = Flags64


class DebugUtilsObjectNameInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.DEBUG_UTILS_OBJECT_NAME_INFO_EXT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("object_type", ObjectType.ctype()),
        ("object_handle", c_uint64),
        ("object_name", c_char_p),
    ]


class DebugUtilsLabelEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.DEBUG_UTILS_LABEL_EXT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("label_name", c_char_p),
    ]


class DebugUtilsMessengerCallbackDataEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.DEBUG_UTILS_MESSENGER_CALLBACK_DATA_EXT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
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
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.DEBUG_UTILS_MESSENGER_CREATE_INFO_EXT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("message_severities", DebugUtilsMessageSeverityFlagsEXT),
        ("message_types", DebugUtilsMessageTypeFlagsEXT),
        ("user_callback", PFN_xrDebugUtilsMessengerCallbackEXT),
        ("user_data", c_void_p),
    ]


PFN_xrSetDebugUtilsObjectNameEXT = CFUNCTYPE(Result.ctype(), InstanceHandle, POINTER(DebugUtilsObjectNameInfoEXT))

PFN_xrCreateDebugUtilsMessengerEXT = CFUNCTYPE(Result.ctype(), InstanceHandle, POINTER(DebugUtilsMessengerCreateInfoEXT), POINTER(DebugUtilsMessengerEXTHandle))

PFN_xrDestroyDebugUtilsMessengerEXT = CFUNCTYPE(Result.ctype(), DebugUtilsMessengerEXTHandle)

PFN_xrSubmitDebugUtilsMessageEXT = CFUNCTYPE(Result.ctype(), InstanceHandle, DebugUtilsMessageSeverityFlagsEXT, DebugUtilsMessageTypeFlagsEXT, POINTER(DebugUtilsMessengerCallbackDataEXT))

PFN_xrSessionBeginDebugUtilsLabelRegionEXT = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(DebugUtilsLabelEXT))

PFN_xrSessionEndDebugUtilsLabelRegionEXT = CFUNCTYPE(Result.ctype(), SessionHandle)

PFN_xrSessionInsertDebugUtilsLabelEXT = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(DebugUtilsLabelEXT))


class SystemEyeGazeInteractionPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SYSTEM_EYE_GAZE_INTERACTION_PROPERTIES_EXT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_eye_gaze_interaction", Bool32),
    ]


class EyeGazeSampleTimeEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.EYE_GAZE_SAMPLE_TIME_EXT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("time", Time),
    ]


OverlaySessionCreateFlagsEXTX = Flags64

OverlayMainSessionFlagsEXTX = Flags64


class SessionCreateInfoOverlayEXTX(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SESSION_CREATE_INFO_OVERLAY_EXTX.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("create_flags", OverlaySessionCreateFlagsEXTX),
        ("session_layers_placement", c_uint32),
    ]


class EventDataMainSessionVisibilityChangedEXTX(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.EVENT_DATA_MAIN_SESSION_VISIBILITY_CHANGED_EXTX.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("visible", Bool32),
        ("flags", OverlayMainSessionFlagsEXTX),
    ]


class SpatialAnchorMSFT_T(Structure):
    pass


SpatialAnchorMSFTHandle = POINTER(SpatialAnchorMSFT_T)


class SpatialAnchorCreateInfoMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SPATIAL_ANCHOR_CREATE_INFO_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("space", SpaceHandle),
        ("pose", Posef),
        ("time", Time),
    ]


class SpatialAnchorSpaceCreateInfoMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SPATIAL_ANCHOR_SPACE_CREATE_INFO_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("anchor", SpatialAnchorMSFTHandle),
        ("pose_in_anchor_space", Posef),
    ]


PFN_xrCreateSpatialAnchorMSFT = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(SpatialAnchorCreateInfoMSFT), POINTER(SpatialAnchorMSFTHandle))

PFN_xrCreateSpatialAnchorSpaceMSFT = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(SpatialAnchorSpaceCreateInfoMSFT), POINTER(SpaceHandle))

PFN_xrDestroySpatialAnchorMSFT = CFUNCTYPE(Result.ctype(), SpatialAnchorMSFTHandle)

CompositionLayerImageLayoutFlagsFB = Flags64


class CompositionLayerImageLayoutFB(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.COMPOSITION_LAYER_IMAGE_LAYOUT_FB.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", CompositionLayerImageLayoutFlagsFB),
    ]


class CompositionLayerAlphaBlendFB(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.COMPOSITION_LAYER_ALPHA_BLEND_FB.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("src_factor_color", BlendFactorFB.ctype()),
        ("dst_factor_color", BlendFactorFB.ctype()),
        ("src_factor_alpha", BlendFactorFB.ctype()),
        ("dst_factor_alpha", BlendFactorFB.ctype()),
    ]


class ViewConfigurationDepthRangeEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.VIEW_CONFIGURATION_DEPTH_RANGE_EXT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("recommended_near_z", c_float),
        ("min_near_z", c_float),
        ("recommended_far_z", c_float),
        ("max_far_z", c_float),
    ]


PFN_xrSetInputDeviceActiveEXT = CFUNCTYPE(Result.ctype(), SessionHandle, Path, Path, Bool32)

PFN_xrSetInputDeviceStateBoolEXT = CFUNCTYPE(Result.ctype(), SessionHandle, Path, Path, Bool32)

PFN_xrSetInputDeviceStateFloatEXT = CFUNCTYPE(Result.ctype(), SessionHandle, Path, Path, c_float)

PFN_xrSetInputDeviceStateVector2fEXT = CFUNCTYPE(Result.ctype(), SessionHandle, Path, Path, Vector2f)

PFN_xrSetInputDeviceLocationEXT = CFUNCTYPE(Result.ctype(), SessionHandle, Path, Path, SpaceHandle, Posef)


class SpatialGraphNodeSpaceCreateInfoMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SPATIAL_GRAPH_NODE_SPACE_CREATE_INFO_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("node_type", SpatialGraphNodeTypeMSFT.ctype()),
        ("node_id", (c_uint8 * 16)),
        ("pose", Posef),
    ]


PFN_xrCreateSpatialGraphNodeSpaceMSFT = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(SpatialGraphNodeSpaceCreateInfoMSFT), POINTER(SpaceHandle))


class HandTrackerEXT_T(Structure):
    pass


HandTrackerEXTHandle = POINTER(HandTrackerEXT_T)


class SystemHandTrackingPropertiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SYSTEM_HAND_TRACKING_PROPERTIES_EXT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_hand_tracking", Bool32),
    ]


class HandTrackerCreateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.HAND_TRACKER_CREATE_INFO_EXT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("hand", HandEXT.ctype()),
        ("hand_joint_set", HandJointSetEXT.ctype()),
    ]


class HandJointsLocateInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.HAND_JOINTS_LOCATE_INFO_EXT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("base_space", SpaceHandle),
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
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.HAND_JOINT_LOCATIONS_EXT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("is_active", Bool32),
        ("joint_count", c_uint32),
        ("joint_locations", POINTER(HandJointLocationEXT)),
    ]


class HandJointVelocitiesEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.HAND_JOINT_VELOCITIES_EXT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("joint_count", c_uint32),
        ("joint_velocities", POINTER(HandJointVelocityEXT)),
    ]


PFN_xrCreateHandTrackerEXT = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(HandTrackerCreateInfoEXT), POINTER(HandTrackerEXTHandle))

PFN_xrDestroyHandTrackerEXT = CFUNCTYPE(Result.ctype(), HandTrackerEXTHandle)

PFN_xrLocateHandJointsEXT = CFUNCTYPE(Result.ctype(), HandTrackerEXTHandle, POINTER(HandJointsLocateInfoEXT), POINTER(HandJointLocationsEXT))


class SystemHandTrackingMeshPropertiesMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SYSTEM_HAND_TRACKING_MESH_PROPERTIES_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_hand_tracking_mesh", Bool32),
        ("max_hand_mesh_index_count", c_uint32),
        ("max_hand_mesh_vertex_count", c_uint32),
    ]


class HandMeshSpaceCreateInfoMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.HAND_MESH_SPACE_CREATE_INFO_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("hand_pose_type", HandPoseTypeMSFT.ctype()),
        ("pose_in_hand_mesh_space", Posef),
    ]


class HandMeshUpdateInfoMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.HAND_MESH_UPDATE_INFO_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("time", Time),
        ("hand_pose_type", HandPoseTypeMSFT.ctype()),
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
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.HAND_MESH_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("is_active", Bool32),
        ("index_buffer_changed", Bool32),
        ("vertex_buffer_changed", Bool32),
        ("index_buffer", HandMeshIndexBufferMSFT),
        ("vertex_buffer", HandMeshVertexBufferMSFT),
    ]


class HandPoseTypeInfoMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.HAND_POSE_TYPE_INFO_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("hand_pose_type", HandPoseTypeMSFT.ctype()),
    ]


PFN_xrCreateHandMeshSpaceMSFT = CFUNCTYPE(Result.ctype(), HandTrackerEXTHandle, POINTER(HandMeshSpaceCreateInfoMSFT), POINTER(SpaceHandle))

PFN_xrUpdateHandMeshMSFT = CFUNCTYPE(Result.ctype(), HandTrackerEXTHandle, POINTER(HandMeshUpdateInfoMSFT), POINTER(HandMeshMSFT))


class SecondaryViewConfigurationSessionBeginInfoMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SECONDARY_VIEW_CONFIGURATION_SESSION_BEGIN_INFO_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_configuration_count", c_uint32),
        ("enabled_view_configuration_types", POINTER(c_int)),
    ]


class SecondaryViewConfigurationStateMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SECONDARY_VIEW_CONFIGURATION_STATE_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_configuration_type", ViewConfigurationType.ctype()),
        ("active", Bool32),
    ]


class SecondaryViewConfigurationFrameStateMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SECONDARY_VIEW_CONFIGURATION_FRAME_STATE_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_configuration_count", c_uint32),
        ("view_configuration_states", POINTER(SecondaryViewConfigurationStateMSFT)),
    ]


class SecondaryViewConfigurationLayerInfoMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SECONDARY_VIEW_CONFIGURATION_LAYER_INFO_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_configuration_type", ViewConfigurationType.ctype()),
        ("environment_blend_mode", EnvironmentBlendMode.ctype()),
        ("layer_count", c_uint32),
        ("layers", POINTER(POINTER(CompositionLayerBaseHeader))),
    ]


class SecondaryViewConfigurationFrameEndInfoMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SECONDARY_VIEW_CONFIGURATION_FRAME_END_INFO_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_configuration_count", c_uint32),
        ("view_configuration_layers_info", POINTER(SecondaryViewConfigurationLayerInfoMSFT)),
    ]


class SecondaryViewConfigurationSwapchainCreateInfoMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SECONDARY_VIEW_CONFIGURATION_SWAPCHAIN_CREATE_INFO_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_configuration_type", ViewConfigurationType.ctype()),
    ]


ControllerModelKeyMSFT = c_uint64


class ControllerModelKeyStateMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.CONTROLLER_MODEL_KEY_STATE_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("model_key", ControllerModelKeyMSFT),
    ]


class ControllerModelNodePropertiesMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.CONTROLLER_MODEL_NODE_PROPERTIES_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("parent_node_name", (c_char * 64)),
        ("node_name", (c_char * 64)),
    ]


class ControllerModelPropertiesMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.CONTROLLER_MODEL_PROPERTIES_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("node_capacity_input", c_uint32),
        ("node_count_output", c_uint32),
        ("node_properties", POINTER(ControllerModelNodePropertiesMSFT)),
    ]


class ControllerModelNodeStateMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.CONTROLLER_MODEL_NODE_STATE_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("node_pose", Posef),
    ]


class ControllerModelStateMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.CONTROLLER_MODEL_STATE_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("node_capacity_input", c_uint32),
        ("node_count_output", c_uint32),
        ("node_states", POINTER(ControllerModelNodeStateMSFT)),
    ]


PFN_xrGetControllerModelKeyMSFT = CFUNCTYPE(Result.ctype(), SessionHandle, Path, POINTER(ControllerModelKeyStateMSFT))

PFN_xrLoadControllerModelMSFT = CFUNCTYPE(Result.ctype(), SessionHandle, ControllerModelKeyMSFT, c_uint32, POINTER(c_uint32), POINTER(c_uint8))

PFN_xrGetControllerModelPropertiesMSFT = CFUNCTYPE(Result.ctype(), SessionHandle, ControllerModelKeyMSFT, POINTER(ControllerModelPropertiesMSFT))

PFN_xrGetControllerModelStateMSFT = CFUNCTYPE(Result.ctype(), SessionHandle, ControllerModelKeyMSFT, POINTER(ControllerModelStateMSFT))


class ViewConfigurationViewFovEPIC(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.VIEW_CONFIGURATION_VIEW_FOV_EPIC.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("recommended_fov", Fovf),
        ("max_mutable_fov", Fovf),
    ]


class CompositionLayerReprojectionInfoMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.COMPOSITION_LAYER_REPROJECTION_INFO_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("reprojection_mode", ReprojectionModeMSFT.ctype()),
    ]


class CompositionLayerReprojectionPlaneOverrideMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.COMPOSITION_LAYER_REPROJECTION_PLANE_OVERRIDE_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("position", Vector3f),
        ("normal", Vector3f),
        ("velocity", Vector3f),
    ]


PFN_xrEnumerateReprojectionModesMSFT = CFUNCTYPE(Result.ctype(), InstanceHandle, SystemId, ViewConfigurationType.ctype(), c_uint32, POINTER(c_uint32), POINTER(ReprojectionModeMSFT.ctype()))


class SwapchainStateBaseHeaderFB(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SWAPCHAIN_STATE_BASE_HEADER_FB.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


PFN_xrUpdateSwapchainFB = CFUNCTYPE(Result.ctype(), SwapchainHandle, POINTER(SwapchainStateBaseHeaderFB))

PFN_xrGetSwapchainStateFB = CFUNCTYPE(Result.ctype(), SwapchainHandle, POINTER(SwapchainStateBaseHeaderFB))

CompositionLayerSecureContentFlagsFB = Flags64


class CompositionLayerSecureContentFB(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.COMPOSITION_LAYER_SECURE_CONTENT_FB.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", CompositionLayerSecureContentFlagsFB),
    ]


class InteractionProfileAnalogThresholdVALVE(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.INTERACTION_PROFILE_ANALOG_THRESHOLD_VALVE.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("action", ActionHandle),
        ("binding", Path),
        ("on_threshold", c_float),
        ("off_threshold", c_float),
        ("on_haptic", POINTER(HapticBaseHeader)),
        ("off_haptic", POINTER(HapticBaseHeader)),
    ]


class HandJointsMotionRangeInfoEXT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.HAND_JOINTS_MOTION_RANGE_INFO_EXT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("hand_joints_motion_range", HandJointsMotionRangeEXT.ctype()),
    ]


class SceneObserverMSFT_T(Structure):
    pass


SceneObserverMSFTHandle = POINTER(SceneObserverMSFT_T)


class SceneMSFT_T(Structure):
    pass


SceneMSFTHandle = POINTER(SceneMSFT_T)


class UuidMSFT(Structure):
    _fields_ = [
        ("bytes", (c_uint8 * 16)),
    ]


class SceneObserverCreateInfoMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SCENE_OBSERVER_CREATE_INFO_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SceneCreateInfoMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SCENE_CREATE_INFO_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
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
        ("space", SpaceHandle),
        ("time", Time),
        ("sphere_count", c_uint32),
        ("spheres", POINTER(SceneSphereBoundMSFT)),
        ("box_count", c_uint32),
        ("boxes", POINTER(SceneOrientedBoxBoundMSFT)),
        ("frustum_count", c_uint32),
        ("frustums", POINTER(SceneFrustumBoundMSFT)),
    ]


class NewSceneComputeInfoMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.NEW_SCENE_COMPUTE_INFO_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("requested_feature_count", c_uint32),
        ("requested_features", POINTER(c_int)),
        ("consistency", SceneComputeConsistencyMSFT.ctype()),
        ("bounds", SceneBoundsMSFT),
    ]


class VisualMeshComputeLodInfoMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.VISUAL_MESH_COMPUTE_LOD_INFO_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("lod", MeshComputeLodMSFT.ctype()),
    ]


class SceneComponentMSFT(Structure):
    _fields_ = [
        ("component_type", SceneComponentTypeMSFT.ctype()),
        ("id", UuidMSFT),
        ("parent_id", UuidMSFT),
        ("update_time", Time),
    ]


class SceneComponentsMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SCENE_COMPONENTS_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("component_capacity_input", c_uint32),
        ("component_count_output", c_uint32),
        ("components", POINTER(SceneComponentMSFT)),
    ]


class SceneComponentsGetInfoMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SCENE_COMPONENTS_GET_INFO_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("component_type", SceneComponentTypeMSFT.ctype()),
    ]


class SceneComponentLocationMSFT(Structure):
    _fields_ = [
        ("flags", SpaceLocationFlags),
        ("pose", Posef),
    ]


class SceneComponentLocationsMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SCENE_COMPONENT_LOCATIONS_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("location_count", c_uint32),
        ("locations", POINTER(SceneComponentLocationMSFT)),
    ]


class SceneComponentsLocateInfoMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SCENE_COMPONENTS_LOCATE_INFO_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("base_space", SpaceHandle),
        ("time", Time),
        ("component_id_count", c_uint32),
        ("component_ids", POINTER(UuidMSFT)),
    ]


class SceneObjectMSFT(Structure):
    _fields_ = [
        ("object_type", SceneObjectTypeMSFT.ctype()),
    ]


class SceneObjectsMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SCENE_OBJECTS_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("scene_object_count", c_uint32),
        ("scene_objects", POINTER(SceneObjectMSFT)),
    ]


class SceneComponentParentFilterInfoMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SCENE_COMPONENT_PARENT_FILTER_INFO_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("parent_id", UuidMSFT),
    ]


class SceneObjectTypesFilterInfoMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SCENE_OBJECT_TYPES_FILTER_INFO_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("object_type_count", c_uint32),
        ("object_types", POINTER(c_int)),
    ]


class ScenePlaneMSFT(Structure):
    _fields_ = [
        ("alignment", ScenePlaneAlignmentTypeMSFT.ctype()),
        ("size", Extent2Df),
        ("mesh_buffer_id", c_uint64),
        ("supports_indices_uint16", Bool32),
    ]


class ScenePlanesMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SCENE_PLANES_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("scene_plane_count", c_uint32),
        ("scene_planes", POINTER(ScenePlaneMSFT)),
    ]


class ScenePlaneAlignmentFilterInfoMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SCENE_PLANE_ALIGNMENT_FILTER_INFO_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("alignment_count", c_uint32),
        ("alignments", POINTER(c_int)),
    ]


class SceneMeshMSFT(Structure):
    _fields_ = [
        ("mesh_buffer_id", c_uint64),
        ("supports_indices_uint16", Bool32),
    ]


class SceneMeshesMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SCENE_MESHES_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("scene_mesh_count", c_uint32),
        ("scene_meshes", POINTER(SceneMeshMSFT)),
    ]


class SceneMeshBuffersGetInfoMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SCENE_MESH_BUFFERS_GET_INFO_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("mesh_buffer_id", c_uint64),
    ]


class SceneMeshBuffersMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SCENE_MESH_BUFFERS_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SceneMeshVertexBufferMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SCENE_MESH_VERTEX_BUFFER_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("vertex_capacity_input", c_uint32),
        ("vertex_count_output", c_uint32),
        ("vertices", POINTER(Vector3f)),
    ]


class SceneMeshIndicesUint32MSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SCENE_MESH_INDICES_UINT32_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("index_capacity_input", c_uint32),
        ("index_count_output", c_uint32),
        ("indices", POINTER(c_uint32)),
    ]


class SceneMeshIndicesUint16MSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SCENE_MESH_INDICES_UINT16_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("index_capacity_input", c_uint32),
        ("index_count_output", c_uint32),
        ("indices", POINTER(c_uint16)),
    ]


PFN_xrEnumerateSceneComputeFeaturesMSFT = CFUNCTYPE(Result.ctype(), InstanceHandle, SystemId, c_uint32, POINTER(c_uint32), POINTER(SceneComputeFeatureMSFT.ctype()))

PFN_xrCreateSceneObserverMSFT = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(SceneObserverCreateInfoMSFT), POINTER(SceneObserverMSFTHandle))

PFN_xrDestroySceneObserverMSFT = CFUNCTYPE(Result.ctype(), SceneObserverMSFTHandle)

PFN_xrCreateSceneMSFT = CFUNCTYPE(Result.ctype(), SceneObserverMSFTHandle, POINTER(SceneCreateInfoMSFT), POINTER(SceneMSFTHandle))

PFN_xrDestroySceneMSFT = CFUNCTYPE(Result.ctype(), SceneMSFTHandle)

PFN_xrComputeNewSceneMSFT = CFUNCTYPE(Result.ctype(), SceneObserverMSFTHandle, POINTER(NewSceneComputeInfoMSFT))

PFN_xrGetSceneComputeStateMSFT = CFUNCTYPE(Result.ctype(), SceneObserverMSFTHandle, POINTER(SceneComputeStateMSFT.ctype()))

PFN_xrGetSceneComponentsMSFT = CFUNCTYPE(Result.ctype(), SceneMSFTHandle, POINTER(SceneComponentsGetInfoMSFT), POINTER(SceneComponentsMSFT))

PFN_xrLocateSceneComponentsMSFT = CFUNCTYPE(Result.ctype(), SceneMSFTHandle, POINTER(SceneComponentsLocateInfoMSFT), POINTER(SceneComponentLocationsMSFT))

PFN_xrGetSceneMeshBuffersMSFT = CFUNCTYPE(Result.ctype(), SceneMSFTHandle, POINTER(SceneMeshBuffersGetInfoMSFT), POINTER(SceneMeshBuffersMSFT))


class SerializedSceneFragmentDataGetInfoMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SERIALIZED_SCENE_FRAGMENT_DATA_GET_INFO_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("scene_fragment_id", UuidMSFT),
    ]


class DeserializeSceneFragmentMSFT(Structure):
    _fields_ = [
        ("buffer_size", c_uint32),
        ("buffer", POINTER(c_uint8)),
    ]


class SceneDeserializeInfoMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SCENE_DESERIALIZE_INFO_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("fragment_count", c_uint32),
        ("fragments", POINTER(DeserializeSceneFragmentMSFT)),
    ]


PFN_xrDeserializeSceneMSFT = CFUNCTYPE(Result.ctype(), SceneObserverMSFTHandle, POINTER(SceneDeserializeInfoMSFT))

PFN_xrGetSerializedSceneFragmentDataMSFT = CFUNCTYPE(Result.ctype(), SceneMSFTHandle, POINTER(SerializedSceneFragmentDataGetInfoMSFT), c_uint32, POINTER(c_uint32), POINTER(c_uint8))


class EventDataDisplayRefreshRateChangedFB(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.EVENT_DATA_DISPLAY_REFRESH_RATE_CHANGED_FB.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("from_display_refresh_rate", c_float),
        ("to_display_refresh_rate", c_float),
    ]


PFN_xrEnumerateDisplayRefreshRatesFB = CFUNCTYPE(Result.ctype(), SessionHandle, c_uint32, POINTER(c_uint32), POINTER(c_float))

PFN_xrGetDisplayRefreshRateFB = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(c_float))

PFN_xrRequestDisplayRefreshRateFB = CFUNCTYPE(Result.ctype(), SessionHandle, c_float)


class SystemColorSpacePropertiesFB(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SYSTEM_COLOR_SPACE_PROPERTIES_FB.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("color_space", ColorSpaceFB.ctype()),
    ]


PFN_xrEnumerateColorSpacesFB = CFUNCTYPE(Result.ctype(), SessionHandle, c_uint32, POINTER(c_uint32), POINTER(ColorSpaceFB.ctype()))

PFN_xrSetColorSpaceFB = CFUNCTYPE(Result.ctype(), SessionHandle, c_int)


class Vector4sFB(Structure):
    _fields_ = [
        ("x", c_int16),
        ("y", c_int16),
        ("z", c_int16),
        ("w", c_int16),
    ]


class HandTrackingMeshFB(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.HAND_TRACKING_MESH_FB.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("joint_capacity_input", c_uint32),
        ("joint_count_output", c_uint32),
        ("joint_bind_poses", POINTER(Posef)),
        ("joint_radii", POINTER(c_float)),
        ("joint_parents", POINTER(HandJointEXT.ctype())),
        ("vertex_capacity_input", c_uint32),
        ("vertex_count_output", c_uint32),
        ("vertex_positions", POINTER(Vector3f)),
        ("vertex_normals", POINTER(Vector3f)),
        ("vertex_uvs", POINTER(Vector2f)),
        ("vertex_blend_indices", POINTER(Vector4sFB)),
        ("vertex_blend_weights", POINTER(Vector4f)),
        ("index_capacity_input", c_uint32),
        ("index_count_output", c_uint32),
        ("indices", POINTER(c_int16)),
    ]


class HandTrackingScaleFB(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.HAND_TRACKING_SCALE_FB.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("sensor_output", c_float),
        ("current_output", c_float),
        ("override_hand_scale", Bool32),
        ("override_value_input", c_float),
    ]


PFN_xrGetHandMeshFB = CFUNCTYPE(Result.ctype(), HandTrackerEXTHandle, POINTER(HandTrackingMeshFB))

HandTrackingAimFlagsFB = Flags64


class HandTrackingAimStateFB(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.HAND_TRACKING_AIM_STATE_FB.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("status", HandTrackingAimFlagsFB),
        ("aim_pose", Posef),
        ("pinch_strength_index", c_float),
        ("pinch_strength_middle", c_float),
        ("pinch_strength_ring", c_float),
        ("pinch_strength_little", c_float),
    ]


class HandCapsuleFB(Structure):
    _fields_ = [
        ("points", (Vector3f * 2)),
        ("radius", c_float),
        ("joint", HandJointEXT.ctype()),
    ]


class HandTrackingCapsulesStateFB(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.HAND_TRACKING_CAPSULES_STATE_FB.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("capsules", (HandCapsuleFB * 19)),
    ]


class FoveationProfileFB_T(Structure):
    pass


FoveationProfileFBHandle = POINTER(FoveationProfileFB_T)

SwapchainCreateFoveationFlagsFB = Flags64

SwapchainStateFoveationFlagsFB = Flags64


class FoveationProfileCreateInfoFB(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.FOVEATION_PROFILE_CREATE_INFO_FB.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SwapchainCreateInfoFoveationFB(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SWAPCHAIN_CREATE_INFO_FOVEATION_FB.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", SwapchainCreateFoveationFlagsFB),
    ]


class SwapchainStateFoveationFB(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SWAPCHAIN_STATE_FOVEATION_FB.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", SwapchainStateFoveationFlagsFB),
        ("profile", FoveationProfileFBHandle),
    ]


PFN_xrCreateFoveationProfileFB = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(FoveationProfileCreateInfoFB), POINTER(FoveationProfileFBHandle))

PFN_xrDestroyFoveationProfileFB = CFUNCTYPE(Result.ctype(), FoveationProfileFBHandle)


class FoveationLevelProfileCreateInfoFB(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.FOVEATION_LEVEL_PROFILE_CREATE_INFO_FB.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("level", FoveationLevelFB.ctype()),
        ("vertical_offset", c_float),
        ("dynamic", FoveationDynamicFB.ctype()),
    ]


class ViewLocateFoveatedRenderingVARJO(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.VIEW_LOCATE_FOVEATED_RENDERING_VARJO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("foveated_rendering_active", Bool32),
    ]


class FoveatedViewConfigurationViewVARJO(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.FOVEATED_VIEW_CONFIGURATION_VIEW_VARJO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("foveated_rendering_active", Bool32),
    ]


class SystemFoveatedRenderingPropertiesVARJO(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SYSTEM_FOVEATED_RENDERING_PROPERTIES_VARJO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_foveated_rendering", Bool32),
    ]


class CompositionLayerDepthTestVARJO(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.COMPOSITION_LAYER_DEPTH_TEST_VARJO.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("depth_test_range_near_z", c_float),
        ("depth_test_range_far_z", c_float),
    ]


PFN_xrSetEnvironmentDepthEstimationVARJO = CFUNCTYPE(Result.ctype(), SessionHandle, Bool32)


class SpatialAnchorStoreConnectionMSFT_T(Structure):
    pass


SpatialAnchorStoreConnectionMSFTHandle = POINTER(SpatialAnchorStoreConnectionMSFT_T)


class SpatialAnchorPersistenceNameMSFT(Structure):
    _fields_ = [
        ("name", (c_char * 256)),
    ]


class SpatialAnchorPersistenceInfoMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SPATIAL_ANCHOR_PERSISTENCE_INFO_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("spatial_anchor_persistence_name", SpatialAnchorPersistenceNameMSFT),
        ("spatial_anchor", SpatialAnchorMSFTHandle),
    ]


class SpatialAnchorFromPersistedAnchorCreateInfoMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SPATIAL_ANCHOR_FROM_PERSISTED_ANCHOR_CREATE_INFO_MSFT.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("spatial_anchor_store", SpatialAnchorStoreConnectionMSFTHandle),
        ("spatial_anchor_persistence_name", SpatialAnchorPersistenceNameMSFT),
    ]


PFN_xrCreateSpatialAnchorStoreConnectionMSFT = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(SpatialAnchorStoreConnectionMSFTHandle))

PFN_xrDestroySpatialAnchorStoreConnectionMSFT = CFUNCTYPE(Result.ctype(), SpatialAnchorStoreConnectionMSFTHandle)

PFN_xrPersistSpatialAnchorMSFT = CFUNCTYPE(Result.ctype(), SpatialAnchorStoreConnectionMSFTHandle, POINTER(SpatialAnchorPersistenceInfoMSFT))

PFN_xrEnumeratePersistedSpatialAnchorNamesMSFT = CFUNCTYPE(Result.ctype(), SpatialAnchorStoreConnectionMSFTHandle, c_uint32, POINTER(c_uint32), POINTER(SpatialAnchorPersistenceNameMSFT))

PFN_xrCreateSpatialAnchorFromPersistedNameMSFT = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(SpatialAnchorFromPersistedAnchorCreateInfoMSFT), POINTER(SpatialAnchorMSFTHandle))

PFN_xrUnpersistSpatialAnchorMSFT = CFUNCTYPE(Result.ctype(), SpatialAnchorStoreConnectionMSFTHandle, POINTER(SpatialAnchorPersistenceNameMSFT))

PFN_xrClearSpatialAnchorStoreMSFT = CFUNCTYPE(Result.ctype(), SpatialAnchorStoreConnectionMSFTHandle)

CompositionLayerSpaceWarpInfoFlagsFB = Flags64


class CompositionLayerSpaceWarpInfoFB(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.COMPOSITION_LAYER_SPACE_WARP_INFO_FB.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerSpaceWarpInfoFlagsFB),
        ("motion_vector_sub_image", SwapchainSubImage),
        ("app_space_delta_pose", Posef),
        ("depth_sub_image", SwapchainSubImage),
        ("min_depth", c_float),
        ("max_depth", c_float),
        ("near_z", c_float),
        ("far_z", c_float),
    ]


class SystemSpaceWarpPropertiesFB(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SYSTEM_SPACE_WARP_PROPERTIES_FB.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("recommended_motion_vector_image_rect_width", c_uint32),
        ("recommended_motion_vector_image_rect_height", c_uint32),
    ]


__all__ = [
    "VersionNumber",
    "Flags64",
    "SystemId",
    "Bool32",
    "Path",
    "Time",
    "Duration",
    "Instance_T",
    "InstanceHandle",
    "Session_T",
    "SessionHandle",
    "Space_T",
    "SpaceHandle",
    "Action_T",
    "ActionHandle",
    "Swapchain_T",
    "SwapchainHandle",
    "ActionSet_T",
    "ActionSetHandle",
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
    "DebugUtilsMessengerEXTHandle",
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
    "SpatialAnchorMSFTHandle",
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
    "HandTrackerEXTHandle",
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
    "SceneObserverMSFTHandle",
    "SceneMSFT_T",
    "SceneMSFTHandle",
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
    "Vector4sFB",
    "HandTrackingMeshFB",
    "HandTrackingScaleFB",
    "PFN_xrGetHandMeshFB",
    "HandTrackingAimFlagsFB",
    "HandTrackingAimStateFB",
    "HandCapsuleFB",
    "HandTrackingCapsulesStateFB",
    "FoveationProfileFB_T",
    "FoveationProfileFBHandle",
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
    "SpatialAnchorStoreConnectionMSFTHandle",
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
    "CompositionLayerSpaceWarpInfoFlagsFB",
    "CompositionLayerSpaceWarpInfoFB",
    "SystemSpaceWarpPropertiesFB",
]
