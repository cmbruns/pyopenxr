# Warning: this file is auto-generated. Do not edit.

from ctypes import CFUNCTYPE, POINTER, Structure, addressof, c_char, c_char_p, c_float, c_int, c_int16, c_int32, c_int64, c_uint16, c_uint32, c_uint64, c_uint8, c_void_p, cast
from typing import Generator

import numpy

from .enums import *
from .version import *

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
    def __init__(
        self,
        layer_name: str = "",
        spec_version: Version = Version(),
        layer_version: int = 0,
        description: str = "",
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.API_LAYER_PROPERTIES,
    ) -> None:
        super().__init__(
            layer_name=layer_name.encode(),
            spec_version=spec_version.number(),
            layer_version=layer_version,
            description=description.encode(),
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ApiLayerProperties(type={repr(self.type)}, next={repr(self.next)}, layer_name={repr(self.layer_name)}, spec_version={repr(self.spec_version)}, layer_version={repr(self.layer_version)}, description={repr(self.description)})"

    def __str__(self) -> str:
        return f"xr.ApiLayerProperties(type={str(self.type)}, next={str(self.next)}, layer_name={str(self.layer_name)}, spec_version={str(self.spec_version)}, layer_version={str(self.layer_version)}, description={str(self.description)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_name", (c_char * 256)),
        ("spec_version", VersionNumber),
        ("layer_version", c_uint32),
        ("description", (c_char * 256)),
    ]


class ExtensionProperties(Structure):
    def __init__(
        self,
        extension_name: str = "",
        extension_version: int = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.EXTENSION_PROPERTIES,
    ) -> None:
        super().__init__(
            extension_name=extension_name.encode(),
            extension_version=extension_version,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ExtensionProperties(type={repr(self.type)}, next={repr(self.next)}, extension_name={repr(self.extension_name)}, extension_version={repr(self.extension_version)})"

    def __str__(self) -> str:
        return f"xr.ExtensionProperties(type={str(self.type)}, next={str(self.next)}, extension_name={str(self.extension_name)}, extension_version={str(self.extension_version)})"

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
    def __init__(
        self,
        application_name: str = "",
        application_version: int = 0,
        engine_name: str = "",
        engine_version: int = 0,
        api_version: Version = Version(),
    ) -> None:
        super().__init__(
            application_name=application_name.encode(),
            application_version=application_version,
            engine_name=engine_name.encode(),
            engine_version=engine_version,
            api_version=api_version.number(),
        )

    def __repr__(self) -> str:
        return f"xr.ApplicationInfo(application_name={repr(self.application_name)}, application_version={repr(self.application_version)}, engine_name={repr(self.engine_name)}, engine_version={repr(self.engine_version)}, api_version={repr(self.api_version)})"

    def __str__(self) -> str:
        return f"xr.ApplicationInfo(application_name={str(self.application_name)}, application_version={str(self.application_version)}, engine_name={str(self.engine_name)}, engine_version={str(self.engine_version)}, api_version={str(self.api_version)})"

    _fields_ = [
        ("application_name", (c_char * 128)),
        ("application_version", c_uint32),
        ("engine_name", (c_char * 128)),
        ("engine_version", c_uint32),
        ("api_version", VersionNumber),
    ]


class InstanceCreateInfo(Structure):
    def __init__(
        self,
        create_flags: InstanceCreateFlags = 0,
        application_info: ApplicationInfo = None,
        enabled_api_layer_count: int = 0,
        enabled_api_layer_names: POINTER(c_char_p) = None,
        enabled_extension_count: int = 0,
        enabled_extension_names: POINTER(c_char_p) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.INSTANCE_CREATE_INFO,
    ) -> None:
        if application_info is None:
            application_info = ApplicationInfo()
        super().__init__(
            create_flags=create_flags,
            application_info=application_info,
            enabled_api_layer_count=enabled_api_layer_count,
            enabled_api_layer_names=enabled_api_layer_names,
            enabled_extension_count=enabled_extension_count,
            enabled_extension_names=enabled_extension_names,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.InstanceCreateInfo(type={repr(self.type)}, next={repr(self.next)}, create_flags={repr(self.create_flags)}, application_info={repr(self.application_info)}, enabled_api_layer_count={repr(self.enabled_api_layer_count)}, enabled_api_layer_names={repr(self.enabled_api_layer_names)}, enabled_extension_count={repr(self.enabled_extension_count)}, enabled_extension_names={repr(self.enabled_extension_names)})"

    def __str__(self) -> str:
        return f"xr.InstanceCreateInfo(type={str(self.type)}, next={str(self.next)}, create_flags={str(self.create_flags)}, application_info={str(self.application_info)}, enabled_api_layer_count={str(self.enabled_api_layer_count)}, enabled_api_layer_names={str(self.enabled_api_layer_names)}, enabled_extension_count={str(self.enabled_extension_count)}, enabled_extension_names={str(self.enabled_extension_names)})"

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
    def __init__(
        self,
        runtime_version: Version = Version(),
        runtime_name: str = "",
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.INSTANCE_PROPERTIES,
    ) -> None:
        super().__init__(
            runtime_version=runtime_version.number(),
            runtime_name=runtime_name.encode(),
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.InstanceProperties(type={repr(self.type)}, next={repr(self.next)}, runtime_version={repr(self.runtime_version)}, runtime_name={repr(self.runtime_name)})"

    def __str__(self) -> str:
        return f"xr.InstanceProperties(type={str(self.type)}, next={str(self.next)}, runtime_version={str(self.runtime_version)}, runtime_name={str(self.runtime_name)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("runtime_version", VersionNumber),
        ("runtime_name", (c_char * 128)),
    ]


class EventDataBuffer(Structure):
    def __init__(
        self,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.EVENT_DATA_BUFFER,
    ) -> None:
        super().__init__(
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataBuffer(type={repr(self.type)}, next={repr(self.next)}, varying={repr(self.varying)})"

    def __str__(self) -> str:
        return f"xr.EventDataBuffer(type={str(self.type)}, next={str(self.next)}, varying={str(self.varying)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("varying", (c_uint8 * 4000)),
    ]


class SystemGetInfo(Structure):
    def __init__(
        self,
        form_factor: FormFactor = FormFactor(1),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SYSTEM_GET_INFO,
    ) -> None:
        super().__init__(
            form_factor=form_factor.value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SystemGetInfo(type={repr(self.type)}, next={repr(self.next)}, form_factor={repr(self.form_factor)})"

    def __str__(self) -> str:
        return f"xr.SystemGetInfo(type={str(self.type)}, next={str(self.next)}, form_factor={str(self.form_factor)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("form_factor", FormFactor.ctype()),
    ]


class SystemGraphicsProperties(Structure):
    def __init__(
        self,
        max_swapchain_image_height: int = 0,
        max_swapchain_image_width: int = 0,
        max_layer_count: int = 0,
    ) -> None:
        super().__init__(
            max_swapchain_image_height=max_swapchain_image_height,
            max_swapchain_image_width=max_swapchain_image_width,
            max_layer_count=max_layer_count,
        )

    def __repr__(self) -> str:
        return f"xr.SystemGraphicsProperties(max_swapchain_image_height={repr(self.max_swapchain_image_height)}, max_swapchain_image_width={repr(self.max_swapchain_image_width)}, max_layer_count={repr(self.max_layer_count)})"

    def __str__(self) -> str:
        return f"xr.SystemGraphicsProperties(max_swapchain_image_height={str(self.max_swapchain_image_height)}, max_swapchain_image_width={str(self.max_swapchain_image_width)}, max_layer_count={str(self.max_layer_count)})"

    _fields_ = [
        ("max_swapchain_image_height", c_uint32),
        ("max_swapchain_image_width", c_uint32),
        ("max_layer_count", c_uint32),
    ]


class SystemTrackingProperties(Structure):
    def __init__(
        self,
        orientation_tracking: Bool32 = 0,
        position_tracking: Bool32 = 0,
    ) -> None:
        super().__init__(
            orientation_tracking=orientation_tracking,
            position_tracking=position_tracking,
        )

    def __repr__(self) -> str:
        return f"xr.SystemTrackingProperties(orientation_tracking={repr(self.orientation_tracking)}, position_tracking={repr(self.position_tracking)})"

    def __str__(self) -> str:
        return f"xr.SystemTrackingProperties(orientation_tracking={str(self.orientation_tracking)}, position_tracking={str(self.position_tracking)})"

    _fields_ = [
        ("orientation_tracking", Bool32),
        ("position_tracking", Bool32),
    ]


class SystemProperties(Structure):
    def __init__(
        self,
        system_id: SystemId = 0,
        vendor_id: int = 0,
        system_name: str = "",
        graphics_properties: SystemGraphicsProperties = None,
        tracking_properties: SystemTrackingProperties = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SYSTEM_PROPERTIES,
    ) -> None:
        if graphics_properties is None:
            graphics_properties = SystemGraphicsProperties()
        if tracking_properties is None:
            tracking_properties = SystemTrackingProperties()
        super().__init__(
            system_id=system_id,
            vendor_id=vendor_id,
            system_name=system_name.encode(),
            graphics_properties=graphics_properties,
            tracking_properties=tracking_properties,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SystemProperties(type={repr(self.type)}, next={repr(self.next)}, system_id={repr(self.system_id)}, vendor_id={repr(self.vendor_id)}, system_name={repr(self.system_name)}, graphics_properties={repr(self.graphics_properties)}, tracking_properties={repr(self.tracking_properties)})"

    def __str__(self) -> str:
        return f"xr.SystemProperties(type={str(self.type)}, next={str(self.next)}, system_id={str(self.system_id)}, vendor_id={str(self.vendor_id)}, system_name={str(self.system_name)}, graphics_properties={str(self.graphics_properties)}, tracking_properties={str(self.tracking_properties)})"

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
    def __init__(
        self,
        create_flags: SessionCreateFlags = 0,
        system_id: SystemId = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SESSION_CREATE_INFO,
    ) -> None:
        super().__init__(
            create_flags=create_flags,
            system_id=system_id,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SessionCreateInfo(type={repr(self.type)}, next={repr(self.next)}, create_flags={repr(self.create_flags)}, system_id={repr(self.system_id)})"

    def __str__(self) -> str:
        return f"xr.SessionCreateInfo(type={str(self.type)}, next={str(self.next)}, create_flags={str(self.create_flags)}, system_id={str(self.system_id)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("create_flags", SessionCreateFlags),
        ("system_id", SystemId),
    ]


class Vector3f(Structure):
    def __init__(
        self,
        x: float = 0,
        y: float = 0,
        z: float = 0,
    ) -> None:
        super().__init__(
            x=x,
            y=y,
            z=z,
        )

        self._numpy = None

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

    def as_numpy(self):
        if self._numpy is None:
            # Just in time construction
            buffer = (c_float * len(self)).from_address(addressof(self))
            buffer._wrapper = self  # To link lifetime of buffer to self
            self._numpy = numpy.ctypeslib.as_array(buffer)
        return self._numpy

    _fields_ = [
        ("x", c_float),
        ("y", c_float),
        ("z", c_float),
    ]


class SpaceVelocity(Structure):
    def __init__(
        self,
        velocity_flags: SpaceVelocityFlags = 0,
        linear_velocity: Vector3f = None,
        angular_velocity: Vector3f = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SPACE_VELOCITY,
    ) -> None:
        if linear_velocity is None:
            linear_velocity = Vector3f()
        if angular_velocity is None:
            angular_velocity = Vector3f()
        super().__init__(
            velocity_flags=velocity_flags,
            linear_velocity=linear_velocity,
            angular_velocity=angular_velocity,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceVelocity(type={repr(self.type)}, next={repr(self.next)}, velocity_flags={repr(self.velocity_flags)}, linear_velocity={repr(self.linear_velocity)}, angular_velocity={repr(self.angular_velocity)})"

    def __str__(self) -> str:
        return f"xr.SpaceVelocity(type={str(self.type)}, next={str(self.next)}, velocity_flags={str(self.velocity_flags)}, linear_velocity={str(self.linear_velocity)}, angular_velocity={str(self.angular_velocity)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("velocity_flags", SpaceVelocityFlags),
        ("linear_velocity", Vector3f),
        ("angular_velocity", Vector3f),
    ]


class Quaternionf(Structure):
    def __init__(
        self,
        x: float = 0,
        y: float = 0,
        z: float = 0,
        w: float = 1,
    ) -> None:
        super().__init__(
            x=x,
            y=y,
            z=z,
            w=w,
        )

        self._numpy = None

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

    _fields_ = [
        ("x", c_float),
        ("y", c_float),
        ("z", c_float),
        ("w", c_float),
    ]


class Posef(Structure):
    def __init__(
        self,
        orientation: Quaternionf = None,
        position: Vector3f = None,
    ) -> None:
        if orientation is None:
            orientation = Quaternionf()
        if position is None:
            position = Vector3f()
        super().__init__(
            orientation=orientation,
            position=position,
        )

    def __repr__(self) -> str:
        return f"xr.Posef(orientation={repr(self.orientation)}, position={repr(self.position)})"

    def __str__(self) -> str:
        return f"xr.Posef(orientation={str(self.orientation)}, position={str(self.position)})"

    _fields_ = [
        ("orientation", Quaternionf),
        ("position", Vector3f),
    ]


class ReferenceSpaceCreateInfo(Structure):
    def __init__(
        self,
        reference_space_type: ReferenceSpaceType = ReferenceSpaceType(1),
        pose_in_reference_space: Posef = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.REFERENCE_SPACE_CREATE_INFO,
    ) -> None:
        if pose_in_reference_space is None:
            pose_in_reference_space = Posef()
        super().__init__(
            reference_space_type=reference_space_type.value,
            pose_in_reference_space=pose_in_reference_space,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ReferenceSpaceCreateInfo(type={repr(self.type)}, next={repr(self.next)}, reference_space_type={repr(self.reference_space_type)}, pose_in_reference_space={repr(self.pose_in_reference_space)})"

    def __str__(self) -> str:
        return f"xr.ReferenceSpaceCreateInfo(type={str(self.type)}, next={str(self.next)}, reference_space_type={str(self.reference_space_type)}, pose_in_reference_space={str(self.pose_in_reference_space)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("reference_space_type", ReferenceSpaceType.ctype()),
        ("pose_in_reference_space", Posef),
    ]


class Extent2Df(Structure):
    def __init__(
        self,
        width: float = 0,
        height: float = 0,
    ) -> None:
        super().__init__(
            width=width,
            height=height,
        )

        self._numpy = None

    def __iter__(self) -> Generator[float, None, None]:
        yield self.width
        yield self.height

    def __getitem__(self, key):
        return tuple(self)[key]

    def __len__(self) -> int:
        return 2

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

    _fields_ = [
        ("width", c_float),
        ("height", c_float),
    ]


class ActionSpaceCreateInfo(Structure):
    def __init__(
        self,
        action: ActionHandle = None,
        subaction_path: Path = 0,
        pose_in_action_space: Posef = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.ACTION_SPACE_CREATE_INFO,
    ) -> None:
        if pose_in_action_space is None:
            pose_in_action_space = Posef()
        super().__init__(
            action=action,
            subaction_path=subaction_path,
            pose_in_action_space=pose_in_action_space,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ActionSpaceCreateInfo(type={repr(self.type)}, next={repr(self.next)}, action={repr(self.action)}, subaction_path={repr(self.subaction_path)}, pose_in_action_space={repr(self.pose_in_action_space)})"

    def __str__(self) -> str:
        return f"xr.ActionSpaceCreateInfo(type={str(self.type)}, next={str(self.next)}, action={str(self.action)}, subaction_path={str(self.subaction_path)}, pose_in_action_space={str(self.pose_in_action_space)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("action", ActionHandle),
        ("subaction_path", Path),
        ("pose_in_action_space", Posef),
    ]


class SpaceLocation(Structure):
    def __init__(
        self,
        location_flags: SpaceLocationFlags = 0,
        pose: Posef = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SPACE_LOCATION,
    ) -> None:
        if pose is None:
            pose = Posef()
        super().__init__(
            location_flags=location_flags,
            pose=pose,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceLocation(type={repr(self.type)}, next={repr(self.next)}, location_flags={repr(self.location_flags)}, pose={repr(self.pose)})"

    def __str__(self) -> str:
        return f"xr.SpaceLocation(type={str(self.type)}, next={str(self.next)}, location_flags={str(self.location_flags)}, pose={str(self.pose)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("location_flags", SpaceLocationFlags),
        ("pose", Posef),
    ]


class ViewConfigurationProperties(Structure):
    def __init__(
        self,
        view_configuration_type: ViewConfigurationType = ViewConfigurationType(1),
        fov_mutable: Bool32 = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.VIEW_CONFIGURATION_PROPERTIES,
    ) -> None:
        super().__init__(
            view_configuration_type=view_configuration_type.value,
            fov_mutable=fov_mutable,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ViewConfigurationProperties(type={repr(self.type)}, next={repr(self.next)}, view_configuration_type={repr(self.view_configuration_type)}, fov_mutable={repr(self.fov_mutable)})"

    def __str__(self) -> str:
        return f"xr.ViewConfigurationProperties(type={str(self.type)}, next={str(self.next)}, view_configuration_type={str(self.view_configuration_type)}, fov_mutable={str(self.fov_mutable)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_configuration_type", ViewConfigurationType.ctype()),
        ("fov_mutable", Bool32),
    ]


class ViewConfigurationView(Structure):
    def __init__(
        self,
        recommended_image_rect_width: int = 0,
        max_image_rect_width: int = 0,
        recommended_image_rect_height: int = 0,
        max_image_rect_height: int = 0,
        recommended_swapchain_sample_count: int = 0,
        max_swapchain_sample_count: int = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.VIEW_CONFIGURATION_VIEW,
    ) -> None:
        super().__init__(
            recommended_image_rect_width=recommended_image_rect_width,
            max_image_rect_width=max_image_rect_width,
            recommended_image_rect_height=recommended_image_rect_height,
            max_image_rect_height=max_image_rect_height,
            recommended_swapchain_sample_count=recommended_swapchain_sample_count,
            max_swapchain_sample_count=max_swapchain_sample_count,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ViewConfigurationView(type={repr(self.type)}, next={repr(self.next)}, recommended_image_rect_width={repr(self.recommended_image_rect_width)}, max_image_rect_width={repr(self.max_image_rect_width)}, recommended_image_rect_height={repr(self.recommended_image_rect_height)}, max_image_rect_height={repr(self.max_image_rect_height)}, recommended_swapchain_sample_count={repr(self.recommended_swapchain_sample_count)}, max_swapchain_sample_count={repr(self.max_swapchain_sample_count)})"

    def __str__(self) -> str:
        return f"xr.ViewConfigurationView(type={str(self.type)}, next={str(self.next)}, recommended_image_rect_width={str(self.recommended_image_rect_width)}, max_image_rect_width={str(self.max_image_rect_width)}, recommended_image_rect_height={str(self.recommended_image_rect_height)}, max_image_rect_height={str(self.max_image_rect_height)}, recommended_swapchain_sample_count={str(self.recommended_swapchain_sample_count)}, max_swapchain_sample_count={str(self.max_swapchain_sample_count)})"

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
    def __init__(
        self,
        create_flags: SwapchainCreateFlags = 0,
        usage_flags: SwapchainUsageFlags = 0,
        format: int = 0,
        sample_count: int = 0,
        width: int = 0,
        height: int = 0,
        face_count: int = 0,
        array_size: int = 0,
        mip_count: int = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SWAPCHAIN_CREATE_INFO,
    ) -> None:
        super().__init__(
            create_flags=create_flags,
            usage_flags=usage_flags,
            format=format,
            sample_count=sample_count,
            width=width,
            height=height,
            face_count=face_count,
            array_size=array_size,
            mip_count=mip_count,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainCreateInfo(type={repr(self.type)}, next={repr(self.next)}, create_flags={repr(self.create_flags)}, usage_flags={repr(self.usage_flags)}, format={repr(self.format)}, sample_count={repr(self.sample_count)}, width={repr(self.width)}, height={repr(self.height)}, face_count={repr(self.face_count)}, array_size={repr(self.array_size)}, mip_count={repr(self.mip_count)})"

    def __str__(self) -> str:
        return f"xr.SwapchainCreateInfo(type={str(self.type)}, next={str(self.next)}, create_flags={str(self.create_flags)}, usage_flags={str(self.usage_flags)}, format={str(self.format)}, sample_count={str(self.sample_count)}, width={str(self.width)}, height={str(self.height)}, face_count={str(self.face_count)}, array_size={str(self.array_size)}, mip_count={str(self.mip_count)})"

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
    def __init__(
        self,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainImageBaseHeader(type={repr(self.type)}, next={repr(self.next)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageBaseHeader(type={str(self.type)}, next={str(self.next)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SwapchainImageAcquireInfo(Structure):
    def __init__(
        self,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SWAPCHAIN_IMAGE_ACQUIRE_INFO,
    ) -> None:
        super().__init__(
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainImageAcquireInfo(type={repr(self.type)}, next={repr(self.next)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageAcquireInfo(type={str(self.type)}, next={str(self.next)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SwapchainImageWaitInfo(Structure):
    def __init__(
        self,
        timeout: Duration = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SWAPCHAIN_IMAGE_WAIT_INFO,
    ) -> None:
        super().__init__(
            timeout=timeout,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainImageWaitInfo(type={repr(self.type)}, next={repr(self.next)}, timeout={repr(self.timeout)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageWaitInfo(type={str(self.type)}, next={str(self.next)}, timeout={str(self.timeout)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("timeout", Duration),
    ]


class SwapchainImageReleaseInfo(Structure):
    def __init__(
        self,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SWAPCHAIN_IMAGE_RELEASE_INFO,
    ) -> None:
        super().__init__(
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainImageReleaseInfo(type={repr(self.type)}, next={repr(self.next)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageReleaseInfo(type={str(self.type)}, next={str(self.next)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SessionBeginInfo(Structure):
    def __init__(
        self,
        primary_view_configuration_type: ViewConfigurationType = ViewConfigurationType(1),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SESSION_BEGIN_INFO,
    ) -> None:
        super().__init__(
            primary_view_configuration_type=primary_view_configuration_type.value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SessionBeginInfo(type={repr(self.type)}, next={repr(self.next)}, primary_view_configuration_type={repr(self.primary_view_configuration_type)})"

    def __str__(self) -> str:
        return f"xr.SessionBeginInfo(type={str(self.type)}, next={str(self.next)}, primary_view_configuration_type={str(self.primary_view_configuration_type)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("primary_view_configuration_type", ViewConfigurationType.ctype()),
    ]


class FrameWaitInfo(Structure):
    def __init__(
        self,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.FRAME_WAIT_INFO,
    ) -> None:
        super().__init__(
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.FrameWaitInfo(type={repr(self.type)}, next={repr(self.next)})"

    def __str__(self) -> str:
        return f"xr.FrameWaitInfo(type={str(self.type)}, next={str(self.next)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class FrameState(Structure):
    def __init__(
        self,
        predicted_display_time: Time = 0,
        predicted_display_period: Duration = 0,
        should_render: Bool32 = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.FRAME_STATE,
    ) -> None:
        super().__init__(
            predicted_display_time=predicted_display_time,
            predicted_display_period=predicted_display_period,
            should_render=should_render,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.FrameState(type={repr(self.type)}, next={repr(self.next)}, predicted_display_time={repr(self.predicted_display_time)}, predicted_display_period={repr(self.predicted_display_period)}, should_render={repr(self.should_render)})"

    def __str__(self) -> str:
        return f"xr.FrameState(type={str(self.type)}, next={str(self.next)}, predicted_display_time={str(self.predicted_display_time)}, predicted_display_period={str(self.predicted_display_period)}, should_render={str(self.should_render)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("predicted_display_time", Time),
        ("predicted_display_period", Duration),
        ("should_render", Bool32),
    ]


class FrameBeginInfo(Structure):
    def __init__(
        self,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.FRAME_BEGIN_INFO,
    ) -> None:
        super().__init__(
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.FrameBeginInfo(type={repr(self.type)}, next={repr(self.next)})"

    def __str__(self) -> str:
        return f"xr.FrameBeginInfo(type={str(self.type)}, next={str(self.next)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class CompositionLayerBaseHeader(Structure):
    def __init__(
        self,
        layer_flags: CompositionLayerFlags = 0,
        space: SpaceHandle = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            layer_flags=layer_flags,
            space=space,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerBaseHeader(type={repr(self.type)}, next={repr(self.next)}, layer_flags={repr(self.layer_flags)}, space={repr(self.space)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerBaseHeader(type={str(self.type)}, next={str(self.next)}, layer_flags={str(self.layer_flags)}, space={str(self.space)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlags),
        ("space", SpaceHandle),
    ]


class FrameEndInfo(Structure):
    def __init__(
        self,
        display_time: Time = 0,
        environment_blend_mode: EnvironmentBlendMode = EnvironmentBlendMode(1),
        layer_count: int = 0,
        layers: POINTER(POINTER(CompositionLayerBaseHeader)) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.FRAME_END_INFO,
    ) -> None:
        super().__init__(
            display_time=display_time,
            environment_blend_mode=environment_blend_mode.value,
            layer_count=layer_count,
            layers=layers,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.FrameEndInfo(type={repr(self.type)}, next={repr(self.next)}, display_time={repr(self.display_time)}, environment_blend_mode={repr(self.environment_blend_mode)}, layer_count={repr(self.layer_count)}, layers={repr(self.layers)})"

    def __str__(self) -> str:
        return f"xr.FrameEndInfo(type={str(self.type)}, next={str(self.next)}, display_time={str(self.display_time)}, environment_blend_mode={str(self.environment_blend_mode)}, layer_count={str(self.layer_count)}, layers={str(self.layers)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("display_time", Time),
        ("environment_blend_mode", EnvironmentBlendMode.ctype()),
        ("layer_count", c_uint32),
        ("layers", POINTER(POINTER(CompositionLayerBaseHeader))),
    ]


class ViewLocateInfo(Structure):
    def __init__(
        self,
        view_configuration_type: ViewConfigurationType = ViewConfigurationType(1),
        display_time: Time = 0,
        space: SpaceHandle = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.VIEW_LOCATE_INFO,
    ) -> None:
        super().__init__(
            view_configuration_type=view_configuration_type.value,
            display_time=display_time,
            space=space,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ViewLocateInfo(type={repr(self.type)}, next={repr(self.next)}, view_configuration_type={repr(self.view_configuration_type)}, display_time={repr(self.display_time)}, space={repr(self.space)})"

    def __str__(self) -> str:
        return f"xr.ViewLocateInfo(type={str(self.type)}, next={str(self.next)}, view_configuration_type={str(self.view_configuration_type)}, display_time={str(self.display_time)}, space={str(self.space)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_configuration_type", ViewConfigurationType.ctype()),
        ("display_time", Time),
        ("space", SpaceHandle),
    ]


class ViewState(Structure):
    def __init__(
        self,
        view_state_flags: ViewStateFlags = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.VIEW_STATE,
    ) -> None:
        super().__init__(
            view_state_flags=view_state_flags,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ViewState(type={repr(self.type)}, next={repr(self.next)}, view_state_flags={repr(self.view_state_flags)})"

    def __str__(self) -> str:
        return f"xr.ViewState(type={str(self.type)}, next={str(self.next)}, view_state_flags={str(self.view_state_flags)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_state_flags", ViewStateFlags),
    ]


class Fovf(Structure):
    def __init__(
        self,
        angle_left: float = 0,
        angle_right: float = 0,
        angle_up: float = 0,
        angle_down: float = 0,
    ) -> None:
        super().__init__(
            angle_left=angle_left,
            angle_right=angle_right,
            angle_up=angle_up,
            angle_down=angle_down,
        )

        self._numpy = None

    def __iter__(self) -> Generator[float, None, None]:
        yield self.angle_left
        yield self.angle_right
        yield self.angle_up
        yield self.angle_down

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

    _fields_ = [
        ("angle_left", c_float),
        ("angle_right", c_float),
        ("angle_up", c_float),
        ("angle_down", c_float),
    ]


class View(Structure):
    def __init__(
        self,
        pose: Posef = None,
        fov: Fovf = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.VIEW,
    ) -> None:
        if pose is None:
            pose = Posef()
        if fov is None:
            fov = Fovf()
        super().__init__(
            pose=pose,
            fov=fov,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.View(type={repr(self.type)}, next={repr(self.next)}, pose={repr(self.pose)}, fov={repr(self.fov)})"

    def __str__(self) -> str:
        return f"xr.View(type={str(self.type)}, next={str(self.next)}, pose={str(self.pose)}, fov={str(self.fov)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("pose", Posef),
        ("fov", Fovf),
    ]


class ActionSetCreateInfo(Structure):
    def __init__(
        self,
        action_set_name: str = "",
        localized_action_set_name: str = "",
        priority: int = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.ACTION_SET_CREATE_INFO,
    ) -> None:
        super().__init__(
            action_set_name=action_set_name.encode(),
            localized_action_set_name=localized_action_set_name.encode(),
            priority=priority,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ActionSetCreateInfo(type={repr(self.type)}, next={repr(self.next)}, action_set_name={repr(self.action_set_name)}, localized_action_set_name={repr(self.localized_action_set_name)}, priority={repr(self.priority)})"

    def __str__(self) -> str:
        return f"xr.ActionSetCreateInfo(type={str(self.type)}, next={str(self.next)}, action_set_name={str(self.action_set_name)}, localized_action_set_name={str(self.localized_action_set_name)}, priority={str(self.priority)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("action_set_name", (c_char * 64)),
        ("localized_action_set_name", (c_char * 128)),
        ("priority", c_uint32),
    ]


class ActionCreateInfo(Structure):
    def __init__(
        self,
        action_name: str = "",
        action_type: ActionType = ActionType(1),
        count_subaction_paths: int = 0,
        subaction_paths: POINTER(c_uint64) = None,
        localized_action_name: str = "",
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.ACTION_CREATE_INFO,
    ) -> None:
        super().__init__(
            action_name=action_name.encode(),
            action_type=action_type.value,
            count_subaction_paths=count_subaction_paths,
            subaction_paths=subaction_paths,
            localized_action_name=localized_action_name.encode(),
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ActionCreateInfo(type={repr(self.type)}, next={repr(self.next)}, action_name={repr(self.action_name)}, action_type={repr(self.action_type)}, count_subaction_paths={repr(self.count_subaction_paths)}, subaction_paths={repr(self.subaction_paths)}, localized_action_name={repr(self.localized_action_name)})"

    def __str__(self) -> str:
        return f"xr.ActionCreateInfo(type={str(self.type)}, next={str(self.next)}, action_name={str(self.action_name)}, action_type={str(self.action_type)}, count_subaction_paths={str(self.count_subaction_paths)}, subaction_paths={str(self.subaction_paths)}, localized_action_name={str(self.localized_action_name)})"

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
    def __init__(
        self,
        action: ActionHandle = None,
        binding: Path = 0,
    ) -> None:
        super().__init__(
            action=action,
            binding=binding,
        )

    def __repr__(self) -> str:
        return f"xr.ActionSuggestedBinding(action={repr(self.action)}, binding={repr(self.binding)})"

    def __str__(self) -> str:
        return f"xr.ActionSuggestedBinding(action={str(self.action)}, binding={str(self.binding)})"

    _fields_ = [
        ("action", ActionHandle),
        ("binding", Path),
    ]


class InteractionProfileSuggestedBinding(Structure):
    def __init__(
        self,
        interaction_profile: Path = 0,
        count_suggested_bindings: int = 0,
        suggested_bindings: POINTER(ActionSuggestedBinding) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.INTERACTION_PROFILE_SUGGESTED_BINDING,
    ) -> None:
        super().__init__(
            interaction_profile=interaction_profile,
            count_suggested_bindings=count_suggested_bindings,
            suggested_bindings=suggested_bindings,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.InteractionProfileSuggestedBinding(type={repr(self.type)}, next={repr(self.next)}, interaction_profile={repr(self.interaction_profile)}, count_suggested_bindings={repr(self.count_suggested_bindings)}, suggested_bindings={repr(self.suggested_bindings)})"

    def __str__(self) -> str:
        return f"xr.InteractionProfileSuggestedBinding(type={str(self.type)}, next={str(self.next)}, interaction_profile={str(self.interaction_profile)}, count_suggested_bindings={str(self.count_suggested_bindings)}, suggested_bindings={str(self.suggested_bindings)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("interaction_profile", Path),
        ("count_suggested_bindings", c_uint32),
        ("suggested_bindings", POINTER(ActionSuggestedBinding)),
    ]


class SessionActionSetsAttachInfo(Structure):
    def __init__(
        self,
        count_action_sets: int = 0,
        action_sets: POINTER(POINTER(ActionSet_T)) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SESSION_ACTION_SETS_ATTACH_INFO,
    ) -> None:
        super().__init__(
            count_action_sets=count_action_sets,
            action_sets=action_sets,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SessionActionSetsAttachInfo(type={repr(self.type)}, next={repr(self.next)}, count_action_sets={repr(self.count_action_sets)}, action_sets={repr(self.action_sets)})"

    def __str__(self) -> str:
        return f"xr.SessionActionSetsAttachInfo(type={str(self.type)}, next={str(self.next)}, count_action_sets={str(self.count_action_sets)}, action_sets={str(self.action_sets)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("count_action_sets", c_uint32),
        ("action_sets", POINTER(POINTER(ActionSet_T))),
    ]


class InteractionProfileState(Structure):
    def __init__(
        self,
        interaction_profile: Path = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.INTERACTION_PROFILE_STATE,
    ) -> None:
        super().__init__(
            interaction_profile=interaction_profile,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.InteractionProfileState(type={repr(self.type)}, next={repr(self.next)}, interaction_profile={repr(self.interaction_profile)})"

    def __str__(self) -> str:
        return f"xr.InteractionProfileState(type={str(self.type)}, next={str(self.next)}, interaction_profile={str(self.interaction_profile)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("interaction_profile", Path),
    ]


class ActionStateGetInfo(Structure):
    def __init__(
        self,
        action: ActionHandle = None,
        subaction_path: Path = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.ACTION_STATE_GET_INFO,
    ) -> None:
        super().__init__(
            action=action,
            subaction_path=subaction_path,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ActionStateGetInfo(type={repr(self.type)}, next={repr(self.next)}, action={repr(self.action)}, subaction_path={repr(self.subaction_path)})"

    def __str__(self) -> str:
        return f"xr.ActionStateGetInfo(type={str(self.type)}, next={str(self.next)}, action={str(self.action)}, subaction_path={str(self.subaction_path)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("action", ActionHandle),
        ("subaction_path", Path),
    ]


class ActionStateBoolean(Structure):
    def __init__(
        self,
        current_state: Bool32 = 0,
        changed_since_last_sync: Bool32 = 0,
        last_change_time: Time = 0,
        is_active: Bool32 = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.ACTION_STATE_BOOLEAN,
    ) -> None:
        super().__init__(
            current_state=current_state,
            changed_since_last_sync=changed_since_last_sync,
            last_change_time=last_change_time,
            is_active=is_active,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ActionStateBoolean(type={repr(self.type)}, next={repr(self.next)}, current_state={repr(self.current_state)}, changed_since_last_sync={repr(self.changed_since_last_sync)}, last_change_time={repr(self.last_change_time)}, is_active={repr(self.is_active)})"

    def __str__(self) -> str:
        return f"xr.ActionStateBoolean(type={str(self.type)}, next={str(self.next)}, current_state={str(self.current_state)}, changed_since_last_sync={str(self.changed_since_last_sync)}, last_change_time={str(self.last_change_time)}, is_active={str(self.is_active)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("current_state", Bool32),
        ("changed_since_last_sync", Bool32),
        ("last_change_time", Time),
        ("is_active", Bool32),
    ]


class ActionStateFloat(Structure):
    def __init__(
        self,
        current_state: float = 0,
        changed_since_last_sync: Bool32 = 0,
        last_change_time: Time = 0,
        is_active: Bool32 = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.ACTION_STATE_FLOAT,
    ) -> None:
        super().__init__(
            current_state=current_state,
            changed_since_last_sync=changed_since_last_sync,
            last_change_time=last_change_time,
            is_active=is_active,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ActionStateFloat(type={repr(self.type)}, next={repr(self.next)}, current_state={repr(self.current_state)}, changed_since_last_sync={repr(self.changed_since_last_sync)}, last_change_time={repr(self.last_change_time)}, is_active={repr(self.is_active)})"

    def __str__(self) -> str:
        return f"xr.ActionStateFloat(type={str(self.type)}, next={str(self.next)}, current_state={str(self.current_state)}, changed_since_last_sync={str(self.changed_since_last_sync)}, last_change_time={str(self.last_change_time)}, is_active={str(self.is_active)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("current_state", c_float),
        ("changed_since_last_sync", Bool32),
        ("last_change_time", Time),
        ("is_active", Bool32),
    ]


class Vector2f(Structure):
    def __init__(
        self,
        x: float = 0,
        y: float = 0,
    ) -> None:
        super().__init__(
            x=x,
            y=y,
        )

        self._numpy = None

    def __iter__(self) -> Generator[float, None, None]:
        yield self.x
        yield self.y

    def __getitem__(self, key):
        return tuple(self)[key]

    def __len__(self) -> int:
        return 2

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

    _fields_ = [
        ("x", c_float),
        ("y", c_float),
    ]


class ActionStateVector2f(Structure):
    def __init__(
        self,
        current_state: Vector2f = None,
        changed_since_last_sync: Bool32 = 0,
        last_change_time: Time = 0,
        is_active: Bool32 = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.ACTION_STATE_VECTOR2F,
    ) -> None:
        if current_state is None:
            current_state = Vector2f()
        super().__init__(
            current_state=current_state,
            changed_since_last_sync=changed_since_last_sync,
            last_change_time=last_change_time,
            is_active=is_active,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ActionStateVector2f(type={repr(self.type)}, next={repr(self.next)}, current_state={repr(self.current_state)}, changed_since_last_sync={repr(self.changed_since_last_sync)}, last_change_time={repr(self.last_change_time)}, is_active={repr(self.is_active)})"

    def __str__(self) -> str:
        return f"xr.ActionStateVector2f(type={str(self.type)}, next={str(self.next)}, current_state={str(self.current_state)}, changed_since_last_sync={str(self.changed_since_last_sync)}, last_change_time={str(self.last_change_time)}, is_active={str(self.is_active)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("current_state", Vector2f),
        ("changed_since_last_sync", Bool32),
        ("last_change_time", Time),
        ("is_active", Bool32),
    ]


class ActionStatePose(Structure):
    def __init__(
        self,
        is_active: Bool32 = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.ACTION_STATE_POSE,
    ) -> None:
        super().__init__(
            is_active=is_active,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ActionStatePose(type={repr(self.type)}, next={repr(self.next)}, is_active={repr(self.is_active)})"

    def __str__(self) -> str:
        return f"xr.ActionStatePose(type={str(self.type)}, next={str(self.next)}, is_active={str(self.is_active)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("is_active", Bool32),
    ]


class ActiveActionSet(Structure):
    def __init__(
        self,
        action_set: ActionSetHandle = None,
        subaction_path: Path = 0,
    ) -> None:
        super().__init__(
            action_set=action_set,
            subaction_path=subaction_path,
        )

    def __repr__(self) -> str:
        return f"xr.ActiveActionSet(action_set={repr(self.action_set)}, subaction_path={repr(self.subaction_path)})"

    def __str__(self) -> str:
        return f"xr.ActiveActionSet(action_set={str(self.action_set)}, subaction_path={str(self.subaction_path)})"

    _fields_ = [
        ("action_set", ActionSetHandle),
        ("subaction_path", Path),
    ]


class ActionsSyncInfo(Structure):
    def __init__(
        self,
        count_active_action_sets: int = 0,
        active_action_sets: POINTER(ActiveActionSet) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.ACTIONS_SYNC_INFO,
    ) -> None:
        super().__init__(
            count_active_action_sets=count_active_action_sets,
            active_action_sets=active_action_sets,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ActionsSyncInfo(type={repr(self.type)}, next={repr(self.next)}, count_active_action_sets={repr(self.count_active_action_sets)}, active_action_sets={repr(self.active_action_sets)})"

    def __str__(self) -> str:
        return f"xr.ActionsSyncInfo(type={str(self.type)}, next={str(self.next)}, count_active_action_sets={str(self.count_active_action_sets)}, active_action_sets={str(self.active_action_sets)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("count_active_action_sets", c_uint32),
        ("active_action_sets", POINTER(ActiveActionSet)),
    ]


class BoundSourcesForActionEnumerateInfo(Structure):
    def __init__(
        self,
        action: ActionHandle = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.BOUND_SOURCES_FOR_ACTION_ENUMERATE_INFO,
    ) -> None:
        super().__init__(
            action=action,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.BoundSourcesForActionEnumerateInfo(type={repr(self.type)}, next={repr(self.next)}, action={repr(self.action)})"

    def __str__(self) -> str:
        return f"xr.BoundSourcesForActionEnumerateInfo(type={str(self.type)}, next={str(self.next)}, action={str(self.action)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("action", ActionHandle),
    ]


class InputSourceLocalizedNameGetInfo(Structure):
    def __init__(
        self,
        source_path: Path = 0,
        which_components: InputSourceLocalizedNameFlags = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.INPUT_SOURCE_LOCALIZED_NAME_GET_INFO,
    ) -> None:
        super().__init__(
            source_path=source_path,
            which_components=which_components,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.InputSourceLocalizedNameGetInfo(type={repr(self.type)}, next={repr(self.next)}, source_path={repr(self.source_path)}, which_components={repr(self.which_components)})"

    def __str__(self) -> str:
        return f"xr.InputSourceLocalizedNameGetInfo(type={str(self.type)}, next={str(self.next)}, source_path={str(self.source_path)}, which_components={str(self.which_components)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("source_path", Path),
        ("which_components", InputSourceLocalizedNameFlags),
    ]


class HapticActionInfo(Structure):
    def __init__(
        self,
        action: ActionHandle = None,
        subaction_path: Path = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.HAPTIC_ACTION_INFO,
    ) -> None:
        super().__init__(
            action=action,
            subaction_path=subaction_path,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.HapticActionInfo(type={repr(self.type)}, next={repr(self.next)}, action={repr(self.action)}, subaction_path={repr(self.subaction_path)})"

    def __str__(self) -> str:
        return f"xr.HapticActionInfo(type={str(self.type)}, next={str(self.next)}, action={str(self.action)}, subaction_path={str(self.subaction_path)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("action", ActionHandle),
        ("subaction_path", Path),
    ]


class HapticBaseHeader(Structure):
    def __init__(
        self,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.HapticBaseHeader(type={repr(self.type)}, next={repr(self.next)})"

    def __str__(self) -> str:
        return f"xr.HapticBaseHeader(type={str(self.type)}, next={str(self.next)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class BaseInStructure(Structure):
    def __init__(
        self,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.BaseInStructure(type={repr(self.type)}, next={repr(self.next)})"

    def __str__(self) -> str:
        return f"xr.BaseInStructure(type={str(self.type)}, next={str(self.next)})"

    pass


BaseInStructure._fields_ = [
        ("type", StructureType.ctype()),
        ("next", POINTER(BaseInStructure)),
    ]


class BaseOutStructure(Structure):
    def __init__(
        self,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.BaseOutStructure(type={repr(self.type)}, next={repr(self.next)})"

    def __str__(self) -> str:
        return f"xr.BaseOutStructure(type={str(self.type)}, next={str(self.next)})"

    pass


BaseOutStructure._fields_ = [
        ("type", StructureType.ctype()),
        ("next", POINTER(BaseOutStructure)),
    ]


class Offset2Di(Structure):
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
    ) -> None:
        super().__init__(
            x=x,
            y=y,
        )

    def __repr__(self) -> str:
        return f"xr.Offset2Di(x={repr(self.x)}, y={repr(self.y)})"

    def __str__(self) -> str:
        return f"xr.Offset2Di(x={str(self.x)}, y={str(self.y)})"

    _fields_ = [
        ("x", c_int32),
        ("y", c_int32),
    ]


class Extent2Di(Structure):
    def __init__(
        self,
        width: int = 0,
        height: int = 0,
    ) -> None:
        super().__init__(
            width=width,
            height=height,
        )

    def __repr__(self) -> str:
        return f"xr.Extent2Di(width={repr(self.width)}, height={repr(self.height)})"

    def __str__(self) -> str:
        return f"xr.Extent2Di(width={str(self.width)}, height={str(self.height)})"

    _fields_ = [
        ("width", c_int32),
        ("height", c_int32),
    ]


class Rect2Di(Structure):
    def __init__(
        self,
        offset: Offset2Di = None,
        extent: Extent2Di = None,
    ) -> None:
        if offset is None:
            offset = Offset2Di()
        if extent is None:
            extent = Extent2Di()
        super().__init__(
            offset=offset,
            extent=extent,
        )

    def __repr__(self) -> str:
        return f"xr.Rect2Di(offset={repr(self.offset)}, extent={repr(self.extent)})"

    def __str__(self) -> str:
        return f"xr.Rect2Di(offset={str(self.offset)}, extent={str(self.extent)})"

    _fields_ = [
        ("offset", Offset2Di),
        ("extent", Extent2Di),
    ]


class SwapchainSubImage(Structure):
    def __init__(
        self,
        swapchain: SwapchainHandle = None,
        image_rect: Rect2Di = None,
        image_array_index: int = 0,
    ) -> None:
        if image_rect is None:
            image_rect = Rect2Di()
        super().__init__(
            swapchain=swapchain,
            image_rect=image_rect,
            image_array_index=image_array_index,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainSubImage(swapchain={repr(self.swapchain)}, image_rect={repr(self.image_rect)}, image_array_index={repr(self.image_array_index)})"

    def __str__(self) -> str:
        return f"xr.SwapchainSubImage(swapchain={str(self.swapchain)}, image_rect={str(self.image_rect)}, image_array_index={str(self.image_array_index)})"

    _fields_ = [
        ("swapchain", SwapchainHandle),
        ("image_rect", Rect2Di),
        ("image_array_index", c_uint32),
    ]


class CompositionLayerProjectionView(Structure):
    def __init__(
        self,
        pose: Posef = None,
        fov: Fovf = None,
        sub_image: SwapchainSubImage = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.COMPOSITION_LAYER_PROJECTION_VIEW,
    ) -> None:
        if pose is None:
            pose = Posef()
        if fov is None:
            fov = Fovf()
        if sub_image is None:
            sub_image = SwapchainSubImage()
        super().__init__(
            pose=pose,
            fov=fov,
            sub_image=sub_image,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerProjectionView(type={repr(self.type)}, next={repr(self.next)}, pose={repr(self.pose)}, fov={repr(self.fov)}, sub_image={repr(self.sub_image)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerProjectionView(type={str(self.type)}, next={str(self.next)}, pose={str(self.pose)}, fov={str(self.fov)}, sub_image={str(self.sub_image)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("pose", Posef),
        ("fov", Fovf),
        ("sub_image", SwapchainSubImage),
    ]


class CompositionLayerProjection(Structure):
    def __init__(
        self,
        layer_flags: CompositionLayerFlags = 0,
        space: SpaceHandle = None,
        view_count: int = 0,
        views: POINTER(CompositionLayerProjectionView) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.COMPOSITION_LAYER_PROJECTION,
    ) -> None:
        super().__init__(
            layer_flags=layer_flags,
            space=space,
            view_count=view_count,
            views=views,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerProjection(type={repr(self.type)}, next={repr(self.next)}, layer_flags={repr(self.layer_flags)}, space={repr(self.space)}, view_count={repr(self.view_count)}, views={repr(self.views)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerProjection(type={str(self.type)}, next={str(self.next)}, layer_flags={str(self.layer_flags)}, space={str(self.space)}, view_count={str(self.view_count)}, views={str(self.views)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlags),
        ("space", SpaceHandle),
        ("view_count", c_uint32),
        ("views", POINTER(CompositionLayerProjectionView)),
    ]


class CompositionLayerQuad(Structure):
    def __init__(
        self,
        layer_flags: CompositionLayerFlags = 0,
        space: SpaceHandle = None,
        eye_visibility: EyeVisibility = EyeVisibility(1),
        sub_image: SwapchainSubImage = None,
        pose: Posef = None,
        size: Extent2Df = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.COMPOSITION_LAYER_QUAD,
    ) -> None:
        if sub_image is None:
            sub_image = SwapchainSubImage()
        if pose is None:
            pose = Posef()
        if size is None:
            size = Extent2Df()
        super().__init__(
            layer_flags=layer_flags,
            space=space,
            eye_visibility=eye_visibility.value,
            sub_image=sub_image,
            pose=pose,
            size=size,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerQuad(type={repr(self.type)}, next={repr(self.next)}, layer_flags={repr(self.layer_flags)}, space={repr(self.space)}, eye_visibility={repr(self.eye_visibility)}, sub_image={repr(self.sub_image)}, pose={repr(self.pose)}, size={repr(self.size)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerQuad(type={str(self.type)}, next={str(self.next)}, layer_flags={str(self.layer_flags)}, space={str(self.space)}, eye_visibility={str(self.eye_visibility)}, sub_image={str(self.sub_image)}, pose={str(self.pose)}, size={str(self.size)})"

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
    def __init__(
        self,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataBaseHeader(type={repr(self.type)}, next={repr(self.next)})"

    def __str__(self) -> str:
        return f"xr.EventDataBaseHeader(type={str(self.type)}, next={str(self.next)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class EventDataEventsLost(Structure):
    def __init__(
        self,
        lost_event_count: int = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.EVENT_DATA_EVENTS_LOST,
    ) -> None:
        super().__init__(
            lost_event_count=lost_event_count,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataEventsLost(type={repr(self.type)}, next={repr(self.next)}, lost_event_count={repr(self.lost_event_count)})"

    def __str__(self) -> str:
        return f"xr.EventDataEventsLost(type={str(self.type)}, next={str(self.next)}, lost_event_count={str(self.lost_event_count)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("lost_event_count", c_uint32),
    ]


class EventDataInstanceLossPending(Structure):
    def __init__(
        self,
        loss_time: Time = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.EVENT_DATA_INSTANCE_LOSS_PENDING,
    ) -> None:
        super().__init__(
            loss_time=loss_time,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataInstanceLossPending(type={repr(self.type)}, next={repr(self.next)}, loss_time={repr(self.loss_time)})"

    def __str__(self) -> str:
        return f"xr.EventDataInstanceLossPending(type={str(self.type)}, next={str(self.next)}, loss_time={str(self.loss_time)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("loss_time", Time),
    ]


class EventDataSessionStateChanged(Structure):
    def __init__(
        self,
        session: SessionHandle = None,
        state: SessionState = SessionState(1),
        time: Time = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.EVENT_DATA_SESSION_STATE_CHANGED,
    ) -> None:
        super().__init__(
            session=session,
            state=state.value,
            time=time,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataSessionStateChanged(type={repr(self.type)}, next={repr(self.next)}, session={repr(self.session)}, state={repr(self.state)}, time={repr(self.time)})"

    def __str__(self) -> str:
        return f"xr.EventDataSessionStateChanged(type={str(self.type)}, next={str(self.next)}, session={str(self.session)}, state={str(self.state)}, time={str(self.time)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("session", SessionHandle),
        ("state", SessionState.ctype()),
        ("time", Time),
    ]


class EventDataReferenceSpaceChangePending(Structure):
    def __init__(
        self,
        session: SessionHandle = None,
        reference_space_type: ReferenceSpaceType = ReferenceSpaceType(1),
        change_time: Time = 0,
        pose_valid: Bool32 = 0,
        pose_in_previous_space: Posef = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.EVENT_DATA_REFERENCE_SPACE_CHANGE_PENDING,
    ) -> None:
        if pose_in_previous_space is None:
            pose_in_previous_space = Posef()
        super().__init__(
            session=session,
            reference_space_type=reference_space_type.value,
            change_time=change_time,
            pose_valid=pose_valid,
            pose_in_previous_space=pose_in_previous_space,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataReferenceSpaceChangePending(type={repr(self.type)}, next={repr(self.next)}, session={repr(self.session)}, reference_space_type={repr(self.reference_space_type)}, change_time={repr(self.change_time)}, pose_valid={repr(self.pose_valid)}, pose_in_previous_space={repr(self.pose_in_previous_space)})"

    def __str__(self) -> str:
        return f"xr.EventDataReferenceSpaceChangePending(type={str(self.type)}, next={str(self.next)}, session={str(self.session)}, reference_space_type={str(self.reference_space_type)}, change_time={str(self.change_time)}, pose_valid={str(self.pose_valid)}, pose_in_previous_space={str(self.pose_in_previous_space)})"

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
    def __init__(
        self,
        session: SessionHandle = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.EVENT_DATA_INTERACTION_PROFILE_CHANGED,
    ) -> None:
        super().__init__(
            session=session,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataInteractionProfileChanged(type={repr(self.type)}, next={repr(self.next)}, session={repr(self.session)})"

    def __str__(self) -> str:
        return f"xr.EventDataInteractionProfileChanged(type={str(self.type)}, next={str(self.next)}, session={str(self.session)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("session", SessionHandle),
    ]


class HapticVibration(Structure):
    def __init__(
        self,
        duration: Duration = 0,
        frequency: float = 0,
        amplitude: float = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.HAPTIC_VIBRATION,
    ) -> None:
        super().__init__(
            duration=duration,
            frequency=frequency,
            amplitude=amplitude,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.HapticVibration(type={repr(self.type)}, next={repr(self.next)}, duration={repr(self.duration)}, frequency={repr(self.frequency)}, amplitude={repr(self.amplitude)})"

    def __str__(self) -> str:
        return f"xr.HapticVibration(type={str(self.type)}, next={str(self.next)}, duration={str(self.duration)}, frequency={str(self.frequency)}, amplitude={str(self.amplitude)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("duration", Duration),
        ("frequency", c_float),
        ("amplitude", c_float),
    ]


class Offset2Df(Structure):
    def __init__(
        self,
        x: float = 0,
        y: float = 0,
    ) -> None:
        super().__init__(
            x=x,
            y=y,
        )

        self._numpy = None

    def __iter__(self) -> Generator[float, None, None]:
        yield self.x
        yield self.y

    def __getitem__(self, key):
        return tuple(self)[key]

    def __len__(self) -> int:
        return 2

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

    _fields_ = [
        ("x", c_float),
        ("y", c_float),
    ]


class Rect2Df(Structure):
    def __init__(
        self,
        offset: Offset2Df = None,
        extent: Extent2Df = None,
    ) -> None:
        if offset is None:
            offset = Offset2Df()
        if extent is None:
            extent = Extent2Df()
        super().__init__(
            offset=offset,
            extent=extent,
        )

    def __repr__(self) -> str:
        return f"xr.Rect2Df(offset={repr(self.offset)}, extent={repr(self.extent)})"

    def __str__(self) -> str:
        return f"xr.Rect2Df(offset={str(self.offset)}, extent={str(self.extent)})"

    _fields_ = [
        ("offset", Offset2Df),
        ("extent", Extent2Df),
    ]


class Vector4f(Structure):
    def __init__(
        self,
        x: float = 0,
        y: float = 0,
        z: float = 0,
        w: float = 0,
    ) -> None:
        super().__init__(
            x=x,
            y=y,
            z=z,
            w=w,
        )

        self._numpy = None

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

    _fields_ = [
        ("x", c_float),
        ("y", c_float),
        ("z", c_float),
        ("w", c_float),
    ]


class Color4f(Structure):
    def __init__(
        self,
        r: float = 0,
        g: float = 0,
        b: float = 0,
        a: float = 0,
    ) -> None:
        super().__init__(
            r=r,
            g=g,
            b=b,
            a=a,
        )

        self._numpy = None

    def __iter__(self) -> Generator[float, None, None]:
        yield self.r
        yield self.g
        yield self.b
        yield self.a

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
    def __init__(
        self,
        layer_flags: CompositionLayerFlags = 0,
        space: SpaceHandle = None,
        eye_visibility: EyeVisibility = EyeVisibility(1),
        swapchain: SwapchainHandle = None,
        image_array_index: int = 0,
        orientation: Quaternionf = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.COMPOSITION_LAYER_CUBE_KHR,
    ) -> None:
        if orientation is None:
            orientation = Quaternionf()
        super().__init__(
            layer_flags=layer_flags,
            space=space,
            eye_visibility=eye_visibility.value,
            swapchain=swapchain,
            image_array_index=image_array_index,
            orientation=orientation,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerCubeKHR(type={repr(self.type)}, next={repr(self.next)}, layer_flags={repr(self.layer_flags)}, space={repr(self.space)}, eye_visibility={repr(self.eye_visibility)}, swapchain={repr(self.swapchain)}, image_array_index={repr(self.image_array_index)}, orientation={repr(self.orientation)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerCubeKHR(type={str(self.type)}, next={str(self.next)}, layer_flags={str(self.layer_flags)}, space={str(self.space)}, eye_visibility={str(self.eye_visibility)}, swapchain={str(self.swapchain)}, image_array_index={str(self.image_array_index)}, orientation={str(self.orientation)})"

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
    def __init__(
        self,
        sub_image: SwapchainSubImage = None,
        min_depth: float = 0,
        max_depth: float = 0,
        near_z: float = 0,
        far_z: float = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.COMPOSITION_LAYER_DEPTH_INFO_KHR,
    ) -> None:
        if sub_image is None:
            sub_image = SwapchainSubImage()
        super().__init__(
            sub_image=sub_image,
            min_depth=min_depth,
            max_depth=max_depth,
            near_z=near_z,
            far_z=far_z,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerDepthInfoKHR(type={repr(self.type)}, next={repr(self.next)}, sub_image={repr(self.sub_image)}, min_depth={repr(self.min_depth)}, max_depth={repr(self.max_depth)}, near_z={repr(self.near_z)}, far_z={repr(self.far_z)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerDepthInfoKHR(type={str(self.type)}, next={str(self.next)}, sub_image={str(self.sub_image)}, min_depth={str(self.min_depth)}, max_depth={str(self.max_depth)}, near_z={str(self.near_z)}, far_z={str(self.far_z)})"

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
    def __init__(
        self,
        layer_flags: CompositionLayerFlags = 0,
        space: SpaceHandle = None,
        eye_visibility: EyeVisibility = EyeVisibility(1),
        sub_image: SwapchainSubImage = None,
        pose: Posef = None,
        radius: float = 0,
        central_angle: float = 0,
        aspect_ratio: float = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.COMPOSITION_LAYER_CYLINDER_KHR,
    ) -> None:
        if sub_image is None:
            sub_image = SwapchainSubImage()
        if pose is None:
            pose = Posef()
        super().__init__(
            layer_flags=layer_flags,
            space=space,
            eye_visibility=eye_visibility.value,
            sub_image=sub_image,
            pose=pose,
            radius=radius,
            central_angle=central_angle,
            aspect_ratio=aspect_ratio,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerCylinderKHR(type={repr(self.type)}, next={repr(self.next)}, layer_flags={repr(self.layer_flags)}, space={repr(self.space)}, eye_visibility={repr(self.eye_visibility)}, sub_image={repr(self.sub_image)}, pose={repr(self.pose)}, radius={repr(self.radius)}, central_angle={repr(self.central_angle)}, aspect_ratio={repr(self.aspect_ratio)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerCylinderKHR(type={str(self.type)}, next={str(self.next)}, layer_flags={str(self.layer_flags)}, space={str(self.space)}, eye_visibility={str(self.eye_visibility)}, sub_image={str(self.sub_image)}, pose={str(self.pose)}, radius={str(self.radius)}, central_angle={str(self.central_angle)}, aspect_ratio={str(self.aspect_ratio)})"

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
    def __init__(
        self,
        layer_flags: CompositionLayerFlags = 0,
        space: SpaceHandle = None,
        eye_visibility: EyeVisibility = EyeVisibility(1),
        sub_image: SwapchainSubImage = None,
        pose: Posef = None,
        radius: float = 0,
        scale: Vector2f = None,
        bias: Vector2f = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.COMPOSITION_LAYER_EQUIRECT_KHR,
    ) -> None:
        if sub_image is None:
            sub_image = SwapchainSubImage()
        if pose is None:
            pose = Posef()
        if scale is None:
            scale = Vector2f()
        if bias is None:
            bias = Vector2f()
        super().__init__(
            layer_flags=layer_flags,
            space=space,
            eye_visibility=eye_visibility.value,
            sub_image=sub_image,
            pose=pose,
            radius=radius,
            scale=scale,
            bias=bias,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerEquirectKHR(type={repr(self.type)}, next={repr(self.next)}, layer_flags={repr(self.layer_flags)}, space={repr(self.space)}, eye_visibility={repr(self.eye_visibility)}, sub_image={repr(self.sub_image)}, pose={repr(self.pose)}, radius={repr(self.radius)}, scale={repr(self.scale)}, bias={repr(self.bias)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerEquirectKHR(type={str(self.type)}, next={str(self.next)}, layer_flags={str(self.layer_flags)}, space={str(self.space)}, eye_visibility={str(self.eye_visibility)}, sub_image={str(self.sub_image)}, pose={str(self.pose)}, radius={str(self.radius)}, scale={str(self.scale)}, bias={str(self.bias)})"

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
    def __init__(
        self,
        vertex_capacity_input: int = 0,
        vertex_count_output: int = 0,
        vertices: POINTER(Vector2f) = None,
        index_capacity_input: int = 0,
        index_count_output: int = 0,
        indices: POINTER(c_uint32) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.VISIBILITY_MASK_KHR,
    ) -> None:
        super().__init__(
            vertex_capacity_input=vertex_capacity_input,
            vertex_count_output=vertex_count_output,
            vertices=vertices,
            index_capacity_input=index_capacity_input,
            index_count_output=index_count_output,
            indices=indices,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.VisibilityMaskKHR(type={repr(self.type)}, next={repr(self.next)}, vertex_capacity_input={repr(self.vertex_capacity_input)}, vertex_count_output={repr(self.vertex_count_output)}, vertices={repr(self.vertices)}, index_capacity_input={repr(self.index_capacity_input)}, index_count_output={repr(self.index_count_output)}, indices={repr(self.indices)})"

    def __str__(self) -> str:
        return f"xr.VisibilityMaskKHR(type={str(self.type)}, next={str(self.next)}, vertex_capacity_input={str(self.vertex_capacity_input)}, vertex_count_output={str(self.vertex_count_output)}, vertices={str(self.vertices)}, index_capacity_input={str(self.index_capacity_input)}, index_count_output={str(self.index_count_output)}, indices={str(self.indices)})"

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
    def __init__(
        self,
        session: SessionHandle = None,
        view_configuration_type: ViewConfigurationType = ViewConfigurationType(1),
        view_index: int = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.EVENT_DATA_VISIBILITY_MASK_CHANGED_KHR,
    ) -> None:
        super().__init__(
            session=session,
            view_configuration_type=view_configuration_type.value,
            view_index=view_index,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataVisibilityMaskChangedKHR(type={repr(self.type)}, next={repr(self.next)}, session={repr(self.session)}, view_configuration_type={repr(self.view_configuration_type)}, view_index={repr(self.view_index)})"

    def __str__(self) -> str:
        return f"xr.EventDataVisibilityMaskChangedKHR(type={str(self.type)}, next={str(self.next)}, session={str(self.session)}, view_configuration_type={str(self.view_configuration_type)}, view_index={str(self.view_index)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("session", SessionHandle),
        ("view_configuration_type", ViewConfigurationType.ctype()),
        ("view_index", c_uint32),
    ]


PFN_xrGetVisibilityMaskKHR = CFUNCTYPE(Result.ctype(), SessionHandle, ViewConfigurationType.ctype(), c_uint32, VisibilityMaskTypeKHR.ctype(), POINTER(VisibilityMaskKHR))


class CompositionLayerColorScaleBiasKHR(Structure):
    def __init__(
        self,
        color_scale: Color4f = None,
        color_bias: Color4f = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.COMPOSITION_LAYER_COLOR_SCALE_BIAS_KHR,
    ) -> None:
        if color_scale is None:
            color_scale = Color4f()
        if color_bias is None:
            color_bias = Color4f()
        super().__init__(
            color_scale=color_scale,
            color_bias=color_bias,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerColorScaleBiasKHR(type={repr(self.type)}, next={repr(self.next)}, color_scale={repr(self.color_scale)}, color_bias={repr(self.color_bias)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerColorScaleBiasKHR(type={str(self.type)}, next={str(self.next)}, color_scale={str(self.color_scale)}, color_bias={str(self.color_bias)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("color_scale", Color4f),
        ("color_bias", Color4f),
    ]


class LoaderInitInfoBaseHeaderKHR(Structure):
    def __init__(
        self,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.LoaderInitInfoBaseHeaderKHR(type={repr(self.type)}, next={repr(self.next)})"

    def __str__(self) -> str:
        return f"xr.LoaderInitInfoBaseHeaderKHR(type={str(self.type)}, next={str(self.next)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


PFN_xrInitializeLoaderKHR = CFUNCTYPE(Result.ctype(), POINTER(LoaderInitInfoBaseHeaderKHR))


class CompositionLayerEquirect2KHR(Structure):
    def __init__(
        self,
        layer_flags: CompositionLayerFlags = 0,
        space: SpaceHandle = None,
        eye_visibility: EyeVisibility = EyeVisibility(1),
        sub_image: SwapchainSubImage = None,
        pose: Posef = None,
        radius: float = 0,
        central_horizontal_angle: float = 0,
        upper_vertical_angle: float = 0,
        lower_vertical_angle: float = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.COMPOSITION_LAYER_EQUIRECT2_KHR,
    ) -> None:
        if sub_image is None:
            sub_image = SwapchainSubImage()
        if pose is None:
            pose = Posef()
        super().__init__(
            layer_flags=layer_flags,
            space=space,
            eye_visibility=eye_visibility.value,
            sub_image=sub_image,
            pose=pose,
            radius=radius,
            central_horizontal_angle=central_horizontal_angle,
            upper_vertical_angle=upper_vertical_angle,
            lower_vertical_angle=lower_vertical_angle,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerEquirect2KHR(type={repr(self.type)}, next={repr(self.next)}, layer_flags={repr(self.layer_flags)}, space={repr(self.space)}, eye_visibility={repr(self.eye_visibility)}, sub_image={repr(self.sub_image)}, pose={repr(self.pose)}, radius={repr(self.radius)}, central_horizontal_angle={repr(self.central_horizontal_angle)}, upper_vertical_angle={repr(self.upper_vertical_angle)}, lower_vertical_angle={repr(self.lower_vertical_angle)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerEquirect2KHR(type={str(self.type)}, next={str(self.next)}, layer_flags={str(self.layer_flags)}, space={str(self.space)}, eye_visibility={str(self.eye_visibility)}, sub_image={str(self.sub_image)}, pose={str(self.pose)}, radius={str(self.radius)}, central_horizontal_angle={str(self.central_horizontal_angle)}, upper_vertical_angle={str(self.upper_vertical_angle)}, lower_vertical_angle={str(self.lower_vertical_angle)})"

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
    def __init__(
        self,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.BindingModificationBaseHeaderKHR(type={repr(self.type)}, next={repr(self.next)})"

    def __str__(self) -> str:
        return f"xr.BindingModificationBaseHeaderKHR(type={str(self.type)}, next={str(self.next)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class BindingModificationsKHR(Structure):
    def __init__(
        self,
        binding_modification_count: int = 0,
        binding_modifications: POINTER(POINTER(BindingModificationBaseHeaderKHR)) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.BINDING_MODIFICATIONS_KHR,
    ) -> None:
        super().__init__(
            binding_modification_count=binding_modification_count,
            binding_modifications=binding_modifications,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.BindingModificationsKHR(type={repr(self.type)}, next={repr(self.next)}, binding_modification_count={repr(self.binding_modification_count)}, binding_modifications={repr(self.binding_modifications)})"

    def __str__(self) -> str:
        return f"xr.BindingModificationsKHR(type={str(self.type)}, next={str(self.next)}, binding_modification_count={str(self.binding_modification_count)}, binding_modifications={str(self.binding_modifications)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("binding_modification_count", c_uint32),
        ("binding_modifications", POINTER(POINTER(BindingModificationBaseHeaderKHR))),
    ]


class EventDataPerfSettingsEXT(Structure):
    def __init__(
        self,
        domain: PerfSettingsDomainEXT = PerfSettingsDomainEXT(1),
        sub_domain: PerfSettingsSubDomainEXT = PerfSettingsSubDomainEXT(1),
        from_level: PerfSettingsNotificationLevelEXT = PerfSettingsNotificationLevelEXT(0),
        to_level: PerfSettingsNotificationLevelEXT = PerfSettingsNotificationLevelEXT(0),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.EVENT_DATA_PERF_SETTINGS_EXT,
    ) -> None:
        super().__init__(
            domain=domain.value,
            sub_domain=sub_domain.value,
            from_level=from_level.value,
            to_level=to_level.value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataPerfSettingsEXT(type={repr(self.type)}, next={repr(self.next)}, domain={repr(self.domain)}, sub_domain={repr(self.sub_domain)}, from_level={repr(self.from_level)}, to_level={repr(self.to_level)})"

    def __str__(self) -> str:
        return f"xr.EventDataPerfSettingsEXT(type={str(self.type)}, next={str(self.next)}, domain={str(self.domain)}, sub_domain={str(self.sub_domain)}, from_level={str(self.from_level)}, to_level={str(self.to_level)})"

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
    def __init__(
        self,
        object_type: ObjectType = ObjectType(1),
        object_handle: int = 0,
        object_name: str = "",
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.DEBUG_UTILS_OBJECT_NAME_INFO_EXT,
    ) -> None:
        super().__init__(
            object_type=object_type.value,
            object_handle=object_handle,
            object_name=object_name.encode(),
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.DebugUtilsObjectNameInfoEXT(type={repr(self.type)}, next={repr(self.next)}, object_type={repr(self.object_type)}, object_handle={repr(self.object_handle)}, object_name={repr(self.object_name)})"

    def __str__(self) -> str:
        return f"xr.DebugUtilsObjectNameInfoEXT(type={str(self.type)}, next={str(self.next)}, object_type={str(self.object_type)}, object_handle={str(self.object_handle)}, object_name={str(self.object_name)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("object_type", ObjectType.ctype()),
        ("object_handle", c_uint64),
        ("object_name", c_char_p),
    ]


class DebugUtilsLabelEXT(Structure):
    def __init__(
        self,
        label_name: str = "",
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.DEBUG_UTILS_LABEL_EXT,
    ) -> None:
        super().__init__(
            label_name=label_name.encode(),
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.DebugUtilsLabelEXT(type={repr(self.type)}, next={repr(self.next)}, label_name={repr(self.label_name)})"

    def __str__(self) -> str:
        return f"xr.DebugUtilsLabelEXT(type={str(self.type)}, next={str(self.next)}, label_name={str(self.label_name)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("label_name", c_char_p),
    ]


class DebugUtilsMessengerCallbackDataEXT(Structure):
    def __init__(
        self,
        message_id: str = "",
        function_name: str = "",
        message: str = "",
        object_count: int = 0,
        objects: POINTER(DebugUtilsObjectNameInfoEXT) = None,
        session_label_count: int = 0,
        session_labels: POINTER(DebugUtilsLabelEXT) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.DEBUG_UTILS_MESSENGER_CALLBACK_DATA_EXT,
    ) -> None:
        super().__init__(
            message_id=message_id.encode(),
            function_name=function_name.encode(),
            message=message.encode(),
            object_count=object_count,
            objects=objects,
            session_label_count=session_label_count,
            session_labels=session_labels,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.DebugUtilsMessengerCallbackDataEXT(type={repr(self.type)}, next={repr(self.next)}, message_id={repr(self.message_id)}, function_name={repr(self.function_name)}, message={repr(self.message)}, object_count={repr(self.object_count)}, objects={repr(self.objects)}, session_label_count={repr(self.session_label_count)}, session_labels={repr(self.session_labels)})"

    def __str__(self) -> str:
        return f"xr.DebugUtilsMessengerCallbackDataEXT(type={str(self.type)}, next={str(self.next)}, message_id={str(self.message_id)}, function_name={str(self.function_name)}, message={str(self.message)}, object_count={str(self.object_count)}, objects={str(self.objects)}, session_label_count={str(self.session_label_count)}, session_labels={str(self.session_labels)})"

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
    def __init__(
        self,
        message_severities: DebugUtilsMessageSeverityFlagsEXT = 0,
        message_types: DebugUtilsMessageTypeFlagsEXT = 0,
        user_callback: PFN_xrDebugUtilsMessengerCallbackEXT = cast(None, PFN_xrDebugUtilsMessengerCallbackEXT),
        user_data: c_void_p = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.DEBUG_UTILS_MESSENGER_CREATE_INFO_EXT,
    ) -> None:
        super().__init__(
            message_severities=message_severities,
            message_types=message_types,
            user_callback=user_callback,
            user_data=user_data,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.DebugUtilsMessengerCreateInfoEXT(type={repr(self.type)}, next={repr(self.next)}, message_severities={repr(self.message_severities)}, message_types={repr(self.message_types)}, user_callback={repr(self.user_callback)}, user_data={repr(self.user_data)})"

    def __str__(self) -> str:
        return f"xr.DebugUtilsMessengerCreateInfoEXT(type={str(self.type)}, next={str(self.next)}, message_severities={str(self.message_severities)}, message_types={str(self.message_types)}, user_callback={str(self.user_callback)}, user_data={str(self.user_data)})"

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
    def __init__(
        self,
        supports_eye_gaze_interaction: Bool32 = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SYSTEM_EYE_GAZE_INTERACTION_PROPERTIES_EXT,
    ) -> None:
        super().__init__(
            supports_eye_gaze_interaction=supports_eye_gaze_interaction,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SystemEyeGazeInteractionPropertiesEXT(type={repr(self.type)}, next={repr(self.next)}, supports_eye_gaze_interaction={repr(self.supports_eye_gaze_interaction)})"

    def __str__(self) -> str:
        return f"xr.SystemEyeGazeInteractionPropertiesEXT(type={str(self.type)}, next={str(self.next)}, supports_eye_gaze_interaction={str(self.supports_eye_gaze_interaction)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_eye_gaze_interaction", Bool32),
    ]


class EyeGazeSampleTimeEXT(Structure):
    def __init__(
        self,
        time: Time = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.EYE_GAZE_SAMPLE_TIME_EXT,
    ) -> None:
        super().__init__(
            time=time,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.EyeGazeSampleTimeEXT(type={repr(self.type)}, next={repr(self.next)}, time={repr(self.time)})"

    def __str__(self) -> str:
        return f"xr.EyeGazeSampleTimeEXT(type={str(self.type)}, next={str(self.next)}, time={str(self.time)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("time", Time),
    ]


OverlaySessionCreateFlagsEXTX = Flags64

OverlayMainSessionFlagsEXTX = Flags64


class SessionCreateInfoOverlayEXTX(Structure):
    def __init__(
        self,
        create_flags: OverlaySessionCreateFlagsEXTX = 0,
        session_layers_placement: int = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SESSION_CREATE_INFO_OVERLAY_EXTX,
    ) -> None:
        super().__init__(
            create_flags=create_flags,
            session_layers_placement=session_layers_placement,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SessionCreateInfoOverlayEXTX(type={repr(self.type)}, next={repr(self.next)}, create_flags={repr(self.create_flags)}, session_layers_placement={repr(self.session_layers_placement)})"

    def __str__(self) -> str:
        return f"xr.SessionCreateInfoOverlayEXTX(type={str(self.type)}, next={str(self.next)}, create_flags={str(self.create_flags)}, session_layers_placement={str(self.session_layers_placement)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("create_flags", OverlaySessionCreateFlagsEXTX),
        ("session_layers_placement", c_uint32),
    ]


class EventDataMainSessionVisibilityChangedEXTX(Structure):
    def __init__(
        self,
        visible: Bool32 = 0,
        flags: OverlayMainSessionFlagsEXTX = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.EVENT_DATA_MAIN_SESSION_VISIBILITY_CHANGED_EXTX,
    ) -> None:
        super().__init__(
            visible=visible,
            flags=flags,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataMainSessionVisibilityChangedEXTX(type={repr(self.type)}, next={repr(self.next)}, visible={repr(self.visible)}, flags={repr(self.flags)})"

    def __str__(self) -> str:
        return f"xr.EventDataMainSessionVisibilityChangedEXTX(type={str(self.type)}, next={str(self.next)}, visible={str(self.visible)}, flags={str(self.flags)})"

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
    def __init__(
        self,
        space: SpaceHandle = None,
        pose: Posef = None,
        time: Time = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SPATIAL_ANCHOR_CREATE_INFO_MSFT,
    ) -> None:
        if pose is None:
            pose = Posef()
        super().__init__(
            space=space,
            pose=pose,
            time=time,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorCreateInfoMSFT(type={repr(self.type)}, next={repr(self.next)}, space={repr(self.space)}, pose={repr(self.pose)}, time={repr(self.time)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorCreateInfoMSFT(type={str(self.type)}, next={str(self.next)}, space={str(self.space)}, pose={str(self.pose)}, time={str(self.time)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("space", SpaceHandle),
        ("pose", Posef),
        ("time", Time),
    ]


class SpatialAnchorSpaceCreateInfoMSFT(Structure):
    def __init__(
        self,
        anchor: SpatialAnchorMSFTHandle = None,
        pose_in_anchor_space: Posef = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SPATIAL_ANCHOR_SPACE_CREATE_INFO_MSFT,
    ) -> None:
        if pose_in_anchor_space is None:
            pose_in_anchor_space = Posef()
        super().__init__(
            anchor=anchor,
            pose_in_anchor_space=pose_in_anchor_space,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorSpaceCreateInfoMSFT(type={repr(self.type)}, next={repr(self.next)}, anchor={repr(self.anchor)}, pose_in_anchor_space={repr(self.pose_in_anchor_space)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorSpaceCreateInfoMSFT(type={str(self.type)}, next={str(self.next)}, anchor={str(self.anchor)}, pose_in_anchor_space={str(self.pose_in_anchor_space)})"

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
    def __init__(
        self,
        flags: CompositionLayerImageLayoutFlagsFB = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.COMPOSITION_LAYER_IMAGE_LAYOUT_FB,
    ) -> None:
        super().__init__(
            flags=flags,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerImageLayoutFB(type={repr(self.type)}, next={repr(self.next)}, flags={repr(self.flags)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerImageLayoutFB(type={str(self.type)}, next={str(self.next)}, flags={str(self.flags)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", CompositionLayerImageLayoutFlagsFB),
    ]


class CompositionLayerAlphaBlendFB(Structure):
    def __init__(
        self,
        src_factor_color: BlendFactorFB = BlendFactorFB(1),
        dst_factor_color: BlendFactorFB = BlendFactorFB(1),
        src_factor_alpha: BlendFactorFB = BlendFactorFB(1),
        dst_factor_alpha: BlendFactorFB = BlendFactorFB(1),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.COMPOSITION_LAYER_ALPHA_BLEND_FB,
    ) -> None:
        super().__init__(
            src_factor_color=src_factor_color.value,
            dst_factor_color=dst_factor_color.value,
            src_factor_alpha=src_factor_alpha.value,
            dst_factor_alpha=dst_factor_alpha.value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerAlphaBlendFB(type={repr(self.type)}, next={repr(self.next)}, src_factor_color={repr(self.src_factor_color)}, dst_factor_color={repr(self.dst_factor_color)}, src_factor_alpha={repr(self.src_factor_alpha)}, dst_factor_alpha={repr(self.dst_factor_alpha)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerAlphaBlendFB(type={str(self.type)}, next={str(self.next)}, src_factor_color={str(self.src_factor_color)}, dst_factor_color={str(self.dst_factor_color)}, src_factor_alpha={str(self.src_factor_alpha)}, dst_factor_alpha={str(self.dst_factor_alpha)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("src_factor_color", BlendFactorFB.ctype()),
        ("dst_factor_color", BlendFactorFB.ctype()),
        ("src_factor_alpha", BlendFactorFB.ctype()),
        ("dst_factor_alpha", BlendFactorFB.ctype()),
    ]


class ViewConfigurationDepthRangeEXT(Structure):
    def __init__(
        self,
        recommended_near_z: float = 0,
        min_near_z: float = 0,
        recommended_far_z: float = 0,
        max_far_z: float = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.VIEW_CONFIGURATION_DEPTH_RANGE_EXT,
    ) -> None:
        super().__init__(
            recommended_near_z=recommended_near_z,
            min_near_z=min_near_z,
            recommended_far_z=recommended_far_z,
            max_far_z=max_far_z,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ViewConfigurationDepthRangeEXT(type={repr(self.type)}, next={repr(self.next)}, recommended_near_z={repr(self.recommended_near_z)}, min_near_z={repr(self.min_near_z)}, recommended_far_z={repr(self.recommended_far_z)}, max_far_z={repr(self.max_far_z)})"

    def __str__(self) -> str:
        return f"xr.ViewConfigurationDepthRangeEXT(type={str(self.type)}, next={str(self.next)}, recommended_near_z={str(self.recommended_near_z)}, min_near_z={str(self.min_near_z)}, recommended_far_z={str(self.recommended_far_z)}, max_far_z={str(self.max_far_z)})"

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
    def __init__(
        self,
        node_type: SpatialGraphNodeTypeMSFT = SpatialGraphNodeTypeMSFT(1),
        pose: Posef = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SPATIAL_GRAPH_NODE_SPACE_CREATE_INFO_MSFT,
    ) -> None:
        if pose is None:
            pose = Posef()
        super().__init__(
            node_type=node_type.value,
            pose=pose,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialGraphNodeSpaceCreateInfoMSFT(type={repr(self.type)}, next={repr(self.next)}, node_type={repr(self.node_type)}, node_id={repr(self.node_id)}, pose={repr(self.pose)})"

    def __str__(self) -> str:
        return f"xr.SpatialGraphNodeSpaceCreateInfoMSFT(type={str(self.type)}, next={str(self.next)}, node_type={str(self.node_type)}, node_id={str(self.node_id)}, pose={str(self.pose)})"

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
    def __init__(
        self,
        supports_hand_tracking: Bool32 = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SYSTEM_HAND_TRACKING_PROPERTIES_EXT,
    ) -> None:
        super().__init__(
            supports_hand_tracking=supports_hand_tracking,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SystemHandTrackingPropertiesEXT(type={repr(self.type)}, next={repr(self.next)}, supports_hand_tracking={repr(self.supports_hand_tracking)})"

    def __str__(self) -> str:
        return f"xr.SystemHandTrackingPropertiesEXT(type={str(self.type)}, next={str(self.next)}, supports_hand_tracking={str(self.supports_hand_tracking)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_hand_tracking", Bool32),
    ]


class HandTrackerCreateInfoEXT(Structure):
    def __init__(
        self,
        hand: HandEXT = HandEXT(1),
        hand_joint_set: HandJointSetEXT = HandJointSetEXT(0),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.HAND_TRACKER_CREATE_INFO_EXT,
    ) -> None:
        super().__init__(
            hand=hand.value,
            hand_joint_set=hand_joint_set.value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.HandTrackerCreateInfoEXT(type={repr(self.type)}, next={repr(self.next)}, hand={repr(self.hand)}, hand_joint_set={repr(self.hand_joint_set)})"

    def __str__(self) -> str:
        return f"xr.HandTrackerCreateInfoEXT(type={str(self.type)}, next={str(self.next)}, hand={str(self.hand)}, hand_joint_set={str(self.hand_joint_set)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("hand", HandEXT.ctype()),
        ("hand_joint_set", HandJointSetEXT.ctype()),
    ]


class HandJointsLocateInfoEXT(Structure):
    def __init__(
        self,
        base_space: SpaceHandle = None,
        time: Time = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.HAND_JOINTS_LOCATE_INFO_EXT,
    ) -> None:
        super().__init__(
            base_space=base_space,
            time=time,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.HandJointsLocateInfoEXT(type={repr(self.type)}, next={repr(self.next)}, base_space={repr(self.base_space)}, time={repr(self.time)})"

    def __str__(self) -> str:
        return f"xr.HandJointsLocateInfoEXT(type={str(self.type)}, next={str(self.next)}, base_space={str(self.base_space)}, time={str(self.time)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("base_space", SpaceHandle),
        ("time", Time),
    ]


class HandJointLocationEXT(Structure):
    def __init__(
        self,
        location_flags: SpaceLocationFlags = 0,
        pose: Posef = None,
        radius: float = 0,
    ) -> None:
        if pose is None:
            pose = Posef()
        super().__init__(
            location_flags=location_flags,
            pose=pose,
            radius=radius,
        )

    def __repr__(self) -> str:
        return f"xr.HandJointLocationEXT(location_flags={repr(self.location_flags)}, pose={repr(self.pose)}, radius={repr(self.radius)})"

    def __str__(self) -> str:
        return f"xr.HandJointLocationEXT(location_flags={str(self.location_flags)}, pose={str(self.pose)}, radius={str(self.radius)})"

    _fields_ = [
        ("location_flags", SpaceLocationFlags),
        ("pose", Posef),
        ("radius", c_float),
    ]


class HandJointVelocityEXT(Structure):
    def __init__(
        self,
        velocity_flags: SpaceVelocityFlags = 0,
        linear_velocity: Vector3f = None,
        angular_velocity: Vector3f = None,
    ) -> None:
        if linear_velocity is None:
            linear_velocity = Vector3f()
        if angular_velocity is None:
            angular_velocity = Vector3f()
        super().__init__(
            velocity_flags=velocity_flags,
            linear_velocity=linear_velocity,
            angular_velocity=angular_velocity,
        )

    def __repr__(self) -> str:
        return f"xr.HandJointVelocityEXT(velocity_flags={repr(self.velocity_flags)}, linear_velocity={repr(self.linear_velocity)}, angular_velocity={repr(self.angular_velocity)})"

    def __str__(self) -> str:
        return f"xr.HandJointVelocityEXT(velocity_flags={str(self.velocity_flags)}, linear_velocity={str(self.linear_velocity)}, angular_velocity={str(self.angular_velocity)})"

    _fields_ = [
        ("velocity_flags", SpaceVelocityFlags),
        ("linear_velocity", Vector3f),
        ("angular_velocity", Vector3f),
    ]


class HandJointLocationsEXT(Structure):
    def __init__(
        self,
        is_active: Bool32 = 0,
        joint_count: int = 0,
        joint_locations: POINTER(HandJointLocationEXT) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.HAND_JOINT_LOCATIONS_EXT,
    ) -> None:
        super().__init__(
            is_active=is_active,
            joint_count=joint_count,
            joint_locations=joint_locations,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.HandJointLocationsEXT(type={repr(self.type)}, next={repr(self.next)}, is_active={repr(self.is_active)}, joint_count={repr(self.joint_count)}, joint_locations={repr(self.joint_locations)})"

    def __str__(self) -> str:
        return f"xr.HandJointLocationsEXT(type={str(self.type)}, next={str(self.next)}, is_active={str(self.is_active)}, joint_count={str(self.joint_count)}, joint_locations={str(self.joint_locations)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("is_active", Bool32),
        ("joint_count", c_uint32),
        ("joint_locations", POINTER(HandJointLocationEXT)),
    ]


class HandJointVelocitiesEXT(Structure):
    def __init__(
        self,
        joint_count: int = 0,
        joint_velocities: POINTER(HandJointVelocityEXT) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.HAND_JOINT_VELOCITIES_EXT,
    ) -> None:
        super().__init__(
            joint_count=joint_count,
            joint_velocities=joint_velocities,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.HandJointVelocitiesEXT(type={repr(self.type)}, next={repr(self.next)}, joint_count={repr(self.joint_count)}, joint_velocities={repr(self.joint_velocities)})"

    def __str__(self) -> str:
        return f"xr.HandJointVelocitiesEXT(type={str(self.type)}, next={str(self.next)}, joint_count={str(self.joint_count)}, joint_velocities={str(self.joint_velocities)})"

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
    def __init__(
        self,
        supports_hand_tracking_mesh: Bool32 = 0,
        max_hand_mesh_index_count: int = 0,
        max_hand_mesh_vertex_count: int = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SYSTEM_HAND_TRACKING_MESH_PROPERTIES_MSFT,
    ) -> None:
        super().__init__(
            supports_hand_tracking_mesh=supports_hand_tracking_mesh,
            max_hand_mesh_index_count=max_hand_mesh_index_count,
            max_hand_mesh_vertex_count=max_hand_mesh_vertex_count,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SystemHandTrackingMeshPropertiesMSFT(type={repr(self.type)}, next={repr(self.next)}, supports_hand_tracking_mesh={repr(self.supports_hand_tracking_mesh)}, max_hand_mesh_index_count={repr(self.max_hand_mesh_index_count)}, max_hand_mesh_vertex_count={repr(self.max_hand_mesh_vertex_count)})"

    def __str__(self) -> str:
        return f"xr.SystemHandTrackingMeshPropertiesMSFT(type={str(self.type)}, next={str(self.next)}, supports_hand_tracking_mesh={str(self.supports_hand_tracking_mesh)}, max_hand_mesh_index_count={str(self.max_hand_mesh_index_count)}, max_hand_mesh_vertex_count={str(self.max_hand_mesh_vertex_count)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_hand_tracking_mesh", Bool32),
        ("max_hand_mesh_index_count", c_uint32),
        ("max_hand_mesh_vertex_count", c_uint32),
    ]


class HandMeshSpaceCreateInfoMSFT(Structure):
    def __init__(
        self,
        hand_pose_type: HandPoseTypeMSFT = HandPoseTypeMSFT(1),
        pose_in_hand_mesh_space: Posef = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.HAND_MESH_SPACE_CREATE_INFO_MSFT,
    ) -> None:
        if pose_in_hand_mesh_space is None:
            pose_in_hand_mesh_space = Posef()
        super().__init__(
            hand_pose_type=hand_pose_type.value,
            pose_in_hand_mesh_space=pose_in_hand_mesh_space,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.HandMeshSpaceCreateInfoMSFT(type={repr(self.type)}, next={repr(self.next)}, hand_pose_type={repr(self.hand_pose_type)}, pose_in_hand_mesh_space={repr(self.pose_in_hand_mesh_space)})"

    def __str__(self) -> str:
        return f"xr.HandMeshSpaceCreateInfoMSFT(type={str(self.type)}, next={str(self.next)}, hand_pose_type={str(self.hand_pose_type)}, pose_in_hand_mesh_space={str(self.pose_in_hand_mesh_space)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("hand_pose_type", HandPoseTypeMSFT.ctype()),
        ("pose_in_hand_mesh_space", Posef),
    ]


class HandMeshUpdateInfoMSFT(Structure):
    def __init__(
        self,
        time: Time = 0,
        hand_pose_type: HandPoseTypeMSFT = HandPoseTypeMSFT(1),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.HAND_MESH_UPDATE_INFO_MSFT,
    ) -> None:
        super().__init__(
            time=time,
            hand_pose_type=hand_pose_type.value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.HandMeshUpdateInfoMSFT(type={repr(self.type)}, next={repr(self.next)}, time={repr(self.time)}, hand_pose_type={repr(self.hand_pose_type)})"

    def __str__(self) -> str:
        return f"xr.HandMeshUpdateInfoMSFT(type={str(self.type)}, next={str(self.next)}, time={str(self.time)}, hand_pose_type={str(self.hand_pose_type)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("time", Time),
        ("hand_pose_type", HandPoseTypeMSFT.ctype()),
    ]


class HandMeshIndexBufferMSFT(Structure):
    def __init__(
        self,
        index_buffer_key: int = 0,
        index_capacity_input: int = 0,
        index_count_output: int = 0,
        indices: POINTER(c_uint32) = None,
    ) -> None:
        super().__init__(
            index_buffer_key=index_buffer_key,
            index_capacity_input=index_capacity_input,
            index_count_output=index_count_output,
            indices=indices,
        )

    def __repr__(self) -> str:
        return f"xr.HandMeshIndexBufferMSFT(index_buffer_key={repr(self.index_buffer_key)}, index_capacity_input={repr(self.index_capacity_input)}, index_count_output={repr(self.index_count_output)}, indices={repr(self.indices)})"

    def __str__(self) -> str:
        return f"xr.HandMeshIndexBufferMSFT(index_buffer_key={str(self.index_buffer_key)}, index_capacity_input={str(self.index_capacity_input)}, index_count_output={str(self.index_count_output)}, indices={str(self.indices)})"

    _fields_ = [
        ("index_buffer_key", c_uint32),
        ("index_capacity_input", c_uint32),
        ("index_count_output", c_uint32),
        ("indices", POINTER(c_uint32)),
    ]


class HandMeshVertexMSFT(Structure):
    def __init__(
        self,
        position: Vector3f = None,
        normal: Vector3f = None,
    ) -> None:
        if position is None:
            position = Vector3f()
        if normal is None:
            normal = Vector3f()
        super().__init__(
            position=position,
            normal=normal,
        )

    def __repr__(self) -> str:
        return f"xr.HandMeshVertexMSFT(position={repr(self.position)}, normal={repr(self.normal)})"

    def __str__(self) -> str:
        return f"xr.HandMeshVertexMSFT(position={str(self.position)}, normal={str(self.normal)})"

    _fields_ = [
        ("position", Vector3f),
        ("normal", Vector3f),
    ]


class HandMeshVertexBufferMSFT(Structure):
    def __init__(
        self,
        vertex_update_time: Time = 0,
        vertex_capacity_input: int = 0,
        vertex_count_output: int = 0,
        vertices: POINTER(HandMeshVertexMSFT) = None,
    ) -> None:
        super().__init__(
            vertex_update_time=vertex_update_time,
            vertex_capacity_input=vertex_capacity_input,
            vertex_count_output=vertex_count_output,
            vertices=vertices,
        )

    def __repr__(self) -> str:
        return f"xr.HandMeshVertexBufferMSFT(vertex_update_time={repr(self.vertex_update_time)}, vertex_capacity_input={repr(self.vertex_capacity_input)}, vertex_count_output={repr(self.vertex_count_output)}, vertices={repr(self.vertices)})"

    def __str__(self) -> str:
        return f"xr.HandMeshVertexBufferMSFT(vertex_update_time={str(self.vertex_update_time)}, vertex_capacity_input={str(self.vertex_capacity_input)}, vertex_count_output={str(self.vertex_count_output)}, vertices={str(self.vertices)})"

    _fields_ = [
        ("vertex_update_time", Time),
        ("vertex_capacity_input", c_uint32),
        ("vertex_count_output", c_uint32),
        ("vertices", POINTER(HandMeshVertexMSFT)),
    ]


class HandMeshMSFT(Structure):
    def __init__(
        self,
        is_active: Bool32 = 0,
        index_buffer_changed: Bool32 = 0,
        vertex_buffer_changed: Bool32 = 0,
        index_buffer: HandMeshIndexBufferMSFT = None,
        vertex_buffer: HandMeshVertexBufferMSFT = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.HAND_MESH_MSFT,
    ) -> None:
        if index_buffer is None:
            index_buffer = HandMeshIndexBufferMSFT()
        if vertex_buffer is None:
            vertex_buffer = HandMeshVertexBufferMSFT()
        super().__init__(
            is_active=is_active,
            index_buffer_changed=index_buffer_changed,
            vertex_buffer_changed=vertex_buffer_changed,
            index_buffer=index_buffer,
            vertex_buffer=vertex_buffer,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.HandMeshMSFT(type={repr(self.type)}, next={repr(self.next)}, is_active={repr(self.is_active)}, index_buffer_changed={repr(self.index_buffer_changed)}, vertex_buffer_changed={repr(self.vertex_buffer_changed)}, index_buffer={repr(self.index_buffer)}, vertex_buffer={repr(self.vertex_buffer)})"

    def __str__(self) -> str:
        return f"xr.HandMeshMSFT(type={str(self.type)}, next={str(self.next)}, is_active={str(self.is_active)}, index_buffer_changed={str(self.index_buffer_changed)}, vertex_buffer_changed={str(self.vertex_buffer_changed)}, index_buffer={str(self.index_buffer)}, vertex_buffer={str(self.vertex_buffer)})"

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
    def __init__(
        self,
        hand_pose_type: HandPoseTypeMSFT = HandPoseTypeMSFT(1),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.HAND_POSE_TYPE_INFO_MSFT,
    ) -> None:
        super().__init__(
            hand_pose_type=hand_pose_type.value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.HandPoseTypeInfoMSFT(type={repr(self.type)}, next={repr(self.next)}, hand_pose_type={repr(self.hand_pose_type)})"

    def __str__(self) -> str:
        return f"xr.HandPoseTypeInfoMSFT(type={str(self.type)}, next={str(self.next)}, hand_pose_type={str(self.hand_pose_type)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("hand_pose_type", HandPoseTypeMSFT.ctype()),
    ]


PFN_xrCreateHandMeshSpaceMSFT = CFUNCTYPE(Result.ctype(), HandTrackerEXTHandle, POINTER(HandMeshSpaceCreateInfoMSFT), POINTER(SpaceHandle))

PFN_xrUpdateHandMeshMSFT = CFUNCTYPE(Result.ctype(), HandTrackerEXTHandle, POINTER(HandMeshUpdateInfoMSFT), POINTER(HandMeshMSFT))


class SecondaryViewConfigurationSessionBeginInfoMSFT(Structure):
    def __init__(
        self,
        view_configuration_count: int = 0,
        enabled_view_configuration_types: POINTER(c_int) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SECONDARY_VIEW_CONFIGURATION_SESSION_BEGIN_INFO_MSFT,
    ) -> None:
        super().__init__(
            view_configuration_count=view_configuration_count,
            enabled_view_configuration_types=enabled_view_configuration_types,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SecondaryViewConfigurationSessionBeginInfoMSFT(type={repr(self.type)}, next={repr(self.next)}, view_configuration_count={repr(self.view_configuration_count)}, enabled_view_configuration_types={repr(self.enabled_view_configuration_types)})"

    def __str__(self) -> str:
        return f"xr.SecondaryViewConfigurationSessionBeginInfoMSFT(type={str(self.type)}, next={str(self.next)}, view_configuration_count={str(self.view_configuration_count)}, enabled_view_configuration_types={str(self.enabled_view_configuration_types)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_configuration_count", c_uint32),
        ("enabled_view_configuration_types", POINTER(c_int)),
    ]


class SecondaryViewConfigurationStateMSFT(Structure):
    def __init__(
        self,
        view_configuration_type: ViewConfigurationType = ViewConfigurationType(1),
        active: Bool32 = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SECONDARY_VIEW_CONFIGURATION_STATE_MSFT,
    ) -> None:
        super().__init__(
            view_configuration_type=view_configuration_type.value,
            active=active,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SecondaryViewConfigurationStateMSFT(type={repr(self.type)}, next={repr(self.next)}, view_configuration_type={repr(self.view_configuration_type)}, active={repr(self.active)})"

    def __str__(self) -> str:
        return f"xr.SecondaryViewConfigurationStateMSFT(type={str(self.type)}, next={str(self.next)}, view_configuration_type={str(self.view_configuration_type)}, active={str(self.active)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_configuration_type", ViewConfigurationType.ctype()),
        ("active", Bool32),
    ]


class SecondaryViewConfigurationFrameStateMSFT(Structure):
    def __init__(
        self,
        view_configuration_count: int = 0,
        view_configuration_states: POINTER(SecondaryViewConfigurationStateMSFT) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SECONDARY_VIEW_CONFIGURATION_FRAME_STATE_MSFT,
    ) -> None:
        super().__init__(
            view_configuration_count=view_configuration_count,
            view_configuration_states=view_configuration_states,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SecondaryViewConfigurationFrameStateMSFT(type={repr(self.type)}, next={repr(self.next)}, view_configuration_count={repr(self.view_configuration_count)}, view_configuration_states={repr(self.view_configuration_states)})"

    def __str__(self) -> str:
        return f"xr.SecondaryViewConfigurationFrameStateMSFT(type={str(self.type)}, next={str(self.next)}, view_configuration_count={str(self.view_configuration_count)}, view_configuration_states={str(self.view_configuration_states)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_configuration_count", c_uint32),
        ("view_configuration_states", POINTER(SecondaryViewConfigurationStateMSFT)),
    ]


class SecondaryViewConfigurationLayerInfoMSFT(Structure):
    def __init__(
        self,
        view_configuration_type: ViewConfigurationType = ViewConfigurationType(1),
        environment_blend_mode: EnvironmentBlendMode = EnvironmentBlendMode(1),
        layer_count: int = 0,
        layers: POINTER(POINTER(CompositionLayerBaseHeader)) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SECONDARY_VIEW_CONFIGURATION_LAYER_INFO_MSFT,
    ) -> None:
        super().__init__(
            view_configuration_type=view_configuration_type.value,
            environment_blend_mode=environment_blend_mode.value,
            layer_count=layer_count,
            layers=layers,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SecondaryViewConfigurationLayerInfoMSFT(type={repr(self.type)}, next={repr(self.next)}, view_configuration_type={repr(self.view_configuration_type)}, environment_blend_mode={repr(self.environment_blend_mode)}, layer_count={repr(self.layer_count)}, layers={repr(self.layers)})"

    def __str__(self) -> str:
        return f"xr.SecondaryViewConfigurationLayerInfoMSFT(type={str(self.type)}, next={str(self.next)}, view_configuration_type={str(self.view_configuration_type)}, environment_blend_mode={str(self.environment_blend_mode)}, layer_count={str(self.layer_count)}, layers={str(self.layers)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_configuration_type", ViewConfigurationType.ctype()),
        ("environment_blend_mode", EnvironmentBlendMode.ctype()),
        ("layer_count", c_uint32),
        ("layers", POINTER(POINTER(CompositionLayerBaseHeader))),
    ]


class SecondaryViewConfigurationFrameEndInfoMSFT(Structure):
    def __init__(
        self,
        view_configuration_count: int = 0,
        view_configuration_layers_info: POINTER(SecondaryViewConfigurationLayerInfoMSFT) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SECONDARY_VIEW_CONFIGURATION_FRAME_END_INFO_MSFT,
    ) -> None:
        super().__init__(
            view_configuration_count=view_configuration_count,
            view_configuration_layers_info=view_configuration_layers_info,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SecondaryViewConfigurationFrameEndInfoMSFT(type={repr(self.type)}, next={repr(self.next)}, view_configuration_count={repr(self.view_configuration_count)}, view_configuration_layers_info={repr(self.view_configuration_layers_info)})"

    def __str__(self) -> str:
        return f"xr.SecondaryViewConfigurationFrameEndInfoMSFT(type={str(self.type)}, next={str(self.next)}, view_configuration_count={str(self.view_configuration_count)}, view_configuration_layers_info={str(self.view_configuration_layers_info)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_configuration_count", c_uint32),
        ("view_configuration_layers_info", POINTER(SecondaryViewConfigurationLayerInfoMSFT)),
    ]


class SecondaryViewConfigurationSwapchainCreateInfoMSFT(Structure):
    def __init__(
        self,
        view_configuration_type: ViewConfigurationType = ViewConfigurationType(1),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SECONDARY_VIEW_CONFIGURATION_SWAPCHAIN_CREATE_INFO_MSFT,
    ) -> None:
        super().__init__(
            view_configuration_type=view_configuration_type.value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SecondaryViewConfigurationSwapchainCreateInfoMSFT(type={repr(self.type)}, next={repr(self.next)}, view_configuration_type={repr(self.view_configuration_type)})"

    def __str__(self) -> str:
        return f"xr.SecondaryViewConfigurationSwapchainCreateInfoMSFT(type={str(self.type)}, next={str(self.next)}, view_configuration_type={str(self.view_configuration_type)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_configuration_type", ViewConfigurationType.ctype()),
    ]


ControllerModelKeyMSFT = c_uint64


class ControllerModelKeyStateMSFT(Structure):
    def __init__(
        self,
        model_key: ControllerModelKeyMSFT = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.CONTROLLER_MODEL_KEY_STATE_MSFT,
    ) -> None:
        super().__init__(
            model_key=model_key,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ControllerModelKeyStateMSFT(type={repr(self.type)}, next={repr(self.next)}, model_key={repr(self.model_key)})"

    def __str__(self) -> str:
        return f"xr.ControllerModelKeyStateMSFT(type={str(self.type)}, next={str(self.next)}, model_key={str(self.model_key)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("model_key", ControllerModelKeyMSFT),
    ]


class ControllerModelNodePropertiesMSFT(Structure):
    def __init__(
        self,
        parent_node_name: str = "",
        node_name: str = "",
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.CONTROLLER_MODEL_NODE_PROPERTIES_MSFT,
    ) -> None:
        super().__init__(
            parent_node_name=parent_node_name.encode(),
            node_name=node_name.encode(),
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ControllerModelNodePropertiesMSFT(type={repr(self.type)}, next={repr(self.next)}, parent_node_name={repr(self.parent_node_name)}, node_name={repr(self.node_name)})"

    def __str__(self) -> str:
        return f"xr.ControllerModelNodePropertiesMSFT(type={str(self.type)}, next={str(self.next)}, parent_node_name={str(self.parent_node_name)}, node_name={str(self.node_name)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("parent_node_name", (c_char * 64)),
        ("node_name", (c_char * 64)),
    ]


class ControllerModelPropertiesMSFT(Structure):
    def __init__(
        self,
        node_capacity_input: int = 0,
        node_count_output: int = 0,
        node_properties: POINTER(ControllerModelNodePropertiesMSFT) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.CONTROLLER_MODEL_PROPERTIES_MSFT,
    ) -> None:
        super().__init__(
            node_capacity_input=node_capacity_input,
            node_count_output=node_count_output,
            node_properties=node_properties,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ControllerModelPropertiesMSFT(type={repr(self.type)}, next={repr(self.next)}, node_capacity_input={repr(self.node_capacity_input)}, node_count_output={repr(self.node_count_output)}, node_properties={repr(self.node_properties)})"

    def __str__(self) -> str:
        return f"xr.ControllerModelPropertiesMSFT(type={str(self.type)}, next={str(self.next)}, node_capacity_input={str(self.node_capacity_input)}, node_count_output={str(self.node_count_output)}, node_properties={str(self.node_properties)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("node_capacity_input", c_uint32),
        ("node_count_output", c_uint32),
        ("node_properties", POINTER(ControllerModelNodePropertiesMSFT)),
    ]


class ControllerModelNodeStateMSFT(Structure):
    def __init__(
        self,
        node_pose: Posef = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.CONTROLLER_MODEL_NODE_STATE_MSFT,
    ) -> None:
        if node_pose is None:
            node_pose = Posef()
        super().__init__(
            node_pose=node_pose,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ControllerModelNodeStateMSFT(type={repr(self.type)}, next={repr(self.next)}, node_pose={repr(self.node_pose)})"

    def __str__(self) -> str:
        return f"xr.ControllerModelNodeStateMSFT(type={str(self.type)}, next={str(self.next)}, node_pose={str(self.node_pose)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("node_pose", Posef),
    ]


class ControllerModelStateMSFT(Structure):
    def __init__(
        self,
        node_capacity_input: int = 0,
        node_count_output: int = 0,
        node_states: POINTER(ControllerModelNodeStateMSFT) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.CONTROLLER_MODEL_STATE_MSFT,
    ) -> None:
        super().__init__(
            node_capacity_input=node_capacity_input,
            node_count_output=node_count_output,
            node_states=node_states,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ControllerModelStateMSFT(type={repr(self.type)}, next={repr(self.next)}, node_capacity_input={repr(self.node_capacity_input)}, node_count_output={repr(self.node_count_output)}, node_states={repr(self.node_states)})"

    def __str__(self) -> str:
        return f"xr.ControllerModelStateMSFT(type={str(self.type)}, next={str(self.next)}, node_capacity_input={str(self.node_capacity_input)}, node_count_output={str(self.node_count_output)}, node_states={str(self.node_states)})"

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
    def __init__(
        self,
        recommended_fov: Fovf = None,
        max_mutable_fov: Fovf = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.VIEW_CONFIGURATION_VIEW_FOV_EPIC,
    ) -> None:
        if recommended_fov is None:
            recommended_fov = Fovf()
        if max_mutable_fov is None:
            max_mutable_fov = Fovf()
        super().__init__(
            recommended_fov=recommended_fov,
            max_mutable_fov=max_mutable_fov,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ViewConfigurationViewFovEPIC(type={repr(self.type)}, next={repr(self.next)}, recommended_fov={repr(self.recommended_fov)}, max_mutable_fov={repr(self.max_mutable_fov)})"

    def __str__(self) -> str:
        return f"xr.ViewConfigurationViewFovEPIC(type={str(self.type)}, next={str(self.next)}, recommended_fov={str(self.recommended_fov)}, max_mutable_fov={str(self.max_mutable_fov)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("recommended_fov", Fovf),
        ("max_mutable_fov", Fovf),
    ]


class CompositionLayerReprojectionInfoMSFT(Structure):
    def __init__(
        self,
        reprojection_mode: ReprojectionModeMSFT = ReprojectionModeMSFT(1),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.COMPOSITION_LAYER_REPROJECTION_INFO_MSFT,
    ) -> None:
        super().__init__(
            reprojection_mode=reprojection_mode.value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerReprojectionInfoMSFT(type={repr(self.type)}, next={repr(self.next)}, reprojection_mode={repr(self.reprojection_mode)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerReprojectionInfoMSFT(type={str(self.type)}, next={str(self.next)}, reprojection_mode={str(self.reprojection_mode)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("reprojection_mode", ReprojectionModeMSFT.ctype()),
    ]


class CompositionLayerReprojectionPlaneOverrideMSFT(Structure):
    def __init__(
        self,
        position: Vector3f = None,
        normal: Vector3f = None,
        velocity: Vector3f = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.COMPOSITION_LAYER_REPROJECTION_PLANE_OVERRIDE_MSFT,
    ) -> None:
        if position is None:
            position = Vector3f()
        if normal is None:
            normal = Vector3f()
        if velocity is None:
            velocity = Vector3f()
        super().__init__(
            position=position,
            normal=normal,
            velocity=velocity,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerReprojectionPlaneOverrideMSFT(type={repr(self.type)}, next={repr(self.next)}, position={repr(self.position)}, normal={repr(self.normal)}, velocity={repr(self.velocity)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerReprojectionPlaneOverrideMSFT(type={str(self.type)}, next={str(self.next)}, position={str(self.position)}, normal={str(self.normal)}, velocity={str(self.velocity)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("position", Vector3f),
        ("normal", Vector3f),
        ("velocity", Vector3f),
    ]


PFN_xrEnumerateReprojectionModesMSFT = CFUNCTYPE(Result.ctype(), InstanceHandle, SystemId, ViewConfigurationType.ctype(), c_uint32, POINTER(c_uint32), POINTER(ReprojectionModeMSFT.ctype()))


class SwapchainStateBaseHeaderFB(Structure):
    def __init__(
        self,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainStateBaseHeaderFB(type={repr(self.type)}, next={repr(self.next)})"

    def __str__(self) -> str:
        return f"xr.SwapchainStateBaseHeaderFB(type={str(self.type)}, next={str(self.next)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


PFN_xrUpdateSwapchainFB = CFUNCTYPE(Result.ctype(), SwapchainHandle, POINTER(SwapchainStateBaseHeaderFB))

PFN_xrGetSwapchainStateFB = CFUNCTYPE(Result.ctype(), SwapchainHandle, POINTER(SwapchainStateBaseHeaderFB))

CompositionLayerSecureContentFlagsFB = Flags64


class CompositionLayerSecureContentFB(Structure):
    def __init__(
        self,
        flags: CompositionLayerSecureContentFlagsFB = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.COMPOSITION_LAYER_SECURE_CONTENT_FB,
    ) -> None:
        super().__init__(
            flags=flags,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerSecureContentFB(type={repr(self.type)}, next={repr(self.next)}, flags={repr(self.flags)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerSecureContentFB(type={str(self.type)}, next={str(self.next)}, flags={str(self.flags)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", CompositionLayerSecureContentFlagsFB),
    ]


class InteractionProfileAnalogThresholdVALVE(Structure):
    def __init__(
        self,
        action: ActionHandle = None,
        binding: Path = 0,
        on_threshold: float = 0,
        off_threshold: float = 0,
        on_haptic: POINTER(HapticBaseHeader) = None,
        off_haptic: POINTER(HapticBaseHeader) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.INTERACTION_PROFILE_ANALOG_THRESHOLD_VALVE,
    ) -> None:
        super().__init__(
            action=action,
            binding=binding,
            on_threshold=on_threshold,
            off_threshold=off_threshold,
            on_haptic=on_haptic,
            off_haptic=off_haptic,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.InteractionProfileAnalogThresholdVALVE(type={repr(self.type)}, next={repr(self.next)}, action={repr(self.action)}, binding={repr(self.binding)}, on_threshold={repr(self.on_threshold)}, off_threshold={repr(self.off_threshold)}, on_haptic={repr(self.on_haptic)}, off_haptic={repr(self.off_haptic)})"

    def __str__(self) -> str:
        return f"xr.InteractionProfileAnalogThresholdVALVE(type={str(self.type)}, next={str(self.next)}, action={str(self.action)}, binding={str(self.binding)}, on_threshold={str(self.on_threshold)}, off_threshold={str(self.off_threshold)}, on_haptic={str(self.on_haptic)}, off_haptic={str(self.off_haptic)})"

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
    def __init__(
        self,
        hand_joints_motion_range: HandJointsMotionRangeEXT = HandJointsMotionRangeEXT(1),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.HAND_JOINTS_MOTION_RANGE_INFO_EXT,
    ) -> None:
        super().__init__(
            hand_joints_motion_range=hand_joints_motion_range.value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.HandJointsMotionRangeInfoEXT(type={repr(self.type)}, next={repr(self.next)}, hand_joints_motion_range={repr(self.hand_joints_motion_range)})"

    def __str__(self) -> str:
        return f"xr.HandJointsMotionRangeInfoEXT(type={str(self.type)}, next={str(self.next)}, hand_joints_motion_range={str(self.hand_joints_motion_range)})"

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
    def __init__(
        self,
    ) -> None:
        super().__init__(
        )

    def __repr__(self) -> str:
        return f"xr.UuidMSFT(bytes={repr(self.bytes)})"

    def __str__(self) -> str:
        return f"xr.UuidMSFT(bytes={str(self.bytes)})"

    _fields_ = [
        ("bytes", (c_uint8 * 16)),
    ]


class SceneObserverCreateInfoMSFT(Structure):
    def __init__(
        self,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SCENE_OBSERVER_CREATE_INFO_MSFT,
    ) -> None:
        super().__init__(
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SceneObserverCreateInfoMSFT(type={repr(self.type)}, next={repr(self.next)})"

    def __str__(self) -> str:
        return f"xr.SceneObserverCreateInfoMSFT(type={str(self.type)}, next={str(self.next)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SceneCreateInfoMSFT(Structure):
    def __init__(
        self,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SCENE_CREATE_INFO_MSFT,
    ) -> None:
        super().__init__(
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SceneCreateInfoMSFT(type={repr(self.type)}, next={repr(self.next)})"

    def __str__(self) -> str:
        return f"xr.SceneCreateInfoMSFT(type={str(self.type)}, next={str(self.next)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SceneSphereBoundMSFT(Structure):
    def __init__(
        self,
        center: Vector3f = None,
        radius: float = 0,
    ) -> None:
        if center is None:
            center = Vector3f()
        super().__init__(
            center=center,
            radius=radius,
        )

    def __repr__(self) -> str:
        return f"xr.SceneSphereBoundMSFT(center={repr(self.center)}, radius={repr(self.radius)})"

    def __str__(self) -> str:
        return f"xr.SceneSphereBoundMSFT(center={str(self.center)}, radius={str(self.radius)})"

    _fields_ = [
        ("center", Vector3f),
        ("radius", c_float),
    ]


class SceneOrientedBoxBoundMSFT(Structure):
    def __init__(
        self,
        pose: Posef = None,
        extents: Vector3f = None,
    ) -> None:
        if pose is None:
            pose = Posef()
        if extents is None:
            extents = Vector3f()
        super().__init__(
            pose=pose,
            extents=extents,
        )

    def __repr__(self) -> str:
        return f"xr.SceneOrientedBoxBoundMSFT(pose={repr(self.pose)}, extents={repr(self.extents)})"

    def __str__(self) -> str:
        return f"xr.SceneOrientedBoxBoundMSFT(pose={str(self.pose)}, extents={str(self.extents)})"

    _fields_ = [
        ("pose", Posef),
        ("extents", Vector3f),
    ]


class SceneFrustumBoundMSFT(Structure):
    def __init__(
        self,
        pose: Posef = None,
        fov: Fovf = None,
        far_distance: float = 0,
    ) -> None:
        if pose is None:
            pose = Posef()
        if fov is None:
            fov = Fovf()
        super().__init__(
            pose=pose,
            fov=fov,
            far_distance=far_distance,
        )

    def __repr__(self) -> str:
        return f"xr.SceneFrustumBoundMSFT(pose={repr(self.pose)}, fov={repr(self.fov)}, far_distance={repr(self.far_distance)})"

    def __str__(self) -> str:
        return f"xr.SceneFrustumBoundMSFT(pose={str(self.pose)}, fov={str(self.fov)}, far_distance={str(self.far_distance)})"

    _fields_ = [
        ("pose", Posef),
        ("fov", Fovf),
        ("far_distance", c_float),
    ]


class SceneBoundsMSFT(Structure):
    def __init__(
        self,
        space: SpaceHandle = None,
        time: Time = 0,
        sphere_count: int = 0,
        spheres: POINTER(SceneSphereBoundMSFT) = None,
        box_count: int = 0,
        boxes: POINTER(SceneOrientedBoxBoundMSFT) = None,
        frustum_count: int = 0,
        frustums: POINTER(SceneFrustumBoundMSFT) = None,
    ) -> None:
        super().__init__(
            space=space,
            time=time,
            sphere_count=sphere_count,
            spheres=spheres,
            box_count=box_count,
            boxes=boxes,
            frustum_count=frustum_count,
            frustums=frustums,
        )

    def __repr__(self) -> str:
        return f"xr.SceneBoundsMSFT(space={repr(self.space)}, time={repr(self.time)}, sphere_count={repr(self.sphere_count)}, spheres={repr(self.spheres)}, box_count={repr(self.box_count)}, boxes={repr(self.boxes)}, frustum_count={repr(self.frustum_count)}, frustums={repr(self.frustums)})"

    def __str__(self) -> str:
        return f"xr.SceneBoundsMSFT(space={str(self.space)}, time={str(self.time)}, sphere_count={str(self.sphere_count)}, spheres={str(self.spheres)}, box_count={str(self.box_count)}, boxes={str(self.boxes)}, frustum_count={str(self.frustum_count)}, frustums={str(self.frustums)})"

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
    def __init__(
        self,
        requested_feature_count: int = 0,
        requested_features: POINTER(c_int) = None,
        consistency: SceneComputeConsistencyMSFT = SceneComputeConsistencyMSFT(1),
        bounds: SceneBoundsMSFT = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.NEW_SCENE_COMPUTE_INFO_MSFT,
    ) -> None:
        if bounds is None:
            bounds = SceneBoundsMSFT()
        super().__init__(
            requested_feature_count=requested_feature_count,
            requested_features=requested_features,
            consistency=consistency.value,
            bounds=bounds,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.NewSceneComputeInfoMSFT(type={repr(self.type)}, next={repr(self.next)}, requested_feature_count={repr(self.requested_feature_count)}, requested_features={repr(self.requested_features)}, consistency={repr(self.consistency)}, bounds={repr(self.bounds)})"

    def __str__(self) -> str:
        return f"xr.NewSceneComputeInfoMSFT(type={str(self.type)}, next={str(self.next)}, requested_feature_count={str(self.requested_feature_count)}, requested_features={str(self.requested_features)}, consistency={str(self.consistency)}, bounds={str(self.bounds)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("requested_feature_count", c_uint32),
        ("requested_features", POINTER(c_int)),
        ("consistency", SceneComputeConsistencyMSFT.ctype()),
        ("bounds", SceneBoundsMSFT),
    ]


class VisualMeshComputeLodInfoMSFT(Structure):
    def __init__(
        self,
        lod: MeshComputeLodMSFT = MeshComputeLodMSFT(1),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.VISUAL_MESH_COMPUTE_LOD_INFO_MSFT,
    ) -> None:
        super().__init__(
            lod=lod.value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.VisualMeshComputeLodInfoMSFT(type={repr(self.type)}, next={repr(self.next)}, lod={repr(self.lod)})"

    def __str__(self) -> str:
        return f"xr.VisualMeshComputeLodInfoMSFT(type={str(self.type)}, next={str(self.next)}, lod={str(self.lod)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("lod", MeshComputeLodMSFT.ctype()),
    ]


class SceneComponentMSFT(Structure):
    def __init__(
        self,
        component_type: SceneComponentTypeMSFT = SceneComponentTypeMSFT(1),
        id: UuidMSFT = None,
        parent_id: UuidMSFT = None,
        update_time: Time = 0,
    ) -> None:
        if id is None:
            id = UuidMSFT()
        if parent_id is None:
            parent_id = UuidMSFT()
        super().__init__(
            component_type=component_type.value,
            id=id,
            parent_id=parent_id,
            update_time=update_time,
        )

    def __repr__(self) -> str:
        return f"xr.SceneComponentMSFT(component_type={repr(self.component_type)}, id={repr(self.id)}, parent_id={repr(self.parent_id)}, update_time={repr(self.update_time)})"

    def __str__(self) -> str:
        return f"xr.SceneComponentMSFT(component_type={str(self.component_type)}, id={str(self.id)}, parent_id={str(self.parent_id)}, update_time={str(self.update_time)})"

    _fields_ = [
        ("component_type", SceneComponentTypeMSFT.ctype()),
        ("id", UuidMSFT),
        ("parent_id", UuidMSFT),
        ("update_time", Time),
    ]


class SceneComponentsMSFT(Structure):
    def __init__(
        self,
        component_capacity_input: int = 0,
        component_count_output: int = 0,
        components: POINTER(SceneComponentMSFT) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SCENE_COMPONENTS_MSFT,
    ) -> None:
        super().__init__(
            component_capacity_input=component_capacity_input,
            component_count_output=component_count_output,
            components=components,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SceneComponentsMSFT(type={repr(self.type)}, next={repr(self.next)}, component_capacity_input={repr(self.component_capacity_input)}, component_count_output={repr(self.component_count_output)}, components={repr(self.components)})"

    def __str__(self) -> str:
        return f"xr.SceneComponentsMSFT(type={str(self.type)}, next={str(self.next)}, component_capacity_input={str(self.component_capacity_input)}, component_count_output={str(self.component_count_output)}, components={str(self.components)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("component_capacity_input", c_uint32),
        ("component_count_output", c_uint32),
        ("components", POINTER(SceneComponentMSFT)),
    ]


class SceneComponentsGetInfoMSFT(Structure):
    def __init__(
        self,
        component_type: SceneComponentTypeMSFT = SceneComponentTypeMSFT(1),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SCENE_COMPONENTS_GET_INFO_MSFT,
    ) -> None:
        super().__init__(
            component_type=component_type.value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SceneComponentsGetInfoMSFT(type={repr(self.type)}, next={repr(self.next)}, component_type={repr(self.component_type)})"

    def __str__(self) -> str:
        return f"xr.SceneComponentsGetInfoMSFT(type={str(self.type)}, next={str(self.next)}, component_type={str(self.component_type)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("component_type", SceneComponentTypeMSFT.ctype()),
    ]


class SceneComponentLocationMSFT(Structure):
    def __init__(
        self,
        flags: SpaceLocationFlags = 0,
        pose: Posef = None,
    ) -> None:
        if pose is None:
            pose = Posef()
        super().__init__(
            flags=flags,
            pose=pose,
        )

    def __repr__(self) -> str:
        return f"xr.SceneComponentLocationMSFT(flags={repr(self.flags)}, pose={repr(self.pose)})"

    def __str__(self) -> str:
        return f"xr.SceneComponentLocationMSFT(flags={str(self.flags)}, pose={str(self.pose)})"

    _fields_ = [
        ("flags", SpaceLocationFlags),
        ("pose", Posef),
    ]


class SceneComponentLocationsMSFT(Structure):
    def __init__(
        self,
        location_count: int = 0,
        locations: POINTER(SceneComponentLocationMSFT) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SCENE_COMPONENT_LOCATIONS_MSFT,
    ) -> None:
        super().__init__(
            location_count=location_count,
            locations=locations,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SceneComponentLocationsMSFT(type={repr(self.type)}, next={repr(self.next)}, location_count={repr(self.location_count)}, locations={repr(self.locations)})"

    def __str__(self) -> str:
        return f"xr.SceneComponentLocationsMSFT(type={str(self.type)}, next={str(self.next)}, location_count={str(self.location_count)}, locations={str(self.locations)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("location_count", c_uint32),
        ("locations", POINTER(SceneComponentLocationMSFT)),
    ]


class SceneComponentsLocateInfoMSFT(Structure):
    def __init__(
        self,
        base_space: SpaceHandle = None,
        time: Time = 0,
        component_id_count: int = 0,
        component_ids: POINTER(UuidMSFT) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SCENE_COMPONENTS_LOCATE_INFO_MSFT,
    ) -> None:
        super().__init__(
            base_space=base_space,
            time=time,
            component_id_count=component_id_count,
            component_ids=component_ids,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SceneComponentsLocateInfoMSFT(type={repr(self.type)}, next={repr(self.next)}, base_space={repr(self.base_space)}, time={repr(self.time)}, component_id_count={repr(self.component_id_count)}, component_ids={repr(self.component_ids)})"

    def __str__(self) -> str:
        return f"xr.SceneComponentsLocateInfoMSFT(type={str(self.type)}, next={str(self.next)}, base_space={str(self.base_space)}, time={str(self.time)}, component_id_count={str(self.component_id_count)}, component_ids={str(self.component_ids)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("base_space", SpaceHandle),
        ("time", Time),
        ("component_id_count", c_uint32),
        ("component_ids", POINTER(UuidMSFT)),
    ]


class SceneObjectMSFT(Structure):
    def __init__(
        self,
        object_type: SceneObjectTypeMSFT = SceneObjectTypeMSFT(1),
    ) -> None:
        super().__init__(
            object_type=object_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SceneObjectMSFT(object_type={repr(self.object_type)})"

    def __str__(self) -> str:
        return f"xr.SceneObjectMSFT(object_type={str(self.object_type)})"

    _fields_ = [
        ("object_type", SceneObjectTypeMSFT.ctype()),
    ]


class SceneObjectsMSFT(Structure):
    def __init__(
        self,
        scene_object_count: int = 0,
        scene_objects: POINTER(SceneObjectMSFT) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SCENE_OBJECTS_MSFT,
    ) -> None:
        super().__init__(
            scene_object_count=scene_object_count,
            scene_objects=scene_objects,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SceneObjectsMSFT(type={repr(self.type)}, next={repr(self.next)}, scene_object_count={repr(self.scene_object_count)}, scene_objects={repr(self.scene_objects)})"

    def __str__(self) -> str:
        return f"xr.SceneObjectsMSFT(type={str(self.type)}, next={str(self.next)}, scene_object_count={str(self.scene_object_count)}, scene_objects={str(self.scene_objects)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("scene_object_count", c_uint32),
        ("scene_objects", POINTER(SceneObjectMSFT)),
    ]


class SceneComponentParentFilterInfoMSFT(Structure):
    def __init__(
        self,
        parent_id: UuidMSFT = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SCENE_COMPONENT_PARENT_FILTER_INFO_MSFT,
    ) -> None:
        if parent_id is None:
            parent_id = UuidMSFT()
        super().__init__(
            parent_id=parent_id,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SceneComponentParentFilterInfoMSFT(type={repr(self.type)}, next={repr(self.next)}, parent_id={repr(self.parent_id)})"

    def __str__(self) -> str:
        return f"xr.SceneComponentParentFilterInfoMSFT(type={str(self.type)}, next={str(self.next)}, parent_id={str(self.parent_id)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("parent_id", UuidMSFT),
    ]


class SceneObjectTypesFilterInfoMSFT(Structure):
    def __init__(
        self,
        object_type_count: int = 0,
        object_types: POINTER(c_int) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SCENE_OBJECT_TYPES_FILTER_INFO_MSFT,
    ) -> None:
        super().__init__(
            object_type_count=object_type_count,
            object_types=object_types,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SceneObjectTypesFilterInfoMSFT(type={repr(self.type)}, next={repr(self.next)}, object_type_count={repr(self.object_type_count)}, object_types={repr(self.object_types)})"

    def __str__(self) -> str:
        return f"xr.SceneObjectTypesFilterInfoMSFT(type={str(self.type)}, next={str(self.next)}, object_type_count={str(self.object_type_count)}, object_types={str(self.object_types)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("object_type_count", c_uint32),
        ("object_types", POINTER(c_int)),
    ]


class ScenePlaneMSFT(Structure):
    def __init__(
        self,
        alignment: ScenePlaneAlignmentTypeMSFT = ScenePlaneAlignmentTypeMSFT(1),
        size: Extent2Df = None,
        mesh_buffer_id: int = 0,
        supports_indices_uint16: Bool32 = 0,
    ) -> None:
        if size is None:
            size = Extent2Df()
        super().__init__(
            alignment=alignment.value,
            size=size,
            mesh_buffer_id=mesh_buffer_id,
            supports_indices_uint16=supports_indices_uint16,
        )

    def __repr__(self) -> str:
        return f"xr.ScenePlaneMSFT(alignment={repr(self.alignment)}, size={repr(self.size)}, mesh_buffer_id={repr(self.mesh_buffer_id)}, supports_indices_uint16={repr(self.supports_indices_uint16)})"

    def __str__(self) -> str:
        return f"xr.ScenePlaneMSFT(alignment={str(self.alignment)}, size={str(self.size)}, mesh_buffer_id={str(self.mesh_buffer_id)}, supports_indices_uint16={str(self.supports_indices_uint16)})"

    _fields_ = [
        ("alignment", ScenePlaneAlignmentTypeMSFT.ctype()),
        ("size", Extent2Df),
        ("mesh_buffer_id", c_uint64),
        ("supports_indices_uint16", Bool32),
    ]


class ScenePlanesMSFT(Structure):
    def __init__(
        self,
        scene_plane_count: int = 0,
        scene_planes: POINTER(ScenePlaneMSFT) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SCENE_PLANES_MSFT,
    ) -> None:
        super().__init__(
            scene_plane_count=scene_plane_count,
            scene_planes=scene_planes,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ScenePlanesMSFT(type={repr(self.type)}, next={repr(self.next)}, scene_plane_count={repr(self.scene_plane_count)}, scene_planes={repr(self.scene_planes)})"

    def __str__(self) -> str:
        return f"xr.ScenePlanesMSFT(type={str(self.type)}, next={str(self.next)}, scene_plane_count={str(self.scene_plane_count)}, scene_planes={str(self.scene_planes)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("scene_plane_count", c_uint32),
        ("scene_planes", POINTER(ScenePlaneMSFT)),
    ]


class ScenePlaneAlignmentFilterInfoMSFT(Structure):
    def __init__(
        self,
        alignment_count: int = 0,
        alignments: POINTER(c_int) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SCENE_PLANE_ALIGNMENT_FILTER_INFO_MSFT,
    ) -> None:
        super().__init__(
            alignment_count=alignment_count,
            alignments=alignments,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ScenePlaneAlignmentFilterInfoMSFT(type={repr(self.type)}, next={repr(self.next)}, alignment_count={repr(self.alignment_count)}, alignments={repr(self.alignments)})"

    def __str__(self) -> str:
        return f"xr.ScenePlaneAlignmentFilterInfoMSFT(type={str(self.type)}, next={str(self.next)}, alignment_count={str(self.alignment_count)}, alignments={str(self.alignments)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("alignment_count", c_uint32),
        ("alignments", POINTER(c_int)),
    ]


class SceneMeshMSFT(Structure):
    def __init__(
        self,
        mesh_buffer_id: int = 0,
        supports_indices_uint16: Bool32 = 0,
    ) -> None:
        super().__init__(
            mesh_buffer_id=mesh_buffer_id,
            supports_indices_uint16=supports_indices_uint16,
        )

    def __repr__(self) -> str:
        return f"xr.SceneMeshMSFT(mesh_buffer_id={repr(self.mesh_buffer_id)}, supports_indices_uint16={repr(self.supports_indices_uint16)})"

    def __str__(self) -> str:
        return f"xr.SceneMeshMSFT(mesh_buffer_id={str(self.mesh_buffer_id)}, supports_indices_uint16={str(self.supports_indices_uint16)})"

    _fields_ = [
        ("mesh_buffer_id", c_uint64),
        ("supports_indices_uint16", Bool32),
    ]


class SceneMeshesMSFT(Structure):
    def __init__(
        self,
        scene_mesh_count: int = 0,
        scene_meshes: POINTER(SceneMeshMSFT) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SCENE_MESHES_MSFT,
    ) -> None:
        super().__init__(
            scene_mesh_count=scene_mesh_count,
            scene_meshes=scene_meshes,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SceneMeshesMSFT(type={repr(self.type)}, next={repr(self.next)}, scene_mesh_count={repr(self.scene_mesh_count)}, scene_meshes={repr(self.scene_meshes)})"

    def __str__(self) -> str:
        return f"xr.SceneMeshesMSFT(type={str(self.type)}, next={str(self.next)}, scene_mesh_count={str(self.scene_mesh_count)}, scene_meshes={str(self.scene_meshes)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("scene_mesh_count", c_uint32),
        ("scene_meshes", POINTER(SceneMeshMSFT)),
    ]


class SceneMeshBuffersGetInfoMSFT(Structure):
    def __init__(
        self,
        mesh_buffer_id: int = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SCENE_MESH_BUFFERS_GET_INFO_MSFT,
    ) -> None:
        super().__init__(
            mesh_buffer_id=mesh_buffer_id,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SceneMeshBuffersGetInfoMSFT(type={repr(self.type)}, next={repr(self.next)}, mesh_buffer_id={repr(self.mesh_buffer_id)})"

    def __str__(self) -> str:
        return f"xr.SceneMeshBuffersGetInfoMSFT(type={str(self.type)}, next={str(self.next)}, mesh_buffer_id={str(self.mesh_buffer_id)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("mesh_buffer_id", c_uint64),
    ]


class SceneMeshBuffersMSFT(Structure):
    def __init__(
        self,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SCENE_MESH_BUFFERS_MSFT,
    ) -> None:
        super().__init__(
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SceneMeshBuffersMSFT(type={repr(self.type)}, next={repr(self.next)})"

    def __str__(self) -> str:
        return f"xr.SceneMeshBuffersMSFT(type={str(self.type)}, next={str(self.next)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SceneMeshVertexBufferMSFT(Structure):
    def __init__(
        self,
        vertex_capacity_input: int = 0,
        vertex_count_output: int = 0,
        vertices: POINTER(Vector3f) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SCENE_MESH_VERTEX_BUFFER_MSFT,
    ) -> None:
        super().__init__(
            vertex_capacity_input=vertex_capacity_input,
            vertex_count_output=vertex_count_output,
            vertices=vertices,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SceneMeshVertexBufferMSFT(type={repr(self.type)}, next={repr(self.next)}, vertex_capacity_input={repr(self.vertex_capacity_input)}, vertex_count_output={repr(self.vertex_count_output)}, vertices={repr(self.vertices)})"

    def __str__(self) -> str:
        return f"xr.SceneMeshVertexBufferMSFT(type={str(self.type)}, next={str(self.next)}, vertex_capacity_input={str(self.vertex_capacity_input)}, vertex_count_output={str(self.vertex_count_output)}, vertices={str(self.vertices)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("vertex_capacity_input", c_uint32),
        ("vertex_count_output", c_uint32),
        ("vertices", POINTER(Vector3f)),
    ]


class SceneMeshIndicesUint32MSFT(Structure):
    def __init__(
        self,
        index_capacity_input: int = 0,
        index_count_output: int = 0,
        indices: POINTER(c_uint32) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SCENE_MESH_INDICES_UINT32_MSFT,
    ) -> None:
        super().__init__(
            index_capacity_input=index_capacity_input,
            index_count_output=index_count_output,
            indices=indices,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SceneMeshIndicesUint32MSFT(type={repr(self.type)}, next={repr(self.next)}, index_capacity_input={repr(self.index_capacity_input)}, index_count_output={repr(self.index_count_output)}, indices={repr(self.indices)})"

    def __str__(self) -> str:
        return f"xr.SceneMeshIndicesUint32MSFT(type={str(self.type)}, next={str(self.next)}, index_capacity_input={str(self.index_capacity_input)}, index_count_output={str(self.index_count_output)}, indices={str(self.indices)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("index_capacity_input", c_uint32),
        ("index_count_output", c_uint32),
        ("indices", POINTER(c_uint32)),
    ]


class SceneMeshIndicesUint16MSFT(Structure):
    def __init__(
        self,
        index_capacity_input: int = 0,
        index_count_output: int = 0,
        indices: POINTER(c_uint16) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SCENE_MESH_INDICES_UINT16_MSFT,
    ) -> None:
        super().__init__(
            index_capacity_input=index_capacity_input,
            index_count_output=index_count_output,
            indices=indices,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SceneMeshIndicesUint16MSFT(type={repr(self.type)}, next={repr(self.next)}, index_capacity_input={repr(self.index_capacity_input)}, index_count_output={repr(self.index_count_output)}, indices={repr(self.indices)})"

    def __str__(self) -> str:
        return f"xr.SceneMeshIndicesUint16MSFT(type={str(self.type)}, next={str(self.next)}, index_capacity_input={str(self.index_capacity_input)}, index_count_output={str(self.index_count_output)}, indices={str(self.indices)})"

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
    def __init__(
        self,
        scene_fragment_id: UuidMSFT = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SERIALIZED_SCENE_FRAGMENT_DATA_GET_INFO_MSFT,
    ) -> None:
        if scene_fragment_id is None:
            scene_fragment_id = UuidMSFT()
        super().__init__(
            scene_fragment_id=scene_fragment_id,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SerializedSceneFragmentDataGetInfoMSFT(type={repr(self.type)}, next={repr(self.next)}, scene_fragment_id={repr(self.scene_fragment_id)})"

    def __str__(self) -> str:
        return f"xr.SerializedSceneFragmentDataGetInfoMSFT(type={str(self.type)}, next={str(self.next)}, scene_fragment_id={str(self.scene_fragment_id)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("scene_fragment_id", UuidMSFT),
    ]


class DeserializeSceneFragmentMSFT(Structure):
    def __init__(
        self,
        buffer_size: int = 0,
        buffer: POINTER(c_uint8) = None,
    ) -> None:
        super().__init__(
            buffer_size=buffer_size,
            buffer=buffer,
        )

    def __repr__(self) -> str:
        return f"xr.DeserializeSceneFragmentMSFT(buffer_size={repr(self.buffer_size)}, buffer={repr(self.buffer)})"

    def __str__(self) -> str:
        return f"xr.DeserializeSceneFragmentMSFT(buffer_size={str(self.buffer_size)}, buffer={str(self.buffer)})"

    _fields_ = [
        ("buffer_size", c_uint32),
        ("buffer", POINTER(c_uint8)),
    ]


class SceneDeserializeInfoMSFT(Structure):
    def __init__(
        self,
        fragment_count: int = 0,
        fragments: POINTER(DeserializeSceneFragmentMSFT) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SCENE_DESERIALIZE_INFO_MSFT,
    ) -> None:
        super().__init__(
            fragment_count=fragment_count,
            fragments=fragments,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SceneDeserializeInfoMSFT(type={repr(self.type)}, next={repr(self.next)}, fragment_count={repr(self.fragment_count)}, fragments={repr(self.fragments)})"

    def __str__(self) -> str:
        return f"xr.SceneDeserializeInfoMSFT(type={str(self.type)}, next={str(self.next)}, fragment_count={str(self.fragment_count)}, fragments={str(self.fragments)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("fragment_count", c_uint32),
        ("fragments", POINTER(DeserializeSceneFragmentMSFT)),
    ]


PFN_xrDeserializeSceneMSFT = CFUNCTYPE(Result.ctype(), SceneObserverMSFTHandle, POINTER(SceneDeserializeInfoMSFT))

PFN_xrGetSerializedSceneFragmentDataMSFT = CFUNCTYPE(Result.ctype(), SceneMSFTHandle, POINTER(SerializedSceneFragmentDataGetInfoMSFT), c_uint32, POINTER(c_uint32), POINTER(c_uint8))


class EventDataDisplayRefreshRateChangedFB(Structure):
    def __init__(
        self,
        from_display_refresh_rate: float = 0,
        to_display_refresh_rate: float = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.EVENT_DATA_DISPLAY_REFRESH_RATE_CHANGED_FB,
    ) -> None:
        super().__init__(
            from_display_refresh_rate=from_display_refresh_rate,
            to_display_refresh_rate=to_display_refresh_rate,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataDisplayRefreshRateChangedFB(type={repr(self.type)}, next={repr(self.next)}, from_display_refresh_rate={repr(self.from_display_refresh_rate)}, to_display_refresh_rate={repr(self.to_display_refresh_rate)})"

    def __str__(self) -> str:
        return f"xr.EventDataDisplayRefreshRateChangedFB(type={str(self.type)}, next={str(self.next)}, from_display_refresh_rate={str(self.from_display_refresh_rate)}, to_display_refresh_rate={str(self.to_display_refresh_rate)})"

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
    def __init__(
        self,
        color_space: ColorSpaceFB = ColorSpaceFB(1),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SYSTEM_COLOR_SPACE_PROPERTIES_FB,
    ) -> None:
        super().__init__(
            color_space=color_space.value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SystemColorSpacePropertiesFB(type={repr(self.type)}, next={repr(self.next)}, color_space={repr(self.color_space)})"

    def __str__(self) -> str:
        return f"xr.SystemColorSpacePropertiesFB(type={str(self.type)}, next={str(self.next)}, color_space={str(self.color_space)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("color_space", ColorSpaceFB.ctype()),
    ]


PFN_xrEnumerateColorSpacesFB = CFUNCTYPE(Result.ctype(), SessionHandle, c_uint32, POINTER(c_uint32), POINTER(ColorSpaceFB.ctype()))

PFN_xrSetColorSpaceFB = CFUNCTYPE(Result.ctype(), SessionHandle, c_int)


class Vector4sFB(Structure):
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        z: int = 0,
        w: int = 0,
    ) -> None:
        super().__init__(
            x=x,
            y=y,
            z=z,
            w=w,
        )

    def __repr__(self) -> str:
        return f"xr.Vector4sFB(x={repr(self.x)}, y={repr(self.y)}, z={repr(self.z)}, w={repr(self.w)})"

    def __str__(self) -> str:
        return f"xr.Vector4sFB(x={str(self.x)}, y={str(self.y)}, z={str(self.z)}, w={str(self.w)})"

    _fields_ = [
        ("x", c_int16),
        ("y", c_int16),
        ("z", c_int16),
        ("w", c_int16),
    ]


class HandTrackingMeshFB(Structure):
    def __init__(
        self,
        joint_capacity_input: int = 0,
        joint_count_output: int = 0,
        joint_bind_poses: POINTER(Posef) = None,
        joint_radii: POINTER(c_float) = None,
        joint_parents: POINTER(HandJointEXT.ctype()) = None,
        vertex_capacity_input: int = 0,
        vertex_count_output: int = 0,
        vertex_positions: POINTER(Vector3f) = None,
        vertex_normals: POINTER(Vector3f) = None,
        vertex_uvs: POINTER(Vector2f) = None,
        vertex_blend_indices: POINTER(Vector4sFB) = None,
        vertex_blend_weights: POINTER(Vector4f) = None,
        index_capacity_input: int = 0,
        index_count_output: int = 0,
        indices: POINTER(c_int16) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.HAND_TRACKING_MESH_FB,
    ) -> None:
        super().__init__(
            joint_capacity_input=joint_capacity_input,
            joint_count_output=joint_count_output,
            joint_bind_poses=joint_bind_poses,
            joint_radii=joint_radii,
            joint_parents=joint_parents,
            vertex_capacity_input=vertex_capacity_input,
            vertex_count_output=vertex_count_output,
            vertex_positions=vertex_positions,
            vertex_normals=vertex_normals,
            vertex_uvs=vertex_uvs,
            vertex_blend_indices=vertex_blend_indices,
            vertex_blend_weights=vertex_blend_weights,
            index_capacity_input=index_capacity_input,
            index_count_output=index_count_output,
            indices=indices,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.HandTrackingMeshFB(type={repr(self.type)}, next={repr(self.next)}, joint_capacity_input={repr(self.joint_capacity_input)}, joint_count_output={repr(self.joint_count_output)}, joint_bind_poses={repr(self.joint_bind_poses)}, joint_radii={repr(self.joint_radii)}, joint_parents={repr(self.joint_parents)}, vertex_capacity_input={repr(self.vertex_capacity_input)}, vertex_count_output={repr(self.vertex_count_output)}, vertex_positions={repr(self.vertex_positions)}, vertex_normals={repr(self.vertex_normals)}, vertex_uvs={repr(self.vertex_uvs)}, vertex_blend_indices={repr(self.vertex_blend_indices)}, vertex_blend_weights={repr(self.vertex_blend_weights)}, index_capacity_input={repr(self.index_capacity_input)}, index_count_output={repr(self.index_count_output)}, indices={repr(self.indices)})"

    def __str__(self) -> str:
        return f"xr.HandTrackingMeshFB(type={str(self.type)}, next={str(self.next)}, joint_capacity_input={str(self.joint_capacity_input)}, joint_count_output={str(self.joint_count_output)}, joint_bind_poses={str(self.joint_bind_poses)}, joint_radii={str(self.joint_radii)}, joint_parents={str(self.joint_parents)}, vertex_capacity_input={str(self.vertex_capacity_input)}, vertex_count_output={str(self.vertex_count_output)}, vertex_positions={str(self.vertex_positions)}, vertex_normals={str(self.vertex_normals)}, vertex_uvs={str(self.vertex_uvs)}, vertex_blend_indices={str(self.vertex_blend_indices)}, vertex_blend_weights={str(self.vertex_blend_weights)}, index_capacity_input={str(self.index_capacity_input)}, index_count_output={str(self.index_count_output)}, indices={str(self.indices)})"

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
    def __init__(
        self,
        sensor_output: float = 0,
        current_output: float = 0,
        override_hand_scale: Bool32 = 0,
        override_value_input: float = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.HAND_TRACKING_SCALE_FB,
    ) -> None:
        super().__init__(
            sensor_output=sensor_output,
            current_output=current_output,
            override_hand_scale=override_hand_scale,
            override_value_input=override_value_input,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.HandTrackingScaleFB(type={repr(self.type)}, next={repr(self.next)}, sensor_output={repr(self.sensor_output)}, current_output={repr(self.current_output)}, override_hand_scale={repr(self.override_hand_scale)}, override_value_input={repr(self.override_value_input)})"

    def __str__(self) -> str:
        return f"xr.HandTrackingScaleFB(type={str(self.type)}, next={str(self.next)}, sensor_output={str(self.sensor_output)}, current_output={str(self.current_output)}, override_hand_scale={str(self.override_hand_scale)}, override_value_input={str(self.override_value_input)})"

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
    def __init__(
        self,
        status: HandTrackingAimFlagsFB = 0,
        aim_pose: Posef = None,
        pinch_strength_index: float = 0,
        pinch_strength_middle: float = 0,
        pinch_strength_ring: float = 0,
        pinch_strength_little: float = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.HAND_TRACKING_AIM_STATE_FB,
    ) -> None:
        if aim_pose is None:
            aim_pose = Posef()
        super().__init__(
            status=status,
            aim_pose=aim_pose,
            pinch_strength_index=pinch_strength_index,
            pinch_strength_middle=pinch_strength_middle,
            pinch_strength_ring=pinch_strength_ring,
            pinch_strength_little=pinch_strength_little,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.HandTrackingAimStateFB(type={repr(self.type)}, next={repr(self.next)}, status={repr(self.status)}, aim_pose={repr(self.aim_pose)}, pinch_strength_index={repr(self.pinch_strength_index)}, pinch_strength_middle={repr(self.pinch_strength_middle)}, pinch_strength_ring={repr(self.pinch_strength_ring)}, pinch_strength_little={repr(self.pinch_strength_little)})"

    def __str__(self) -> str:
        return f"xr.HandTrackingAimStateFB(type={str(self.type)}, next={str(self.next)}, status={str(self.status)}, aim_pose={str(self.aim_pose)}, pinch_strength_index={str(self.pinch_strength_index)}, pinch_strength_middle={str(self.pinch_strength_middle)}, pinch_strength_ring={str(self.pinch_strength_ring)}, pinch_strength_little={str(self.pinch_strength_little)})"

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
    def __init__(
        self,
        radius: float = 0,
        joint: HandJointEXT = HandJointEXT(1),
    ) -> None:
        super().__init__(
            radius=radius,
            joint=joint.value,
        )

    def __repr__(self) -> str:
        return f"xr.HandCapsuleFB(points={repr(self.points)}, radius={repr(self.radius)}, joint={repr(self.joint)})"

    def __str__(self) -> str:
        return f"xr.HandCapsuleFB(points={str(self.points)}, radius={str(self.radius)}, joint={str(self.joint)})"

    _fields_ = [
        ("points", (Vector3f * 2)),
        ("radius", c_float),
        ("joint", HandJointEXT.ctype()),
    ]


class HandTrackingCapsulesStateFB(Structure):
    def __init__(
        self,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.HAND_TRACKING_CAPSULES_STATE_FB,
    ) -> None:
        super().__init__(
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.HandTrackingCapsulesStateFB(type={repr(self.type)}, next={repr(self.next)}, capsules={repr(self.capsules)})"

    def __str__(self) -> str:
        return f"xr.HandTrackingCapsulesStateFB(type={str(self.type)}, next={str(self.next)}, capsules={str(self.capsules)})"

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
    def __init__(
        self,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.FOVEATION_PROFILE_CREATE_INFO_FB,
    ) -> None:
        super().__init__(
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.FoveationProfileCreateInfoFB(type={repr(self.type)}, next={repr(self.next)})"

    def __str__(self) -> str:
        return f"xr.FoveationProfileCreateInfoFB(type={str(self.type)}, next={str(self.next)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SwapchainCreateInfoFoveationFB(Structure):
    def __init__(
        self,
        flags: SwapchainCreateFoveationFlagsFB = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SWAPCHAIN_CREATE_INFO_FOVEATION_FB,
    ) -> None:
        super().__init__(
            flags=flags,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainCreateInfoFoveationFB(type={repr(self.type)}, next={repr(self.next)}, flags={repr(self.flags)})"

    def __str__(self) -> str:
        return f"xr.SwapchainCreateInfoFoveationFB(type={str(self.type)}, next={str(self.next)}, flags={str(self.flags)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", SwapchainCreateFoveationFlagsFB),
    ]


class SwapchainStateFoveationFB(Structure):
    def __init__(
        self,
        flags: SwapchainStateFoveationFlagsFB = 0,
        profile: FoveationProfileFBHandle = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SWAPCHAIN_STATE_FOVEATION_FB,
    ) -> None:
        super().__init__(
            flags=flags,
            profile=profile,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainStateFoveationFB(type={repr(self.type)}, next={repr(self.next)}, flags={repr(self.flags)}, profile={repr(self.profile)})"

    def __str__(self) -> str:
        return f"xr.SwapchainStateFoveationFB(type={str(self.type)}, next={str(self.next)}, flags={str(self.flags)}, profile={str(self.profile)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", SwapchainStateFoveationFlagsFB),
        ("profile", FoveationProfileFBHandle),
    ]


PFN_xrCreateFoveationProfileFB = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(FoveationProfileCreateInfoFB), POINTER(FoveationProfileFBHandle))

PFN_xrDestroyFoveationProfileFB = CFUNCTYPE(Result.ctype(), FoveationProfileFBHandle)


class FoveationLevelProfileCreateInfoFB(Structure):
    def __init__(
        self,
        level: FoveationLevelFB = FoveationLevelFB(1),
        vertical_offset: float = 0,
        dynamic: FoveationDynamicFB = FoveationDynamicFB(1),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.FOVEATION_LEVEL_PROFILE_CREATE_INFO_FB,
    ) -> None:
        super().__init__(
            level=level.value,
            vertical_offset=vertical_offset,
            dynamic=dynamic.value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.FoveationLevelProfileCreateInfoFB(type={repr(self.type)}, next={repr(self.next)}, level={repr(self.level)}, vertical_offset={repr(self.vertical_offset)}, dynamic={repr(self.dynamic)})"

    def __str__(self) -> str:
        return f"xr.FoveationLevelProfileCreateInfoFB(type={str(self.type)}, next={str(self.next)}, level={str(self.level)}, vertical_offset={str(self.vertical_offset)}, dynamic={str(self.dynamic)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("level", FoveationLevelFB.ctype()),
        ("vertical_offset", c_float),
        ("dynamic", FoveationDynamicFB.ctype()),
    ]


class ViewLocateFoveatedRenderingVARJO(Structure):
    def __init__(
        self,
        foveated_rendering_active: Bool32 = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.VIEW_LOCATE_FOVEATED_RENDERING_VARJO,
    ) -> None:
        super().__init__(
            foveated_rendering_active=foveated_rendering_active,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ViewLocateFoveatedRenderingVARJO(type={repr(self.type)}, next={repr(self.next)}, foveated_rendering_active={repr(self.foveated_rendering_active)})"

    def __str__(self) -> str:
        return f"xr.ViewLocateFoveatedRenderingVARJO(type={str(self.type)}, next={str(self.next)}, foveated_rendering_active={str(self.foveated_rendering_active)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("foveated_rendering_active", Bool32),
    ]


class FoveatedViewConfigurationViewVARJO(Structure):
    def __init__(
        self,
        foveated_rendering_active: Bool32 = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.FOVEATED_VIEW_CONFIGURATION_VIEW_VARJO,
    ) -> None:
        super().__init__(
            foveated_rendering_active=foveated_rendering_active,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.FoveatedViewConfigurationViewVARJO(type={repr(self.type)}, next={repr(self.next)}, foveated_rendering_active={repr(self.foveated_rendering_active)})"

    def __str__(self) -> str:
        return f"xr.FoveatedViewConfigurationViewVARJO(type={str(self.type)}, next={str(self.next)}, foveated_rendering_active={str(self.foveated_rendering_active)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("foveated_rendering_active", Bool32),
    ]


class SystemFoveatedRenderingPropertiesVARJO(Structure):
    def __init__(
        self,
        supports_foveated_rendering: Bool32 = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SYSTEM_FOVEATED_RENDERING_PROPERTIES_VARJO,
    ) -> None:
        super().__init__(
            supports_foveated_rendering=supports_foveated_rendering,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SystemFoveatedRenderingPropertiesVARJO(type={repr(self.type)}, next={repr(self.next)}, supports_foveated_rendering={repr(self.supports_foveated_rendering)})"

    def __str__(self) -> str:
        return f"xr.SystemFoveatedRenderingPropertiesVARJO(type={str(self.type)}, next={str(self.next)}, supports_foveated_rendering={str(self.supports_foveated_rendering)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_foveated_rendering", Bool32),
    ]


class CompositionLayerDepthTestVARJO(Structure):
    def __init__(
        self,
        depth_test_range_near_z: float = 0,
        depth_test_range_far_z: float = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.COMPOSITION_LAYER_DEPTH_TEST_VARJO,
    ) -> None:
        super().__init__(
            depth_test_range_near_z=depth_test_range_near_z,
            depth_test_range_far_z=depth_test_range_far_z,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerDepthTestVARJO(type={repr(self.type)}, next={repr(self.next)}, depth_test_range_near_z={repr(self.depth_test_range_near_z)}, depth_test_range_far_z={repr(self.depth_test_range_far_z)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerDepthTestVARJO(type={str(self.type)}, next={str(self.next)}, depth_test_range_near_z={str(self.depth_test_range_near_z)}, depth_test_range_far_z={str(self.depth_test_range_far_z)})"

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
    def __init__(
        self,
        name: str = "",
    ) -> None:
        super().__init__(
            name=name.encode(),
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorPersistenceNameMSFT(name={repr(self.name)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorPersistenceNameMSFT(name={str(self.name)})"

    _fields_ = [
        ("name", (c_char * 256)),
    ]


class SpatialAnchorPersistenceInfoMSFT(Structure):
    def __init__(
        self,
        spatial_anchor_persistence_name: SpatialAnchorPersistenceNameMSFT = None,
        spatial_anchor: SpatialAnchorMSFTHandle = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SPATIAL_ANCHOR_PERSISTENCE_INFO_MSFT,
    ) -> None:
        if spatial_anchor_persistence_name is None:
            spatial_anchor_persistence_name = SpatialAnchorPersistenceNameMSFT()
        super().__init__(
            spatial_anchor_persistence_name=spatial_anchor_persistence_name,
            spatial_anchor=spatial_anchor,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorPersistenceInfoMSFT(type={repr(self.type)}, next={repr(self.next)}, spatial_anchor_persistence_name={repr(self.spatial_anchor_persistence_name)}, spatial_anchor={repr(self.spatial_anchor)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorPersistenceInfoMSFT(type={str(self.type)}, next={str(self.next)}, spatial_anchor_persistence_name={str(self.spatial_anchor_persistence_name)}, spatial_anchor={str(self.spatial_anchor)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("spatial_anchor_persistence_name", SpatialAnchorPersistenceNameMSFT),
        ("spatial_anchor", SpatialAnchorMSFTHandle),
    ]


class SpatialAnchorFromPersistedAnchorCreateInfoMSFT(Structure):
    def __init__(
        self,
        spatial_anchor_store: SpatialAnchorStoreConnectionMSFTHandle = None,
        spatial_anchor_persistence_name: SpatialAnchorPersistenceNameMSFT = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SPATIAL_ANCHOR_FROM_PERSISTED_ANCHOR_CREATE_INFO_MSFT,
    ) -> None:
        if spatial_anchor_persistence_name is None:
            spatial_anchor_persistence_name = SpatialAnchorPersistenceNameMSFT()
        super().__init__(
            spatial_anchor_store=spatial_anchor_store,
            spatial_anchor_persistence_name=spatial_anchor_persistence_name,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorFromPersistedAnchorCreateInfoMSFT(type={repr(self.type)}, next={repr(self.next)}, spatial_anchor_store={repr(self.spatial_anchor_store)}, spatial_anchor_persistence_name={repr(self.spatial_anchor_persistence_name)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorFromPersistedAnchorCreateInfoMSFT(type={str(self.type)}, next={str(self.next)}, spatial_anchor_store={str(self.spatial_anchor_store)}, spatial_anchor_persistence_name={str(self.spatial_anchor_persistence_name)})"

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
    def __init__(
        self,
        layer_flags: CompositionLayerSpaceWarpInfoFlagsFB = 0,
        motion_vector_sub_image: SwapchainSubImage = None,
        app_space_delta_pose: Posef = None,
        depth_sub_image: SwapchainSubImage = None,
        min_depth: float = 0,
        max_depth: float = 0,
        near_z: float = 0,
        far_z: float = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.COMPOSITION_LAYER_SPACE_WARP_INFO_FB,
    ) -> None:
        if motion_vector_sub_image is None:
            motion_vector_sub_image = SwapchainSubImage()
        if app_space_delta_pose is None:
            app_space_delta_pose = Posef()
        if depth_sub_image is None:
            depth_sub_image = SwapchainSubImage()
        super().__init__(
            layer_flags=layer_flags,
            motion_vector_sub_image=motion_vector_sub_image,
            app_space_delta_pose=app_space_delta_pose,
            depth_sub_image=depth_sub_image,
            min_depth=min_depth,
            max_depth=max_depth,
            near_z=near_z,
            far_z=far_z,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerSpaceWarpInfoFB(type={repr(self.type)}, next={repr(self.next)}, layer_flags={repr(self.layer_flags)}, motion_vector_sub_image={repr(self.motion_vector_sub_image)}, app_space_delta_pose={repr(self.app_space_delta_pose)}, depth_sub_image={repr(self.depth_sub_image)}, min_depth={repr(self.min_depth)}, max_depth={repr(self.max_depth)}, near_z={repr(self.near_z)}, far_z={repr(self.far_z)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerSpaceWarpInfoFB(type={str(self.type)}, next={str(self.next)}, layer_flags={str(self.layer_flags)}, motion_vector_sub_image={str(self.motion_vector_sub_image)}, app_space_delta_pose={str(self.app_space_delta_pose)}, depth_sub_image={str(self.depth_sub_image)}, min_depth={str(self.min_depth)}, max_depth={str(self.max_depth)}, near_z={str(self.near_z)}, far_z={str(self.far_z)})"

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
    def __init__(
        self,
        recommended_motion_vector_image_rect_width: int = 0,
        recommended_motion_vector_image_rect_height: int = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SYSTEM_SPACE_WARP_PROPERTIES_FB,
    ) -> None:
        super().__init__(
            recommended_motion_vector_image_rect_width=recommended_motion_vector_image_rect_width,
            recommended_motion_vector_image_rect_height=recommended_motion_vector_image_rect_height,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SystemSpaceWarpPropertiesFB(type={repr(self.type)}, next={repr(self.next)}, recommended_motion_vector_image_rect_width={repr(self.recommended_motion_vector_image_rect_width)}, recommended_motion_vector_image_rect_height={repr(self.recommended_motion_vector_image_rect_height)})"

    def __str__(self) -> str:
        return f"xr.SystemSpaceWarpPropertiesFB(type={str(self.type)}, next={str(self.next)}, recommended_motion_vector_image_rect_width={str(self.recommended_motion_vector_image_rect_width)}, recommended_motion_vector_image_rect_height={str(self.recommended_motion_vector_image_rect_height)})"

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
