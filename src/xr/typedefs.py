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

InstanceCreateFlagsCInt = Flags64

SessionCreateFlagsCInt = Flags64

SpaceVelocityFlagsCInt = Flags64

SpaceLocationFlagsCInt = Flags64

SwapchainCreateFlagsCInt = Flags64

SwapchainUsageFlagsCInt = Flags64

CompositionLayerFlagsCInt = Flags64

ViewStateFlagsCInt = Flags64

InputSourceLocalizedNameFlagsCInt = Flags64

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
        return f"xr.ApiLayerProperties(layer_name={repr(self.layer_name)}, spec_version={repr(self.spec_version)}, layer_version={repr(self.layer_version)}, description={repr(self.description)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ApiLayerProperties(layer_name={self.layer_name}, spec_version={self.spec_version}, layer_version={self.layer_version}, description={self.description}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.ApplicationInfo(application_name={self.application_name}, application_version={self.application_version}, engine_name={self.engine_name}, engine_version={self.engine_version}, api_version={self.api_version})"

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
        create_flags: InstanceCreateFlags = InstanceCreateFlags(),
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
            create_flags=InstanceCreateFlags(create_flags).value,
            application_info=application_info,
            enabled_api_layer_count=enabled_api_layer_count,
            enabled_api_layer_names=enabled_api_layer_names,
            enabled_extension_count=enabled_extension_count,
            enabled_extension_names=enabled_extension_names,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.InstanceCreateInfo(create_flags={repr(self.create_flags)}, application_info={repr(self.application_info)}, enabled_api_layer_count={repr(self.enabled_api_layer_count)}, enabled_api_layer_names={repr(self.enabled_api_layer_names)}, enabled_extension_count={repr(self.enabled_extension_count)}, enabled_extension_names={repr(self.enabled_extension_names)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.InstanceCreateInfo(create_flags={self.create_flags}, application_info={self.application_info}, enabled_api_layer_count={self.enabled_api_layer_count}, enabled_api_layer_names={self.enabled_api_layer_names}, enabled_extension_count={self.enabled_extension_count}, enabled_extension_names={self.enabled_extension_names}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("create_flags", InstanceCreateFlagsCInt),
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
        return f"xr.InstanceProperties(runtime_version={repr(self.runtime_version)}, runtime_name={repr(self.runtime_name)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.InstanceProperties(runtime_version={self.runtime_version}, runtime_name={self.runtime_name}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.EventDataBuffer(varying={repr(self.varying)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.EventDataBuffer(next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("varying", (c_uint8 * 4000)),
    ]


class SystemGetInfo(Structure):
    def __init__(
        self,
        form_factor: FormFactor = FormFactor(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SYSTEM_GET_INFO,
    ) -> None:
        super().__init__(
            form_factor=FormFactor(form_factor).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SystemGetInfo(form_factor={repr(self.form_factor)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SystemGetInfo(form_factor={self.form_factor}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SystemGraphicsProperties(max_swapchain_image_height={self.max_swapchain_image_height}, max_swapchain_image_width={self.max_swapchain_image_width}, max_layer_count={self.max_layer_count})"

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
        return f"xr.SystemTrackingProperties(orientation_tracking={self.orientation_tracking}, position_tracking={self.position_tracking})"

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
        return f"xr.SystemProperties(system_id={repr(self.system_id)}, vendor_id={repr(self.vendor_id)}, system_name={repr(self.system_name)}, graphics_properties={repr(self.graphics_properties)}, tracking_properties={repr(self.tracking_properties)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SystemProperties(system_id={self.system_id}, vendor_id={self.vendor_id}, system_name={self.system_name}, graphics_properties={self.graphics_properties}, tracking_properties={self.tracking_properties}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        create_flags: SessionCreateFlags = SessionCreateFlags(),
        system_id: SystemId = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SESSION_CREATE_INFO,
    ) -> None:
        super().__init__(
            create_flags=SessionCreateFlags(create_flags).value,
            system_id=system_id,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SessionCreateInfo(create_flags={repr(self.create_flags)}, system_id={repr(self.system_id)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SessionCreateInfo(create_flags={self.create_flags}, system_id={self.system_id}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("create_flags", SessionCreateFlagsCInt),
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

    def as_numpy(self):
        if self._numpy is None:
            # Just in time construction
            buffer = (c_float * len(self)).from_address(addressof(self))
            buffer._wrapper = self  # To link lifetime of buffer to self
            self._numpy = numpy.ctypeslib.as_array(buffer)
        return self._numpy
    def __repr__(self) -> str:
        return f"xr.Vector3f(x={repr(self.x)}, y={repr(self.y)}, z={repr(self.z)})"

    def __str__(self) -> str:
        return f"(x={self.x:.3f}, y={self.y:.3f}, z={self.z:.3f})"

    _fields_ = [
        ("x", c_float),
        ("y", c_float),
        ("z", c_float),
    ]


class SpaceVelocity(Structure):
    def __init__(
        self,
        velocity_flags: SpaceVelocityFlags = SpaceVelocityFlags(),
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
            velocity_flags=SpaceVelocityFlags(velocity_flags).value,
            linear_velocity=linear_velocity,
            angular_velocity=angular_velocity,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceVelocity(velocity_flags={repr(self.velocity_flags)}, linear_velocity={repr(self.linear_velocity)}, angular_velocity={repr(self.angular_velocity)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SpaceVelocity(velocity_flags={self.velocity_flags}, linear_velocity={self.linear_velocity}, angular_velocity={self.angular_velocity}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("velocity_flags", SpaceVelocityFlagsCInt),
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

    def as_numpy(self):
        if self._numpy is None:
            # Just in time construction
            buffer = (c_float * len(self)).from_address(addressof(self))
            buffer._wrapper = self  # To link lifetime of buffer to self
            self._numpy = numpy.ctypeslib.as_array(buffer)
        return self._numpy
    def __repr__(self) -> str:
        return f"xr.Quaternionf(x={repr(self.x)}, y={repr(self.y)}, z={repr(self.z)}, w={repr(self.w)})"

    def __str__(self) -> str:
        return f"(x={self.x:.3f}, y={self.y:.3f}, z={self.z:.3f}, w={self.w:.3f})"

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
        return f"(orientation={self.orientation}, position={self.position})"

    _fields_ = [
        ("orientation", Quaternionf),
        ("position", Vector3f),
    ]


class ReferenceSpaceCreateInfo(Structure):
    def __init__(
        self,
        reference_space_type: ReferenceSpaceType = ReferenceSpaceType(),
        pose_in_reference_space: Posef = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.REFERENCE_SPACE_CREATE_INFO,
    ) -> None:
        if pose_in_reference_space is None:
            pose_in_reference_space = Posef()
        super().__init__(
            reference_space_type=ReferenceSpaceType(reference_space_type).value,
            pose_in_reference_space=pose_in_reference_space,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ReferenceSpaceCreateInfo(reference_space_type={repr(self.reference_space_type)}, pose_in_reference_space={repr(self.pose_in_reference_space)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ReferenceSpaceCreateInfo(reference_space_type={self.reference_space_type}, pose_in_reference_space={self.pose_in_reference_space}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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

    def as_numpy(self):
        if self._numpy is None:
            # Just in time construction
            buffer = (c_float * len(self)).from_address(addressof(self))
            buffer._wrapper = self  # To link lifetime of buffer to self
            self._numpy = numpy.ctypeslib.as_array(buffer)
        return self._numpy
    def __repr__(self) -> str:
        return f"xr.Extent2Df(width={repr(self.width)}, height={repr(self.height)})"

    def __str__(self) -> str:
        return f"xr.Extent2Df(width={self.width:.3f}, height={self.height:.3f})"

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
        return f"xr.ActionSpaceCreateInfo(action={repr(self.action)}, subaction_path={repr(self.subaction_path)}, pose_in_action_space={repr(self.pose_in_action_space)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ActionSpaceCreateInfo(action={self.action}, subaction_path={self.subaction_path}, pose_in_action_space={self.pose_in_action_space}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        location_flags: SpaceLocationFlags = SpaceLocationFlags(),
        pose: Posef = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SPACE_LOCATION,
    ) -> None:
        if pose is None:
            pose = Posef()
        super().__init__(
            location_flags=SpaceLocationFlags(location_flags).value,
            pose=pose,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceLocation(location_flags={repr(self.location_flags)}, pose={repr(self.pose)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SpaceLocation(location_flags={self.location_flags}, pose={self.pose}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("location_flags", SpaceLocationFlagsCInt),
        ("pose", Posef),
    ]


class ViewConfigurationProperties(Structure):
    def __init__(
        self,
        view_configuration_type: ViewConfigurationType = ViewConfigurationType(),
        fov_mutable: Bool32 = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.VIEW_CONFIGURATION_PROPERTIES,
    ) -> None:
        super().__init__(
            view_configuration_type=ViewConfigurationType(view_configuration_type).value,
            fov_mutable=fov_mutable,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ViewConfigurationProperties(view_configuration_type={repr(self.view_configuration_type)}, fov_mutable={repr(self.fov_mutable)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ViewConfigurationProperties(view_configuration_type={self.view_configuration_type}, fov_mutable={self.fov_mutable}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.ViewConfigurationView(recommended_image_rect_width={repr(self.recommended_image_rect_width)}, max_image_rect_width={repr(self.max_image_rect_width)}, recommended_image_rect_height={repr(self.recommended_image_rect_height)}, max_image_rect_height={repr(self.max_image_rect_height)}, recommended_swapchain_sample_count={repr(self.recommended_swapchain_sample_count)}, max_swapchain_sample_count={repr(self.max_swapchain_sample_count)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ViewConfigurationView(recommended_image_rect_width={self.recommended_image_rect_width}, max_image_rect_width={self.max_image_rect_width}, recommended_image_rect_height={self.recommended_image_rect_height}, max_image_rect_height={self.max_image_rect_height}, recommended_swapchain_sample_count={self.recommended_swapchain_sample_count}, max_swapchain_sample_count={self.max_swapchain_sample_count}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        create_flags: SwapchainCreateFlags = SwapchainCreateFlags(),
        usage_flags: SwapchainUsageFlags = SwapchainUsageFlags(),
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
            create_flags=SwapchainCreateFlags(create_flags).value,
            usage_flags=SwapchainUsageFlags(usage_flags).value,
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
        return f"xr.SwapchainCreateInfo(create_flags={repr(self.create_flags)}, usage_flags={repr(self.usage_flags)}, format={repr(self.format)}, sample_count={repr(self.sample_count)}, width={repr(self.width)}, height={repr(self.height)}, face_count={repr(self.face_count)}, array_size={repr(self.array_size)}, mip_count={repr(self.mip_count)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainCreateInfo(create_flags={self.create_flags}, usage_flags={self.usage_flags}, format={self.format}, sample_count={self.sample_count}, width={self.width}, height={self.height}, face_count={self.face_count}, array_size={self.array_size}, mip_count={self.mip_count}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("create_flags", SwapchainCreateFlagsCInt),
        ("usage_flags", SwapchainUsageFlagsCInt),
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
        return f"xr.SwapchainImageBaseHeader(next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageBaseHeader(next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SwapchainImageAcquireInfo(next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageAcquireInfo(next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SwapchainImageWaitInfo(timeout={repr(self.timeout)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageWaitInfo(timeout={self.timeout}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SwapchainImageReleaseInfo(next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageReleaseInfo(next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SessionBeginInfo(Structure):
    def __init__(
        self,
        primary_view_configuration_type: ViewConfigurationType = ViewConfigurationType(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SESSION_BEGIN_INFO,
    ) -> None:
        super().__init__(
            primary_view_configuration_type=ViewConfigurationType(primary_view_configuration_type).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SessionBeginInfo(primary_view_configuration_type={repr(self.primary_view_configuration_type)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SessionBeginInfo(primary_view_configuration_type={self.primary_view_configuration_type}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.FrameWaitInfo(next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.FrameWaitInfo(next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.FrameState(predicted_display_time={repr(self.predicted_display_time)}, predicted_display_period={repr(self.predicted_display_period)}, should_render={repr(self.should_render)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.FrameState(predicted_display_time={self.predicted_display_time}, predicted_display_period={self.predicted_display_period}, should_render={self.should_render}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.FrameBeginInfo(next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.FrameBeginInfo(next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class CompositionLayerBaseHeader(Structure):
    def __init__(
        self,
        layer_flags: CompositionLayerFlags = CompositionLayerFlags(),
        space: SpaceHandle = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            layer_flags=CompositionLayerFlags(layer_flags).value,
            space=space,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerBaseHeader(layer_flags={repr(self.layer_flags)}, space={repr(self.space)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerBaseHeader(layer_flags={self.layer_flags}, space={self.space}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlagsCInt),
        ("space", SpaceHandle),
    ]


class FrameEndInfo(Structure):
    def __init__(
        self,
        display_time: Time = 0,
        environment_blend_mode: EnvironmentBlendMode = EnvironmentBlendMode(),
        layer_count: int = 0,
        layers: POINTER(POINTER(CompositionLayerBaseHeader)) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.FRAME_END_INFO,
    ) -> None:
        super().__init__(
            display_time=display_time,
            environment_blend_mode=EnvironmentBlendMode(environment_blend_mode).value,
            layer_count=layer_count,
            layers=layers,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.FrameEndInfo(display_time={repr(self.display_time)}, environment_blend_mode={repr(self.environment_blend_mode)}, layer_count={repr(self.layer_count)}, layers={repr(self.layers)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.FrameEndInfo(display_time={self.display_time}, environment_blend_mode={self.environment_blend_mode}, layer_count={self.layer_count}, layers={self.layers}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        view_configuration_type: ViewConfigurationType = ViewConfigurationType(),
        display_time: Time = 0,
        space: SpaceHandle = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.VIEW_LOCATE_INFO,
    ) -> None:
        super().__init__(
            view_configuration_type=ViewConfigurationType(view_configuration_type).value,
            display_time=display_time,
            space=space,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ViewLocateInfo(view_configuration_type={repr(self.view_configuration_type)}, display_time={repr(self.display_time)}, space={repr(self.space)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ViewLocateInfo(view_configuration_type={self.view_configuration_type}, display_time={self.display_time}, space={self.space}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        view_state_flags: ViewStateFlags = ViewStateFlags(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.VIEW_STATE,
    ) -> None:
        super().__init__(
            view_state_flags=ViewStateFlags(view_state_flags).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ViewState(view_state_flags={repr(self.view_state_flags)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ViewState(view_state_flags={self.view_state_flags}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_state_flags", ViewStateFlagsCInt),
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

    def as_numpy(self):
        if self._numpy is None:
            # Just in time construction
            buffer = (c_float * len(self)).from_address(addressof(self))
            buffer._wrapper = self  # To link lifetime of buffer to self
            self._numpy = numpy.ctypeslib.as_array(buffer)
        return self._numpy
    def __repr__(self) -> str:
        return f"xr.Fovf(angle_left={repr(self.angle_left)}, angle_right={repr(self.angle_right)}, angle_up={repr(self.angle_up)}, angle_down={repr(self.angle_down)})"

    def __str__(self) -> str:
        return f"xr.Fovf(angle_left={self.angle_left:.3f}, angle_right={self.angle_right:.3f}, angle_up={self.angle_up:.3f}, angle_down={self.angle_down:.3f})"

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
        return f"xr.View(pose={repr(self.pose)}, fov={repr(self.fov)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.View(pose={self.pose}, fov={self.fov}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.ActionSetCreateInfo(action_set_name={repr(self.action_set_name)}, localized_action_set_name={repr(self.localized_action_set_name)}, priority={repr(self.priority)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ActionSetCreateInfo(action_set_name={self.action_set_name}, localized_action_set_name={self.localized_action_set_name}, priority={self.priority}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        action_type: ActionType = ActionType(),
        count_subaction_paths: int = 0,
        subaction_paths: POINTER(c_uint64) = None,
        localized_action_name: str = "",
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.ACTION_CREATE_INFO,
    ) -> None:
        super().__init__(
            action_name=action_name.encode(),
            action_type=ActionType(action_type).value,
            count_subaction_paths=count_subaction_paths,
            subaction_paths=subaction_paths,
            localized_action_name=localized_action_name.encode(),
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ActionCreateInfo(action_name={repr(self.action_name)}, action_type={repr(self.action_type)}, count_subaction_paths={repr(self.count_subaction_paths)}, subaction_paths={repr(self.subaction_paths)}, localized_action_name={repr(self.localized_action_name)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ActionCreateInfo(action_name={self.action_name}, action_type={self.action_type}, count_subaction_paths={self.count_subaction_paths}, subaction_paths={self.subaction_paths}, localized_action_name={self.localized_action_name}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.ActionSuggestedBinding(action={self.action}, binding={self.binding})"

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
        return f"xr.InteractionProfileSuggestedBinding(interaction_profile={repr(self.interaction_profile)}, count_suggested_bindings={repr(self.count_suggested_bindings)}, suggested_bindings={repr(self.suggested_bindings)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.InteractionProfileSuggestedBinding(interaction_profile={self.interaction_profile}, count_suggested_bindings={self.count_suggested_bindings}, suggested_bindings={self.suggested_bindings}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SessionActionSetsAttachInfo(count_action_sets={repr(self.count_action_sets)}, action_sets={repr(self.action_sets)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SessionActionSetsAttachInfo(count_action_sets={self.count_action_sets}, action_sets={self.action_sets}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.InteractionProfileState(interaction_profile={repr(self.interaction_profile)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.InteractionProfileState(interaction_profile={self.interaction_profile}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.ActionStateGetInfo(action={repr(self.action)}, subaction_path={repr(self.subaction_path)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ActionStateGetInfo(action={self.action}, subaction_path={self.subaction_path}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.ActionStateBoolean(current_state={repr(self.current_state)}, changed_since_last_sync={repr(self.changed_since_last_sync)}, last_change_time={repr(self.last_change_time)}, is_active={repr(self.is_active)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ActionStateBoolean(current_state={self.current_state}, changed_since_last_sync={self.changed_since_last_sync}, last_change_time={self.last_change_time}, is_active={self.is_active}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.ActionStateFloat(current_state={repr(self.current_state)}, changed_since_last_sync={repr(self.changed_since_last_sync)}, last_change_time={repr(self.last_change_time)}, is_active={repr(self.is_active)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ActionStateFloat(current_state={self.current_state:.3f}, changed_since_last_sync={self.changed_since_last_sync}, last_change_time={self.last_change_time}, is_active={self.is_active}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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

    def as_numpy(self):
        if self._numpy is None:
            # Just in time construction
            buffer = (c_float * len(self)).from_address(addressof(self))
            buffer._wrapper = self  # To link lifetime of buffer to self
            self._numpy = numpy.ctypeslib.as_array(buffer)
        return self._numpy
    def __repr__(self) -> str:
        return f"xr.Vector2f(x={repr(self.x)}, y={repr(self.y)})"

    def __str__(self) -> str:
        return f"xr.Vector2f(x={self.x:.3f}, y={self.y:.3f})"

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
        return f"xr.ActionStateVector2f(current_state={repr(self.current_state)}, changed_since_last_sync={repr(self.changed_since_last_sync)}, last_change_time={repr(self.last_change_time)}, is_active={repr(self.is_active)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ActionStateVector2f(current_state={self.current_state}, changed_since_last_sync={self.changed_since_last_sync}, last_change_time={self.last_change_time}, is_active={self.is_active}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.ActionStatePose(is_active={repr(self.is_active)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ActionStatePose(is_active={self.is_active}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.ActiveActionSet(action_set={self.action_set}, subaction_path={self.subaction_path})"

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
        return f"xr.ActionsSyncInfo(count_active_action_sets={repr(self.count_active_action_sets)}, active_action_sets={repr(self.active_action_sets)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ActionsSyncInfo(count_active_action_sets={self.count_active_action_sets}, active_action_sets={self.active_action_sets}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.BoundSourcesForActionEnumerateInfo(action={repr(self.action)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.BoundSourcesForActionEnumerateInfo(action={self.action}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("action", ActionHandle),
    ]


class InputSourceLocalizedNameGetInfo(Structure):
    def __init__(
        self,
        source_path: Path = 0,
        which_components: InputSourceLocalizedNameFlags = InputSourceLocalizedNameFlags(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.INPUT_SOURCE_LOCALIZED_NAME_GET_INFO,
    ) -> None:
        super().__init__(
            source_path=source_path,
            which_components=InputSourceLocalizedNameFlags(which_components).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.InputSourceLocalizedNameGetInfo(source_path={repr(self.source_path)}, which_components={repr(self.which_components)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.InputSourceLocalizedNameGetInfo(source_path={self.source_path}, which_components={self.which_components}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("source_path", Path),
        ("which_components", InputSourceLocalizedNameFlagsCInt),
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
        return f"xr.HapticActionInfo(action={repr(self.action)}, subaction_path={repr(self.subaction_path)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.HapticActionInfo(action={self.action}, subaction_path={self.subaction_path}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.HapticBaseHeader(next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.HapticBaseHeader(next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.BaseInStructure(next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.BaseInStructure(next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.BaseOutStructure(next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.BaseOutStructure(next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.Offset2Di(x={self.x}, y={self.y})"

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
        return f"xr.Extent2Di(width={self.width}, height={self.height})"

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
        return f"xr.Rect2Di(offset={self.offset}, extent={self.extent})"

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
        return f"xr.SwapchainSubImage(swapchain={self.swapchain}, image_rect={self.image_rect}, image_array_index={self.image_array_index})"

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
        return f"xr.CompositionLayerProjectionView(pose={repr(self.pose)}, fov={repr(self.fov)}, sub_image={repr(self.sub_image)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerProjectionView(pose={self.pose}, fov={self.fov}, sub_image={self.sub_image}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        layer_flags: CompositionLayerFlags = CompositionLayerFlags(),
        space: SpaceHandle = None,
        view_count: int = 0,
        views: POINTER(CompositionLayerProjectionView) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.COMPOSITION_LAYER_PROJECTION,
    ) -> None:
        super().__init__(
            layer_flags=CompositionLayerFlags(layer_flags).value,
            space=space,
            view_count=view_count,
            views=views,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerProjection(layer_flags={repr(self.layer_flags)}, space={repr(self.space)}, view_count={repr(self.view_count)}, views={repr(self.views)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerProjection(layer_flags={self.layer_flags}, space={self.space}, view_count={self.view_count}, views={self.views}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlagsCInt),
        ("space", SpaceHandle),
        ("view_count", c_uint32),
        ("views", POINTER(CompositionLayerProjectionView)),
    ]


class CompositionLayerQuad(Structure):
    def __init__(
        self,
        layer_flags: CompositionLayerFlags = CompositionLayerFlags(),
        space: SpaceHandle = None,
        eye_visibility: EyeVisibility = EyeVisibility(),
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
            layer_flags=CompositionLayerFlags(layer_flags).value,
            space=space,
            eye_visibility=EyeVisibility(eye_visibility).value,
            sub_image=sub_image,
            pose=pose,
            size=size,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerQuad(layer_flags={repr(self.layer_flags)}, space={repr(self.space)}, eye_visibility={repr(self.eye_visibility)}, sub_image={repr(self.sub_image)}, pose={repr(self.pose)}, size={repr(self.size)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerQuad(layer_flags={self.layer_flags}, space={self.space}, eye_visibility={self.eye_visibility}, sub_image={self.sub_image}, pose={self.pose}, size={self.size}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlagsCInt),
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
        return f"xr.EventDataBaseHeader(next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.EventDataBaseHeader(next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.EventDataEventsLost(lost_event_count={repr(self.lost_event_count)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.EventDataEventsLost(lost_event_count={self.lost_event_count}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.EventDataInstanceLossPending(loss_time={repr(self.loss_time)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.EventDataInstanceLossPending(loss_time={self.loss_time}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("loss_time", Time),
    ]


class EventDataSessionStateChanged(Structure):
    def __init__(
        self,
        session: SessionHandle = None,
        state: SessionState = SessionState(),
        time: Time = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.EVENT_DATA_SESSION_STATE_CHANGED,
    ) -> None:
        super().__init__(
            session=session,
            state=SessionState(state).value,
            time=time,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataSessionStateChanged(session={repr(self.session)}, state={repr(self.state)}, time={repr(self.time)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.EventDataSessionStateChanged(session={self.session}, state={self.state}, time={self.time}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        reference_space_type: ReferenceSpaceType = ReferenceSpaceType(),
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
            reference_space_type=ReferenceSpaceType(reference_space_type).value,
            change_time=change_time,
            pose_valid=pose_valid,
            pose_in_previous_space=pose_in_previous_space,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataReferenceSpaceChangePending(session={repr(self.session)}, reference_space_type={repr(self.reference_space_type)}, change_time={repr(self.change_time)}, pose_valid={repr(self.pose_valid)}, pose_in_previous_space={repr(self.pose_in_previous_space)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.EventDataReferenceSpaceChangePending(session={self.session}, reference_space_type={self.reference_space_type}, change_time={self.change_time}, pose_valid={self.pose_valid}, pose_in_previous_space={self.pose_in_previous_space}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.EventDataInteractionProfileChanged(session={repr(self.session)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.EventDataInteractionProfileChanged(session={self.session}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.HapticVibration(duration={repr(self.duration)}, frequency={repr(self.frequency)}, amplitude={repr(self.amplitude)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.HapticVibration(duration={self.duration}, frequency={self.frequency:.3f}, amplitude={self.amplitude:.3f}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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

    def as_numpy(self):
        if self._numpy is None:
            # Just in time construction
            buffer = (c_float * len(self)).from_address(addressof(self))
            buffer._wrapper = self  # To link lifetime of buffer to self
            self._numpy = numpy.ctypeslib.as_array(buffer)
        return self._numpy
    def __repr__(self) -> str:
        return f"xr.Offset2Df(x={repr(self.x)}, y={repr(self.y)})"

    def __str__(self) -> str:
        return f"xr.Offset2Df(x={self.x:.3f}, y={self.y:.3f})"

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
        return f"xr.Rect2Df(offset={self.offset}, extent={self.extent})"

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

    def as_numpy(self):
        if self._numpy is None:
            # Just in time construction
            buffer = (c_float * len(self)).from_address(addressof(self))
            buffer._wrapper = self  # To link lifetime of buffer to self
            self._numpy = numpy.ctypeslib.as_array(buffer)
        return self._numpy
    def __repr__(self) -> str:
        return f"xr.Vector4f(x={repr(self.x)}, y={repr(self.y)}, z={repr(self.z)}, w={repr(self.w)})"

    def __str__(self) -> str:
        return f"xr.Vector4f(x={self.x:.3f}, y={self.y:.3f}, z={self.z:.3f}, w={self.w:.3f})"

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

    def as_numpy(self):
        if self._numpy is None:
            # Just in time construction
            buffer = (c_float * len(self)).from_address(addressof(self))
            buffer._wrapper = self  # To link lifetime of buffer to self
            self._numpy = numpy.ctypeslib.as_array(buffer)
        return self._numpy
    def __repr__(self) -> str:
        return f"xr.Color4f(r={repr(self.r)}, g={repr(self.g)}, b={repr(self.b)}, a={repr(self.a)})"

    def __str__(self) -> str:
        return f"xr.Color4f(r={self.r:.3f}, g={self.g:.3f}, b={self.b:.3f}, a={self.a:.3f})"

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
        layer_flags: CompositionLayerFlags = CompositionLayerFlags(),
        space: SpaceHandle = None,
        eye_visibility: EyeVisibility = EyeVisibility(),
        swapchain: SwapchainHandle = None,
        image_array_index: int = 0,
        orientation: Quaternionf = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.COMPOSITION_LAYER_CUBE_KHR,
    ) -> None:
        if orientation is None:
            orientation = Quaternionf()
        super().__init__(
            layer_flags=CompositionLayerFlags(layer_flags).value,
            space=space,
            eye_visibility=EyeVisibility(eye_visibility).value,
            swapchain=swapchain,
            image_array_index=image_array_index,
            orientation=orientation,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerCubeKHR(layer_flags={repr(self.layer_flags)}, space={repr(self.space)}, eye_visibility={repr(self.eye_visibility)}, swapchain={repr(self.swapchain)}, image_array_index={repr(self.image_array_index)}, orientation={repr(self.orientation)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerCubeKHR(layer_flags={self.layer_flags}, space={self.space}, eye_visibility={self.eye_visibility}, swapchain={self.swapchain}, image_array_index={self.image_array_index}, orientation={self.orientation}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlagsCInt),
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
        return f"xr.CompositionLayerDepthInfoKHR(sub_image={repr(self.sub_image)}, min_depth={repr(self.min_depth)}, max_depth={repr(self.max_depth)}, near_z={repr(self.near_z)}, far_z={repr(self.far_z)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerDepthInfoKHR(sub_image={self.sub_image}, min_depth={self.min_depth:.3f}, max_depth={self.max_depth:.3f}, near_z={self.near_z:.3f}, far_z={self.far_z:.3f}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        layer_flags: CompositionLayerFlags = CompositionLayerFlags(),
        space: SpaceHandle = None,
        eye_visibility: EyeVisibility = EyeVisibility(),
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
            layer_flags=CompositionLayerFlags(layer_flags).value,
            space=space,
            eye_visibility=EyeVisibility(eye_visibility).value,
            sub_image=sub_image,
            pose=pose,
            radius=radius,
            central_angle=central_angle,
            aspect_ratio=aspect_ratio,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerCylinderKHR(layer_flags={repr(self.layer_flags)}, space={repr(self.space)}, eye_visibility={repr(self.eye_visibility)}, sub_image={repr(self.sub_image)}, pose={repr(self.pose)}, radius={repr(self.radius)}, central_angle={repr(self.central_angle)}, aspect_ratio={repr(self.aspect_ratio)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerCylinderKHR(layer_flags={self.layer_flags}, space={self.space}, eye_visibility={self.eye_visibility}, sub_image={self.sub_image}, pose={self.pose}, radius={self.radius:.3f}, central_angle={self.central_angle:.3f}, aspect_ratio={self.aspect_ratio:.3f}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlagsCInt),
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
        layer_flags: CompositionLayerFlags = CompositionLayerFlags(),
        space: SpaceHandle = None,
        eye_visibility: EyeVisibility = EyeVisibility(),
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
            layer_flags=CompositionLayerFlags(layer_flags).value,
            space=space,
            eye_visibility=EyeVisibility(eye_visibility).value,
            sub_image=sub_image,
            pose=pose,
            radius=radius,
            scale=scale,
            bias=bias,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerEquirectKHR(layer_flags={repr(self.layer_flags)}, space={repr(self.space)}, eye_visibility={repr(self.eye_visibility)}, sub_image={repr(self.sub_image)}, pose={repr(self.pose)}, radius={repr(self.radius)}, scale={repr(self.scale)}, bias={repr(self.bias)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerEquirectKHR(layer_flags={self.layer_flags}, space={self.space}, eye_visibility={self.eye_visibility}, sub_image={self.sub_image}, pose={self.pose}, radius={self.radius:.3f}, scale={self.scale}, bias={self.bias}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlagsCInt),
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
        return f"xr.VisibilityMaskKHR(vertex_capacity_input={repr(self.vertex_capacity_input)}, vertex_count_output={repr(self.vertex_count_output)}, vertices={repr(self.vertices)}, index_capacity_input={repr(self.index_capacity_input)}, index_count_output={repr(self.index_count_output)}, indices={repr(self.indices)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.VisibilityMaskKHR(vertex_capacity_input={self.vertex_capacity_input}, vertex_count_output={self.vertex_count_output}, vertices={self.vertices}, index_capacity_input={self.index_capacity_input}, index_count_output={self.index_count_output}, indices={self.indices}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        view_configuration_type: ViewConfigurationType = ViewConfigurationType(),
        view_index: int = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.EVENT_DATA_VISIBILITY_MASK_CHANGED_KHR,
    ) -> None:
        super().__init__(
            session=session,
            view_configuration_type=ViewConfigurationType(view_configuration_type).value,
            view_index=view_index,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataVisibilityMaskChangedKHR(session={repr(self.session)}, view_configuration_type={repr(self.view_configuration_type)}, view_index={repr(self.view_index)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.EventDataVisibilityMaskChangedKHR(session={self.session}, view_configuration_type={self.view_configuration_type}, view_index={self.view_index}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.CompositionLayerColorScaleBiasKHR(color_scale={repr(self.color_scale)}, color_bias={repr(self.color_bias)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerColorScaleBiasKHR(color_scale={self.color_scale}, color_bias={self.color_bias}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.LoaderInitInfoBaseHeaderKHR(next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.LoaderInitInfoBaseHeaderKHR(next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


PFN_xrInitializeLoaderKHR = CFUNCTYPE(Result.ctype(), POINTER(LoaderInitInfoBaseHeaderKHR))


class CompositionLayerEquirect2KHR(Structure):
    def __init__(
        self,
        layer_flags: CompositionLayerFlags = CompositionLayerFlags(),
        space: SpaceHandle = None,
        eye_visibility: EyeVisibility = EyeVisibility(),
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
            layer_flags=CompositionLayerFlags(layer_flags).value,
            space=space,
            eye_visibility=EyeVisibility(eye_visibility).value,
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
        return f"xr.CompositionLayerEquirect2KHR(layer_flags={repr(self.layer_flags)}, space={repr(self.space)}, eye_visibility={repr(self.eye_visibility)}, sub_image={repr(self.sub_image)}, pose={repr(self.pose)}, radius={repr(self.radius)}, central_horizontal_angle={repr(self.central_horizontal_angle)}, upper_vertical_angle={repr(self.upper_vertical_angle)}, lower_vertical_angle={repr(self.lower_vertical_angle)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerEquirect2KHR(layer_flags={self.layer_flags}, space={self.space}, eye_visibility={self.eye_visibility}, sub_image={self.sub_image}, pose={self.pose}, radius={self.radius:.3f}, central_horizontal_angle={self.central_horizontal_angle:.3f}, upper_vertical_angle={self.upper_vertical_angle:.3f}, lower_vertical_angle={self.lower_vertical_angle:.3f}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlagsCInt),
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
        return f"xr.BindingModificationBaseHeaderKHR(next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.BindingModificationBaseHeaderKHR(next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.BindingModificationsKHR(binding_modification_count={repr(self.binding_modification_count)}, binding_modifications={repr(self.binding_modifications)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.BindingModificationsKHR(binding_modification_count={self.binding_modification_count}, binding_modifications={self.binding_modifications}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("binding_modification_count", c_uint32),
        ("binding_modifications", POINTER(POINTER(BindingModificationBaseHeaderKHR))),
    ]


class EventDataPerfSettingsEXT(Structure):
    def __init__(
        self,
        domain: PerfSettingsDomainEXT = PerfSettingsDomainEXT(),
        sub_domain: PerfSettingsSubDomainEXT = PerfSettingsSubDomainEXT(),
        from_level: PerfSettingsNotificationLevelEXT = PerfSettingsNotificationLevelEXT(),
        to_level: PerfSettingsNotificationLevelEXT = PerfSettingsNotificationLevelEXT(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.EVENT_DATA_PERF_SETTINGS_EXT,
    ) -> None:
        super().__init__(
            domain=PerfSettingsDomainEXT(domain).value,
            sub_domain=PerfSettingsSubDomainEXT(sub_domain).value,
            from_level=PerfSettingsNotificationLevelEXT(from_level).value,
            to_level=PerfSettingsNotificationLevelEXT(to_level).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataPerfSettingsEXT(domain={repr(self.domain)}, sub_domain={repr(self.sub_domain)}, from_level={repr(self.from_level)}, to_level={repr(self.to_level)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.EventDataPerfSettingsEXT(domain={self.domain}, sub_domain={self.sub_domain}, from_level={self.from_level}, to_level={self.to_level}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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

DebugUtilsMessageSeverityFlagsEXTCInt = Flags64

DebugUtilsMessageTypeFlagsEXTCInt = Flags64


class DebugUtilsObjectNameInfoEXT(Structure):
    def __init__(
        self,
        object_type: ObjectType = ObjectType(),
        object_handle: int = 0,
        object_name: str = "",
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.DEBUG_UTILS_OBJECT_NAME_INFO_EXT,
    ) -> None:
        super().__init__(
            object_type=ObjectType(object_type).value,
            object_handle=object_handle,
            object_name=object_name.encode(),
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.DebugUtilsObjectNameInfoEXT(object_type={repr(self.object_type)}, object_handle={repr(self.object_handle)}, object_name={repr(self.object_name)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.DebugUtilsObjectNameInfoEXT(object_type={self.object_type}, object_handle={self.object_handle}, object_name={self.object_name}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.DebugUtilsLabelEXT(label_name={repr(self.label_name)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.DebugUtilsLabelEXT(label_name={self.label_name}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.DebugUtilsMessengerCallbackDataEXT(message_id={repr(self.message_id)}, function_name={repr(self.function_name)}, message={repr(self.message)}, object_count={repr(self.object_count)}, objects={repr(self.objects)}, session_label_count={repr(self.session_label_count)}, session_labels={repr(self.session_labels)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.DebugUtilsMessengerCallbackDataEXT(message_id={self.message_id}, function_name={self.function_name}, message={self.message}, object_count={self.object_count}, objects={self.objects}, session_label_count={self.session_label_count}, session_labels={self.session_labels}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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


PFN_xrDebugUtilsMessengerCallbackEXT = CFUNCTYPE(Bool32, DebugUtilsMessageSeverityFlagsEXTCInt, DebugUtilsMessageTypeFlagsEXTCInt, POINTER(DebugUtilsMessengerCallbackDataEXT), c_void_p)


class DebugUtilsMessengerCreateInfoEXT(Structure):
    def __init__(
        self,
        message_severities: DebugUtilsMessageSeverityFlagsEXT = DebugUtilsMessageSeverityFlagsEXT(),
        message_types: DebugUtilsMessageTypeFlagsEXT = DebugUtilsMessageTypeFlagsEXT(),
        user_callback: PFN_xrDebugUtilsMessengerCallbackEXT = cast(None, PFN_xrDebugUtilsMessengerCallbackEXT),
        user_data: c_void_p = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.DEBUG_UTILS_MESSENGER_CREATE_INFO_EXT,
    ) -> None:
        super().__init__(
            message_severities=DebugUtilsMessageSeverityFlagsEXT(message_severities).value,
            message_types=DebugUtilsMessageTypeFlagsEXT(message_types).value,
            user_callback=user_callback,
            user_data=user_data,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.DebugUtilsMessengerCreateInfoEXT(message_severities={repr(self.message_severities)}, message_types={repr(self.message_types)}, user_callback={repr(self.user_callback)}, user_data={repr(self.user_data)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.DebugUtilsMessengerCreateInfoEXT(message_severities={self.message_severities}, message_types={self.message_types}, user_callback={self.user_callback}, user_data={self.user_data}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("message_severities", DebugUtilsMessageSeverityFlagsEXTCInt),
        ("message_types", DebugUtilsMessageTypeFlagsEXTCInt),
        ("user_callback", PFN_xrDebugUtilsMessengerCallbackEXT),
        ("user_data", c_void_p),
    ]


PFN_xrSetDebugUtilsObjectNameEXT = CFUNCTYPE(Result.ctype(), InstanceHandle, POINTER(DebugUtilsObjectNameInfoEXT))

PFN_xrCreateDebugUtilsMessengerEXT = CFUNCTYPE(Result.ctype(), InstanceHandle, POINTER(DebugUtilsMessengerCreateInfoEXT), POINTER(DebugUtilsMessengerEXTHandle))

PFN_xrDestroyDebugUtilsMessengerEXT = CFUNCTYPE(Result.ctype(), DebugUtilsMessengerEXTHandle)

PFN_xrSubmitDebugUtilsMessageEXT = CFUNCTYPE(Result.ctype(), InstanceHandle, DebugUtilsMessageSeverityFlagsEXTCInt, DebugUtilsMessageTypeFlagsEXTCInt, POINTER(DebugUtilsMessengerCallbackDataEXT))

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
        return f"xr.SystemEyeGazeInteractionPropertiesEXT(supports_eye_gaze_interaction={repr(self.supports_eye_gaze_interaction)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SystemEyeGazeInteractionPropertiesEXT(supports_eye_gaze_interaction={self.supports_eye_gaze_interaction}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.EyeGazeSampleTimeEXT(time={repr(self.time)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.EyeGazeSampleTimeEXT(time={self.time}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("time", Time),
    ]


OverlaySessionCreateFlagsEXTXCInt = Flags64

OverlayMainSessionFlagsEXTXCInt = Flags64


class SessionCreateInfoOverlayEXTX(Structure):
    def __init__(
        self,
        create_flags: OverlaySessionCreateFlagsEXTX = OverlaySessionCreateFlagsEXTX(),
        session_layers_placement: int = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SESSION_CREATE_INFO_OVERLAY_EXTX,
    ) -> None:
        super().__init__(
            create_flags=OverlaySessionCreateFlagsEXTX(create_flags).value,
            session_layers_placement=session_layers_placement,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SessionCreateInfoOverlayEXTX(create_flags={repr(self.create_flags)}, session_layers_placement={repr(self.session_layers_placement)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SessionCreateInfoOverlayEXTX(create_flags={self.create_flags}, session_layers_placement={self.session_layers_placement}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("create_flags", OverlaySessionCreateFlagsEXTXCInt),
        ("session_layers_placement", c_uint32),
    ]


class EventDataMainSessionVisibilityChangedEXTX(Structure):
    def __init__(
        self,
        visible: Bool32 = 0,
        flags: OverlayMainSessionFlagsEXTX = OverlayMainSessionFlagsEXTX(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.EVENT_DATA_MAIN_SESSION_VISIBILITY_CHANGED_EXTX,
    ) -> None:
        super().__init__(
            visible=visible,
            flags=OverlayMainSessionFlagsEXTX(flags).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataMainSessionVisibilityChangedEXTX(visible={repr(self.visible)}, flags={repr(self.flags)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.EventDataMainSessionVisibilityChangedEXTX(visible={self.visible}, flags={self.flags}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("visible", Bool32),
        ("flags", OverlayMainSessionFlagsEXTXCInt),
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
        return f"xr.SpatialAnchorCreateInfoMSFT(space={repr(self.space)}, pose={repr(self.pose)}, time={repr(self.time)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorCreateInfoMSFT(space={self.space}, pose={self.pose}, time={self.time}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SpatialAnchorSpaceCreateInfoMSFT(anchor={repr(self.anchor)}, pose_in_anchor_space={repr(self.pose_in_anchor_space)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorSpaceCreateInfoMSFT(anchor={self.anchor}, pose_in_anchor_space={self.pose_in_anchor_space}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("anchor", SpatialAnchorMSFTHandle),
        ("pose_in_anchor_space", Posef),
    ]


PFN_xrCreateSpatialAnchorMSFT = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(SpatialAnchorCreateInfoMSFT), POINTER(SpatialAnchorMSFTHandle))

PFN_xrCreateSpatialAnchorSpaceMSFT = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(SpatialAnchorSpaceCreateInfoMSFT), POINTER(SpaceHandle))

PFN_xrDestroySpatialAnchorMSFT = CFUNCTYPE(Result.ctype(), SpatialAnchorMSFTHandle)

CompositionLayerImageLayoutFlagsFBCInt = Flags64


class CompositionLayerImageLayoutFB(Structure):
    def __init__(
        self,
        flags: CompositionLayerImageLayoutFlagsFB = CompositionLayerImageLayoutFlagsFB(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.COMPOSITION_LAYER_IMAGE_LAYOUT_FB,
    ) -> None:
        super().__init__(
            flags=CompositionLayerImageLayoutFlagsFB(flags).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerImageLayoutFB(flags={repr(self.flags)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerImageLayoutFB(flags={self.flags}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", CompositionLayerImageLayoutFlagsFBCInt),
    ]


class CompositionLayerAlphaBlendFB(Structure):
    def __init__(
        self,
        src_factor_color: BlendFactorFB = BlendFactorFB(),
        dst_factor_color: BlendFactorFB = BlendFactorFB(),
        src_factor_alpha: BlendFactorFB = BlendFactorFB(),
        dst_factor_alpha: BlendFactorFB = BlendFactorFB(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.COMPOSITION_LAYER_ALPHA_BLEND_FB,
    ) -> None:
        super().__init__(
            src_factor_color=BlendFactorFB(src_factor_color).value,
            dst_factor_color=BlendFactorFB(dst_factor_color).value,
            src_factor_alpha=BlendFactorFB(src_factor_alpha).value,
            dst_factor_alpha=BlendFactorFB(dst_factor_alpha).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerAlphaBlendFB(src_factor_color={repr(self.src_factor_color)}, dst_factor_color={repr(self.dst_factor_color)}, src_factor_alpha={repr(self.src_factor_alpha)}, dst_factor_alpha={repr(self.dst_factor_alpha)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerAlphaBlendFB(src_factor_color={self.src_factor_color}, dst_factor_color={self.dst_factor_color}, src_factor_alpha={self.src_factor_alpha}, dst_factor_alpha={self.dst_factor_alpha}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.ViewConfigurationDepthRangeEXT(recommended_near_z={repr(self.recommended_near_z)}, min_near_z={repr(self.min_near_z)}, recommended_far_z={repr(self.recommended_far_z)}, max_far_z={repr(self.max_far_z)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ViewConfigurationDepthRangeEXT(recommended_near_z={self.recommended_near_z:.3f}, min_near_z={self.min_near_z:.3f}, recommended_far_z={self.recommended_far_z:.3f}, max_far_z={self.max_far_z:.3f}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        node_type: SpatialGraphNodeTypeMSFT = SpatialGraphNodeTypeMSFT(),
        pose: Posef = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SPATIAL_GRAPH_NODE_SPACE_CREATE_INFO_MSFT,
    ) -> None:
        if pose is None:
            pose = Posef()
        super().__init__(
            node_type=SpatialGraphNodeTypeMSFT(node_type).value,
            pose=pose,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialGraphNodeSpaceCreateInfoMSFT(node_type={repr(self.node_type)}, node_id={repr(self.node_id)}, pose={repr(self.pose)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SpatialGraphNodeSpaceCreateInfoMSFT(node_type={self.node_type}, pose={self.pose}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SystemHandTrackingPropertiesEXT(supports_hand_tracking={repr(self.supports_hand_tracking)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SystemHandTrackingPropertiesEXT(supports_hand_tracking={self.supports_hand_tracking}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_hand_tracking", Bool32),
    ]


class HandTrackerCreateInfoEXT(Structure):
    def __init__(
        self,
        hand: HandEXT = HandEXT(),
        hand_joint_set: HandJointSetEXT = HandJointSetEXT(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.HAND_TRACKER_CREATE_INFO_EXT,
    ) -> None:
        super().__init__(
            hand=HandEXT(hand).value,
            hand_joint_set=HandJointSetEXT(hand_joint_set).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.HandTrackerCreateInfoEXT(hand={repr(self.hand)}, hand_joint_set={repr(self.hand_joint_set)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.HandTrackerCreateInfoEXT(hand={self.hand}, hand_joint_set={self.hand_joint_set}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.HandJointsLocateInfoEXT(base_space={repr(self.base_space)}, time={repr(self.time)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.HandJointsLocateInfoEXT(base_space={self.base_space}, time={self.time}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("base_space", SpaceHandle),
        ("time", Time),
    ]


class HandJointLocationEXT(Structure):
    def __init__(
        self,
        location_flags: SpaceLocationFlags = SpaceLocationFlags(),
        pose: Posef = None,
        radius: float = 0,
    ) -> None:
        if pose is None:
            pose = Posef()
        super().__init__(
            location_flags=SpaceLocationFlags(location_flags).value,
            pose=pose,
            radius=radius,
        )

    def __repr__(self) -> str:
        return f"xr.HandJointLocationEXT(location_flags={repr(self.location_flags)}, pose={repr(self.pose)}, radius={repr(self.radius)})"

    def __str__(self) -> str:
        return f"xr.HandJointLocationEXT(location_flags={self.location_flags}, pose={self.pose}, radius={self.radius:.3f})"

    _fields_ = [
        ("location_flags", SpaceLocationFlagsCInt),
        ("pose", Posef),
        ("radius", c_float),
    ]


class HandJointVelocityEXT(Structure):
    def __init__(
        self,
        velocity_flags: SpaceVelocityFlags = SpaceVelocityFlags(),
        linear_velocity: Vector3f = None,
        angular_velocity: Vector3f = None,
    ) -> None:
        if linear_velocity is None:
            linear_velocity = Vector3f()
        if angular_velocity is None:
            angular_velocity = Vector3f()
        super().__init__(
            velocity_flags=SpaceVelocityFlags(velocity_flags).value,
            linear_velocity=linear_velocity,
            angular_velocity=angular_velocity,
        )

    def __repr__(self) -> str:
        return f"xr.HandJointVelocityEXT(velocity_flags={repr(self.velocity_flags)}, linear_velocity={repr(self.linear_velocity)}, angular_velocity={repr(self.angular_velocity)})"

    def __str__(self) -> str:
        return f"xr.HandJointVelocityEXT(velocity_flags={self.velocity_flags}, linear_velocity={self.linear_velocity}, angular_velocity={self.angular_velocity})"

    _fields_ = [
        ("velocity_flags", SpaceVelocityFlagsCInt),
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
        return f"xr.HandJointLocationsEXT(is_active={repr(self.is_active)}, joint_count={repr(self.joint_count)}, joint_locations={repr(self.joint_locations)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.HandJointLocationsEXT(is_active={self.is_active}, joint_count={self.joint_count}, joint_locations={self.joint_locations}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.HandJointVelocitiesEXT(joint_count={repr(self.joint_count)}, joint_velocities={repr(self.joint_velocities)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.HandJointVelocitiesEXT(joint_count={self.joint_count}, joint_velocities={self.joint_velocities}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SystemHandTrackingMeshPropertiesMSFT(supports_hand_tracking_mesh={repr(self.supports_hand_tracking_mesh)}, max_hand_mesh_index_count={repr(self.max_hand_mesh_index_count)}, max_hand_mesh_vertex_count={repr(self.max_hand_mesh_vertex_count)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SystemHandTrackingMeshPropertiesMSFT(supports_hand_tracking_mesh={self.supports_hand_tracking_mesh}, max_hand_mesh_index_count={self.max_hand_mesh_index_count}, max_hand_mesh_vertex_count={self.max_hand_mesh_vertex_count}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        hand_pose_type: HandPoseTypeMSFT = HandPoseTypeMSFT(),
        pose_in_hand_mesh_space: Posef = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.HAND_MESH_SPACE_CREATE_INFO_MSFT,
    ) -> None:
        if pose_in_hand_mesh_space is None:
            pose_in_hand_mesh_space = Posef()
        super().__init__(
            hand_pose_type=HandPoseTypeMSFT(hand_pose_type).value,
            pose_in_hand_mesh_space=pose_in_hand_mesh_space,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.HandMeshSpaceCreateInfoMSFT(hand_pose_type={repr(self.hand_pose_type)}, pose_in_hand_mesh_space={repr(self.pose_in_hand_mesh_space)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.HandMeshSpaceCreateInfoMSFT(hand_pose_type={self.hand_pose_type}, pose_in_hand_mesh_space={self.pose_in_hand_mesh_space}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        hand_pose_type: HandPoseTypeMSFT = HandPoseTypeMSFT(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.HAND_MESH_UPDATE_INFO_MSFT,
    ) -> None:
        super().__init__(
            time=time,
            hand_pose_type=HandPoseTypeMSFT(hand_pose_type).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.HandMeshUpdateInfoMSFT(time={repr(self.time)}, hand_pose_type={repr(self.hand_pose_type)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.HandMeshUpdateInfoMSFT(time={self.time}, hand_pose_type={self.hand_pose_type}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.HandMeshIndexBufferMSFT(index_buffer_key={self.index_buffer_key}, index_capacity_input={self.index_capacity_input}, index_count_output={self.index_count_output}, indices={self.indices})"

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
        return f"xr.HandMeshVertexMSFT(position={self.position}, normal={self.normal})"

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
        return f"xr.HandMeshVertexBufferMSFT(vertex_update_time={self.vertex_update_time}, vertex_capacity_input={self.vertex_capacity_input}, vertex_count_output={self.vertex_count_output}, vertices={self.vertices})"

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
        return f"xr.HandMeshMSFT(is_active={repr(self.is_active)}, index_buffer_changed={repr(self.index_buffer_changed)}, vertex_buffer_changed={repr(self.vertex_buffer_changed)}, index_buffer={repr(self.index_buffer)}, vertex_buffer={repr(self.vertex_buffer)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.HandMeshMSFT(is_active={self.is_active}, index_buffer_changed={self.index_buffer_changed}, vertex_buffer_changed={self.vertex_buffer_changed}, index_buffer={self.index_buffer}, vertex_buffer={self.vertex_buffer}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        hand_pose_type: HandPoseTypeMSFT = HandPoseTypeMSFT(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.HAND_POSE_TYPE_INFO_MSFT,
    ) -> None:
        super().__init__(
            hand_pose_type=HandPoseTypeMSFT(hand_pose_type).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.HandPoseTypeInfoMSFT(hand_pose_type={repr(self.hand_pose_type)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.HandPoseTypeInfoMSFT(hand_pose_type={self.hand_pose_type}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SecondaryViewConfigurationSessionBeginInfoMSFT(view_configuration_count={repr(self.view_configuration_count)}, enabled_view_configuration_types={repr(self.enabled_view_configuration_types)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SecondaryViewConfigurationSessionBeginInfoMSFT(view_configuration_count={self.view_configuration_count}, enabled_view_configuration_types={self.enabled_view_configuration_types}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_configuration_count", c_uint32),
        ("enabled_view_configuration_types", POINTER(c_int)),
    ]


class SecondaryViewConfigurationStateMSFT(Structure):
    def __init__(
        self,
        view_configuration_type: ViewConfigurationType = ViewConfigurationType(),
        active: Bool32 = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SECONDARY_VIEW_CONFIGURATION_STATE_MSFT,
    ) -> None:
        super().__init__(
            view_configuration_type=ViewConfigurationType(view_configuration_type).value,
            active=active,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SecondaryViewConfigurationStateMSFT(view_configuration_type={repr(self.view_configuration_type)}, active={repr(self.active)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SecondaryViewConfigurationStateMSFT(view_configuration_type={self.view_configuration_type}, active={self.active}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SecondaryViewConfigurationFrameStateMSFT(view_configuration_count={repr(self.view_configuration_count)}, view_configuration_states={repr(self.view_configuration_states)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SecondaryViewConfigurationFrameStateMSFT(view_configuration_count={self.view_configuration_count}, view_configuration_states={self.view_configuration_states}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_configuration_count", c_uint32),
        ("view_configuration_states", POINTER(SecondaryViewConfigurationStateMSFT)),
    ]


class SecondaryViewConfigurationLayerInfoMSFT(Structure):
    def __init__(
        self,
        view_configuration_type: ViewConfigurationType = ViewConfigurationType(),
        environment_blend_mode: EnvironmentBlendMode = EnvironmentBlendMode(),
        layer_count: int = 0,
        layers: POINTER(POINTER(CompositionLayerBaseHeader)) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SECONDARY_VIEW_CONFIGURATION_LAYER_INFO_MSFT,
    ) -> None:
        super().__init__(
            view_configuration_type=ViewConfigurationType(view_configuration_type).value,
            environment_blend_mode=EnvironmentBlendMode(environment_blend_mode).value,
            layer_count=layer_count,
            layers=layers,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SecondaryViewConfigurationLayerInfoMSFT(view_configuration_type={repr(self.view_configuration_type)}, environment_blend_mode={repr(self.environment_blend_mode)}, layer_count={repr(self.layer_count)}, layers={repr(self.layers)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SecondaryViewConfigurationLayerInfoMSFT(view_configuration_type={self.view_configuration_type}, environment_blend_mode={self.environment_blend_mode}, layer_count={self.layer_count}, layers={self.layers}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SecondaryViewConfigurationFrameEndInfoMSFT(view_configuration_count={repr(self.view_configuration_count)}, view_configuration_layers_info={repr(self.view_configuration_layers_info)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SecondaryViewConfigurationFrameEndInfoMSFT(view_configuration_count={self.view_configuration_count}, view_configuration_layers_info={self.view_configuration_layers_info}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_configuration_count", c_uint32),
        ("view_configuration_layers_info", POINTER(SecondaryViewConfigurationLayerInfoMSFT)),
    ]


class SecondaryViewConfigurationSwapchainCreateInfoMSFT(Structure):
    def __init__(
        self,
        view_configuration_type: ViewConfigurationType = ViewConfigurationType(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SECONDARY_VIEW_CONFIGURATION_SWAPCHAIN_CREATE_INFO_MSFT,
    ) -> None:
        super().__init__(
            view_configuration_type=ViewConfigurationType(view_configuration_type).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SecondaryViewConfigurationSwapchainCreateInfoMSFT(view_configuration_type={repr(self.view_configuration_type)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SecondaryViewConfigurationSwapchainCreateInfoMSFT(view_configuration_type={self.view_configuration_type}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.ControllerModelKeyStateMSFT(model_key={repr(self.model_key)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ControllerModelKeyStateMSFT(model_key={self.model_key}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.ControllerModelNodePropertiesMSFT(parent_node_name={repr(self.parent_node_name)}, node_name={repr(self.node_name)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ControllerModelNodePropertiesMSFT(parent_node_name={self.parent_node_name}, node_name={self.node_name}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.ControllerModelPropertiesMSFT(node_capacity_input={repr(self.node_capacity_input)}, node_count_output={repr(self.node_count_output)}, node_properties={repr(self.node_properties)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ControllerModelPropertiesMSFT(node_capacity_input={self.node_capacity_input}, node_count_output={self.node_count_output}, node_properties={self.node_properties}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.ControllerModelNodeStateMSFT(node_pose={repr(self.node_pose)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ControllerModelNodeStateMSFT(node_pose={self.node_pose}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.ControllerModelStateMSFT(node_capacity_input={repr(self.node_capacity_input)}, node_count_output={repr(self.node_count_output)}, node_states={repr(self.node_states)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ControllerModelStateMSFT(node_capacity_input={self.node_capacity_input}, node_count_output={self.node_count_output}, node_states={self.node_states}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.ViewConfigurationViewFovEPIC(recommended_fov={repr(self.recommended_fov)}, max_mutable_fov={repr(self.max_mutable_fov)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ViewConfigurationViewFovEPIC(recommended_fov={self.recommended_fov}, max_mutable_fov={self.max_mutable_fov}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("recommended_fov", Fovf),
        ("max_mutable_fov", Fovf),
    ]


class CompositionLayerReprojectionInfoMSFT(Structure):
    def __init__(
        self,
        reprojection_mode: ReprojectionModeMSFT = ReprojectionModeMSFT(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.COMPOSITION_LAYER_REPROJECTION_INFO_MSFT,
    ) -> None:
        super().__init__(
            reprojection_mode=ReprojectionModeMSFT(reprojection_mode).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerReprojectionInfoMSFT(reprojection_mode={repr(self.reprojection_mode)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerReprojectionInfoMSFT(reprojection_mode={self.reprojection_mode}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.CompositionLayerReprojectionPlaneOverrideMSFT(position={repr(self.position)}, normal={repr(self.normal)}, velocity={repr(self.velocity)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerReprojectionPlaneOverrideMSFT(position={self.position}, normal={self.normal}, velocity={self.velocity}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SwapchainStateBaseHeaderFB(next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainStateBaseHeaderFB(next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


PFN_xrUpdateSwapchainFB = CFUNCTYPE(Result.ctype(), SwapchainHandle, POINTER(SwapchainStateBaseHeaderFB))

PFN_xrGetSwapchainStateFB = CFUNCTYPE(Result.ctype(), SwapchainHandle, POINTER(SwapchainStateBaseHeaderFB))

CompositionLayerSecureContentFlagsFBCInt = Flags64


class CompositionLayerSecureContentFB(Structure):
    def __init__(
        self,
        flags: CompositionLayerSecureContentFlagsFB = CompositionLayerSecureContentFlagsFB(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.COMPOSITION_LAYER_SECURE_CONTENT_FB,
    ) -> None:
        super().__init__(
            flags=CompositionLayerSecureContentFlagsFB(flags).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerSecureContentFB(flags={repr(self.flags)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerSecureContentFB(flags={self.flags}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", CompositionLayerSecureContentFlagsFBCInt),
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
        return f"xr.InteractionProfileAnalogThresholdVALVE(action={repr(self.action)}, binding={repr(self.binding)}, on_threshold={repr(self.on_threshold)}, off_threshold={repr(self.off_threshold)}, on_haptic={repr(self.on_haptic)}, off_haptic={repr(self.off_haptic)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.InteractionProfileAnalogThresholdVALVE(action={self.action}, binding={self.binding}, on_threshold={self.on_threshold:.3f}, off_threshold={self.off_threshold:.3f}, on_haptic={self.on_haptic}, off_haptic={self.off_haptic}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        hand_joints_motion_range: HandJointsMotionRangeEXT = HandJointsMotionRangeEXT(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.HAND_JOINTS_MOTION_RANGE_INFO_EXT,
    ) -> None:
        super().__init__(
            hand_joints_motion_range=HandJointsMotionRangeEXT(hand_joints_motion_range).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.HandJointsMotionRangeInfoEXT(hand_joints_motion_range={repr(self.hand_joints_motion_range)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.HandJointsMotionRangeInfoEXT(hand_joints_motion_range={self.hand_joints_motion_range}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.UuidMSFT()"

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
        return f"xr.SceneObserverCreateInfoMSFT(next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SceneObserverCreateInfoMSFT(next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SceneCreateInfoMSFT(next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SceneCreateInfoMSFT(next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SceneSphereBoundMSFT(center={self.center}, radius={self.radius:.3f})"

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
        return f"xr.SceneOrientedBoxBoundMSFT(pose={self.pose}, extents={self.extents})"

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
        return f"xr.SceneFrustumBoundMSFT(pose={self.pose}, fov={self.fov}, far_distance={self.far_distance:.3f})"

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
        return f"xr.SceneBoundsMSFT(space={self.space}, time={self.time}, sphere_count={self.sphere_count}, spheres={self.spheres}, box_count={self.box_count}, boxes={self.boxes}, frustum_count={self.frustum_count}, frustums={self.frustums})"

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
        consistency: SceneComputeConsistencyMSFT = SceneComputeConsistencyMSFT(),
        bounds: SceneBoundsMSFT = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.NEW_SCENE_COMPUTE_INFO_MSFT,
    ) -> None:
        if bounds is None:
            bounds = SceneBoundsMSFT()
        super().__init__(
            requested_feature_count=requested_feature_count,
            requested_features=requested_features,
            consistency=SceneComputeConsistencyMSFT(consistency).value,
            bounds=bounds,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.NewSceneComputeInfoMSFT(requested_feature_count={repr(self.requested_feature_count)}, requested_features={repr(self.requested_features)}, consistency={repr(self.consistency)}, bounds={repr(self.bounds)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.NewSceneComputeInfoMSFT(requested_feature_count={self.requested_feature_count}, requested_features={self.requested_features}, consistency={self.consistency}, bounds={self.bounds}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        lod: MeshComputeLodMSFT = MeshComputeLodMSFT(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.VISUAL_MESH_COMPUTE_LOD_INFO_MSFT,
    ) -> None:
        super().__init__(
            lod=MeshComputeLodMSFT(lod).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.VisualMeshComputeLodInfoMSFT(lod={repr(self.lod)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.VisualMeshComputeLodInfoMSFT(lod={self.lod}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("lod", MeshComputeLodMSFT.ctype()),
    ]


class SceneComponentMSFT(Structure):
    def __init__(
        self,
        component_type: SceneComponentTypeMSFT = SceneComponentTypeMSFT(),
        id: UuidMSFT = None,
        parent_id: UuidMSFT = None,
        update_time: Time = 0,
    ) -> None:
        if id is None:
            id = UuidMSFT()
        if parent_id is None:
            parent_id = UuidMSFT()
        super().__init__(
            component_type=SceneComponentTypeMSFT(component_type).value,
            id=id,
            parent_id=parent_id,
            update_time=update_time,
        )

    def __repr__(self) -> str:
        return f"xr.SceneComponentMSFT(component_type={repr(self.component_type)}, id={repr(self.id)}, parent_id={repr(self.parent_id)}, update_time={repr(self.update_time)})"

    def __str__(self) -> str:
        return f"xr.SceneComponentMSFT(component_type={self.component_type}, id={self.id}, parent_id={self.parent_id}, update_time={self.update_time})"

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
        return f"xr.SceneComponentsMSFT(component_capacity_input={repr(self.component_capacity_input)}, component_count_output={repr(self.component_count_output)}, components={repr(self.components)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SceneComponentsMSFT(component_capacity_input={self.component_capacity_input}, component_count_output={self.component_count_output}, components={self.components}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        component_type: SceneComponentTypeMSFT = SceneComponentTypeMSFT(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SCENE_COMPONENTS_GET_INFO_MSFT,
    ) -> None:
        super().__init__(
            component_type=SceneComponentTypeMSFT(component_type).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SceneComponentsGetInfoMSFT(component_type={repr(self.component_type)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SceneComponentsGetInfoMSFT(component_type={self.component_type}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("component_type", SceneComponentTypeMSFT.ctype()),
    ]


class SceneComponentLocationMSFT(Structure):
    def __init__(
        self,
        flags: SpaceLocationFlags = SpaceLocationFlags(),
        pose: Posef = None,
    ) -> None:
        if pose is None:
            pose = Posef()
        super().__init__(
            flags=SpaceLocationFlags(flags).value,
            pose=pose,
        )

    def __repr__(self) -> str:
        return f"xr.SceneComponentLocationMSFT(flags={repr(self.flags)}, pose={repr(self.pose)})"

    def __str__(self) -> str:
        return f"xr.SceneComponentLocationMSFT(flags={self.flags}, pose={self.pose})"

    _fields_ = [
        ("flags", SpaceLocationFlagsCInt),
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
        return f"xr.SceneComponentLocationsMSFT(location_count={repr(self.location_count)}, locations={repr(self.locations)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SceneComponentLocationsMSFT(location_count={self.location_count}, locations={self.locations}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SceneComponentsLocateInfoMSFT(base_space={repr(self.base_space)}, time={repr(self.time)}, component_id_count={repr(self.component_id_count)}, component_ids={repr(self.component_ids)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SceneComponentsLocateInfoMSFT(base_space={self.base_space}, time={self.time}, component_id_count={self.component_id_count}, component_ids={self.component_ids}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        object_type: SceneObjectTypeMSFT = SceneObjectTypeMSFT(),
    ) -> None:
        super().__init__(
            object_type=SceneObjectTypeMSFT(object_type).value,
        )

    def __repr__(self) -> str:
        return f"xr.SceneObjectMSFT(object_type={repr(self.object_type)})"

    def __str__(self) -> str:
        return f"xr.SceneObjectMSFT(object_type={self.object_type})"

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
        return f"xr.SceneObjectsMSFT(scene_object_count={repr(self.scene_object_count)}, scene_objects={repr(self.scene_objects)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SceneObjectsMSFT(scene_object_count={self.scene_object_count}, scene_objects={self.scene_objects}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SceneComponentParentFilterInfoMSFT(parent_id={repr(self.parent_id)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SceneComponentParentFilterInfoMSFT(parent_id={self.parent_id}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SceneObjectTypesFilterInfoMSFT(object_type_count={repr(self.object_type_count)}, object_types={repr(self.object_types)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SceneObjectTypesFilterInfoMSFT(object_type_count={self.object_type_count}, object_types={self.object_types}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("object_type_count", c_uint32),
        ("object_types", POINTER(c_int)),
    ]


class ScenePlaneMSFT(Structure):
    def __init__(
        self,
        alignment: ScenePlaneAlignmentTypeMSFT = ScenePlaneAlignmentTypeMSFT(),
        size: Extent2Df = None,
        mesh_buffer_id: int = 0,
        supports_indices_uint16: Bool32 = 0,
    ) -> None:
        if size is None:
            size = Extent2Df()
        super().__init__(
            alignment=ScenePlaneAlignmentTypeMSFT(alignment).value,
            size=size,
            mesh_buffer_id=mesh_buffer_id,
            supports_indices_uint16=supports_indices_uint16,
        )

    def __repr__(self) -> str:
        return f"xr.ScenePlaneMSFT(alignment={repr(self.alignment)}, size={repr(self.size)}, mesh_buffer_id={repr(self.mesh_buffer_id)}, supports_indices_uint16={repr(self.supports_indices_uint16)})"

    def __str__(self) -> str:
        return f"xr.ScenePlaneMSFT(alignment={self.alignment}, size={self.size}, mesh_buffer_id={self.mesh_buffer_id}, supports_indices_uint16={self.supports_indices_uint16})"

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
        return f"xr.ScenePlanesMSFT(scene_plane_count={repr(self.scene_plane_count)}, scene_planes={repr(self.scene_planes)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ScenePlanesMSFT(scene_plane_count={self.scene_plane_count}, scene_planes={self.scene_planes}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.ScenePlaneAlignmentFilterInfoMSFT(alignment_count={repr(self.alignment_count)}, alignments={repr(self.alignments)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ScenePlaneAlignmentFilterInfoMSFT(alignment_count={self.alignment_count}, alignments={self.alignments}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SceneMeshMSFT(mesh_buffer_id={self.mesh_buffer_id}, supports_indices_uint16={self.supports_indices_uint16})"

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
        return f"xr.SceneMeshesMSFT(scene_mesh_count={repr(self.scene_mesh_count)}, scene_meshes={repr(self.scene_meshes)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SceneMeshesMSFT(scene_mesh_count={self.scene_mesh_count}, scene_meshes={self.scene_meshes}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SceneMeshBuffersGetInfoMSFT(mesh_buffer_id={repr(self.mesh_buffer_id)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SceneMeshBuffersGetInfoMSFT(mesh_buffer_id={self.mesh_buffer_id}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SceneMeshBuffersMSFT(next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SceneMeshBuffersMSFT(next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SceneMeshVertexBufferMSFT(vertex_capacity_input={repr(self.vertex_capacity_input)}, vertex_count_output={repr(self.vertex_count_output)}, vertices={repr(self.vertices)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SceneMeshVertexBufferMSFT(vertex_capacity_input={self.vertex_capacity_input}, vertex_count_output={self.vertex_count_output}, vertices={self.vertices}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SceneMeshIndicesUint32MSFT(index_capacity_input={repr(self.index_capacity_input)}, index_count_output={repr(self.index_count_output)}, indices={repr(self.indices)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SceneMeshIndicesUint32MSFT(index_capacity_input={self.index_capacity_input}, index_count_output={self.index_count_output}, indices={self.indices}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SceneMeshIndicesUint16MSFT(index_capacity_input={repr(self.index_capacity_input)}, index_count_output={repr(self.index_count_output)}, indices={repr(self.indices)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SceneMeshIndicesUint16MSFT(index_capacity_input={self.index_capacity_input}, index_count_output={self.index_count_output}, indices={self.indices}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SerializedSceneFragmentDataGetInfoMSFT(scene_fragment_id={repr(self.scene_fragment_id)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SerializedSceneFragmentDataGetInfoMSFT(scene_fragment_id={self.scene_fragment_id}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.DeserializeSceneFragmentMSFT(buffer_size={self.buffer_size}, buffer={self.buffer})"

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
        return f"xr.SceneDeserializeInfoMSFT(fragment_count={repr(self.fragment_count)}, fragments={repr(self.fragments)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SceneDeserializeInfoMSFT(fragment_count={self.fragment_count}, fragments={self.fragments}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.EventDataDisplayRefreshRateChangedFB(from_display_refresh_rate={repr(self.from_display_refresh_rate)}, to_display_refresh_rate={repr(self.to_display_refresh_rate)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.EventDataDisplayRefreshRateChangedFB(from_display_refresh_rate={self.from_display_refresh_rate:.3f}, to_display_refresh_rate={self.to_display_refresh_rate:.3f}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("from_display_refresh_rate", c_float),
        ("to_display_refresh_rate", c_float),
    ]


PFN_xrEnumerateDisplayRefreshRatesFB = CFUNCTYPE(Result.ctype(), SessionHandle, c_uint32, POINTER(c_uint32), POINTER(c_float))

PFN_xrGetDisplayRefreshRateFB = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(c_float))

PFN_xrRequestDisplayRefreshRateFB = CFUNCTYPE(Result.ctype(), SessionHandle, c_float)


class ViveTrackerPathsHTCX(Structure):
    def __init__(
        self,
        persistent_path: Path = 0,
        role_path: Path = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.VIVE_TRACKER_PATHS_HTCX,
    ) -> None:
        super().__init__(
            persistent_path=persistent_path,
            role_path=role_path,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.ViveTrackerPathsHTCX(persistent_path={repr(self.persistent_path)}, role_path={repr(self.role_path)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ViveTrackerPathsHTCX(persistent_path={self.persistent_path}, role_path={self.role_path}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("persistent_path", Path),
        ("role_path", Path),
    ]


class EventDataViveTrackerConnectedHTCX(Structure):
    def __init__(
        self,
        paths: POINTER(ViveTrackerPathsHTCX) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.EVENT_DATA_VIVE_TRACKER_CONNECTED_HTCX,
    ) -> None:
        super().__init__(
            paths=paths,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataViveTrackerConnectedHTCX(paths={repr(self.paths)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.EventDataViveTrackerConnectedHTCX(paths={self.paths}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("paths", POINTER(ViveTrackerPathsHTCX)),
    ]


PFN_xrEnumerateViveTrackerPathsHTCX = CFUNCTYPE(Result.ctype(), InstanceHandle, c_uint32, POINTER(c_uint32), POINTER(ViveTrackerPathsHTCX))


class FacialTrackerHTC_T(Structure):
    pass


FacialTrackerHTCHandle = POINTER(FacialTrackerHTC_T)


class SystemFacialTrackingPropertiesHTC(Structure):
    def __init__(
        self,
        support_eye_facial_tracking: Bool32 = 0,
        support_lip_facial_tracking: Bool32 = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SYSTEM_FACIAL_TRACKING_PROPERTIES_HTC,
    ) -> None:
        super().__init__(
            support_eye_facial_tracking=support_eye_facial_tracking,
            support_lip_facial_tracking=support_lip_facial_tracking,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SystemFacialTrackingPropertiesHTC(support_eye_facial_tracking={repr(self.support_eye_facial_tracking)}, support_lip_facial_tracking={repr(self.support_lip_facial_tracking)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SystemFacialTrackingPropertiesHTC(support_eye_facial_tracking={self.support_eye_facial_tracking}, support_lip_facial_tracking={self.support_lip_facial_tracking}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("support_eye_facial_tracking", Bool32),
        ("support_lip_facial_tracking", Bool32),
    ]


class FacialExpressionsHTC(Structure):
    def __init__(
        self,
        is_active: Bool32 = 0,
        sample_time: Time = 0,
        expression_count: int = 0,
        expression_weightings: POINTER(c_float) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.FACIAL_EXPRESSIONS_HTC,
    ) -> None:
        super().__init__(
            is_active=is_active,
            sample_time=sample_time,
            expression_count=expression_count,
            expression_weightings=expression_weightings,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.FacialExpressionsHTC(is_active={repr(self.is_active)}, sample_time={repr(self.sample_time)}, expression_count={repr(self.expression_count)}, expression_weightings={repr(self.expression_weightings)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.FacialExpressionsHTC(is_active={self.is_active}, sample_time={self.sample_time}, expression_count={self.expression_count}, expression_weightings={self.expression_weightings}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("is_active", Bool32),
        ("sample_time", Time),
        ("expression_count", c_uint32),
        ("expression_weightings", POINTER(c_float)),
    ]


class FacialTrackerCreateInfoHTC(Structure):
    def __init__(
        self,
        facial_tracking_type: FacialTrackingTypeHTC = FacialTrackingTypeHTC(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.FACIAL_TRACKER_CREATE_INFO_HTC,
    ) -> None:
        super().__init__(
            facial_tracking_type=FacialTrackingTypeHTC(facial_tracking_type).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.FacialTrackerCreateInfoHTC(facial_tracking_type={repr(self.facial_tracking_type)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.FacialTrackerCreateInfoHTC(facial_tracking_type={self.facial_tracking_type}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("facial_tracking_type", FacialTrackingTypeHTC.ctype()),
    ]


PFN_xrCreateFacialTrackerHTC = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(FacialTrackerCreateInfoHTC), POINTER(FacialTrackerHTCHandle))

PFN_xrDestroyFacialTrackerHTC = CFUNCTYPE(Result.ctype(), FacialTrackerHTCHandle)

PFN_xrGetFacialExpressionsHTC = CFUNCTYPE(Result.ctype(), FacialTrackerHTCHandle, POINTER(FacialExpressionsHTC))


class SystemColorSpacePropertiesFB(Structure):
    def __init__(
        self,
        color_space: ColorSpaceFB = ColorSpaceFB(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SYSTEM_COLOR_SPACE_PROPERTIES_FB,
    ) -> None:
        super().__init__(
            color_space=ColorSpaceFB(color_space).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SystemColorSpacePropertiesFB(color_space={repr(self.color_space)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SystemColorSpacePropertiesFB(color_space={self.color_space}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.Vector4sFB(x={self.x}, y={self.y}, z={self.z}, w={self.w})"

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
        return f"xr.HandTrackingMeshFB(joint_capacity_input={repr(self.joint_capacity_input)}, joint_count_output={repr(self.joint_count_output)}, joint_bind_poses={repr(self.joint_bind_poses)}, joint_radii={repr(self.joint_radii)}, joint_parents={repr(self.joint_parents)}, vertex_capacity_input={repr(self.vertex_capacity_input)}, vertex_count_output={repr(self.vertex_count_output)}, vertex_positions={repr(self.vertex_positions)}, vertex_normals={repr(self.vertex_normals)}, vertex_uvs={repr(self.vertex_uvs)}, vertex_blend_indices={repr(self.vertex_blend_indices)}, vertex_blend_weights={repr(self.vertex_blend_weights)}, index_capacity_input={repr(self.index_capacity_input)}, index_count_output={repr(self.index_count_output)}, indices={repr(self.indices)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.HandTrackingMeshFB(joint_capacity_input={self.joint_capacity_input}, joint_count_output={self.joint_count_output}, joint_bind_poses={self.joint_bind_poses}, joint_radii={self.joint_radii}, joint_parents={self.joint_parents}, vertex_capacity_input={self.vertex_capacity_input}, vertex_count_output={self.vertex_count_output}, vertex_positions={self.vertex_positions}, vertex_normals={self.vertex_normals}, vertex_uvs={self.vertex_uvs}, vertex_blend_indices={self.vertex_blend_indices}, vertex_blend_weights={self.vertex_blend_weights}, index_capacity_input={self.index_capacity_input}, index_count_output={self.index_count_output}, indices={self.indices}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.HandTrackingScaleFB(sensor_output={repr(self.sensor_output)}, current_output={repr(self.current_output)}, override_hand_scale={repr(self.override_hand_scale)}, override_value_input={repr(self.override_value_input)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.HandTrackingScaleFB(sensor_output={self.sensor_output:.3f}, current_output={self.current_output:.3f}, override_hand_scale={self.override_hand_scale}, override_value_input={self.override_value_input:.3f}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("sensor_output", c_float),
        ("current_output", c_float),
        ("override_hand_scale", Bool32),
        ("override_value_input", c_float),
    ]


PFN_xrGetHandMeshFB = CFUNCTYPE(Result.ctype(), HandTrackerEXTHandle, POINTER(HandTrackingMeshFB))

HandTrackingAimFlagsFBCInt = Flags64


class HandTrackingAimStateFB(Structure):
    def __init__(
        self,
        status: HandTrackingAimFlagsFB = HandTrackingAimFlagsFB(),
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
            status=HandTrackingAimFlagsFB(status).value,
            aim_pose=aim_pose,
            pinch_strength_index=pinch_strength_index,
            pinch_strength_middle=pinch_strength_middle,
            pinch_strength_ring=pinch_strength_ring,
            pinch_strength_little=pinch_strength_little,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.HandTrackingAimStateFB(status={repr(self.status)}, aim_pose={repr(self.aim_pose)}, pinch_strength_index={repr(self.pinch_strength_index)}, pinch_strength_middle={repr(self.pinch_strength_middle)}, pinch_strength_ring={repr(self.pinch_strength_ring)}, pinch_strength_little={repr(self.pinch_strength_little)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.HandTrackingAimStateFB(status={self.status}, aim_pose={self.aim_pose}, pinch_strength_index={self.pinch_strength_index:.3f}, pinch_strength_middle={self.pinch_strength_middle:.3f}, pinch_strength_ring={self.pinch_strength_ring:.3f}, pinch_strength_little={self.pinch_strength_little:.3f}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("status", HandTrackingAimFlagsFBCInt),
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
        joint: HandJointEXT = HandJointEXT(),
    ) -> None:
        super().__init__(
            radius=radius,
            joint=HandJointEXT(joint).value,
        )

    def __repr__(self) -> str:
        return f"xr.HandCapsuleFB(points={repr(self.points)}, radius={repr(self.radius)}, joint={repr(self.joint)})"

    def __str__(self) -> str:
        return f"xr.HandCapsuleFB(radius={self.radius:.3f}, joint={self.joint})"

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
        return f"xr.HandTrackingCapsulesStateFB(capsules={repr(self.capsules)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.HandTrackingCapsulesStateFB(next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("capsules", (HandCapsuleFB * 19)),
    ]


class FoveationProfileFB_T(Structure):
    pass


FoveationProfileFBHandle = POINTER(FoveationProfileFB_T)

SwapchainCreateFoveationFlagsFBCInt = Flags64

SwapchainStateFoveationFlagsFBCInt = Flags64


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
        return f"xr.FoveationProfileCreateInfoFB(next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.FoveationProfileCreateInfoFB(next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SwapchainCreateInfoFoveationFB(Structure):
    def __init__(
        self,
        flags: SwapchainCreateFoveationFlagsFB = SwapchainCreateFoveationFlagsFB(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SWAPCHAIN_CREATE_INFO_FOVEATION_FB,
    ) -> None:
        super().__init__(
            flags=SwapchainCreateFoveationFlagsFB(flags).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainCreateInfoFoveationFB(flags={repr(self.flags)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainCreateInfoFoveationFB(flags={self.flags}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", SwapchainCreateFoveationFlagsFBCInt),
    ]


class SwapchainStateFoveationFB(Structure):
    def __init__(
        self,
        flags: SwapchainStateFoveationFlagsFB = SwapchainStateFoveationFlagsFB(),
        profile: FoveationProfileFBHandle = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SWAPCHAIN_STATE_FOVEATION_FB,
    ) -> None:
        super().__init__(
            flags=SwapchainStateFoveationFlagsFB(flags).value,
            profile=profile,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainStateFoveationFB(flags={repr(self.flags)}, profile={repr(self.profile)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainStateFoveationFB(flags={self.flags}, profile={self.profile}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", SwapchainStateFoveationFlagsFBCInt),
        ("profile", FoveationProfileFBHandle),
    ]


PFN_xrCreateFoveationProfileFB = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(FoveationProfileCreateInfoFB), POINTER(FoveationProfileFBHandle))

PFN_xrDestroyFoveationProfileFB = CFUNCTYPE(Result.ctype(), FoveationProfileFBHandle)


class FoveationLevelProfileCreateInfoFB(Structure):
    def __init__(
        self,
        level: FoveationLevelFB = FoveationLevelFB(),
        vertical_offset: float = 0,
        dynamic: FoveationDynamicFB = FoveationDynamicFB(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.FOVEATION_LEVEL_PROFILE_CREATE_INFO_FB,
    ) -> None:
        super().__init__(
            level=FoveationLevelFB(level).value,
            vertical_offset=vertical_offset,
            dynamic=FoveationDynamicFB(dynamic).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.FoveationLevelProfileCreateInfoFB(level={repr(self.level)}, vertical_offset={repr(self.vertical_offset)}, dynamic={repr(self.dynamic)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.FoveationLevelProfileCreateInfoFB(level={self.level}, vertical_offset={self.vertical_offset:.3f}, dynamic={self.dynamic}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("level", FoveationLevelFB.ctype()),
        ("vertical_offset", c_float),
        ("dynamic", FoveationDynamicFB.ctype()),
    ]


KeyboardTrackingFlagsFBCInt = Flags64

KeyboardTrackingQueryFlagsFBCInt = Flags64


class SystemKeyboardTrackingPropertiesFB(Structure):
    def __init__(
        self,
        supports_keyboard_tracking: Bool32 = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SYSTEM_KEYBOARD_TRACKING_PROPERTIES_FB,
    ) -> None:
        super().__init__(
            supports_keyboard_tracking=supports_keyboard_tracking,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SystemKeyboardTrackingPropertiesFB(supports_keyboard_tracking={repr(self.supports_keyboard_tracking)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SystemKeyboardTrackingPropertiesFB(supports_keyboard_tracking={self.supports_keyboard_tracking}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_keyboard_tracking", Bool32),
    ]


class KeyboardTrackingDescriptionFB(Structure):
    def __init__(
        self,
        tracked_keyboard_id: int = 0,
        size: Vector3f = None,
        flags: KeyboardTrackingFlagsFB = KeyboardTrackingFlagsFB(),
        name: str = "",
    ) -> None:
        if size is None:
            size = Vector3f()
        super().__init__(
            tracked_keyboard_id=tracked_keyboard_id,
            size=size,
            flags=KeyboardTrackingFlagsFB(flags).value,
            name=name.encode(),
        )

    def __repr__(self) -> str:
        return f"xr.KeyboardTrackingDescriptionFB(tracked_keyboard_id={repr(self.tracked_keyboard_id)}, size={repr(self.size)}, flags={repr(self.flags)}, name={repr(self.name)})"

    def __str__(self) -> str:
        return f"xr.KeyboardTrackingDescriptionFB(tracked_keyboard_id={self.tracked_keyboard_id}, size={self.size}, flags={self.flags}, name={self.name})"

    _fields_ = [
        ("tracked_keyboard_id", c_uint64),
        ("size", Vector3f),
        ("flags", KeyboardTrackingFlagsFBCInt),
        ("name", (c_char * 128)),
    ]


class KeyboardSpaceCreateInfoFB(Structure):
    def __init__(
        self,
        tracked_keyboard_id: int = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.KEYBOARD_SPACE_CREATE_INFO_FB,
    ) -> None:
        super().__init__(
            tracked_keyboard_id=tracked_keyboard_id,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.KeyboardSpaceCreateInfoFB(tracked_keyboard_id={repr(self.tracked_keyboard_id)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.KeyboardSpaceCreateInfoFB(tracked_keyboard_id={self.tracked_keyboard_id}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("tracked_keyboard_id", c_uint64),
    ]


class KeyboardTrackingQueryFB(Structure):
    def __init__(
        self,
        flags: KeyboardTrackingQueryFlagsFB = KeyboardTrackingQueryFlagsFB(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.KEYBOARD_TRACKING_QUERY_FB,
    ) -> None:
        super().__init__(
            flags=KeyboardTrackingQueryFlagsFB(flags).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.KeyboardTrackingQueryFB(flags={repr(self.flags)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.KeyboardTrackingQueryFB(flags={self.flags}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", KeyboardTrackingQueryFlagsFBCInt),
    ]


PFN_xrQuerySystemTrackedKeyboardFB = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(KeyboardTrackingQueryFB), POINTER(KeyboardTrackingDescriptionFB))

PFN_xrCreateKeyboardSpaceFB = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(KeyboardSpaceCreateInfoFB), POINTER(SpaceHandle))


class TriangleMeshFB_T(Structure):
    pass


TriangleMeshFBHandle = POINTER(TriangleMeshFB_T)

TriangleMeshFlagsFBCInt = Flags64


class TriangleMeshCreateInfoFB(Structure):
    def __init__(
        self,
        flags: TriangleMeshFlagsFB = TriangleMeshFlagsFB(),
        winding_order: WindingOrderFB = WindingOrderFB(),
        vertex_count: int = 0,
        vertex_buffer: POINTER(Vector3f) = None,
        triangle_count: int = 0,
        index_buffer: POINTER(c_uint32) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.TRIANGLE_MESH_CREATE_INFO_FB,
    ) -> None:
        super().__init__(
            flags=TriangleMeshFlagsFB(flags).value,
            winding_order=WindingOrderFB(winding_order).value,
            vertex_count=vertex_count,
            vertex_buffer=vertex_buffer,
            triangle_count=triangle_count,
            index_buffer=index_buffer,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.TriangleMeshCreateInfoFB(flags={repr(self.flags)}, winding_order={repr(self.winding_order)}, vertex_count={repr(self.vertex_count)}, vertex_buffer={repr(self.vertex_buffer)}, triangle_count={repr(self.triangle_count)}, index_buffer={repr(self.index_buffer)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.TriangleMeshCreateInfoFB(flags={self.flags}, winding_order={self.winding_order}, vertex_count={self.vertex_count}, vertex_buffer={self.vertex_buffer}, triangle_count={self.triangle_count}, index_buffer={self.index_buffer}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", TriangleMeshFlagsFBCInt),
        ("winding_order", WindingOrderFB.ctype()),
        ("vertex_count", c_uint32),
        ("vertex_buffer", POINTER(Vector3f)),
        ("triangle_count", c_uint32),
        ("index_buffer", POINTER(c_uint32)),
    ]


PFN_xrCreateTriangleMeshFB = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(TriangleMeshCreateInfoFB), POINTER(TriangleMeshFBHandle))

PFN_xrDestroyTriangleMeshFB = CFUNCTYPE(Result.ctype(), TriangleMeshFBHandle)

PFN_xrTriangleMeshGetVertexBufferFB = CFUNCTYPE(Result.ctype(), TriangleMeshFBHandle, POINTER(POINTER(Vector3f)))

PFN_xrTriangleMeshGetIndexBufferFB = CFUNCTYPE(Result.ctype(), TriangleMeshFBHandle, POINTER(POINTER(c_uint32)))

PFN_xrTriangleMeshBeginUpdateFB = CFUNCTYPE(Result.ctype(), TriangleMeshFBHandle)

PFN_xrTriangleMeshEndUpdateFB = CFUNCTYPE(Result.ctype(), TriangleMeshFBHandle, c_uint32, c_uint32)

PFN_xrTriangleMeshBeginVertexBufferUpdateFB = CFUNCTYPE(Result.ctype(), TriangleMeshFBHandle, POINTER(c_uint32))

PFN_xrTriangleMeshEndVertexBufferUpdateFB = CFUNCTYPE(Result.ctype(), TriangleMeshFBHandle)


class PassthroughFB_T(Structure):
    pass


PassthroughFBHandle = POINTER(PassthroughFB_T)


class PassthroughLayerFB_T(Structure):
    pass


PassthroughLayerFBHandle = POINTER(PassthroughLayerFB_T)


class GeometryInstanceFB_T(Structure):
    pass


GeometryInstanceFBHandle = POINTER(GeometryInstanceFB_T)

PassthroughFlagsFBCInt = Flags64

PassthroughStateChangedFlagsFBCInt = Flags64


class SystemPassthroughPropertiesFB(Structure):
    def __init__(
        self,
        supports_passthrough: Bool32 = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SYSTEM_PASSTHROUGH_PROPERTIES_FB,
    ) -> None:
        super().__init__(
            supports_passthrough=supports_passthrough,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SystemPassthroughPropertiesFB(supports_passthrough={repr(self.supports_passthrough)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SystemPassthroughPropertiesFB(supports_passthrough={self.supports_passthrough}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_passthrough", Bool32),
    ]


class PassthroughCreateInfoFB(Structure):
    def __init__(
        self,
        flags: PassthroughFlagsFB = PassthroughFlagsFB(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.PASSTHROUGH_CREATE_INFO_FB,
    ) -> None:
        super().__init__(
            flags=PassthroughFlagsFB(flags).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.PassthroughCreateInfoFB(flags={repr(self.flags)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.PassthroughCreateInfoFB(flags={self.flags}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", PassthroughFlagsFBCInt),
    ]


class PassthroughLayerCreateInfoFB(Structure):
    def __init__(
        self,
        passthrough: PassthroughFBHandle = None,
        flags: PassthroughFlagsFB = PassthroughFlagsFB(),
        purpose: PassthroughLayerPurposeFB = PassthroughLayerPurposeFB(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.PASSTHROUGH_LAYER_CREATE_INFO_FB,
    ) -> None:
        super().__init__(
            passthrough=passthrough,
            flags=PassthroughFlagsFB(flags).value,
            purpose=PassthroughLayerPurposeFB(purpose).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.PassthroughLayerCreateInfoFB(passthrough={repr(self.passthrough)}, flags={repr(self.flags)}, purpose={repr(self.purpose)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.PassthroughLayerCreateInfoFB(passthrough={self.passthrough}, flags={self.flags}, purpose={self.purpose}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("passthrough", PassthroughFBHandle),
        ("flags", PassthroughFlagsFBCInt),
        ("purpose", PassthroughLayerPurposeFB.ctype()),
    ]


class CompositionLayerPassthroughFB(Structure):
    def __init__(
        self,
        flags: CompositionLayerFlags = CompositionLayerFlags(),
        space: SpaceHandle = None,
        layer_handle: PassthroughLayerFBHandle = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.COMPOSITION_LAYER_PASSTHROUGH_FB,
    ) -> None:
        super().__init__(
            flags=CompositionLayerFlags(flags).value,
            space=space,
            layer_handle=layer_handle,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerPassthroughFB(flags={repr(self.flags)}, space={repr(self.space)}, layer_handle={repr(self.layer_handle)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerPassthroughFB(flags={self.flags}, space={self.space}, layer_handle={self.layer_handle}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", CompositionLayerFlagsCInt),
        ("space", SpaceHandle),
        ("layer_handle", PassthroughLayerFBHandle),
    ]


class GeometryInstanceCreateInfoFB(Structure):
    def __init__(
        self,
        layer: PassthroughLayerFBHandle = None,
        mesh: TriangleMeshFBHandle = None,
        base_space: SpaceHandle = None,
        pose: Posef = None,
        scale: Vector3f = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.GEOMETRY_INSTANCE_CREATE_INFO_FB,
    ) -> None:
        if pose is None:
            pose = Posef()
        if scale is None:
            scale = Vector3f()
        super().__init__(
            layer=layer,
            mesh=mesh,
            base_space=base_space,
            pose=pose,
            scale=scale,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.GeometryInstanceCreateInfoFB(layer={repr(self.layer)}, mesh={repr(self.mesh)}, base_space={repr(self.base_space)}, pose={repr(self.pose)}, scale={repr(self.scale)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.GeometryInstanceCreateInfoFB(layer={self.layer}, mesh={self.mesh}, base_space={self.base_space}, pose={self.pose}, scale={self.scale}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer", PassthroughLayerFBHandle),
        ("mesh", TriangleMeshFBHandle),
        ("base_space", SpaceHandle),
        ("pose", Posef),
        ("scale", Vector3f),
    ]


class GeometryInstanceTransformFB(Structure):
    def __init__(
        self,
        base_space: SpaceHandle = None,
        time: Time = 0,
        pose: Posef = None,
        scale: Vector3f = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.GEOMETRY_INSTANCE_TRANSFORM_FB,
    ) -> None:
        if pose is None:
            pose = Posef()
        if scale is None:
            scale = Vector3f()
        super().__init__(
            base_space=base_space,
            time=time,
            pose=pose,
            scale=scale,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.GeometryInstanceTransformFB(base_space={repr(self.base_space)}, time={repr(self.time)}, pose={repr(self.pose)}, scale={repr(self.scale)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.GeometryInstanceTransformFB(base_space={self.base_space}, time={self.time}, pose={self.pose}, scale={self.scale}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("base_space", SpaceHandle),
        ("time", Time),
        ("pose", Posef),
        ("scale", Vector3f),
    ]


class PassthroughStyleFB(Structure):
    def __init__(
        self,
        texture_opacity_factor: float = 0,
        edge_color: Color4f = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.PASSTHROUGH_STYLE_FB,
    ) -> None:
        if edge_color is None:
            edge_color = Color4f()
        super().__init__(
            texture_opacity_factor=texture_opacity_factor,
            edge_color=edge_color,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.PassthroughStyleFB(texture_opacity_factor={repr(self.texture_opacity_factor)}, edge_color={repr(self.edge_color)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.PassthroughStyleFB(texture_opacity_factor={self.texture_opacity_factor:.3f}, edge_color={self.edge_color}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("texture_opacity_factor", c_float),
        ("edge_color", Color4f),
    ]


class PassthroughColorMapMonoToRgbaFB(Structure):
    def __init__(
        self,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.PASSTHROUGH_COLOR_MAP_MONO_TO_RGBA_FB,
    ) -> None:
        super().__init__(
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.PassthroughColorMapMonoToRgbaFB(texture_color_map={repr(self.texture_color_map)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.PassthroughColorMapMonoToRgbaFB(next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("texture_color_map", (Color4f * 256)),
    ]


class PassthroughColorMapMonoToMonoFB(Structure):
    def __init__(
        self,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.PASSTHROUGH_COLOR_MAP_MONO_TO_MONO_FB,
    ) -> None:
        super().__init__(
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.PassthroughColorMapMonoToMonoFB(texture_color_map={repr(self.texture_color_map)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.PassthroughColorMapMonoToMonoFB(next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("texture_color_map", (c_uint8 * 256)),
    ]


class EventDataPassthroughStateChangedFB(Structure):
    def __init__(
        self,
        flags: PassthroughStateChangedFlagsFB = PassthroughStateChangedFlagsFB(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.EVENT_DATA_PASSTHROUGH_STATE_CHANGED_FB,
    ) -> None:
        super().__init__(
            flags=PassthroughStateChangedFlagsFB(flags).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataPassthroughStateChangedFB(flags={repr(self.flags)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.EventDataPassthroughStateChangedFB(flags={self.flags}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", PassthroughStateChangedFlagsFBCInt),
    ]


PFN_xrCreatePassthroughFB = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(PassthroughCreateInfoFB), POINTER(PassthroughFBHandle))

PFN_xrDestroyPassthroughFB = CFUNCTYPE(Result.ctype(), PassthroughFBHandle)

PFN_xrPassthroughStartFB = CFUNCTYPE(Result.ctype(), PassthroughFBHandle)

PFN_xrPassthroughPauseFB = CFUNCTYPE(Result.ctype(), PassthroughFBHandle)

PFN_xrCreatePassthroughLayerFB = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(PassthroughLayerCreateInfoFB), POINTER(PassthroughLayerFBHandle))

PFN_xrDestroyPassthroughLayerFB = CFUNCTYPE(Result.ctype(), PassthroughLayerFBHandle)

PFN_xrPassthroughLayerPauseFB = CFUNCTYPE(Result.ctype(), PassthroughLayerFBHandle)

PFN_xrPassthroughLayerResumeFB = CFUNCTYPE(Result.ctype(), PassthroughLayerFBHandle)

PFN_xrPassthroughLayerSetStyleFB = CFUNCTYPE(Result.ctype(), PassthroughLayerFBHandle, POINTER(PassthroughStyleFB))

PFN_xrCreateGeometryInstanceFB = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(GeometryInstanceCreateInfoFB), POINTER(GeometryInstanceFBHandle))

PFN_xrDestroyGeometryInstanceFB = CFUNCTYPE(Result.ctype(), GeometryInstanceFBHandle)

PFN_xrGeometryInstanceSetTransformFB = CFUNCTYPE(Result.ctype(), GeometryInstanceFBHandle, POINTER(GeometryInstanceTransformFB))

RenderModelKeyFB = c_uint64

RenderModelFlagsFBCInt = Flags64


class RenderModelPathInfoFB(Structure):
    def __init__(
        self,
        path: Path = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.RENDER_MODEL_PATH_INFO_FB,
    ) -> None:
        super().__init__(
            path=path,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.RenderModelPathInfoFB(path={repr(self.path)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.RenderModelPathInfoFB(path={self.path}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("path", Path),
    ]


class RenderModelPropertiesFB(Structure):
    def __init__(
        self,
        vendor_id: int = 0,
        model_name: str = "",
        model_key: RenderModelKeyFB = 0,
        model_version: int = 0,
        flags: RenderModelFlagsFB = RenderModelFlagsFB(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.RENDER_MODEL_PROPERTIES_FB,
    ) -> None:
        super().__init__(
            vendor_id=vendor_id,
            model_name=model_name.encode(),
            model_key=model_key,
            model_version=model_version,
            flags=RenderModelFlagsFB(flags).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.RenderModelPropertiesFB(vendor_id={repr(self.vendor_id)}, model_name={repr(self.model_name)}, model_key={repr(self.model_key)}, model_version={repr(self.model_version)}, flags={repr(self.flags)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.RenderModelPropertiesFB(vendor_id={self.vendor_id}, model_name={self.model_name}, model_key={self.model_key}, model_version={self.model_version}, flags={self.flags}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("vendor_id", c_uint32),
        ("model_name", (c_char * 64)),
        ("model_key", RenderModelKeyFB),
        ("model_version", c_uint32),
        ("flags", RenderModelFlagsFBCInt),
    ]


class RenderModelBufferFB(Structure):
    def __init__(
        self,
        buffer_capacity_input: int = 0,
        buffer_count_output: int = 0,
        buffer: POINTER(c_uint8) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.RENDER_MODEL_BUFFER_FB,
    ) -> None:
        super().__init__(
            buffer_capacity_input=buffer_capacity_input,
            buffer_count_output=buffer_count_output,
            buffer=buffer,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.RenderModelBufferFB(buffer_capacity_input={repr(self.buffer_capacity_input)}, buffer_count_output={repr(self.buffer_count_output)}, buffer={repr(self.buffer)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.RenderModelBufferFB(buffer_capacity_input={self.buffer_capacity_input}, buffer_count_output={self.buffer_count_output}, buffer={self.buffer}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("buffer_capacity_input", c_uint32),
        ("buffer_count_output", c_uint32),
        ("buffer", POINTER(c_uint8)),
    ]


class RenderModelLoadInfoFB(Structure):
    def __init__(
        self,
        model_key: RenderModelKeyFB = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.RENDER_MODEL_LOAD_INFO_FB,
    ) -> None:
        super().__init__(
            model_key=model_key,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.RenderModelLoadInfoFB(model_key={repr(self.model_key)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.RenderModelLoadInfoFB(model_key={self.model_key}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("model_key", RenderModelKeyFB),
    ]


class SystemRenderModelPropertiesFB(Structure):
    def __init__(
        self,
        supports_render_model_loading: Bool32 = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SYSTEM_RENDER_MODEL_PROPERTIES_FB,
    ) -> None:
        super().__init__(
            supports_render_model_loading=supports_render_model_loading,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SystemRenderModelPropertiesFB(supports_render_model_loading={repr(self.supports_render_model_loading)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SystemRenderModelPropertiesFB(supports_render_model_loading={self.supports_render_model_loading}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_render_model_loading", Bool32),
    ]


PFN_xrEnumerateRenderModelPathsFB = CFUNCTYPE(Result.ctype(), SessionHandle, c_uint32, POINTER(c_uint32), POINTER(RenderModelPathInfoFB))

PFN_xrGetRenderModelPropertiesFB = CFUNCTYPE(Result.ctype(), SessionHandle, Path, POINTER(RenderModelPropertiesFB))

PFN_xrLoadRenderModelFB = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(RenderModelLoadInfoFB), POINTER(RenderModelBufferFB))


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
        return f"xr.ViewLocateFoveatedRenderingVARJO(foveated_rendering_active={repr(self.foveated_rendering_active)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.ViewLocateFoveatedRenderingVARJO(foveated_rendering_active={self.foveated_rendering_active}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.FoveatedViewConfigurationViewVARJO(foveated_rendering_active={repr(self.foveated_rendering_active)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.FoveatedViewConfigurationViewVARJO(foveated_rendering_active={self.foveated_rendering_active}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SystemFoveatedRenderingPropertiesVARJO(supports_foveated_rendering={repr(self.supports_foveated_rendering)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SystemFoveatedRenderingPropertiesVARJO(supports_foveated_rendering={self.supports_foveated_rendering}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.CompositionLayerDepthTestVARJO(depth_test_range_near_z={repr(self.depth_test_range_near_z)}, depth_test_range_far_z={repr(self.depth_test_range_far_z)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerDepthTestVARJO(depth_test_range_near_z={self.depth_test_range_near_z:.3f}, depth_test_range_far_z={self.depth_test_range_far_z:.3f}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("depth_test_range_near_z", c_float),
        ("depth_test_range_far_z", c_float),
    ]


PFN_xrSetEnvironmentDepthEstimationVARJO = CFUNCTYPE(Result.ctype(), SessionHandle, Bool32)


class SystemMarkerTrackingPropertiesVARJO(Structure):
    def __init__(
        self,
        supports_marker_tracking: Bool32 = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SYSTEM_MARKER_TRACKING_PROPERTIES_VARJO,
    ) -> None:
        super().__init__(
            supports_marker_tracking=supports_marker_tracking,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SystemMarkerTrackingPropertiesVARJO(supports_marker_tracking={repr(self.supports_marker_tracking)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SystemMarkerTrackingPropertiesVARJO(supports_marker_tracking={self.supports_marker_tracking}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_marker_tracking", Bool32),
    ]


class EventDataMarkerTrackingUpdateVARJO(Structure):
    def __init__(
        self,
        marker_id: int = 0,
        is_active: Bool32 = 0,
        is_predicted: Bool32 = 0,
        time: Time = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.EVENT_DATA_MARKER_TRACKING_UPDATE_VARJO,
    ) -> None:
        super().__init__(
            marker_id=marker_id,
            is_active=is_active,
            is_predicted=is_predicted,
            time=time,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataMarkerTrackingUpdateVARJO(marker_id={repr(self.marker_id)}, is_active={repr(self.is_active)}, is_predicted={repr(self.is_predicted)}, time={repr(self.time)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.EventDataMarkerTrackingUpdateVARJO(marker_id={self.marker_id}, is_active={self.is_active}, is_predicted={self.is_predicted}, time={self.time}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("marker_id", c_uint64),
        ("is_active", Bool32),
        ("is_predicted", Bool32),
        ("time", Time),
    ]


class MarkerSpaceCreateInfoVARJO(Structure):
    def __init__(
        self,
        marker_id: int = 0,
        pose_in_marker_space: Posef = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.MARKER_SPACE_CREATE_INFO_VARJO,
    ) -> None:
        if pose_in_marker_space is None:
            pose_in_marker_space = Posef()
        super().__init__(
            marker_id=marker_id,
            pose_in_marker_space=pose_in_marker_space,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.MarkerSpaceCreateInfoVARJO(marker_id={repr(self.marker_id)}, pose_in_marker_space={repr(self.pose_in_marker_space)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.MarkerSpaceCreateInfoVARJO(marker_id={self.marker_id}, pose_in_marker_space={self.pose_in_marker_space}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("marker_id", c_uint64),
        ("pose_in_marker_space", Posef),
    ]


PFN_xrSetMarkerTrackingVARJO = CFUNCTYPE(Result.ctype(), SessionHandle, Bool32)

PFN_xrSetMarkerTrackingTimeoutVARJO = CFUNCTYPE(Result.ctype(), SessionHandle, c_uint64, Duration)

PFN_xrSetMarkerTrackingPredictionVARJO = CFUNCTYPE(Result.ctype(), SessionHandle, c_uint64, Bool32)

PFN_xrGetMarkerSizeVARJO = CFUNCTYPE(Result.ctype(), SessionHandle, c_uint64, POINTER(Extent2Df))

PFN_xrCreateMarkerSpaceVARJO = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(MarkerSpaceCreateInfoVARJO), POINTER(SpaceHandle))


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
        return f"xr.SpatialAnchorPersistenceNameMSFT(name={self.name})"

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
        return f"xr.SpatialAnchorPersistenceInfoMSFT(spatial_anchor_persistence_name={repr(self.spatial_anchor_persistence_name)}, spatial_anchor={repr(self.spatial_anchor)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorPersistenceInfoMSFT(spatial_anchor_persistence_name={self.spatial_anchor_persistence_name}, spatial_anchor={self.spatial_anchor}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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
        return f"xr.SpatialAnchorFromPersistedAnchorCreateInfoMSFT(spatial_anchor_store={repr(self.spatial_anchor_store)}, spatial_anchor_persistence_name={repr(self.spatial_anchor_persistence_name)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorFromPersistedAnchorCreateInfoMSFT(spatial_anchor_store={self.spatial_anchor_store}, spatial_anchor_persistence_name={self.spatial_anchor_persistence_name}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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

CompositionLayerSpaceWarpInfoFlagsFBCInt = Flags64


class CompositionLayerSpaceWarpInfoFB(Structure):
    def __init__(
        self,
        layer_flags: CompositionLayerSpaceWarpInfoFlagsFB = CompositionLayerSpaceWarpInfoFlagsFB(),
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
            layer_flags=CompositionLayerSpaceWarpInfoFlagsFB(layer_flags).value,
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
        return f"xr.CompositionLayerSpaceWarpInfoFB(layer_flags={repr(self.layer_flags)}, motion_vector_sub_image={repr(self.motion_vector_sub_image)}, app_space_delta_pose={repr(self.app_space_delta_pose)}, depth_sub_image={repr(self.depth_sub_image)}, min_depth={repr(self.min_depth)}, max_depth={repr(self.max_depth)}, near_z={repr(self.near_z)}, far_z={repr(self.far_z)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerSpaceWarpInfoFB(layer_flags={self.layer_flags}, motion_vector_sub_image={self.motion_vector_sub_image}, app_space_delta_pose={self.app_space_delta_pose}, depth_sub_image={self.depth_sub_image}, min_depth={self.min_depth:.3f}, max_depth={self.max_depth:.3f}, near_z={self.near_z:.3f}, far_z={self.far_z:.3f}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerSpaceWarpInfoFlagsFBCInt),
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
        return f"xr.SystemSpaceWarpPropertiesFB(recommended_motion_vector_image_rect_width={repr(self.recommended_motion_vector_image_rect_width)}, recommended_motion_vector_image_rect_height={repr(self.recommended_motion_vector_image_rect_height)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SystemSpaceWarpPropertiesFB(recommended_motion_vector_image_rect_width={self.recommended_motion_vector_image_rect_width}, recommended_motion_vector_image_rect_height={self.recommended_motion_vector_image_rect_height}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("recommended_motion_vector_image_rect_width", c_uint32),
        ("recommended_motion_vector_image_rect_height", c_uint32),
    ]


DigitalLensControlFlagsALMALENCECInt = Flags64


class DigitalLensControlALMALENCE(Structure):
    def __init__(
        self,
        flags: DigitalLensControlFlagsALMALENCE = DigitalLensControlFlagsALMALENCE(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.DIGITAL_LENS_CONTROL_ALMALENCE,
    ) -> None:
        super().__init__(
            flags=DigitalLensControlFlagsALMALENCE(flags).value,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.DigitalLensControlALMALENCE(flags={repr(self.flags)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.DigitalLensControlALMALENCE(flags={self.flags}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", DigitalLensControlFlagsALMALENCECInt),
    ]


PFN_xrSetDigitalLensControlALMALENCE = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(DigitalLensControlALMALENCE))


class PassthroughKeyboardHandsIntensityFB(Structure):
    def __init__(
        self,
        left_hand_intensity: float = 0,
        right_hand_intensity: float = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.PASSTHROUGH_KEYBOARD_HANDS_INTENSITY_FB,
    ) -> None:
        super().__init__(
            left_hand_intensity=left_hand_intensity,
            right_hand_intensity=right_hand_intensity,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.PassthroughKeyboardHandsIntensityFB(left_hand_intensity={repr(self.left_hand_intensity)}, right_hand_intensity={repr(self.right_hand_intensity)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.PassthroughKeyboardHandsIntensityFB(left_hand_intensity={self.left_hand_intensity:.3f}, right_hand_intensity={self.right_hand_intensity:.3f}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("left_hand_intensity", c_float),
        ("right_hand_intensity", c_float),
    ]


PFN_xrPassthroughLayerSetKeyboardHandsIntensityFB = CFUNCTYPE(Result.ctype(), PassthroughLayerFBHandle, POINTER(PassthroughKeyboardHandsIntensityFB))


class UuidEXT(Structure):
    def __init__(
        self,
    ) -> None:
        super().__init__(
        )

    def __repr__(self) -> str:
        return f"xr.UuidEXT(data={repr(self.data)})"

    def __str__(self) -> str:
        return f"xr.UuidEXT()"

    _fields_ = [
        ("data", (c_uint8 * 16)),
    ]


__all__ = [
    "ActionCreateInfo",
    "ActionHandle",
    "ActionSetCreateInfo",
    "ActionSetHandle",
    "ActionSet_T",
    "ActionSpaceCreateInfo",
    "ActionStateBoolean",
    "ActionStateFloat",
    "ActionStateGetInfo",
    "ActionStatePose",
    "ActionStateVector2f",
    "ActionSuggestedBinding",
    "Action_T",
    "ActionsSyncInfo",
    "ActiveActionSet",
    "ApiLayerProperties",
    "ApplicationInfo",
    "BaseInStructure",
    "BaseOutStructure",
    "BindingModificationBaseHeaderKHR",
    "BindingModificationsKHR",
    "Bool32",
    "BoundSourcesForActionEnumerateInfo",
    "Color4f",
    "CompositionLayerAlphaBlendFB",
    "CompositionLayerBaseHeader",
    "CompositionLayerColorScaleBiasKHR",
    "CompositionLayerCubeKHR",
    "CompositionLayerCylinderKHR",
    "CompositionLayerDepthInfoKHR",
    "CompositionLayerDepthTestVARJO",
    "CompositionLayerEquirect2KHR",
    "CompositionLayerEquirectKHR",
    "CompositionLayerFlagsCInt",
    "CompositionLayerImageLayoutFB",
    "CompositionLayerImageLayoutFlagsFBCInt",
    "CompositionLayerPassthroughFB",
    "CompositionLayerProjection",
    "CompositionLayerProjectionView",
    "CompositionLayerQuad",
    "CompositionLayerReprojectionInfoMSFT",
    "CompositionLayerReprojectionPlaneOverrideMSFT",
    "CompositionLayerSecureContentFB",
    "CompositionLayerSecureContentFlagsFBCInt",
    "CompositionLayerSpaceWarpInfoFB",
    "CompositionLayerSpaceWarpInfoFlagsFBCInt",
    "ControllerModelKeyMSFT",
    "ControllerModelKeyStateMSFT",
    "ControllerModelNodePropertiesMSFT",
    "ControllerModelNodeStateMSFT",
    "ControllerModelPropertiesMSFT",
    "ControllerModelStateMSFT",
    "DebugUtilsLabelEXT",
    "DebugUtilsMessageSeverityFlagsEXTCInt",
    "DebugUtilsMessageTypeFlagsEXTCInt",
    "DebugUtilsMessengerCallbackDataEXT",
    "DebugUtilsMessengerCreateInfoEXT",
    "DebugUtilsMessengerEXTHandle",
    "DebugUtilsMessengerEXT_T",
    "DebugUtilsObjectNameInfoEXT",
    "DeserializeSceneFragmentMSFT",
    "DigitalLensControlALMALENCE",
    "DigitalLensControlFlagsALMALENCECInt",
    "Duration",
    "EventDataBaseHeader",
    "EventDataBuffer",
    "EventDataDisplayRefreshRateChangedFB",
    "EventDataEventsLost",
    "EventDataInstanceLossPending",
    "EventDataInteractionProfileChanged",
    "EventDataMainSessionVisibilityChangedEXTX",
    "EventDataMarkerTrackingUpdateVARJO",
    "EventDataPassthroughStateChangedFB",
    "EventDataPerfSettingsEXT",
    "EventDataReferenceSpaceChangePending",
    "EventDataSessionStateChanged",
    "EventDataVisibilityMaskChangedKHR",
    "EventDataViveTrackerConnectedHTCX",
    "ExtensionProperties",
    "Extent2Df",
    "Extent2Di",
    "EyeGazeSampleTimeEXT",
    "FacialExpressionsHTC",
    "FacialTrackerCreateInfoHTC",
    "FacialTrackerHTCHandle",
    "FacialTrackerHTC_T",
    "Flags64",
    "FoveatedViewConfigurationViewVARJO",
    "FoveationLevelProfileCreateInfoFB",
    "FoveationProfileCreateInfoFB",
    "FoveationProfileFBHandle",
    "FoveationProfileFB_T",
    "Fovf",
    "FrameBeginInfo",
    "FrameEndInfo",
    "FrameState",
    "FrameWaitInfo",
    "GeometryInstanceCreateInfoFB",
    "GeometryInstanceFBHandle",
    "GeometryInstanceFB_T",
    "GeometryInstanceTransformFB",
    "HandCapsuleFB",
    "HandJointLocationEXT",
    "HandJointLocationsEXT",
    "HandJointVelocitiesEXT",
    "HandJointVelocityEXT",
    "HandJointsLocateInfoEXT",
    "HandJointsMotionRangeInfoEXT",
    "HandMeshIndexBufferMSFT",
    "HandMeshMSFT",
    "HandMeshSpaceCreateInfoMSFT",
    "HandMeshUpdateInfoMSFT",
    "HandMeshVertexBufferMSFT",
    "HandMeshVertexMSFT",
    "HandPoseTypeInfoMSFT",
    "HandTrackerCreateInfoEXT",
    "HandTrackerEXTHandle",
    "HandTrackerEXT_T",
    "HandTrackingAimFlagsFBCInt",
    "HandTrackingAimStateFB",
    "HandTrackingCapsulesStateFB",
    "HandTrackingMeshFB",
    "HandTrackingScaleFB",
    "HapticActionInfo",
    "HapticBaseHeader",
    "HapticVibration",
    "InputSourceLocalizedNameFlagsCInt",
    "InputSourceLocalizedNameGetInfo",
    "InstanceCreateFlagsCInt",
    "InstanceCreateInfo",
    "InstanceHandle",
    "InstanceProperties",
    "Instance_T",
    "InteractionProfileAnalogThresholdVALVE",
    "InteractionProfileState",
    "InteractionProfileSuggestedBinding",
    "KeyboardSpaceCreateInfoFB",
    "KeyboardTrackingDescriptionFB",
    "KeyboardTrackingFlagsFBCInt",
    "KeyboardTrackingQueryFB",
    "KeyboardTrackingQueryFlagsFBCInt",
    "LoaderInitInfoBaseHeaderKHR",
    "MarkerSpaceCreateInfoVARJO",
    "NewSceneComputeInfoMSFT",
    "Offset2Df",
    "Offset2Di",
    "OverlayMainSessionFlagsEXTXCInt",
    "OverlaySessionCreateFlagsEXTXCInt",
    "PFN_xrAcquireSwapchainImage",
    "PFN_xrApplyHapticFeedback",
    "PFN_xrAttachSessionActionSets",
    "PFN_xrBeginFrame",
    "PFN_xrBeginSession",
    "PFN_xrClearSpatialAnchorStoreMSFT",
    "PFN_xrComputeNewSceneMSFT",
    "PFN_xrCreateAction",
    "PFN_xrCreateActionSet",
    "PFN_xrCreateActionSpace",
    "PFN_xrCreateDebugUtilsMessengerEXT",
    "PFN_xrCreateFacialTrackerHTC",
    "PFN_xrCreateFoveationProfileFB",
    "PFN_xrCreateGeometryInstanceFB",
    "PFN_xrCreateHandMeshSpaceMSFT",
    "PFN_xrCreateHandTrackerEXT",
    "PFN_xrCreateInstance",
    "PFN_xrCreateKeyboardSpaceFB",
    "PFN_xrCreateMarkerSpaceVARJO",
    "PFN_xrCreatePassthroughFB",
    "PFN_xrCreatePassthroughLayerFB",
    "PFN_xrCreateReferenceSpace",
    "PFN_xrCreateSceneMSFT",
    "PFN_xrCreateSceneObserverMSFT",
    "PFN_xrCreateSession",
    "PFN_xrCreateSpatialAnchorFromPersistedNameMSFT",
    "PFN_xrCreateSpatialAnchorMSFT",
    "PFN_xrCreateSpatialAnchorSpaceMSFT",
    "PFN_xrCreateSpatialAnchorStoreConnectionMSFT",
    "PFN_xrCreateSpatialGraphNodeSpaceMSFT",
    "PFN_xrCreateSwapchain",
    "PFN_xrCreateTriangleMeshFB",
    "PFN_xrDebugUtilsMessengerCallbackEXT",
    "PFN_xrDeserializeSceneMSFT",
    "PFN_xrDestroyAction",
    "PFN_xrDestroyActionSet",
    "PFN_xrDestroyDebugUtilsMessengerEXT",
    "PFN_xrDestroyFacialTrackerHTC",
    "PFN_xrDestroyFoveationProfileFB",
    "PFN_xrDestroyGeometryInstanceFB",
    "PFN_xrDestroyHandTrackerEXT",
    "PFN_xrDestroyInstance",
    "PFN_xrDestroyPassthroughFB",
    "PFN_xrDestroyPassthroughLayerFB",
    "PFN_xrDestroySceneMSFT",
    "PFN_xrDestroySceneObserverMSFT",
    "PFN_xrDestroySession",
    "PFN_xrDestroySpace",
    "PFN_xrDestroySpatialAnchorMSFT",
    "PFN_xrDestroySpatialAnchorStoreConnectionMSFT",
    "PFN_xrDestroySwapchain",
    "PFN_xrDestroyTriangleMeshFB",
    "PFN_xrEndFrame",
    "PFN_xrEndSession",
    "PFN_xrEnumerateApiLayerProperties",
    "PFN_xrEnumerateBoundSourcesForAction",
    "PFN_xrEnumerateColorSpacesFB",
    "PFN_xrEnumerateDisplayRefreshRatesFB",
    "PFN_xrEnumerateEnvironmentBlendModes",
    "PFN_xrEnumerateInstanceExtensionProperties",
    "PFN_xrEnumeratePersistedSpatialAnchorNamesMSFT",
    "PFN_xrEnumerateReferenceSpaces",
    "PFN_xrEnumerateRenderModelPathsFB",
    "PFN_xrEnumerateReprojectionModesMSFT",
    "PFN_xrEnumerateSceneComputeFeaturesMSFT",
    "PFN_xrEnumerateSwapchainFormats",
    "PFN_xrEnumerateSwapchainImages",
    "PFN_xrEnumerateViewConfigurationViews",
    "PFN_xrEnumerateViewConfigurations",
    "PFN_xrEnumerateViveTrackerPathsHTCX",
    "PFN_xrGeometryInstanceSetTransformFB",
    "PFN_xrGetActionStateBoolean",
    "PFN_xrGetActionStateFloat",
    "PFN_xrGetActionStatePose",
    "PFN_xrGetActionStateVector2f",
    "PFN_xrGetControllerModelKeyMSFT",
    "PFN_xrGetControllerModelPropertiesMSFT",
    "PFN_xrGetControllerModelStateMSFT",
    "PFN_xrGetCurrentInteractionProfile",
    "PFN_xrGetDisplayRefreshRateFB",
    "PFN_xrGetFacialExpressionsHTC",
    "PFN_xrGetHandMeshFB",
    "PFN_xrGetInputSourceLocalizedName",
    "PFN_xrGetInstanceProcAddr",
    "PFN_xrGetInstanceProperties",
    "PFN_xrGetMarkerSizeVARJO",
    "PFN_xrGetReferenceSpaceBoundsRect",
    "PFN_xrGetRenderModelPropertiesFB",
    "PFN_xrGetSceneComponentsMSFT",
    "PFN_xrGetSceneComputeStateMSFT",
    "PFN_xrGetSceneMeshBuffersMSFT",
    "PFN_xrGetSerializedSceneFragmentDataMSFT",
    "PFN_xrGetSwapchainStateFB",
    "PFN_xrGetSystem",
    "PFN_xrGetSystemProperties",
    "PFN_xrGetViewConfigurationProperties",
    "PFN_xrGetVisibilityMaskKHR",
    "PFN_xrInitializeLoaderKHR",
    "PFN_xrLoadControllerModelMSFT",
    "PFN_xrLoadRenderModelFB",
    "PFN_xrLocateHandJointsEXT",
    "PFN_xrLocateSceneComponentsMSFT",
    "PFN_xrLocateSpace",
    "PFN_xrLocateViews",
    "PFN_xrPassthroughLayerPauseFB",
    "PFN_xrPassthroughLayerResumeFB",
    "PFN_xrPassthroughLayerSetKeyboardHandsIntensityFB",
    "PFN_xrPassthroughLayerSetStyleFB",
    "PFN_xrPassthroughPauseFB",
    "PFN_xrPassthroughStartFB",
    "PFN_xrPathToString",
    "PFN_xrPerfSettingsSetPerformanceLevelEXT",
    "PFN_xrPersistSpatialAnchorMSFT",
    "PFN_xrPollEvent",
    "PFN_xrQuerySystemTrackedKeyboardFB",
    "PFN_xrReleaseSwapchainImage",
    "PFN_xrRequestDisplayRefreshRateFB",
    "PFN_xrRequestExitSession",
    "PFN_xrResultToString",
    "PFN_xrSessionBeginDebugUtilsLabelRegionEXT",
    "PFN_xrSessionEndDebugUtilsLabelRegionEXT",
    "PFN_xrSessionInsertDebugUtilsLabelEXT",
    "PFN_xrSetColorSpaceFB",
    "PFN_xrSetDebugUtilsObjectNameEXT",
    "PFN_xrSetDigitalLensControlALMALENCE",
    "PFN_xrSetEnvironmentDepthEstimationVARJO",
    "PFN_xrSetInputDeviceActiveEXT",
    "PFN_xrSetInputDeviceLocationEXT",
    "PFN_xrSetInputDeviceStateBoolEXT",
    "PFN_xrSetInputDeviceStateFloatEXT",
    "PFN_xrSetInputDeviceStateVector2fEXT",
    "PFN_xrSetMarkerTrackingPredictionVARJO",
    "PFN_xrSetMarkerTrackingTimeoutVARJO",
    "PFN_xrSetMarkerTrackingVARJO",
    "PFN_xrStopHapticFeedback",
    "PFN_xrStringToPath",
    "PFN_xrStructureTypeToString",
    "PFN_xrSubmitDebugUtilsMessageEXT",
    "PFN_xrSuggestInteractionProfileBindings",
    "PFN_xrSyncActions",
    "PFN_xrThermalGetTemperatureTrendEXT",
    "PFN_xrTriangleMeshBeginUpdateFB",
    "PFN_xrTriangleMeshBeginVertexBufferUpdateFB",
    "PFN_xrTriangleMeshEndUpdateFB",
    "PFN_xrTriangleMeshEndVertexBufferUpdateFB",
    "PFN_xrTriangleMeshGetIndexBufferFB",
    "PFN_xrTriangleMeshGetVertexBufferFB",
    "PFN_xrUnpersistSpatialAnchorMSFT",
    "PFN_xrUpdateHandMeshMSFT",
    "PFN_xrUpdateSwapchainFB",
    "PFN_xrVoidFunction",
    "PFN_xrWaitFrame",
    "PFN_xrWaitSwapchainImage",
    "PassthroughColorMapMonoToMonoFB",
    "PassthroughColorMapMonoToRgbaFB",
    "PassthroughCreateInfoFB",
    "PassthroughFBHandle",
    "PassthroughFB_T",
    "PassthroughFlagsFBCInt",
    "PassthroughKeyboardHandsIntensityFB",
    "PassthroughLayerCreateInfoFB",
    "PassthroughLayerFBHandle",
    "PassthroughLayerFB_T",
    "PassthroughStateChangedFlagsFBCInt",
    "PassthroughStyleFB",
    "Path",
    "Posef",
    "Quaternionf",
    "Rect2Df",
    "Rect2Di",
    "ReferenceSpaceCreateInfo",
    "RenderModelBufferFB",
    "RenderModelFlagsFBCInt",
    "RenderModelKeyFB",
    "RenderModelLoadInfoFB",
    "RenderModelPathInfoFB",
    "RenderModelPropertiesFB",
    "SceneBoundsMSFT",
    "SceneComponentLocationMSFT",
    "SceneComponentLocationsMSFT",
    "SceneComponentMSFT",
    "SceneComponentParentFilterInfoMSFT",
    "SceneComponentsGetInfoMSFT",
    "SceneComponentsLocateInfoMSFT",
    "SceneComponentsMSFT",
    "SceneCreateInfoMSFT",
    "SceneDeserializeInfoMSFT",
    "SceneFrustumBoundMSFT",
    "SceneMSFTHandle",
    "SceneMSFT_T",
    "SceneMeshBuffersGetInfoMSFT",
    "SceneMeshBuffersMSFT",
    "SceneMeshIndicesUint16MSFT",
    "SceneMeshIndicesUint32MSFT",
    "SceneMeshMSFT",
    "SceneMeshVertexBufferMSFT",
    "SceneMeshesMSFT",
    "SceneObjectMSFT",
    "SceneObjectTypesFilterInfoMSFT",
    "SceneObjectsMSFT",
    "SceneObserverCreateInfoMSFT",
    "SceneObserverMSFTHandle",
    "SceneObserverMSFT_T",
    "SceneOrientedBoxBoundMSFT",
    "ScenePlaneAlignmentFilterInfoMSFT",
    "ScenePlaneMSFT",
    "ScenePlanesMSFT",
    "SceneSphereBoundMSFT",
    "SecondaryViewConfigurationFrameEndInfoMSFT",
    "SecondaryViewConfigurationFrameStateMSFT",
    "SecondaryViewConfigurationLayerInfoMSFT",
    "SecondaryViewConfigurationSessionBeginInfoMSFT",
    "SecondaryViewConfigurationStateMSFT",
    "SecondaryViewConfigurationSwapchainCreateInfoMSFT",
    "SerializedSceneFragmentDataGetInfoMSFT",
    "SessionActionSetsAttachInfo",
    "SessionBeginInfo",
    "SessionCreateFlagsCInt",
    "SessionCreateInfo",
    "SessionCreateInfoOverlayEXTX",
    "SessionHandle",
    "Session_T",
    "SpaceHandle",
    "SpaceLocation",
    "SpaceLocationFlagsCInt",
    "SpaceVelocity",
    "SpaceVelocityFlagsCInt",
    "Space_T",
    "SpatialAnchorCreateInfoMSFT",
    "SpatialAnchorFromPersistedAnchorCreateInfoMSFT",
    "SpatialAnchorMSFTHandle",
    "SpatialAnchorMSFT_T",
    "SpatialAnchorPersistenceInfoMSFT",
    "SpatialAnchorPersistenceNameMSFT",
    "SpatialAnchorSpaceCreateInfoMSFT",
    "SpatialAnchorStoreConnectionMSFTHandle",
    "SpatialAnchorStoreConnectionMSFT_T",
    "SpatialGraphNodeSpaceCreateInfoMSFT",
    "SwapchainCreateFlagsCInt",
    "SwapchainCreateFoveationFlagsFBCInt",
    "SwapchainCreateInfo",
    "SwapchainCreateInfoFoveationFB",
    "SwapchainHandle",
    "SwapchainImageAcquireInfo",
    "SwapchainImageBaseHeader",
    "SwapchainImageReleaseInfo",
    "SwapchainImageWaitInfo",
    "SwapchainStateBaseHeaderFB",
    "SwapchainStateFoveationFB",
    "SwapchainStateFoveationFlagsFBCInt",
    "SwapchainSubImage",
    "SwapchainUsageFlagsCInt",
    "Swapchain_T",
    "SystemColorSpacePropertiesFB",
    "SystemEyeGazeInteractionPropertiesEXT",
    "SystemFacialTrackingPropertiesHTC",
    "SystemFoveatedRenderingPropertiesVARJO",
    "SystemGetInfo",
    "SystemGraphicsProperties",
    "SystemHandTrackingMeshPropertiesMSFT",
    "SystemHandTrackingPropertiesEXT",
    "SystemId",
    "SystemKeyboardTrackingPropertiesFB",
    "SystemMarkerTrackingPropertiesVARJO",
    "SystemPassthroughPropertiesFB",
    "SystemProperties",
    "SystemRenderModelPropertiesFB",
    "SystemSpaceWarpPropertiesFB",
    "SystemTrackingProperties",
    "Time",
    "TriangleMeshCreateInfoFB",
    "TriangleMeshFBHandle",
    "TriangleMeshFB_T",
    "TriangleMeshFlagsFBCInt",
    "UuidEXT",
    "UuidMSFT",
    "Vector2f",
    "Vector3f",
    "Vector4f",
    "Vector4sFB",
    "VersionNumber",
    "View",
    "ViewConfigurationDepthRangeEXT",
    "ViewConfigurationProperties",
    "ViewConfigurationView",
    "ViewConfigurationViewFovEPIC",
    "ViewLocateFoveatedRenderingVARJO",
    "ViewLocateInfo",
    "ViewState",
    "ViewStateFlagsCInt",
    "VisibilityMaskKHR",
    "VisualMeshComputeLodInfoMSFT",
    "ViveTrackerPathsHTCX",
]
