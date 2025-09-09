# Warning: this file is auto-generated. Do not edit.

from ctypes import (
    CFUNCTYPE, POINTER, Structure, addressof, byref, c_char, c_char_p, c_float,
    c_int, c_int16, c_int32, c_int64, c_uint16, c_uint32, c_uint64, c_uint8,
    c_void_p, cast, py_object,
)
import ctypes

import os
import sys
from typing import Any, Callable, Generator, Optional

import numpy

from .array_field import *
from .enums import *
from .version import *
from .handle import HandleMixin

VersionNumber = c_uint64

Flags64 = c_uint64

SystemId = c_uint64

Bool32 = c_uint32

Path = c_uint64

Time = c_int64

Duration = c_int64


class Instance_T(Structure):
    pass


class Instance(POINTER(Instance_T), HandleMixin):
    """
    Opaque handle to an OpenXR instance object.

    An `xr.Instance` represents a connection between an OpenXR application and the
    OpenXR runtime. It encapsulates all runtime-managed state and serves as the root
    object for most OpenXR operations, including system queries, session creation,
    and extension dispatch.

    `Instance` supports context management protocols and may be used in a `with` block
    for automatic teardown via :func:`xr.destroy_instance`:

    .. code-block:: python

        with xr.create_instance(...) as instance:
            ...

    Internally, this object wraps a pointer to the OpenXR instance and delegates all
    interactions to the runtime via raw API functions. It is opaque and cannot be
    directly inspected or modified.

    :seealso: :func:`xr.create_instance`, :func:`xr.destroy_instance`, :class:`xr.InstanceCreateInfo`
    :see: https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrInstance.html
    """
    _type_ = Instance_T  # ctypes idiosyncrasy


class Session_T(Structure):
    pass


class Session(POINTER(Session_T), HandleMixin):
    _type_ = Session_T  # ctypes idiosyncrasy


class Space_T(Structure):
    pass


class Space(POINTER(Space_T), HandleMixin):
    _type_ = Space_T  # ctypes idiosyncrasy


class Action_T(Structure):
    pass


class Action(POINTER(Action_T), HandleMixin):
    _type_ = Action_T  # ctypes idiosyncrasy


class Swapchain_T(Structure):
    pass


class Swapchain(POINTER(Swapchain_T), HandleMixin):
    _type_ = Swapchain_T  # ctypes idiosyncrasy


class ActionSet_T(Structure):
    pass


class ActionSet(POINTER(ActionSet_T), HandleMixin):
    _type_ = ActionSet_T  # ctypes idiosyncrasy

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
        next: c_void_p = None,
        type: StructureType = StructureType.API_LAYER_PROPERTIES,
    ) -> None:
        super().__init__(
            layer_name=layer_name.encode(),
            _spec_version=spec_version.number(),
            layer_version=layer_version,
            description=description.encode(),
            next=next,
            type=type,
        )

    def __bytes__(self):
        return self.layer_name

    def __eq__(self, other):
        try:
            if other.type != self.type:
                return False
        except AttributeError:
            pass  # That's OK, objects without those attributes can use string comparison
        return str(other) == str(self)

    def __str__(self):
        return self.layer_name.decode()

    @property
    def spec_version(self) -> Version:
        return Version(self._spec_version)
    
    @spec_version.setter
    def spec_version(self, value: Version) -> None:
        if hasattr(value, 'number'):
            # noinspection PyAttributeOutsideInit
            self._spec_version = value.number()
        else:
            # noinspection PyAttributeOutsideInit
            self._spec_version = value

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_name", (c_char * 256)),
        ("_spec_version", VersionNumber),
        ("layer_version", c_uint32),
        ("description", (c_char * 256)),
    ]


class ExtensionProperties(Structure):
    def __init__(
        self,
        extension_name: str = "",
        extension_version: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.EXTENSION_PROPERTIES,
    ) -> None:
        super().__init__(
            extension_name=extension_name.encode(),
            extension_version=extension_version,
            next=next,
            type=type,
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
        application_name: str = os.path.basename(sys.argv[0]),
        application_version: int = 0,
        engine_name: str = "pyopenxr",
        engine_version: int = PYOPENXR_CURRENT_API_VERSION,
        api_version: Version = Version(1, 0, XR_VERSION_PATCH),
    ) -> None:
        super().__init__(
            application_name=application_name.encode(),
            application_version=application_version,
            engine_name=engine_name.encode(),
            engine_version=engine_version,
            _api_version=api_version.number(),
        )

    def __repr__(self) -> str:
        return f"xr.ApplicationInfo(application_name={repr(self.application_name)}, application_version={repr(self.application_version)}, engine_name={repr(self.engine_name)}, engine_version={repr(self.engine_version)}, api_version={repr(self._api_version)})"

    def __str__(self) -> str:
        return f"xr.ApplicationInfo(application_name={self.application_name}, application_version={self.application_version}, engine_name={self.engine_name}, engine_version={self.engine_version}, api_version={self._api_version})"

    @property
    def api_version(self) -> Version:
        return Version(self._api_version)
    
    @api_version.setter
    def api_version(self, value: Version) -> None:
        if hasattr(value, 'number'):
            # noinspection PyAttributeOutsideInit
            self._api_version = value.number()
        else:
            # noinspection PyAttributeOutsideInit
            self._api_version = value

    _fields_ = [
        ("application_name", (c_char * 128)),
        ("application_version", c_uint32),
        ("engine_name", (c_char * 128)),
        ("engine_version", c_uint32),
        ("_api_version", VersionNumber),
    ]


class InstanceCreateInfo(Structure):
    """
    Descriptor for creating an OpenXR instance.

    This structure configures the parameters required to initialize an OpenXR runtime
    connection. It includes application metadata, optional API layers, requested extensions,
    and platform-specific chaining via the `next` pointer.

    A default instance may be constructed with no arguments, which will populate the
    `application_info` field with generic values and leave extensions and layers empty.
    The `enabled_api_layer_names` and `enabled_extension_names` properties provide access
    to the underlying string arrays and may be set directly.

    :param create_flags: Optional bitmask of creation flags. Reserved for future use.
    :type create_flags: xr.InstanceCreateFlags
    :param application_info: Metadata describing the application name, engine name, and API version.
    :type application_info: xr.ApplicationInfo
    :param enabled_api_layer_count: Number of API layers to enable. If None, inferred from `enabled_api_layer_names`.
    :type enabled_api_layer_count: int or None
    :param enabled_api_layer_names: List of API layer names to enable. Typically used for validation.
    :type enabled_api_layer_names: List[str] or None
    :param enabled_extension_count: Number of extensions to enable. If None, inferred from `enabled_extension_names`.
    :type enabled_extension_count: int or None
    :param enabled_extension_names: List of extension names to enable during instance creation.
    :type enabled_extension_names: List[str] or None
    :param next: Optional pointer to extension-specific structures for platform chaining.
    :type next: ctypes.c_void_p
    :param type: Structure type identifier. Defaults to `XR_TYPE_INSTANCE_CREATE_INFO`.
    :type type: xr.StructureType

    :property enabled_api_layer_names: Accessor for the API layer name array.
    :property enabled_extension_names: Accessor for the extension name array.

    :seealso: :class:`xr.Instance`, :class:`xr.ApplicationInfo`, :func:`xr.create_instance`
    :see: https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrInstanceCreateInfo.html
    """
    def __init__(
        self,
        create_flags: InstanceCreateFlags = InstanceCreateFlags(),  # noqa
        application_info: ApplicationInfo = ApplicationInfo(),
        enabled_api_layer_count: Optional[int] = None,
        enabled_api_layer_names: StringArrayFieldParamType = None,
        enabled_extension_count: Optional[int] = None,
        enabled_extension_names: StringArrayFieldParamType = None,
        next: c_void_p = None,
        type: StructureType = StructureType.INSTANCE_CREATE_INFO,
    ) -> None:
        if application_info is None:
            application_info = ApplicationInfo()
        enabled_api_layer_count, enabled_api_layer_names = string_array_field_helper(
            enabled_api_layer_count, enabled_api_layer_names)
        enabled_extension_count, enabled_extension_names = string_array_field_helper(
            enabled_extension_count, enabled_extension_names)
        super().__init__(
            create_flags=InstanceCreateFlags(create_flags).value,
            application_info=application_info,
            enabled_api_layer_count=enabled_api_layer_count,
            _enabled_api_layer_names=enabled_api_layer_names,
            enabled_extension_count=enabled_extension_count,
            _enabled_extension_names=enabled_extension_names,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.InstanceCreateInfo(create_flags={repr(self.create_flags)}, application_info={repr(self.application_info)}, enabled_api_layer_count={repr(self.enabled_api_layer_count)}, enabled_api_layer_names={repr(self._enabled_api_layer_names)}, enabled_extension_count={repr(self.enabled_extension_count)}, enabled_extension_names={repr(self._enabled_extension_names)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.InstanceCreateInfo(create_flags={self.create_flags}, application_info={self.application_info}, enabled_api_layer_count={self.enabled_api_layer_count}, enabled_api_layer_names={self._enabled_api_layer_names}, enabled_extension_count={self.enabled_extension_count}, enabled_extension_names={self._enabled_extension_names}, next={self.next}, type={self.type})"

    @property
    def enabled_api_layer_names(self):
        if self.enabled_api_layer_count == 0:
            return (c_char_p * 0)()
        else:
            return (c_char_p * self.enabled_api_layer_count).from_address(
                ctypes.addressof(self._enabled_api_layer_names.contents))

    @enabled_api_layer_names.setter
    def enabled_api_layer_names(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.enabled_api_layer_count, self._enabled_api_layer_names = string_array_field_helper(
            None, value)

    @property
    def enabled_extension_names(self):
        if self.enabled_extension_count == 0:
            return (c_char_p * 0)()
        else:
            return (c_char_p * self.enabled_extension_count).from_address(
                ctypes.addressof(self._enabled_extension_names.contents))

    @enabled_extension_names.setter
    def enabled_extension_names(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.enabled_extension_count, self._enabled_extension_names = string_array_field_helper(
            None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("create_flags", InstanceCreateFlagsCInt),
        ("application_info", ApplicationInfo),
        ("enabled_api_layer_count", c_uint32),
        ("_enabled_api_layer_names", POINTER(c_char_p)),
        ("enabled_extension_count", c_uint32),
        ("_enabled_extension_names", POINTER(c_char_p)),
    ]


class InstanceProperties(Structure):
    def __init__(
        self,
        runtime_version: Version = Version(),
        runtime_name: str = "",
        next: c_void_p = None,
        type: StructureType = StructureType.INSTANCE_PROPERTIES,
    ) -> None:
        super().__init__(
            _runtime_version=runtime_version.number(),
            runtime_name=runtime_name.encode(),
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.InstanceProperties(runtime_version={repr(self._runtime_version)}, runtime_name={repr(self.runtime_name)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.InstanceProperties(runtime_version={self._runtime_version}, runtime_name={self.runtime_name}, next={self.next}, type={self.type})"

    @property
    def runtime_version(self) -> Version:
        return Version(self._runtime_version)
    
    @runtime_version.setter
    def runtime_version(self, value: Version) -> None:
        if hasattr(value, 'number'):
            # noinspection PyAttributeOutsideInit
            self._runtime_version = value.number()
        else:
            # noinspection PyAttributeOutsideInit
            self._runtime_version = value

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("_runtime_version", VersionNumber),
        ("runtime_name", (c_char * 128)),
    ]


class EventDataBuffer(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_BUFFER,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataBuffer(varying={repr(self.varying)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataBuffer(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("varying", (c_uint8 * 4000)),
    ]


class SystemGetInfo(Structure):
    def __init__(
        self,
        form_factor: FormFactor = FormFactor(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_GET_INFO,
    ) -> None:
        super().__init__(
            form_factor=FormFactor(form_factor).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemGetInfo(form_factor={repr(self.form_factor)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemGetInfo(form_factor={self.form_factor}, next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_PROPERTIES,
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
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemProperties(system_id={repr(self.system_id)}, vendor_id={repr(self.vendor_id)}, system_name={repr(self.system_name)}, graphics_properties={repr(self.graphics_properties)}, tracking_properties={repr(self.tracking_properties)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemProperties(system_id={self.system_id}, vendor_id={self.vendor_id}, system_name={self.system_name}, graphics_properties={self.graphics_properties}, tracking_properties={self.tracking_properties}, next={self.next}, type={self.type})"

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
        create_flags: SessionCreateFlags = SessionCreateFlags(),  # noqa
        system_id: SystemId = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SESSION_CREATE_INFO,
    ) -> None:
        super().__init__(
            create_flags=SessionCreateFlags(create_flags).value,
            system_id=system_id,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SessionCreateInfo(create_flags={repr(self.create_flags)}, system_id={repr(self.system_id)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SessionCreateInfo(create_flags={self.create_flags}, system_id={self.system_id}, next={self.next}, type={self.type})"

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

    def __setitem__(self, key, value):
        self.as_numpy()[key] = value

    def __len__(self) -> int:
        return 3

    def as_numpy(self):
        if not hasattr(self, "_numpy") or self._numpy is None:
            # Just in time construction
            buffer = (c_float * len(self)).from_address(addressof(self))
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
        velocity_flags: SpaceVelocityFlags = SpaceVelocityFlags(),  # noqa
        linear_velocity: Vector3f = None,
        angular_velocity: Vector3f = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPACE_VELOCITY,
    ) -> None:
        if linear_velocity is None:
            linear_velocity = Vector3f()
        if angular_velocity is None:
            angular_velocity = Vector3f()
        super().__init__(
            velocity_flags=SpaceVelocityFlags(velocity_flags).value,
            linear_velocity=linear_velocity,
            angular_velocity=angular_velocity,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceVelocity(velocity_flags={repr(self.velocity_flags)}, linear_velocity={repr(self.linear_velocity)}, angular_velocity={repr(self.angular_velocity)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpaceVelocity(velocity_flags={self.velocity_flags}, linear_velocity={self.linear_velocity}, angular_velocity={self.angular_velocity}, next={self.next}, type={self.type})"

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

    def __setitem__(self, key, value):
        self.as_numpy()[key] = value

    def __len__(self) -> int:
        return 4

    def as_numpy(self):
        if not hasattr(self, "_numpy") or self._numpy is None:
            # Just in time construction
            buffer = (c_float * len(self)).from_address(addressof(self))
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
        reference_space_type: ReferenceSpaceType = ReferenceSpaceType.STAGE,
        pose_in_reference_space: Posef = Posef(),
        next: c_void_p = None,
        type: StructureType = StructureType.REFERENCE_SPACE_CREATE_INFO,
    ) -> None:
        super().__init__(
            reference_space_type=ReferenceSpaceType(reference_space_type).value,
            pose_in_reference_space=pose_in_reference_space,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ReferenceSpaceCreateInfo(reference_space_type={repr(self.reference_space_type)}, pose_in_reference_space={repr(self.pose_in_reference_space)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ReferenceSpaceCreateInfo(reference_space_type={self.reference_space_type}, pose_in_reference_space={self.pose_in_reference_space}, next={self.next}, type={self.type})"

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

    def __setitem__(self, key, value):
        self.as_numpy()[key] = value

    def __len__(self) -> int:
        return 2

    def as_numpy(self):
        if not hasattr(self, "_numpy") or self._numpy is None:
            # Just in time construction
            buffer = (c_float * len(self)).from_address(addressof(self))
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
        action: Action = None,
        subaction_path: Path = 0,
        pose_in_action_space: Posef = Posef(),
        next: c_void_p = None,
        type: StructureType = StructureType.ACTION_SPACE_CREATE_INFO,
    ) -> None:
        super().__init__(
            action=action,
            subaction_path=subaction_path,
            pose_in_action_space=pose_in_action_space,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ActionSpaceCreateInfo(action={repr(self.action)}, subaction_path={repr(self.subaction_path)}, pose_in_action_space={repr(self.pose_in_action_space)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ActionSpaceCreateInfo(action={self.action}, subaction_path={self.subaction_path}, pose_in_action_space={self.pose_in_action_space}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("action", Action),
        ("subaction_path", Path),
        ("pose_in_action_space", Posef),
    ]


class SpaceLocation(Structure):
    def __init__(
        self,
        location_flags: SpaceLocationFlags = SpaceLocationFlags(),  # noqa
        pose: Posef = Posef(),
        next: c_void_p = None,
        type: StructureType = StructureType.SPACE_LOCATION,
    ) -> None:
        super().__init__(
            location_flags=SpaceLocationFlags(location_flags).value,
            pose=pose,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceLocation(location_flags={repr(self.location_flags)}, pose={repr(self.pose)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpaceLocation(location_flags={self.location_flags}, pose={self.pose}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("location_flags", SpaceLocationFlagsCInt),
        ("pose", Posef),
    ]


class ViewConfigurationProperties(Structure):
    def __init__(
        self,
        view_configuration_type: ViewConfigurationType = ViewConfigurationType(),  # noqa
        fov_mutable: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.VIEW_CONFIGURATION_PROPERTIES,
    ) -> None:
        super().__init__(
            view_configuration_type=ViewConfigurationType(view_configuration_type).value,
            fov_mutable=fov_mutable,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ViewConfigurationProperties(view_configuration_type={repr(self.view_configuration_type)}, fov_mutable={repr(self.fov_mutable)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ViewConfigurationProperties(view_configuration_type={self.view_configuration_type}, fov_mutable={self.fov_mutable}, next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.VIEW_CONFIGURATION_VIEW,
    ) -> None:
        super().__init__(
            recommended_image_rect_width=recommended_image_rect_width,
            max_image_rect_width=max_image_rect_width,
            recommended_image_rect_height=recommended_image_rect_height,
            max_image_rect_height=max_image_rect_height,
            recommended_swapchain_sample_count=recommended_swapchain_sample_count,
            max_swapchain_sample_count=max_swapchain_sample_count,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ViewConfigurationView(recommended_image_rect_width={repr(self.recommended_image_rect_width)}, max_image_rect_width={repr(self.max_image_rect_width)}, recommended_image_rect_height={repr(self.recommended_image_rect_height)}, max_image_rect_height={repr(self.max_image_rect_height)}, recommended_swapchain_sample_count={repr(self.recommended_swapchain_sample_count)}, max_swapchain_sample_count={repr(self.max_swapchain_sample_count)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ViewConfigurationView(recommended_image_rect_width={self.recommended_image_rect_width}, max_image_rect_width={self.max_image_rect_width}, recommended_image_rect_height={self.recommended_image_rect_height}, max_image_rect_height={self.max_image_rect_height}, recommended_swapchain_sample_count={self.recommended_swapchain_sample_count}, max_swapchain_sample_count={self.max_swapchain_sample_count}, next={self.next}, type={self.type})"

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
        create_flags: SwapchainCreateFlags = SwapchainCreateFlags(),  # noqa
        usage_flags: SwapchainUsageFlags = SwapchainUsageFlags(),  # noqa
        format: int = 0,
        sample_count: int = 0,
        width: int = 0,
        height: int = 0,
        face_count: int = 0,
        array_size: int = 0,
        mip_count: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SWAPCHAIN_CREATE_INFO,
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
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainCreateInfo(create_flags={repr(self.create_flags)}, usage_flags={repr(self.usage_flags)}, format={repr(self.format)}, sample_count={repr(self.sample_count)}, width={repr(self.width)}, height={repr(self.height)}, face_count={repr(self.face_count)}, array_size={repr(self.array_size)}, mip_count={repr(self.mip_count)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainCreateInfo(create_flags={self.create_flags}, usage_flags={self.usage_flags}, format={self.format}, sample_count={self.sample_count}, width={self.width}, height={self.height}, face_count={self.face_count}, array_size={self.array_size}, mip_count={self.mip_count}, next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainImageBaseHeader(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageBaseHeader(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SwapchainImageAcquireInfo(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.SWAPCHAIN_IMAGE_ACQUIRE_INFO,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainImageAcquireInfo(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageAcquireInfo(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SwapchainImageWaitInfo(Structure):
    def __init__(
        self,
        timeout: Duration = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SWAPCHAIN_IMAGE_WAIT_INFO,
    ) -> None:
        super().__init__(
            timeout=timeout,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainImageWaitInfo(timeout={repr(self.timeout)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageWaitInfo(timeout={self.timeout}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("timeout", Duration),
    ]


class SwapchainImageReleaseInfo(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.SWAPCHAIN_IMAGE_RELEASE_INFO,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainImageReleaseInfo(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageReleaseInfo(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SessionBeginInfo(Structure):
    def __init__(
        self,
        primary_view_configuration_type: ViewConfigurationType = ViewConfigurationType(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.SESSION_BEGIN_INFO,
    ) -> None:
        super().__init__(
            primary_view_configuration_type=ViewConfigurationType(primary_view_configuration_type).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SessionBeginInfo(primary_view_configuration_type={repr(self.primary_view_configuration_type)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SessionBeginInfo(primary_view_configuration_type={self.primary_view_configuration_type}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("primary_view_configuration_type", ViewConfigurationType.ctype()),
    ]


class FrameWaitInfo(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.FRAME_WAIT_INFO,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FrameWaitInfo(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FrameWaitInfo(next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.FRAME_STATE,
    ) -> None:
        super().__init__(
            predicted_display_time=predicted_display_time,
            predicted_display_period=predicted_display_period,
            should_render=should_render,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FrameState(predicted_display_time={repr(self.predicted_display_time)}, predicted_display_period={repr(self.predicted_display_period)}, should_render={repr(self.should_render)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FrameState(predicted_display_time={self.predicted_display_time}, predicted_display_period={self.predicted_display_period}, should_render={self.should_render}, next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.FRAME_BEGIN_INFO,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FrameBeginInfo(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FrameBeginInfo(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class CompositionLayerBaseHeader(Structure):
    def __init__(
        self,
        layer_flags: CompositionLayerFlags = CompositionLayerFlags(),  # noqa
        space: Space = None,
        next: c_void_p = None,
        type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            layer_flags=CompositionLayerFlags(layer_flags).value,
            space=space,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerBaseHeader(layer_flags={repr(self.layer_flags)}, space={repr(self.space)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerBaseHeader(layer_flags={self.layer_flags}, space={self.space}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlagsCInt),
        ("space", Space),
    ]


class FrameEndInfo(Structure):
    def __init__(
        self,
        display_time: Time = 0,
        environment_blend_mode: EnvironmentBlendMode = EnvironmentBlendMode(),  # noqa
        layer_count: Optional[int] = None,
        layers: BaseArrayFieldParamType = None,
        next: c_void_p = None,
        type: StructureType = StructureType.FRAME_END_INFO,
    ) -> None:
        layer_count, layers = base_array_field_helper(
            POINTER(CompositionLayerBaseHeader), layer_count, layers)
        super().__init__(
            display_time=display_time,
            environment_blend_mode=EnvironmentBlendMode(environment_blend_mode).value,
            layer_count=layer_count,
            _layers=layers,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FrameEndInfo(display_time={repr(self.display_time)}, environment_blend_mode={repr(self.environment_blend_mode)}, layer_count={repr(self.layer_count)}, layers={repr(self._layers)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FrameEndInfo(display_time={self.display_time}, environment_blend_mode={self.environment_blend_mode}, layer_count={self.layer_count}, layers={self._layers}, next={self.next}, type={self.type})"

    @property
    def layers(self):
        if self.layer_count == 0:
            return (POINTER(CompositionLayerBaseHeader) * 0)()
        else:
            return (POINTER(CompositionLayerBaseHeader) * self.layer_count).from_address(
                ctypes.addressof(self._layers.contents))

    @layers.setter
    def layers(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.layer_count, self._layers = base_array_field_helper(
            POINTER(CompositionLayerBaseHeader), None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("display_time", Time),
        ("environment_blend_mode", EnvironmentBlendMode.ctype()),
        ("layer_count", c_uint32),
        ("_layers", POINTER(POINTER(CompositionLayerBaseHeader))),
    ]


class ViewLocateInfo(Structure):
    def __init__(
        self,
        view_configuration_type: ViewConfigurationType = ViewConfigurationType(),  # noqa
        display_time: Time = 0,
        space: Space = None,
        next: c_void_p = None,
        type: StructureType = StructureType.VIEW_LOCATE_INFO,
    ) -> None:
        super().__init__(
            view_configuration_type=ViewConfigurationType(view_configuration_type).value,
            display_time=display_time,
            space=space,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ViewLocateInfo(view_configuration_type={repr(self.view_configuration_type)}, display_time={repr(self.display_time)}, space={repr(self.space)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ViewLocateInfo(view_configuration_type={self.view_configuration_type}, display_time={self.display_time}, space={self.space}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_configuration_type", ViewConfigurationType.ctype()),
        ("display_time", Time),
        ("space", Space),
    ]


class ViewState(Structure):
    def __init__(
        self,
        view_state_flags: ViewStateFlags = ViewStateFlags(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.VIEW_STATE,
    ) -> None:
        super().__init__(
            view_state_flags=ViewStateFlags(view_state_flags).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ViewState(view_state_flags={repr(self.view_state_flags)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ViewState(view_state_flags={self.view_state_flags}, next={self.next}, type={self.type})"

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

    def __setitem__(self, key, value):
        self.as_numpy()[key] = value

    def __len__(self) -> int:
        return 4

    def as_numpy(self):
        if not hasattr(self, "_numpy") or self._numpy is None:
            # Just in time construction
            buffer = (c_float * len(self)).from_address(addressof(self))
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
        pose: Posef = Posef(),
        fov: Fovf = None,
        next: c_void_p = None,
        type: StructureType = StructureType.VIEW,
    ) -> None:
        if fov is None:
            fov = Fovf()
        super().__init__(
            pose=pose,
            fov=fov,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.View(pose={repr(self.pose)}, fov={repr(self.fov)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.View(pose={self.pose}, fov={self.fov}, next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.ACTION_SET_CREATE_INFO,
    ) -> None:
        super().__init__(
            action_set_name=action_set_name.encode(),
            localized_action_set_name=localized_action_set_name.encode(),
            priority=priority,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ActionSetCreateInfo(action_set_name={repr(self.action_set_name)}, localized_action_set_name={repr(self.localized_action_set_name)}, priority={repr(self.priority)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ActionSetCreateInfo(action_set_name={self.action_set_name}, localized_action_set_name={self.localized_action_set_name}, priority={self.priority}, next={self.next}, type={self.type})"

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
        action_type: ActionType = ActionType(),  # noqa
        count_subaction_paths: Optional[int] = None,
        subaction_paths: ArrayFieldParamType[c_uint64] = None,
        localized_action_name: str = "",
        next: c_void_p = None,
        type: StructureType = StructureType.ACTION_CREATE_INFO,
    ) -> None:
        count_subaction_paths, subaction_paths = array_field_helper(
            c_uint64, count_subaction_paths, subaction_paths)
        super().__init__(
            action_name=action_name.encode(),
            action_type=ActionType(action_type).value,
            count_subaction_paths=count_subaction_paths,
            _subaction_paths=subaction_paths,
            localized_action_name=localized_action_name.encode(),
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ActionCreateInfo(action_name={repr(self.action_name)}, action_type={repr(self.action_type)}, count_subaction_paths={repr(self.count_subaction_paths)}, subaction_paths={repr(self._subaction_paths)}, localized_action_name={repr(self.localized_action_name)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ActionCreateInfo(action_name={self.action_name}, action_type={self.action_type}, count_subaction_paths={self.count_subaction_paths}, subaction_paths={self._subaction_paths}, localized_action_name={self.localized_action_name}, next={self.next}, type={self.type})"

    @property
    def subaction_paths(self):
        if self.count_subaction_paths == 0:
            return (c_uint64 * 0)()
        else:
            return (c_uint64 * self.count_subaction_paths).from_address(
                ctypes.addressof(self._subaction_paths.contents))

    @subaction_paths.setter
    def subaction_paths(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.count_subaction_paths, self._subaction_paths = array_field_helper(
            c_uint64, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("action_name", (c_char * 64)),
        ("action_type", ActionType.ctype()),
        ("count_subaction_paths", c_uint32),
        ("_subaction_paths", POINTER(c_uint64)),
        ("localized_action_name", (c_char * 128)),
    ]


class ActionSuggestedBinding(Structure):
    def __init__(
        self,
        action: Action = None,
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
        ("action", Action),
        ("binding", Path),
    ]


class InteractionProfileSuggestedBinding(Structure):
    def __init__(
        self,
        interaction_profile: Path = 0,
        count_suggested_bindings: Optional[int] = None,
        suggested_bindings: ArrayFieldParamType[ActionSuggestedBinding] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.INTERACTION_PROFILE_SUGGESTED_BINDING,
    ) -> None:
        count_suggested_bindings, suggested_bindings = array_field_helper(
            ActionSuggestedBinding, count_suggested_bindings, suggested_bindings)
        super().__init__(
            interaction_profile=interaction_profile,
            count_suggested_bindings=count_suggested_bindings,
            _suggested_bindings=suggested_bindings,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.InteractionProfileSuggestedBinding(interaction_profile={repr(self.interaction_profile)}, count_suggested_bindings={repr(self.count_suggested_bindings)}, suggested_bindings={repr(self._suggested_bindings)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.InteractionProfileSuggestedBinding(interaction_profile={self.interaction_profile}, count_suggested_bindings={self.count_suggested_bindings}, suggested_bindings={self._suggested_bindings}, next={self.next}, type={self.type})"

    @property
    def suggested_bindings(self):
        if self.count_suggested_bindings == 0:
            return (ActionSuggestedBinding * 0)()
        else:
            return (ActionSuggestedBinding * self.count_suggested_bindings).from_address(
                ctypes.addressof(self._suggested_bindings.contents))

    @suggested_bindings.setter
    def suggested_bindings(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.count_suggested_bindings, self._suggested_bindings = array_field_helper(
            ActionSuggestedBinding, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("interaction_profile", Path),
        ("count_suggested_bindings", c_uint32),
        ("_suggested_bindings", POINTER(ActionSuggestedBinding)),
    ]


class SessionActionSetsAttachInfo(Structure):
    def __init__(
        self,
        count_action_sets: Optional[int] = None,
        action_sets: ArrayFieldParamType[ActionSet] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SESSION_ACTION_SETS_ATTACH_INFO,
    ) -> None:
        count_action_sets, action_sets = array_field_helper(
            ActionSet, count_action_sets, action_sets)
        super().__init__(
            count_action_sets=count_action_sets,
            _action_sets=action_sets,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SessionActionSetsAttachInfo(count_action_sets={repr(self.count_action_sets)}, action_sets={repr(self._action_sets)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SessionActionSetsAttachInfo(count_action_sets={self.count_action_sets}, action_sets={self._action_sets}, next={self.next}, type={self.type})"

    @property
    def action_sets(self):
        if self.count_action_sets == 0:
            return (ActionSet * 0)()
        else:
            return (ActionSet * self.count_action_sets).from_address(
                ctypes.addressof(self._action_sets.contents))

    @action_sets.setter
    def action_sets(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.count_action_sets, self._action_sets = array_field_helper(
            ActionSet, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("count_action_sets", c_uint32),
        ("_action_sets", POINTER(ActionSet)),
    ]


class InteractionProfileState(Structure):
    def __init__(
        self,
        interaction_profile: Path = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.INTERACTION_PROFILE_STATE,
    ) -> None:
        super().__init__(
            interaction_profile=interaction_profile,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.InteractionProfileState(interaction_profile={repr(self.interaction_profile)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.InteractionProfileState(interaction_profile={self.interaction_profile}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("interaction_profile", Path),
    ]


class ActionStateGetInfo(Structure):
    def __init__(
        self,
        action: Action = None,
        subaction_path: Path = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.ACTION_STATE_GET_INFO,
    ) -> None:
        super().__init__(
            action=action,
            subaction_path=subaction_path,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ActionStateGetInfo(action={repr(self.action)}, subaction_path={repr(self.subaction_path)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ActionStateGetInfo(action={self.action}, subaction_path={self.subaction_path}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("action", Action),
        ("subaction_path", Path),
    ]


class ActionStateBoolean(Structure):
    def __init__(
        self,
        current_state: Bool32 = 0,
        changed_since_last_sync: Bool32 = 0,
        last_change_time: Time = 0,
        is_active: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.ACTION_STATE_BOOLEAN,
    ) -> None:
        super().__init__(
            current_state=current_state,
            changed_since_last_sync=changed_since_last_sync,
            last_change_time=last_change_time,
            is_active=is_active,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ActionStateBoolean(current_state={repr(self.current_state)}, changed_since_last_sync={repr(self.changed_since_last_sync)}, last_change_time={repr(self.last_change_time)}, is_active={repr(self.is_active)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ActionStateBoolean(current_state={self.current_state}, changed_since_last_sync={self.changed_since_last_sync}, last_change_time={self.last_change_time}, is_active={self.is_active}, next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.ACTION_STATE_FLOAT,
    ) -> None:
        super().__init__(
            current_state=current_state,
            changed_since_last_sync=changed_since_last_sync,
            last_change_time=last_change_time,
            is_active=is_active,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ActionStateFloat(current_state={repr(self.current_state)}, changed_since_last_sync={repr(self.changed_since_last_sync)}, last_change_time={repr(self.last_change_time)}, is_active={repr(self.is_active)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ActionStateFloat(current_state={self.current_state:.3f}, changed_since_last_sync={self.changed_since_last_sync}, last_change_time={self.last_change_time}, is_active={self.is_active}, next={self.next}, type={self.type})"

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

    def __setitem__(self, key, value):
        self.as_numpy()[key] = value

    def __len__(self) -> int:
        return 2

    def as_numpy(self):
        if not hasattr(self, "_numpy") or self._numpy is None:
            # Just in time construction
            buffer = (c_float * len(self)).from_address(addressof(self))
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
        next: c_void_p = None,
        type: StructureType = StructureType.ACTION_STATE_VECTOR2F,
    ) -> None:
        if current_state is None:
            current_state = Vector2f()
        super().__init__(
            current_state=current_state,
            changed_since_last_sync=changed_since_last_sync,
            last_change_time=last_change_time,
            is_active=is_active,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ActionStateVector2f(current_state={repr(self.current_state)}, changed_since_last_sync={repr(self.changed_since_last_sync)}, last_change_time={repr(self.last_change_time)}, is_active={repr(self.is_active)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ActionStateVector2f(current_state={self.current_state}, changed_since_last_sync={self.changed_since_last_sync}, last_change_time={self.last_change_time}, is_active={self.is_active}, next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.ACTION_STATE_POSE,
    ) -> None:
        super().__init__(
            is_active=is_active,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ActionStatePose(is_active={repr(self.is_active)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ActionStatePose(is_active={self.is_active}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("is_active", Bool32),
    ]


class ActiveActionSet(Structure):
    def __init__(
        self,
        action_set: ActionSet = None,
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
        ("action_set", ActionSet),
        ("subaction_path", Path),
    ]


class ActionsSyncInfo(Structure):
    def __init__(
        self,
        count_active_action_sets: Optional[int] = None,
        active_action_sets: ArrayFieldParamType[ActiveActionSet] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.ACTIONS_SYNC_INFO,
    ) -> None:
        count_active_action_sets, active_action_sets = array_field_helper(
            ActiveActionSet, count_active_action_sets, active_action_sets)
        super().__init__(
            count_active_action_sets=count_active_action_sets,
            _active_action_sets=active_action_sets,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ActionsSyncInfo(count_active_action_sets={repr(self.count_active_action_sets)}, active_action_sets={repr(self._active_action_sets)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ActionsSyncInfo(count_active_action_sets={self.count_active_action_sets}, active_action_sets={self._active_action_sets}, next={self.next}, type={self.type})"

    @property
    def active_action_sets(self):
        if self.count_active_action_sets == 0:
            return (ActiveActionSet * 0)()
        else:
            return (ActiveActionSet * self.count_active_action_sets).from_address(
                ctypes.addressof(self._active_action_sets.contents))

    @active_action_sets.setter
    def active_action_sets(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.count_active_action_sets, self._active_action_sets = array_field_helper(
            ActiveActionSet, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("count_active_action_sets", c_uint32),
        ("_active_action_sets", POINTER(ActiveActionSet)),
    ]


class BoundSourcesForActionEnumerateInfo(Structure):
    def __init__(
        self,
        action: Action = None,
        next: c_void_p = None,
        type: StructureType = StructureType.BOUND_SOURCES_FOR_ACTION_ENUMERATE_INFO,
    ) -> None:
        super().__init__(
            action=action,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.BoundSourcesForActionEnumerateInfo(action={repr(self.action)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.BoundSourcesForActionEnumerateInfo(action={self.action}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("action", Action),
    ]


class InputSourceLocalizedNameGetInfo(Structure):
    def __init__(
        self,
        source_path: Path = 0,
        which_components: InputSourceLocalizedNameFlags = InputSourceLocalizedNameFlags(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.INPUT_SOURCE_LOCALIZED_NAME_GET_INFO,
    ) -> None:
        super().__init__(
            source_path=source_path,
            which_components=InputSourceLocalizedNameFlags(which_components).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.InputSourceLocalizedNameGetInfo(source_path={repr(self.source_path)}, which_components={repr(self.which_components)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.InputSourceLocalizedNameGetInfo(source_path={self.source_path}, which_components={self.which_components}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("source_path", Path),
        ("which_components", InputSourceLocalizedNameFlagsCInt),
    ]


class HapticActionInfo(Structure):
    def __init__(
        self,
        action: Action = None,
        subaction_path: Path = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.HAPTIC_ACTION_INFO,
    ) -> None:
        super().__init__(
            action=action,
            subaction_path=subaction_path,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.HapticActionInfo(action={repr(self.action)}, subaction_path={repr(self.subaction_path)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.HapticActionInfo(action={self.action}, subaction_path={self.subaction_path}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("action", Action),
        ("subaction_path", Path),
    ]


class HapticBaseHeader(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.HapticBaseHeader(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.HapticBaseHeader(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class BaseInStructure(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.BaseInStructure(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.BaseInStructure(next={self.next}, type={self.type})"

    pass


BaseInStructure._fields_ = [
    ("type", StructureType.ctype()),
    ("next", POINTER(BaseInStructure)),
]


class BaseOutStructure(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.BaseOutStructure(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.BaseOutStructure(next={self.next}, type={self.type})"

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
        self._numpy = None

    def __iter__(self) -> Generator[int, None, None]:
        yield self.x
        yield self.y

    def __getitem__(self, key):
        return tuple(self)[key]

    def __setitem__(self, key, value):
        self.as_numpy()[key] = value

    def __len__(self) -> int:
        return 2

    def as_numpy(self):
        if not hasattr(self, "_numpy") or self._numpy is None:
            # Just in time construction
            buffer = (c_int32 * len(self)).from_address(addressof(self))
            self._numpy = numpy.ctypeslib.as_array(buffer)
        return self._numpy

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
        self._numpy = None

    def __iter__(self) -> Generator[int, None, None]:
        yield self.width
        yield self.height

    def __getitem__(self, key):
        return tuple(self)[key]

    def __setitem__(self, key, value):
        self.as_numpy()[key] = value

    def __len__(self) -> int:
        return 2

    def as_numpy(self):
        if not hasattr(self, "_numpy") or self._numpy is None:
            # Just in time construction
            buffer = (c_int32 * len(self)).from_address(addressof(self))
            self._numpy = numpy.ctypeslib.as_array(buffer)
        return self._numpy

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
        swapchain: Swapchain = None,
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
        ("swapchain", Swapchain),
        ("image_rect", Rect2Di),
        ("image_array_index", c_uint32),
    ]


class CompositionLayerProjectionView(Structure):
    def __init__(
        self,
        pose: Posef = Posef(),
        fov: Fovf = None,
        sub_image: SwapchainSubImage = None,
        next: c_void_p = None,
        type: StructureType = StructureType.COMPOSITION_LAYER_PROJECTION_VIEW,
    ) -> None:
        if fov is None:
            fov = Fovf()
        if sub_image is None:
            sub_image = SwapchainSubImage()
        super().__init__(
            pose=pose,
            fov=fov,
            sub_image=sub_image,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerProjectionView(pose={repr(self.pose)}, fov={repr(self.fov)}, sub_image={repr(self.sub_image)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerProjectionView(pose={self.pose}, fov={self.fov}, sub_image={self.sub_image}, next={self.next}, type={self.type})"

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
        layer_flags: CompositionLayerFlags = CompositionLayerFlags(),  # noqa
        space: Space = None,
        view_count: Optional[int] = None,
        views: ArrayFieldParamType[CompositionLayerProjectionView] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.COMPOSITION_LAYER_PROJECTION,
    ) -> None:
        view_count, views = array_field_helper(
            CompositionLayerProjectionView, view_count, views)
        super().__init__(
            layer_flags=CompositionLayerFlags(layer_flags).value,
            space=space,
            view_count=view_count,
            _views=views,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerProjection(layer_flags={repr(self.layer_flags)}, space={repr(self.space)}, view_count={repr(self.view_count)}, views={repr(self._views)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerProjection(layer_flags={self.layer_flags}, space={self.space}, view_count={self.view_count}, views={self._views}, next={self.next}, type={self.type})"

    @property
    def views(self):
        if self.view_count == 0:
            return (CompositionLayerProjectionView * 0)()
        else:
            return (CompositionLayerProjectionView * self.view_count).from_address(
                ctypes.addressof(self._views.contents))

    @views.setter
    def views(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.view_count, self._views = array_field_helper(
            CompositionLayerProjectionView, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlagsCInt),
        ("space", Space),
        ("view_count", c_uint32),
        ("_views", POINTER(CompositionLayerProjectionView)),
    ]


class CompositionLayerQuad(Structure):
    def __init__(
        self,
        layer_flags: CompositionLayerFlags = CompositionLayerFlags(),  # noqa
        space: Space = None,
        eye_visibility: EyeVisibility = EyeVisibility(),  # noqa
        sub_image: SwapchainSubImage = None,
        pose: Posef = Posef(),
        size: Extent2Df = None,
        next: c_void_p = None,
        type: StructureType = StructureType.COMPOSITION_LAYER_QUAD,
    ) -> None:
        if sub_image is None:
            sub_image = SwapchainSubImage()
        if size is None:
            size = Extent2Df()
        super().__init__(
            layer_flags=CompositionLayerFlags(layer_flags).value,
            space=space,
            eye_visibility=EyeVisibility(eye_visibility).value,
            sub_image=sub_image,
            pose=pose,
            size=size,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerQuad(layer_flags={repr(self.layer_flags)}, space={repr(self.space)}, eye_visibility={repr(self.eye_visibility)}, sub_image={repr(self.sub_image)}, pose={repr(self.pose)}, size={repr(self.size)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerQuad(layer_flags={self.layer_flags}, space={self.space}, eye_visibility={self.eye_visibility}, sub_image={self.sub_image}, pose={self.pose}, size={self.size}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlagsCInt),
        ("space", Space),
        ("eye_visibility", EyeVisibility.ctype()),
        ("sub_image", SwapchainSubImage),
        ("pose", Posef),
        ("size", Extent2Df),
    ]


class EventDataBaseHeader(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataBaseHeader(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataBaseHeader(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class EventDataEventsLost(Structure):
    def __init__(
        self,
        lost_event_count: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_EVENTS_LOST,
    ) -> None:
        super().__init__(
            lost_event_count=lost_event_count,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataEventsLost(lost_event_count={repr(self.lost_event_count)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataEventsLost(lost_event_count={self.lost_event_count}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("lost_event_count", c_uint32),
    ]


class EventDataInstanceLossPending(Structure):
    def __init__(
        self,
        loss_time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_INSTANCE_LOSS_PENDING,
    ) -> None:
        super().__init__(
            loss_time=loss_time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataInstanceLossPending(loss_time={repr(self.loss_time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataInstanceLossPending(loss_time={self.loss_time}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("loss_time", Time),
    ]


class EventDataSessionStateChanged(Structure):
    def __init__(
        self,
        session: Session = None,
        state: SessionState = SessionState(),  # noqa
        time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_SESSION_STATE_CHANGED,
    ) -> None:
        super().__init__(
            session=session,
            state=SessionState(state).value,
            time=time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataSessionStateChanged(session={repr(self.session)}, state={repr(self.state)}, time={repr(self.time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataSessionStateChanged(session={self.session}, state={self.state}, time={self.time}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("session", Session),
        ("state", SessionState.ctype()),
        ("time", Time),
    ]


class EventDataReferenceSpaceChangePending(Structure):
    def __init__(
        self,
        session: Session = None,
        reference_space_type: ReferenceSpaceType = ReferenceSpaceType(),  # noqa
        change_time: Time = 0,
        pose_valid: Bool32 = 0,
        pose_in_previous_space: Posef = Posef(),
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_REFERENCE_SPACE_CHANGE_PENDING,
    ) -> None:
        super().__init__(
            session=session,
            reference_space_type=ReferenceSpaceType(reference_space_type).value,
            change_time=change_time,
            pose_valid=pose_valid,
            pose_in_previous_space=pose_in_previous_space,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataReferenceSpaceChangePending(session={repr(self.session)}, reference_space_type={repr(self.reference_space_type)}, change_time={repr(self.change_time)}, pose_valid={repr(self.pose_valid)}, pose_in_previous_space={repr(self.pose_in_previous_space)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataReferenceSpaceChangePending(session={self.session}, reference_space_type={self.reference_space_type}, change_time={self.change_time}, pose_valid={self.pose_valid}, pose_in_previous_space={self.pose_in_previous_space}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("session", Session),
        ("reference_space_type", ReferenceSpaceType.ctype()),
        ("change_time", Time),
        ("pose_valid", Bool32),
        ("pose_in_previous_space", Posef),
    ]


class EventDataInteractionProfileChanged(Structure):
    def __init__(
        self,
        session: Session = None,
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_INTERACTION_PROFILE_CHANGED,
    ) -> None:
        super().__init__(
            session=session,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataInteractionProfileChanged(session={repr(self.session)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataInteractionProfileChanged(session={self.session}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("session", Session),
    ]


class HapticVibration(Structure):
    def __init__(
        self,
        duration: Duration = 0,
        frequency: float = 0,
        amplitude: float = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.HAPTIC_VIBRATION,
    ) -> None:
        super().__init__(
            duration=duration,
            frequency=frequency,
            amplitude=amplitude,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.HapticVibration(duration={repr(self.duration)}, frequency={repr(self.frequency)}, amplitude={repr(self.amplitude)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.HapticVibration(duration={self.duration}, frequency={self.frequency:.3f}, amplitude={self.amplitude:.3f}, next={self.next}, type={self.type})"

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

    def __setitem__(self, key, value):
        self.as_numpy()[key] = value

    def __len__(self) -> int:
        return 2

    def as_numpy(self):
        if not hasattr(self, "_numpy") or self._numpy is None:
            # Just in time construction
            buffer = (c_float * len(self)).from_address(addressof(self))
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

    def __setitem__(self, key, value):
        self.as_numpy()[key] = value

    def __len__(self) -> int:
        return 4

    def as_numpy(self):
        if not hasattr(self, "_numpy") or self._numpy is None:
            # Just in time construction
            buffer = (c_float * len(self)).from_address(addressof(self))
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

    def __setitem__(self, key, value):
        self.as_numpy()[key] = value

    def __len__(self) -> int:
        return 4

    def as_numpy(self):
        if not hasattr(self, "_numpy") or self._numpy is None:
            # Just in time construction
            buffer = (c_float * len(self)).from_address(addressof(self))
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


PFN_xrGetInstanceProcAddr = CFUNCTYPE(Result.ctype(), Instance, c_char_p, POINTER(PFN_xrVoidFunction))

PFN_xrEnumerateApiLayerProperties = CFUNCTYPE(Result.ctype(), c_uint32, POINTER(c_uint32), POINTER(ApiLayerProperties))

PFN_xrEnumerateInstanceExtensionProperties = CFUNCTYPE(Result.ctype(), c_char_p, c_uint32, POINTER(c_uint32), POINTER(ExtensionProperties))

PFN_xrCreateInstance = CFUNCTYPE(Result.ctype(), POINTER(InstanceCreateInfo), POINTER(Instance))

PFN_xrDestroyInstance = CFUNCTYPE(Result.ctype(), Instance)

PFN_xrGetInstanceProperties = CFUNCTYPE(Result.ctype(), Instance, POINTER(InstanceProperties))

PFN_xrPollEvent = CFUNCTYPE(Result.ctype(), Instance, POINTER(EventDataBuffer))

PFN_xrResultToString = CFUNCTYPE(Result.ctype(), Instance, Result.ctype(), (c_char * 64))

PFN_xrStructureTypeToString = CFUNCTYPE(Result.ctype(), Instance, StructureType.ctype(), (c_char * 64))

PFN_xrGetSystem = CFUNCTYPE(Result.ctype(), Instance, POINTER(SystemGetInfo), POINTER(SystemId))

PFN_xrGetSystemProperties = CFUNCTYPE(Result.ctype(), Instance, SystemId, POINTER(SystemProperties))

PFN_xrEnumerateEnvironmentBlendModes = CFUNCTYPE(Result.ctype(), Instance, SystemId, ViewConfigurationType.ctype(), c_uint32, POINTER(c_uint32), POINTER(EnvironmentBlendMode.ctype()))

PFN_xrCreateSession = CFUNCTYPE(Result.ctype(), Instance, POINTER(SessionCreateInfo), POINTER(Session))

PFN_xrDestroySession = CFUNCTYPE(Result.ctype(), Session)

PFN_xrEnumerateReferenceSpaces = CFUNCTYPE(Result.ctype(), Session, c_uint32, POINTER(c_uint32), POINTER(ReferenceSpaceType.ctype()))

PFN_xrCreateReferenceSpace = CFUNCTYPE(Result.ctype(), Session, POINTER(ReferenceSpaceCreateInfo), POINTER(Space))

PFN_xrGetReferenceSpaceBoundsRect = CFUNCTYPE(Result.ctype(), Session, ReferenceSpaceType.ctype(), POINTER(Extent2Df))

PFN_xrCreateActionSpace = CFUNCTYPE(Result.ctype(), Session, POINTER(ActionSpaceCreateInfo), POINTER(Space))

PFN_xrLocateSpace = CFUNCTYPE(Result.ctype(), Space, Space, Time, POINTER(SpaceLocation))

PFN_xrDestroySpace = CFUNCTYPE(Result.ctype(), Space)

PFN_xrEnumerateViewConfigurations = CFUNCTYPE(Result.ctype(), Instance, SystemId, c_uint32, POINTER(c_uint32), POINTER(ViewConfigurationType.ctype()))

PFN_xrGetViewConfigurationProperties = CFUNCTYPE(Result.ctype(), Instance, SystemId, ViewConfigurationType.ctype(), POINTER(ViewConfigurationProperties))

PFN_xrEnumerateViewConfigurationViews = CFUNCTYPE(Result.ctype(), Instance, SystemId, ViewConfigurationType.ctype(), c_uint32, POINTER(c_uint32), POINTER(ViewConfigurationView))

PFN_xrEnumerateSwapchainFormats = CFUNCTYPE(Result.ctype(), Session, c_uint32, POINTER(c_uint32), POINTER(c_int64))

PFN_xrCreateSwapchain = CFUNCTYPE(Result.ctype(), Session, POINTER(SwapchainCreateInfo), POINTER(Swapchain))

PFN_xrDestroySwapchain = CFUNCTYPE(Result.ctype(), Swapchain)

PFN_xrEnumerateSwapchainImages = CFUNCTYPE(Result.ctype(), Swapchain, c_uint32, POINTER(c_uint32), POINTER(SwapchainImageBaseHeader))

PFN_xrAcquireSwapchainImage = CFUNCTYPE(Result.ctype(), Swapchain, POINTER(SwapchainImageAcquireInfo), POINTER(c_uint32))

PFN_xrWaitSwapchainImage = CFUNCTYPE(Result.ctype(), Swapchain, POINTER(SwapchainImageWaitInfo))

PFN_xrReleaseSwapchainImage = CFUNCTYPE(Result.ctype(), Swapchain, POINTER(SwapchainImageReleaseInfo))

PFN_xrBeginSession = CFUNCTYPE(Result.ctype(), Session, POINTER(SessionBeginInfo))

PFN_xrEndSession = CFUNCTYPE(Result.ctype(), Session)

PFN_xrRequestExitSession = CFUNCTYPE(Result.ctype(), Session)

PFN_xrWaitFrame = CFUNCTYPE(Result.ctype(), Session, POINTER(FrameWaitInfo), POINTER(FrameState))

PFN_xrBeginFrame = CFUNCTYPE(Result.ctype(), Session, POINTER(FrameBeginInfo))

PFN_xrEndFrame = CFUNCTYPE(Result.ctype(), Session, POINTER(FrameEndInfo))

PFN_xrLocateViews = CFUNCTYPE(Result.ctype(), Session, POINTER(ViewLocateInfo), POINTER(ViewState), c_uint32, POINTER(c_uint32), POINTER(View))

PFN_xrStringToPath = CFUNCTYPE(Result.ctype(), Instance, c_char_p, POINTER(Path))

PFN_xrPathToString = CFUNCTYPE(Result.ctype(), Instance, Path, c_uint32, POINTER(c_uint32), c_char_p)

PFN_xrCreateActionSet = CFUNCTYPE(Result.ctype(), Instance, POINTER(ActionSetCreateInfo), POINTER(ActionSet))

PFN_xrDestroyActionSet = CFUNCTYPE(Result.ctype(), ActionSet)

PFN_xrCreateAction = CFUNCTYPE(Result.ctype(), ActionSet, POINTER(ActionCreateInfo), POINTER(Action))

PFN_xrDestroyAction = CFUNCTYPE(Result.ctype(), Action)

PFN_xrSuggestInteractionProfileBindings = CFUNCTYPE(Result.ctype(), Instance, POINTER(InteractionProfileSuggestedBinding))

PFN_xrAttachSessionActionSets = CFUNCTYPE(Result.ctype(), Session, POINTER(SessionActionSetsAttachInfo))

PFN_xrGetCurrentInteractionProfile = CFUNCTYPE(Result.ctype(), Session, Path, POINTER(InteractionProfileState))

PFN_xrGetActionStateBoolean = CFUNCTYPE(Result.ctype(), Session, POINTER(ActionStateGetInfo), POINTER(ActionStateBoolean))

PFN_xrGetActionStateFloat = CFUNCTYPE(Result.ctype(), Session, POINTER(ActionStateGetInfo), POINTER(ActionStateFloat))

PFN_xrGetActionStateVector2f = CFUNCTYPE(Result.ctype(), Session, POINTER(ActionStateGetInfo), POINTER(ActionStateVector2f))

PFN_xrGetActionStatePose = CFUNCTYPE(Result.ctype(), Session, POINTER(ActionStateGetInfo), POINTER(ActionStatePose))

PFN_xrSyncActions = CFUNCTYPE(Result.ctype(), Session, POINTER(ActionsSyncInfo))

PFN_xrEnumerateBoundSourcesForAction = CFUNCTYPE(Result.ctype(), Session, POINTER(BoundSourcesForActionEnumerateInfo), c_uint32, POINTER(c_uint32), POINTER(Path))

PFN_xrGetInputSourceLocalizedName = CFUNCTYPE(Result.ctype(), Session, POINTER(InputSourceLocalizedNameGetInfo), c_uint32, POINTER(c_uint32), c_char_p)

PFN_xrApplyHapticFeedback = CFUNCTYPE(Result.ctype(), Session, POINTER(HapticActionInfo), POINTER(HapticBaseHeader))

PFN_xrStopHapticFeedback = CFUNCTYPE(Result.ctype(), Session, POINTER(HapticActionInfo))


class Color3f(Structure):
    def __init__(
        self,
        r: float = 0,
        g: float = 0,
        b: float = 0,
    ) -> None:
        super().__init__(
            r=r,
            g=g,
            b=b,
        )
        self._numpy = None

    def __iter__(self) -> Generator[float, None, None]:
        yield self.r
        yield self.g
        yield self.b

    def __getitem__(self, key):
        return tuple(self)[key]

    def __setitem__(self, key, value):
        self.as_numpy()[key] = value

    def __len__(self) -> int:
        return 3

    def as_numpy(self):
        if not hasattr(self, "_numpy") or self._numpy is None:
            # Just in time construction
            buffer = (c_float * len(self)).from_address(addressof(self))
            self._numpy = numpy.ctypeslib.as_array(buffer)
        return self._numpy

    def __repr__(self) -> str:
        return f"xr.Color3f(r={repr(self.r)}, g={repr(self.g)}, b={repr(self.b)})"

    def __str__(self) -> str:
        return f"xr.Color3f(r={self.r:.3f}, g={self.g:.3f}, b={self.b:.3f})"

    _fields_ = [
        ("r", c_float),
        ("g", c_float),
        ("b", c_float),
    ]


class Extent3Df(Structure):
    def __init__(
        self,
        width: float = 0,
        height: float = 0,
        depth: float = 0,
    ) -> None:
        super().__init__(
            width=width,
            height=height,
            depth=depth,
        )
        self._numpy = None

    def __iter__(self) -> Generator[float, None, None]:
        yield self.width
        yield self.height
        yield self.depth

    def __getitem__(self, key):
        return tuple(self)[key]

    def __setitem__(self, key, value):
        self.as_numpy()[key] = value

    def __len__(self) -> int:
        return 3

    def as_numpy(self):
        if not hasattr(self, "_numpy") or self._numpy is None:
            # Just in time construction
            buffer = (c_float * len(self)).from_address(addressof(self))
            self._numpy = numpy.ctypeslib.as_array(buffer)
        return self._numpy

    def __repr__(self) -> str:
        return f"xr.Extent3Df(width={repr(self.width)}, height={repr(self.height)}, depth={repr(self.depth)})"

    def __str__(self) -> str:
        return f"xr.Extent3Df(width={self.width:.3f}, height={self.height:.3f}, depth={self.depth:.3f})"

    _fields_ = [
        ("width", c_float),
        ("height", c_float),
        ("depth", c_float),
    ]


class Spheref(Structure):
    def __init__(
        self,
        center: Posef = Posef(),
        radius: float = 0,
    ) -> None:
        super().__init__(
            center=center,
            radius=radius,
        )

    def __repr__(self) -> str:
        return f"xr.Spheref(center={repr(self.center)}, radius={repr(self.radius)})"

    def __str__(self) -> str:
        return f"xr.Spheref(center={self.center}, radius={self.radius:.3f})"

    _fields_ = [
        ("center", Posef),
        ("radius", c_float),
    ]


class Boxf(Structure):
    def __init__(
        self,
        center: Posef = Posef(),
        extents: Extent3Df = None,
    ) -> None:
        if extents is None:
            extents = Extent3Df()
        super().__init__(
            center=center,
            extents=extents,
        )

    def __repr__(self) -> str:
        return f"xr.Boxf(center={repr(self.center)}, extents={repr(self.extents)})"

    def __str__(self) -> str:
        return f"xr.Boxf(center={self.center}, extents={self.extents})"

    _fields_ = [
        ("center", Posef),
        ("extents", Extent3Df),
    ]


class Frustumf(Structure):
    def __init__(
        self,
        pose: Posef = Posef(),
        fov: Fovf = None,
        near_z: float = 0,
        far_z: float = 0,
    ) -> None:
        if fov is None:
            fov = Fovf()
        super().__init__(
            pose=pose,
            fov=fov,
            near_z=near_z,
            far_z=far_z,
        )

    def __repr__(self) -> str:
        return f"xr.Frustumf(pose={repr(self.pose)}, fov={repr(self.fov)}, near_z={repr(self.near_z)}, far_z={repr(self.far_z)})"

    def __str__(self) -> str:
        return f"xr.Frustumf(pose={self.pose}, fov={self.fov}, near_z={self.near_z:.3f}, far_z={self.far_z:.3f})"

    _fields_ = [
        ("pose", Posef),
        ("fov", Fovf),
        ("near_z", c_float),
        ("far_z", c_float),
    ]


class Uuid(Structure):
    def __init__(
        self,
    ) -> None:
        super().__init__(
        )

    def __repr__(self) -> str:
        return f"xr.Uuid(data={repr(self.data)})"

    def __str__(self) -> str:
        return f"xr.Uuid()"

    _fields_ = [
        ("data", (c_uint8 * 16)),
    ]


class SpacesLocateInfo(Structure):
    def __init__(
        self,
        base_space: Space = None,
        time: Time = 0,
        space_count: Optional[int] = None,
        spaces: ArrayFieldParamType[Space] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPACES_LOCATE_INFO,
    ) -> None:
        space_count, spaces = array_field_helper(
            Space, space_count, spaces)
        super().__init__(
            base_space=base_space,
            time=time,
            space_count=space_count,
            _spaces=spaces,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpacesLocateInfo(base_space={repr(self.base_space)}, time={repr(self.time)}, space_count={repr(self.space_count)}, spaces={repr(self._spaces)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpacesLocateInfo(base_space={self.base_space}, time={self.time}, space_count={self.space_count}, spaces={self._spaces}, next={self.next}, type={self.type})"

    @property
    def spaces(self):
        if self.space_count == 0:
            return (Space * 0)()
        else:
            return (Space * self.space_count).from_address(
                ctypes.addressof(self._spaces.contents))

    @spaces.setter
    def spaces(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.space_count, self._spaces = array_field_helper(
            Space, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("base_space", Space),
        ("time", Time),
        ("space_count", c_uint32),
        ("_spaces", POINTER(Space)),
    ]


class SpaceLocationData(Structure):
    def __init__(
        self,
        location_flags: SpaceLocationFlags = SpaceLocationFlags(),  # noqa
        pose: Posef = Posef(),
    ) -> None:
        super().__init__(
            location_flags=SpaceLocationFlags(location_flags).value,
            pose=pose,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceLocationData(location_flags={repr(self.location_flags)}, pose={repr(self.pose)})"

    def __str__(self) -> str:
        return f"xr.SpaceLocationData(location_flags={self.location_flags}, pose={self.pose})"

    _fields_ = [
        ("location_flags", SpaceLocationFlagsCInt),
        ("pose", Posef),
    ]


class SpaceLocations(Structure):
    def __init__(
        self,
        location_count: Optional[int] = None,
        locations: ArrayFieldParamType[SpaceLocationData] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPACE_LOCATIONS,
    ) -> None:
        location_count, locations = array_field_helper(
            SpaceLocationData, location_count, locations)
        super().__init__(
            location_count=location_count,
            _locations=locations,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceLocations(location_count={repr(self.location_count)}, locations={repr(self._locations)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpaceLocations(location_count={self.location_count}, locations={self._locations}, next={self.next}, type={self.type})"

    @property
    def locations(self):
        if self.location_count == 0:
            return (SpaceLocationData * 0)()
        else:
            return (SpaceLocationData * self.location_count).from_address(
                ctypes.addressof(self._locations.contents))

    @locations.setter
    def locations(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.location_count, self._locations = array_field_helper(
            SpaceLocationData, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("location_count", c_uint32),
        ("_locations", POINTER(SpaceLocationData)),
    ]


class SpaceVelocityData(Structure):
    def __init__(
        self,
        velocity_flags: SpaceVelocityFlags = SpaceVelocityFlags(),  # noqa
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
        return f"xr.SpaceVelocityData(velocity_flags={repr(self.velocity_flags)}, linear_velocity={repr(self.linear_velocity)}, angular_velocity={repr(self.angular_velocity)})"

    def __str__(self) -> str:
        return f"xr.SpaceVelocityData(velocity_flags={self.velocity_flags}, linear_velocity={self.linear_velocity}, angular_velocity={self.angular_velocity})"

    _fields_ = [
        ("velocity_flags", SpaceVelocityFlagsCInt),
        ("linear_velocity", Vector3f),
        ("angular_velocity", Vector3f),
    ]


class SpaceVelocities(Structure):
    def __init__(
        self,
        velocity_count: int = 0,
        velocities: POINTER(SpaceVelocityData) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPACE_VELOCITIES,
    ) -> None:
        super().__init__(
            velocity_count=velocity_count,
            velocities=velocities,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceVelocities(velocity_count={repr(self.velocity_count)}, velocities={repr(self.velocities)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpaceVelocities(velocity_count={self.velocity_count}, velocities={self.velocities}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("velocity_count", c_uint32),
        ("velocities", POINTER(SpaceVelocityData)),
    ]


PFN_xrLocateSpaces = CFUNCTYPE(Result.ctype(), Session, POINTER(SpacesLocateInfo), POINTER(SpaceLocations))


class CompositionLayerCubeKHR(Structure):
    def __init__(
        self,
        layer_flags: CompositionLayerFlags = CompositionLayerFlags(),  # noqa
        space: Space = None,
        eye_visibility: EyeVisibility = EyeVisibility(),  # noqa
        swapchain: Swapchain = None,
        image_array_index: int = 0,
        orientation: Quaternionf = None,
        next: c_void_p = None,
        type: StructureType = StructureType.COMPOSITION_LAYER_CUBE_KHR,
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
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerCubeKHR(layer_flags={repr(self.layer_flags)}, space={repr(self.space)}, eye_visibility={repr(self.eye_visibility)}, swapchain={repr(self.swapchain)}, image_array_index={repr(self.image_array_index)}, orientation={repr(self.orientation)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerCubeKHR(layer_flags={self.layer_flags}, space={self.space}, eye_visibility={self.eye_visibility}, swapchain={self.swapchain}, image_array_index={self.image_array_index}, orientation={self.orientation}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlagsCInt),
        ("space", Space),
        ("eye_visibility", EyeVisibility.ctype()),
        ("swapchain", Swapchain),
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
        next: c_void_p = None,
        type: StructureType = StructureType.COMPOSITION_LAYER_DEPTH_INFO_KHR,
    ) -> None:
        if sub_image is None:
            sub_image = SwapchainSubImage()
        super().__init__(
            sub_image=sub_image,
            min_depth=min_depth,
            max_depth=max_depth,
            near_z=near_z,
            far_z=far_z,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerDepthInfoKHR(sub_image={repr(self.sub_image)}, min_depth={repr(self.min_depth)}, max_depth={repr(self.max_depth)}, near_z={repr(self.near_z)}, far_z={repr(self.far_z)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerDepthInfoKHR(sub_image={self.sub_image}, min_depth={self.min_depth:.3f}, max_depth={self.max_depth:.3f}, near_z={self.near_z:.3f}, far_z={self.far_z:.3f}, next={self.next}, type={self.type})"

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
        layer_flags: CompositionLayerFlags = CompositionLayerFlags(),  # noqa
        space: Space = None,
        eye_visibility: EyeVisibility = EyeVisibility(),  # noqa
        sub_image: SwapchainSubImage = None,
        pose: Posef = Posef(),
        radius: float = 0,
        central_angle: float = 0,
        aspect_ratio: float = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.COMPOSITION_LAYER_CYLINDER_KHR,
    ) -> None:
        if sub_image is None:
            sub_image = SwapchainSubImage()
        super().__init__(
            layer_flags=CompositionLayerFlags(layer_flags).value,
            space=space,
            eye_visibility=EyeVisibility(eye_visibility).value,
            sub_image=sub_image,
            pose=pose,
            radius=radius,
            central_angle=central_angle,
            aspect_ratio=aspect_ratio,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerCylinderKHR(layer_flags={repr(self.layer_flags)}, space={repr(self.space)}, eye_visibility={repr(self.eye_visibility)}, sub_image={repr(self.sub_image)}, pose={repr(self.pose)}, radius={repr(self.radius)}, central_angle={repr(self.central_angle)}, aspect_ratio={repr(self.aspect_ratio)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerCylinderKHR(layer_flags={self.layer_flags}, space={self.space}, eye_visibility={self.eye_visibility}, sub_image={self.sub_image}, pose={self.pose}, radius={self.radius:.3f}, central_angle={self.central_angle:.3f}, aspect_ratio={self.aspect_ratio:.3f}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlagsCInt),
        ("space", Space),
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
        layer_flags: CompositionLayerFlags = CompositionLayerFlags(),  # noqa
        space: Space = None,
        eye_visibility: EyeVisibility = EyeVisibility(),  # noqa
        sub_image: SwapchainSubImage = None,
        pose: Posef = Posef(),
        radius: float = 0,
        scale: Vector2f = None,
        bias: Vector2f = None,
        next: c_void_p = None,
        type: StructureType = StructureType.COMPOSITION_LAYER_EQUIRECT_KHR,
    ) -> None:
        if sub_image is None:
            sub_image = SwapchainSubImage()
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
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerEquirectKHR(layer_flags={repr(self.layer_flags)}, space={repr(self.space)}, eye_visibility={repr(self.eye_visibility)}, sub_image={repr(self.sub_image)}, pose={repr(self.pose)}, radius={repr(self.radius)}, scale={repr(self.scale)}, bias={repr(self.bias)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerEquirectKHR(layer_flags={self.layer_flags}, space={self.space}, eye_visibility={self.eye_visibility}, sub_image={self.sub_image}, pose={self.pose}, radius={self.radius:.3f}, scale={self.scale}, bias={self.bias}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlagsCInt),
        ("space", Space),
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
        next: c_void_p = None,
        type: StructureType = StructureType.VISIBILITY_MASK_KHR,
    ) -> None:
        super().__init__(
            vertex_capacity_input=vertex_capacity_input,
            vertex_count_output=vertex_count_output,
            vertices=vertices,
            index_capacity_input=index_capacity_input,
            index_count_output=index_count_output,
            indices=indices,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.VisibilityMaskKHR(vertex_capacity_input={repr(self.vertex_capacity_input)}, vertex_count_output={repr(self.vertex_count_output)}, vertices={repr(self.vertices)}, index_capacity_input={repr(self.index_capacity_input)}, index_count_output={repr(self.index_count_output)}, indices={repr(self.indices)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.VisibilityMaskKHR(vertex_capacity_input={self.vertex_capacity_input}, vertex_count_output={self.vertex_count_output}, vertices={self.vertices}, index_capacity_input={self.index_capacity_input}, index_count_output={self.index_count_output}, indices={self.indices}, next={self.next}, type={self.type})"

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
        session: Session = None,
        view_configuration_type: ViewConfigurationType = ViewConfigurationType(),  # noqa
        view_index: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_VISIBILITY_MASK_CHANGED_KHR,
    ) -> None:
        super().__init__(
            session=session,
            view_configuration_type=ViewConfigurationType(view_configuration_type).value,
            view_index=view_index,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataVisibilityMaskChangedKHR(session={repr(self.session)}, view_configuration_type={repr(self.view_configuration_type)}, view_index={repr(self.view_index)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataVisibilityMaskChangedKHR(session={self.session}, view_configuration_type={self.view_configuration_type}, view_index={self.view_index}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("session", Session),
        ("view_configuration_type", ViewConfigurationType.ctype()),
        ("view_index", c_uint32),
    ]


PFN_xrGetVisibilityMaskKHR = CFUNCTYPE(Result.ctype(), Session, ViewConfigurationType.ctype(), c_uint32, VisibilityMaskTypeKHR.ctype(), POINTER(VisibilityMaskKHR))


class CompositionLayerColorScaleBiasKHR(Structure):
    def __init__(
        self,
        color_scale: Color4f = None,
        color_bias: Color4f = None,
        next: c_void_p = None,
        type: StructureType = StructureType.COMPOSITION_LAYER_COLOR_SCALE_BIAS_KHR,
    ) -> None:
        if color_scale is None:
            color_scale = Color4f()
        if color_bias is None:
            color_bias = Color4f()
        super().__init__(
            color_scale=color_scale,
            color_bias=color_bias,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerColorScaleBiasKHR(color_scale={repr(self.color_scale)}, color_bias={repr(self.color_bias)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerColorScaleBiasKHR(color_scale={self.color_scale}, color_bias={self.color_bias}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("color_scale", Color4f),
        ("color_bias", Color4f),
    ]


class LoaderInitInfoBaseHeaderKHR(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.LoaderInitInfoBaseHeaderKHR(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.LoaderInitInfoBaseHeaderKHR(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


PFN_xrInitializeLoaderKHR = CFUNCTYPE(Result.ctype(), POINTER(LoaderInitInfoBaseHeaderKHR))


class CompositionLayerEquirect2KHR(Structure):
    def __init__(
        self,
        layer_flags: CompositionLayerFlags = CompositionLayerFlags(),  # noqa
        space: Space = None,
        eye_visibility: EyeVisibility = EyeVisibility(),  # noqa
        sub_image: SwapchainSubImage = None,
        pose: Posef = Posef(),
        radius: float = 0,
        central_horizontal_angle: float = 0,
        upper_vertical_angle: float = 0,
        lower_vertical_angle: float = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.COMPOSITION_LAYER_EQUIRECT2_KHR,
    ) -> None:
        if sub_image is None:
            sub_image = SwapchainSubImage()
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
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerEquirect2KHR(layer_flags={repr(self.layer_flags)}, space={repr(self.space)}, eye_visibility={repr(self.eye_visibility)}, sub_image={repr(self.sub_image)}, pose={repr(self.pose)}, radius={repr(self.radius)}, central_horizontal_angle={repr(self.central_horizontal_angle)}, upper_vertical_angle={repr(self.upper_vertical_angle)}, lower_vertical_angle={repr(self.lower_vertical_angle)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerEquirect2KHR(layer_flags={self.layer_flags}, space={self.space}, eye_visibility={self.eye_visibility}, sub_image={self.sub_image}, pose={self.pose}, radius={self.radius:.3f}, central_horizontal_angle={self.central_horizontal_angle:.3f}, upper_vertical_angle={self.upper_vertical_angle:.3f}, lower_vertical_angle={self.lower_vertical_angle:.3f}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlagsCInt),
        ("space", Space),
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
        next: c_void_p = None,
        type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.BindingModificationBaseHeaderKHR(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.BindingModificationBaseHeaderKHR(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class BindingModificationsKHR(Structure):
    def __init__(
        self,
        binding_modification_count: Optional[int] = None,
        binding_modifications: BaseArrayFieldParamType = None,
        next: c_void_p = None,
        type: StructureType = StructureType.BINDING_MODIFICATIONS_KHR,
    ) -> None:
        binding_modification_count, binding_modifications = base_array_field_helper(
            POINTER(BindingModificationBaseHeaderKHR), binding_modification_count, binding_modifications)
        super().__init__(
            binding_modification_count=binding_modification_count,
            _binding_modifications=binding_modifications,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.BindingModificationsKHR(binding_modification_count={repr(self.binding_modification_count)}, binding_modifications={repr(self._binding_modifications)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.BindingModificationsKHR(binding_modification_count={self.binding_modification_count}, binding_modifications={self._binding_modifications}, next={self.next}, type={self.type})"

    @property
    def binding_modifications(self):
        if self.binding_modification_count == 0:
            return (POINTER(BindingModificationBaseHeaderKHR) * 0)()
        else:
            return (POINTER(BindingModificationBaseHeaderKHR) * self.binding_modification_count).from_address(
                ctypes.addressof(self._binding_modifications.contents))

    @binding_modifications.setter
    def binding_modifications(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.binding_modification_count, self._binding_modifications = base_array_field_helper(
            POINTER(BindingModificationBaseHeaderKHR), None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("binding_modification_count", c_uint32),
        ("_binding_modifications", POINTER(POINTER(BindingModificationBaseHeaderKHR))),
    ]


PFN_xrStructureTypeToString2KHR = CFUNCTYPE(Result.ctype(), Instance, StructureType.ctype(), (c_char * 256))

SpacesLocateInfoKHR = SpacesLocateInfo

SpaceLocationDataKHR = SpaceLocationData

SpaceLocationsKHR = SpaceLocations

SpaceVelocityDataKHR = SpaceVelocityData

SpaceVelocitiesKHR = SpaceVelocities

PFN_xrLocateSpacesKHR = CFUNCTYPE(Result.ctype(), Session, POINTER(SpacesLocateInfo), POINTER(SpaceLocations))

Color3fKHR = Color3f

Extent3DfKHR = Extent3Df

SpherefKHR = Spheref

BoxfKHR = Boxf

FrustumfKHR = Frustumf


class EventDataPerfSettingsEXT(Structure):
    def __init__(
        self,
        domain: PerfSettingsDomainEXT = PerfSettingsDomainEXT(),  # noqa
        sub_domain: PerfSettingsSubDomainEXT = PerfSettingsSubDomainEXT(),  # noqa
        from_level: PerfSettingsNotificationLevelEXT = PerfSettingsNotificationLevelEXT(),  # noqa
        to_level: PerfSettingsNotificationLevelEXT = PerfSettingsNotificationLevelEXT(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_PERF_SETTINGS_EXT,
    ) -> None:
        super().__init__(
            domain=PerfSettingsDomainEXT(domain).value,
            sub_domain=PerfSettingsSubDomainEXT(sub_domain).value,
            from_level=PerfSettingsNotificationLevelEXT(from_level).value,
            to_level=PerfSettingsNotificationLevelEXT(to_level).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataPerfSettingsEXT(domain={repr(self.domain)}, sub_domain={repr(self.sub_domain)}, from_level={repr(self.from_level)}, to_level={repr(self.to_level)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataPerfSettingsEXT(domain={self.domain}, sub_domain={self.sub_domain}, from_level={self.from_level}, to_level={self.to_level}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("domain", PerfSettingsDomainEXT.ctype()),
        ("sub_domain", PerfSettingsSubDomainEXT.ctype()),
        ("from_level", PerfSettingsNotificationLevelEXT.ctype()),
        ("to_level", PerfSettingsNotificationLevelEXT.ctype()),
    ]


PFN_xrPerfSettingsSetPerformanceLevelEXT = CFUNCTYPE(Result.ctype(), Session, PerfSettingsDomainEXT.ctype(), PerfSettingsLevelEXT.ctype())

PFN_xrThermalGetTemperatureTrendEXT = CFUNCTYPE(Result.ctype(), Session, PerfSettingsDomainEXT.ctype(), POINTER(PerfSettingsNotificationLevelEXT.ctype()), POINTER(c_float), POINTER(c_float))


class DebugUtilsMessengerEXT_T(Structure):
    pass


class DebugUtilsMessengerEXT(POINTER(DebugUtilsMessengerEXT_T), HandleMixin):
    """
    Opaque handle to an OpenXR debug messenger object.

    A `xr.DebugUtilsMessengerEXT` enables runtime diagnostics and logging via the
    `XR_EXT_debug_utils` extension. It allows applications to receive structured
    messages from the runtime, including validation errors, warnings, and performance
    hints.

    This object wraps the native `xrCreateDebugUtilsMessengerEXT` and
    `xrDestroyDebugUtilsMessengerEXT` calls. It supports context management for
    automatic teardown, though manual destruction via :func:`xr.ext.EXT.debug_utils.destroy_messenger`
    is preferred for explicit control.

    .. code-block:: python

        from xr.ext.EXT import debug_utils

        with xr.DebugUtilsMessengerEXT(instance) as messenger:
            ...

    The `create_info` parameter may be omitted to use default settings, which enable all
    message types and severities and use the built-in `_default_debug_callback`.

    :param instance: The OpenXR instance to bind the messenger to.
    :type instance: xr.Instance
    :param create_info: Optional descriptor specifying callback behavior and message filtering.
    :type create_info: xr.DebugUtilsMessengerCreateInfoEXT or None

    :raises xr.FunctionUnsupportedError: If `XR_EXT_debug_utils` is not enabled or the function is unavailable.
    :raises xr.ValidationFailureError: If the callback or parameters are rejected by the runtime.
    :raises xr.RuntimeFailureError: If the runtime encounters an internal error.
    :raises xr.HandleInvalidError: If the instance handle is invalid.
    :raises xr.InstanceLostError: If the instance has been lost.
    :raises xr.OutOfMemoryError: If the runtime cannot allocate the messenger.
    :raises xr.LimitReachedError: If the runtime cannot support additional messengers.
    :seealso: :class:`xr.DebugUtilsMessengerCreateInfoEXT`, :func:`xr.ext.EXT.debug_utils.destroy_messenger`
    :see: https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrDebugUtilsMessengerEXT.html
    """
    _type_ = DebugUtilsMessengerEXT_T  # ctypes idiosyncrasy

DebugUtilsMessageSeverityFlagsEXTCInt = Flags64

DebugUtilsMessageTypeFlagsEXTCInt = Flags64


class DebugUtilsObjectNameInfoEXT(Structure):
    def __init__(
        self,
        object_type: ObjectType = ObjectType(),  # noqa
        object_handle: int = 0,
        object_name: str = "",
        next: c_void_p = None,
        type: StructureType = StructureType.DEBUG_UTILS_OBJECT_NAME_INFO_EXT,
    ) -> None:
        super().__init__(
            object_type=ObjectType(object_type).value,
            object_handle=object_handle,
            _object_name=object_name.encode(),
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.DebugUtilsObjectNameInfoEXT(object_type={repr(self.object_type)}, object_handle={repr(self.object_handle)}, object_name={repr(self._object_name)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.DebugUtilsObjectNameInfoEXT(object_type={self.object_type}, object_handle={self.object_handle}, object_name={self._object_name}, next={self.next}, type={self.type})"

    @property
    def object_name(self) -> str:
        return self._object_name.decode()
    
    @object_name.setter
    def object_name(self, value: str) -> None:
        # noinspection PyAttributeOutsideInit
        self._object_name = value.encode()

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("object_type", ObjectType.ctype()),
        ("object_handle", c_uint64),
        ("_object_name", c_char_p),
    ]


class DebugUtilsLabelEXT(Structure):
    def __init__(
        self,
        label_name: str = "",
        next: c_void_p = None,
        type: StructureType = StructureType.DEBUG_UTILS_LABEL_EXT,
    ) -> None:
        super().__init__(
            _label_name=label_name.encode(),
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.DebugUtilsLabelEXT(label_name={repr(self._label_name)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.DebugUtilsLabelEXT(label_name={self._label_name}, next={self.next}, type={self.type})"

    @property
    def label_name(self) -> str:
        return self._label_name.decode()
    
    @label_name.setter
    def label_name(self, value: str) -> None:
        # noinspection PyAttributeOutsideInit
        self._label_name = value.encode()

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("_label_name", c_char_p),
    ]


class DebugUtilsMessengerCallbackDataEXT(Structure):
    def __init__(
        self,
        message_id: str = "",
        function_name: str = "",
        message: str = "",
        object_count: Optional[int] = None,
        objects: ArrayFieldParamType[DebugUtilsObjectNameInfoEXT] = None,
        session_label_count: Optional[int] = None,
        session_labels: ArrayFieldParamType[DebugUtilsLabelEXT] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.DEBUG_UTILS_MESSENGER_CALLBACK_DATA_EXT,
    ) -> None:
        object_count, objects = array_field_helper(
            DebugUtilsObjectNameInfoEXT, object_count, objects)
        session_label_count, session_labels = array_field_helper(
            DebugUtilsLabelEXT, session_label_count, session_labels)
        super().__init__(
            _message_id=message_id.encode(),
            _function_name=function_name.encode(),
            _message=message.encode(),
            object_count=object_count,
            _objects=objects,
            session_label_count=session_label_count,
            _session_labels=session_labels,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.DebugUtilsMessengerCallbackDataEXT(message_id={repr(self._message_id)}, function_name={repr(self._function_name)}, message={repr(self._message)}, object_count={repr(self.object_count)}, objects={repr(self._objects)}, session_label_count={repr(self.session_label_count)}, session_labels={repr(self._session_labels)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.DebugUtilsMessengerCallbackDataEXT(message_id={self._message_id}, function_name={self._function_name}, message={self._message}, object_count={self.object_count}, objects={self._objects}, session_label_count={self.session_label_count}, session_labels={self._session_labels}, next={self.next}, type={self.type})"

    @property
    def message_id(self) -> str:
        return self._message_id.decode()
    
    @message_id.setter
    def message_id(self, value: str) -> None:
        # noinspection PyAttributeOutsideInit
        self._message_id = value.encode()

    @property
    def function_name(self) -> str:
        return self._function_name.decode()
    
    @function_name.setter
    def function_name(self, value: str) -> None:
        # noinspection PyAttributeOutsideInit
        self._function_name = value.encode()

    @property
    def message(self) -> str:
        return self._message.decode()
    
    @message.setter
    def message(self, value: str) -> None:
        # noinspection PyAttributeOutsideInit
        self._message = value.encode()

    @property
    def objects(self):
        if self.object_count == 0:
            return (DebugUtilsObjectNameInfoEXT * 0)()
        else:
            return (DebugUtilsObjectNameInfoEXT * self.object_count).from_address(
                ctypes.addressof(self._objects.contents))

    @objects.setter
    def objects(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.object_count, self._objects = array_field_helper(
            DebugUtilsObjectNameInfoEXT, None, value)

    @property
    def session_labels(self):
        if self.session_label_count == 0:
            return (DebugUtilsLabelEXT * 0)()
        else:
            return (DebugUtilsLabelEXT * self.session_label_count).from_address(
                ctypes.addressof(self._session_labels.contents))

    @session_labels.setter
    def session_labels(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.session_label_count, self._session_labels = array_field_helper(
            DebugUtilsLabelEXT, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("_message_id", c_char_p),
        ("_function_name", c_char_p),
        ("_message", c_char_p),
        ("object_count", c_uint32),
        ("_objects", POINTER(DebugUtilsObjectNameInfoEXT)),
        ("session_label_count", c_uint32),
        ("_session_labels", POINTER(DebugUtilsLabelEXT)),
    ]


PFN_xrDebugUtilsMessengerCallbackEXT = CFUNCTYPE(Bool32, DebugUtilsMessageSeverityFlagsEXTCInt, DebugUtilsMessageTypeFlagsEXTCInt, POINTER(DebugUtilsMessengerCallbackDataEXT), c_void_p)

# TODO: inject these three items in the generator:

DebugCallbackType = Callable[[
    DebugUtilsMessageSeverityFlagsEXT,
    DebugUtilsMessageTypeFlagsEXT,
    DebugUtilsMessengerCallbackDataEXT,
    c_void_p,
], bool]


def default_debug_callback(
        severity: DebugUtilsMessageSeverityFlagsEXT,
        type_flags: DebugUtilsMessageTypeFlagsEXT,
        callback_data: "DebugUtilsMessengerCallbackDataEXT",
        _user_data: c_void_p,
) -> bool:
    """
    Default diagnostic callback for `XR_EXT_debug_utils`.

    This function is invoked by the OpenXR runtime when a debug message is emitted.
    It prints the message to standard output, including severity, type, and function name.

    This is a minimal implementation intended primarily as a reference or starting point
    for client applications. Users are encouraged to implement their own callback to
    integrate with logging frameworks, telemetry systems, or custom filtering logic.

    :param severity: Bitmask of message severity flags.
    :type severity: xr.DebugUtilsMessageSeverityFlagsEXT
    :param type_flags: Bitmask of message type flags.
    :type type_flags: xr.DebugUtilsMessageTypeFlagsEXT
    :param callback_data: Pointer to a populated `DebugUtilsMessengerCallbackDataEXT` structure.
    :type callback_data: ctypes.POINTER(xr.DebugUtilsMessengerCallbackDataEXT)
    :param _user_data: Optional user data passed during messenger creation. Unused by default.
    :type _user_data: ctypes.c_void_p

    :seealso: :class:`xr.DebugUtilsMessengerCreateInfoEXT`, :class:`xr.DebugUtilsMessengerEXT`
    """

    message = callback_data.message
    func_name = callback_data.function_name
    print(f"[XR DEBUG] Severity={severity} Type={type_flags} Message={message} Function={func_name}")
    return False  # important!


def wrap_debug_callback(user_callback: DebugCallbackType, user_data: Any):
    def _shim(
            severity: int,
            type_flags: int,
            callback_data_ptr: POINTER("DebugUtilsMessengerCallbackDataEXT"),
            _user_data_ptr: c_void_p,
    ):
        try:
            severity_enum = DebugUtilsMessageSeverityFlagsEXT(severity)
            type_enum = DebugUtilsMessageTypeFlagsEXT(type_flags)
            callback_data = callback_data_ptr.contents
            return user_callback(severity_enum, type_enum, callback_data, user_data)
        except Exception as e:
            print(f"Exception in debug callback: {e}")
            return False
    return PFN_xrDebugUtilsMessengerCallbackEXT(_shim)


class DebugUtilsMessengerCreateInfoEXT(Structure):
    """
    Descriptor for creating a debug messenger via `XR_EXT_debug_utils`.

    This structure configures the behavior of a debug messenger, including which
    message severities and types to receive, and the callback function to invoke.

    A default instance may be constructed with no arguments, enabling all message
    types and severities and using the built-in `_default_debug_callback`.

    :param message_severities: Bitmask of message severities to receive.
    :type message_severities: xr.DebugUtilsMessageSeverityFlagsEXT
    :param message_types: Bitmask of message types to receive.
    :type message_types: xr.DebugUtilsMessageTypeFlagsEXT
    :param user_callback: Python callable accepting `(severity, type_flags, callback_data, user_data)`.
                          This will be wrapped into a native function pointer.
    :type user_callback: Callable[[int, int,
                                   ctypes.POINTER(xr.DebugUtilsMessengerCallbackDataEXT), ctypes.c_void_p], bool]
    :param user_data: Optional Python object passed to the callback.
    :type user_data: Any
    :param next: Optional pointer to extension-specific structures.
    :type next: ctypes.c_void_p
    :param type: Structure type identifier. Defaults to `DEBUG_UTILS_MESSENGER_CREATE_INFO_EXT`.
    :type type: xr.StructureType

    :seealso: :class:`xr.DebugUtilsMessengerEXT`, :func:`xr.ext.EXT.debug_utils._default_debug_callback`
    :see: https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrDebugUtilsMessengerCreateInfoEXT.html
    """

    def __init__(
        self,
        message_severities: DebugUtilsMessageSeverityFlagsEXT = (
            DebugUtilsMessageSeverityFlagsEXT.ERROR_BIT
            | DebugUtilsMessageSeverityFlagsEXT.WARNING_BIT
            | DebugUtilsMessageSeverityFlagsEXT.INFO_BIT
            | DebugUtilsMessageSeverityFlagsEXT.VERBOSE_BIT),
        message_types: DebugUtilsMessageTypeFlagsEXT = (
            DebugUtilsMessageTypeFlagsEXT.CONFORMANCE_BIT
            | DebugUtilsMessageTypeFlagsEXT.GENERAL_BIT
            | DebugUtilsMessageTypeFlagsEXT.PERFORMANCE_BIT
            | DebugUtilsMessageTypeFlagsEXT.VALIDATION_BIT),
        user_callback: DebugCallbackType = default_debug_callback,
        user_data: Any = None,
        next: c_void_p = None,
        type: StructureType = StructureType.DEBUG_UTILS_MESSENGER_CREATE_INFO_EXT,
    ) -> None:
        self._cached_user_data = user_data  # in case it does not fit in a c_void_p
        super().__init__(
            message_severities=DebugUtilsMessageSeverityFlagsEXT(message_severities).value,
            message_types=DebugUtilsMessageTypeFlagsEXT(message_types).value,
            _user_callback=wrap_debug_callback(user_callback, user_data),
            _user_data=cast(py_object(user_data), c_void_p) if user_data else None,
            next=next,
            type=type,
        )

    @property
    def user_data(self):
        return self._cached_user_data

    @user_data.setter
    def user_data(self, value: Any):
        self._cached_user_data = value
        self._user_data = cast(py_object(value), c_void_p) if value else None

    @property
    def user_callback(self) -> PFN_xrDebugUtilsMessengerCallbackEXT:
        return self._user_callback

    @user_callback.setter
    def user_callback(
            self,
            user_callback: DebugCallbackType,
    ) -> None:
        self._user_callback = wrap_debug_callback(user_callback, self._cached_user_data)

    def __repr__(self) -> str:
        return f"xr.DebugUtilsMessengerCreateInfoEXT(message_severities={repr(self.message_severities)}, message_types={repr(self.message_types)}, user_callback={repr(self.user_callback)}, user_data={repr(self.user_data)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.DebugUtilsMessengerCreateInfoEXT(message_severities={self.message_severities}, message_types={self.message_types}, user_callback={self.user_callback}, user_data={self.user_data}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("message_severities", DebugUtilsMessageSeverityFlagsEXTCInt),
        ("message_types", DebugUtilsMessageTypeFlagsEXTCInt),
        ("_user_callback", PFN_xrDebugUtilsMessengerCallbackEXT),
        ("user_data", c_void_p),
    ]


PFN_xrSetDebugUtilsObjectNameEXT = CFUNCTYPE(Result.ctype(), Instance, POINTER(DebugUtilsObjectNameInfoEXT))

PFN_xrCreateDebugUtilsMessengerEXT = CFUNCTYPE(Result.ctype(), Instance, POINTER(DebugUtilsMessengerCreateInfoEXT), POINTER(DebugUtilsMessengerEXT))

PFN_xrDestroyDebugUtilsMessengerEXT = CFUNCTYPE(Result.ctype(), DebugUtilsMessengerEXT)

PFN_xrSubmitDebugUtilsMessageEXT = CFUNCTYPE(Result.ctype(), Instance, DebugUtilsMessageSeverityFlagsEXTCInt, DebugUtilsMessageTypeFlagsEXTCInt, POINTER(DebugUtilsMessengerCallbackDataEXT))

PFN_xrSessionBeginDebugUtilsLabelRegionEXT = CFUNCTYPE(Result.ctype(), Session, POINTER(DebugUtilsLabelEXT))

PFN_xrSessionEndDebugUtilsLabelRegionEXT = CFUNCTYPE(Result.ctype(), Session)

PFN_xrSessionInsertDebugUtilsLabelEXT = CFUNCTYPE(Result.ctype(), Session, POINTER(DebugUtilsLabelEXT))


class SystemEyeGazeInteractionPropertiesEXT(Structure):
    def __init__(
        self,
        supports_eye_gaze_interaction: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_EYE_GAZE_INTERACTION_PROPERTIES_EXT,
    ) -> None:
        super().__init__(
            supports_eye_gaze_interaction=supports_eye_gaze_interaction,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemEyeGazeInteractionPropertiesEXT(supports_eye_gaze_interaction={repr(self.supports_eye_gaze_interaction)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemEyeGazeInteractionPropertiesEXT(supports_eye_gaze_interaction={self.supports_eye_gaze_interaction}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_eye_gaze_interaction", Bool32),
    ]


class EyeGazeSampleTimeEXT(Structure):
    def __init__(
        self,
        time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.EYE_GAZE_SAMPLE_TIME_EXT,
    ) -> None:
        super().__init__(
            time=time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EyeGazeSampleTimeEXT(time={repr(self.time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EyeGazeSampleTimeEXT(time={self.time}, next={self.next}, type={self.type})"

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
        create_flags: OverlaySessionCreateFlagsEXTX = OverlaySessionCreateFlagsEXTX(),  # noqa
        session_layers_placement: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SESSION_CREATE_INFO_OVERLAY_EXTX,
    ) -> None:
        super().__init__(
            create_flags=OverlaySessionCreateFlagsEXTX(create_flags).value,
            session_layers_placement=session_layers_placement,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SessionCreateInfoOverlayEXTX(create_flags={repr(self.create_flags)}, session_layers_placement={repr(self.session_layers_placement)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SessionCreateInfoOverlayEXTX(create_flags={self.create_flags}, session_layers_placement={self.session_layers_placement}, next={self.next}, type={self.type})"

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
        flags: OverlayMainSessionFlagsEXTX = OverlayMainSessionFlagsEXTX(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_MAIN_SESSION_VISIBILITY_CHANGED_EXTX,
    ) -> None:
        super().__init__(
            visible=visible,
            flags=OverlayMainSessionFlagsEXTX(flags).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataMainSessionVisibilityChangedEXTX(visible={repr(self.visible)}, flags={repr(self.flags)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataMainSessionVisibilityChangedEXTX(visible={self.visible}, flags={self.flags}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("visible", Bool32),
        ("flags", OverlayMainSessionFlagsEXTXCInt),
    ]


class SpatialAnchorMSFT_T(Structure):
    pass


class SpatialAnchorMSFT(POINTER(SpatialAnchorMSFT_T), HandleMixin):
    _type_ = SpatialAnchorMSFT_T  # ctypes idiosyncrasy


class SpatialAnchorCreateInfoMSFT(Structure):
    def __init__(
        self,
        space: Space = None,
        pose: Posef = Posef(),
        time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHOR_CREATE_INFO_MSFT,
    ) -> None:
        super().__init__(
            space=space,
            pose=pose,
            time=time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorCreateInfoMSFT(space={repr(self.space)}, pose={repr(self.pose)}, time={repr(self.time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorCreateInfoMSFT(space={self.space}, pose={self.pose}, time={self.time}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("space", Space),
        ("pose", Posef),
        ("time", Time),
    ]


class SpatialAnchorSpaceCreateInfoMSFT(Structure):
    def __init__(
        self,
        anchor: SpatialAnchorMSFT = None,
        pose_in_anchor_space: Posef = Posef(),
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHOR_SPACE_CREATE_INFO_MSFT,
    ) -> None:
        super().__init__(
            anchor=anchor,
            pose_in_anchor_space=pose_in_anchor_space,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorSpaceCreateInfoMSFT(anchor={repr(self.anchor)}, pose_in_anchor_space={repr(self.pose_in_anchor_space)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorSpaceCreateInfoMSFT(anchor={self.anchor}, pose_in_anchor_space={self.pose_in_anchor_space}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("anchor", SpatialAnchorMSFT),
        ("pose_in_anchor_space", Posef),
    ]


PFN_xrCreateSpatialAnchorMSFT = CFUNCTYPE(Result.ctype(), Session, POINTER(SpatialAnchorCreateInfoMSFT), POINTER(SpatialAnchorMSFT))

PFN_xrCreateSpatialAnchorSpaceMSFT = CFUNCTYPE(Result.ctype(), Session, POINTER(SpatialAnchorSpaceCreateInfoMSFT), POINTER(Space))

PFN_xrDestroySpatialAnchorMSFT = CFUNCTYPE(Result.ctype(), SpatialAnchorMSFT)

CompositionLayerImageLayoutFlagsFBCInt = Flags64


class CompositionLayerImageLayoutFB(Structure):
    def __init__(
        self,
        flags: CompositionLayerImageLayoutFlagsFB = CompositionLayerImageLayoutFlagsFB(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.COMPOSITION_LAYER_IMAGE_LAYOUT_FB,
    ) -> None:
        super().__init__(
            flags=CompositionLayerImageLayoutFlagsFB(flags).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerImageLayoutFB(flags={repr(self.flags)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerImageLayoutFB(flags={self.flags}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", CompositionLayerImageLayoutFlagsFBCInt),
    ]


class CompositionLayerAlphaBlendFB(Structure):
    def __init__(
        self,
        src_factor_color: BlendFactorFB = BlendFactorFB(),  # noqa
        dst_factor_color: BlendFactorFB = BlendFactorFB(),  # noqa
        src_factor_alpha: BlendFactorFB = BlendFactorFB(),  # noqa
        dst_factor_alpha: BlendFactorFB = BlendFactorFB(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.COMPOSITION_LAYER_ALPHA_BLEND_FB,
    ) -> None:
        super().__init__(
            src_factor_color=BlendFactorFB(src_factor_color).value,
            dst_factor_color=BlendFactorFB(dst_factor_color).value,
            src_factor_alpha=BlendFactorFB(src_factor_alpha).value,
            dst_factor_alpha=BlendFactorFB(dst_factor_alpha).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerAlphaBlendFB(src_factor_color={repr(self.src_factor_color)}, dst_factor_color={repr(self.dst_factor_color)}, src_factor_alpha={repr(self.src_factor_alpha)}, dst_factor_alpha={repr(self.dst_factor_alpha)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerAlphaBlendFB(src_factor_color={self.src_factor_color}, dst_factor_color={self.dst_factor_color}, src_factor_alpha={self.src_factor_alpha}, dst_factor_alpha={self.dst_factor_alpha}, next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.VIEW_CONFIGURATION_DEPTH_RANGE_EXT,
    ) -> None:
        super().__init__(
            recommended_near_z=recommended_near_z,
            min_near_z=min_near_z,
            recommended_far_z=recommended_far_z,
            max_far_z=max_far_z,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ViewConfigurationDepthRangeEXT(recommended_near_z={repr(self.recommended_near_z)}, min_near_z={repr(self.min_near_z)}, recommended_far_z={repr(self.recommended_far_z)}, max_far_z={repr(self.max_far_z)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ViewConfigurationDepthRangeEXT(recommended_near_z={self.recommended_near_z:.3f}, min_near_z={self.min_near_z:.3f}, recommended_far_z={self.recommended_far_z:.3f}, max_far_z={self.max_far_z:.3f}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("recommended_near_z", c_float),
        ("min_near_z", c_float),
        ("recommended_far_z", c_float),
        ("max_far_z", c_float),
    ]


PFN_xrSetInputDeviceActiveEXT = CFUNCTYPE(Result.ctype(), Session, Path, Path, Bool32)

PFN_xrSetInputDeviceStateBoolEXT = CFUNCTYPE(Result.ctype(), Session, Path, Path, Bool32)

PFN_xrSetInputDeviceStateFloatEXT = CFUNCTYPE(Result.ctype(), Session, Path, Path, c_float)

PFN_xrSetInputDeviceStateVector2fEXT = CFUNCTYPE(Result.ctype(), Session, Path, Path, Vector2f)

PFN_xrSetInputDeviceLocationEXT = CFUNCTYPE(Result.ctype(), Session, Path, Path, Space, Posef)


class SpatialGraphNodeBindingMSFT_T(Structure):
    pass


class SpatialGraphNodeBindingMSFT(POINTER(SpatialGraphNodeBindingMSFT_T), HandleMixin):
    _type_ = SpatialGraphNodeBindingMSFT_T  # ctypes idiosyncrasy


class SpatialGraphNodeSpaceCreateInfoMSFT(Structure):
    def __init__(
        self,
        node_type: SpatialGraphNodeTypeMSFT = SpatialGraphNodeTypeMSFT(),  # noqa
        pose: Posef = Posef(),
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_GRAPH_NODE_SPACE_CREATE_INFO_MSFT,
    ) -> None:
        super().__init__(
            node_type=SpatialGraphNodeTypeMSFT(node_type).value,
            pose=pose,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialGraphNodeSpaceCreateInfoMSFT(node_type={repr(self.node_type)}, node_id={repr(self.node_id)}, pose={repr(self.pose)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialGraphNodeSpaceCreateInfoMSFT(node_type={self.node_type}, pose={self.pose}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("node_type", SpatialGraphNodeTypeMSFT.ctype()),
        ("node_id", (c_uint8 * 16)),
        ("pose", Posef),
    ]


class SpatialGraphStaticNodeBindingCreateInfoMSFT(Structure):
    def __init__(
        self,
        space: Space = None,
        pose_in_space: Posef = Posef(),
        time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_GRAPH_STATIC_NODE_BINDING_CREATE_INFO_MSFT,
    ) -> None:
        super().__init__(
            space=space,
            pose_in_space=pose_in_space,
            time=time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialGraphStaticNodeBindingCreateInfoMSFT(space={repr(self.space)}, pose_in_space={repr(self.pose_in_space)}, time={repr(self.time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialGraphStaticNodeBindingCreateInfoMSFT(space={self.space}, pose_in_space={self.pose_in_space}, time={self.time}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("space", Space),
        ("pose_in_space", Posef),
        ("time", Time),
    ]


class SpatialGraphNodeBindingPropertiesGetInfoMSFT(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_GRAPH_NODE_BINDING_PROPERTIES_GET_INFO_MSFT,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialGraphNodeBindingPropertiesGetInfoMSFT(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialGraphNodeBindingPropertiesGetInfoMSFT(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SpatialGraphNodeBindingPropertiesMSFT(Structure):
    def __init__(
        self,
        pose_in_node_space: Posef = Posef(),
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_GRAPH_NODE_BINDING_PROPERTIES_MSFT,
    ) -> None:
        super().__init__(
            pose_in_node_space=pose_in_node_space,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialGraphNodeBindingPropertiesMSFT(node_id={repr(self.node_id)}, pose_in_node_space={repr(self.pose_in_node_space)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialGraphNodeBindingPropertiesMSFT(pose_in_node_space={self.pose_in_node_space}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("node_id", (c_uint8 * 16)),
        ("pose_in_node_space", Posef),
    ]


PFN_xrCreateSpatialGraphNodeSpaceMSFT = CFUNCTYPE(Result.ctype(), Session, POINTER(SpatialGraphNodeSpaceCreateInfoMSFT), POINTER(Space))

PFN_xrTryCreateSpatialGraphStaticNodeBindingMSFT = CFUNCTYPE(Result.ctype(), Session, POINTER(SpatialGraphStaticNodeBindingCreateInfoMSFT), POINTER(SpatialGraphNodeBindingMSFT))

PFN_xrDestroySpatialGraphNodeBindingMSFT = CFUNCTYPE(Result.ctype(), SpatialGraphNodeBindingMSFT)

PFN_xrGetSpatialGraphNodeBindingPropertiesMSFT = CFUNCTYPE(Result.ctype(), SpatialGraphNodeBindingMSFT, POINTER(SpatialGraphNodeBindingPropertiesGetInfoMSFT), POINTER(SpatialGraphNodeBindingPropertiesMSFT))


class HandTrackerEXT_T(Structure):
    pass


class HandTrackerEXT(POINTER(HandTrackerEXT_T), HandleMixin):
    _type_ = HandTrackerEXT_T  # ctypes idiosyncrasy


class SystemHandTrackingPropertiesEXT(Structure):
    def __init__(
        self,
        supports_hand_tracking: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_HAND_TRACKING_PROPERTIES_EXT,
    ) -> None:
        super().__init__(
            supports_hand_tracking=supports_hand_tracking,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemHandTrackingPropertiesEXT(supports_hand_tracking={repr(self.supports_hand_tracking)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemHandTrackingPropertiesEXT(supports_hand_tracking={self.supports_hand_tracking}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_hand_tracking", Bool32),
    ]


class HandTrackerCreateInfoEXT(Structure):
    def __init__(
        self,
        hand: HandEXT = HandEXT(),  # noqa
        hand_joint_set: HandJointSetEXT = HandJointSetEXT(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.HAND_TRACKER_CREATE_INFO_EXT,
    ) -> None:
        super().__init__(
            hand=HandEXT(hand).value,
            hand_joint_set=HandJointSetEXT(hand_joint_set).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.HandTrackerCreateInfoEXT(hand={repr(self.hand)}, hand_joint_set={repr(self.hand_joint_set)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.HandTrackerCreateInfoEXT(hand={self.hand}, hand_joint_set={self.hand_joint_set}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("hand", HandEXT.ctype()),
        ("hand_joint_set", HandJointSetEXT.ctype()),
    ]


class HandJointsLocateInfoEXT(Structure):
    def __init__(
        self,
        base_space: Space = None,
        time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.HAND_JOINTS_LOCATE_INFO_EXT,
    ) -> None:
        super().__init__(
            base_space=base_space,
            time=time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.HandJointsLocateInfoEXT(base_space={repr(self.base_space)}, time={repr(self.time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.HandJointsLocateInfoEXT(base_space={self.base_space}, time={self.time}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("base_space", Space),
        ("time", Time),
    ]


class HandJointLocationEXT(Structure):
    def __init__(
        self,
        location_flags: SpaceLocationFlags = SpaceLocationFlags(),  # noqa
        pose: Posef = Posef(),
        radius: float = 0,
    ) -> None:
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
        velocity_flags: SpaceVelocityFlags = SpaceVelocityFlags(),  # noqa
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
        joint_count: Optional[int] = None,
        joint_locations: ArrayFieldParamType[HandJointLocationEXT] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.HAND_JOINT_LOCATIONS_EXT,
    ) -> None:
        joint_count, joint_locations = array_field_helper(
            HandJointLocationEXT, joint_count, joint_locations)
        super().__init__(
            is_active=is_active,
            joint_count=joint_count,
            _joint_locations=joint_locations,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.HandJointLocationsEXT(is_active={repr(self.is_active)}, joint_count={repr(self.joint_count)}, joint_locations={repr(self._joint_locations)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.HandJointLocationsEXT(is_active={self.is_active}, joint_count={self.joint_count}, joint_locations={self._joint_locations}, next={self.next}, type={self.type})"

    @property
    def joint_locations(self):
        if self.joint_count == 0:
            return (HandJointLocationEXT * 0)()
        else:
            return (HandJointLocationEXT * self.joint_count).from_address(
                ctypes.addressof(self._joint_locations.contents))

    @joint_locations.setter
    def joint_locations(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.joint_count, self._joint_locations = array_field_helper(
            HandJointLocationEXT, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("is_active", Bool32),
        ("joint_count", c_uint32),
        ("_joint_locations", POINTER(HandJointLocationEXT)),
    ]


class HandJointVelocitiesEXT(Structure):
    def __init__(
        self,
        joint_count: Optional[int] = None,
        joint_velocities: ArrayFieldParamType[HandJointVelocityEXT] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.HAND_JOINT_VELOCITIES_EXT,
    ) -> None:
        joint_count, joint_velocities = array_field_helper(
            HandJointVelocityEXT, joint_count, joint_velocities)
        super().__init__(
            joint_count=joint_count,
            _joint_velocities=joint_velocities,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.HandJointVelocitiesEXT(joint_count={repr(self.joint_count)}, joint_velocities={repr(self._joint_velocities)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.HandJointVelocitiesEXT(joint_count={self.joint_count}, joint_velocities={self._joint_velocities}, next={self.next}, type={self.type})"

    @property
    def joint_velocities(self):
        if self.joint_count == 0:
            return (HandJointVelocityEXT * 0)()
        else:
            return (HandJointVelocityEXT * self.joint_count).from_address(
                ctypes.addressof(self._joint_velocities.contents))

    @joint_velocities.setter
    def joint_velocities(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.joint_count, self._joint_velocities = array_field_helper(
            HandJointVelocityEXT, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("joint_count", c_uint32),
        ("_joint_velocities", POINTER(HandJointVelocityEXT)),
    ]


PFN_xrCreateHandTrackerEXT = CFUNCTYPE(Result.ctype(), Session, POINTER(HandTrackerCreateInfoEXT), POINTER(HandTrackerEXT))

PFN_xrDestroyHandTrackerEXT = CFUNCTYPE(Result.ctype(), HandTrackerEXT)

PFN_xrLocateHandJointsEXT = CFUNCTYPE(Result.ctype(), HandTrackerEXT, POINTER(HandJointsLocateInfoEXT), POINTER(HandJointLocationsEXT))


class SystemHandTrackingMeshPropertiesMSFT(Structure):
    def __init__(
        self,
        supports_hand_tracking_mesh: Bool32 = 0,
        max_hand_mesh_index_count: int = 0,
        max_hand_mesh_vertex_count: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_HAND_TRACKING_MESH_PROPERTIES_MSFT,
    ) -> None:
        super().__init__(
            supports_hand_tracking_mesh=supports_hand_tracking_mesh,
            max_hand_mesh_index_count=max_hand_mesh_index_count,
            max_hand_mesh_vertex_count=max_hand_mesh_vertex_count,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemHandTrackingMeshPropertiesMSFT(supports_hand_tracking_mesh={repr(self.supports_hand_tracking_mesh)}, max_hand_mesh_index_count={repr(self.max_hand_mesh_index_count)}, max_hand_mesh_vertex_count={repr(self.max_hand_mesh_vertex_count)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemHandTrackingMeshPropertiesMSFT(supports_hand_tracking_mesh={self.supports_hand_tracking_mesh}, max_hand_mesh_index_count={self.max_hand_mesh_index_count}, max_hand_mesh_vertex_count={self.max_hand_mesh_vertex_count}, next={self.next}, type={self.type})"

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
        hand_pose_type: HandPoseTypeMSFT = HandPoseTypeMSFT(),  # noqa
        pose_in_hand_mesh_space: Posef = Posef(),
        next: c_void_p = None,
        type: StructureType = StructureType.HAND_MESH_SPACE_CREATE_INFO_MSFT,
    ) -> None:
        super().__init__(
            hand_pose_type=HandPoseTypeMSFT(hand_pose_type).value,
            pose_in_hand_mesh_space=pose_in_hand_mesh_space,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.HandMeshSpaceCreateInfoMSFT(hand_pose_type={repr(self.hand_pose_type)}, pose_in_hand_mesh_space={repr(self.pose_in_hand_mesh_space)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.HandMeshSpaceCreateInfoMSFT(hand_pose_type={self.hand_pose_type}, pose_in_hand_mesh_space={self.pose_in_hand_mesh_space}, next={self.next}, type={self.type})"

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
        hand_pose_type: HandPoseTypeMSFT = HandPoseTypeMSFT(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.HAND_MESH_UPDATE_INFO_MSFT,
    ) -> None:
        super().__init__(
            time=time,
            hand_pose_type=HandPoseTypeMSFT(hand_pose_type).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.HandMeshUpdateInfoMSFT(time={repr(self.time)}, hand_pose_type={repr(self.hand_pose_type)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.HandMeshUpdateInfoMSFT(time={self.time}, hand_pose_type={self.hand_pose_type}, next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.HAND_MESH_MSFT,
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
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.HandMeshMSFT(is_active={repr(self.is_active)}, index_buffer_changed={repr(self.index_buffer_changed)}, vertex_buffer_changed={repr(self.vertex_buffer_changed)}, index_buffer={repr(self.index_buffer)}, vertex_buffer={repr(self.vertex_buffer)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.HandMeshMSFT(is_active={self.is_active}, index_buffer_changed={self.index_buffer_changed}, vertex_buffer_changed={self.vertex_buffer_changed}, index_buffer={self.index_buffer}, vertex_buffer={self.vertex_buffer}, next={self.next}, type={self.type})"

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
        hand_pose_type: HandPoseTypeMSFT = HandPoseTypeMSFT(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.HAND_POSE_TYPE_INFO_MSFT,
    ) -> None:
        super().__init__(
            hand_pose_type=HandPoseTypeMSFT(hand_pose_type).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.HandPoseTypeInfoMSFT(hand_pose_type={repr(self.hand_pose_type)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.HandPoseTypeInfoMSFT(hand_pose_type={self.hand_pose_type}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("hand_pose_type", HandPoseTypeMSFT.ctype()),
    ]


PFN_xrCreateHandMeshSpaceMSFT = CFUNCTYPE(Result.ctype(), HandTrackerEXT, POINTER(HandMeshSpaceCreateInfoMSFT), POINTER(Space))

PFN_xrUpdateHandMeshMSFT = CFUNCTYPE(Result.ctype(), HandTrackerEXT, POINTER(HandMeshUpdateInfoMSFT), POINTER(HandMeshMSFT))


class SecondaryViewConfigurationSessionBeginInfoMSFT(Structure):
    def __init__(
        self,
        view_configuration_count: Optional[int] = None,
        enabled_view_configuration_types: ArrayFieldParamType[c_int] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SECONDARY_VIEW_CONFIGURATION_SESSION_BEGIN_INFO_MSFT,
    ) -> None:
        view_configuration_count, enabled_view_configuration_types = array_field_helper(
            c_int, view_configuration_count, enabled_view_configuration_types)
        super().__init__(
            view_configuration_count=view_configuration_count,
            _enabled_view_configuration_types=enabled_view_configuration_types,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SecondaryViewConfigurationSessionBeginInfoMSFT(view_configuration_count={repr(self.view_configuration_count)}, enabled_view_configuration_types={repr(self._enabled_view_configuration_types)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SecondaryViewConfigurationSessionBeginInfoMSFT(view_configuration_count={self.view_configuration_count}, enabled_view_configuration_types={self._enabled_view_configuration_types}, next={self.next}, type={self.type})"

    @property
    def enabled_view_configuration_types(self):
        if self.view_configuration_count == 0:
            return (c_int * 0)()
        else:
            return (c_int * self.view_configuration_count).from_address(
                ctypes.addressof(self._enabled_view_configuration_types.contents))

    @enabled_view_configuration_types.setter
    def enabled_view_configuration_types(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.view_configuration_count, self._enabled_view_configuration_types = array_field_helper(
            c_int, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_configuration_count", c_uint32),
        ("_enabled_view_configuration_types", POINTER(c_int)),
    ]


class SecondaryViewConfigurationStateMSFT(Structure):
    def __init__(
        self,
        view_configuration_type: ViewConfigurationType = ViewConfigurationType(),  # noqa
        active: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SECONDARY_VIEW_CONFIGURATION_STATE_MSFT,
    ) -> None:
        super().__init__(
            view_configuration_type=ViewConfigurationType(view_configuration_type).value,
            active=active,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SecondaryViewConfigurationStateMSFT(view_configuration_type={repr(self.view_configuration_type)}, active={repr(self.active)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SecondaryViewConfigurationStateMSFT(view_configuration_type={self.view_configuration_type}, active={self.active}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_configuration_type", ViewConfigurationType.ctype()),
        ("active", Bool32),
    ]


class SecondaryViewConfigurationFrameStateMSFT(Structure):
    def __init__(
        self,
        view_configuration_count: Optional[int] = None,
        view_configuration_states: ArrayFieldParamType[SecondaryViewConfigurationStateMSFT] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SECONDARY_VIEW_CONFIGURATION_FRAME_STATE_MSFT,
    ) -> None:
        view_configuration_count, view_configuration_states = array_field_helper(
            SecondaryViewConfigurationStateMSFT, view_configuration_count, view_configuration_states)
        super().__init__(
            view_configuration_count=view_configuration_count,
            _view_configuration_states=view_configuration_states,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SecondaryViewConfigurationFrameStateMSFT(view_configuration_count={repr(self.view_configuration_count)}, view_configuration_states={repr(self._view_configuration_states)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SecondaryViewConfigurationFrameStateMSFT(view_configuration_count={self.view_configuration_count}, view_configuration_states={self._view_configuration_states}, next={self.next}, type={self.type})"

    @property
    def view_configuration_states(self):
        if self.view_configuration_count == 0:
            return (SecondaryViewConfigurationStateMSFT * 0)()
        else:
            return (SecondaryViewConfigurationStateMSFT * self.view_configuration_count).from_address(
                ctypes.addressof(self._view_configuration_states.contents))

    @view_configuration_states.setter
    def view_configuration_states(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.view_configuration_count, self._view_configuration_states = array_field_helper(
            SecondaryViewConfigurationStateMSFT, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_configuration_count", c_uint32),
        ("_view_configuration_states", POINTER(SecondaryViewConfigurationStateMSFT)),
    ]


class SecondaryViewConfigurationLayerInfoMSFT(Structure):
    def __init__(
        self,
        view_configuration_type: ViewConfigurationType = ViewConfigurationType(),  # noqa
        environment_blend_mode: EnvironmentBlendMode = EnvironmentBlendMode(),  # noqa
        layer_count: Optional[int] = None,
        layers: BaseArrayFieldParamType = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SECONDARY_VIEW_CONFIGURATION_LAYER_INFO_MSFT,
    ) -> None:
        layer_count, layers = base_array_field_helper(
            POINTER(CompositionLayerBaseHeader), layer_count, layers)
        super().__init__(
            view_configuration_type=ViewConfigurationType(view_configuration_type).value,
            environment_blend_mode=EnvironmentBlendMode(environment_blend_mode).value,
            layer_count=layer_count,
            _layers=layers,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SecondaryViewConfigurationLayerInfoMSFT(view_configuration_type={repr(self.view_configuration_type)}, environment_blend_mode={repr(self.environment_blend_mode)}, layer_count={repr(self.layer_count)}, layers={repr(self._layers)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SecondaryViewConfigurationLayerInfoMSFT(view_configuration_type={self.view_configuration_type}, environment_blend_mode={self.environment_blend_mode}, layer_count={self.layer_count}, layers={self._layers}, next={self.next}, type={self.type})"

    @property
    def layers(self):
        if self.layer_count == 0:
            return (POINTER(CompositionLayerBaseHeader) * 0)()
        else:
            return (POINTER(CompositionLayerBaseHeader) * self.layer_count).from_address(
                ctypes.addressof(self._layers.contents))

    @layers.setter
    def layers(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.layer_count, self._layers = base_array_field_helper(
            POINTER(CompositionLayerBaseHeader), None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_configuration_type", ViewConfigurationType.ctype()),
        ("environment_blend_mode", EnvironmentBlendMode.ctype()),
        ("layer_count", c_uint32),
        ("_layers", POINTER(POINTER(CompositionLayerBaseHeader))),
    ]


class SecondaryViewConfigurationFrameEndInfoMSFT(Structure):
    def __init__(
        self,
        view_configuration_count: int = 0,
        view_configuration_layers_info: POINTER(SecondaryViewConfigurationLayerInfoMSFT) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SECONDARY_VIEW_CONFIGURATION_FRAME_END_INFO_MSFT,
    ) -> None:
        super().__init__(
            view_configuration_count=view_configuration_count,
            view_configuration_layers_info=view_configuration_layers_info,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SecondaryViewConfigurationFrameEndInfoMSFT(view_configuration_count={repr(self.view_configuration_count)}, view_configuration_layers_info={repr(self.view_configuration_layers_info)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SecondaryViewConfigurationFrameEndInfoMSFT(view_configuration_count={self.view_configuration_count}, view_configuration_layers_info={self.view_configuration_layers_info}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_configuration_count", c_uint32),
        ("view_configuration_layers_info", POINTER(SecondaryViewConfigurationLayerInfoMSFT)),
    ]


class SecondaryViewConfigurationSwapchainCreateInfoMSFT(Structure):
    def __init__(
        self,
        view_configuration_type: ViewConfigurationType = ViewConfigurationType(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.SECONDARY_VIEW_CONFIGURATION_SWAPCHAIN_CREATE_INFO_MSFT,
    ) -> None:
        super().__init__(
            view_configuration_type=ViewConfigurationType(view_configuration_type).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SecondaryViewConfigurationSwapchainCreateInfoMSFT(view_configuration_type={repr(self.view_configuration_type)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SecondaryViewConfigurationSwapchainCreateInfoMSFT(view_configuration_type={self.view_configuration_type}, next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.CONTROLLER_MODEL_KEY_STATE_MSFT,
    ) -> None:
        super().__init__(
            model_key=model_key,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ControllerModelKeyStateMSFT(model_key={repr(self.model_key)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ControllerModelKeyStateMSFT(model_key={self.model_key}, next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.CONTROLLER_MODEL_NODE_PROPERTIES_MSFT,
    ) -> None:
        super().__init__(
            parent_node_name=parent_node_name.encode(),
            node_name=node_name.encode(),
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ControllerModelNodePropertiesMSFT(parent_node_name={repr(self.parent_node_name)}, node_name={repr(self.node_name)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ControllerModelNodePropertiesMSFT(parent_node_name={self.parent_node_name}, node_name={self.node_name}, next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.CONTROLLER_MODEL_PROPERTIES_MSFT,
    ) -> None:
        super().__init__(
            node_capacity_input=node_capacity_input,
            node_count_output=node_count_output,
            node_properties=node_properties,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ControllerModelPropertiesMSFT(node_capacity_input={repr(self.node_capacity_input)}, node_count_output={repr(self.node_count_output)}, node_properties={repr(self.node_properties)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ControllerModelPropertiesMSFT(node_capacity_input={self.node_capacity_input}, node_count_output={self.node_count_output}, node_properties={self.node_properties}, next={self.next}, type={self.type})"

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
        node_pose: Posef = Posef(),
        next: c_void_p = None,
        type: StructureType = StructureType.CONTROLLER_MODEL_NODE_STATE_MSFT,
    ) -> None:
        super().__init__(
            node_pose=node_pose,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ControllerModelNodeStateMSFT(node_pose={repr(self.node_pose)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ControllerModelNodeStateMSFT(node_pose={self.node_pose}, next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.CONTROLLER_MODEL_STATE_MSFT,
    ) -> None:
        super().__init__(
            node_capacity_input=node_capacity_input,
            node_count_output=node_count_output,
            node_states=node_states,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ControllerModelStateMSFT(node_capacity_input={repr(self.node_capacity_input)}, node_count_output={repr(self.node_count_output)}, node_states={repr(self.node_states)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ControllerModelStateMSFT(node_capacity_input={self.node_capacity_input}, node_count_output={self.node_count_output}, node_states={self.node_states}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("node_capacity_input", c_uint32),
        ("node_count_output", c_uint32),
        ("node_states", POINTER(ControllerModelNodeStateMSFT)),
    ]


PFN_xrGetControllerModelKeyMSFT = CFUNCTYPE(Result.ctype(), Session, Path, POINTER(ControllerModelKeyStateMSFT))

PFN_xrLoadControllerModelMSFT = CFUNCTYPE(Result.ctype(), Session, ControllerModelKeyMSFT, c_uint32, POINTER(c_uint32), POINTER(c_uint8))

PFN_xrGetControllerModelPropertiesMSFT = CFUNCTYPE(Result.ctype(), Session, ControllerModelKeyMSFT, POINTER(ControllerModelPropertiesMSFT))

PFN_xrGetControllerModelStateMSFT = CFUNCTYPE(Result.ctype(), Session, ControllerModelKeyMSFT, POINTER(ControllerModelStateMSFT))


class ViewConfigurationViewFovEPIC(Structure):
    def __init__(
        self,
        recommended_fov: Fovf = None,
        max_mutable_fov: Fovf = None,
        next: c_void_p = None,
        type: StructureType = StructureType.VIEW_CONFIGURATION_VIEW_FOV_EPIC,
    ) -> None:
        if recommended_fov is None:
            recommended_fov = Fovf()
        if max_mutable_fov is None:
            max_mutable_fov = Fovf()
        super().__init__(
            recommended_fov=recommended_fov,
            max_mutable_fov=max_mutable_fov,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ViewConfigurationViewFovEPIC(recommended_fov={repr(self.recommended_fov)}, max_mutable_fov={repr(self.max_mutable_fov)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ViewConfigurationViewFovEPIC(recommended_fov={self.recommended_fov}, max_mutable_fov={self.max_mutable_fov}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("recommended_fov", Fovf),
        ("max_mutable_fov", Fovf),
    ]


class CompositionLayerReprojectionInfoMSFT(Structure):
    def __init__(
        self,
        reprojection_mode: ReprojectionModeMSFT = ReprojectionModeMSFT(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.COMPOSITION_LAYER_REPROJECTION_INFO_MSFT,
    ) -> None:
        super().__init__(
            reprojection_mode=ReprojectionModeMSFT(reprojection_mode).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerReprojectionInfoMSFT(reprojection_mode={repr(self.reprojection_mode)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerReprojectionInfoMSFT(reprojection_mode={self.reprojection_mode}, next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.COMPOSITION_LAYER_REPROJECTION_PLANE_OVERRIDE_MSFT,
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
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerReprojectionPlaneOverrideMSFT(position={repr(self.position)}, normal={repr(self.normal)}, velocity={repr(self.velocity)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerReprojectionPlaneOverrideMSFT(position={self.position}, normal={self.normal}, velocity={self.velocity}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("position", Vector3f),
        ("normal", Vector3f),
        ("velocity", Vector3f),
    ]


PFN_xrEnumerateReprojectionModesMSFT = CFUNCTYPE(Result.ctype(), Instance, SystemId, ViewConfigurationType.ctype(), c_uint32, POINTER(c_uint32), POINTER(ReprojectionModeMSFT.ctype()))


class SwapchainStateBaseHeaderFB(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainStateBaseHeaderFB(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainStateBaseHeaderFB(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


PFN_xrUpdateSwapchainFB = CFUNCTYPE(Result.ctype(), Swapchain, POINTER(SwapchainStateBaseHeaderFB))

PFN_xrGetSwapchainStateFB = CFUNCTYPE(Result.ctype(), Swapchain, POINTER(SwapchainStateBaseHeaderFB))

CompositionLayerSecureContentFlagsFBCInt = Flags64


class CompositionLayerSecureContentFB(Structure):
    def __init__(
        self,
        flags: CompositionLayerSecureContentFlagsFB = CompositionLayerSecureContentFlagsFB(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.COMPOSITION_LAYER_SECURE_CONTENT_FB,
    ) -> None:
        super().__init__(
            flags=CompositionLayerSecureContentFlagsFB(flags).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerSecureContentFB(flags={repr(self.flags)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerSecureContentFB(flags={self.flags}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", CompositionLayerSecureContentFlagsFBCInt),
    ]


class BodyTrackerFB_T(Structure):
    pass


class BodyTrackerFB(POINTER(BodyTrackerFB_T), HandleMixin):
    _type_ = BodyTrackerFB_T  # ctypes idiosyncrasy


class BodyJointLocationFB(Structure):
    def __init__(
        self,
        location_flags: SpaceLocationFlags = SpaceLocationFlags(),  # noqa
        pose: Posef = Posef(),
    ) -> None:
        super().__init__(
            location_flags=SpaceLocationFlags(location_flags).value,
            pose=pose,
        )

    def __repr__(self) -> str:
        return f"xr.BodyJointLocationFB(location_flags={repr(self.location_flags)}, pose={repr(self.pose)})"

    def __str__(self) -> str:
        return f"xr.BodyJointLocationFB(location_flags={self.location_flags}, pose={self.pose})"

    _fields_ = [
        ("location_flags", SpaceLocationFlagsCInt),
        ("pose", Posef),
    ]


class SystemBodyTrackingPropertiesFB(Structure):
    def __init__(
        self,
        supports_body_tracking: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_BODY_TRACKING_PROPERTIES_FB,
    ) -> None:
        super().__init__(
            supports_body_tracking=supports_body_tracking,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemBodyTrackingPropertiesFB(supports_body_tracking={repr(self.supports_body_tracking)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemBodyTrackingPropertiesFB(supports_body_tracking={self.supports_body_tracking}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_body_tracking", Bool32),
    ]


class BodyTrackerCreateInfoFB(Structure):
    def __init__(
        self,
        body_joint_set: BodyJointSetFB = BodyJointSetFB(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.BODY_TRACKER_CREATE_INFO_FB,
    ) -> None:
        super().__init__(
            body_joint_set=BodyJointSetFB(body_joint_set).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.BodyTrackerCreateInfoFB(body_joint_set={repr(self.body_joint_set)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.BodyTrackerCreateInfoFB(body_joint_set={self.body_joint_set}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("body_joint_set", BodyJointSetFB.ctype()),
    ]


class BodySkeletonJointFB(Structure):
    def __init__(
        self,
        joint: int = 0,
        parent_joint: int = 0,
        pose: Posef = Posef(),
    ) -> None:
        super().__init__(
            joint=joint,
            parent_joint=parent_joint,
            pose=pose,
        )

    def __repr__(self) -> str:
        return f"xr.BodySkeletonJointFB(joint={repr(self.joint)}, parent_joint={repr(self.parent_joint)}, pose={repr(self.pose)})"

    def __str__(self) -> str:
        return f"xr.BodySkeletonJointFB(joint={self.joint}, parent_joint={self.parent_joint}, pose={self.pose})"

    _fields_ = [
        ("joint", c_int32),
        ("parent_joint", c_int32),
        ("pose", Posef),
    ]


class BodySkeletonFB(Structure):
    def __init__(
        self,
        joint_count: Optional[int] = None,
        joints: ArrayFieldParamType[BodySkeletonJointFB] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.BODY_SKELETON_FB,
    ) -> None:
        joint_count, joints = array_field_helper(
            BodySkeletonJointFB, joint_count, joints)
        super().__init__(
            joint_count=joint_count,
            _joints=joints,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.BodySkeletonFB(joint_count={repr(self.joint_count)}, joints={repr(self._joints)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.BodySkeletonFB(joint_count={self.joint_count}, joints={self._joints}, next={self.next}, type={self.type})"

    @property
    def joints(self):
        if self.joint_count == 0:
            return (BodySkeletonJointFB * 0)()
        else:
            return (BodySkeletonJointFB * self.joint_count).from_address(
                ctypes.addressof(self._joints.contents))

    @joints.setter
    def joints(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.joint_count, self._joints = array_field_helper(
            BodySkeletonJointFB, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("joint_count", c_uint32),
        ("_joints", POINTER(BodySkeletonJointFB)),
    ]


class BodyJointsLocateInfoFB(Structure):
    def __init__(
        self,
        base_space: Space = None,
        time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.BODY_JOINTS_LOCATE_INFO_FB,
    ) -> None:
        super().__init__(
            base_space=base_space,
            time=time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.BodyJointsLocateInfoFB(base_space={repr(self.base_space)}, time={repr(self.time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.BodyJointsLocateInfoFB(base_space={self.base_space}, time={self.time}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("base_space", Space),
        ("time", Time),
    ]


class BodyJointLocationsFB(Structure):
    def __init__(
        self,
        is_active: Bool32 = 0,
        confidence: float = 0,
        joint_count: Optional[int] = None,
        joint_locations: ArrayFieldParamType[BodyJointLocationFB] = None,
        skeleton_changed_count: int = 0,
        time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.BODY_JOINT_LOCATIONS_FB,
    ) -> None:
        joint_count, joint_locations = array_field_helper(
            BodyJointLocationFB, joint_count, joint_locations)
        super().__init__(
            is_active=is_active,
            confidence=confidence,
            joint_count=joint_count,
            _joint_locations=joint_locations,
            skeleton_changed_count=skeleton_changed_count,
            time=time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.BodyJointLocationsFB(is_active={repr(self.is_active)}, confidence={repr(self.confidence)}, joint_count={repr(self.joint_count)}, joint_locations={repr(self._joint_locations)}, skeleton_changed_count={repr(self.skeleton_changed_count)}, time={repr(self.time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.BodyJointLocationsFB(is_active={self.is_active}, confidence={self.confidence:.3f}, joint_count={self.joint_count}, joint_locations={self._joint_locations}, skeleton_changed_count={self.skeleton_changed_count}, time={self.time}, next={self.next}, type={self.type})"

    @property
    def joint_locations(self):
        if self.joint_count == 0:
            return (BodyJointLocationFB * 0)()
        else:
            return (BodyJointLocationFB * self.joint_count).from_address(
                ctypes.addressof(self._joint_locations.contents))

    @joint_locations.setter
    def joint_locations(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.joint_count, self._joint_locations = array_field_helper(
            BodyJointLocationFB, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("is_active", Bool32),
        ("confidence", c_float),
        ("joint_count", c_uint32),
        ("_joint_locations", POINTER(BodyJointLocationFB)),
        ("skeleton_changed_count", c_uint32),
        ("time", Time),
    ]


PFN_xrCreateBodyTrackerFB = CFUNCTYPE(Result.ctype(), Session, POINTER(BodyTrackerCreateInfoFB), POINTER(BodyTrackerFB))

PFN_xrDestroyBodyTrackerFB = CFUNCTYPE(Result.ctype(), BodyTrackerFB)

PFN_xrLocateBodyJointsFB = CFUNCTYPE(Result.ctype(), BodyTrackerFB, POINTER(BodyJointsLocateInfoFB), POINTER(BodyJointLocationsFB))

PFN_xrGetBodySkeletonFB = CFUNCTYPE(Result.ctype(), BodyTrackerFB, POINTER(BodySkeletonFB))


class InteractionProfileDpadBindingEXT(Structure):
    def __init__(
        self,
        binding: Path = 0,
        action_set: ActionSet = None,
        force_threshold: float = 0,
        force_threshold_released: float = 0,
        center_region: float = 0,
        wedge_angle: float = 0,
        is_sticky: Bool32 = 0,
        on_haptic: POINTER(HapticBaseHeader) = None,
        off_haptic: POINTER(HapticBaseHeader) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.INTERACTION_PROFILE_DPAD_BINDING_EXT,
    ) -> None:
        super().__init__(
            binding=binding,
            action_set=action_set,
            force_threshold=force_threshold,
            force_threshold_released=force_threshold_released,
            center_region=center_region,
            wedge_angle=wedge_angle,
            is_sticky=is_sticky,
            on_haptic=on_haptic,
            off_haptic=off_haptic,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.InteractionProfileDpadBindingEXT(binding={repr(self.binding)}, action_set={repr(self.action_set)}, force_threshold={repr(self.force_threshold)}, force_threshold_released={repr(self.force_threshold_released)}, center_region={repr(self.center_region)}, wedge_angle={repr(self.wedge_angle)}, is_sticky={repr(self.is_sticky)}, on_haptic={repr(self.on_haptic)}, off_haptic={repr(self.off_haptic)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.InteractionProfileDpadBindingEXT(binding={self.binding}, action_set={self.action_set}, force_threshold={self.force_threshold:.3f}, force_threshold_released={self.force_threshold_released:.3f}, center_region={self.center_region:.3f}, wedge_angle={self.wedge_angle:.3f}, is_sticky={self.is_sticky}, on_haptic={self.on_haptic}, off_haptic={self.off_haptic}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("binding", Path),
        ("action_set", ActionSet),
        ("force_threshold", c_float),
        ("force_threshold_released", c_float),
        ("center_region", c_float),
        ("wedge_angle", c_float),
        ("is_sticky", Bool32),
        ("on_haptic", POINTER(HapticBaseHeader)),
        ("off_haptic", POINTER(HapticBaseHeader)),
    ]


class InteractionProfileAnalogThresholdVALVE(Structure):
    def __init__(
        self,
        action: Action = None,
        binding: Path = 0,
        on_threshold: float = 0,
        off_threshold: float = 0,
        on_haptic: POINTER(HapticBaseHeader) = None,
        off_haptic: POINTER(HapticBaseHeader) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.INTERACTION_PROFILE_ANALOG_THRESHOLD_VALVE,
    ) -> None:
        super().__init__(
            action=action,
            binding=binding,
            on_threshold=on_threshold,
            off_threshold=off_threshold,
            on_haptic=on_haptic,
            off_haptic=off_haptic,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.InteractionProfileAnalogThresholdVALVE(action={repr(self.action)}, binding={repr(self.binding)}, on_threshold={repr(self.on_threshold)}, off_threshold={repr(self.off_threshold)}, on_haptic={repr(self.on_haptic)}, off_haptic={repr(self.off_haptic)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.InteractionProfileAnalogThresholdVALVE(action={self.action}, binding={self.binding}, on_threshold={self.on_threshold:.3f}, off_threshold={self.off_threshold:.3f}, on_haptic={self.on_haptic}, off_haptic={self.off_haptic}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("action", Action),
        ("binding", Path),
        ("on_threshold", c_float),
        ("off_threshold", c_float),
        ("on_haptic", POINTER(HapticBaseHeader)),
        ("off_haptic", POINTER(HapticBaseHeader)),
    ]


class HandJointsMotionRangeInfoEXT(Structure):
    def __init__(
        self,
        hand_joints_motion_range: HandJointsMotionRangeEXT = HandJointsMotionRangeEXT(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.HAND_JOINTS_MOTION_RANGE_INFO_EXT,
    ) -> None:
        super().__init__(
            hand_joints_motion_range=HandJointsMotionRangeEXT(hand_joints_motion_range).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.HandJointsMotionRangeInfoEXT(hand_joints_motion_range={repr(self.hand_joints_motion_range)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.HandJointsMotionRangeInfoEXT(hand_joints_motion_range={self.hand_joints_motion_range}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("hand_joints_motion_range", HandJointsMotionRangeEXT.ctype()),
    ]


class SceneObserverMSFT_T(Structure):
    pass


class SceneObserverMSFT(POINTER(SceneObserverMSFT_T), HandleMixin):
    _type_ = SceneObserverMSFT_T  # ctypes idiosyncrasy


class SceneMSFT_T(Structure):
    pass


class SceneMSFT(POINTER(SceneMSFT_T), HandleMixin):
    _type_ = SceneMSFT_T  # ctypes idiosyncrasy


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
        next: c_void_p = None,
        type: StructureType = StructureType.SCENE_OBSERVER_CREATE_INFO_MSFT,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SceneObserverCreateInfoMSFT(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SceneObserverCreateInfoMSFT(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SceneCreateInfoMSFT(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.SCENE_CREATE_INFO_MSFT,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SceneCreateInfoMSFT(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SceneCreateInfoMSFT(next={self.next}, type={self.type})"

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
        pose: Posef = Posef(),
        extents: Vector3f = None,
    ) -> None:
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
        pose: Posef = Posef(),
        fov: Fovf = None,
        far_distance: float = 0,
    ) -> None:
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
        space: Space = None,
        time: Time = 0,
        sphere_count: Optional[int] = None,
        spheres: ArrayFieldParamType[SceneSphereBoundMSFT] = None,
        box_count: Optional[int] = None,
        boxes: ArrayFieldParamType[SceneOrientedBoxBoundMSFT] = None,
        frustum_count: Optional[int] = None,
        frustums: ArrayFieldParamType[SceneFrustumBoundMSFT] = None,
    ) -> None:
        sphere_count, spheres = array_field_helper(
            SceneSphereBoundMSFT, sphere_count, spheres)
        box_count, boxes = array_field_helper(
            SceneOrientedBoxBoundMSFT, box_count, boxes)
        frustum_count, frustums = array_field_helper(
            SceneFrustumBoundMSFT, frustum_count, frustums)
        super().__init__(
            space=space,
            time=time,
            sphere_count=sphere_count,
            _spheres=spheres,
            box_count=box_count,
            _boxes=boxes,
            frustum_count=frustum_count,
            _frustums=frustums,
        )

    def __repr__(self) -> str:
        return f"xr.SceneBoundsMSFT(space={repr(self.space)}, time={repr(self.time)}, sphere_count={repr(self.sphere_count)}, spheres={repr(self._spheres)}, box_count={repr(self.box_count)}, boxes={repr(self._boxes)}, frustum_count={repr(self.frustum_count)}, frustums={repr(self._frustums)})"

    def __str__(self) -> str:
        return f"xr.SceneBoundsMSFT(space={self.space}, time={self.time}, sphere_count={self.sphere_count}, spheres={self._spheres}, box_count={self.box_count}, boxes={self._boxes}, frustum_count={self.frustum_count}, frustums={self._frustums})"

    @property
    def spheres(self):
        if self.sphere_count == 0:
            return (SceneSphereBoundMSFT * 0)()
        else:
            return (SceneSphereBoundMSFT * self.sphere_count).from_address(
                ctypes.addressof(self._spheres.contents))

    @spheres.setter
    def spheres(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.sphere_count, self._spheres = array_field_helper(
            SceneSphereBoundMSFT, None, value)

    @property
    def boxes(self):
        if self.box_count == 0:
            return (SceneOrientedBoxBoundMSFT * 0)()
        else:
            return (SceneOrientedBoxBoundMSFT * self.box_count).from_address(
                ctypes.addressof(self._boxes.contents))

    @boxes.setter
    def boxes(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.box_count, self._boxes = array_field_helper(
            SceneOrientedBoxBoundMSFT, None, value)

    @property
    def frustums(self):
        if self.frustum_count == 0:
            return (SceneFrustumBoundMSFT * 0)()
        else:
            return (SceneFrustumBoundMSFT * self.frustum_count).from_address(
                ctypes.addressof(self._frustums.contents))

    @frustums.setter
    def frustums(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.frustum_count, self._frustums = array_field_helper(
            SceneFrustumBoundMSFT, None, value)

    _fields_ = [
        ("space", Space),
        ("time", Time),
        ("sphere_count", c_uint32),
        ("_spheres", POINTER(SceneSphereBoundMSFT)),
        ("box_count", c_uint32),
        ("_boxes", POINTER(SceneOrientedBoxBoundMSFT)),
        ("frustum_count", c_uint32),
        ("_frustums", POINTER(SceneFrustumBoundMSFT)),
    ]


class NewSceneComputeInfoMSFT(Structure):
    def __init__(
        self,
        requested_feature_count: Optional[int] = None,
        requested_features: ArrayFieldParamType[c_int] = None,
        consistency: SceneComputeConsistencyMSFT = SceneComputeConsistencyMSFT(),  # noqa
        bounds: SceneBoundsMSFT = None,
        next: c_void_p = None,
        type: StructureType = StructureType.NEW_SCENE_COMPUTE_INFO_MSFT,
    ) -> None:
        requested_feature_count, requested_features = array_field_helper(
            c_int, requested_feature_count, requested_features)
        if bounds is None:
            bounds = SceneBoundsMSFT()
        super().__init__(
            requested_feature_count=requested_feature_count,
            _requested_features=requested_features,
            consistency=SceneComputeConsistencyMSFT(consistency).value,
            bounds=bounds,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.NewSceneComputeInfoMSFT(requested_feature_count={repr(self.requested_feature_count)}, requested_features={repr(self._requested_features)}, consistency={repr(self.consistency)}, bounds={repr(self.bounds)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.NewSceneComputeInfoMSFT(requested_feature_count={self.requested_feature_count}, requested_features={self._requested_features}, consistency={self.consistency}, bounds={self.bounds}, next={self.next}, type={self.type})"

    @property
    def requested_features(self):
        if self.requested_feature_count == 0:
            return (c_int * 0)()
        else:
            return (c_int * self.requested_feature_count).from_address(
                ctypes.addressof(self._requested_features.contents))

    @requested_features.setter
    def requested_features(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.requested_feature_count, self._requested_features = array_field_helper(
            c_int, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("requested_feature_count", c_uint32),
        ("_requested_features", POINTER(c_int)),
        ("consistency", SceneComputeConsistencyMSFT.ctype()),
        ("bounds", SceneBoundsMSFT),
    ]


class VisualMeshComputeLodInfoMSFT(Structure):
    def __init__(
        self,
        lod: MeshComputeLodMSFT = MeshComputeLodMSFT(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.VISUAL_MESH_COMPUTE_LOD_INFO_MSFT,
    ) -> None:
        super().__init__(
            lod=MeshComputeLodMSFT(lod).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.VisualMeshComputeLodInfoMSFT(lod={repr(self.lod)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.VisualMeshComputeLodInfoMSFT(lod={self.lod}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("lod", MeshComputeLodMSFT.ctype()),
    ]


class SceneComponentMSFT(Structure):
    def __init__(
        self,
        component_type: SceneComponentTypeMSFT = SceneComponentTypeMSFT(),  # noqa
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
        next: c_void_p = None,
        type: StructureType = StructureType.SCENE_COMPONENTS_MSFT,
    ) -> None:
        super().__init__(
            component_capacity_input=component_capacity_input,
            component_count_output=component_count_output,
            components=components,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SceneComponentsMSFT(component_capacity_input={repr(self.component_capacity_input)}, component_count_output={repr(self.component_count_output)}, components={repr(self.components)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SceneComponentsMSFT(component_capacity_input={self.component_capacity_input}, component_count_output={self.component_count_output}, components={self.components}, next={self.next}, type={self.type})"

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
        component_type: SceneComponentTypeMSFT = SceneComponentTypeMSFT(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.SCENE_COMPONENTS_GET_INFO_MSFT,
    ) -> None:
        super().__init__(
            component_type=SceneComponentTypeMSFT(component_type).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SceneComponentsGetInfoMSFT(component_type={repr(self.component_type)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SceneComponentsGetInfoMSFT(component_type={self.component_type}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("component_type", SceneComponentTypeMSFT.ctype()),
    ]


class SceneComponentLocationMSFT(Structure):
    def __init__(
        self,
        flags: SpaceLocationFlags = SpaceLocationFlags(),  # noqa
        pose: Posef = Posef(),
    ) -> None:
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
        location_count: Optional[int] = None,
        locations: ArrayFieldParamType[SceneComponentLocationMSFT] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SCENE_COMPONENT_LOCATIONS_MSFT,
    ) -> None:
        location_count, locations = array_field_helper(
            SceneComponentLocationMSFT, location_count, locations)
        super().__init__(
            location_count=location_count,
            _locations=locations,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SceneComponentLocationsMSFT(location_count={repr(self.location_count)}, locations={repr(self._locations)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SceneComponentLocationsMSFT(location_count={self.location_count}, locations={self._locations}, next={self.next}, type={self.type})"

    @property
    def locations(self):
        if self.location_count == 0:
            return (SceneComponentLocationMSFT * 0)()
        else:
            return (SceneComponentLocationMSFT * self.location_count).from_address(
                ctypes.addressof(self._locations.contents))

    @locations.setter
    def locations(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.location_count, self._locations = array_field_helper(
            SceneComponentLocationMSFT, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("location_count", c_uint32),
        ("_locations", POINTER(SceneComponentLocationMSFT)),
    ]


class SceneComponentsLocateInfoMSFT(Structure):
    def __init__(
        self,
        base_space: Space = None,
        time: Time = 0,
        component_id_count: Optional[int] = None,
        component_ids: ArrayFieldParamType[UuidMSFT] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SCENE_COMPONENTS_LOCATE_INFO_MSFT,
    ) -> None:
        component_id_count, component_ids = array_field_helper(
            UuidMSFT, component_id_count, component_ids)
        super().__init__(
            base_space=base_space,
            time=time,
            component_id_count=component_id_count,
            _component_ids=component_ids,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SceneComponentsLocateInfoMSFT(base_space={repr(self.base_space)}, time={repr(self.time)}, component_id_count={repr(self.component_id_count)}, component_ids={repr(self._component_ids)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SceneComponentsLocateInfoMSFT(base_space={self.base_space}, time={self.time}, component_id_count={self.component_id_count}, component_ids={self._component_ids}, next={self.next}, type={self.type})"

    @property
    def component_ids(self):
        if self.component_id_count == 0:
            return (UuidMSFT * 0)()
        else:
            return (UuidMSFT * self.component_id_count).from_address(
                ctypes.addressof(self._component_ids.contents))

    @component_ids.setter
    def component_ids(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.component_id_count, self._component_ids = array_field_helper(
            UuidMSFT, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("base_space", Space),
        ("time", Time),
        ("component_id_count", c_uint32),
        ("_component_ids", POINTER(UuidMSFT)),
    ]


class SceneObjectMSFT(Structure):
    def __init__(
        self,
        object_type: SceneObjectTypeMSFT = SceneObjectTypeMSFT(),  # noqa
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
        scene_object_count: Optional[int] = None,
        scene_objects: ArrayFieldParamType[SceneObjectMSFT] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SCENE_OBJECTS_MSFT,
    ) -> None:
        scene_object_count, scene_objects = array_field_helper(
            SceneObjectMSFT, scene_object_count, scene_objects)
        super().__init__(
            scene_object_count=scene_object_count,
            _scene_objects=scene_objects,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SceneObjectsMSFT(scene_object_count={repr(self.scene_object_count)}, scene_objects={repr(self._scene_objects)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SceneObjectsMSFT(scene_object_count={self.scene_object_count}, scene_objects={self._scene_objects}, next={self.next}, type={self.type})"

    @property
    def scene_objects(self):
        if self.scene_object_count == 0:
            return (SceneObjectMSFT * 0)()
        else:
            return (SceneObjectMSFT * self.scene_object_count).from_address(
                ctypes.addressof(self._scene_objects.contents))

    @scene_objects.setter
    def scene_objects(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.scene_object_count, self._scene_objects = array_field_helper(
            SceneObjectMSFT, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("scene_object_count", c_uint32),
        ("_scene_objects", POINTER(SceneObjectMSFT)),
    ]


class SceneComponentParentFilterInfoMSFT(Structure):
    def __init__(
        self,
        parent_id: UuidMSFT = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SCENE_COMPONENT_PARENT_FILTER_INFO_MSFT,
    ) -> None:
        if parent_id is None:
            parent_id = UuidMSFT()
        super().__init__(
            parent_id=parent_id,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SceneComponentParentFilterInfoMSFT(parent_id={repr(self.parent_id)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SceneComponentParentFilterInfoMSFT(parent_id={self.parent_id}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("parent_id", UuidMSFT),
    ]


class SceneObjectTypesFilterInfoMSFT(Structure):
    def __init__(
        self,
        object_type_count: Optional[int] = None,
        object_types: ArrayFieldParamType[c_int] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SCENE_OBJECT_TYPES_FILTER_INFO_MSFT,
    ) -> None:
        object_type_count, object_types = array_field_helper(
            c_int, object_type_count, object_types)
        super().__init__(
            object_type_count=object_type_count,
            _object_types=object_types,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SceneObjectTypesFilterInfoMSFT(object_type_count={repr(self.object_type_count)}, object_types={repr(self._object_types)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SceneObjectTypesFilterInfoMSFT(object_type_count={self.object_type_count}, object_types={self._object_types}, next={self.next}, type={self.type})"

    @property
    def object_types(self):
        if self.object_type_count == 0:
            return (c_int * 0)()
        else:
            return (c_int * self.object_type_count).from_address(
                ctypes.addressof(self._object_types.contents))

    @object_types.setter
    def object_types(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.object_type_count, self._object_types = array_field_helper(
            c_int, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("object_type_count", c_uint32),
        ("_object_types", POINTER(c_int)),
    ]


class ScenePlaneMSFT(Structure):
    def __init__(
        self,
        alignment: ScenePlaneAlignmentTypeMSFT = ScenePlaneAlignmentTypeMSFT(),  # noqa
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
        scene_plane_count: Optional[int] = None,
        scene_planes: ArrayFieldParamType[ScenePlaneMSFT] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SCENE_PLANES_MSFT,
    ) -> None:
        scene_plane_count, scene_planes = array_field_helper(
            ScenePlaneMSFT, scene_plane_count, scene_planes)
        super().__init__(
            scene_plane_count=scene_plane_count,
            _scene_planes=scene_planes,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ScenePlanesMSFT(scene_plane_count={repr(self.scene_plane_count)}, scene_planes={repr(self._scene_planes)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ScenePlanesMSFT(scene_plane_count={self.scene_plane_count}, scene_planes={self._scene_planes}, next={self.next}, type={self.type})"

    @property
    def scene_planes(self):
        if self.scene_plane_count == 0:
            return (ScenePlaneMSFT * 0)()
        else:
            return (ScenePlaneMSFT * self.scene_plane_count).from_address(
                ctypes.addressof(self._scene_planes.contents))

    @scene_planes.setter
    def scene_planes(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.scene_plane_count, self._scene_planes = array_field_helper(
            ScenePlaneMSFT, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("scene_plane_count", c_uint32),
        ("_scene_planes", POINTER(ScenePlaneMSFT)),
    ]


class ScenePlaneAlignmentFilterInfoMSFT(Structure):
    def __init__(
        self,
        alignment_count: Optional[int] = None,
        alignments: ArrayFieldParamType[c_int] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SCENE_PLANE_ALIGNMENT_FILTER_INFO_MSFT,
    ) -> None:
        alignment_count, alignments = array_field_helper(
            c_int, alignment_count, alignments)
        super().__init__(
            alignment_count=alignment_count,
            _alignments=alignments,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ScenePlaneAlignmentFilterInfoMSFT(alignment_count={repr(self.alignment_count)}, alignments={repr(self._alignments)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ScenePlaneAlignmentFilterInfoMSFT(alignment_count={self.alignment_count}, alignments={self._alignments}, next={self.next}, type={self.type})"

    @property
    def alignments(self):
        if self.alignment_count == 0:
            return (c_int * 0)()
        else:
            return (c_int * self.alignment_count).from_address(
                ctypes.addressof(self._alignments.contents))

    @alignments.setter
    def alignments(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.alignment_count, self._alignments = array_field_helper(
            c_int, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("alignment_count", c_uint32),
        ("_alignments", POINTER(c_int)),
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
        scene_mesh_count: Optional[int] = None,
        scene_meshes: ArrayFieldParamType[SceneMeshMSFT] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SCENE_MESHES_MSFT,
    ) -> None:
        scene_mesh_count, scene_meshes = array_field_helper(
            SceneMeshMSFT, scene_mesh_count, scene_meshes)
        super().__init__(
            scene_mesh_count=scene_mesh_count,
            _scene_meshes=scene_meshes,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SceneMeshesMSFT(scene_mesh_count={repr(self.scene_mesh_count)}, scene_meshes={repr(self._scene_meshes)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SceneMeshesMSFT(scene_mesh_count={self.scene_mesh_count}, scene_meshes={self._scene_meshes}, next={self.next}, type={self.type})"

    @property
    def scene_meshes(self):
        if self.scene_mesh_count == 0:
            return (SceneMeshMSFT * 0)()
        else:
            return (SceneMeshMSFT * self.scene_mesh_count).from_address(
                ctypes.addressof(self._scene_meshes.contents))

    @scene_meshes.setter
    def scene_meshes(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.scene_mesh_count, self._scene_meshes = array_field_helper(
            SceneMeshMSFT, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("scene_mesh_count", c_uint32),
        ("_scene_meshes", POINTER(SceneMeshMSFT)),
    ]


class SceneMeshBuffersGetInfoMSFT(Structure):
    def __init__(
        self,
        mesh_buffer_id: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SCENE_MESH_BUFFERS_GET_INFO_MSFT,
    ) -> None:
        super().__init__(
            mesh_buffer_id=mesh_buffer_id,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SceneMeshBuffersGetInfoMSFT(mesh_buffer_id={repr(self.mesh_buffer_id)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SceneMeshBuffersGetInfoMSFT(mesh_buffer_id={self.mesh_buffer_id}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("mesh_buffer_id", c_uint64),
    ]


class SceneMeshBuffersMSFT(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.SCENE_MESH_BUFFERS_MSFT,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SceneMeshBuffersMSFT(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SceneMeshBuffersMSFT(next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.SCENE_MESH_VERTEX_BUFFER_MSFT,
    ) -> None:
        super().__init__(
            vertex_capacity_input=vertex_capacity_input,
            vertex_count_output=vertex_count_output,
            vertices=vertices,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SceneMeshVertexBufferMSFT(vertex_capacity_input={repr(self.vertex_capacity_input)}, vertex_count_output={repr(self.vertex_count_output)}, vertices={repr(self.vertices)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SceneMeshVertexBufferMSFT(vertex_capacity_input={self.vertex_capacity_input}, vertex_count_output={self.vertex_count_output}, vertices={self.vertices}, next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.SCENE_MESH_INDICES_UINT32_MSFT,
    ) -> None:
        super().__init__(
            index_capacity_input=index_capacity_input,
            index_count_output=index_count_output,
            indices=indices,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SceneMeshIndicesUint32MSFT(index_capacity_input={repr(self.index_capacity_input)}, index_count_output={repr(self.index_count_output)}, indices={repr(self.indices)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SceneMeshIndicesUint32MSFT(index_capacity_input={self.index_capacity_input}, index_count_output={self.index_count_output}, indices={self.indices}, next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.SCENE_MESH_INDICES_UINT16_MSFT,
    ) -> None:
        super().__init__(
            index_capacity_input=index_capacity_input,
            index_count_output=index_count_output,
            indices=indices,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SceneMeshIndicesUint16MSFT(index_capacity_input={repr(self.index_capacity_input)}, index_count_output={repr(self.index_count_output)}, indices={repr(self.indices)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SceneMeshIndicesUint16MSFT(index_capacity_input={self.index_capacity_input}, index_count_output={self.index_count_output}, indices={self.indices}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("index_capacity_input", c_uint32),
        ("index_count_output", c_uint32),
        ("indices", POINTER(c_uint16)),
    ]


PFN_xrEnumerateSceneComputeFeaturesMSFT = CFUNCTYPE(Result.ctype(), Instance, SystemId, c_uint32, POINTER(c_uint32), POINTER(SceneComputeFeatureMSFT.ctype()))

PFN_xrCreateSceneObserverMSFT = CFUNCTYPE(Result.ctype(), Session, POINTER(SceneObserverCreateInfoMSFT), POINTER(SceneObserverMSFT))

PFN_xrDestroySceneObserverMSFT = CFUNCTYPE(Result.ctype(), SceneObserverMSFT)

PFN_xrCreateSceneMSFT = CFUNCTYPE(Result.ctype(), SceneObserverMSFT, POINTER(SceneCreateInfoMSFT), POINTER(SceneMSFT))

PFN_xrDestroySceneMSFT = CFUNCTYPE(Result.ctype(), SceneMSFT)

PFN_xrComputeNewSceneMSFT = CFUNCTYPE(Result.ctype(), SceneObserverMSFT, POINTER(NewSceneComputeInfoMSFT))

PFN_xrGetSceneComputeStateMSFT = CFUNCTYPE(Result.ctype(), SceneObserverMSFT, POINTER(SceneComputeStateMSFT.ctype()))

PFN_xrGetSceneComponentsMSFT = CFUNCTYPE(Result.ctype(), SceneMSFT, POINTER(SceneComponentsGetInfoMSFT), POINTER(SceneComponentsMSFT))

PFN_xrLocateSceneComponentsMSFT = CFUNCTYPE(Result.ctype(), SceneMSFT, POINTER(SceneComponentsLocateInfoMSFT), POINTER(SceneComponentLocationsMSFT))

PFN_xrGetSceneMeshBuffersMSFT = CFUNCTYPE(Result.ctype(), SceneMSFT, POINTER(SceneMeshBuffersGetInfoMSFT), POINTER(SceneMeshBuffersMSFT))


class SerializedSceneFragmentDataGetInfoMSFT(Structure):
    def __init__(
        self,
        scene_fragment_id: UuidMSFT = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SERIALIZED_SCENE_FRAGMENT_DATA_GET_INFO_MSFT,
    ) -> None:
        if scene_fragment_id is None:
            scene_fragment_id = UuidMSFT()
        super().__init__(
            scene_fragment_id=scene_fragment_id,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SerializedSceneFragmentDataGetInfoMSFT(scene_fragment_id={repr(self.scene_fragment_id)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SerializedSceneFragmentDataGetInfoMSFT(scene_fragment_id={self.scene_fragment_id}, next={self.next}, type={self.type})"

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
        fragment_count: Optional[int] = None,
        fragments: ArrayFieldParamType[DeserializeSceneFragmentMSFT] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SCENE_DESERIALIZE_INFO_MSFT,
    ) -> None:
        fragment_count, fragments = array_field_helper(
            DeserializeSceneFragmentMSFT, fragment_count, fragments)
        super().__init__(
            fragment_count=fragment_count,
            _fragments=fragments,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SceneDeserializeInfoMSFT(fragment_count={repr(self.fragment_count)}, fragments={repr(self._fragments)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SceneDeserializeInfoMSFT(fragment_count={self.fragment_count}, fragments={self._fragments}, next={self.next}, type={self.type})"

    @property
    def fragments(self):
        if self.fragment_count == 0:
            return (DeserializeSceneFragmentMSFT * 0)()
        else:
            return (DeserializeSceneFragmentMSFT * self.fragment_count).from_address(
                ctypes.addressof(self._fragments.contents))

    @fragments.setter
    def fragments(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.fragment_count, self._fragments = array_field_helper(
            DeserializeSceneFragmentMSFT, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("fragment_count", c_uint32),
        ("_fragments", POINTER(DeserializeSceneFragmentMSFT)),
    ]


PFN_xrDeserializeSceneMSFT = CFUNCTYPE(Result.ctype(), SceneObserverMSFT, POINTER(SceneDeserializeInfoMSFT))

PFN_xrGetSerializedSceneFragmentDataMSFT = CFUNCTYPE(Result.ctype(), SceneMSFT, POINTER(SerializedSceneFragmentDataGetInfoMSFT), c_uint32, POINTER(c_uint32), POINTER(c_uint8))


class EventDataDisplayRefreshRateChangedFB(Structure):
    def __init__(
        self,
        from_display_refresh_rate: float = 0,
        to_display_refresh_rate: float = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_DISPLAY_REFRESH_RATE_CHANGED_FB,
    ) -> None:
        super().__init__(
            from_display_refresh_rate=from_display_refresh_rate,
            to_display_refresh_rate=to_display_refresh_rate,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataDisplayRefreshRateChangedFB(from_display_refresh_rate={repr(self.from_display_refresh_rate)}, to_display_refresh_rate={repr(self.to_display_refresh_rate)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataDisplayRefreshRateChangedFB(from_display_refresh_rate={self.from_display_refresh_rate:.3f}, to_display_refresh_rate={self.to_display_refresh_rate:.3f}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("from_display_refresh_rate", c_float),
        ("to_display_refresh_rate", c_float),
    ]


PFN_xrEnumerateDisplayRefreshRatesFB = CFUNCTYPE(Result.ctype(), Session, c_uint32, POINTER(c_uint32), POINTER(c_float))

PFN_xrGetDisplayRefreshRateFB = CFUNCTYPE(Result.ctype(), Session, POINTER(c_float))

PFN_xrRequestDisplayRefreshRateFB = CFUNCTYPE(Result.ctype(), Session, c_float)


class ViveTrackerPathsHTCX(Structure):
    def __init__(
        self,
        persistent_path: Path = 0,
        role_path: Path = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.VIVE_TRACKER_PATHS_HTCX,
    ) -> None:
        super().__init__(
            persistent_path=persistent_path,
            role_path=role_path,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ViveTrackerPathsHTCX(persistent_path={repr(self.persistent_path)}, role_path={repr(self.role_path)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ViveTrackerPathsHTCX(persistent_path={self.persistent_path}, role_path={self.role_path}, next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_VIVE_TRACKER_CONNECTED_HTCX,
    ) -> None:
        super().__init__(
            paths=paths,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataViveTrackerConnectedHTCX(paths={repr(self.paths)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataViveTrackerConnectedHTCX(paths={self.paths}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("paths", POINTER(ViveTrackerPathsHTCX)),
    ]


PFN_xrEnumerateViveTrackerPathsHTCX = CFUNCTYPE(Result.ctype(), Instance, c_uint32, POINTER(c_uint32), POINTER(ViveTrackerPathsHTCX))


class FacialTrackerHTC_T(Structure):
    pass


class FacialTrackerHTC(POINTER(FacialTrackerHTC_T), HandleMixin):
    _type_ = FacialTrackerHTC_T  # ctypes idiosyncrasy


class SystemFacialTrackingPropertiesHTC(Structure):
    def __init__(
        self,
        support_eye_facial_tracking: Bool32 = 0,
        support_lip_facial_tracking: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_FACIAL_TRACKING_PROPERTIES_HTC,
    ) -> None:
        super().__init__(
            support_eye_facial_tracking=support_eye_facial_tracking,
            support_lip_facial_tracking=support_lip_facial_tracking,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemFacialTrackingPropertiesHTC(support_eye_facial_tracking={repr(self.support_eye_facial_tracking)}, support_lip_facial_tracking={repr(self.support_lip_facial_tracking)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemFacialTrackingPropertiesHTC(support_eye_facial_tracking={self.support_eye_facial_tracking}, support_lip_facial_tracking={self.support_lip_facial_tracking}, next={self.next}, type={self.type})"

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
        expression_count: Optional[int] = None,
        expression_weightings: ArrayFieldParamType[c_float] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.FACIAL_EXPRESSIONS_HTC,
    ) -> None:
        expression_count, expression_weightings = array_field_helper(
            c_float, expression_count, expression_weightings)
        super().__init__(
            is_active=is_active,
            sample_time=sample_time,
            expression_count=expression_count,
            _expression_weightings=expression_weightings,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FacialExpressionsHTC(is_active={repr(self.is_active)}, sample_time={repr(self.sample_time)}, expression_count={repr(self.expression_count)}, expression_weightings={repr(self._expression_weightings)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FacialExpressionsHTC(is_active={self.is_active}, sample_time={self.sample_time}, expression_count={self.expression_count}, expression_weightings={self._expression_weightings}, next={self.next}, type={self.type})"

    @property
    def expression_weightings(self):
        if self.expression_count == 0:
            return (c_float * 0)()
        else:
            return (c_float * self.expression_count).from_address(
                ctypes.addressof(self._expression_weightings.contents))

    @expression_weightings.setter
    def expression_weightings(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.expression_count, self._expression_weightings = array_field_helper(
            c_float, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("is_active", Bool32),
        ("sample_time", Time),
        ("expression_count", c_uint32),
        ("_expression_weightings", POINTER(c_float)),
    ]


class FacialTrackerCreateInfoHTC(Structure):
    def __init__(
        self,
        facial_tracking_type: FacialTrackingTypeHTC = FacialTrackingTypeHTC(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.FACIAL_TRACKER_CREATE_INFO_HTC,
    ) -> None:
        super().__init__(
            facial_tracking_type=FacialTrackingTypeHTC(facial_tracking_type).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FacialTrackerCreateInfoHTC(facial_tracking_type={repr(self.facial_tracking_type)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FacialTrackerCreateInfoHTC(facial_tracking_type={self.facial_tracking_type}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("facial_tracking_type", FacialTrackingTypeHTC.ctype()),
    ]


PFN_xrCreateFacialTrackerHTC = CFUNCTYPE(Result.ctype(), Session, POINTER(FacialTrackerCreateInfoHTC), POINTER(FacialTrackerHTC))

PFN_xrDestroyFacialTrackerHTC = CFUNCTYPE(Result.ctype(), FacialTrackerHTC)

PFN_xrGetFacialExpressionsHTC = CFUNCTYPE(Result.ctype(), FacialTrackerHTC, POINTER(FacialExpressionsHTC))


class SystemColorSpacePropertiesFB(Structure):
    def __init__(
        self,
        color_space: ColorSpaceFB = ColorSpaceFB(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_COLOR_SPACE_PROPERTIES_FB,
    ) -> None:
        super().__init__(
            color_space=ColorSpaceFB(color_space).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemColorSpacePropertiesFB(color_space={repr(self.color_space)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemColorSpacePropertiesFB(color_space={self.color_space}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("color_space", ColorSpaceFB.ctype()),
    ]


PFN_xrEnumerateColorSpacesFB = CFUNCTYPE(Result.ctype(), Session, c_uint32, POINTER(c_uint32), POINTER(ColorSpaceFB.ctype()))

PFN_xrSetColorSpaceFB = CFUNCTYPE(Result.ctype(), Session, c_int)


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
        next: c_void_p = None,
        type: StructureType = StructureType.HAND_TRACKING_MESH_FB,
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
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.HandTrackingMeshFB(joint_capacity_input={repr(self.joint_capacity_input)}, joint_count_output={repr(self.joint_count_output)}, joint_bind_poses={repr(self.joint_bind_poses)}, joint_radii={repr(self.joint_radii)}, joint_parents={repr(self.joint_parents)}, vertex_capacity_input={repr(self.vertex_capacity_input)}, vertex_count_output={repr(self.vertex_count_output)}, vertex_positions={repr(self.vertex_positions)}, vertex_normals={repr(self.vertex_normals)}, vertex_uvs={repr(self.vertex_uvs)}, vertex_blend_indices={repr(self.vertex_blend_indices)}, vertex_blend_weights={repr(self.vertex_blend_weights)}, index_capacity_input={repr(self.index_capacity_input)}, index_count_output={repr(self.index_count_output)}, indices={repr(self.indices)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.HandTrackingMeshFB(joint_capacity_input={self.joint_capacity_input}, joint_count_output={self.joint_count_output}, joint_bind_poses={self.joint_bind_poses}, joint_radii={self.joint_radii}, joint_parents={self.joint_parents}, vertex_capacity_input={self.vertex_capacity_input}, vertex_count_output={self.vertex_count_output}, vertex_positions={self.vertex_positions}, vertex_normals={self.vertex_normals}, vertex_uvs={self.vertex_uvs}, vertex_blend_indices={self.vertex_blend_indices}, vertex_blend_weights={self.vertex_blend_weights}, index_capacity_input={self.index_capacity_input}, index_count_output={self.index_count_output}, indices={self.indices}, next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.HAND_TRACKING_SCALE_FB,
    ) -> None:
        super().__init__(
            sensor_output=sensor_output,
            current_output=current_output,
            override_hand_scale=override_hand_scale,
            override_value_input=override_value_input,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.HandTrackingScaleFB(sensor_output={repr(self.sensor_output)}, current_output={repr(self.current_output)}, override_hand_scale={repr(self.override_hand_scale)}, override_value_input={repr(self.override_value_input)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.HandTrackingScaleFB(sensor_output={self.sensor_output:.3f}, current_output={self.current_output:.3f}, override_hand_scale={self.override_hand_scale}, override_value_input={self.override_value_input:.3f}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("sensor_output", c_float),
        ("current_output", c_float),
        ("override_hand_scale", Bool32),
        ("override_value_input", c_float),
    ]


PFN_xrGetHandMeshFB = CFUNCTYPE(Result.ctype(), HandTrackerEXT, POINTER(HandTrackingMeshFB))

HandTrackingAimFlagsFBCInt = Flags64


class HandTrackingAimStateFB(Structure):
    def __init__(
        self,
        status: HandTrackingAimFlagsFB = HandTrackingAimFlagsFB(),  # noqa
        aim_pose: Posef = Posef(),
        pinch_strength_index: float = 0,
        pinch_strength_middle: float = 0,
        pinch_strength_ring: float = 0,
        pinch_strength_little: float = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.HAND_TRACKING_AIM_STATE_FB,
    ) -> None:
        super().__init__(
            status=HandTrackingAimFlagsFB(status).value,
            aim_pose=aim_pose,
            pinch_strength_index=pinch_strength_index,
            pinch_strength_middle=pinch_strength_middle,
            pinch_strength_ring=pinch_strength_ring,
            pinch_strength_little=pinch_strength_little,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.HandTrackingAimStateFB(status={repr(self.status)}, aim_pose={repr(self.aim_pose)}, pinch_strength_index={repr(self.pinch_strength_index)}, pinch_strength_middle={repr(self.pinch_strength_middle)}, pinch_strength_ring={repr(self.pinch_strength_ring)}, pinch_strength_little={repr(self.pinch_strength_little)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.HandTrackingAimStateFB(status={self.status}, aim_pose={self.aim_pose}, pinch_strength_index={self.pinch_strength_index:.3f}, pinch_strength_middle={self.pinch_strength_middle:.3f}, pinch_strength_ring={self.pinch_strength_ring:.3f}, pinch_strength_little={self.pinch_strength_little:.3f}, next={self.next}, type={self.type})"

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
        joint: HandJointEXT = HandJointEXT(),  # noqa
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
        next: c_void_p = None,
        type: StructureType = StructureType.HAND_TRACKING_CAPSULES_STATE_FB,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.HandTrackingCapsulesStateFB(capsules={repr(self.capsules)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.HandTrackingCapsulesStateFB(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("capsules", (HandCapsuleFB * 19)),
    ]


AsyncRequestIdFB = c_uint64


class SystemSpatialEntityPropertiesFB(Structure):
    def __init__(
        self,
        supports_spatial_entity: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_SPATIAL_ENTITY_PROPERTIES_FB,
    ) -> None:
        super().__init__(
            supports_spatial_entity=supports_spatial_entity,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemSpatialEntityPropertiesFB(supports_spatial_entity={repr(self.supports_spatial_entity)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemSpatialEntityPropertiesFB(supports_spatial_entity={self.supports_spatial_entity}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_spatial_entity", Bool32),
    ]


class SpatialAnchorCreateInfoFB(Structure):
    def __init__(
        self,
        space: Space = None,
        pose_in_space: Posef = Posef(),
        time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHOR_CREATE_INFO_FB,
    ) -> None:
        super().__init__(
            space=space,
            pose_in_space=pose_in_space,
            time=time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorCreateInfoFB(space={repr(self.space)}, pose_in_space={repr(self.pose_in_space)}, time={repr(self.time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorCreateInfoFB(space={self.space}, pose_in_space={self.pose_in_space}, time={self.time}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("space", Space),
        ("pose_in_space", Posef),
        ("time", Time),
    ]


class SpaceComponentStatusSetInfoFB(Structure):
    def __init__(
        self,
        component_type: SpaceComponentTypeFB = SpaceComponentTypeFB(),  # noqa
        enabled: Bool32 = 0,
        timeout: Duration = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SPACE_COMPONENT_STATUS_SET_INFO_FB,
    ) -> None:
        super().__init__(
            component_type=SpaceComponentTypeFB(component_type).value,
            enabled=enabled,
            timeout=timeout,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceComponentStatusSetInfoFB(component_type={repr(self.component_type)}, enabled={repr(self.enabled)}, timeout={repr(self.timeout)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpaceComponentStatusSetInfoFB(component_type={self.component_type}, enabled={self.enabled}, timeout={self.timeout}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("component_type", SpaceComponentTypeFB.ctype()),
        ("enabled", Bool32),
        ("timeout", Duration),
    ]


class SpaceComponentStatusFB(Structure):
    def __init__(
        self,
        enabled: Bool32 = 0,
        change_pending: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SPACE_COMPONENT_STATUS_FB,
    ) -> None:
        super().__init__(
            enabled=enabled,
            change_pending=change_pending,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceComponentStatusFB(enabled={repr(self.enabled)}, change_pending={repr(self.change_pending)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpaceComponentStatusFB(enabled={self.enabled}, change_pending={self.change_pending}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("enabled", Bool32),
        ("change_pending", Bool32),
    ]


UuidEXT = Uuid


class EventDataSpatialAnchorCreateCompleteFB(Structure):
    def __init__(
        self,
        request_id: AsyncRequestIdFB = 0,
        result: Result = Result(),  # noqa
        space: Space = None,
        uuid: UuidEXT = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_SPATIAL_ANCHOR_CREATE_COMPLETE_FB,
    ) -> None:
        super().__init__(
            request_id=request_id,
            result=Result(result).value,
            space=space,
            uuid=uuid,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataSpatialAnchorCreateCompleteFB(request_id={repr(self.request_id)}, result={repr(self.result)}, space={repr(self.space)}, uuid={repr(self.uuid)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataSpatialAnchorCreateCompleteFB(request_id={self.request_id}, result={self.result}, space={self.space}, uuid={self.uuid}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("request_id", AsyncRequestIdFB),
        ("result", Result.ctype()),
        ("space", Space),
        ("uuid", UuidEXT),
    ]


class EventDataSpaceSetStatusCompleteFB(Structure):
    def __init__(
        self,
        request_id: AsyncRequestIdFB = 0,
        result: Result = Result(),  # noqa
        space: Space = None,
        uuid: UuidEXT = 0,
        component_type: SpaceComponentTypeFB = SpaceComponentTypeFB(),  # noqa
        enabled: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_SPACE_SET_STATUS_COMPLETE_FB,
    ) -> None:
        super().__init__(
            request_id=request_id,
            result=Result(result).value,
            space=space,
            uuid=uuid,
            component_type=SpaceComponentTypeFB(component_type).value,
            enabled=enabled,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataSpaceSetStatusCompleteFB(request_id={repr(self.request_id)}, result={repr(self.result)}, space={repr(self.space)}, uuid={repr(self.uuid)}, component_type={repr(self.component_type)}, enabled={repr(self.enabled)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataSpaceSetStatusCompleteFB(request_id={self.request_id}, result={self.result}, space={self.space}, uuid={self.uuid}, component_type={self.component_type}, enabled={self.enabled}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("request_id", AsyncRequestIdFB),
        ("result", Result.ctype()),
        ("space", Space),
        ("uuid", UuidEXT),
        ("component_type", SpaceComponentTypeFB.ctype()),
        ("enabled", Bool32),
    ]


PFN_xrCreateSpatialAnchorFB = CFUNCTYPE(Result.ctype(), Session, POINTER(SpatialAnchorCreateInfoFB), POINTER(AsyncRequestIdFB))

PFN_xrGetSpaceUuidFB = CFUNCTYPE(Result.ctype(), Space, POINTER(UuidEXT))

PFN_xrEnumerateSpaceSupportedComponentsFB = CFUNCTYPE(Result.ctype(), Space, c_uint32, POINTER(c_uint32), POINTER(SpaceComponentTypeFB.ctype()))

PFN_xrSetSpaceComponentStatusFB = CFUNCTYPE(Result.ctype(), Space, POINTER(SpaceComponentStatusSetInfoFB), POINTER(AsyncRequestIdFB))

PFN_xrGetSpaceComponentStatusFB = CFUNCTYPE(Result.ctype(), Space, SpaceComponentTypeFB.ctype(), POINTER(SpaceComponentStatusFB))


class FoveationProfileFB_T(Structure):
    pass


class FoveationProfileFB(POINTER(FoveationProfileFB_T), HandleMixin):
    _type_ = FoveationProfileFB_T  # ctypes idiosyncrasy

SwapchainCreateFoveationFlagsFBCInt = Flags64

SwapchainStateFoveationFlagsFBCInt = Flags64


class FoveationProfileCreateInfoFB(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.FOVEATION_PROFILE_CREATE_INFO_FB,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FoveationProfileCreateInfoFB(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FoveationProfileCreateInfoFB(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SwapchainCreateInfoFoveationFB(Structure):
    def __init__(
        self,
        flags: SwapchainCreateFoveationFlagsFB = SwapchainCreateFoveationFlagsFB(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.SWAPCHAIN_CREATE_INFO_FOVEATION_FB,
    ) -> None:
        super().__init__(
            flags=SwapchainCreateFoveationFlagsFB(flags).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainCreateInfoFoveationFB(flags={repr(self.flags)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainCreateInfoFoveationFB(flags={self.flags}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", SwapchainCreateFoveationFlagsFBCInt),
    ]


class SwapchainStateFoveationFB(Structure):
    def __init__(
        self,
        flags: SwapchainStateFoveationFlagsFB = SwapchainStateFoveationFlagsFB(),  # noqa
        profile: FoveationProfileFB = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SWAPCHAIN_STATE_FOVEATION_FB,
    ) -> None:
        super().__init__(
            flags=SwapchainStateFoveationFlagsFB(flags).value,
            profile=profile,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainStateFoveationFB(flags={repr(self.flags)}, profile={repr(self.profile)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainStateFoveationFB(flags={self.flags}, profile={self.profile}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", SwapchainStateFoveationFlagsFBCInt),
        ("profile", FoveationProfileFB),
    ]


PFN_xrCreateFoveationProfileFB = CFUNCTYPE(Result.ctype(), Session, POINTER(FoveationProfileCreateInfoFB), POINTER(FoveationProfileFB))

PFN_xrDestroyFoveationProfileFB = CFUNCTYPE(Result.ctype(), FoveationProfileFB)


class FoveationLevelProfileCreateInfoFB(Structure):
    def __init__(
        self,
        level: FoveationLevelFB = FoveationLevelFB(),  # noqa
        vertical_offset: float = 0,
        dynamic: FoveationDynamicFB = FoveationDynamicFB(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.FOVEATION_LEVEL_PROFILE_CREATE_INFO_FB,
    ) -> None:
        super().__init__(
            level=FoveationLevelFB(level).value,
            vertical_offset=vertical_offset,
            dynamic=FoveationDynamicFB(dynamic).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FoveationLevelProfileCreateInfoFB(level={repr(self.level)}, vertical_offset={repr(self.vertical_offset)}, dynamic={repr(self.dynamic)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FoveationLevelProfileCreateInfoFB(level={self.level}, vertical_offset={self.vertical_offset:.3f}, dynamic={self.dynamic}, next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_KEYBOARD_TRACKING_PROPERTIES_FB,
    ) -> None:
        super().__init__(
            supports_keyboard_tracking=supports_keyboard_tracking,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemKeyboardTrackingPropertiesFB(supports_keyboard_tracking={repr(self.supports_keyboard_tracking)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemKeyboardTrackingPropertiesFB(supports_keyboard_tracking={self.supports_keyboard_tracking}, next={self.next}, type={self.type})"

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
        flags: KeyboardTrackingFlagsFB = KeyboardTrackingFlagsFB(),  # noqa
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
        next: c_void_p = None,
        type: StructureType = StructureType.KEYBOARD_SPACE_CREATE_INFO_FB,
    ) -> None:
        super().__init__(
            tracked_keyboard_id=tracked_keyboard_id,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.KeyboardSpaceCreateInfoFB(tracked_keyboard_id={repr(self.tracked_keyboard_id)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.KeyboardSpaceCreateInfoFB(tracked_keyboard_id={self.tracked_keyboard_id}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("tracked_keyboard_id", c_uint64),
    ]


class KeyboardTrackingQueryFB(Structure):
    def __init__(
        self,
        flags: KeyboardTrackingQueryFlagsFB = KeyboardTrackingQueryFlagsFB(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.KEYBOARD_TRACKING_QUERY_FB,
    ) -> None:
        super().__init__(
            flags=KeyboardTrackingQueryFlagsFB(flags).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.KeyboardTrackingQueryFB(flags={repr(self.flags)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.KeyboardTrackingQueryFB(flags={self.flags}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", KeyboardTrackingQueryFlagsFBCInt),
    ]


PFN_xrQuerySystemTrackedKeyboardFB = CFUNCTYPE(Result.ctype(), Session, POINTER(KeyboardTrackingQueryFB), POINTER(KeyboardTrackingDescriptionFB))

PFN_xrCreateKeyboardSpaceFB = CFUNCTYPE(Result.ctype(), Session, POINTER(KeyboardSpaceCreateInfoFB), POINTER(Space))


class TriangleMeshFB_T(Structure):
    pass


class TriangleMeshFB(POINTER(TriangleMeshFB_T), HandleMixin):
    _type_ = TriangleMeshFB_T  # ctypes idiosyncrasy

TriangleMeshFlagsFBCInt = Flags64


class TriangleMeshCreateInfoFB(Structure):
    def __init__(
        self,
        flags: TriangleMeshFlagsFB = TriangleMeshFlagsFB(),  # noqa
        winding_order: WindingOrderFB = WindingOrderFB(),  # noqa
        vertex_count: int = 0,
        vertex_buffer: POINTER(Vector3f) = None,
        triangle_count: int = 0,
        index_buffer: POINTER(c_uint32) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.TRIANGLE_MESH_CREATE_INFO_FB,
    ) -> None:
        super().__init__(
            flags=TriangleMeshFlagsFB(flags).value,
            winding_order=WindingOrderFB(winding_order).value,
            vertex_count=vertex_count,
            vertex_buffer=vertex_buffer,
            triangle_count=triangle_count,
            index_buffer=index_buffer,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.TriangleMeshCreateInfoFB(flags={repr(self.flags)}, winding_order={repr(self.winding_order)}, vertex_count={repr(self.vertex_count)}, vertex_buffer={repr(self.vertex_buffer)}, triangle_count={repr(self.triangle_count)}, index_buffer={repr(self.index_buffer)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.TriangleMeshCreateInfoFB(flags={self.flags}, winding_order={self.winding_order}, vertex_count={self.vertex_count}, vertex_buffer={self.vertex_buffer}, triangle_count={self.triangle_count}, index_buffer={self.index_buffer}, next={self.next}, type={self.type})"

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


PFN_xrCreateTriangleMeshFB = CFUNCTYPE(Result.ctype(), Session, POINTER(TriangleMeshCreateInfoFB), POINTER(TriangleMeshFB))

PFN_xrDestroyTriangleMeshFB = CFUNCTYPE(Result.ctype(), TriangleMeshFB)

PFN_xrTriangleMeshGetVertexBufferFB = CFUNCTYPE(Result.ctype(), TriangleMeshFB, POINTER(POINTER(Vector3f)))

PFN_xrTriangleMeshGetIndexBufferFB = CFUNCTYPE(Result.ctype(), TriangleMeshFB, POINTER(POINTER(c_uint32)))

PFN_xrTriangleMeshBeginUpdateFB = CFUNCTYPE(Result.ctype(), TriangleMeshFB)

PFN_xrTriangleMeshEndUpdateFB = CFUNCTYPE(Result.ctype(), TriangleMeshFB, c_uint32, c_uint32)

PFN_xrTriangleMeshBeginVertexBufferUpdateFB = CFUNCTYPE(Result.ctype(), TriangleMeshFB, POINTER(c_uint32))

PFN_xrTriangleMeshEndVertexBufferUpdateFB = CFUNCTYPE(Result.ctype(), TriangleMeshFB)


class PassthroughFB_T(Structure):
    pass


class PassthroughFB(POINTER(PassthroughFB_T), HandleMixin):
    _type_ = PassthroughFB_T  # ctypes idiosyncrasy


class PassthroughLayerFB_T(Structure):
    pass


class PassthroughLayerFB(POINTER(PassthroughLayerFB_T), HandleMixin):
    _type_ = PassthroughLayerFB_T  # ctypes idiosyncrasy


class GeometryInstanceFB_T(Structure):
    pass


class GeometryInstanceFB(POINTER(GeometryInstanceFB_T), HandleMixin):
    _type_ = GeometryInstanceFB_T  # ctypes idiosyncrasy

PassthroughCapabilityFlagsFBCInt = Flags64

PassthroughFlagsFBCInt = Flags64

PassthroughStateChangedFlagsFBCInt = Flags64


class SystemPassthroughPropertiesFB(Structure):
    def __init__(
        self,
        supports_passthrough: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_PASSTHROUGH_PROPERTIES_FB,
    ) -> None:
        super().__init__(
            supports_passthrough=supports_passthrough,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemPassthroughPropertiesFB(supports_passthrough={repr(self.supports_passthrough)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemPassthroughPropertiesFB(supports_passthrough={self.supports_passthrough}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_passthrough", Bool32),
    ]


class SystemPassthroughProperties2FB(Structure):
    def __init__(
        self,
        capabilities: PassthroughCapabilityFlagsFB = PassthroughCapabilityFlagsFB(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_PASSTHROUGH_PROPERTIES2_FB,
    ) -> None:
        super().__init__(
            capabilities=PassthroughCapabilityFlagsFB(capabilities).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemPassthroughProperties2FB(capabilities={repr(self.capabilities)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemPassthroughProperties2FB(capabilities={self.capabilities}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("capabilities", PassthroughCapabilityFlagsFBCInt),
    ]


class PassthroughCreateInfoFB(Structure):
    def __init__(
        self,
        flags: PassthroughFlagsFB = PassthroughFlagsFB(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.PASSTHROUGH_CREATE_INFO_FB,
    ) -> None:
        super().__init__(
            flags=PassthroughFlagsFB(flags).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PassthroughCreateInfoFB(flags={repr(self.flags)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PassthroughCreateInfoFB(flags={self.flags}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", PassthroughFlagsFBCInt),
    ]


class PassthroughLayerCreateInfoFB(Structure):
    def __init__(
        self,
        passthrough: PassthroughFB = None,
        flags: PassthroughFlagsFB = PassthroughFlagsFB(),  # noqa
        purpose: PassthroughLayerPurposeFB = PassthroughLayerPurposeFB(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.PASSTHROUGH_LAYER_CREATE_INFO_FB,
    ) -> None:
        super().__init__(
            passthrough=passthrough,
            flags=PassthroughFlagsFB(flags).value,
            purpose=PassthroughLayerPurposeFB(purpose).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PassthroughLayerCreateInfoFB(passthrough={repr(self.passthrough)}, flags={repr(self.flags)}, purpose={repr(self.purpose)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PassthroughLayerCreateInfoFB(passthrough={self.passthrough}, flags={self.flags}, purpose={self.purpose}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("passthrough", PassthroughFB),
        ("flags", PassthroughFlagsFBCInt),
        ("purpose", PassthroughLayerPurposeFB.ctype()),
    ]


class CompositionLayerPassthroughFB(Structure):
    def __init__(
        self,
        flags: CompositionLayerFlags = CompositionLayerFlags(),  # noqa
        space: Space = None,
        layer_handle: PassthroughLayerFB = None,
        next: c_void_p = None,
        type: StructureType = StructureType.COMPOSITION_LAYER_PASSTHROUGH_FB,
    ) -> None:
        super().__init__(
            flags=CompositionLayerFlags(flags).value,
            space=space,
            layer_handle=layer_handle,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerPassthroughFB(flags={repr(self.flags)}, space={repr(self.space)}, layer_handle={repr(self.layer_handle)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerPassthroughFB(flags={self.flags}, space={self.space}, layer_handle={self.layer_handle}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", CompositionLayerFlagsCInt),
        ("space", Space),
        ("layer_handle", PassthroughLayerFB),
    ]


class GeometryInstanceCreateInfoFB(Structure):
    def __init__(
        self,
        layer: PassthroughLayerFB = None,
        mesh: TriangleMeshFB = None,
        base_space: Space = None,
        pose: Posef = Posef(),
        scale: Vector3f = None,
        next: c_void_p = None,
        type: StructureType = StructureType.GEOMETRY_INSTANCE_CREATE_INFO_FB,
    ) -> None:
        if scale is None:
            scale = Vector3f()
        super().__init__(
            layer=layer,
            mesh=mesh,
            base_space=base_space,
            pose=pose,
            scale=scale,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.GeometryInstanceCreateInfoFB(layer={repr(self.layer)}, mesh={repr(self.mesh)}, base_space={repr(self.base_space)}, pose={repr(self.pose)}, scale={repr(self.scale)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.GeometryInstanceCreateInfoFB(layer={self.layer}, mesh={self.mesh}, base_space={self.base_space}, pose={self.pose}, scale={self.scale}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer", PassthroughLayerFB),
        ("mesh", TriangleMeshFB),
        ("base_space", Space),
        ("pose", Posef),
        ("scale", Vector3f),
    ]


class GeometryInstanceTransformFB(Structure):
    def __init__(
        self,
        base_space: Space = None,
        time: Time = 0,
        pose: Posef = Posef(),
        scale: Vector3f = None,
        next: c_void_p = None,
        type: StructureType = StructureType.GEOMETRY_INSTANCE_TRANSFORM_FB,
    ) -> None:
        if scale is None:
            scale = Vector3f()
        super().__init__(
            base_space=base_space,
            time=time,
            pose=pose,
            scale=scale,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.GeometryInstanceTransformFB(base_space={repr(self.base_space)}, time={repr(self.time)}, pose={repr(self.pose)}, scale={repr(self.scale)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.GeometryInstanceTransformFB(base_space={self.base_space}, time={self.time}, pose={self.pose}, scale={self.scale}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("base_space", Space),
        ("time", Time),
        ("pose", Posef),
        ("scale", Vector3f),
    ]


class PassthroughStyleFB(Structure):
    def __init__(
        self,
        texture_opacity_factor: float = 0,
        edge_color: Color4f = None,
        next: c_void_p = None,
        type: StructureType = StructureType.PASSTHROUGH_STYLE_FB,
    ) -> None:
        if edge_color is None:
            edge_color = Color4f()
        super().__init__(
            texture_opacity_factor=texture_opacity_factor,
            edge_color=edge_color,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PassthroughStyleFB(texture_opacity_factor={repr(self.texture_opacity_factor)}, edge_color={repr(self.edge_color)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PassthroughStyleFB(texture_opacity_factor={self.texture_opacity_factor:.3f}, edge_color={self.edge_color}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("texture_opacity_factor", c_float),
        ("edge_color", Color4f),
    ]


class PassthroughColorMapMonoToRgbaFB(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.PASSTHROUGH_COLOR_MAP_MONO_TO_RGBA_FB,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PassthroughColorMapMonoToRgbaFB(texture_color_map={repr(self.texture_color_map)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PassthroughColorMapMonoToRgbaFB(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("texture_color_map", (Color4f * 256)),
    ]


class PassthroughColorMapMonoToMonoFB(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.PASSTHROUGH_COLOR_MAP_MONO_TO_MONO_FB,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PassthroughColorMapMonoToMonoFB(texture_color_map={repr(self.texture_color_map)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PassthroughColorMapMonoToMonoFB(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("texture_color_map", (c_uint8 * 256)),
    ]


class PassthroughBrightnessContrastSaturationFB(Structure):
    def __init__(
        self,
        brightness: float = 0,
        contrast: float = 0,
        saturation: float = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.PASSTHROUGH_BRIGHTNESS_CONTRAST_SATURATION_FB,
    ) -> None:
        super().__init__(
            brightness=brightness,
            contrast=contrast,
            saturation=saturation,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PassthroughBrightnessContrastSaturationFB(brightness={repr(self.brightness)}, contrast={repr(self.contrast)}, saturation={repr(self.saturation)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PassthroughBrightnessContrastSaturationFB(brightness={self.brightness:.3f}, contrast={self.contrast:.3f}, saturation={self.saturation:.3f}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("brightness", c_float),
        ("contrast", c_float),
        ("saturation", c_float),
    ]


class EventDataPassthroughStateChangedFB(Structure):
    def __init__(
        self,
        flags: PassthroughStateChangedFlagsFB = PassthroughStateChangedFlagsFB(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_PASSTHROUGH_STATE_CHANGED_FB,
    ) -> None:
        super().__init__(
            flags=PassthroughStateChangedFlagsFB(flags).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataPassthroughStateChangedFB(flags={repr(self.flags)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataPassthroughStateChangedFB(flags={self.flags}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", PassthroughStateChangedFlagsFBCInt),
    ]


PFN_xrCreatePassthroughFB = CFUNCTYPE(Result.ctype(), Session, POINTER(PassthroughCreateInfoFB), POINTER(PassthroughFB))

PFN_xrDestroyPassthroughFB = CFUNCTYPE(Result.ctype(), PassthroughFB)

PFN_xrPassthroughStartFB = CFUNCTYPE(Result.ctype(), PassthroughFB)

PFN_xrPassthroughPauseFB = CFUNCTYPE(Result.ctype(), PassthroughFB)

PFN_xrCreatePassthroughLayerFB = CFUNCTYPE(Result.ctype(), Session, POINTER(PassthroughLayerCreateInfoFB), POINTER(PassthroughLayerFB))

PFN_xrDestroyPassthroughLayerFB = CFUNCTYPE(Result.ctype(), PassthroughLayerFB)

PFN_xrPassthroughLayerPauseFB = CFUNCTYPE(Result.ctype(), PassthroughLayerFB)

PFN_xrPassthroughLayerResumeFB = CFUNCTYPE(Result.ctype(), PassthroughLayerFB)

PFN_xrPassthroughLayerSetStyleFB = CFUNCTYPE(Result.ctype(), PassthroughLayerFB, POINTER(PassthroughStyleFB))

PFN_xrCreateGeometryInstanceFB = CFUNCTYPE(Result.ctype(), Session, POINTER(GeometryInstanceCreateInfoFB), POINTER(GeometryInstanceFB))

PFN_xrDestroyGeometryInstanceFB = CFUNCTYPE(Result.ctype(), GeometryInstanceFB)

PFN_xrGeometryInstanceSetTransformFB = CFUNCTYPE(Result.ctype(), GeometryInstanceFB, POINTER(GeometryInstanceTransformFB))

RenderModelKeyFB = c_uint64

RenderModelFlagsFBCInt = Flags64


class RenderModelPathInfoFB(Structure):
    def __init__(
        self,
        path: Path = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.RENDER_MODEL_PATH_INFO_FB,
    ) -> None:
        super().__init__(
            path=path,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.RenderModelPathInfoFB(path={repr(self.path)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.RenderModelPathInfoFB(path={self.path}, next={self.next}, type={self.type})"

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
        flags: RenderModelFlagsFB = RenderModelFlagsFB(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.RENDER_MODEL_PROPERTIES_FB,
    ) -> None:
        super().__init__(
            vendor_id=vendor_id,
            model_name=model_name.encode(),
            model_key=model_key,
            model_version=model_version,
            flags=RenderModelFlagsFB(flags).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.RenderModelPropertiesFB(vendor_id={repr(self.vendor_id)}, model_name={repr(self.model_name)}, model_key={repr(self.model_key)}, model_version={repr(self.model_version)}, flags={repr(self.flags)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.RenderModelPropertiesFB(vendor_id={self.vendor_id}, model_name={self.model_name}, model_key={self.model_key}, model_version={self.model_version}, flags={self.flags}, next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.RENDER_MODEL_BUFFER_FB,
    ) -> None:
        super().__init__(
            buffer_capacity_input=buffer_capacity_input,
            buffer_count_output=buffer_count_output,
            buffer=buffer,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.RenderModelBufferFB(buffer_capacity_input={repr(self.buffer_capacity_input)}, buffer_count_output={repr(self.buffer_count_output)}, buffer={repr(self.buffer)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.RenderModelBufferFB(buffer_capacity_input={self.buffer_capacity_input}, buffer_count_output={self.buffer_count_output}, buffer={self.buffer}, next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.RENDER_MODEL_LOAD_INFO_FB,
    ) -> None:
        super().__init__(
            model_key=model_key,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.RenderModelLoadInfoFB(model_key={repr(self.model_key)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.RenderModelLoadInfoFB(model_key={self.model_key}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("model_key", RenderModelKeyFB),
    ]


class SystemRenderModelPropertiesFB(Structure):
    def __init__(
        self,
        supports_render_model_loading: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_RENDER_MODEL_PROPERTIES_FB,
    ) -> None:
        super().__init__(
            supports_render_model_loading=supports_render_model_loading,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemRenderModelPropertiesFB(supports_render_model_loading={repr(self.supports_render_model_loading)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemRenderModelPropertiesFB(supports_render_model_loading={self.supports_render_model_loading}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_render_model_loading", Bool32),
    ]


class RenderModelCapabilitiesRequestFB(Structure):
    def __init__(
        self,
        flags: RenderModelFlagsFB = RenderModelFlagsFB(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.RENDER_MODEL_CAPABILITIES_REQUEST_FB,
    ) -> None:
        super().__init__(
            flags=RenderModelFlagsFB(flags).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.RenderModelCapabilitiesRequestFB(flags={repr(self.flags)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.RenderModelCapabilitiesRequestFB(flags={self.flags}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", RenderModelFlagsFBCInt),
    ]


PFN_xrEnumerateRenderModelPathsFB = CFUNCTYPE(Result.ctype(), Session, c_uint32, POINTER(c_uint32), POINTER(RenderModelPathInfoFB))

PFN_xrGetRenderModelPropertiesFB = CFUNCTYPE(Result.ctype(), Session, Path, POINTER(RenderModelPropertiesFB))

PFN_xrLoadRenderModelFB = CFUNCTYPE(Result.ctype(), Session, POINTER(RenderModelLoadInfoFB), POINTER(RenderModelBufferFB))


class ViewLocateFoveatedRenderingVARJO(Structure):
    def __init__(
        self,
        foveated_rendering_active: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.VIEW_LOCATE_FOVEATED_RENDERING_VARJO,
    ) -> None:
        super().__init__(
            foveated_rendering_active=foveated_rendering_active,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ViewLocateFoveatedRenderingVARJO(foveated_rendering_active={repr(self.foveated_rendering_active)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ViewLocateFoveatedRenderingVARJO(foveated_rendering_active={self.foveated_rendering_active}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("foveated_rendering_active", Bool32),
    ]


class FoveatedViewConfigurationViewVARJO(Structure):
    def __init__(
        self,
        foveated_rendering_active: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.FOVEATED_VIEW_CONFIGURATION_VIEW_VARJO,
    ) -> None:
        super().__init__(
            foveated_rendering_active=foveated_rendering_active,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FoveatedViewConfigurationViewVARJO(foveated_rendering_active={repr(self.foveated_rendering_active)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FoveatedViewConfigurationViewVARJO(foveated_rendering_active={self.foveated_rendering_active}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("foveated_rendering_active", Bool32),
    ]


class SystemFoveatedRenderingPropertiesVARJO(Structure):
    def __init__(
        self,
        supports_foveated_rendering: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_FOVEATED_RENDERING_PROPERTIES_VARJO,
    ) -> None:
        super().__init__(
            supports_foveated_rendering=supports_foveated_rendering,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemFoveatedRenderingPropertiesVARJO(supports_foveated_rendering={repr(self.supports_foveated_rendering)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemFoveatedRenderingPropertiesVARJO(supports_foveated_rendering={self.supports_foveated_rendering}, next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.COMPOSITION_LAYER_DEPTH_TEST_VARJO,
    ) -> None:
        super().__init__(
            depth_test_range_near_z=depth_test_range_near_z,
            depth_test_range_far_z=depth_test_range_far_z,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerDepthTestVARJO(depth_test_range_near_z={repr(self.depth_test_range_near_z)}, depth_test_range_far_z={repr(self.depth_test_range_far_z)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerDepthTestVARJO(depth_test_range_near_z={self.depth_test_range_near_z:.3f}, depth_test_range_far_z={self.depth_test_range_far_z:.3f}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("depth_test_range_near_z", c_float),
        ("depth_test_range_far_z", c_float),
    ]


PFN_xrSetEnvironmentDepthEstimationVARJO = CFUNCTYPE(Result.ctype(), Session, Bool32)


class SystemMarkerTrackingPropertiesVARJO(Structure):
    def __init__(
        self,
        supports_marker_tracking: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_MARKER_TRACKING_PROPERTIES_VARJO,
    ) -> None:
        super().__init__(
            supports_marker_tracking=supports_marker_tracking,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemMarkerTrackingPropertiesVARJO(supports_marker_tracking={repr(self.supports_marker_tracking)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemMarkerTrackingPropertiesVARJO(supports_marker_tracking={self.supports_marker_tracking}, next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_MARKER_TRACKING_UPDATE_VARJO,
    ) -> None:
        super().__init__(
            marker_id=marker_id,
            is_active=is_active,
            is_predicted=is_predicted,
            time=time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataMarkerTrackingUpdateVARJO(marker_id={repr(self.marker_id)}, is_active={repr(self.is_active)}, is_predicted={repr(self.is_predicted)}, time={repr(self.time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataMarkerTrackingUpdateVARJO(marker_id={self.marker_id}, is_active={self.is_active}, is_predicted={self.is_predicted}, time={self.time}, next={self.next}, type={self.type})"

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
        pose_in_marker_space: Posef = Posef(),
        next: c_void_p = None,
        type: StructureType = StructureType.MARKER_SPACE_CREATE_INFO_VARJO,
    ) -> None:
        super().__init__(
            marker_id=marker_id,
            pose_in_marker_space=pose_in_marker_space,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.MarkerSpaceCreateInfoVARJO(marker_id={repr(self.marker_id)}, pose_in_marker_space={repr(self.pose_in_marker_space)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.MarkerSpaceCreateInfoVARJO(marker_id={self.marker_id}, pose_in_marker_space={self.pose_in_marker_space}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("marker_id", c_uint64),
        ("pose_in_marker_space", Posef),
    ]


PFN_xrSetMarkerTrackingVARJO = CFUNCTYPE(Result.ctype(), Session, Bool32)

PFN_xrSetMarkerTrackingTimeoutVARJO = CFUNCTYPE(Result.ctype(), Session, c_uint64, Duration)

PFN_xrSetMarkerTrackingPredictionVARJO = CFUNCTYPE(Result.ctype(), Session, c_uint64, Bool32)

PFN_xrGetMarkerSizeVARJO = CFUNCTYPE(Result.ctype(), Session, c_uint64, POINTER(Extent2Df))

PFN_xrCreateMarkerSpaceVARJO = CFUNCTYPE(Result.ctype(), Session, POINTER(MarkerSpaceCreateInfoVARJO), POINTER(Space))

PFN_xrSetViewOffsetVARJO = CFUNCTYPE(Result.ctype(), Session, c_float)

FrameEndInfoFlagsMLCInt = Flags64


class FrameEndInfoML(Structure):
    def __init__(
        self,
        focus_distance: float = 0,
        flags: FrameEndInfoFlagsML = FrameEndInfoFlagsML(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.FRAME_END_INFO_ML,
    ) -> None:
        super().__init__(
            focus_distance=focus_distance,
            flags=FrameEndInfoFlagsML(flags).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FrameEndInfoML(focus_distance={repr(self.focus_distance)}, flags={repr(self.flags)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FrameEndInfoML(focus_distance={self.focus_distance:.3f}, flags={self.flags}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("focus_distance", c_float),
        ("flags", FrameEndInfoFlagsMLCInt),
    ]


GlobalDimmerFrameEndInfoFlagsMLCInt = Flags64


class GlobalDimmerFrameEndInfoML(Structure):
    def __init__(
        self,
        dimmer_value: float = 0,
        flags: GlobalDimmerFrameEndInfoFlagsML = GlobalDimmerFrameEndInfoFlagsML(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.GLOBAL_DIMMER_FRAME_END_INFO_ML,
    ) -> None:
        super().__init__(
            dimmer_value=dimmer_value,
            flags=GlobalDimmerFrameEndInfoFlagsML(flags).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.GlobalDimmerFrameEndInfoML(dimmer_value={repr(self.dimmer_value)}, flags={repr(self.flags)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.GlobalDimmerFrameEndInfoML(dimmer_value={self.dimmer_value:.3f}, flags={self.flags}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("dimmer_value", c_float),
        ("flags", GlobalDimmerFrameEndInfoFlagsMLCInt),
    ]


MarkerML = c_uint64


class MarkerDetectorML_T(Structure):
    pass


class MarkerDetectorML(POINTER(MarkerDetectorML_T), HandleMixin):
    _type_ = MarkerDetectorML_T  # ctypes idiosyncrasy


class SystemMarkerUnderstandingPropertiesML(Structure):
    def __init__(
        self,
        supports_marker_understanding: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_MARKER_UNDERSTANDING_PROPERTIES_ML,
    ) -> None:
        super().__init__(
            supports_marker_understanding=supports_marker_understanding,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemMarkerUnderstandingPropertiesML(supports_marker_understanding={repr(self.supports_marker_understanding)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemMarkerUnderstandingPropertiesML(supports_marker_understanding={self.supports_marker_understanding}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_marker_understanding", Bool32),
    ]


class MarkerDetectorCreateInfoML(Structure):
    def __init__(
        self,
        profile: MarkerDetectorProfileML = MarkerDetectorProfileML(),  # noqa
        marker_type: MarkerTypeML = MarkerTypeML(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.MARKER_DETECTOR_CREATE_INFO_ML,
    ) -> None:
        super().__init__(
            profile=MarkerDetectorProfileML(profile).value,
            marker_type=MarkerTypeML(marker_type).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.MarkerDetectorCreateInfoML(profile={repr(self.profile)}, marker_type={repr(self.marker_type)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.MarkerDetectorCreateInfoML(profile={self.profile}, marker_type={self.marker_type}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("profile", MarkerDetectorProfileML.ctype()),
        ("marker_type", MarkerTypeML.ctype()),
    ]


class MarkerDetectorArucoInfoML(Structure):
    def __init__(
        self,
        aruco_dict: MarkerArucoDictML = MarkerArucoDictML(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.MARKER_DETECTOR_ARUCO_INFO_ML,
    ) -> None:
        super().__init__(
            aruco_dict=MarkerArucoDictML(aruco_dict).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.MarkerDetectorArucoInfoML(aruco_dict={repr(self.aruco_dict)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.MarkerDetectorArucoInfoML(aruco_dict={self.aruco_dict}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("aruco_dict", MarkerArucoDictML.ctype()),
    ]


class MarkerDetectorSizeInfoML(Structure):
    def __init__(
        self,
        marker_length: float = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.MARKER_DETECTOR_SIZE_INFO_ML,
    ) -> None:
        super().__init__(
            marker_length=marker_length,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.MarkerDetectorSizeInfoML(marker_length={repr(self.marker_length)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.MarkerDetectorSizeInfoML(marker_length={self.marker_length:.3f}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("marker_length", c_float),
    ]


class MarkerDetectorAprilTagInfoML(Structure):
    def __init__(
        self,
        april_tag_dict: MarkerAprilTagDictML = MarkerAprilTagDictML(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.MARKER_DETECTOR_APRIL_TAG_INFO_ML,
    ) -> None:
        super().__init__(
            april_tag_dict=MarkerAprilTagDictML(april_tag_dict).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.MarkerDetectorAprilTagInfoML(april_tag_dict={repr(self.april_tag_dict)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.MarkerDetectorAprilTagInfoML(april_tag_dict={self.april_tag_dict}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("april_tag_dict", MarkerAprilTagDictML.ctype()),
    ]


class MarkerDetectorCustomProfileInfoML(Structure):
    def __init__(
        self,
        fps_hint: MarkerDetectorFpsML = MarkerDetectorFpsML(),  # noqa
        resolution_hint: MarkerDetectorResolutionML = MarkerDetectorResolutionML(),  # noqa
        camera_hint: MarkerDetectorCameraML = MarkerDetectorCameraML(),  # noqa
        corner_refine_method: MarkerDetectorCornerRefineMethodML = MarkerDetectorCornerRefineMethodML(),  # noqa
        use_edge_refinement: Bool32 = 0,
        full_analysis_interval_hint: MarkerDetectorFullAnalysisIntervalML = MarkerDetectorFullAnalysisIntervalML(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.MARKER_DETECTOR_CUSTOM_PROFILE_INFO_ML,
    ) -> None:
        super().__init__(
            fps_hint=MarkerDetectorFpsML(fps_hint).value,
            resolution_hint=MarkerDetectorResolutionML(resolution_hint).value,
            camera_hint=MarkerDetectorCameraML(camera_hint).value,
            corner_refine_method=MarkerDetectorCornerRefineMethodML(corner_refine_method).value,
            use_edge_refinement=use_edge_refinement,
            full_analysis_interval_hint=MarkerDetectorFullAnalysisIntervalML(full_analysis_interval_hint).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.MarkerDetectorCustomProfileInfoML(fps_hint={repr(self.fps_hint)}, resolution_hint={repr(self.resolution_hint)}, camera_hint={repr(self.camera_hint)}, corner_refine_method={repr(self.corner_refine_method)}, use_edge_refinement={repr(self.use_edge_refinement)}, full_analysis_interval_hint={repr(self.full_analysis_interval_hint)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.MarkerDetectorCustomProfileInfoML(fps_hint={self.fps_hint}, resolution_hint={self.resolution_hint}, camera_hint={self.camera_hint}, corner_refine_method={self.corner_refine_method}, use_edge_refinement={self.use_edge_refinement}, full_analysis_interval_hint={self.full_analysis_interval_hint}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("fps_hint", MarkerDetectorFpsML.ctype()),
        ("resolution_hint", MarkerDetectorResolutionML.ctype()),
        ("camera_hint", MarkerDetectorCameraML.ctype()),
        ("corner_refine_method", MarkerDetectorCornerRefineMethodML.ctype()),
        ("use_edge_refinement", Bool32),
        ("full_analysis_interval_hint", MarkerDetectorFullAnalysisIntervalML.ctype()),
    ]


class MarkerDetectorSnapshotInfoML(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.MARKER_DETECTOR_SNAPSHOT_INFO_ML,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.MarkerDetectorSnapshotInfoML(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.MarkerDetectorSnapshotInfoML(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class MarkerDetectorStateML(Structure):
    def __init__(
        self,
        state: MarkerDetectorStatusML = MarkerDetectorStatusML(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.MARKER_DETECTOR_STATE_ML,
    ) -> None:
        super().__init__(
            state=MarkerDetectorStatusML(state).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.MarkerDetectorStateML(state={repr(self.state)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.MarkerDetectorStateML(state={self.state}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("state", MarkerDetectorStatusML.ctype()),
    ]


class MarkerSpaceCreateInfoML(Structure):
    def __init__(
        self,
        marker_detector: MarkerDetectorML = None,
        marker: MarkerML = 0,
        pose_in_marker_space: Posef = Posef(),
        next: c_void_p = None,
        type: StructureType = StructureType.MARKER_SPACE_CREATE_INFO_ML,
    ) -> None:
        super().__init__(
            marker_detector=marker_detector,
            marker=marker,
            pose_in_marker_space=pose_in_marker_space,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.MarkerSpaceCreateInfoML(marker_detector={repr(self.marker_detector)}, marker={repr(self.marker)}, pose_in_marker_space={repr(self.pose_in_marker_space)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.MarkerSpaceCreateInfoML(marker_detector={self.marker_detector}, marker={self.marker}, pose_in_marker_space={self.pose_in_marker_space}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("marker_detector", MarkerDetectorML),
        ("marker", MarkerML),
        ("pose_in_marker_space", Posef),
    ]


PFN_xrCreateMarkerDetectorML = CFUNCTYPE(Result.ctype(), Session, POINTER(MarkerDetectorCreateInfoML), POINTER(MarkerDetectorML))

PFN_xrDestroyMarkerDetectorML = CFUNCTYPE(Result.ctype(), MarkerDetectorML)

PFN_xrSnapshotMarkerDetectorML = CFUNCTYPE(Result.ctype(), MarkerDetectorML, POINTER(MarkerDetectorSnapshotInfoML))

PFN_xrGetMarkerDetectorStateML = CFUNCTYPE(Result.ctype(), MarkerDetectorML, POINTER(MarkerDetectorStateML))

PFN_xrGetMarkersML = CFUNCTYPE(Result.ctype(), MarkerDetectorML, c_uint32, POINTER(c_uint32), POINTER(MarkerML))

PFN_xrGetMarkerReprojectionErrorML = CFUNCTYPE(Result.ctype(), MarkerDetectorML, MarkerML, POINTER(c_float))

PFN_xrGetMarkerLengthML = CFUNCTYPE(Result.ctype(), MarkerDetectorML, MarkerML, POINTER(c_float))

PFN_xrGetMarkerNumberML = CFUNCTYPE(Result.ctype(), MarkerDetectorML, MarkerML, POINTER(c_uint64))

PFN_xrGetMarkerStringML = CFUNCTYPE(Result.ctype(), MarkerDetectorML, MarkerML, c_uint32, POINTER(c_uint32), c_char_p)

PFN_xrCreateMarkerSpaceML = CFUNCTYPE(Result.ctype(), Session, POINTER(MarkerSpaceCreateInfoML), POINTER(Space))


class ExportedLocalizationMapML_T(Structure):
    pass


class ExportedLocalizationMapML(POINTER(ExportedLocalizationMapML_T), HandleMixin):
    _type_ = ExportedLocalizationMapML_T  # ctypes idiosyncrasy

LocalizationMapErrorFlagsMLCInt = Flags64


class LocalizationMapML(Structure):
    def __init__(
        self,
        name: str = "",
        map_uuid: UuidEXT = 0,
        map_type: LocalizationMapTypeML = LocalizationMapTypeML(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.LOCALIZATION_MAP_ML,
    ) -> None:
        super().__init__(
            name=name.encode(),
            map_uuid=map_uuid,
            map_type=LocalizationMapTypeML(map_type).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.LocalizationMapML(name={repr(self.name)}, map_uuid={repr(self.map_uuid)}, map_type={repr(self.map_type)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.LocalizationMapML(name={self.name}, map_uuid={self.map_uuid}, map_type={self.map_type}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("name", (c_char * 64)),
        ("map_uuid", UuidEXT),
        ("map_type", LocalizationMapTypeML.ctype()),
    ]


class EventDataLocalizationChangedML(Structure):
    def __init__(
        self,
        session: Session = None,
        state: LocalizationMapStateML = LocalizationMapStateML(),  # noqa
        map: LocalizationMapML = None,
        confidence: LocalizationMapConfidenceML = LocalizationMapConfidenceML(),  # noqa
        error_flags: LocalizationMapErrorFlagsML = LocalizationMapErrorFlagsML(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_LOCALIZATION_CHANGED_ML,
    ) -> None:
        if map is None:
            map = LocalizationMapML()
        super().__init__(
            session=session,
            state=LocalizationMapStateML(state).value,
            map=map,
            confidence=LocalizationMapConfidenceML(confidence).value,
            error_flags=LocalizationMapErrorFlagsML(error_flags).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataLocalizationChangedML(session={repr(self.session)}, state={repr(self.state)}, map={repr(self.map)}, confidence={repr(self.confidence)}, error_flags={repr(self.error_flags)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataLocalizationChangedML(session={self.session}, state={self.state}, map={self.map}, confidence={self.confidence}, error_flags={self.error_flags}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("session", Session),
        ("state", LocalizationMapStateML.ctype()),
        ("map", LocalizationMapML),
        ("confidence", LocalizationMapConfidenceML.ctype()),
        ("error_flags", LocalizationMapErrorFlagsMLCInt),
    ]


class LocalizationMapQueryInfoBaseHeaderML(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.LocalizationMapQueryInfoBaseHeaderML(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.LocalizationMapQueryInfoBaseHeaderML(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class MapLocalizationRequestInfoML(Structure):
    def __init__(
        self,
        map_uuid: UuidEXT = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.MAP_LOCALIZATION_REQUEST_INFO_ML,
    ) -> None:
        super().__init__(
            map_uuid=map_uuid,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.MapLocalizationRequestInfoML(map_uuid={repr(self.map_uuid)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.MapLocalizationRequestInfoML(map_uuid={self.map_uuid}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("map_uuid", UuidEXT),
    ]


class LocalizationMapImportInfoML(Structure):
    def __init__(
        self,
        size: int = 0,
        data: str = "",
        next: c_void_p = None,
        type: StructureType = StructureType.LOCALIZATION_MAP_IMPORT_INFO_ML,
    ) -> None:
        super().__init__(
            size=size,
            _data=data.encode(),
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.LocalizationMapImportInfoML(size={repr(self.size)}, data={repr(self._data)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.LocalizationMapImportInfoML(size={self.size}, data={self._data}, next={self.next}, type={self.type})"

    @property
    def data(self) -> str:
        return self._data.decode()
    
    @data.setter
    def data(self, value: str) -> None:
        # noinspection PyAttributeOutsideInit
        self._data = value.encode()

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("size", c_uint32),
        ("_data", c_char_p),
    ]


class LocalizationEnableEventsInfoML(Structure):
    def __init__(
        self,
        enabled: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.LOCALIZATION_ENABLE_EVENTS_INFO_ML,
    ) -> None:
        super().__init__(
            enabled=enabled,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.LocalizationEnableEventsInfoML(enabled={repr(self.enabled)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.LocalizationEnableEventsInfoML(enabled={self.enabled}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("enabled", Bool32),
    ]


PFN_xrEnableLocalizationEventsML = CFUNCTYPE(Result.ctype(), Session, POINTER(LocalizationEnableEventsInfoML))

PFN_xrQueryLocalizationMapsML = CFUNCTYPE(Result.ctype(), Session, POINTER(LocalizationMapQueryInfoBaseHeaderML), c_uint32, POINTER(c_uint32), POINTER(LocalizationMapML))

PFN_xrRequestMapLocalizationML = CFUNCTYPE(Result.ctype(), Session, POINTER(MapLocalizationRequestInfoML))

PFN_xrImportLocalizationMapML = CFUNCTYPE(Result.ctype(), Session, POINTER(LocalizationMapImportInfoML), POINTER(UuidEXT))

PFN_xrCreateExportedLocalizationMapML = CFUNCTYPE(Result.ctype(), Session, POINTER(Uuid), POINTER(ExportedLocalizationMapML))

PFN_xrDestroyExportedLocalizationMapML = CFUNCTYPE(Result.ctype(), ExportedLocalizationMapML)

PFN_xrGetExportedLocalizationMapDataML = CFUNCTYPE(Result.ctype(), ExportedLocalizationMapML, c_uint32, POINTER(c_uint32), c_char_p)


class FutureEXT_T(Structure):
    pass


FutureEXT = POINTER(FutureEXT_T)


class SpatialAnchorsCreateInfoBaseHeaderML(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorsCreateInfoBaseHeaderML(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorsCreateInfoBaseHeaderML(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SpatialAnchorsCreateInfoFromPoseML(Structure):
    def __init__(
        self,
        base_space: Space = None,
        pose_in_base_space: Posef = Posef(),
        time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHORS_CREATE_INFO_FROM_POSE_ML,
    ) -> None:
        super().__init__(
            base_space=base_space,
            pose_in_base_space=pose_in_base_space,
            time=time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorsCreateInfoFromPoseML(base_space={repr(self.base_space)}, pose_in_base_space={repr(self.pose_in_base_space)}, time={repr(self.time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorsCreateInfoFromPoseML(base_space={self.base_space}, pose_in_base_space={self.pose_in_base_space}, time={self.time}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("base_space", Space),
        ("pose_in_base_space", Posef),
        ("time", Time),
    ]


class CreateSpatialAnchorsCompletionML(Structure):
    def __init__(
        self,
        future_result: Result = Result(),  # noqa
        space_count: Optional[int] = None,
        spaces: ArrayFieldParamType[Space] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.CREATE_SPATIAL_ANCHORS_COMPLETION_ML,
    ) -> None:
        space_count, spaces = array_field_helper(
            Space, space_count, spaces)
        super().__init__(
            future_result=Result(future_result).value,
            space_count=space_count,
            _spaces=spaces,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CreateSpatialAnchorsCompletionML(future_result={repr(self.future_result)}, space_count={repr(self.space_count)}, spaces={repr(self._spaces)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CreateSpatialAnchorsCompletionML(future_result={self.future_result}, space_count={self.space_count}, spaces={self._spaces}, next={self.next}, type={self.type})"

    @property
    def spaces(self):
        if self.space_count == 0:
            return (Space * 0)()
        else:
            return (Space * self.space_count).from_address(
                ctypes.addressof(self._spaces.contents))

    @spaces.setter
    def spaces(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.space_count, self._spaces = array_field_helper(
            Space, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("future_result", Result.ctype()),
        ("space_count", c_uint32),
        ("_spaces", POINTER(Space)),
    ]


class SpatialAnchorStateML(Structure):
    def __init__(
        self,
        confidence: SpatialAnchorConfidenceML = SpatialAnchorConfidenceML(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHOR_STATE_ML,
    ) -> None:
        super().__init__(
            confidence=SpatialAnchorConfidenceML(confidence).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorStateML(confidence={repr(self.confidence)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorStateML(confidence={self.confidence}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("confidence", SpatialAnchorConfidenceML.ctype()),
    ]


PFN_xrCreateSpatialAnchorsAsyncML = CFUNCTYPE(Result.ctype(), Session, POINTER(SpatialAnchorsCreateInfoBaseHeaderML), POINTER(FutureEXT))

PFN_xrCreateSpatialAnchorsCompleteML = CFUNCTYPE(Result.ctype(), Session, FutureEXT, POINTER(CreateSpatialAnchorsCompletionML))

PFN_xrGetSpatialAnchorStateML = CFUNCTYPE(Result.ctype(), Space, POINTER(SpatialAnchorStateML))


class SpatialAnchorsStorageML_T(Structure):
    pass


class SpatialAnchorsStorageML(POINTER(SpatialAnchorsStorageML_T), HandleMixin):
    _type_ = SpatialAnchorsStorageML_T  # ctypes idiosyncrasy


class SpatialAnchorsCreateStorageInfoML(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHORS_CREATE_STORAGE_INFO_ML,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorsCreateStorageInfoML(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorsCreateStorageInfoML(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SpatialAnchorsQueryInfoBaseHeaderML(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorsQueryInfoBaseHeaderML(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorsQueryInfoBaseHeaderML(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SpatialAnchorsQueryInfoRadiusML(Structure):
    def __init__(
        self,
        base_space: Space = None,
        center: Vector3f = None,
        time: Time = 0,
        radius: float = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHORS_QUERY_INFO_RADIUS_ML,
    ) -> None:
        if center is None:
            center = Vector3f()
        super().__init__(
            base_space=base_space,
            center=center,
            time=time,
            radius=radius,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorsQueryInfoRadiusML(base_space={repr(self.base_space)}, center={repr(self.center)}, time={repr(self.time)}, radius={repr(self.radius)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorsQueryInfoRadiusML(base_space={self.base_space}, center={self.center}, time={self.time}, radius={self.radius:.3f}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("base_space", Space),
        ("center", Vector3f),
        ("time", Time),
        ("radius", c_float),
    ]


class SpatialAnchorsQueryCompletionML(Structure):
    def __init__(
        self,
        future_result: Result = Result(),  # noqa
        uuid_capacity_input: int = 0,
        uuid_count_output: int = 0,
        uuids: POINTER(UuidEXT) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHORS_QUERY_COMPLETION_ML,
    ) -> None:
        super().__init__(
            future_result=Result(future_result).value,
            uuid_capacity_input=uuid_capacity_input,
            uuid_count_output=uuid_count_output,
            uuids=uuids,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorsQueryCompletionML(future_result={repr(self.future_result)}, uuid_capacity_input={repr(self.uuid_capacity_input)}, uuid_count_output={repr(self.uuid_count_output)}, uuids={repr(self.uuids)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorsQueryCompletionML(future_result={self.future_result}, uuid_capacity_input={self.uuid_capacity_input}, uuid_count_output={self.uuid_count_output}, uuids={self.uuids}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("future_result", Result.ctype()),
        ("uuid_capacity_input", c_uint32),
        ("uuid_count_output", c_uint32),
        ("uuids", POINTER(UuidEXT)),
    ]


class SpatialAnchorsCreateInfoFromUuidsML(Structure):
    def __init__(
        self,
        storage: SpatialAnchorsStorageML = None,
        uuid_count: Optional[int] = None,
        uuids: ArrayFieldParamType[Uuid] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHORS_CREATE_INFO_FROM_UUIDS_ML,
    ) -> None:
        uuid_count, uuids = array_field_helper(
            Uuid, uuid_count, uuids)
        super().__init__(
            storage=storage,
            uuid_count=uuid_count,
            _uuids=uuids,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorsCreateInfoFromUuidsML(storage={repr(self.storage)}, uuid_count={repr(self.uuid_count)}, uuids={repr(self._uuids)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorsCreateInfoFromUuidsML(storage={self.storage}, uuid_count={self.uuid_count}, uuids={self._uuids}, next={self.next}, type={self.type})"

    @property
    def uuids(self):
        if self.uuid_count == 0:
            return (Uuid * 0)()
        else:
            return (Uuid * self.uuid_count).from_address(
                ctypes.addressof(self._uuids.contents))

    @uuids.setter
    def uuids(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.uuid_count, self._uuids = array_field_helper(
            Uuid, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("storage", SpatialAnchorsStorageML),
        ("uuid_count", c_uint32),
        ("_uuids", POINTER(Uuid)),
    ]


class SpatialAnchorsPublishInfoML(Structure):
    def __init__(
        self,
        anchor_count: Optional[int] = None,
        anchors: ArrayFieldParamType[Space] = None,
        expiration: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHORS_PUBLISH_INFO_ML,
    ) -> None:
        anchor_count, anchors = array_field_helper(
            Space, anchor_count, anchors)
        super().__init__(
            anchor_count=anchor_count,
            _anchors=anchors,
            expiration=expiration,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorsPublishInfoML(anchor_count={repr(self.anchor_count)}, anchors={repr(self._anchors)}, expiration={repr(self.expiration)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorsPublishInfoML(anchor_count={self.anchor_count}, anchors={self._anchors}, expiration={self.expiration}, next={self.next}, type={self.type})"

    @property
    def anchors(self):
        if self.anchor_count == 0:
            return (Space * 0)()
        else:
            return (Space * self.anchor_count).from_address(
                ctypes.addressof(self._anchors.contents))

    @anchors.setter
    def anchors(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.anchor_count, self._anchors = array_field_helper(
            Space, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("anchor_count", c_uint32),
        ("_anchors", POINTER(Space)),
        ("expiration", c_uint64),
    ]


class SpatialAnchorsPublishCompletionML(Structure):
    def __init__(
        self,
        future_result: Result = Result(),  # noqa
        uuid_count: Optional[int] = None,
        uuids: ArrayFieldParamType[UuidEXT] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHORS_PUBLISH_COMPLETION_ML,
    ) -> None:
        uuid_count, uuids = array_field_helper(
            UuidEXT, uuid_count, uuids)
        super().__init__(
            future_result=Result(future_result).value,
            uuid_count=uuid_count,
            _uuids=uuids,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorsPublishCompletionML(future_result={repr(self.future_result)}, uuid_count={repr(self.uuid_count)}, uuids={repr(self._uuids)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorsPublishCompletionML(future_result={self.future_result}, uuid_count={self.uuid_count}, uuids={self._uuids}, next={self.next}, type={self.type})"

    @property
    def uuids(self):
        if self.uuid_count == 0:
            return (UuidEXT * 0)()
        else:
            return (UuidEXT * self.uuid_count).from_address(
                ctypes.addressof(self._uuids.contents))

    @uuids.setter
    def uuids(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.uuid_count, self._uuids = array_field_helper(
            UuidEXT, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("future_result", Result.ctype()),
        ("uuid_count", c_uint32),
        ("_uuids", POINTER(UuidEXT)),
    ]


class SpatialAnchorsDeleteInfoML(Structure):
    def __init__(
        self,
        uuid_count: Optional[int] = None,
        uuids: ArrayFieldParamType[Uuid] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHORS_DELETE_INFO_ML,
    ) -> None:
        uuid_count, uuids = array_field_helper(
            Uuid, uuid_count, uuids)
        super().__init__(
            uuid_count=uuid_count,
            _uuids=uuids,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorsDeleteInfoML(uuid_count={repr(self.uuid_count)}, uuids={repr(self._uuids)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorsDeleteInfoML(uuid_count={self.uuid_count}, uuids={self._uuids}, next={self.next}, type={self.type})"

    @property
    def uuids(self):
        if self.uuid_count == 0:
            return (Uuid * 0)()
        else:
            return (Uuid * self.uuid_count).from_address(
                ctypes.addressof(self._uuids.contents))

    @uuids.setter
    def uuids(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.uuid_count, self._uuids = array_field_helper(
            Uuid, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("uuid_count", c_uint32),
        ("_uuids", POINTER(Uuid)),
    ]


class SpatialAnchorsDeleteCompletionML(Structure):
    def __init__(
        self,
        future_result: Result = Result(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHORS_DELETE_COMPLETION_ML,
    ) -> None:
        super().__init__(
            future_result=Result(future_result).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorsDeleteCompletionML(future_result={repr(self.future_result)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorsDeleteCompletionML(future_result={self.future_result}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("future_result", Result.ctype()),
    ]


class SpatialAnchorsUpdateExpirationInfoML(Structure):
    def __init__(
        self,
        uuid_count: Optional[int] = None,
        uuids: ArrayFieldParamType[Uuid] = None,
        expiration: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHORS_UPDATE_EXPIRATION_INFO_ML,
    ) -> None:
        uuid_count, uuids = array_field_helper(
            Uuid, uuid_count, uuids)
        super().__init__(
            uuid_count=uuid_count,
            _uuids=uuids,
            expiration=expiration,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorsUpdateExpirationInfoML(uuid_count={repr(self.uuid_count)}, uuids={repr(self._uuids)}, expiration={repr(self.expiration)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorsUpdateExpirationInfoML(uuid_count={self.uuid_count}, uuids={self._uuids}, expiration={self.expiration}, next={self.next}, type={self.type})"

    @property
    def uuids(self):
        if self.uuid_count == 0:
            return (Uuid * 0)()
        else:
            return (Uuid * self.uuid_count).from_address(
                ctypes.addressof(self._uuids.contents))

    @uuids.setter
    def uuids(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.uuid_count, self._uuids = array_field_helper(
            Uuid, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("uuid_count", c_uint32),
        ("_uuids", POINTER(Uuid)),
        ("expiration", c_uint64),
    ]


class SpatialAnchorsUpdateExpirationCompletionML(Structure):
    def __init__(
        self,
        future_result: Result = Result(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHORS_UPDATE_EXPIRATION_COMPLETION_ML,
    ) -> None:
        super().__init__(
            future_result=Result(future_result).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorsUpdateExpirationCompletionML(future_result={repr(self.future_result)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorsUpdateExpirationCompletionML(future_result={self.future_result}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("future_result", Result.ctype()),
    ]


class SpatialAnchorCompletionResultML(Structure):
    def __init__(
        self,
        uuid: UuidEXT = 0,
        result: Result = Result(),  # noqa
    ) -> None:
        super().__init__(
            uuid=uuid,
            result=Result(result).value,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorCompletionResultML(uuid={repr(self.uuid)}, result={repr(self.result)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorCompletionResultML(uuid={self.uuid}, result={self.result})"

    _fields_ = [
        ("uuid", UuidEXT),
        ("result", Result.ctype()),
    ]


class SpatialAnchorsPublishCompletionDetailsML(Structure):
    def __init__(
        self,
        result_count: Optional[int] = None,
        results: ArrayFieldParamType[SpatialAnchorCompletionResultML] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHORS_PUBLISH_COMPLETION_DETAILS_ML,
    ) -> None:
        result_count, results = array_field_helper(
            SpatialAnchorCompletionResultML, result_count, results)
        super().__init__(
            result_count=result_count,
            _results=results,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorsPublishCompletionDetailsML(result_count={repr(self.result_count)}, results={repr(self._results)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorsPublishCompletionDetailsML(result_count={self.result_count}, results={self._results}, next={self.next}, type={self.type})"

    @property
    def results(self):
        if self.result_count == 0:
            return (SpatialAnchorCompletionResultML * 0)()
        else:
            return (SpatialAnchorCompletionResultML * self.result_count).from_address(
                ctypes.addressof(self._results.contents))

    @results.setter
    def results(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.result_count, self._results = array_field_helper(
            SpatialAnchorCompletionResultML, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("result_count", c_uint32),
        ("_results", POINTER(SpatialAnchorCompletionResultML)),
    ]


class SpatialAnchorsDeleteCompletionDetailsML(Structure):
    def __init__(
        self,
        result_count: Optional[int] = None,
        results: ArrayFieldParamType[SpatialAnchorCompletionResultML] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHORS_DELETE_COMPLETION_DETAILS_ML,
    ) -> None:
        result_count, results = array_field_helper(
            SpatialAnchorCompletionResultML, result_count, results)
        super().__init__(
            result_count=result_count,
            _results=results,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorsDeleteCompletionDetailsML(result_count={repr(self.result_count)}, results={repr(self._results)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorsDeleteCompletionDetailsML(result_count={self.result_count}, results={self._results}, next={self.next}, type={self.type})"

    @property
    def results(self):
        if self.result_count == 0:
            return (SpatialAnchorCompletionResultML * 0)()
        else:
            return (SpatialAnchorCompletionResultML * self.result_count).from_address(
                ctypes.addressof(self._results.contents))

    @results.setter
    def results(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.result_count, self._results = array_field_helper(
            SpatialAnchorCompletionResultML, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("result_count", c_uint32),
        ("_results", POINTER(SpatialAnchorCompletionResultML)),
    ]


class SpatialAnchorsUpdateExpirationCompletionDetailsML(Structure):
    def __init__(
        self,
        result_count: Optional[int] = None,
        results: ArrayFieldParamType[SpatialAnchorCompletionResultML] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHORS_UPDATE_EXPIRATION_COMPLETION_DETAILS_ML,
    ) -> None:
        result_count, results = array_field_helper(
            SpatialAnchorCompletionResultML, result_count, results)
        super().__init__(
            result_count=result_count,
            _results=results,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorsUpdateExpirationCompletionDetailsML(result_count={repr(self.result_count)}, results={repr(self._results)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorsUpdateExpirationCompletionDetailsML(result_count={self.result_count}, results={self._results}, next={self.next}, type={self.type})"

    @property
    def results(self):
        if self.result_count == 0:
            return (SpatialAnchorCompletionResultML * 0)()
        else:
            return (SpatialAnchorCompletionResultML * self.result_count).from_address(
                ctypes.addressof(self._results.contents))

    @results.setter
    def results(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.result_count, self._results = array_field_helper(
            SpatialAnchorCompletionResultML, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("result_count", c_uint32),
        ("_results", POINTER(SpatialAnchorCompletionResultML)),
    ]


PFN_xrCreateSpatialAnchorsStorageML = CFUNCTYPE(Result.ctype(), Session, POINTER(SpatialAnchorsCreateStorageInfoML), POINTER(SpatialAnchorsStorageML))

PFN_xrDestroySpatialAnchorsStorageML = CFUNCTYPE(Result.ctype(), SpatialAnchorsStorageML)

PFN_xrQuerySpatialAnchorsAsyncML = CFUNCTYPE(Result.ctype(), SpatialAnchorsStorageML, POINTER(SpatialAnchorsQueryInfoBaseHeaderML), POINTER(FutureEXT))

PFN_xrQuerySpatialAnchorsCompleteML = CFUNCTYPE(Result.ctype(), SpatialAnchorsStorageML, FutureEXT, POINTER(SpatialAnchorsQueryCompletionML))

PFN_xrPublishSpatialAnchorsAsyncML = CFUNCTYPE(Result.ctype(), SpatialAnchorsStorageML, POINTER(SpatialAnchorsPublishInfoML), POINTER(FutureEXT))

PFN_xrPublishSpatialAnchorsCompleteML = CFUNCTYPE(Result.ctype(), SpatialAnchorsStorageML, FutureEXT, POINTER(SpatialAnchorsPublishCompletionML))

PFN_xrDeleteSpatialAnchorsAsyncML = CFUNCTYPE(Result.ctype(), SpatialAnchorsStorageML, POINTER(SpatialAnchorsDeleteInfoML), POINTER(FutureEXT))

PFN_xrDeleteSpatialAnchorsCompleteML = CFUNCTYPE(Result.ctype(), SpatialAnchorsStorageML, FutureEXT, POINTER(SpatialAnchorsDeleteCompletionML))

PFN_xrUpdateSpatialAnchorsExpirationAsyncML = CFUNCTYPE(Result.ctype(), SpatialAnchorsStorageML, POINTER(SpatialAnchorsUpdateExpirationInfoML), POINTER(FutureEXT))

PFN_xrUpdateSpatialAnchorsExpirationCompleteML = CFUNCTYPE(Result.ctype(), SpatialAnchorsStorageML, FutureEXT, POINTER(SpatialAnchorsUpdateExpirationCompletionML))


class SpatialAnchorStoreConnectionMSFT_T(Structure):
    pass


class SpatialAnchorStoreConnectionMSFT(POINTER(SpatialAnchorStoreConnectionMSFT_T), HandleMixin):
    _type_ = SpatialAnchorStoreConnectionMSFT_T  # ctypes idiosyncrasy


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
        spatial_anchor: SpatialAnchorMSFT = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHOR_PERSISTENCE_INFO_MSFT,
    ) -> None:
        if spatial_anchor_persistence_name is None:
            spatial_anchor_persistence_name = SpatialAnchorPersistenceNameMSFT()
        super().__init__(
            spatial_anchor_persistence_name=spatial_anchor_persistence_name,
            spatial_anchor=spatial_anchor,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorPersistenceInfoMSFT(spatial_anchor_persistence_name={repr(self.spatial_anchor_persistence_name)}, spatial_anchor={repr(self.spatial_anchor)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorPersistenceInfoMSFT(spatial_anchor_persistence_name={self.spatial_anchor_persistence_name}, spatial_anchor={self.spatial_anchor}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("spatial_anchor_persistence_name", SpatialAnchorPersistenceNameMSFT),
        ("spatial_anchor", SpatialAnchorMSFT),
    ]


class SpatialAnchorFromPersistedAnchorCreateInfoMSFT(Structure):
    def __init__(
        self,
        spatial_anchor_store: SpatialAnchorStoreConnectionMSFT = None,
        spatial_anchor_persistence_name: SpatialAnchorPersistenceNameMSFT = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHOR_FROM_PERSISTED_ANCHOR_CREATE_INFO_MSFT,
    ) -> None:
        if spatial_anchor_persistence_name is None:
            spatial_anchor_persistence_name = SpatialAnchorPersistenceNameMSFT()
        super().__init__(
            spatial_anchor_store=spatial_anchor_store,
            spatial_anchor_persistence_name=spatial_anchor_persistence_name,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorFromPersistedAnchorCreateInfoMSFT(spatial_anchor_store={repr(self.spatial_anchor_store)}, spatial_anchor_persistence_name={repr(self.spatial_anchor_persistence_name)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorFromPersistedAnchorCreateInfoMSFT(spatial_anchor_store={self.spatial_anchor_store}, spatial_anchor_persistence_name={self.spatial_anchor_persistence_name}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("spatial_anchor_store", SpatialAnchorStoreConnectionMSFT),
        ("spatial_anchor_persistence_name", SpatialAnchorPersistenceNameMSFT),
    ]


PFN_xrCreateSpatialAnchorStoreConnectionMSFT = CFUNCTYPE(Result.ctype(), Session, POINTER(SpatialAnchorStoreConnectionMSFT))

PFN_xrDestroySpatialAnchorStoreConnectionMSFT = CFUNCTYPE(Result.ctype(), SpatialAnchorStoreConnectionMSFT)

PFN_xrPersistSpatialAnchorMSFT = CFUNCTYPE(Result.ctype(), SpatialAnchorStoreConnectionMSFT, POINTER(SpatialAnchorPersistenceInfoMSFT))

PFN_xrEnumeratePersistedSpatialAnchorNamesMSFT = CFUNCTYPE(Result.ctype(), SpatialAnchorStoreConnectionMSFT, c_uint32, POINTER(c_uint32), POINTER(SpatialAnchorPersistenceNameMSFT))

PFN_xrCreateSpatialAnchorFromPersistedNameMSFT = CFUNCTYPE(Result.ctype(), Session, POINTER(SpatialAnchorFromPersistedAnchorCreateInfoMSFT), POINTER(SpatialAnchorMSFT))

PFN_xrUnpersistSpatialAnchorMSFT = CFUNCTYPE(Result.ctype(), SpatialAnchorStoreConnectionMSFT, POINTER(SpatialAnchorPersistenceNameMSFT))

PFN_xrClearSpatialAnchorStoreMSFT = CFUNCTYPE(Result.ctype(), SpatialAnchorStoreConnectionMSFT)


class SceneMarkerMSFT(Structure):
    def __init__(
        self,
        marker_type: SceneMarkerTypeMSFT = SceneMarkerTypeMSFT(),  # noqa
        last_seen_time: Time = 0,
        center: Offset2Df = None,
        size: Extent2Df = None,
    ) -> None:
        if center is None:
            center = Offset2Df()
        if size is None:
            size = Extent2Df()
        super().__init__(
            marker_type=SceneMarkerTypeMSFT(marker_type).value,
            last_seen_time=last_seen_time,
            center=center,
            size=size,
        )

    def __repr__(self) -> str:
        return f"xr.SceneMarkerMSFT(marker_type={repr(self.marker_type)}, last_seen_time={repr(self.last_seen_time)}, center={repr(self.center)}, size={repr(self.size)})"

    def __str__(self) -> str:
        return f"xr.SceneMarkerMSFT(marker_type={self.marker_type}, last_seen_time={self.last_seen_time}, center={self.center}, size={self.size})"

    _fields_ = [
        ("marker_type", SceneMarkerTypeMSFT.ctype()),
        ("last_seen_time", Time),
        ("center", Offset2Df),
        ("size", Extent2Df),
    ]


class SceneMarkersMSFT(Structure):
    def __init__(
        self,
        scene_marker_capacity_input: int = 0,
        scene_markers: POINTER(SceneMarkerMSFT) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SCENE_MARKERS_MSFT,
    ) -> None:
        super().__init__(
            scene_marker_capacity_input=scene_marker_capacity_input,
            scene_markers=scene_markers,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SceneMarkersMSFT(scene_marker_capacity_input={repr(self.scene_marker_capacity_input)}, scene_markers={repr(self.scene_markers)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SceneMarkersMSFT(scene_marker_capacity_input={self.scene_marker_capacity_input}, scene_markers={self.scene_markers}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("scene_marker_capacity_input", c_uint32),
        ("scene_markers", POINTER(SceneMarkerMSFT)),
    ]


class SceneMarkerTypeFilterMSFT(Structure):
    def __init__(
        self,
        marker_type_count: Optional[int] = None,
        marker_types: ArrayFieldParamType[SceneMarkerTypeMSFT.ctype()] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SCENE_MARKER_TYPE_FILTER_MSFT,
    ) -> None:
        marker_type_count, marker_types = array_field_helper(
            SceneMarkerTypeMSFT.ctype(), marker_type_count, marker_types)
        super().__init__(
            marker_type_count=marker_type_count,
            _marker_types=marker_types,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SceneMarkerTypeFilterMSFT(marker_type_count={repr(self.marker_type_count)}, marker_types={repr(self._marker_types)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SceneMarkerTypeFilterMSFT(marker_type_count={self.marker_type_count}, marker_types={self._marker_types}, next={self.next}, type={self.type})"

    @property
    def marker_types(self):
        if self.marker_type_count == 0:
            return (SceneMarkerTypeMSFT.ctype() * 0)()
        else:
            return (SceneMarkerTypeMSFT.ctype() * self.marker_type_count).from_address(
                ctypes.addressof(self._marker_types.contents))

    @marker_types.setter
    def marker_types(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.marker_type_count, self._marker_types = array_field_helper(
            SceneMarkerTypeMSFT.ctype(), None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("marker_type_count", c_uint32),
        ("_marker_types", POINTER(SceneMarkerTypeMSFT.ctype())),
    ]


class SceneMarkerQRCodeMSFT(Structure):
    def __init__(
        self,
        symbol_type: SceneMarkerQRCodeSymbolTypeMSFT = SceneMarkerQRCodeSymbolTypeMSFT(),  # noqa
        version: int = 0,
    ) -> None:
        super().__init__(
            symbol_type=SceneMarkerQRCodeSymbolTypeMSFT(symbol_type).value,
            version=version,
        )

    def __repr__(self) -> str:
        return f"xr.SceneMarkerQRCodeMSFT(symbol_type={repr(self.symbol_type)}, version={repr(self.version)})"

    def __str__(self) -> str:
        return f"xr.SceneMarkerQRCodeMSFT(symbol_type={self.symbol_type}, version={self.version})"

    _fields_ = [
        ("symbol_type", SceneMarkerQRCodeSymbolTypeMSFT.ctype()),
        ("version", c_uint8),
    ]


class SceneMarkerQRCodesMSFT(Structure):
    def __init__(
        self,
        qr_code_capacity_input: int = 0,
        qr_codes: POINTER(SceneMarkerQRCodeMSFT) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SCENE_MARKER_QR_CODES_MSFT,
    ) -> None:
        super().__init__(
            qr_code_capacity_input=qr_code_capacity_input,
            qr_codes=qr_codes,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SceneMarkerQRCodesMSFT(qr_code_capacity_input={repr(self.qr_code_capacity_input)}, qr_codes={repr(self.qr_codes)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SceneMarkerQRCodesMSFT(qr_code_capacity_input={self.qr_code_capacity_input}, qr_codes={self.qr_codes}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("qr_code_capacity_input", c_uint32),
        ("qr_codes", POINTER(SceneMarkerQRCodeMSFT)),
    ]


PFN_xrGetSceneMarkerRawDataMSFT = CFUNCTYPE(Result.ctype(), SceneMSFT, POINTER(UuidMSFT), c_uint32, POINTER(c_uint32), POINTER(c_uint8))

PFN_xrGetSceneMarkerDecodedStringMSFT = CFUNCTYPE(Result.ctype(), SceneMSFT, POINTER(UuidMSFT), c_uint32, POINTER(c_uint32), c_char_p)


class SpaceQueryInfoBaseHeaderFB(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceQueryInfoBaseHeaderFB(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpaceQueryInfoBaseHeaderFB(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SpaceFilterInfoBaseHeaderFB(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceFilterInfoBaseHeaderFB(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpaceFilterInfoBaseHeaderFB(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SpaceQueryInfoFB(Structure):
    def __init__(
        self,
        query_action: SpaceQueryActionFB = SpaceQueryActionFB(),  # noqa
        max_result_count: int = 0,
        timeout: Duration = 0,
        filter: POINTER(SpaceFilterInfoBaseHeaderFB) = None,
        exclude_filter: POINTER(SpaceFilterInfoBaseHeaderFB) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPACE_QUERY_INFO_FB,
    ) -> None:
        super().__init__(
            query_action=SpaceQueryActionFB(query_action).value,
            max_result_count=max_result_count,
            timeout=timeout,
            filter=filter,
            exclude_filter=exclude_filter,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceQueryInfoFB(query_action={repr(self.query_action)}, max_result_count={repr(self.max_result_count)}, timeout={repr(self.timeout)}, filter={repr(self.filter)}, exclude_filter={repr(self.exclude_filter)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpaceQueryInfoFB(query_action={self.query_action}, max_result_count={self.max_result_count}, timeout={self.timeout}, filter={self.filter}, exclude_filter={self.exclude_filter}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("query_action", SpaceQueryActionFB.ctype()),
        ("max_result_count", c_uint32),
        ("timeout", Duration),
        ("filter", POINTER(SpaceFilterInfoBaseHeaderFB)),
        ("exclude_filter", POINTER(SpaceFilterInfoBaseHeaderFB)),
    ]


class SpaceStorageLocationFilterInfoFB(Structure):
    def __init__(
        self,
        location: SpaceStorageLocationFB = SpaceStorageLocationFB(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.SPACE_STORAGE_LOCATION_FILTER_INFO_FB,
    ) -> None:
        super().__init__(
            location=SpaceStorageLocationFB(location).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceStorageLocationFilterInfoFB(location={repr(self.location)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpaceStorageLocationFilterInfoFB(location={self.location}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("location", SpaceStorageLocationFB.ctype()),
    ]


class SpaceUuidFilterInfoFB(Structure):
    def __init__(
        self,
        uuid_count: Optional[int] = None,
        uuids: ArrayFieldParamType[UuidEXT] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPACE_UUID_FILTER_INFO_FB,
    ) -> None:
        uuid_count, uuids = array_field_helper(
            UuidEXT, uuid_count, uuids)
        super().__init__(
            uuid_count=uuid_count,
            _uuids=uuids,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceUuidFilterInfoFB(uuid_count={repr(self.uuid_count)}, uuids={repr(self._uuids)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpaceUuidFilterInfoFB(uuid_count={self.uuid_count}, uuids={self._uuids}, next={self.next}, type={self.type})"

    @property
    def uuids(self):
        if self.uuid_count == 0:
            return (UuidEXT * 0)()
        else:
            return (UuidEXT * self.uuid_count).from_address(
                ctypes.addressof(self._uuids.contents))

    @uuids.setter
    def uuids(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.uuid_count, self._uuids = array_field_helper(
            UuidEXT, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("uuid_count", c_uint32),
        ("_uuids", POINTER(UuidEXT)),
    ]


class SpaceComponentFilterInfoFB(Structure):
    def __init__(
        self,
        component_type: SpaceComponentTypeFB = SpaceComponentTypeFB(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.SPACE_COMPONENT_FILTER_INFO_FB,
    ) -> None:
        super().__init__(
            component_type=SpaceComponentTypeFB(component_type).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceComponentFilterInfoFB(component_type={repr(self.component_type)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpaceComponentFilterInfoFB(component_type={self.component_type}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("component_type", SpaceComponentTypeFB.ctype()),
    ]


class SpaceQueryResultFB(Structure):
    def __init__(
        self,
        space: Space = None,
        uuid: UuidEXT = 0,
    ) -> None:
        super().__init__(
            space=space,
            uuid=uuid,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceQueryResultFB(space={repr(self.space)}, uuid={repr(self.uuid)})"

    def __str__(self) -> str:
        return f"xr.SpaceQueryResultFB(space={self.space}, uuid={self.uuid})"

    _fields_ = [
        ("space", Space),
        ("uuid", UuidEXT),
    ]


class SpaceQueryResultsFB(Structure):
    def __init__(
        self,
        result_capacity_input: int = 0,
        result_count_output: int = 0,
        results: POINTER(SpaceQueryResultFB) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPACE_QUERY_RESULTS_FB,
    ) -> None:
        super().__init__(
            result_capacity_input=result_capacity_input,
            result_count_output=result_count_output,
            results=results,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceQueryResultsFB(result_capacity_input={repr(self.result_capacity_input)}, result_count_output={repr(self.result_count_output)}, results={repr(self.results)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpaceQueryResultsFB(result_capacity_input={self.result_capacity_input}, result_count_output={self.result_count_output}, results={self.results}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("result_capacity_input", c_uint32),
        ("result_count_output", c_uint32),
        ("results", POINTER(SpaceQueryResultFB)),
    ]


class EventDataSpaceQueryResultsAvailableFB(Structure):
    def __init__(
        self,
        request_id: AsyncRequestIdFB = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_SPACE_QUERY_RESULTS_AVAILABLE_FB,
    ) -> None:
        super().__init__(
            request_id=request_id,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataSpaceQueryResultsAvailableFB(request_id={repr(self.request_id)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataSpaceQueryResultsAvailableFB(request_id={self.request_id}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("request_id", AsyncRequestIdFB),
    ]


class EventDataSpaceQueryCompleteFB(Structure):
    def __init__(
        self,
        request_id: AsyncRequestIdFB = 0,
        result: Result = Result(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_SPACE_QUERY_COMPLETE_FB,
    ) -> None:
        super().__init__(
            request_id=request_id,
            result=Result(result).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataSpaceQueryCompleteFB(request_id={repr(self.request_id)}, result={repr(self.result)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataSpaceQueryCompleteFB(request_id={self.request_id}, result={self.result}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("request_id", AsyncRequestIdFB),
        ("result", Result.ctype()),
    ]


PFN_xrQuerySpacesFB = CFUNCTYPE(Result.ctype(), Session, POINTER(SpaceQueryInfoBaseHeaderFB), POINTER(AsyncRequestIdFB))

PFN_xrRetrieveSpaceQueryResultsFB = CFUNCTYPE(Result.ctype(), Session, AsyncRequestIdFB, POINTER(SpaceQueryResultsFB))


class SpaceSaveInfoFB(Structure):
    def __init__(
        self,
        space: Space = None,
        location: SpaceStorageLocationFB = SpaceStorageLocationFB(),  # noqa
        persistence_mode: SpacePersistenceModeFB = SpacePersistenceModeFB(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.SPACE_SAVE_INFO_FB,
    ) -> None:
        super().__init__(
            space=space,
            location=SpaceStorageLocationFB(location).value,
            persistence_mode=SpacePersistenceModeFB(persistence_mode).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceSaveInfoFB(space={repr(self.space)}, location={repr(self.location)}, persistence_mode={repr(self.persistence_mode)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpaceSaveInfoFB(space={self.space}, location={self.location}, persistence_mode={self.persistence_mode}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("space", Space),
        ("location", SpaceStorageLocationFB.ctype()),
        ("persistence_mode", SpacePersistenceModeFB.ctype()),
    ]


class SpaceEraseInfoFB(Structure):
    def __init__(
        self,
        space: Space = None,
        location: SpaceStorageLocationFB = SpaceStorageLocationFB(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.SPACE_ERASE_INFO_FB,
    ) -> None:
        super().__init__(
            space=space,
            location=SpaceStorageLocationFB(location).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceEraseInfoFB(space={repr(self.space)}, location={repr(self.location)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpaceEraseInfoFB(space={self.space}, location={self.location}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("space", Space),
        ("location", SpaceStorageLocationFB.ctype()),
    ]


class EventDataSpaceSaveCompleteFB(Structure):
    def __init__(
        self,
        request_id: AsyncRequestIdFB = 0,
        result: Result = Result(),  # noqa
        space: Space = None,
        uuid: UuidEXT = 0,
        location: SpaceStorageLocationFB = SpaceStorageLocationFB(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_SPACE_SAVE_COMPLETE_FB,
    ) -> None:
        super().__init__(
            request_id=request_id,
            result=Result(result).value,
            space=space,
            uuid=uuid,
            location=SpaceStorageLocationFB(location).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataSpaceSaveCompleteFB(request_id={repr(self.request_id)}, result={repr(self.result)}, space={repr(self.space)}, uuid={repr(self.uuid)}, location={repr(self.location)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataSpaceSaveCompleteFB(request_id={self.request_id}, result={self.result}, space={self.space}, uuid={self.uuid}, location={self.location}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("request_id", AsyncRequestIdFB),
        ("result", Result.ctype()),
        ("space", Space),
        ("uuid", UuidEXT),
        ("location", SpaceStorageLocationFB.ctype()),
    ]


class EventDataSpaceEraseCompleteFB(Structure):
    def __init__(
        self,
        request_id: AsyncRequestIdFB = 0,
        result: Result = Result(),  # noqa
        space: Space = None,
        uuid: UuidEXT = 0,
        location: SpaceStorageLocationFB = SpaceStorageLocationFB(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_SPACE_ERASE_COMPLETE_FB,
    ) -> None:
        super().__init__(
            request_id=request_id,
            result=Result(result).value,
            space=space,
            uuid=uuid,
            location=SpaceStorageLocationFB(location).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataSpaceEraseCompleteFB(request_id={repr(self.request_id)}, result={repr(self.result)}, space={repr(self.space)}, uuid={repr(self.uuid)}, location={repr(self.location)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataSpaceEraseCompleteFB(request_id={self.request_id}, result={self.result}, space={self.space}, uuid={self.uuid}, location={self.location}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("request_id", AsyncRequestIdFB),
        ("result", Result.ctype()),
        ("space", Space),
        ("uuid", UuidEXT),
        ("location", SpaceStorageLocationFB.ctype()),
    ]


PFN_xrSaveSpaceFB = CFUNCTYPE(Result.ctype(), Session, POINTER(SpaceSaveInfoFB), POINTER(AsyncRequestIdFB))

PFN_xrEraseSpaceFB = CFUNCTYPE(Result.ctype(), Session, POINTER(SpaceEraseInfoFB), POINTER(AsyncRequestIdFB))


class SpaceUserFB_T(Structure):
    pass


class SpaceUserFB(POINTER(SpaceUserFB_T), HandleMixin):
    _type_ = SpaceUserFB_T  # ctypes idiosyncrasy


class SpaceShareInfoFB(Structure):
    def __init__(
        self,
        space_count: Optional[int] = None,
        spaces: ArrayFieldParamType[Space] = None,
        user_count: Optional[int] = None,
        users: ArrayFieldParamType[SpaceUserFB] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPACE_SHARE_INFO_FB,
    ) -> None:
        space_count, spaces = array_field_helper(
            Space, space_count, spaces)
        user_count, users = array_field_helper(
            SpaceUserFB, user_count, users)
        super().__init__(
            space_count=space_count,
            _spaces=spaces,
            user_count=user_count,
            _users=users,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceShareInfoFB(space_count={repr(self.space_count)}, spaces={repr(self._spaces)}, user_count={repr(self.user_count)}, users={repr(self._users)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpaceShareInfoFB(space_count={self.space_count}, spaces={self._spaces}, user_count={self.user_count}, users={self._users}, next={self.next}, type={self.type})"

    @property
    def spaces(self):
        if self.space_count == 0:
            return (Space * 0)()
        else:
            return (Space * self.space_count).from_address(
                ctypes.addressof(self._spaces.contents))

    @spaces.setter
    def spaces(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.space_count, self._spaces = array_field_helper(
            Space, None, value)

    @property
    def users(self):
        if self.user_count == 0:
            return (SpaceUserFB * 0)()
        else:
            return (SpaceUserFB * self.user_count).from_address(
                ctypes.addressof(self._users.contents))

    @users.setter
    def users(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.user_count, self._users = array_field_helper(
            SpaceUserFB, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("space_count", c_uint32),
        ("_spaces", POINTER(Space)),
        ("user_count", c_uint32),
        ("_users", POINTER(SpaceUserFB)),
    ]


class EventDataSpaceShareCompleteFB(Structure):
    def __init__(
        self,
        request_id: AsyncRequestIdFB = 0,
        result: Result = Result(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_SPACE_SHARE_COMPLETE_FB,
    ) -> None:
        super().__init__(
            request_id=request_id,
            result=Result(result).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataSpaceShareCompleteFB(request_id={repr(self.request_id)}, result={repr(self.result)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataSpaceShareCompleteFB(request_id={self.request_id}, result={self.result}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("request_id", AsyncRequestIdFB),
        ("result", Result.ctype()),
    ]


PFN_xrShareSpacesFB = CFUNCTYPE(Result.ctype(), Session, POINTER(SpaceShareInfoFB), POINTER(AsyncRequestIdFB))

CompositionLayerSpaceWarpInfoFlagsFBCInt = Flags64


class CompositionLayerSpaceWarpInfoFB(Structure):
    def __init__(
        self,
        layer_flags: CompositionLayerSpaceWarpInfoFlagsFB = CompositionLayerSpaceWarpInfoFlagsFB(),  # noqa
        motion_vector_sub_image: SwapchainSubImage = None,
        app_space_delta_pose: Posef = Posef(),
        depth_sub_image: SwapchainSubImage = None,
        min_depth: float = 0,
        max_depth: float = 0,
        near_z: float = 0,
        far_z: float = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.COMPOSITION_LAYER_SPACE_WARP_INFO_FB,
    ) -> None:
        if motion_vector_sub_image is None:
            motion_vector_sub_image = SwapchainSubImage()
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
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerSpaceWarpInfoFB(layer_flags={repr(self.layer_flags)}, motion_vector_sub_image={repr(self.motion_vector_sub_image)}, app_space_delta_pose={repr(self.app_space_delta_pose)}, depth_sub_image={repr(self.depth_sub_image)}, min_depth={repr(self.min_depth)}, max_depth={repr(self.max_depth)}, near_z={repr(self.near_z)}, far_z={repr(self.far_z)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerSpaceWarpInfoFB(layer_flags={self.layer_flags}, motion_vector_sub_image={self.motion_vector_sub_image}, app_space_delta_pose={self.app_space_delta_pose}, depth_sub_image={self.depth_sub_image}, min_depth={self.min_depth:.3f}, max_depth={self.max_depth:.3f}, near_z={self.near_z:.3f}, far_z={self.far_z:.3f}, next={self.next}, type={self.type})"

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
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_SPACE_WARP_PROPERTIES_FB,
    ) -> None:
        super().__init__(
            recommended_motion_vector_image_rect_width=recommended_motion_vector_image_rect_width,
            recommended_motion_vector_image_rect_height=recommended_motion_vector_image_rect_height,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemSpaceWarpPropertiesFB(recommended_motion_vector_image_rect_width={repr(self.recommended_motion_vector_image_rect_width)}, recommended_motion_vector_image_rect_height={repr(self.recommended_motion_vector_image_rect_height)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemSpaceWarpPropertiesFB(recommended_motion_vector_image_rect_width={self.recommended_motion_vector_image_rect_width}, recommended_motion_vector_image_rect_height={self.recommended_motion_vector_image_rect_height}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("recommended_motion_vector_image_rect_width", c_uint32),
        ("recommended_motion_vector_image_rect_height", c_uint32),
    ]


class HapticAmplitudeEnvelopeVibrationFB(Structure):
    def __init__(
        self,
        duration: Duration = 0,
        amplitude_count: Optional[int] = None,
        amplitudes: ArrayFieldParamType[c_float] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.HAPTIC_AMPLITUDE_ENVELOPE_VIBRATION_FB,
    ) -> None:
        amplitude_count, amplitudes = array_field_helper(
            c_float, amplitude_count, amplitudes)
        super().__init__(
            duration=duration,
            amplitude_count=amplitude_count,
            _amplitudes=amplitudes,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.HapticAmplitudeEnvelopeVibrationFB(duration={repr(self.duration)}, amplitude_count={repr(self.amplitude_count)}, amplitudes={repr(self._amplitudes)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.HapticAmplitudeEnvelopeVibrationFB(duration={self.duration}, amplitude_count={self.amplitude_count}, amplitudes={self._amplitudes}, next={self.next}, type={self.type})"

    @property
    def amplitudes(self):
        if self.amplitude_count == 0:
            return (c_float * 0)()
        else:
            return (c_float * self.amplitude_count).from_address(
                ctypes.addressof(self._amplitudes.contents))

    @amplitudes.setter
    def amplitudes(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.amplitude_count, self._amplitudes = array_field_helper(
            c_float, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("duration", Duration),
        ("amplitude_count", c_uint32),
        ("_amplitudes", POINTER(c_float)),
    ]


SemanticLabelsSupportFlagsFBCInt = Flags64

Extent3DfFB = Extent3Df


class Offset3DfFB(Structure):
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

    def __setitem__(self, key, value):
        self.as_numpy()[key] = value

    def __len__(self) -> int:
        return 3

    def as_numpy(self):
        if not hasattr(self, "_numpy") or self._numpy is None:
            # Just in time construction
            buffer = (c_float * len(self)).from_address(addressof(self))
            self._numpy = numpy.ctypeslib.as_array(buffer)
        return self._numpy

    def __repr__(self) -> str:
        return f"xr.Offset3DfFB(x={repr(self.x)}, y={repr(self.y)}, z={repr(self.z)})"

    def __str__(self) -> str:
        return f"xr.Offset3DfFB(x={self.x:.3f}, y={self.y:.3f}, z={self.z:.3f})"

    _fields_ = [
        ("x", c_float),
        ("y", c_float),
        ("z", c_float),
    ]


class Rect3DfFB(Structure):
    def __init__(
        self,
        offset: Offset3DfFB = None,
        extent: Extent3DfFB = 0,
    ) -> None:
        if offset is None:
            offset = Offset3DfFB()
        super().__init__(
            offset=offset,
            extent=extent,
        )

    def __repr__(self) -> str:
        return f"xr.Rect3DfFB(offset={repr(self.offset)}, extent={repr(self.extent)})"

    def __str__(self) -> str:
        return f"xr.Rect3DfFB(offset={self.offset}, extent={self.extent})"

    _fields_ = [
        ("offset", Offset3DfFB),
        ("extent", Extent3DfFB),
    ]


class SemanticLabelsFB(Structure):
    def __init__(
        self,
        buffer_capacity_input: int = 0,
        buffer_count_output: int = 0,
        buffer: str = "",
        next: c_void_p = None,
        type: StructureType = StructureType.SEMANTIC_LABELS_FB,
    ) -> None:
        super().__init__(
            buffer_capacity_input=buffer_capacity_input,
            buffer_count_output=buffer_count_output,
            _buffer=buffer.encode(),
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SemanticLabelsFB(buffer_capacity_input={repr(self.buffer_capacity_input)}, buffer_count_output={repr(self.buffer_count_output)}, buffer={repr(self._buffer)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SemanticLabelsFB(buffer_capacity_input={self.buffer_capacity_input}, buffer_count_output={self.buffer_count_output}, buffer={self._buffer}, next={self.next}, type={self.type})"

    @property
    def buffer(self) -> str:
        return self._buffer.decode()
    
    @buffer.setter
    def buffer(self, value: str) -> None:
        # noinspection PyAttributeOutsideInit
        self._buffer = value.encode()

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("buffer_capacity_input", c_uint32),
        ("buffer_count_output", c_uint32),
        ("_buffer", c_char_p),
    ]


class RoomLayoutFB(Structure):
    def __init__(
        self,
        floor_uuid: UuidEXT = 0,
        ceiling_uuid: UuidEXT = 0,
        wall_uuid_capacity_input: int = 0,
        wall_uuid_count_output: int = 0,
        wall_uuids: POINTER(UuidEXT) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.ROOM_LAYOUT_FB,
    ) -> None:
        super().__init__(
            floor_uuid=floor_uuid,
            ceiling_uuid=ceiling_uuid,
            wall_uuid_capacity_input=wall_uuid_capacity_input,
            wall_uuid_count_output=wall_uuid_count_output,
            wall_uuids=wall_uuids,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.RoomLayoutFB(floor_uuid={repr(self.floor_uuid)}, ceiling_uuid={repr(self.ceiling_uuid)}, wall_uuid_capacity_input={repr(self.wall_uuid_capacity_input)}, wall_uuid_count_output={repr(self.wall_uuid_count_output)}, wall_uuids={repr(self.wall_uuids)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.RoomLayoutFB(floor_uuid={self.floor_uuid}, ceiling_uuid={self.ceiling_uuid}, wall_uuid_capacity_input={self.wall_uuid_capacity_input}, wall_uuid_count_output={self.wall_uuid_count_output}, wall_uuids={self.wall_uuids}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("floor_uuid", UuidEXT),
        ("ceiling_uuid", UuidEXT),
        ("wall_uuid_capacity_input", c_uint32),
        ("wall_uuid_count_output", c_uint32),
        ("wall_uuids", POINTER(UuidEXT)),
    ]


class Boundary2DFB(Structure):
    def __init__(
        self,
        vertex_capacity_input: int = 0,
        vertex_count_output: int = 0,
        vertices: POINTER(Vector2f) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.BOUNDARY_2D_FB,
    ) -> None:
        super().__init__(
            vertex_capacity_input=vertex_capacity_input,
            vertex_count_output=vertex_count_output,
            vertices=vertices,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.Boundary2DFB(vertex_capacity_input={repr(self.vertex_capacity_input)}, vertex_count_output={repr(self.vertex_count_output)}, vertices={repr(self.vertices)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.Boundary2DFB(vertex_capacity_input={self.vertex_capacity_input}, vertex_count_output={self.vertex_count_output}, vertices={self.vertices}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("vertex_capacity_input", c_uint32),
        ("vertex_count_output", c_uint32),
        ("vertices", POINTER(Vector2f)),
    ]


class SemanticLabelsSupportInfoFB(Structure):
    def __init__(
        self,
        flags: SemanticLabelsSupportFlagsFB = SemanticLabelsSupportFlagsFB(),  # noqa
        recognized_labels: str = "",
        next: c_void_p = None,
        type: StructureType = StructureType.SEMANTIC_LABELS_SUPPORT_INFO_FB,
    ) -> None:
        super().__init__(
            flags=SemanticLabelsSupportFlagsFB(flags).value,
            _recognized_labels=recognized_labels.encode(),
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SemanticLabelsSupportInfoFB(flags={repr(self.flags)}, recognized_labels={repr(self._recognized_labels)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SemanticLabelsSupportInfoFB(flags={self.flags}, recognized_labels={self._recognized_labels}, next={self.next}, type={self.type})"

    @property
    def recognized_labels(self) -> str:
        return self._recognized_labels.decode()
    
    @recognized_labels.setter
    def recognized_labels(self, value: str) -> None:
        # noinspection PyAttributeOutsideInit
        self._recognized_labels = value.encode()

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", SemanticLabelsSupportFlagsFBCInt),
        ("_recognized_labels", c_char_p),
    ]


PFN_xrGetSpaceBoundingBox2DFB = CFUNCTYPE(Result.ctype(), Session, Space, POINTER(Rect2Df))

PFN_xrGetSpaceBoundingBox3DFB = CFUNCTYPE(Result.ctype(), Session, Space, POINTER(Rect3DfFB))

PFN_xrGetSpaceSemanticLabelsFB = CFUNCTYPE(Result.ctype(), Session, Space, POINTER(SemanticLabelsFB))

PFN_xrGetSpaceBoundary2DFB = CFUNCTYPE(Result.ctype(), Session, Space, POINTER(Boundary2DFB))

PFN_xrGetSpaceRoomLayoutFB = CFUNCTYPE(Result.ctype(), Session, Space, POINTER(RoomLayoutFB))

DigitalLensControlFlagsALMALENCECInt = Flags64


class DigitalLensControlALMALENCE(Structure):
    def __init__(
        self,
        flags: DigitalLensControlFlagsALMALENCE = DigitalLensControlFlagsALMALENCE(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.DIGITAL_LENS_CONTROL_ALMALENCE,
    ) -> None:
        super().__init__(
            flags=DigitalLensControlFlagsALMALENCE(flags).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.DigitalLensControlALMALENCE(flags={repr(self.flags)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.DigitalLensControlALMALENCE(flags={self.flags}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", DigitalLensControlFlagsALMALENCECInt),
    ]


PFN_xrSetDigitalLensControlALMALENCE = CFUNCTYPE(Result.ctype(), Session, POINTER(DigitalLensControlALMALENCE))


class EventDataSceneCaptureCompleteFB(Structure):
    def __init__(
        self,
        request_id: AsyncRequestIdFB = 0,
        result: Result = Result(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_SCENE_CAPTURE_COMPLETE_FB,
    ) -> None:
        super().__init__(
            request_id=request_id,
            result=Result(result).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataSceneCaptureCompleteFB(request_id={repr(self.request_id)}, result={repr(self.result)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataSceneCaptureCompleteFB(request_id={self.request_id}, result={self.result}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("request_id", AsyncRequestIdFB),
        ("result", Result.ctype()),
    ]


class SceneCaptureRequestInfoFB(Structure):
    def __init__(
        self,
        request_byte_count: int = 0,
        request: str = "",
        next: c_void_p = None,
        type: StructureType = StructureType.SCENE_CAPTURE_REQUEST_INFO_FB,
    ) -> None:
        super().__init__(
            request_byte_count=request_byte_count,
            _request=request.encode(),
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SceneCaptureRequestInfoFB(request_byte_count={repr(self.request_byte_count)}, request={repr(self._request)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SceneCaptureRequestInfoFB(request_byte_count={self.request_byte_count}, request={self._request}, next={self.next}, type={self.type})"

    @property
    def request(self) -> str:
        return self._request.decode()
    
    @request.setter
    def request(self, value: str) -> None:
        # noinspection PyAttributeOutsideInit
        self._request = value.encode()

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("request_byte_count", c_uint32),
        ("_request", c_char_p),
    ]


PFN_xrRequestSceneCaptureFB = CFUNCTYPE(Result.ctype(), Session, POINTER(SceneCaptureRequestInfoFB), POINTER(AsyncRequestIdFB))


class SpaceContainerFB(Structure):
    def __init__(
        self,
        uuid_capacity_input: int = 0,
        uuid_count_output: int = 0,
        uuids: POINTER(UuidEXT) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPACE_CONTAINER_FB,
    ) -> None:
        super().__init__(
            uuid_capacity_input=uuid_capacity_input,
            uuid_count_output=uuid_count_output,
            uuids=uuids,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceContainerFB(uuid_capacity_input={repr(self.uuid_capacity_input)}, uuid_count_output={repr(self.uuid_count_output)}, uuids={repr(self.uuids)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpaceContainerFB(uuid_capacity_input={self.uuid_capacity_input}, uuid_count_output={self.uuid_count_output}, uuids={self.uuids}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("uuid_capacity_input", c_uint32),
        ("uuid_count_output", c_uint32),
        ("uuids", POINTER(UuidEXT)),
    ]


PFN_xrGetSpaceContainerFB = CFUNCTYPE(Result.ctype(), Session, Space, POINTER(SpaceContainerFB))

FoveationEyeTrackedProfileCreateFlagsMETACInt = Flags64

FoveationEyeTrackedStateFlagsMETACInt = Flags64


class FoveationEyeTrackedProfileCreateInfoMETA(Structure):
    def __init__(
        self,
        flags: FoveationEyeTrackedProfileCreateFlagsMETA = FoveationEyeTrackedProfileCreateFlagsMETA(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.FOVEATION_EYE_TRACKED_PROFILE_CREATE_INFO_META,
    ) -> None:
        super().__init__(
            flags=FoveationEyeTrackedProfileCreateFlagsMETA(flags).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FoveationEyeTrackedProfileCreateInfoMETA(flags={repr(self.flags)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FoveationEyeTrackedProfileCreateInfoMETA(flags={self.flags}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", FoveationEyeTrackedProfileCreateFlagsMETACInt),
    ]


class FoveationEyeTrackedStateMETA(Structure):
    def __init__(
        self,
        flags: FoveationEyeTrackedStateFlagsMETA = FoveationEyeTrackedStateFlagsMETA(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.FOVEATION_EYE_TRACKED_STATE_META,
    ) -> None:
        super().__init__(
            flags=FoveationEyeTrackedStateFlagsMETA(flags).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FoveationEyeTrackedStateMETA(foveation_center={repr(self.foveation_center)}, flags={repr(self.flags)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FoveationEyeTrackedStateMETA(flags={self.flags}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("foveation_center", (Vector2f * 2)),
        ("flags", FoveationEyeTrackedStateFlagsMETACInt),
    ]


class SystemFoveationEyeTrackedPropertiesMETA(Structure):
    def __init__(
        self,
        supports_foveation_eye_tracked: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_FOVEATION_EYE_TRACKED_PROPERTIES_META,
    ) -> None:
        super().__init__(
            supports_foveation_eye_tracked=supports_foveation_eye_tracked,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemFoveationEyeTrackedPropertiesMETA(supports_foveation_eye_tracked={repr(self.supports_foveation_eye_tracked)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemFoveationEyeTrackedPropertiesMETA(supports_foveation_eye_tracked={self.supports_foveation_eye_tracked}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_foveation_eye_tracked", Bool32),
    ]


PFN_xrGetFoveationEyeTrackedStateMETA = CFUNCTYPE(Result.ctype(), Session, POINTER(FoveationEyeTrackedStateMETA))


class FaceTrackerFB_T(Structure):
    pass


class FaceTrackerFB(POINTER(FaceTrackerFB_T), HandleMixin):
    _type_ = FaceTrackerFB_T  # ctypes idiosyncrasy


class SystemFaceTrackingPropertiesFB(Structure):
    def __init__(
        self,
        supports_face_tracking: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_FACE_TRACKING_PROPERTIES_FB,
    ) -> None:
        super().__init__(
            supports_face_tracking=supports_face_tracking,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemFaceTrackingPropertiesFB(supports_face_tracking={repr(self.supports_face_tracking)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemFaceTrackingPropertiesFB(supports_face_tracking={self.supports_face_tracking}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_face_tracking", Bool32),
    ]


class FaceTrackerCreateInfoFB(Structure):
    def __init__(
        self,
        face_expression_set: FaceExpressionSetFB = FaceExpressionSetFB(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.FACE_TRACKER_CREATE_INFO_FB,
    ) -> None:
        super().__init__(
            face_expression_set=FaceExpressionSetFB(face_expression_set).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FaceTrackerCreateInfoFB(face_expression_set={repr(self.face_expression_set)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FaceTrackerCreateInfoFB(face_expression_set={self.face_expression_set}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("face_expression_set", FaceExpressionSetFB.ctype()),
    ]


class FaceExpressionInfoFB(Structure):
    def __init__(
        self,
        time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.FACE_EXPRESSION_INFO_FB,
    ) -> None:
        super().__init__(
            time=time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FaceExpressionInfoFB(time={repr(self.time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FaceExpressionInfoFB(time={self.time}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("time", Time),
    ]


class FaceExpressionStatusFB(Structure):
    def __init__(
        self,
        is_valid: Bool32 = 0,
        is_eye_following_blendshapes_valid: Bool32 = 0,
    ) -> None:
        super().__init__(
            is_valid=is_valid,
            is_eye_following_blendshapes_valid=is_eye_following_blendshapes_valid,
        )

    def __repr__(self) -> str:
        return f"xr.FaceExpressionStatusFB(is_valid={repr(self.is_valid)}, is_eye_following_blendshapes_valid={repr(self.is_eye_following_blendshapes_valid)})"

    def __str__(self) -> str:
        return f"xr.FaceExpressionStatusFB(is_valid={self.is_valid}, is_eye_following_blendshapes_valid={self.is_eye_following_blendshapes_valid})"

    _fields_ = [
        ("is_valid", Bool32),
        ("is_eye_following_blendshapes_valid", Bool32),
    ]


class FaceExpressionWeightsFB(Structure):
    def __init__(
        self,
        weight_count: Optional[int] = None,
        weights: ArrayFieldParamType[c_float] = None,
        confidence_count: Optional[int] = None,
        confidences: ArrayFieldParamType[c_float] = None,
        status: FaceExpressionStatusFB = None,
        time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.FACE_EXPRESSION_WEIGHTS_FB,
    ) -> None:
        weight_count, weights = array_field_helper(
            c_float, weight_count, weights)
        confidence_count, confidences = array_field_helper(
            c_float, confidence_count, confidences)
        if status is None:
            status = FaceExpressionStatusFB()
        super().__init__(
            weight_count=weight_count,
            _weights=weights,
            confidence_count=confidence_count,
            _confidences=confidences,
            status=status,
            time=time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FaceExpressionWeightsFB(weight_count={repr(self.weight_count)}, weights={repr(self._weights)}, confidence_count={repr(self.confidence_count)}, confidences={repr(self._confidences)}, status={repr(self.status)}, time={repr(self.time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FaceExpressionWeightsFB(weight_count={self.weight_count}, weights={self._weights}, confidence_count={self.confidence_count}, confidences={self._confidences}, status={self.status}, time={self.time}, next={self.next}, type={self.type})"

    @property
    def weights(self):
        if self.weight_count == 0:
            return (c_float * 0)()
        else:
            return (c_float * self.weight_count).from_address(
                ctypes.addressof(self._weights.contents))

    @weights.setter
    def weights(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.weight_count, self._weights = array_field_helper(
            c_float, None, value)

    @property
    def confidences(self):
        if self.confidence_count == 0:
            return (c_float * 0)()
        else:
            return (c_float * self.confidence_count).from_address(
                ctypes.addressof(self._confidences.contents))

    @confidences.setter
    def confidences(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.confidence_count, self._confidences = array_field_helper(
            c_float, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("weight_count", c_uint32),
        ("_weights", POINTER(c_float)),
        ("confidence_count", c_uint32),
        ("_confidences", POINTER(c_float)),
        ("status", FaceExpressionStatusFB),
        ("time", Time),
    ]


PFN_xrCreateFaceTrackerFB = CFUNCTYPE(Result.ctype(), Session, POINTER(FaceTrackerCreateInfoFB), POINTER(FaceTrackerFB))

PFN_xrDestroyFaceTrackerFB = CFUNCTYPE(Result.ctype(), FaceTrackerFB)

PFN_xrGetFaceExpressionWeightsFB = CFUNCTYPE(Result.ctype(), FaceTrackerFB, POINTER(FaceExpressionInfoFB), POINTER(FaceExpressionWeightsFB))


class EyeTrackerFB_T(Structure):
    pass


class EyeTrackerFB(POINTER(EyeTrackerFB_T), HandleMixin):
    _type_ = EyeTrackerFB_T  # ctypes idiosyncrasy


class EyeGazeFB(Structure):
    def __init__(
        self,
        is_valid: Bool32 = 0,
        gaze_pose: Posef = Posef(),
        gaze_confidence: float = 0,
    ) -> None:
        super().__init__(
            is_valid=is_valid,
            gaze_pose=gaze_pose,
            gaze_confidence=gaze_confidence,
        )

    def __repr__(self) -> str:
        return f"xr.EyeGazeFB(is_valid={repr(self.is_valid)}, gaze_pose={repr(self.gaze_pose)}, gaze_confidence={repr(self.gaze_confidence)})"

    def __str__(self) -> str:
        return f"xr.EyeGazeFB(is_valid={self.is_valid}, gaze_pose={self.gaze_pose}, gaze_confidence={self.gaze_confidence:.3f})"

    _fields_ = [
        ("is_valid", Bool32),
        ("gaze_pose", Posef),
        ("gaze_confidence", c_float),
    ]


class EyeTrackerCreateInfoFB(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.EYE_TRACKER_CREATE_INFO_FB,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EyeTrackerCreateInfoFB(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EyeTrackerCreateInfoFB(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class EyeGazesInfoFB(Structure):
    def __init__(
        self,
        base_space: Space = None,
        time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.EYE_GAZES_INFO_FB,
    ) -> None:
        super().__init__(
            base_space=base_space,
            time=time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EyeGazesInfoFB(base_space={repr(self.base_space)}, time={repr(self.time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EyeGazesInfoFB(base_space={self.base_space}, time={self.time}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("base_space", Space),
        ("time", Time),
    ]


class SystemEyeTrackingPropertiesFB(Structure):
    def __init__(
        self,
        supports_eye_tracking: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_EYE_TRACKING_PROPERTIES_FB,
    ) -> None:
        super().__init__(
            supports_eye_tracking=supports_eye_tracking,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemEyeTrackingPropertiesFB(supports_eye_tracking={repr(self.supports_eye_tracking)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemEyeTrackingPropertiesFB(supports_eye_tracking={self.supports_eye_tracking}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_eye_tracking", Bool32),
    ]


class EyeGazesFB(Structure):
    def __init__(
        self,
        time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.EYE_GAZES_FB,
    ) -> None:
        super().__init__(
            time=time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EyeGazesFB(gaze={repr(self.gaze)}, time={repr(self.time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EyeGazesFB(time={self.time}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("gaze", (EyeGazeFB * 2)),
        ("time", Time),
    ]


PFN_xrCreateEyeTrackerFB = CFUNCTYPE(Result.ctype(), Session, POINTER(EyeTrackerCreateInfoFB), POINTER(EyeTrackerFB))

PFN_xrDestroyEyeTrackerFB = CFUNCTYPE(Result.ctype(), EyeTrackerFB)

PFN_xrGetEyeGazesFB = CFUNCTYPE(Result.ctype(), EyeTrackerFB, POINTER(EyeGazesInfoFB), POINTER(EyeGazesFB))


class PassthroughKeyboardHandsIntensityFB(Structure):
    def __init__(
        self,
        left_hand_intensity: float = 0,
        right_hand_intensity: float = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.PASSTHROUGH_KEYBOARD_HANDS_INTENSITY_FB,
    ) -> None:
        super().__init__(
            left_hand_intensity=left_hand_intensity,
            right_hand_intensity=right_hand_intensity,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PassthroughKeyboardHandsIntensityFB(left_hand_intensity={repr(self.left_hand_intensity)}, right_hand_intensity={repr(self.right_hand_intensity)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PassthroughKeyboardHandsIntensityFB(left_hand_intensity={self.left_hand_intensity:.3f}, right_hand_intensity={self.right_hand_intensity:.3f}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("left_hand_intensity", c_float),
        ("right_hand_intensity", c_float),
    ]


PFN_xrPassthroughLayerSetKeyboardHandsIntensityFB = CFUNCTYPE(Result.ctype(), PassthroughLayerFB, POINTER(PassthroughKeyboardHandsIntensityFB))

CompositionLayerSettingsFlagsFBCInt = Flags64


class CompositionLayerSettingsFB(Structure):
    def __init__(
        self,
        layer_flags: CompositionLayerSettingsFlagsFB = CompositionLayerSettingsFlagsFB(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.COMPOSITION_LAYER_SETTINGS_FB,
    ) -> None:
        super().__init__(
            layer_flags=CompositionLayerSettingsFlagsFB(layer_flags).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerSettingsFB(layer_flags={repr(self.layer_flags)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerSettingsFB(layer_flags={self.layer_flags}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerSettingsFlagsFBCInt),
    ]


class HapticPcmVibrationFB(Structure):
    def __init__(
        self,
        buffer_size: int = 0,
        buffer: POINTER(c_float) = None,
        sample_rate: float = 0,
        append: Bool32 = 0,
        samples_consumed: POINTER(c_uint32) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.HAPTIC_PCM_VIBRATION_FB,
    ) -> None:
        super().__init__(
            buffer_size=buffer_size,
            buffer=buffer,
            sample_rate=sample_rate,
            append=append,
            samples_consumed=samples_consumed,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.HapticPcmVibrationFB(buffer_size={repr(self.buffer_size)}, buffer={repr(self.buffer)}, sample_rate={repr(self.sample_rate)}, append={repr(self.append)}, samples_consumed={repr(self.samples_consumed)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.HapticPcmVibrationFB(buffer_size={self.buffer_size}, buffer={self.buffer}, sample_rate={self.sample_rate:.3f}, append={self.append}, samples_consumed={self.samples_consumed}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("buffer_size", c_uint32),
        ("buffer", POINTER(c_float)),
        ("sample_rate", c_float),
        ("append", Bool32),
        ("samples_consumed", POINTER(c_uint32)),
    ]


class DevicePcmSampleRateStateFB(Structure):
    def __init__(
        self,
        sample_rate: float = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.DEVICE_PCM_SAMPLE_RATE_STATE_FB,
    ) -> None:
        super().__init__(
            sample_rate=sample_rate,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.DevicePcmSampleRateStateFB(sample_rate={repr(self.sample_rate)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.DevicePcmSampleRateStateFB(sample_rate={self.sample_rate:.3f}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("sample_rate", c_float),
    ]


DevicePcmSampleRateGetInfoFB = DevicePcmSampleRateStateFB

PFN_xrGetDeviceSampleRateFB = CFUNCTYPE(Result.ctype(), Session, POINTER(HapticActionInfo), POINTER(DevicePcmSampleRateGetInfoFB))

FrameSynthesisInfoFlagsEXTCInt = Flags64


class FrameSynthesisInfoEXT(Structure):
    def __init__(
        self,
        layer_flags: FrameSynthesisInfoFlagsEXT = FrameSynthesisInfoFlagsEXT(),  # noqa
        motion_vector_sub_image: SwapchainSubImage = None,
        motion_vector_scale: Vector4f = None,
        motion_vector_offset: Vector4f = None,
        app_space_delta_pose: Posef = Posef(),
        depth_sub_image: SwapchainSubImage = None,
        min_depth: float = 0,
        max_depth: float = 0,
        near_z: float = 0,
        far_z: float = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.FRAME_SYNTHESIS_INFO_EXT,
    ) -> None:
        if motion_vector_sub_image is None:
            motion_vector_sub_image = SwapchainSubImage()
        if motion_vector_scale is None:
            motion_vector_scale = Vector4f()
        if motion_vector_offset is None:
            motion_vector_offset = Vector4f()
        if depth_sub_image is None:
            depth_sub_image = SwapchainSubImage()
        super().__init__(
            layer_flags=FrameSynthesisInfoFlagsEXT(layer_flags).value,
            motion_vector_sub_image=motion_vector_sub_image,
            motion_vector_scale=motion_vector_scale,
            motion_vector_offset=motion_vector_offset,
            app_space_delta_pose=app_space_delta_pose,
            depth_sub_image=depth_sub_image,
            min_depth=min_depth,
            max_depth=max_depth,
            near_z=near_z,
            far_z=far_z,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FrameSynthesisInfoEXT(layer_flags={repr(self.layer_flags)}, motion_vector_sub_image={repr(self.motion_vector_sub_image)}, motion_vector_scale={repr(self.motion_vector_scale)}, motion_vector_offset={repr(self.motion_vector_offset)}, app_space_delta_pose={repr(self.app_space_delta_pose)}, depth_sub_image={repr(self.depth_sub_image)}, min_depth={repr(self.min_depth)}, max_depth={repr(self.max_depth)}, near_z={repr(self.near_z)}, far_z={repr(self.far_z)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FrameSynthesisInfoEXT(layer_flags={self.layer_flags}, motion_vector_sub_image={self.motion_vector_sub_image}, motion_vector_scale={self.motion_vector_scale}, motion_vector_offset={self.motion_vector_offset}, app_space_delta_pose={self.app_space_delta_pose}, depth_sub_image={self.depth_sub_image}, min_depth={self.min_depth:.3f}, max_depth={self.max_depth:.3f}, near_z={self.near_z:.3f}, far_z={self.far_z:.3f}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", FrameSynthesisInfoFlagsEXTCInt),
        ("motion_vector_sub_image", SwapchainSubImage),
        ("motion_vector_scale", Vector4f),
        ("motion_vector_offset", Vector4f),
        ("app_space_delta_pose", Posef),
        ("depth_sub_image", SwapchainSubImage),
        ("min_depth", c_float),
        ("max_depth", c_float),
        ("near_z", c_float),
        ("far_z", c_float),
    ]


class FrameSynthesisConfigViewEXT(Structure):
    def __init__(
        self,
        recommended_motion_vector_image_rect_width: int = 0,
        recommended_motion_vector_image_rect_height: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.FRAME_SYNTHESIS_CONFIG_VIEW_EXT,
    ) -> None:
        super().__init__(
            recommended_motion_vector_image_rect_width=recommended_motion_vector_image_rect_width,
            recommended_motion_vector_image_rect_height=recommended_motion_vector_image_rect_height,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FrameSynthesisConfigViewEXT(recommended_motion_vector_image_rect_width={repr(self.recommended_motion_vector_image_rect_width)}, recommended_motion_vector_image_rect_height={repr(self.recommended_motion_vector_image_rect_height)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FrameSynthesisConfigViewEXT(recommended_motion_vector_image_rect_width={self.recommended_motion_vector_image_rect_width}, recommended_motion_vector_image_rect_height={self.recommended_motion_vector_image_rect_height}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("recommended_motion_vector_image_rect_width", c_uint32),
        ("recommended_motion_vector_image_rect_height", c_uint32),
    ]


class CompositionLayerDepthTestFB(Structure):
    def __init__(
        self,
        depth_mask: Bool32 = 0,
        compare_op: CompareOpFB = CompareOpFB(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.COMPOSITION_LAYER_DEPTH_TEST_FB,
    ) -> None:
        super().__init__(
            depth_mask=depth_mask,
            compare_op=CompareOpFB(compare_op).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerDepthTestFB(depth_mask={repr(self.depth_mask)}, compare_op={repr(self.compare_op)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerDepthTestFB(depth_mask={self.depth_mask}, compare_op={self.compare_op}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("depth_mask", Bool32),
        ("compare_op", CompareOpFB.ctype()),
    ]


class LocalDimmingFrameEndInfoMETA(Structure):
    def __init__(
        self,
        local_dimming_mode: LocalDimmingModeMETA = LocalDimmingModeMETA(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.LOCAL_DIMMING_FRAME_END_INFO_META,
    ) -> None:
        super().__init__(
            local_dimming_mode=LocalDimmingModeMETA(local_dimming_mode).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.LocalDimmingFrameEndInfoMETA(local_dimming_mode={repr(self.local_dimming_mode)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.LocalDimmingFrameEndInfoMETA(local_dimming_mode={self.local_dimming_mode}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("local_dimming_mode", LocalDimmingModeMETA.ctype()),
    ]


PassthroughPreferenceFlagsMETACInt = Flags64


class PassthroughPreferencesMETA(Structure):
    def __init__(
        self,
        flags: PassthroughPreferenceFlagsMETA = PassthroughPreferenceFlagsMETA(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.PASSTHROUGH_PREFERENCES_META,
    ) -> None:
        super().__init__(
            flags=PassthroughPreferenceFlagsMETA(flags).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PassthroughPreferencesMETA(flags={repr(self.flags)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PassthroughPreferencesMETA(flags={self.flags}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", PassthroughPreferenceFlagsMETACInt),
    ]


PFN_xrGetPassthroughPreferencesMETA = CFUNCTYPE(Result.ctype(), Session, POINTER(PassthroughPreferencesMETA))


class VirtualKeyboardMETA_T(Structure):
    pass


class VirtualKeyboardMETA(POINTER(VirtualKeyboardMETA_T), HandleMixin):
    _type_ = VirtualKeyboardMETA_T  # ctypes idiosyncrasy

VirtualKeyboardInputStateFlagsMETACInt = Flags64


class SystemVirtualKeyboardPropertiesMETA(Structure):
    def __init__(
        self,
        supports_virtual_keyboard: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_VIRTUAL_KEYBOARD_PROPERTIES_META,
    ) -> None:
        super().__init__(
            supports_virtual_keyboard=supports_virtual_keyboard,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemVirtualKeyboardPropertiesMETA(supports_virtual_keyboard={repr(self.supports_virtual_keyboard)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemVirtualKeyboardPropertiesMETA(supports_virtual_keyboard={self.supports_virtual_keyboard}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_virtual_keyboard", Bool32),
    ]


class VirtualKeyboardCreateInfoMETA(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.VIRTUAL_KEYBOARD_CREATE_INFO_META,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.VirtualKeyboardCreateInfoMETA(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.VirtualKeyboardCreateInfoMETA(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class VirtualKeyboardSpaceCreateInfoMETA(Structure):
    def __init__(
        self,
        location_type: VirtualKeyboardLocationTypeMETA = VirtualKeyboardLocationTypeMETA(),  # noqa
        space: Space = None,
        pose_in_space: Posef = Posef(),
        next: c_void_p = None,
        type: StructureType = StructureType.VIRTUAL_KEYBOARD_SPACE_CREATE_INFO_META,
    ) -> None:
        super().__init__(
            location_type=VirtualKeyboardLocationTypeMETA(location_type).value,
            space=space,
            pose_in_space=pose_in_space,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.VirtualKeyboardSpaceCreateInfoMETA(location_type={repr(self.location_type)}, space={repr(self.space)}, pose_in_space={repr(self.pose_in_space)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.VirtualKeyboardSpaceCreateInfoMETA(location_type={self.location_type}, space={self.space}, pose_in_space={self.pose_in_space}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("location_type", VirtualKeyboardLocationTypeMETA.ctype()),
        ("space", Space),
        ("pose_in_space", Posef),
    ]


class VirtualKeyboardLocationInfoMETA(Structure):
    def __init__(
        self,
        location_type: VirtualKeyboardLocationTypeMETA = VirtualKeyboardLocationTypeMETA(),  # noqa
        space: Space = None,
        pose_in_space: Posef = Posef(),
        scale: float = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.VIRTUAL_KEYBOARD_LOCATION_INFO_META,
    ) -> None:
        super().__init__(
            location_type=VirtualKeyboardLocationTypeMETA(location_type).value,
            space=space,
            pose_in_space=pose_in_space,
            scale=scale,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.VirtualKeyboardLocationInfoMETA(location_type={repr(self.location_type)}, space={repr(self.space)}, pose_in_space={repr(self.pose_in_space)}, scale={repr(self.scale)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.VirtualKeyboardLocationInfoMETA(location_type={self.location_type}, space={self.space}, pose_in_space={self.pose_in_space}, scale={self.scale:.3f}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("location_type", VirtualKeyboardLocationTypeMETA.ctype()),
        ("space", Space),
        ("pose_in_space", Posef),
        ("scale", c_float),
    ]


class VirtualKeyboardModelVisibilitySetInfoMETA(Structure):
    def __init__(
        self,
        visible: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.VIRTUAL_KEYBOARD_MODEL_VISIBILITY_SET_INFO_META,
    ) -> None:
        super().__init__(
            visible=visible,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.VirtualKeyboardModelVisibilitySetInfoMETA(visible={repr(self.visible)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.VirtualKeyboardModelVisibilitySetInfoMETA(visible={self.visible}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("visible", Bool32),
    ]


class VirtualKeyboardAnimationStateMETA(Structure):
    def __init__(
        self,
        animation_index: int = 0,
        fraction: float = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.VIRTUAL_KEYBOARD_ANIMATION_STATE_META,
    ) -> None:
        super().__init__(
            animation_index=animation_index,
            fraction=fraction,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.VirtualKeyboardAnimationStateMETA(animation_index={repr(self.animation_index)}, fraction={repr(self.fraction)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.VirtualKeyboardAnimationStateMETA(animation_index={self.animation_index}, fraction={self.fraction:.3f}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("animation_index", c_int32),
        ("fraction", c_float),
    ]


class VirtualKeyboardModelAnimationStatesMETA(Structure):
    def __init__(
        self,
        state_capacity_input: int = 0,
        state_count_output: int = 0,
        states: POINTER(VirtualKeyboardAnimationStateMETA) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.VIRTUAL_KEYBOARD_MODEL_ANIMATION_STATES_META,
    ) -> None:
        super().__init__(
            state_capacity_input=state_capacity_input,
            state_count_output=state_count_output,
            states=states,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.VirtualKeyboardModelAnimationStatesMETA(state_capacity_input={repr(self.state_capacity_input)}, state_count_output={repr(self.state_count_output)}, states={repr(self.states)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.VirtualKeyboardModelAnimationStatesMETA(state_capacity_input={self.state_capacity_input}, state_count_output={self.state_count_output}, states={self.states}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("state_capacity_input", c_uint32),
        ("state_count_output", c_uint32),
        ("states", POINTER(VirtualKeyboardAnimationStateMETA)),
    ]


class VirtualKeyboardTextureDataMETA(Structure):
    def __init__(
        self,
        texture_width: int = 0,
        texture_height: int = 0,
        buffer_capacity_input: int = 0,
        buffer_count_output: int = 0,
        buffer: POINTER(c_uint8) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.VIRTUAL_KEYBOARD_TEXTURE_DATA_META,
    ) -> None:
        super().__init__(
            texture_width=texture_width,
            texture_height=texture_height,
            buffer_capacity_input=buffer_capacity_input,
            buffer_count_output=buffer_count_output,
            buffer=buffer,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.VirtualKeyboardTextureDataMETA(texture_width={repr(self.texture_width)}, texture_height={repr(self.texture_height)}, buffer_capacity_input={repr(self.buffer_capacity_input)}, buffer_count_output={repr(self.buffer_count_output)}, buffer={repr(self.buffer)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.VirtualKeyboardTextureDataMETA(texture_width={self.texture_width}, texture_height={self.texture_height}, buffer_capacity_input={self.buffer_capacity_input}, buffer_count_output={self.buffer_count_output}, buffer={self.buffer}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("texture_width", c_uint32),
        ("texture_height", c_uint32),
        ("buffer_capacity_input", c_uint32),
        ("buffer_count_output", c_uint32),
        ("buffer", POINTER(c_uint8)),
    ]


class VirtualKeyboardInputInfoMETA(Structure):
    def __init__(
        self,
        input_source: VirtualKeyboardInputSourceMETA = VirtualKeyboardInputSourceMETA(),  # noqa
        input_space: Space = None,
        input_pose_in_space: Posef = Posef(),
        input_state: VirtualKeyboardInputStateFlagsMETA = VirtualKeyboardInputStateFlagsMETA(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.VIRTUAL_KEYBOARD_INPUT_INFO_META,
    ) -> None:
        super().__init__(
            input_source=VirtualKeyboardInputSourceMETA(input_source).value,
            input_space=input_space,
            input_pose_in_space=input_pose_in_space,
            input_state=VirtualKeyboardInputStateFlagsMETA(input_state).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.VirtualKeyboardInputInfoMETA(input_source={repr(self.input_source)}, input_space={repr(self.input_space)}, input_pose_in_space={repr(self.input_pose_in_space)}, input_state={repr(self.input_state)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.VirtualKeyboardInputInfoMETA(input_source={self.input_source}, input_space={self.input_space}, input_pose_in_space={self.input_pose_in_space}, input_state={self.input_state}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("input_source", VirtualKeyboardInputSourceMETA.ctype()),
        ("input_space", Space),
        ("input_pose_in_space", Posef),
        ("input_state", VirtualKeyboardInputStateFlagsMETACInt),
    ]


class VirtualKeyboardTextContextChangeInfoMETA(Structure):
    def __init__(
        self,
        text_context: str = "",
        next: c_void_p = None,
        type: StructureType = StructureType.VIRTUAL_KEYBOARD_TEXT_CONTEXT_CHANGE_INFO_META,
    ) -> None:
        super().__init__(
            _text_context=text_context.encode(),
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.VirtualKeyboardTextContextChangeInfoMETA(text_context={repr(self._text_context)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.VirtualKeyboardTextContextChangeInfoMETA(text_context={self._text_context}, next={self.next}, type={self.type})"

    @property
    def text_context(self) -> str:
        return self._text_context.decode()
    
    @text_context.setter
    def text_context(self, value: str) -> None:
        # noinspection PyAttributeOutsideInit
        self._text_context = value.encode()

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("_text_context", c_char_p),
    ]


class EventDataVirtualKeyboardCommitTextMETA(Structure):
    def __init__(
        self,
        keyboard: VirtualKeyboardMETA = None,
        text: str = "",
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_VIRTUAL_KEYBOARD_COMMIT_TEXT_META,
    ) -> None:
        super().__init__(
            keyboard=keyboard,
            text=text.encode(),
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataVirtualKeyboardCommitTextMETA(keyboard={repr(self.keyboard)}, text={repr(self.text)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataVirtualKeyboardCommitTextMETA(keyboard={self.keyboard}, text={self.text}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("keyboard", VirtualKeyboardMETA),
        ("text", (c_char * 3992)),
    ]


class EventDataVirtualKeyboardBackspaceMETA(Structure):
    def __init__(
        self,
        keyboard: VirtualKeyboardMETA = None,
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_VIRTUAL_KEYBOARD_BACKSPACE_META,
    ) -> None:
        super().__init__(
            keyboard=keyboard,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataVirtualKeyboardBackspaceMETA(keyboard={repr(self.keyboard)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataVirtualKeyboardBackspaceMETA(keyboard={self.keyboard}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("keyboard", VirtualKeyboardMETA),
    ]


class EventDataVirtualKeyboardEnterMETA(Structure):
    def __init__(
        self,
        keyboard: VirtualKeyboardMETA = None,
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_VIRTUAL_KEYBOARD_ENTER_META,
    ) -> None:
        super().__init__(
            keyboard=keyboard,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataVirtualKeyboardEnterMETA(keyboard={repr(self.keyboard)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataVirtualKeyboardEnterMETA(keyboard={self.keyboard}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("keyboard", VirtualKeyboardMETA),
    ]


class EventDataVirtualKeyboardShownMETA(Structure):
    def __init__(
        self,
        keyboard: VirtualKeyboardMETA = None,
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_VIRTUAL_KEYBOARD_SHOWN_META,
    ) -> None:
        super().__init__(
            keyboard=keyboard,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataVirtualKeyboardShownMETA(keyboard={repr(self.keyboard)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataVirtualKeyboardShownMETA(keyboard={self.keyboard}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("keyboard", VirtualKeyboardMETA),
    ]


class EventDataVirtualKeyboardHiddenMETA(Structure):
    def __init__(
        self,
        keyboard: VirtualKeyboardMETA = None,
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_VIRTUAL_KEYBOARD_HIDDEN_META,
    ) -> None:
        super().__init__(
            keyboard=keyboard,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataVirtualKeyboardHiddenMETA(keyboard={repr(self.keyboard)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataVirtualKeyboardHiddenMETA(keyboard={self.keyboard}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("keyboard", VirtualKeyboardMETA),
    ]


PFN_xrCreateVirtualKeyboardMETA = CFUNCTYPE(Result.ctype(), Session, POINTER(VirtualKeyboardCreateInfoMETA), POINTER(VirtualKeyboardMETA))

PFN_xrDestroyVirtualKeyboardMETA = CFUNCTYPE(Result.ctype(), VirtualKeyboardMETA)

PFN_xrCreateVirtualKeyboardSpaceMETA = CFUNCTYPE(Result.ctype(), Session, VirtualKeyboardMETA, POINTER(VirtualKeyboardSpaceCreateInfoMETA), POINTER(Space))

PFN_xrSuggestVirtualKeyboardLocationMETA = CFUNCTYPE(Result.ctype(), VirtualKeyboardMETA, POINTER(VirtualKeyboardLocationInfoMETA))

PFN_xrGetVirtualKeyboardScaleMETA = CFUNCTYPE(Result.ctype(), VirtualKeyboardMETA, POINTER(c_float))

PFN_xrSetVirtualKeyboardModelVisibilityMETA = CFUNCTYPE(Result.ctype(), VirtualKeyboardMETA, POINTER(VirtualKeyboardModelVisibilitySetInfoMETA))

PFN_xrGetVirtualKeyboardModelAnimationStatesMETA = CFUNCTYPE(Result.ctype(), VirtualKeyboardMETA, POINTER(VirtualKeyboardModelAnimationStatesMETA))

PFN_xrGetVirtualKeyboardDirtyTexturesMETA = CFUNCTYPE(Result.ctype(), VirtualKeyboardMETA, c_uint32, POINTER(c_uint32), POINTER(c_uint64))

PFN_xrGetVirtualKeyboardTextureDataMETA = CFUNCTYPE(Result.ctype(), VirtualKeyboardMETA, c_uint64, POINTER(VirtualKeyboardTextureDataMETA))

PFN_xrSendVirtualKeyboardInputMETA = CFUNCTYPE(Result.ctype(), VirtualKeyboardMETA, POINTER(VirtualKeyboardInputInfoMETA), POINTER(Posef))

PFN_xrChangeVirtualKeyboardTextContextMETA = CFUNCTYPE(Result.ctype(), VirtualKeyboardMETA, POINTER(VirtualKeyboardTextContextChangeInfoMETA))

ExternalCameraStatusFlagsOCULUSCInt = Flags64


class ExternalCameraIntrinsicsOCULUS(Structure):
    def __init__(
        self,
        last_change_time: Time = 0,
        fov: Fovf = None,
        virtual_near_plane_distance: float = 0,
        virtual_far_plane_distance: float = 0,
        image_sensor_pixel_resolution: Extent2Di = None,
    ) -> None:
        if fov is None:
            fov = Fovf()
        if image_sensor_pixel_resolution is None:
            image_sensor_pixel_resolution = Extent2Di()
        super().__init__(
            last_change_time=last_change_time,
            fov=fov,
            virtual_near_plane_distance=virtual_near_plane_distance,
            virtual_far_plane_distance=virtual_far_plane_distance,
            image_sensor_pixel_resolution=image_sensor_pixel_resolution,
        )

    def __repr__(self) -> str:
        return f"xr.ExternalCameraIntrinsicsOCULUS(last_change_time={repr(self.last_change_time)}, fov={repr(self.fov)}, virtual_near_plane_distance={repr(self.virtual_near_plane_distance)}, virtual_far_plane_distance={repr(self.virtual_far_plane_distance)}, image_sensor_pixel_resolution={repr(self.image_sensor_pixel_resolution)})"

    def __str__(self) -> str:
        return f"xr.ExternalCameraIntrinsicsOCULUS(last_change_time={self.last_change_time}, fov={self.fov}, virtual_near_plane_distance={self.virtual_near_plane_distance:.3f}, virtual_far_plane_distance={self.virtual_far_plane_distance:.3f}, image_sensor_pixel_resolution={self.image_sensor_pixel_resolution})"

    _fields_ = [
        ("last_change_time", Time),
        ("fov", Fovf),
        ("virtual_near_plane_distance", c_float),
        ("virtual_far_plane_distance", c_float),
        ("image_sensor_pixel_resolution", Extent2Di),
    ]


class ExternalCameraExtrinsicsOCULUS(Structure):
    def __init__(
        self,
        last_change_time: Time = 0,
        camera_status_flags: ExternalCameraStatusFlagsOCULUS = ExternalCameraStatusFlagsOCULUS(),  # noqa
        attached_to_device: ExternalCameraAttachedToDeviceOCULUS = ExternalCameraAttachedToDeviceOCULUS(),  # noqa
        relative_pose: Posef = Posef(),
    ) -> None:
        super().__init__(
            last_change_time=last_change_time,
            camera_status_flags=ExternalCameraStatusFlagsOCULUS(camera_status_flags).value,
            attached_to_device=ExternalCameraAttachedToDeviceOCULUS(attached_to_device).value,
            relative_pose=relative_pose,
        )

    def __repr__(self) -> str:
        return f"xr.ExternalCameraExtrinsicsOCULUS(last_change_time={repr(self.last_change_time)}, camera_status_flags={repr(self.camera_status_flags)}, attached_to_device={repr(self.attached_to_device)}, relative_pose={repr(self.relative_pose)})"

    def __str__(self) -> str:
        return f"xr.ExternalCameraExtrinsicsOCULUS(last_change_time={self.last_change_time}, camera_status_flags={self.camera_status_flags}, attached_to_device={self.attached_to_device}, relative_pose={self.relative_pose})"

    _fields_ = [
        ("last_change_time", Time),
        ("camera_status_flags", ExternalCameraStatusFlagsOCULUSCInt),
        ("attached_to_device", ExternalCameraAttachedToDeviceOCULUS.ctype()),
        ("relative_pose", Posef),
    ]


class ExternalCameraOCULUS(Structure):
    def __init__(
        self,
        name: str = "",
        intrinsics: ExternalCameraIntrinsicsOCULUS = None,
        extrinsics: ExternalCameraExtrinsicsOCULUS = None,
        next: c_void_p = None,
        type: StructureType = StructureType.EXTERNAL_CAMERA_OCULUS,
    ) -> None:
        if intrinsics is None:
            intrinsics = ExternalCameraIntrinsicsOCULUS()
        if extrinsics is None:
            extrinsics = ExternalCameraExtrinsicsOCULUS()
        super().__init__(
            name=name.encode(),
            intrinsics=intrinsics,
            extrinsics=extrinsics,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ExternalCameraOCULUS(name={repr(self.name)}, intrinsics={repr(self.intrinsics)}, extrinsics={repr(self.extrinsics)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ExternalCameraOCULUS(name={self.name}, intrinsics={self.intrinsics}, extrinsics={self.extrinsics}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("name", (c_char * 32)),
        ("intrinsics", ExternalCameraIntrinsicsOCULUS),
        ("extrinsics", ExternalCameraExtrinsicsOCULUS),
    ]


PFN_xrEnumerateExternalCamerasOCULUS = CFUNCTYPE(Result.ctype(), Session, c_uint32, POINTER(c_uint32), POINTER(ExternalCameraOCULUS))

PerformanceMetricsCounterFlagsMETACInt = Flags64


class PerformanceMetricsStateMETA(Structure):
    def __init__(
        self,
        enabled: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.PERFORMANCE_METRICS_STATE_META,
    ) -> None:
        super().__init__(
            enabled=enabled,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PerformanceMetricsStateMETA(enabled={repr(self.enabled)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PerformanceMetricsStateMETA(enabled={self.enabled}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("enabled", Bool32),
    ]


class PerformanceMetricsCounterMETA(Structure):
    def __init__(
        self,
        counter_flags: PerformanceMetricsCounterFlagsMETA = PerformanceMetricsCounterFlagsMETA(),  # noqa
        counter_unit: PerformanceMetricsCounterUnitMETA = PerformanceMetricsCounterUnitMETA(),  # noqa
        uint_value: int = 0,
        float_value: float = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.PERFORMANCE_METRICS_COUNTER_META,
    ) -> None:
        super().__init__(
            counter_flags=PerformanceMetricsCounterFlagsMETA(counter_flags).value,
            counter_unit=PerformanceMetricsCounterUnitMETA(counter_unit).value,
            uint_value=uint_value,
            float_value=float_value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PerformanceMetricsCounterMETA(counter_flags={repr(self.counter_flags)}, counter_unit={repr(self.counter_unit)}, uint_value={repr(self.uint_value)}, float_value={repr(self.float_value)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PerformanceMetricsCounterMETA(counter_flags={self.counter_flags}, counter_unit={self.counter_unit}, uint_value={self.uint_value}, float_value={self.float_value:.3f}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("counter_flags", PerformanceMetricsCounterFlagsMETACInt),
        ("counter_unit", PerformanceMetricsCounterUnitMETA.ctype()),
        ("uint_value", c_uint32),
        ("float_value", c_float),
    ]


PFN_xrEnumeratePerformanceMetricsCounterPathsMETA = CFUNCTYPE(Result.ctype(), Instance, c_uint32, POINTER(c_uint32), POINTER(Path))

PFN_xrSetPerformanceMetricsStateMETA = CFUNCTYPE(Result.ctype(), Session, POINTER(PerformanceMetricsStateMETA))

PFN_xrGetPerformanceMetricsStateMETA = CFUNCTYPE(Result.ctype(), Session, POINTER(PerformanceMetricsStateMETA))

PFN_xrQueryPerformanceMetricsCounterMETA = CFUNCTYPE(Result.ctype(), Session, Path, POINTER(PerformanceMetricsCounterMETA))


class SpaceListSaveInfoFB(Structure):
    def __init__(
        self,
        space_count: Optional[int] = None,
        spaces: ArrayFieldParamType[Space] = None,
        location: SpaceStorageLocationFB = SpaceStorageLocationFB(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.SPACE_LIST_SAVE_INFO_FB,
    ) -> None:
        space_count, spaces = array_field_helper(
            Space, space_count, spaces)
        super().__init__(
            space_count=space_count,
            _spaces=spaces,
            location=SpaceStorageLocationFB(location).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceListSaveInfoFB(space_count={repr(self.space_count)}, spaces={repr(self._spaces)}, location={repr(self.location)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpaceListSaveInfoFB(space_count={self.space_count}, spaces={self._spaces}, location={self.location}, next={self.next}, type={self.type})"

    @property
    def spaces(self):
        if self.space_count == 0:
            return (Space * 0)()
        else:
            return (Space * self.space_count).from_address(
                ctypes.addressof(self._spaces.contents))

    @spaces.setter
    def spaces(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.space_count, self._spaces = array_field_helper(
            Space, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("space_count", c_uint32),
        ("_spaces", POINTER(Space)),
        ("location", SpaceStorageLocationFB.ctype()),
    ]


class EventDataSpaceListSaveCompleteFB(Structure):
    def __init__(
        self,
        request_id: AsyncRequestIdFB = 0,
        result: Result = Result(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_SPACE_LIST_SAVE_COMPLETE_FB,
    ) -> None:
        super().__init__(
            request_id=request_id,
            result=Result(result).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataSpaceListSaveCompleteFB(request_id={repr(self.request_id)}, result={repr(self.result)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataSpaceListSaveCompleteFB(request_id={self.request_id}, result={self.result}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("request_id", AsyncRequestIdFB),
        ("result", Result.ctype()),
    ]


PFN_xrSaveSpaceListFB = CFUNCTYPE(Result.ctype(), Session, POINTER(SpaceListSaveInfoFB), POINTER(AsyncRequestIdFB))

SpaceUserIdFB = c_uint64


class SpaceUserCreateInfoFB(Structure):
    def __init__(
        self,
        user_id: SpaceUserIdFB = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SPACE_USER_CREATE_INFO_FB,
    ) -> None:
        super().__init__(
            user_id=user_id,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceUserCreateInfoFB(user_id={repr(self.user_id)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpaceUserCreateInfoFB(user_id={self.user_id}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("user_id", SpaceUserIdFB),
    ]


PFN_xrCreateSpaceUserFB = CFUNCTYPE(Result.ctype(), Session, POINTER(SpaceUserCreateInfoFB), POINTER(SpaceUserFB))

PFN_xrGetSpaceUserIdFB = CFUNCTYPE(Result.ctype(), SpaceUserFB, POINTER(SpaceUserIdFB))

PFN_xrDestroySpaceUserFB = CFUNCTYPE(Result.ctype(), SpaceUserFB)


class SystemHeadsetIdPropertiesMETA(Structure):
    def __init__(
        self,
        id: UuidEXT = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_HEADSET_ID_PROPERTIES_META,
    ) -> None:
        super().__init__(
            id=id,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemHeadsetIdPropertiesMETA(id={repr(self.id)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemHeadsetIdPropertiesMETA(id={self.id}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("id", UuidEXT),
    ]


class RecommendedLayerResolutionMETA(Structure):
    def __init__(
        self,
        recommended_image_dimensions: Extent2Di = None,
        is_valid: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.RECOMMENDED_LAYER_RESOLUTION_META,
    ) -> None:
        if recommended_image_dimensions is None:
            recommended_image_dimensions = Extent2Di()
        super().__init__(
            recommended_image_dimensions=recommended_image_dimensions,
            is_valid=is_valid,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.RecommendedLayerResolutionMETA(recommended_image_dimensions={repr(self.recommended_image_dimensions)}, is_valid={repr(self.is_valid)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.RecommendedLayerResolutionMETA(recommended_image_dimensions={self.recommended_image_dimensions}, is_valid={self.is_valid}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("recommended_image_dimensions", Extent2Di),
        ("is_valid", Bool32),
    ]


class RecommendedLayerResolutionGetInfoMETA(Structure):
    def __init__(
        self,
        layer: POINTER(CompositionLayerBaseHeader) = None,
        predicted_display_time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.RECOMMENDED_LAYER_RESOLUTION_GET_INFO_META,
    ) -> None:
        super().__init__(
            layer=layer,
            predicted_display_time=predicted_display_time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.RecommendedLayerResolutionGetInfoMETA(layer={repr(self.layer)}, predicted_display_time={repr(self.predicted_display_time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.RecommendedLayerResolutionGetInfoMETA(layer={self.layer}, predicted_display_time={self.predicted_display_time}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer", POINTER(CompositionLayerBaseHeader)),
        ("predicted_display_time", Time),
    ]


PFN_xrGetRecommendedLayerResolutionMETA = CFUNCTYPE(Result.ctype(), Session, POINTER(RecommendedLayerResolutionGetInfoMETA), POINTER(RecommendedLayerResolutionMETA))


class SystemSpacePersistencePropertiesMETA(Structure):
    def __init__(
        self,
        supports_space_persistence: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_SPACE_PERSISTENCE_PROPERTIES_META,
    ) -> None:
        super().__init__(
            supports_space_persistence=supports_space_persistence,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemSpacePersistencePropertiesMETA(supports_space_persistence={repr(self.supports_space_persistence)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemSpacePersistencePropertiesMETA(supports_space_persistence={self.supports_space_persistence}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_space_persistence", Bool32),
    ]


class SpacesSaveInfoMETA(Structure):
    def __init__(
        self,
        space_count: Optional[int] = None,
        spaces: ArrayFieldParamType[Space] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPACES_SAVE_INFO_META,
    ) -> None:
        space_count, spaces = array_field_helper(
            Space, space_count, spaces)
        super().__init__(
            space_count=space_count,
            _spaces=spaces,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpacesSaveInfoMETA(space_count={repr(self.space_count)}, spaces={repr(self._spaces)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpacesSaveInfoMETA(space_count={self.space_count}, spaces={self._spaces}, next={self.next}, type={self.type})"

    @property
    def spaces(self):
        if self.space_count == 0:
            return (Space * 0)()
        else:
            return (Space * self.space_count).from_address(
                ctypes.addressof(self._spaces.contents))

    @spaces.setter
    def spaces(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.space_count, self._spaces = array_field_helper(
            Space, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("space_count", c_uint32),
        ("_spaces", POINTER(Space)),
    ]


class EventDataSpacesSaveResultMETA(Structure):
    def __init__(
        self,
        request_id: AsyncRequestIdFB = 0,
        result: Result = Result(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_SPACES_SAVE_RESULT_META,
    ) -> None:
        super().__init__(
            request_id=request_id,
            result=Result(result).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataSpacesSaveResultMETA(request_id={repr(self.request_id)}, result={repr(self.result)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataSpacesSaveResultMETA(request_id={self.request_id}, result={self.result}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("request_id", AsyncRequestIdFB),
        ("result", Result.ctype()),
    ]


class SpacesEraseInfoMETA(Structure):
    def __init__(
        self,
        space_count: Optional[int] = None,
        spaces: ArrayFieldParamType[Space] = None,
        uuid_count: Optional[int] = None,
        uuids: ArrayFieldParamType[UuidEXT] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPACES_ERASE_INFO_META,
    ) -> None:
        space_count, spaces = array_field_helper(
            Space, space_count, spaces)
        uuid_count, uuids = array_field_helper(
            UuidEXT, uuid_count, uuids)
        super().__init__(
            space_count=space_count,
            _spaces=spaces,
            uuid_count=uuid_count,
            _uuids=uuids,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpacesEraseInfoMETA(space_count={repr(self.space_count)}, spaces={repr(self._spaces)}, uuid_count={repr(self.uuid_count)}, uuids={repr(self._uuids)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpacesEraseInfoMETA(space_count={self.space_count}, spaces={self._spaces}, uuid_count={self.uuid_count}, uuids={self._uuids}, next={self.next}, type={self.type})"

    @property
    def spaces(self):
        if self.space_count == 0:
            return (Space * 0)()
        else:
            return (Space * self.space_count).from_address(
                ctypes.addressof(self._spaces.contents))

    @spaces.setter
    def spaces(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.space_count, self._spaces = array_field_helper(
            Space, None, value)

    @property
    def uuids(self):
        if self.uuid_count == 0:
            return (UuidEXT * 0)()
        else:
            return (UuidEXT * self.uuid_count).from_address(
                ctypes.addressof(self._uuids.contents))

    @uuids.setter
    def uuids(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.uuid_count, self._uuids = array_field_helper(
            UuidEXT, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("space_count", c_uint32),
        ("_spaces", POINTER(Space)),
        ("uuid_count", c_uint32),
        ("_uuids", POINTER(UuidEXT)),
    ]


class EventDataSpacesEraseResultMETA(Structure):
    def __init__(
        self,
        request_id: AsyncRequestIdFB = 0,
        result: Result = Result(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_SPACES_ERASE_RESULT_META,
    ) -> None:
        super().__init__(
            request_id=request_id,
            result=Result(result).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataSpacesEraseResultMETA(request_id={repr(self.request_id)}, result={repr(self.result)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataSpacesEraseResultMETA(request_id={self.request_id}, result={self.result}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("request_id", AsyncRequestIdFB),
        ("result", Result.ctype()),
    ]


PFN_xrSaveSpacesMETA = CFUNCTYPE(Result.ctype(), Session, POINTER(SpacesSaveInfoMETA), POINTER(AsyncRequestIdFB))

PFN_xrEraseSpacesMETA = CFUNCTYPE(Result.ctype(), Session, POINTER(SpacesEraseInfoMETA), POINTER(AsyncRequestIdFB))


class PassthroughColorLutMETA_T(Structure):
    pass


class PassthroughColorLutMETA(POINTER(PassthroughColorLutMETA_T), HandleMixin):
    _type_ = PassthroughColorLutMETA_T  # ctypes idiosyncrasy


class PassthroughColorLutDataMETA(Structure):
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
        return f"xr.PassthroughColorLutDataMETA(buffer_size={repr(self.buffer_size)}, buffer={repr(self.buffer)})"

    def __str__(self) -> str:
        return f"xr.PassthroughColorLutDataMETA(buffer_size={self.buffer_size}, buffer={self.buffer})"

    _fields_ = [
        ("buffer_size", c_uint32),
        ("buffer", POINTER(c_uint8)),
    ]


class PassthroughColorLutCreateInfoMETA(Structure):
    def __init__(
        self,
        channels: PassthroughColorLutChannelsMETA = PassthroughColorLutChannelsMETA(),  # noqa
        resolution: int = 0,
        data: PassthroughColorLutDataMETA = None,
        next: c_void_p = None,
        type: StructureType = StructureType.PASSTHROUGH_COLOR_LUT_CREATE_INFO_META,
    ) -> None:
        if data is None:
            data = PassthroughColorLutDataMETA()
        super().__init__(
            channels=PassthroughColorLutChannelsMETA(channels).value,
            resolution=resolution,
            data=data,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PassthroughColorLutCreateInfoMETA(channels={repr(self.channels)}, resolution={repr(self.resolution)}, data={repr(self.data)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PassthroughColorLutCreateInfoMETA(channels={self.channels}, resolution={self.resolution}, data={self.data}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("channels", PassthroughColorLutChannelsMETA.ctype()),
        ("resolution", c_uint32),
        ("data", PassthroughColorLutDataMETA),
    ]


class PassthroughColorLutUpdateInfoMETA(Structure):
    def __init__(
        self,
        data: PassthroughColorLutDataMETA = None,
        next: c_void_p = None,
        type: StructureType = StructureType.PASSTHROUGH_COLOR_LUT_UPDATE_INFO_META,
    ) -> None:
        if data is None:
            data = PassthroughColorLutDataMETA()
        super().__init__(
            data=data,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PassthroughColorLutUpdateInfoMETA(data={repr(self.data)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PassthroughColorLutUpdateInfoMETA(data={self.data}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("data", PassthroughColorLutDataMETA),
    ]


class PassthroughColorMapLutMETA(Structure):
    def __init__(
        self,
        color_lut: PassthroughColorLutMETA = None,
        weight: float = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.PASSTHROUGH_COLOR_MAP_LUT_META,
    ) -> None:
        super().__init__(
            color_lut=color_lut,
            weight=weight,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PassthroughColorMapLutMETA(color_lut={repr(self.color_lut)}, weight={repr(self.weight)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PassthroughColorMapLutMETA(color_lut={self.color_lut}, weight={self.weight:.3f}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("color_lut", PassthroughColorLutMETA),
        ("weight", c_float),
    ]


class PassthroughColorMapInterpolatedLutMETA(Structure):
    def __init__(
        self,
        source_color_lut: PassthroughColorLutMETA = None,
        target_color_lut: PassthroughColorLutMETA = None,
        weight: float = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.PASSTHROUGH_COLOR_MAP_INTERPOLATED_LUT_META,
    ) -> None:
        super().__init__(
            source_color_lut=source_color_lut,
            target_color_lut=target_color_lut,
            weight=weight,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PassthroughColorMapInterpolatedLutMETA(source_color_lut={repr(self.source_color_lut)}, target_color_lut={repr(self.target_color_lut)}, weight={repr(self.weight)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PassthroughColorMapInterpolatedLutMETA(source_color_lut={self.source_color_lut}, target_color_lut={self.target_color_lut}, weight={self.weight:.3f}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("source_color_lut", PassthroughColorLutMETA),
        ("target_color_lut", PassthroughColorLutMETA),
        ("weight", c_float),
    ]


class SystemPassthroughColorLutPropertiesMETA(Structure):
    def __init__(
        self,
        max_color_lut_resolution: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_PASSTHROUGH_COLOR_LUT_PROPERTIES_META,
    ) -> None:
        super().__init__(
            max_color_lut_resolution=max_color_lut_resolution,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemPassthroughColorLutPropertiesMETA(max_color_lut_resolution={repr(self.max_color_lut_resolution)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemPassthroughColorLutPropertiesMETA(max_color_lut_resolution={self.max_color_lut_resolution}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("max_color_lut_resolution", c_uint32),
    ]


PFN_xrCreatePassthroughColorLutMETA = CFUNCTYPE(Result.ctype(), PassthroughFB, POINTER(PassthroughColorLutCreateInfoMETA), POINTER(PassthroughColorLutMETA))

PFN_xrDestroyPassthroughColorLutMETA = CFUNCTYPE(Result.ctype(), PassthroughColorLutMETA)

PFN_xrUpdatePassthroughColorLutMETA = CFUNCTYPE(Result.ctype(), PassthroughColorLutMETA, POINTER(PassthroughColorLutUpdateInfoMETA))


class SpaceTriangleMeshGetInfoMETA(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.SPACE_TRIANGLE_MESH_GET_INFO_META,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceTriangleMeshGetInfoMETA(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpaceTriangleMeshGetInfoMETA(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SpaceTriangleMeshMETA(Structure):
    def __init__(
        self,
        vertex_capacity_input: int = 0,
        vertex_count_output: int = 0,
        vertices: POINTER(Vector3f) = None,
        index_capacity_input: int = 0,
        index_count_output: int = 0,
        indices: POINTER(c_uint32) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPACE_TRIANGLE_MESH_META,
    ) -> None:
        super().__init__(
            vertex_capacity_input=vertex_capacity_input,
            vertex_count_output=vertex_count_output,
            vertices=vertices,
            index_capacity_input=index_capacity_input,
            index_count_output=index_count_output,
            indices=indices,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceTriangleMeshMETA(vertex_capacity_input={repr(self.vertex_capacity_input)}, vertex_count_output={repr(self.vertex_count_output)}, vertices={repr(self.vertices)}, index_capacity_input={repr(self.index_capacity_input)}, index_count_output={repr(self.index_count_output)}, indices={repr(self.indices)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpaceTriangleMeshMETA(vertex_capacity_input={self.vertex_capacity_input}, vertex_count_output={self.vertex_count_output}, vertices={self.vertices}, index_capacity_input={self.index_capacity_input}, index_count_output={self.index_count_output}, indices={self.indices}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("vertex_capacity_input", c_uint32),
        ("vertex_count_output", c_uint32),
        ("vertices", POINTER(Vector3f)),
        ("index_capacity_input", c_uint32),
        ("index_count_output", c_uint32),
        ("indices", POINTER(c_uint32)),
    ]


PFN_xrGetSpaceTriangleMeshMETA = CFUNCTYPE(Result.ctype(), Space, POINTER(SpaceTriangleMeshGetInfoMETA), POINTER(SpaceTriangleMeshMETA))


class SystemPropertiesBodyTrackingFullBodyMETA(Structure):
    def __init__(
        self,
        supports_full_body_tracking: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_PROPERTIES_BODY_TRACKING_FULL_BODY_META,
    ) -> None:
        super().__init__(
            supports_full_body_tracking=supports_full_body_tracking,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemPropertiesBodyTrackingFullBodyMETA(supports_full_body_tracking={repr(self.supports_full_body_tracking)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemPropertiesBodyTrackingFullBodyMETA(supports_full_body_tracking={self.supports_full_body_tracking}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_full_body_tracking", Bool32),
    ]


class EventDataPassthroughLayerResumedMETA(Structure):
    def __init__(
        self,
        layer: PassthroughLayerFB = None,
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_PASSTHROUGH_LAYER_RESUMED_META,
    ) -> None:
        super().__init__(
            layer=layer,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataPassthroughLayerResumedMETA(layer={repr(self.layer)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataPassthroughLayerResumedMETA(layer={self.layer}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer", PassthroughLayerFB),
    ]


class BodyTrackingCalibrationStatusMETA(Structure):
    def __init__(
        self,
        status: BodyTrackingCalibrationStateMETA = BodyTrackingCalibrationStateMETA(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.BODY_TRACKING_CALIBRATION_STATUS_META,
    ) -> None:
        super().__init__(
            status=BodyTrackingCalibrationStateMETA(status).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.BodyTrackingCalibrationStatusMETA(status={repr(self.status)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.BodyTrackingCalibrationStatusMETA(status={self.status}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("status", BodyTrackingCalibrationStateMETA.ctype()),
    ]


class BodyTrackingCalibrationInfoMETA(Structure):
    def __init__(
        self,
        body_height: float = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.BODY_TRACKING_CALIBRATION_INFO_META,
    ) -> None:
        super().__init__(
            body_height=body_height,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.BodyTrackingCalibrationInfoMETA(body_height={repr(self.body_height)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.BodyTrackingCalibrationInfoMETA(body_height={self.body_height:.3f}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("body_height", c_float),
    ]


class SystemPropertiesBodyTrackingCalibrationMETA(Structure):
    def __init__(
        self,
        supports_height_override: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_PROPERTIES_BODY_TRACKING_CALIBRATION_META,
    ) -> None:
        super().__init__(
            supports_height_override=supports_height_override,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemPropertiesBodyTrackingCalibrationMETA(supports_height_override={repr(self.supports_height_override)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemPropertiesBodyTrackingCalibrationMETA(supports_height_override={self.supports_height_override}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_height_override", Bool32),
    ]


PFN_xrSuggestBodyTrackingCalibrationOverrideMETA = CFUNCTYPE(Result.ctype(), BodyTrackerFB, POINTER(BodyTrackingCalibrationInfoMETA))

PFN_xrResetBodyTrackingCalibrationMETA = CFUNCTYPE(Result.ctype(), BodyTrackerFB)


class FaceTracker2FB_T(Structure):
    pass


class FaceTracker2FB(POINTER(FaceTracker2FB_T), HandleMixin):
    _type_ = FaceTracker2FB_T  # ctypes idiosyncrasy


class SystemFaceTrackingProperties2FB(Structure):
    def __init__(
        self,
        supports_visual_face_tracking: Bool32 = 0,
        supports_audio_face_tracking: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_FACE_TRACKING_PROPERTIES2_FB,
    ) -> None:
        super().__init__(
            supports_visual_face_tracking=supports_visual_face_tracking,
            supports_audio_face_tracking=supports_audio_face_tracking,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemFaceTrackingProperties2FB(supports_visual_face_tracking={repr(self.supports_visual_face_tracking)}, supports_audio_face_tracking={repr(self.supports_audio_face_tracking)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemFaceTrackingProperties2FB(supports_visual_face_tracking={self.supports_visual_face_tracking}, supports_audio_face_tracking={self.supports_audio_face_tracking}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_visual_face_tracking", Bool32),
        ("supports_audio_face_tracking", Bool32),
    ]


class FaceTrackerCreateInfo2FB(Structure):
    def __init__(
        self,
        face_expression_set: FaceExpressionSet2FB = FaceExpressionSet2FB(),  # noqa
        requested_data_source_count: Optional[int] = None,
        requested_data_sources: ArrayFieldParamType[FaceTrackingDataSource2FB.ctype()] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.FACE_TRACKER_CREATE_INFO2_FB,
    ) -> None:
        requested_data_source_count, requested_data_sources = array_field_helper(
            FaceTrackingDataSource2FB.ctype(), requested_data_source_count, requested_data_sources)
        super().__init__(
            face_expression_set=FaceExpressionSet2FB(face_expression_set).value,
            requested_data_source_count=requested_data_source_count,
            _requested_data_sources=requested_data_sources,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FaceTrackerCreateInfo2FB(face_expression_set={repr(self.face_expression_set)}, requested_data_source_count={repr(self.requested_data_source_count)}, requested_data_sources={repr(self._requested_data_sources)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FaceTrackerCreateInfo2FB(face_expression_set={self.face_expression_set}, requested_data_source_count={self.requested_data_source_count}, requested_data_sources={self._requested_data_sources}, next={self.next}, type={self.type})"

    @property
    def requested_data_sources(self):
        if self.requested_data_source_count == 0:
            return (FaceTrackingDataSource2FB.ctype() * 0)()
        else:
            return (FaceTrackingDataSource2FB.ctype() * self.requested_data_source_count).from_address(
                ctypes.addressof(self._requested_data_sources.contents))

    @requested_data_sources.setter
    def requested_data_sources(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.requested_data_source_count, self._requested_data_sources = array_field_helper(
            FaceTrackingDataSource2FB.ctype(), None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("face_expression_set", FaceExpressionSet2FB.ctype()),
        ("requested_data_source_count", c_uint32),
        ("_requested_data_sources", POINTER(FaceTrackingDataSource2FB.ctype())),
    ]


class FaceExpressionInfo2FB(Structure):
    def __init__(
        self,
        time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.FACE_EXPRESSION_INFO2_FB,
    ) -> None:
        super().__init__(
            time=time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FaceExpressionInfo2FB(time={repr(self.time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FaceExpressionInfo2FB(time={self.time}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("time", Time),
    ]


class FaceExpressionWeights2FB(Structure):
    def __init__(
        self,
        weight_count: Optional[int] = None,
        weights: ArrayFieldParamType[c_float] = None,
        confidence_count: Optional[int] = None,
        confidences: ArrayFieldParamType[c_float] = None,
        is_valid: Bool32 = 0,
        is_eye_following_blendshapes_valid: Bool32 = 0,
        data_source: FaceTrackingDataSource2FB = FaceTrackingDataSource2FB(),  # noqa
        time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.FACE_EXPRESSION_WEIGHTS2_FB,
    ) -> None:
        weight_count, weights = array_field_helper(
            c_float, weight_count, weights)
        confidence_count, confidences = array_field_helper(
            c_float, confidence_count, confidences)
        super().__init__(
            weight_count=weight_count,
            _weights=weights,
            confidence_count=confidence_count,
            _confidences=confidences,
            is_valid=is_valid,
            is_eye_following_blendshapes_valid=is_eye_following_blendshapes_valid,
            data_source=FaceTrackingDataSource2FB(data_source).value,
            time=time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FaceExpressionWeights2FB(weight_count={repr(self.weight_count)}, weights={repr(self._weights)}, confidence_count={repr(self.confidence_count)}, confidences={repr(self._confidences)}, is_valid={repr(self.is_valid)}, is_eye_following_blendshapes_valid={repr(self.is_eye_following_blendshapes_valid)}, data_source={repr(self.data_source)}, time={repr(self.time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FaceExpressionWeights2FB(weight_count={self.weight_count}, weights={self._weights}, confidence_count={self.confidence_count}, confidences={self._confidences}, is_valid={self.is_valid}, is_eye_following_blendshapes_valid={self.is_eye_following_blendshapes_valid}, data_source={self.data_source}, time={self.time}, next={self.next}, type={self.type})"

    @property
    def weights(self):
        if self.weight_count == 0:
            return (c_float * 0)()
        else:
            return (c_float * self.weight_count).from_address(
                ctypes.addressof(self._weights.contents))

    @weights.setter
    def weights(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.weight_count, self._weights = array_field_helper(
            c_float, None, value)

    @property
    def confidences(self):
        if self.confidence_count == 0:
            return (c_float * 0)()
        else:
            return (c_float * self.confidence_count).from_address(
                ctypes.addressof(self._confidences.contents))

    @confidences.setter
    def confidences(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.confidence_count, self._confidences = array_field_helper(
            c_float, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("weight_count", c_uint32),
        ("_weights", POINTER(c_float)),
        ("confidence_count", c_uint32),
        ("_confidences", POINTER(c_float)),
        ("is_valid", Bool32),
        ("is_eye_following_blendshapes_valid", Bool32),
        ("data_source", FaceTrackingDataSource2FB.ctype()),
        ("time", Time),
    ]


PFN_xrCreateFaceTracker2FB = CFUNCTYPE(Result.ctype(), Session, POINTER(FaceTrackerCreateInfo2FB), POINTER(FaceTracker2FB))

PFN_xrDestroyFaceTracker2FB = CFUNCTYPE(Result.ctype(), FaceTracker2FB)

PFN_xrGetFaceExpressionWeights2FB = CFUNCTYPE(Result.ctype(), FaceTracker2FB, POINTER(FaceExpressionInfo2FB), POINTER(FaceExpressionWeights2FB))


class SystemSpatialEntitySharingPropertiesMETA(Structure):
    def __init__(
        self,
        supports_spatial_entity_sharing: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_SPATIAL_ENTITY_SHARING_PROPERTIES_META,
    ) -> None:
        super().__init__(
            supports_spatial_entity_sharing=supports_spatial_entity_sharing,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemSpatialEntitySharingPropertiesMETA(supports_spatial_entity_sharing={repr(self.supports_spatial_entity_sharing)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemSpatialEntitySharingPropertiesMETA(supports_spatial_entity_sharing={self.supports_spatial_entity_sharing}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_spatial_entity_sharing", Bool32),
    ]


class ShareSpacesRecipientBaseHeaderMETA(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ShareSpacesRecipientBaseHeaderMETA(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ShareSpacesRecipientBaseHeaderMETA(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class ShareSpacesInfoMETA(Structure):
    def __init__(
        self,
        space_count: Optional[int] = None,
        spaces: ArrayFieldParamType[Space] = None,
        recipient_info: POINTER(ShareSpacesRecipientBaseHeaderMETA) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SHARE_SPACES_INFO_META,
    ) -> None:
        space_count, spaces = array_field_helper(
            Space, space_count, spaces)
        super().__init__(
            space_count=space_count,
            _spaces=spaces,
            recipient_info=recipient_info,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ShareSpacesInfoMETA(space_count={repr(self.space_count)}, spaces={repr(self._spaces)}, recipient_info={repr(self.recipient_info)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ShareSpacesInfoMETA(space_count={self.space_count}, spaces={self._spaces}, recipient_info={self.recipient_info}, next={self.next}, type={self.type})"

    @property
    def spaces(self):
        if self.space_count == 0:
            return (Space * 0)()
        else:
            return (Space * self.space_count).from_address(
                ctypes.addressof(self._spaces.contents))

    @spaces.setter
    def spaces(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.space_count, self._spaces = array_field_helper(
            Space, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("space_count", c_uint32),
        ("_spaces", POINTER(Space)),
        ("recipient_info", POINTER(ShareSpacesRecipientBaseHeaderMETA)),
    ]


class EventDataShareSpacesCompleteMETA(Structure):
    def __init__(
        self,
        request_id: AsyncRequestIdFB = 0,
        result: Result = Result(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_SHARE_SPACES_COMPLETE_META,
    ) -> None:
        super().__init__(
            request_id=request_id,
            result=Result(result).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataShareSpacesCompleteMETA(request_id={repr(self.request_id)}, result={repr(self.result)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataShareSpacesCompleteMETA(request_id={self.request_id}, result={self.result}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("request_id", AsyncRequestIdFB),
        ("result", Result.ctype()),
    ]


PFN_xrShareSpacesMETA = CFUNCTYPE(Result.ctype(), Session, POINTER(ShareSpacesInfoMETA), POINTER(AsyncRequestIdFB))


class EnvironmentDepthProviderMETA_T(Structure):
    pass


class EnvironmentDepthProviderMETA(POINTER(EnvironmentDepthProviderMETA_T), HandleMixin):
    _type_ = EnvironmentDepthProviderMETA_T  # ctypes idiosyncrasy


class EnvironmentDepthSwapchainMETA_T(Structure):
    pass


class EnvironmentDepthSwapchainMETA(POINTER(EnvironmentDepthSwapchainMETA_T), HandleMixin):
    _type_ = EnvironmentDepthSwapchainMETA_T  # ctypes idiosyncrasy

EnvironmentDepthProviderCreateFlagsMETACInt = Flags64

EnvironmentDepthSwapchainCreateFlagsMETACInt = Flags64


class EnvironmentDepthProviderCreateInfoMETA(Structure):
    def __init__(
        self,
        create_flags: EnvironmentDepthProviderCreateFlagsMETA = EnvironmentDepthProviderCreateFlagsMETA(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.ENVIRONMENT_DEPTH_PROVIDER_CREATE_INFO_META,
    ) -> None:
        super().__init__(
            create_flags=EnvironmentDepthProviderCreateFlagsMETA(create_flags).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EnvironmentDepthProviderCreateInfoMETA(create_flags={repr(self.create_flags)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EnvironmentDepthProviderCreateInfoMETA(create_flags={self.create_flags}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("create_flags", EnvironmentDepthProviderCreateFlagsMETACInt),
    ]


class EnvironmentDepthSwapchainCreateInfoMETA(Structure):
    def __init__(
        self,
        create_flags: EnvironmentDepthSwapchainCreateFlagsMETA = EnvironmentDepthSwapchainCreateFlagsMETA(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.ENVIRONMENT_DEPTH_SWAPCHAIN_CREATE_INFO_META,
    ) -> None:
        super().__init__(
            create_flags=EnvironmentDepthSwapchainCreateFlagsMETA(create_flags).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EnvironmentDepthSwapchainCreateInfoMETA(create_flags={repr(self.create_flags)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EnvironmentDepthSwapchainCreateInfoMETA(create_flags={self.create_flags}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("create_flags", EnvironmentDepthSwapchainCreateFlagsMETACInt),
    ]


class EnvironmentDepthSwapchainStateMETA(Structure):
    def __init__(
        self,
        width: int = 0,
        height: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.ENVIRONMENT_DEPTH_SWAPCHAIN_STATE_META,
    ) -> None:
        super().__init__(
            width=width,
            height=height,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EnvironmentDepthSwapchainStateMETA(width={repr(self.width)}, height={repr(self.height)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EnvironmentDepthSwapchainStateMETA(width={self.width}, height={self.height}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("width", c_uint32),
        ("height", c_uint32),
    ]


class EnvironmentDepthImageAcquireInfoMETA(Structure):
    def __init__(
        self,
        space: Space = None,
        display_time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.ENVIRONMENT_DEPTH_IMAGE_ACQUIRE_INFO_META,
    ) -> None:
        super().__init__(
            space=space,
            display_time=display_time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EnvironmentDepthImageAcquireInfoMETA(space={repr(self.space)}, display_time={repr(self.display_time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EnvironmentDepthImageAcquireInfoMETA(space={self.space}, display_time={self.display_time}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("space", Space),
        ("display_time", Time),
    ]


class EnvironmentDepthImageViewMETA(Structure):
    def __init__(
        self,
        fov: Fovf = None,
        pose: Posef = Posef(),
        next: c_void_p = None,
        type: StructureType = StructureType.ENVIRONMENT_DEPTH_IMAGE_VIEW_META,
    ) -> None:
        if fov is None:
            fov = Fovf()
        super().__init__(
            fov=fov,
            pose=pose,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EnvironmentDepthImageViewMETA(fov={repr(self.fov)}, pose={repr(self.pose)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EnvironmentDepthImageViewMETA(fov={self.fov}, pose={self.pose}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("fov", Fovf),
        ("pose", Posef),
    ]


class EnvironmentDepthImageMETA(Structure):
    def __init__(
        self,
        swapchain_index: int = 0,
        near_z: float = 0,
        far_z: float = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.ENVIRONMENT_DEPTH_IMAGE_META,
    ) -> None:
        super().__init__(
            swapchain_index=swapchain_index,
            near_z=near_z,
            far_z=far_z,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EnvironmentDepthImageMETA(swapchain_index={repr(self.swapchain_index)}, near_z={repr(self.near_z)}, far_z={repr(self.far_z)}, views={repr(self.views)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EnvironmentDepthImageMETA(swapchain_index={self.swapchain_index}, near_z={self.near_z:.3f}, far_z={self.far_z:.3f}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("swapchain_index", c_uint32),
        ("near_z", c_float),
        ("far_z", c_float),
        ("views", (EnvironmentDepthImageViewMETA * 2)),
    ]


class EnvironmentDepthHandRemovalSetInfoMETA(Structure):
    def __init__(
        self,
        enabled: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.ENVIRONMENT_DEPTH_HAND_REMOVAL_SET_INFO_META,
    ) -> None:
        super().__init__(
            enabled=enabled,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EnvironmentDepthHandRemovalSetInfoMETA(enabled={repr(self.enabled)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EnvironmentDepthHandRemovalSetInfoMETA(enabled={self.enabled}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("enabled", Bool32),
    ]


class SystemEnvironmentDepthPropertiesMETA(Structure):
    def __init__(
        self,
        supports_environment_depth: Bool32 = 0,
        supports_hand_removal: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_ENVIRONMENT_DEPTH_PROPERTIES_META,
    ) -> None:
        super().__init__(
            supports_environment_depth=supports_environment_depth,
            supports_hand_removal=supports_hand_removal,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemEnvironmentDepthPropertiesMETA(supports_environment_depth={repr(self.supports_environment_depth)}, supports_hand_removal={repr(self.supports_hand_removal)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemEnvironmentDepthPropertiesMETA(supports_environment_depth={self.supports_environment_depth}, supports_hand_removal={self.supports_hand_removal}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_environment_depth", Bool32),
        ("supports_hand_removal", Bool32),
    ]


PFN_xrCreateEnvironmentDepthProviderMETA = CFUNCTYPE(Result.ctype(), Session, POINTER(EnvironmentDepthProviderCreateInfoMETA), POINTER(EnvironmentDepthProviderMETA))

PFN_xrDestroyEnvironmentDepthProviderMETA = CFUNCTYPE(Result.ctype(), EnvironmentDepthProviderMETA)

PFN_xrStartEnvironmentDepthProviderMETA = CFUNCTYPE(Result.ctype(), EnvironmentDepthProviderMETA)

PFN_xrStopEnvironmentDepthProviderMETA = CFUNCTYPE(Result.ctype(), EnvironmentDepthProviderMETA)

PFN_xrCreateEnvironmentDepthSwapchainMETA = CFUNCTYPE(Result.ctype(), EnvironmentDepthProviderMETA, POINTER(EnvironmentDepthSwapchainCreateInfoMETA), POINTER(EnvironmentDepthSwapchainMETA))

PFN_xrDestroyEnvironmentDepthSwapchainMETA = CFUNCTYPE(Result.ctype(), EnvironmentDepthSwapchainMETA)

PFN_xrEnumerateEnvironmentDepthSwapchainImagesMETA = CFUNCTYPE(Result.ctype(), EnvironmentDepthSwapchainMETA, c_uint32, POINTER(c_uint32), POINTER(SwapchainImageBaseHeader))

PFN_xrGetEnvironmentDepthSwapchainStateMETA = CFUNCTYPE(Result.ctype(), EnvironmentDepthSwapchainMETA, POINTER(EnvironmentDepthSwapchainStateMETA))

PFN_xrAcquireEnvironmentDepthImageMETA = CFUNCTYPE(Result.ctype(), EnvironmentDepthProviderMETA, POINTER(EnvironmentDepthImageAcquireInfoMETA), POINTER(EnvironmentDepthImageMETA))

PFN_xrSetEnvironmentDepthHandRemovalMETA = CFUNCTYPE(Result.ctype(), EnvironmentDepthProviderMETA, POINTER(EnvironmentDepthHandRemovalSetInfoMETA))

RenderModelIdEXT = c_uint64


class RenderModelEXT_T(Structure):
    pass


class RenderModelEXT(POINTER(RenderModelEXT_T), HandleMixin):
    _type_ = RenderModelEXT_T  # ctypes idiosyncrasy


class RenderModelAssetEXT_T(Structure):
    pass


class RenderModelAssetEXT(POINTER(RenderModelAssetEXT_T), HandleMixin):
    _type_ = RenderModelAssetEXT_T  # ctypes idiosyncrasy


class RenderModelCreateInfoEXT(Structure):
    def __init__(
        self,
        render_model_id: RenderModelIdEXT = 0,
        gltf_extension_count: Optional[int] = None,
        gltf_extensions: StringArrayFieldParamType = None,
        next: c_void_p = None,
        type: StructureType = StructureType.RENDER_MODEL_CREATE_INFO_EXT,
    ) -> None:
        gltf_extension_count, gltf_extensions = string_array_field_helper(
            gltf_extension_count, gltf_extensions)
        super().__init__(
            render_model_id=render_model_id,
            gltf_extension_count=gltf_extension_count,
            _gltf_extensions=gltf_extensions,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.RenderModelCreateInfoEXT(render_model_id={repr(self.render_model_id)}, gltf_extension_count={repr(self.gltf_extension_count)}, gltf_extensions={repr(self._gltf_extensions)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.RenderModelCreateInfoEXT(render_model_id={self.render_model_id}, gltf_extension_count={self.gltf_extension_count}, gltf_extensions={self._gltf_extensions}, next={self.next}, type={self.type})"

    @property
    def gltf_extensions(self):
        if self.gltf_extension_count == 0:
            return (c_char_p * 0)()
        else:
            return (c_char_p * self.gltf_extension_count).from_address(
                ctypes.addressof(self._gltf_extensions.contents))

    @gltf_extensions.setter
    def gltf_extensions(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.gltf_extension_count, self._gltf_extensions = string_array_field_helper(
            None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("render_model_id", RenderModelIdEXT),
        ("gltf_extension_count", c_uint32),
        ("_gltf_extensions", POINTER(c_char_p)),
    ]


class RenderModelPropertiesGetInfoEXT(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.RENDER_MODEL_PROPERTIES_GET_INFO_EXT,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.RenderModelPropertiesGetInfoEXT(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.RenderModelPropertiesGetInfoEXT(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class RenderModelPropertiesEXT(Structure):
    def __init__(
        self,
        cache_id: UuidEXT = 0,
        animatable_node_count: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.RENDER_MODEL_PROPERTIES_EXT,
    ) -> None:
        super().__init__(
            cache_id=cache_id,
            animatable_node_count=animatable_node_count,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.RenderModelPropertiesEXT(cache_id={repr(self.cache_id)}, animatable_node_count={repr(self.animatable_node_count)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.RenderModelPropertiesEXT(cache_id={self.cache_id}, animatable_node_count={self.animatable_node_count}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("cache_id", UuidEXT),
        ("animatable_node_count", c_uint32),
    ]


class RenderModelSpaceCreateInfoEXT(Structure):
    def __init__(
        self,
        render_model: RenderModelEXT = None,
        next: c_void_p = None,
        type: StructureType = StructureType.RENDER_MODEL_SPACE_CREATE_INFO_EXT,
    ) -> None:
        super().__init__(
            render_model=render_model,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.RenderModelSpaceCreateInfoEXT(render_model={repr(self.render_model)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.RenderModelSpaceCreateInfoEXT(render_model={self.render_model}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("render_model", RenderModelEXT),
    ]


class RenderModelStateGetInfoEXT(Structure):
    def __init__(
        self,
        display_time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.RENDER_MODEL_STATE_GET_INFO_EXT,
    ) -> None:
        super().__init__(
            display_time=display_time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.RenderModelStateGetInfoEXT(display_time={repr(self.display_time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.RenderModelStateGetInfoEXT(display_time={self.display_time}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("display_time", Time),
    ]


class RenderModelNodeStateEXT(Structure):
    def __init__(
        self,
        node_pose: Posef = Posef(),
        is_visible: Bool32 = 0,
    ) -> None:
        super().__init__(
            node_pose=node_pose,
            is_visible=is_visible,
        )

    def __repr__(self) -> str:
        return f"xr.RenderModelNodeStateEXT(node_pose={repr(self.node_pose)}, is_visible={repr(self.is_visible)})"

    def __str__(self) -> str:
        return f"xr.RenderModelNodeStateEXT(node_pose={self.node_pose}, is_visible={self.is_visible})"

    _fields_ = [
        ("node_pose", Posef),
        ("is_visible", Bool32),
    ]


class RenderModelStateEXT(Structure):
    def __init__(
        self,
        node_state_count: Optional[int] = None,
        node_states: ArrayFieldParamType[RenderModelNodeStateEXT] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.RENDER_MODEL_STATE_EXT,
    ) -> None:
        node_state_count, node_states = array_field_helper(
            RenderModelNodeStateEXT, node_state_count, node_states)
        super().__init__(
            node_state_count=node_state_count,
            _node_states=node_states,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.RenderModelStateEXT(node_state_count={repr(self.node_state_count)}, node_states={repr(self._node_states)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.RenderModelStateEXT(node_state_count={self.node_state_count}, node_states={self._node_states}, next={self.next}, type={self.type})"

    @property
    def node_states(self):
        if self.node_state_count == 0:
            return (RenderModelNodeStateEXT * 0)()
        else:
            return (RenderModelNodeStateEXT * self.node_state_count).from_address(
                ctypes.addressof(self._node_states.contents))

    @node_states.setter
    def node_states(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.node_state_count, self._node_states = array_field_helper(
            RenderModelNodeStateEXT, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("node_state_count", c_uint32),
        ("_node_states", POINTER(RenderModelNodeStateEXT)),
    ]


class RenderModelAssetCreateInfoEXT(Structure):
    def __init__(
        self,
        cache_id: UuidEXT = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.RENDER_MODEL_ASSET_CREATE_INFO_EXT,
    ) -> None:
        super().__init__(
            cache_id=cache_id,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.RenderModelAssetCreateInfoEXT(cache_id={repr(self.cache_id)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.RenderModelAssetCreateInfoEXT(cache_id={self.cache_id}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("cache_id", UuidEXT),
    ]


class RenderModelAssetDataGetInfoEXT(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.RENDER_MODEL_ASSET_DATA_GET_INFO_EXT,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.RenderModelAssetDataGetInfoEXT(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.RenderModelAssetDataGetInfoEXT(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class RenderModelAssetDataEXT(Structure):
    def __init__(
        self,
        buffer_capacity_input: int = 0,
        buffer_count_output: int = 0,
        buffer: POINTER(c_uint8) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.RENDER_MODEL_ASSET_DATA_EXT,
    ) -> None:
        super().__init__(
            buffer_capacity_input=buffer_capacity_input,
            buffer_count_output=buffer_count_output,
            buffer=buffer,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.RenderModelAssetDataEXT(buffer_capacity_input={repr(self.buffer_capacity_input)}, buffer_count_output={repr(self.buffer_count_output)}, buffer={repr(self.buffer)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.RenderModelAssetDataEXT(buffer_capacity_input={self.buffer_capacity_input}, buffer_count_output={self.buffer_count_output}, buffer={self.buffer}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("buffer_capacity_input", c_uint32),
        ("buffer_count_output", c_uint32),
        ("buffer", POINTER(c_uint8)),
    ]


class RenderModelAssetPropertiesGetInfoEXT(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.RENDER_MODEL_ASSET_PROPERTIES_GET_INFO_EXT,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.RenderModelAssetPropertiesGetInfoEXT(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.RenderModelAssetPropertiesGetInfoEXT(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class RenderModelAssetNodePropertiesEXT(Structure):
    def __init__(
        self,
        unique_name: str = "",
    ) -> None:
        super().__init__(
            unique_name=unique_name.encode(),
        )

    def __repr__(self) -> str:
        return f"xr.RenderModelAssetNodePropertiesEXT(unique_name={repr(self.unique_name)})"

    def __str__(self) -> str:
        return f"xr.RenderModelAssetNodePropertiesEXT(unique_name={self.unique_name})"

    _fields_ = [
        ("unique_name", (c_char * 64)),
    ]


class RenderModelAssetPropertiesEXT(Structure):
    def __init__(
        self,
        node_property_count: int = 0,
        node_properties: POINTER(RenderModelAssetNodePropertiesEXT) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.RENDER_MODEL_ASSET_PROPERTIES_EXT,
    ) -> None:
        super().__init__(
            node_property_count=node_property_count,
            node_properties=node_properties,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.RenderModelAssetPropertiesEXT(node_property_count={repr(self.node_property_count)}, node_properties={repr(self.node_properties)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.RenderModelAssetPropertiesEXT(node_property_count={self.node_property_count}, node_properties={self.node_properties}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("node_property_count", c_uint32),
        ("node_properties", POINTER(RenderModelAssetNodePropertiesEXT)),
    ]


PFN_xrCreateRenderModelEXT = CFUNCTYPE(Result.ctype(), Session, POINTER(RenderModelCreateInfoEXT), POINTER(RenderModelEXT))

PFN_xrDestroyRenderModelEXT = CFUNCTYPE(Result.ctype(), RenderModelEXT)

PFN_xrGetRenderModelPropertiesEXT = CFUNCTYPE(Result.ctype(), RenderModelEXT, POINTER(RenderModelPropertiesGetInfoEXT), POINTER(RenderModelPropertiesEXT))

PFN_xrCreateRenderModelSpaceEXT = CFUNCTYPE(Result.ctype(), Session, POINTER(RenderModelSpaceCreateInfoEXT), POINTER(Space))

PFN_xrCreateRenderModelAssetEXT = CFUNCTYPE(Result.ctype(), Session, POINTER(RenderModelAssetCreateInfoEXT), POINTER(RenderModelAssetEXT))

PFN_xrDestroyRenderModelAssetEXT = CFUNCTYPE(Result.ctype(), RenderModelAssetEXT)

PFN_xrGetRenderModelAssetDataEXT = CFUNCTYPE(Result.ctype(), RenderModelAssetEXT, POINTER(RenderModelAssetDataGetInfoEXT), POINTER(RenderModelAssetDataEXT))

PFN_xrGetRenderModelAssetPropertiesEXT = CFUNCTYPE(Result.ctype(), RenderModelAssetEXT, POINTER(RenderModelAssetPropertiesGetInfoEXT), POINTER(RenderModelAssetPropertiesEXT))

PFN_xrGetRenderModelStateEXT = CFUNCTYPE(Result.ctype(), RenderModelEXT, POINTER(RenderModelStateGetInfoEXT), POINTER(RenderModelStateEXT))


class InteractionRenderModelIdsEnumerateInfoEXT(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.INTERACTION_RENDER_MODEL_IDS_ENUMERATE_INFO_EXT,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.InteractionRenderModelIdsEnumerateInfoEXT(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.InteractionRenderModelIdsEnumerateInfoEXT(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class InteractionRenderModelSubactionPathInfoEXT(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.INTERACTION_RENDER_MODEL_SUBACTION_PATH_INFO_EXT,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.InteractionRenderModelSubactionPathInfoEXT(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.InteractionRenderModelSubactionPathInfoEXT(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class InteractionRenderModelTopLevelUserPathGetInfoEXT(Structure):
    def __init__(
        self,
        top_level_user_path_count: Optional[int] = None,
        top_level_user_paths: ArrayFieldParamType[c_uint64] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.INTERACTION_RENDER_MODEL_TOP_LEVEL_USER_PATH_GET_INFO_EXT,
    ) -> None:
        top_level_user_path_count, top_level_user_paths = array_field_helper(
            c_uint64, top_level_user_path_count, top_level_user_paths)
        super().__init__(
            top_level_user_path_count=top_level_user_path_count,
            _top_level_user_paths=top_level_user_paths,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.InteractionRenderModelTopLevelUserPathGetInfoEXT(top_level_user_path_count={repr(self.top_level_user_path_count)}, top_level_user_paths={repr(self._top_level_user_paths)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.InteractionRenderModelTopLevelUserPathGetInfoEXT(top_level_user_path_count={self.top_level_user_path_count}, top_level_user_paths={self._top_level_user_paths}, next={self.next}, type={self.type})"

    @property
    def top_level_user_paths(self):
        if self.top_level_user_path_count == 0:
            return (c_uint64 * 0)()
        else:
            return (c_uint64 * self.top_level_user_path_count).from_address(
                ctypes.addressof(self._top_level_user_paths.contents))

    @top_level_user_paths.setter
    def top_level_user_paths(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.top_level_user_path_count, self._top_level_user_paths = array_field_helper(
            c_uint64, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("top_level_user_path_count", c_uint32),
        ("_top_level_user_paths", POINTER(c_uint64)),
    ]


class EventDataInteractionRenderModelsChangedEXT(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_INTERACTION_RENDER_MODELS_CHANGED_EXT,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataInteractionRenderModelsChangedEXT(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataInteractionRenderModelsChangedEXT(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


PFN_xrEnumerateInteractionRenderModelIdsEXT = CFUNCTYPE(Result.ctype(), Session, POINTER(InteractionRenderModelIdsEnumerateInfoEXT), c_uint32, POINTER(c_uint32), POINTER(RenderModelIdEXT))

PFN_xrEnumerateRenderModelSubactionPathsEXT = CFUNCTYPE(Result.ctype(), RenderModelEXT, POINTER(InteractionRenderModelSubactionPathInfoEXT), c_uint32, POINTER(c_uint32), POINTER(Path))

PFN_xrGetRenderModelPoseTopLevelUserPathEXT = CFUNCTYPE(Result.ctype(), RenderModelEXT, POINTER(InteractionRenderModelTopLevelUserPathGetInfoEXT), POINTER(Path))

PFN_xrSetTrackingOptimizationSettingsHintQCOM = CFUNCTYPE(Result.ctype(), Session, TrackingOptimizationSettingsDomainQCOM.ctype(), TrackingOptimizationSettingsHintQCOM.ctype())


class PassthroughHTC_T(Structure):
    pass


class PassthroughHTC(POINTER(PassthroughHTC_T), HandleMixin):
    _type_ = PassthroughHTC_T  # ctypes idiosyncrasy


class PassthroughCreateInfoHTC(Structure):
    def __init__(
        self,
        form: PassthroughFormHTC = PassthroughFormHTC(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.PASSTHROUGH_CREATE_INFO_HTC,
    ) -> None:
        super().__init__(
            form=PassthroughFormHTC(form).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PassthroughCreateInfoHTC(form={repr(self.form)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PassthroughCreateInfoHTC(form={self.form}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("form", PassthroughFormHTC.ctype()),
    ]


class PassthroughColorHTC(Structure):
    def __init__(
        self,
        alpha: float = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.PASSTHROUGH_COLOR_HTC,
    ) -> None:
        super().__init__(
            alpha=alpha,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PassthroughColorHTC(alpha={repr(self.alpha)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PassthroughColorHTC(alpha={self.alpha:.3f}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("alpha", c_float),
    ]


class PassthroughMeshTransformInfoHTC(Structure):
    def __init__(
        self,
        vertex_count: int = 0,
        vertices: POINTER(Vector3f) = None,
        index_count: int = 0,
        indices: POINTER(c_uint32) = None,
        base_space: Space = None,
        time: Time = 0,
        pose: Posef = Posef(),
        scale: Vector3f = None,
        next: c_void_p = None,
        type: StructureType = StructureType.PASSTHROUGH_MESH_TRANSFORM_INFO_HTC,
    ) -> None:
        if scale is None:
            scale = Vector3f()
        super().__init__(
            vertex_count=vertex_count,
            vertices=vertices,
            index_count=index_count,
            indices=indices,
            base_space=base_space,
            time=time,
            pose=pose,
            scale=scale,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PassthroughMeshTransformInfoHTC(vertex_count={repr(self.vertex_count)}, vertices={repr(self.vertices)}, index_count={repr(self.index_count)}, indices={repr(self.indices)}, base_space={repr(self.base_space)}, time={repr(self.time)}, pose={repr(self.pose)}, scale={repr(self.scale)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PassthroughMeshTransformInfoHTC(vertex_count={self.vertex_count}, vertices={self.vertices}, index_count={self.index_count}, indices={self.indices}, base_space={self.base_space}, time={self.time}, pose={self.pose}, scale={self.scale}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("vertex_count", c_uint32),
        ("vertices", POINTER(Vector3f)),
        ("index_count", c_uint32),
        ("indices", POINTER(c_uint32)),
        ("base_space", Space),
        ("time", Time),
        ("pose", Posef),
        ("scale", Vector3f),
    ]


class CompositionLayerPassthroughHTC(Structure):
    def __init__(
        self,
        layer_flags: CompositionLayerFlags = CompositionLayerFlags(),  # noqa
        space: Space = None,
        passthrough: PassthroughHTC = None,
        color: PassthroughColorHTC = None,
        next: c_void_p = None,
        type: StructureType = StructureType.COMPOSITION_LAYER_PASSTHROUGH_HTC,
    ) -> None:
        if color is None:
            color = PassthroughColorHTC()
        super().__init__(
            layer_flags=CompositionLayerFlags(layer_flags).value,
            space=space,
            passthrough=passthrough,
            color=color,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CompositionLayerPassthroughHTC(layer_flags={repr(self.layer_flags)}, space={repr(self.space)}, passthrough={repr(self.passthrough)}, color={repr(self.color)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CompositionLayerPassthroughHTC(layer_flags={self.layer_flags}, space={self.space}, passthrough={self.passthrough}, color={self.color}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("layer_flags", CompositionLayerFlagsCInt),
        ("space", Space),
        ("passthrough", PassthroughHTC),
        ("color", PassthroughColorHTC),
    ]


PFN_xrCreatePassthroughHTC = CFUNCTYPE(Result.ctype(), Session, POINTER(PassthroughCreateInfoHTC), POINTER(PassthroughHTC))

PFN_xrDestroyPassthroughHTC = CFUNCTYPE(Result.ctype(), PassthroughHTC)

FoveationDynamicFlagsHTCCInt = Flags64


class FoveationApplyInfoHTC(Structure):
    def __init__(
        self,
        mode: FoveationModeHTC = FoveationModeHTC(),  # noqa
        sub_image_count: Optional[int] = None,
        sub_images: ArrayFieldParamType[SwapchainSubImage] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.FOVEATION_APPLY_INFO_HTC,
    ) -> None:
        sub_image_count, sub_images = array_field_helper(
            SwapchainSubImage, sub_image_count, sub_images)
        super().__init__(
            mode=FoveationModeHTC(mode).value,
            sub_image_count=sub_image_count,
            _sub_images=sub_images,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FoveationApplyInfoHTC(mode={repr(self.mode)}, sub_image_count={repr(self.sub_image_count)}, sub_images={repr(self._sub_images)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FoveationApplyInfoHTC(mode={self.mode}, sub_image_count={self.sub_image_count}, sub_images={self._sub_images}, next={self.next}, type={self.type})"

    @property
    def sub_images(self):
        if self.sub_image_count == 0:
            return (SwapchainSubImage * 0)()
        else:
            return (SwapchainSubImage * self.sub_image_count).from_address(
                ctypes.addressof(self._sub_images.contents))

    @sub_images.setter
    def sub_images(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.sub_image_count, self._sub_images = array_field_helper(
            SwapchainSubImage, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("mode", FoveationModeHTC.ctype()),
        ("sub_image_count", c_uint32),
        ("_sub_images", POINTER(SwapchainSubImage)),
    ]


class FoveationConfigurationHTC(Structure):
    def __init__(
        self,
        level: FoveationLevelHTC = FoveationLevelHTC(),  # noqa
        clear_fov_degree: float = 0,
        focal_center_offset: Vector2f = None,
    ) -> None:
        if focal_center_offset is None:
            focal_center_offset = Vector2f()
        super().__init__(
            level=FoveationLevelHTC(level).value,
            clear_fov_degree=clear_fov_degree,
            focal_center_offset=focal_center_offset,
        )

    def __repr__(self) -> str:
        return f"xr.FoveationConfigurationHTC(level={repr(self.level)}, clear_fov_degree={repr(self.clear_fov_degree)}, focal_center_offset={repr(self.focal_center_offset)})"

    def __str__(self) -> str:
        return f"xr.FoveationConfigurationHTC(level={self.level}, clear_fov_degree={self.clear_fov_degree:.3f}, focal_center_offset={self.focal_center_offset})"

    _fields_ = [
        ("level", FoveationLevelHTC.ctype()),
        ("clear_fov_degree", c_float),
        ("focal_center_offset", Vector2f),
    ]


class FoveationDynamicModeInfoHTC(Structure):
    def __init__(
        self,
        dynamic_flags: FoveationDynamicFlagsHTC = FoveationDynamicFlagsHTC(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.FOVEATION_DYNAMIC_MODE_INFO_HTC,
    ) -> None:
        super().__init__(
            dynamic_flags=FoveationDynamicFlagsHTC(dynamic_flags).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FoveationDynamicModeInfoHTC(dynamic_flags={repr(self.dynamic_flags)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FoveationDynamicModeInfoHTC(dynamic_flags={self.dynamic_flags}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("dynamic_flags", FoveationDynamicFlagsHTCCInt),
    ]


class FoveationCustomModeInfoHTC(Structure):
    def __init__(
        self,
        config_count: Optional[int] = None,
        configs: ArrayFieldParamType[FoveationConfigurationHTC] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.FOVEATION_CUSTOM_MODE_INFO_HTC,
    ) -> None:
        config_count, configs = array_field_helper(
            FoveationConfigurationHTC, config_count, configs)
        super().__init__(
            config_count=config_count,
            _configs=configs,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FoveationCustomModeInfoHTC(config_count={repr(self.config_count)}, configs={repr(self._configs)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FoveationCustomModeInfoHTC(config_count={self.config_count}, configs={self._configs}, next={self.next}, type={self.type})"

    @property
    def configs(self):
        if self.config_count == 0:
            return (FoveationConfigurationHTC * 0)()
        else:
            return (FoveationConfigurationHTC * self.config_count).from_address(
                ctypes.addressof(self._configs.contents))

    @configs.setter
    def configs(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.config_count, self._configs = array_field_helper(
            FoveationConfigurationHTC, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("config_count", c_uint32),
        ("_configs", POINTER(FoveationConfigurationHTC)),
    ]


PFN_xrApplyFoveationHTC = CFUNCTYPE(Result.ctype(), Session, POINTER(FoveationApplyInfoHTC))


class SystemAnchorPropertiesHTC(Structure):
    def __init__(
        self,
        supports_anchor: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_ANCHOR_PROPERTIES_HTC,
    ) -> None:
        super().__init__(
            supports_anchor=supports_anchor,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemAnchorPropertiesHTC(supports_anchor={repr(self.supports_anchor)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemAnchorPropertiesHTC(supports_anchor={self.supports_anchor}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_anchor", Bool32),
    ]


class SpatialAnchorNameHTC(Structure):
    def __init__(
        self,
        name: str = "",
    ) -> None:
        super().__init__(
            name=name.encode(),
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorNameHTC(name={repr(self.name)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorNameHTC(name={self.name})"

    _fields_ = [
        ("name", (c_char * 256)),
    ]


class SpatialAnchorCreateInfoHTC(Structure):
    def __init__(
        self,
        space: Space = None,
        pose_in_space: Posef = Posef(),
        name: SpatialAnchorNameHTC = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHOR_CREATE_INFO_HTC,
    ) -> None:
        if name is None:
            name = SpatialAnchorNameHTC()
        super().__init__(
            space=space,
            pose_in_space=pose_in_space,
            name=name,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorCreateInfoHTC(space={repr(self.space)}, pose_in_space={repr(self.pose_in_space)}, name={repr(self.name)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorCreateInfoHTC(space={self.space}, pose_in_space={self.pose_in_space}, name={self.name}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("space", Space),
        ("pose_in_space", Posef),
        ("name", SpatialAnchorNameHTC),
    ]


PFN_xrCreateSpatialAnchorHTC = CFUNCTYPE(Result.ctype(), Session, POINTER(SpatialAnchorCreateInfoHTC), POINTER(Space))

PFN_xrGetSpatialAnchorNameHTC = CFUNCTYPE(Result.ctype(), Space, POINTER(SpatialAnchorNameHTC))


class BodyTrackerHTC_T(Structure):
    pass


class BodyTrackerHTC(POINTER(BodyTrackerHTC_T), HandleMixin):
    _type_ = BodyTrackerHTC_T  # ctypes idiosyncrasy


class SystemBodyTrackingPropertiesHTC(Structure):
    def __init__(
        self,
        supports_body_tracking: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_BODY_TRACKING_PROPERTIES_HTC,
    ) -> None:
        super().__init__(
            supports_body_tracking=supports_body_tracking,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemBodyTrackingPropertiesHTC(supports_body_tracking={repr(self.supports_body_tracking)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemBodyTrackingPropertiesHTC(supports_body_tracking={self.supports_body_tracking}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_body_tracking", Bool32),
    ]


class BodyTrackerCreateInfoHTC(Structure):
    def __init__(
        self,
        body_joint_set: BodyJointSetHTC = BodyJointSetHTC(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.BODY_TRACKER_CREATE_INFO_HTC,
    ) -> None:
        super().__init__(
            body_joint_set=BodyJointSetHTC(body_joint_set).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.BodyTrackerCreateInfoHTC(body_joint_set={repr(self.body_joint_set)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.BodyTrackerCreateInfoHTC(body_joint_set={self.body_joint_set}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("body_joint_set", BodyJointSetHTC.ctype()),
    ]


class BodyJointsLocateInfoHTC(Structure):
    def __init__(
        self,
        base_space: Space = None,
        time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.BODY_JOINTS_LOCATE_INFO_HTC,
    ) -> None:
        super().__init__(
            base_space=base_space,
            time=time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.BodyJointsLocateInfoHTC(base_space={repr(self.base_space)}, time={repr(self.time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.BodyJointsLocateInfoHTC(base_space={self.base_space}, time={self.time}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("base_space", Space),
        ("time", Time),
    ]


class BodyJointLocationHTC(Structure):
    def __init__(
        self,
        location_flags: SpaceLocationFlags = SpaceLocationFlags(),  # noqa
        pose: Posef = Posef(),
    ) -> None:
        super().__init__(
            location_flags=SpaceLocationFlags(location_flags).value,
            pose=pose,
        )

    def __repr__(self) -> str:
        return f"xr.BodyJointLocationHTC(location_flags={repr(self.location_flags)}, pose={repr(self.pose)})"

    def __str__(self) -> str:
        return f"xr.BodyJointLocationHTC(location_flags={self.location_flags}, pose={self.pose})"

    _fields_ = [
        ("location_flags", SpaceLocationFlagsCInt),
        ("pose", Posef),
    ]


class BodyJointLocationsHTC(Structure):
    def __init__(
        self,
        combined_location_flags: SpaceLocationFlags = SpaceLocationFlags(),  # noqa
        confidence_level: BodyJointConfidenceHTC = BodyJointConfidenceHTC(),  # noqa
        joint_location_count: Optional[int] = None,
        joint_locations: ArrayFieldParamType[BodyJointLocationHTC] = None,
        skeleton_generation_id: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.BODY_JOINT_LOCATIONS_HTC,
    ) -> None:
        joint_location_count, joint_locations = array_field_helper(
            BodyJointLocationHTC, joint_location_count, joint_locations)
        super().__init__(
            combined_location_flags=SpaceLocationFlags(combined_location_flags).value,
            confidence_level=BodyJointConfidenceHTC(confidence_level).value,
            joint_location_count=joint_location_count,
            _joint_locations=joint_locations,
            skeleton_generation_id=skeleton_generation_id,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.BodyJointLocationsHTC(combined_location_flags={repr(self.combined_location_flags)}, confidence_level={repr(self.confidence_level)}, joint_location_count={repr(self.joint_location_count)}, joint_locations={repr(self._joint_locations)}, skeleton_generation_id={repr(self.skeleton_generation_id)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.BodyJointLocationsHTC(combined_location_flags={self.combined_location_flags}, confidence_level={self.confidence_level}, joint_location_count={self.joint_location_count}, joint_locations={self._joint_locations}, skeleton_generation_id={self.skeleton_generation_id}, next={self.next}, type={self.type})"

    @property
    def joint_locations(self):
        if self.joint_location_count == 0:
            return (BodyJointLocationHTC * 0)()
        else:
            return (BodyJointLocationHTC * self.joint_location_count).from_address(
                ctypes.addressof(self._joint_locations.contents))

    @joint_locations.setter
    def joint_locations(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.joint_location_count, self._joint_locations = array_field_helper(
            BodyJointLocationHTC, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("combined_location_flags", SpaceLocationFlagsCInt),
        ("confidence_level", BodyJointConfidenceHTC.ctype()),
        ("joint_location_count", c_uint32),
        ("_joint_locations", POINTER(BodyJointLocationHTC)),
        ("skeleton_generation_id", c_uint32),
    ]


class BodySkeletonJointHTC(Structure):
    def __init__(
        self,
        pose: Posef = Posef(),
    ) -> None:
        super().__init__(
            pose=pose,
        )

    def __repr__(self) -> str:
        return f"xr.BodySkeletonJointHTC(pose={repr(self.pose)})"

    def __str__(self) -> str:
        return f"xr.BodySkeletonJointHTC(pose={self.pose})"

    _fields_ = [
        ("pose", Posef),
    ]


class BodySkeletonHTC(Structure):
    def __init__(
        self,
        joint_count: Optional[int] = None,
        joints: ArrayFieldParamType[BodySkeletonJointHTC] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.BODY_SKELETON_HTC,
    ) -> None:
        joint_count, joints = array_field_helper(
            BodySkeletonJointHTC, joint_count, joints)
        super().__init__(
            joint_count=joint_count,
            _joints=joints,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.BodySkeletonHTC(joint_count={repr(self.joint_count)}, joints={repr(self._joints)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.BodySkeletonHTC(joint_count={self.joint_count}, joints={self._joints}, next={self.next}, type={self.type})"

    @property
    def joints(self):
        if self.joint_count == 0:
            return (BodySkeletonJointHTC * 0)()
        else:
            return (BodySkeletonJointHTC * self.joint_count).from_address(
                ctypes.addressof(self._joints.contents))

    @joints.setter
    def joints(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.joint_count, self._joints = array_field_helper(
            BodySkeletonJointHTC, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("joint_count", c_uint32),
        ("_joints", POINTER(BodySkeletonJointHTC)),
    ]


PFN_xrCreateBodyTrackerHTC = CFUNCTYPE(Result.ctype(), Session, POINTER(BodyTrackerCreateInfoHTC), POINTER(BodyTrackerHTC))

PFN_xrDestroyBodyTrackerHTC = CFUNCTYPE(Result.ctype(), BodyTrackerHTC)

PFN_xrLocateBodyJointsHTC = CFUNCTYPE(Result.ctype(), BodyTrackerHTC, POINTER(BodyJointsLocateInfoHTC), POINTER(BodyJointLocationsHTC))

PFN_xrGetBodySkeletonHTC = CFUNCTYPE(Result.ctype(), BodyTrackerHTC, Space, c_uint32, POINTER(BodySkeletonHTC))


class ActiveActionSetPriorityEXT(Structure):
    def __init__(
        self,
        action_set: ActionSet = None,
        priority_override: int = 0,
    ) -> None:
        super().__init__(
            action_set=action_set,
            priority_override=priority_override,
        )

    def __repr__(self) -> str:
        return f"xr.ActiveActionSetPriorityEXT(action_set={repr(self.action_set)}, priority_override={repr(self.priority_override)})"

    def __str__(self) -> str:
        return f"xr.ActiveActionSetPriorityEXT(action_set={self.action_set}, priority_override={self.priority_override})"

    _fields_ = [
        ("action_set", ActionSet),
        ("priority_override", c_uint32),
    ]


class ActiveActionSetPrioritiesEXT(Structure):
    def __init__(
        self,
        action_set_priority_count: int = 0,
        action_set_priorities: POINTER(ActiveActionSetPriorityEXT) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.ACTIVE_ACTION_SET_PRIORITIES_EXT,
    ) -> None:
        super().__init__(
            action_set_priority_count=action_set_priority_count,
            action_set_priorities=action_set_priorities,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ActiveActionSetPrioritiesEXT(action_set_priority_count={repr(self.action_set_priority_count)}, action_set_priorities={repr(self.action_set_priorities)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ActiveActionSetPrioritiesEXT(action_set_priority_count={self.action_set_priority_count}, action_set_priorities={self.action_set_priorities}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("action_set_priority_count", c_uint32),
        ("action_set_priorities", POINTER(ActiveActionSetPriorityEXT)),
    ]


class SystemForceFeedbackCurlPropertiesMNDX(Structure):
    def __init__(
        self,
        supports_force_feedback_curl: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_FORCE_FEEDBACK_CURL_PROPERTIES_MNDX,
    ) -> None:
        super().__init__(
            supports_force_feedback_curl=supports_force_feedback_curl,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemForceFeedbackCurlPropertiesMNDX(supports_force_feedback_curl={repr(self.supports_force_feedback_curl)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemForceFeedbackCurlPropertiesMNDX(supports_force_feedback_curl={self.supports_force_feedback_curl}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_force_feedback_curl", Bool32),
    ]


class ForceFeedbackCurlApplyLocationMNDX(Structure):
    def __init__(
        self,
        location: ForceFeedbackCurlLocationMNDX = ForceFeedbackCurlLocationMNDX(),  # noqa
        value: float = 0,
    ) -> None:
        super().__init__(
            location=ForceFeedbackCurlLocationMNDX(location).value,
            value=value,
        )

    def __repr__(self) -> str:
        return f"xr.ForceFeedbackCurlApplyLocationMNDX(location={repr(self.location)}, value={repr(self.value)})"

    def __str__(self) -> str:
        return f"xr.ForceFeedbackCurlApplyLocationMNDX(location={self.location}, value={self.value:.3f})"

    _fields_ = [
        ("location", ForceFeedbackCurlLocationMNDX.ctype()),
        ("value", c_float),
    ]


class ForceFeedbackCurlApplyLocationsMNDX(Structure):
    def __init__(
        self,
        location_count: Optional[int] = None,
        locations: ArrayFieldParamType[ForceFeedbackCurlApplyLocationMNDX] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.FORCE_FEEDBACK_CURL_APPLY_LOCATIONS_MNDX,
    ) -> None:
        location_count, locations = array_field_helper(
            ForceFeedbackCurlApplyLocationMNDX, location_count, locations)
        super().__init__(
            location_count=location_count,
            _locations=locations,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ForceFeedbackCurlApplyLocationsMNDX(location_count={repr(self.location_count)}, locations={repr(self._locations)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ForceFeedbackCurlApplyLocationsMNDX(location_count={self.location_count}, locations={self._locations}, next={self.next}, type={self.type})"

    @property
    def locations(self):
        if self.location_count == 0:
            return (ForceFeedbackCurlApplyLocationMNDX * 0)()
        else:
            return (ForceFeedbackCurlApplyLocationMNDX * self.location_count).from_address(
                ctypes.addressof(self._locations.contents))

    @locations.setter
    def locations(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.location_count, self._locations = array_field_helper(
            ForceFeedbackCurlApplyLocationMNDX, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("location_count", c_uint32),
        ("_locations", POINTER(ForceFeedbackCurlApplyLocationMNDX)),
    ]


PFN_xrApplyForceFeedbackCurlMNDX = CFUNCTYPE(Result.ctype(), HandTrackerEXT, POINTER(ForceFeedbackCurlApplyLocationsMNDX))


class BodyTrackerBD_T(Structure):
    pass


class BodyTrackerBD(POINTER(BodyTrackerBD_T), HandleMixin):
    _type_ = BodyTrackerBD_T  # ctypes idiosyncrasy


class SystemBodyTrackingPropertiesBD(Structure):
    def __init__(
        self,
        supports_body_tracking: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_BODY_TRACKING_PROPERTIES_BD,
    ) -> None:
        super().__init__(
            supports_body_tracking=supports_body_tracking,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemBodyTrackingPropertiesBD(supports_body_tracking={repr(self.supports_body_tracking)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemBodyTrackingPropertiesBD(supports_body_tracking={self.supports_body_tracking}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_body_tracking", Bool32),
    ]


class BodyTrackerCreateInfoBD(Structure):
    def __init__(
        self,
        joint_set: BodyJointSetBD = BodyJointSetBD(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.BODY_TRACKER_CREATE_INFO_BD,
    ) -> None:
        super().__init__(
            joint_set=BodyJointSetBD(joint_set).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.BodyTrackerCreateInfoBD(joint_set={repr(self.joint_set)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.BodyTrackerCreateInfoBD(joint_set={self.joint_set}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("joint_set", BodyJointSetBD.ctype()),
    ]


class BodyJointsLocateInfoBD(Structure):
    def __init__(
        self,
        base_space: Space = None,
        time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.BODY_JOINTS_LOCATE_INFO_BD,
    ) -> None:
        super().__init__(
            base_space=base_space,
            time=time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.BodyJointsLocateInfoBD(base_space={repr(self.base_space)}, time={repr(self.time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.BodyJointsLocateInfoBD(base_space={self.base_space}, time={self.time}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("base_space", Space),
        ("time", Time),
    ]


class BodyJointLocationBD(Structure):
    def __init__(
        self,
        location_flags: SpaceLocationFlags = SpaceLocationFlags(),  # noqa
        pose: Posef = Posef(),
    ) -> None:
        super().__init__(
            location_flags=SpaceLocationFlags(location_flags).value,
            pose=pose,
        )

    def __repr__(self) -> str:
        return f"xr.BodyJointLocationBD(location_flags={repr(self.location_flags)}, pose={repr(self.pose)})"

    def __str__(self) -> str:
        return f"xr.BodyJointLocationBD(location_flags={self.location_flags}, pose={self.pose})"

    _fields_ = [
        ("location_flags", SpaceLocationFlagsCInt),
        ("pose", Posef),
    ]


class BodyJointLocationsBD(Structure):
    def __init__(
        self,
        all_joint_poses_tracked: Bool32 = 0,
        joint_location_count: Optional[int] = None,
        joint_locations: ArrayFieldParamType[BodyJointLocationBD] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.BODY_JOINT_LOCATIONS_BD,
    ) -> None:
        joint_location_count, joint_locations = array_field_helper(
            BodyJointLocationBD, joint_location_count, joint_locations)
        super().__init__(
            all_joint_poses_tracked=all_joint_poses_tracked,
            joint_location_count=joint_location_count,
            _joint_locations=joint_locations,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.BodyJointLocationsBD(all_joint_poses_tracked={repr(self.all_joint_poses_tracked)}, joint_location_count={repr(self.joint_location_count)}, joint_locations={repr(self._joint_locations)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.BodyJointLocationsBD(all_joint_poses_tracked={self.all_joint_poses_tracked}, joint_location_count={self.joint_location_count}, joint_locations={self._joint_locations}, next={self.next}, type={self.type})"

    @property
    def joint_locations(self):
        if self.joint_location_count == 0:
            return (BodyJointLocationBD * 0)()
        else:
            return (BodyJointLocationBD * self.joint_location_count).from_address(
                ctypes.addressof(self._joint_locations.contents))

    @joint_locations.setter
    def joint_locations(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.joint_location_count, self._joint_locations = array_field_helper(
            BodyJointLocationBD, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("all_joint_poses_tracked", Bool32),
        ("joint_location_count", c_uint32),
        ("_joint_locations", POINTER(BodyJointLocationBD)),
    ]


PFN_xrCreateBodyTrackerBD = CFUNCTYPE(Result.ctype(), Session, POINTER(BodyTrackerCreateInfoBD), POINTER(BodyTrackerBD))

PFN_xrDestroyBodyTrackerBD = CFUNCTYPE(Result.ctype(), BodyTrackerBD)

PFN_xrLocateBodyJointsBD = CFUNCTYPE(Result.ctype(), BodyTrackerBD, POINTER(BodyJointsLocateInfoBD), POINTER(BodyJointLocationsBD))

SpatialEntityIdBD = c_uint64


class SenseDataProviderBD_T(Structure):
    pass


class SenseDataProviderBD(POINTER(SenseDataProviderBD_T), HandleMixin):
    _type_ = SenseDataProviderBD_T  # ctypes idiosyncrasy


class SenseDataSnapshotBD_T(Structure):
    pass


class SenseDataSnapshotBD(POINTER(SenseDataSnapshotBD_T), HandleMixin):
    _type_ = SenseDataSnapshotBD_T  # ctypes idiosyncrasy


class AnchorBD_T(Structure):
    pass


class AnchorBD(POINTER(AnchorBD_T), HandleMixin):
    _type_ = AnchorBD_T  # ctypes idiosyncrasy


class SystemSpatialSensingPropertiesBD(Structure):
    def __init__(
        self,
        supports_spatial_sensing: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_SPATIAL_SENSING_PROPERTIES_BD,
    ) -> None:
        super().__init__(
            supports_spatial_sensing=supports_spatial_sensing,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemSpatialSensingPropertiesBD(supports_spatial_sensing={repr(self.supports_spatial_sensing)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemSpatialSensingPropertiesBD(supports_spatial_sensing={self.supports_spatial_sensing}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_spatial_sensing", Bool32),
    ]


class SpatialEntityComponentGetInfoBD(Structure):
    def __init__(
        self,
        entity_id: SpatialEntityIdBD = 0,
        component_type: SpatialEntityComponentTypeBD = SpatialEntityComponentTypeBD(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ENTITY_COMPONENT_GET_INFO_BD,
    ) -> None:
        super().__init__(
            entity_id=entity_id,
            component_type=SpatialEntityComponentTypeBD(component_type).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialEntityComponentGetInfoBD(entity_id={repr(self.entity_id)}, component_type={repr(self.component_type)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialEntityComponentGetInfoBD(entity_id={self.entity_id}, component_type={self.component_type}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("entity_id", SpatialEntityIdBD),
        ("component_type", SpatialEntityComponentTypeBD.ctype()),
    ]


class SpatialEntityComponentDataBaseHeaderBD(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialEntityComponentDataBaseHeaderBD(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialEntityComponentDataBaseHeaderBD(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SpatialEntityLocationGetInfoBD(Structure):
    def __init__(
        self,
        base_space: Space = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ENTITY_LOCATION_GET_INFO_BD,
    ) -> None:
        super().__init__(
            base_space=base_space,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialEntityLocationGetInfoBD(base_space={repr(self.base_space)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialEntityLocationGetInfoBD(base_space={self.base_space}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("base_space", Space),
    ]


class SpatialEntityComponentDataLocationBD(Structure):
    def __init__(
        self,
        location: SpaceLocation = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ENTITY_COMPONENT_DATA_LOCATION_BD,
    ) -> None:
        if location is None:
            location = SpaceLocation()
        super().__init__(
            location=location,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialEntityComponentDataLocationBD(location={repr(self.location)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialEntityComponentDataLocationBD(location={self.location}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("location", SpaceLocation),
    ]


class SpatialEntityComponentDataSemanticBD(Structure):
    def __init__(
        self,
        label_capacity_input: int = 0,
        label_count_output: int = 0,
        labels: POINTER(SemanticLabelBD.ctype()) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ENTITY_COMPONENT_DATA_SEMANTIC_BD,
    ) -> None:
        super().__init__(
            label_capacity_input=label_capacity_input,
            label_count_output=label_count_output,
            labels=labels,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialEntityComponentDataSemanticBD(label_capacity_input={repr(self.label_capacity_input)}, label_count_output={repr(self.label_count_output)}, labels={repr(self.labels)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialEntityComponentDataSemanticBD(label_capacity_input={self.label_capacity_input}, label_count_output={self.label_count_output}, labels={self.labels}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("label_capacity_input", c_uint32),
        ("label_count_output", c_uint32),
        ("labels", POINTER(SemanticLabelBD.ctype())),
    ]


class SpatialEntityComponentDataBoundingBox2DBD(Structure):
    def __init__(
        self,
        bounding_box_2d: Rect2Df = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ENTITY_COMPONENT_DATA_BOUNDING_BOX_2D_BD,
    ) -> None:
        if bounding_box_2d is None:
            bounding_box_2d = Rect2Df()
        super().__init__(
            bounding_box_2d=bounding_box_2d,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialEntityComponentDataBoundingBox2DBD(bounding_box_2d={repr(self.bounding_box_2d)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialEntityComponentDataBoundingBox2DBD(bounding_box_2d={self.bounding_box_2d}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("bounding_box_2d", Rect2Df),
    ]


class SpatialEntityComponentDataPolygonBD(Structure):
    def __init__(
        self,
        vertex_capacity_input: int = 0,
        vertex_count_output: int = 0,
        vertices: POINTER(Vector2f) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ENTITY_COMPONENT_DATA_POLYGON_BD,
    ) -> None:
        super().__init__(
            vertex_capacity_input=vertex_capacity_input,
            vertex_count_output=vertex_count_output,
            vertices=vertices,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialEntityComponentDataPolygonBD(vertex_capacity_input={repr(self.vertex_capacity_input)}, vertex_count_output={repr(self.vertex_count_output)}, vertices={repr(self.vertices)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialEntityComponentDataPolygonBD(vertex_capacity_input={self.vertex_capacity_input}, vertex_count_output={self.vertex_count_output}, vertices={self.vertices}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("vertex_capacity_input", c_uint32),
        ("vertex_count_output", c_uint32),
        ("vertices", POINTER(Vector2f)),
    ]


class SpatialEntityComponentDataBoundingBox3DBD(Structure):
    def __init__(
        self,
        bounding_box_3d: Boxf = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ENTITY_COMPONENT_DATA_BOUNDING_BOX_3D_BD,
    ) -> None:
        if bounding_box_3d is None:
            bounding_box_3d = Boxf()
        super().__init__(
            bounding_box_3d=bounding_box_3d,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialEntityComponentDataBoundingBox3DBD(bounding_box_3d={repr(self.bounding_box_3d)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialEntityComponentDataBoundingBox3DBD(bounding_box_3d={self.bounding_box_3d}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("bounding_box_3d", Boxf),
    ]


class SpatialEntityComponentDataTriangleMeshBD(Structure):
    def __init__(
        self,
        vertex_capacity_input: int = 0,
        vertex_count_output: int = 0,
        vertices: POINTER(Vector3f) = None,
        index_capacity_input: int = 0,
        index_count_output: int = 0,
        indices: POINTER(c_uint16) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ENTITY_COMPONENT_DATA_TRIANGLE_MESH_BD,
    ) -> None:
        super().__init__(
            vertex_capacity_input=vertex_capacity_input,
            vertex_count_output=vertex_count_output,
            vertices=vertices,
            index_capacity_input=index_capacity_input,
            index_count_output=index_count_output,
            indices=indices,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialEntityComponentDataTriangleMeshBD(vertex_capacity_input={repr(self.vertex_capacity_input)}, vertex_count_output={repr(self.vertex_count_output)}, vertices={repr(self.vertices)}, index_capacity_input={repr(self.index_capacity_input)}, index_count_output={repr(self.index_count_output)}, indices={repr(self.indices)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialEntityComponentDataTriangleMeshBD(vertex_capacity_input={self.vertex_capacity_input}, vertex_count_output={self.vertex_count_output}, vertices={self.vertices}, index_capacity_input={self.index_capacity_input}, index_count_output={self.index_count_output}, indices={self.indices}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("vertex_capacity_input", c_uint32),
        ("vertex_count_output", c_uint32),
        ("vertices", POINTER(Vector3f)),
        ("index_capacity_input", c_uint32),
        ("index_count_output", c_uint32),
        ("indices", POINTER(c_uint16)),
    ]


class SenseDataProviderCreateInfoBD(Structure):
    def __init__(
        self,
        provider_type: SenseDataProviderTypeBD = SenseDataProviderTypeBD(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.SENSE_DATA_PROVIDER_CREATE_INFO_BD,
    ) -> None:
        super().__init__(
            provider_type=SenseDataProviderTypeBD(provider_type).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SenseDataProviderCreateInfoBD(provider_type={repr(self.provider_type)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SenseDataProviderCreateInfoBD(provider_type={self.provider_type}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("provider_type", SenseDataProviderTypeBD.ctype()),
    ]


class SenseDataProviderStartInfoBD(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.SENSE_DATA_PROVIDER_START_INFO_BD,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SenseDataProviderStartInfoBD(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SenseDataProviderStartInfoBD(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class EventDataSenseDataProviderStateChangedBD(Structure):
    def __init__(
        self,
        provider: SenseDataProviderBD = None,
        new_state: SenseDataProviderStateBD = SenseDataProviderStateBD(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_SENSE_DATA_PROVIDER_STATE_CHANGED_BD,
    ) -> None:
        super().__init__(
            provider=provider,
            new_state=SenseDataProviderStateBD(new_state).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataSenseDataProviderStateChangedBD(provider={repr(self.provider)}, new_state={repr(self.new_state)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataSenseDataProviderStateChangedBD(provider={self.provider}, new_state={self.new_state}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("provider", SenseDataProviderBD),
        ("new_state", SenseDataProviderStateBD.ctype()),
    ]


class EventDataSenseDataUpdatedBD(Structure):
    def __init__(
        self,
        provider: SenseDataProviderBD = None,
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_SENSE_DATA_UPDATED_BD,
    ) -> None:
        super().__init__(
            provider=provider,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataSenseDataUpdatedBD(provider={repr(self.provider)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataSenseDataUpdatedBD(provider={self.provider}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("provider", SenseDataProviderBD),
    ]


class SenseDataQueryInfoBD(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.SENSE_DATA_QUERY_INFO_BD,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SenseDataQueryInfoBD(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SenseDataQueryInfoBD(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SenseDataQueryCompletionBD(Structure):
    def __init__(
        self,
        future_result: Result = Result(),  # noqa
        snapshot: SenseDataSnapshotBD = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SENSE_DATA_QUERY_COMPLETION_BD,
    ) -> None:
        super().__init__(
            future_result=Result(future_result).value,
            snapshot=snapshot,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SenseDataQueryCompletionBD(future_result={repr(self.future_result)}, snapshot={repr(self.snapshot)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SenseDataQueryCompletionBD(future_result={self.future_result}, snapshot={self.snapshot}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("future_result", Result.ctype()),
        ("snapshot", SenseDataSnapshotBD),
    ]


class QueriedSenseDataGetInfoBD(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.QUERIED_SENSE_DATA_GET_INFO_BD,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.QueriedSenseDataGetInfoBD(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.QueriedSenseDataGetInfoBD(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SpatialEntityStateBD(Structure):
    def __init__(
        self,
        entity_id: SpatialEntityIdBD = 0,
        last_update_time: Time = 0,
        uuid: UuidEXT = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ENTITY_STATE_BD,
    ) -> None:
        super().__init__(
            entity_id=entity_id,
            last_update_time=last_update_time,
            uuid=uuid,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialEntityStateBD(entity_id={repr(self.entity_id)}, last_update_time={repr(self.last_update_time)}, uuid={repr(self.uuid)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialEntityStateBD(entity_id={self.entity_id}, last_update_time={self.last_update_time}, uuid={self.uuid}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("entity_id", SpatialEntityIdBD),
        ("last_update_time", Time),
        ("uuid", UuidEXT),
    ]


class QueriedSenseDataBD(Structure):
    def __init__(
        self,
        state_capacity_input: int = 0,
        state_count_output: int = 0,
        states: POINTER(SpatialEntityStateBD) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.QUERIED_SENSE_DATA_BD,
    ) -> None:
        super().__init__(
            state_capacity_input=state_capacity_input,
            state_count_output=state_count_output,
            states=states,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.QueriedSenseDataBD(state_capacity_input={repr(self.state_capacity_input)}, state_count_output={repr(self.state_count_output)}, states={repr(self.states)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.QueriedSenseDataBD(state_capacity_input={self.state_capacity_input}, state_count_output={self.state_count_output}, states={self.states}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("state_capacity_input", c_uint32),
        ("state_count_output", c_uint32),
        ("states", POINTER(SpatialEntityStateBD)),
    ]


class SenseDataFilterUuidBD(Structure):
    def __init__(
        self,
        uuid_count: Optional[int] = None,
        uuids: ArrayFieldParamType[Uuid] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SENSE_DATA_FILTER_UUID_BD,
    ) -> None:
        uuid_count, uuids = array_field_helper(
            Uuid, uuid_count, uuids)
        super().__init__(
            uuid_count=uuid_count,
            _uuids=uuids,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SenseDataFilterUuidBD(uuid_count={repr(self.uuid_count)}, uuids={repr(self._uuids)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SenseDataFilterUuidBD(uuid_count={self.uuid_count}, uuids={self._uuids}, next={self.next}, type={self.type})"

    @property
    def uuids(self):
        if self.uuid_count == 0:
            return (Uuid * 0)()
        else:
            return (Uuid * self.uuid_count).from_address(
                ctypes.addressof(self._uuids.contents))

    @uuids.setter
    def uuids(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.uuid_count, self._uuids = array_field_helper(
            Uuid, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("uuid_count", c_uint32),
        ("_uuids", POINTER(Uuid)),
    ]


class SenseDataFilterSemanticBD(Structure):
    def __init__(
        self,
        label_count: Optional[int] = None,
        labels: ArrayFieldParamType[c_int] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SENSE_DATA_FILTER_SEMANTIC_BD,
    ) -> None:
        label_count, labels = array_field_helper(
            c_int, label_count, labels)
        super().__init__(
            label_count=label_count,
            _labels=labels,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SenseDataFilterSemanticBD(label_count={repr(self.label_count)}, labels={repr(self._labels)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SenseDataFilterSemanticBD(label_count={self.label_count}, labels={self._labels}, next={self.next}, type={self.type})"

    @property
    def labels(self):
        if self.label_count == 0:
            return (c_int * 0)()
        else:
            return (c_int * self.label_count).from_address(
                ctypes.addressof(self._labels.contents))

    @labels.setter
    def labels(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.label_count, self._labels = array_field_helper(
            c_int, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("label_count", c_uint32),
        ("_labels", POINTER(c_int)),
    ]


class SpatialEntityAnchorCreateInfoBD(Structure):
    def __init__(
        self,
        snapshot: SenseDataSnapshotBD = None,
        entity_id: SpatialEntityIdBD = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ENTITY_ANCHOR_CREATE_INFO_BD,
    ) -> None:
        super().__init__(
            snapshot=snapshot,
            entity_id=entity_id,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialEntityAnchorCreateInfoBD(snapshot={repr(self.snapshot)}, entity_id={repr(self.entity_id)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialEntityAnchorCreateInfoBD(snapshot={self.snapshot}, entity_id={self.entity_id}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("snapshot", SenseDataSnapshotBD),
        ("entity_id", SpatialEntityIdBD),
    ]


class AnchorSpaceCreateInfoBD(Structure):
    def __init__(
        self,
        anchor: AnchorBD = None,
        pose_in_anchor_space: Posef = Posef(),
        next: c_void_p = None,
        type: StructureType = StructureType.ANCHOR_SPACE_CREATE_INFO_BD,
    ) -> None:
        super().__init__(
            anchor=anchor,
            pose_in_anchor_space=pose_in_anchor_space,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.AnchorSpaceCreateInfoBD(anchor={repr(self.anchor)}, pose_in_anchor_space={repr(self.pose_in_anchor_space)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.AnchorSpaceCreateInfoBD(anchor={self.anchor}, pose_in_anchor_space={self.pose_in_anchor_space}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("anchor", AnchorBD),
        ("pose_in_anchor_space", Posef),
    ]


class FutureCompletionEXT(Structure):
    def __init__(
        self,
        future_result: Result = Result(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.FUTURE_COMPLETION_EXT,
    ) -> None:
        super().__init__(
            future_result=Result(future_result).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FutureCompletionEXT(future_result={repr(self.future_result)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FutureCompletionEXT(future_result={self.future_result}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("future_result", Result.ctype()),
    ]


PFN_xrEnumerateSpatialEntityComponentTypesBD = CFUNCTYPE(Result.ctype(), SenseDataSnapshotBD, SpatialEntityIdBD, c_uint32, POINTER(c_uint32), POINTER(SpatialEntityComponentTypeBD.ctype()))

PFN_xrGetSpatialEntityUuidBD = CFUNCTYPE(Result.ctype(), SenseDataSnapshotBD, SpatialEntityIdBD, POINTER(UuidEXT))

PFN_xrGetSpatialEntityComponentDataBD = CFUNCTYPE(Result.ctype(), SenseDataSnapshotBD, POINTER(SpatialEntityComponentGetInfoBD), POINTER(SpatialEntityComponentDataBaseHeaderBD))

PFN_xrCreateSenseDataProviderBD = CFUNCTYPE(Result.ctype(), Session, POINTER(SenseDataProviderCreateInfoBD), POINTER(SenseDataProviderBD))

PFN_xrStartSenseDataProviderAsyncBD = CFUNCTYPE(Result.ctype(), SenseDataProviderBD, POINTER(SenseDataProviderStartInfoBD), POINTER(FutureEXT))

PFN_xrStartSenseDataProviderCompleteBD = CFUNCTYPE(Result.ctype(), Session, FutureEXT, POINTER(FutureCompletionEXT))

PFN_xrGetSenseDataProviderStateBD = CFUNCTYPE(Result.ctype(), SenseDataProviderBD, POINTER(SenseDataProviderStateBD.ctype()))

PFN_xrQuerySenseDataAsyncBD = CFUNCTYPE(Result.ctype(), SenseDataProviderBD, POINTER(SenseDataQueryInfoBD), POINTER(FutureEXT))

PFN_xrQuerySenseDataCompleteBD = CFUNCTYPE(Result.ctype(), SenseDataProviderBD, FutureEXT, POINTER(SenseDataQueryCompletionBD))

PFN_xrDestroySenseDataSnapshotBD = CFUNCTYPE(Result.ctype(), SenseDataSnapshotBD)

PFN_xrGetQueriedSenseDataBD = CFUNCTYPE(Result.ctype(), SenseDataSnapshotBD, POINTER(QueriedSenseDataGetInfoBD), POINTER(QueriedSenseDataBD))

PFN_xrStopSenseDataProviderBD = CFUNCTYPE(Result.ctype(), SenseDataProviderBD)

PFN_xrDestroySenseDataProviderBD = CFUNCTYPE(Result.ctype(), SenseDataProviderBD)

PFN_xrCreateSpatialEntityAnchorBD = CFUNCTYPE(Result.ctype(), SenseDataProviderBD, POINTER(SpatialEntityAnchorCreateInfoBD), POINTER(AnchorBD))

PFN_xrDestroyAnchorBD = CFUNCTYPE(Result.ctype(), AnchorBD)

PFN_xrGetAnchorUuidBD = CFUNCTYPE(Result.ctype(), AnchorBD, POINTER(UuidEXT))

PFN_xrCreateAnchorSpaceBD = CFUNCTYPE(Result.ctype(), Session, POINTER(AnchorSpaceCreateInfoBD), POINTER(Space))


class SystemSpatialAnchorPropertiesBD(Structure):
    def __init__(
        self,
        supports_spatial_anchor: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_SPATIAL_ANCHOR_PROPERTIES_BD,
    ) -> None:
        super().__init__(
            supports_spatial_anchor=supports_spatial_anchor,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemSpatialAnchorPropertiesBD(supports_spatial_anchor={repr(self.supports_spatial_anchor)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemSpatialAnchorPropertiesBD(supports_spatial_anchor={self.supports_spatial_anchor}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_spatial_anchor", Bool32),
    ]


class SpatialAnchorCreateInfoBD(Structure):
    def __init__(
        self,
        space: Space = None,
        pose: Posef = Posef(),
        time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHOR_CREATE_INFO_BD,
    ) -> None:
        super().__init__(
            space=space,
            pose=pose,
            time=time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorCreateInfoBD(space={repr(self.space)}, pose={repr(self.pose)}, time={repr(self.time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorCreateInfoBD(space={self.space}, pose={self.pose}, time={self.time}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("space", Space),
        ("pose", Posef),
        ("time", Time),
    ]


class SpatialAnchorCreateCompletionBD(Structure):
    def __init__(
        self,
        future_result: Result = Result(),  # noqa
        uuid: UuidEXT = 0,
        anchor: AnchorBD = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHOR_CREATE_COMPLETION_BD,
    ) -> None:
        super().__init__(
            future_result=Result(future_result).value,
            uuid=uuid,
            anchor=anchor,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorCreateCompletionBD(future_result={repr(self.future_result)}, uuid={repr(self.uuid)}, anchor={repr(self.anchor)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorCreateCompletionBD(future_result={self.future_result}, uuid={self.uuid}, anchor={self.anchor}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("future_result", Result.ctype()),
        ("uuid", UuidEXT),
        ("anchor", AnchorBD),
    ]


class SpatialAnchorPersistInfoBD(Structure):
    def __init__(
        self,
        location: PersistenceLocationBD = PersistenceLocationBD(),  # noqa
        anchor: AnchorBD = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHOR_PERSIST_INFO_BD,
    ) -> None:
        super().__init__(
            location=PersistenceLocationBD(location).value,
            anchor=anchor,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorPersistInfoBD(location={repr(self.location)}, anchor={repr(self.anchor)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorPersistInfoBD(location={self.location}, anchor={self.anchor}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("location", PersistenceLocationBD.ctype()),
        ("anchor", AnchorBD),
    ]


class SpatialAnchorUnpersistInfoBD(Structure):
    def __init__(
        self,
        location: PersistenceLocationBD = PersistenceLocationBD(),  # noqa
        anchor: AnchorBD = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHOR_UNPERSIST_INFO_BD,
    ) -> None:
        super().__init__(
            location=PersistenceLocationBD(location).value,
            anchor=anchor,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorUnpersistInfoBD(location={repr(self.location)}, anchor={repr(self.anchor)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorUnpersistInfoBD(location={self.location}, anchor={self.anchor}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("location", PersistenceLocationBD.ctype()),
        ("anchor", AnchorBD),
    ]


PFN_xrCreateSpatialAnchorAsyncBD = CFUNCTYPE(Result.ctype(), SenseDataProviderBD, POINTER(SpatialAnchorCreateInfoBD), POINTER(FutureEXT))

PFN_xrCreateSpatialAnchorCompleteBD = CFUNCTYPE(Result.ctype(), SenseDataProviderBD, FutureEXT, POINTER(SpatialAnchorCreateCompletionBD))

PFN_xrPersistSpatialAnchorAsyncBD = CFUNCTYPE(Result.ctype(), SenseDataProviderBD, POINTER(SpatialAnchorPersistInfoBD), POINTER(FutureEXT))

PFN_xrPersistSpatialAnchorCompleteBD = CFUNCTYPE(Result.ctype(), SenseDataProviderBD, FutureEXT, POINTER(FutureCompletionEXT))

PFN_xrUnpersistSpatialAnchorAsyncBD = CFUNCTYPE(Result.ctype(), SenseDataProviderBD, POINTER(SpatialAnchorUnpersistInfoBD), POINTER(FutureEXT))

PFN_xrUnpersistSpatialAnchorCompleteBD = CFUNCTYPE(Result.ctype(), SenseDataProviderBD, FutureEXT, POINTER(FutureCompletionEXT))


class SystemSpatialAnchorSharingPropertiesBD(Structure):
    def __init__(
        self,
        supports_spatial_anchor_sharing: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_SPATIAL_ANCHOR_SHARING_PROPERTIES_BD,
    ) -> None:
        super().__init__(
            supports_spatial_anchor_sharing=supports_spatial_anchor_sharing,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemSpatialAnchorSharingPropertiesBD(supports_spatial_anchor_sharing={repr(self.supports_spatial_anchor_sharing)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemSpatialAnchorSharingPropertiesBD(supports_spatial_anchor_sharing={self.supports_spatial_anchor_sharing}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_spatial_anchor_sharing", Bool32),
    ]


class SpatialAnchorShareInfoBD(Structure):
    def __init__(
        self,
        anchor: AnchorBD = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHOR_SHARE_INFO_BD,
    ) -> None:
        super().__init__(
            anchor=anchor,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorShareInfoBD(anchor={repr(self.anchor)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorShareInfoBD(anchor={self.anchor}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("anchor", AnchorBD),
    ]


class SharedSpatialAnchorDownloadInfoBD(Structure):
    def __init__(
        self,
        uuid: UuidEXT = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SHARED_SPATIAL_ANCHOR_DOWNLOAD_INFO_BD,
    ) -> None:
        super().__init__(
            uuid=uuid,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SharedSpatialAnchorDownloadInfoBD(uuid={repr(self.uuid)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SharedSpatialAnchorDownloadInfoBD(uuid={self.uuid}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("uuid", UuidEXT),
    ]


PFN_xrShareSpatialAnchorAsyncBD = CFUNCTYPE(Result.ctype(), SenseDataProviderBD, POINTER(SpatialAnchorShareInfoBD), POINTER(FutureEXT))

PFN_xrShareSpatialAnchorCompleteBD = CFUNCTYPE(Result.ctype(), SenseDataProviderBD, FutureEXT, POINTER(FutureCompletionEXT))

PFN_xrDownloadSharedSpatialAnchorAsyncBD = CFUNCTYPE(Result.ctype(), SenseDataProviderBD, POINTER(SharedSpatialAnchorDownloadInfoBD), POINTER(FutureEXT))

PFN_xrDownloadSharedSpatialAnchorCompleteBD = CFUNCTYPE(Result.ctype(), SenseDataProviderBD, FutureEXT, POINTER(FutureCompletionEXT))


class SystemSpatialScenePropertiesBD(Structure):
    def __init__(
        self,
        supports_spatial_scene: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_SPATIAL_SCENE_PROPERTIES_BD,
    ) -> None:
        super().__init__(
            supports_spatial_scene=supports_spatial_scene,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemSpatialScenePropertiesBD(supports_spatial_scene={repr(self.supports_spatial_scene)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemSpatialScenePropertiesBD(supports_spatial_scene={self.supports_spatial_scene}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_spatial_scene", Bool32),
    ]


class SceneCaptureInfoBD(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.SCENE_CAPTURE_INFO_BD,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SceneCaptureInfoBD(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SceneCaptureInfoBD(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


PFN_xrCaptureSceneAsyncBD = CFUNCTYPE(Result.ctype(), SenseDataProviderBD, POINTER(SceneCaptureInfoBD), POINTER(FutureEXT))

PFN_xrCaptureSceneCompleteBD = CFUNCTYPE(Result.ctype(), SenseDataProviderBD, FutureEXT, POINTER(FutureCompletionEXT))

SpatialMeshConfigFlagsBDCInt = Flags64


class SystemSpatialMeshPropertiesBD(Structure):
    def __init__(
        self,
        supports_spatial_mesh: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_SPATIAL_MESH_PROPERTIES_BD,
    ) -> None:
        super().__init__(
            supports_spatial_mesh=supports_spatial_mesh,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemSpatialMeshPropertiesBD(supports_spatial_mesh={repr(self.supports_spatial_mesh)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemSpatialMeshPropertiesBD(supports_spatial_mesh={self.supports_spatial_mesh}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_spatial_mesh", Bool32),
    ]


class SenseDataProviderCreateInfoSpatialMeshBD(Structure):
    def __init__(
        self,
        config_flags: SpatialMeshConfigFlagsBD = SpatialMeshConfigFlagsBD(),  # noqa
        lod: SpatialMeshLodBD = SpatialMeshLodBD(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.SENSE_DATA_PROVIDER_CREATE_INFO_SPATIAL_MESH_BD,
    ) -> None:
        super().__init__(
            config_flags=SpatialMeshConfigFlagsBD(config_flags).value,
            lod=SpatialMeshLodBD(lod).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SenseDataProviderCreateInfoSpatialMeshBD(config_flags={repr(self.config_flags)}, lod={repr(self.lod)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SenseDataProviderCreateInfoSpatialMeshBD(config_flags={self.config_flags}, lod={self.lod}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("config_flags", SpatialMeshConfigFlagsBDCInt),
        ("lod", SpatialMeshLodBD.ctype()),
    ]


class FuturePollResultProgressBD(Structure):
    def __init__(
        self,
        is_supported: Bool32 = 0,
        progress_percentage: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.FUTURE_POLL_RESULT_PROGRESS_BD,
    ) -> None:
        super().__init__(
            is_supported=is_supported,
            progress_percentage=progress_percentage,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FuturePollResultProgressBD(is_supported={repr(self.is_supported)}, progress_percentage={repr(self.progress_percentage)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FuturePollResultProgressBD(is_supported={self.is_supported}, progress_percentage={self.progress_percentage}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("is_supported", Bool32),
        ("progress_percentage", c_uint32),
    ]


class SystemSpatialPlanePropertiesBD(Structure):
    def __init__(
        self,
        supports_spatial_plane: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_SPATIAL_PLANE_PROPERTIES_BD,
    ) -> None:
        super().__init__(
            supports_spatial_plane=supports_spatial_plane,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemSpatialPlanePropertiesBD(supports_spatial_plane={repr(self.supports_spatial_plane)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemSpatialPlanePropertiesBD(supports_spatial_plane={self.supports_spatial_plane}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_spatial_plane", Bool32),
    ]


class SpatialEntityComponentDataPlaneOrientationBD(Structure):
    def __init__(
        self,
        orientation: PlaneOrientationBD = PlaneOrientationBD(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ENTITY_COMPONENT_DATA_PLANE_ORIENTATION_BD,
    ) -> None:
        super().__init__(
            orientation=PlaneOrientationBD(orientation).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialEntityComponentDataPlaneOrientationBD(orientation={repr(self.orientation)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialEntityComponentDataPlaneOrientationBD(orientation={self.orientation}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("orientation", PlaneOrientationBD.ctype()),
    ]


class SenseDataFilterPlaneOrientationBD(Structure):
    def __init__(
        self,
        orientation_count: Optional[int] = None,
        orientations: ArrayFieldParamType[PlaneOrientationBD.ctype()] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SENSE_DATA_FILTER_PLANE_ORIENTATION_BD,
    ) -> None:
        orientation_count, orientations = array_field_helper(
            PlaneOrientationBD.ctype(), orientation_count, orientations)
        super().__init__(
            orientation_count=orientation_count,
            _orientations=orientations,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SenseDataFilterPlaneOrientationBD(orientation_count={repr(self.orientation_count)}, orientations={repr(self._orientations)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SenseDataFilterPlaneOrientationBD(orientation_count={self.orientation_count}, orientations={self._orientations}, next={self.next}, type={self.type})"

    @property
    def orientations(self):
        if self.orientation_count == 0:
            return (PlaneOrientationBD.ctype() * 0)()
        else:
            return (PlaneOrientationBD.ctype() * self.orientation_count).from_address(
                ctypes.addressof(self._orientations.contents))

    @orientations.setter
    def orientations(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.orientation_count, self._orientations = array_field_helper(
            PlaneOrientationBD.ctype(), None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("orientation_count", c_uint32),
        ("_orientations", POINTER(PlaneOrientationBD.ctype())),
    ]


class HandTrackingDataSourceInfoEXT(Structure):
    def __init__(
        self,
        requested_data_source_count: Optional[int] = None,
        requested_data_sources: ArrayFieldParamType[HandTrackingDataSourceEXT.ctype()] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.HAND_TRACKING_DATA_SOURCE_INFO_EXT,
    ) -> None:
        requested_data_source_count, requested_data_sources = array_field_helper(
            HandTrackingDataSourceEXT.ctype(), requested_data_source_count, requested_data_sources)
        super().__init__(
            requested_data_source_count=requested_data_source_count,
            _requested_data_sources=requested_data_sources,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.HandTrackingDataSourceInfoEXT(requested_data_source_count={repr(self.requested_data_source_count)}, requested_data_sources={repr(self._requested_data_sources)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.HandTrackingDataSourceInfoEXT(requested_data_source_count={self.requested_data_source_count}, requested_data_sources={self._requested_data_sources}, next={self.next}, type={self.type})"

    @property
    def requested_data_sources(self):
        if self.requested_data_source_count == 0:
            return (HandTrackingDataSourceEXT.ctype() * 0)()
        else:
            return (HandTrackingDataSourceEXT.ctype() * self.requested_data_source_count).from_address(
                ctypes.addressof(self._requested_data_sources.contents))

    @requested_data_sources.setter
    def requested_data_sources(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.requested_data_source_count, self._requested_data_sources = array_field_helper(
            HandTrackingDataSourceEXT.ctype(), None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("requested_data_source_count", c_uint32),
        ("_requested_data_sources", POINTER(HandTrackingDataSourceEXT.ctype())),
    ]


class HandTrackingDataSourceStateEXT(Structure):
    def __init__(
        self,
        is_active: Bool32 = 0,
        data_source: HandTrackingDataSourceEXT = HandTrackingDataSourceEXT(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.HAND_TRACKING_DATA_SOURCE_STATE_EXT,
    ) -> None:
        super().__init__(
            is_active=is_active,
            data_source=HandTrackingDataSourceEXT(data_source).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.HandTrackingDataSourceStateEXT(is_active={repr(self.is_active)}, data_source={repr(self.data_source)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.HandTrackingDataSourceStateEXT(is_active={self.is_active}, data_source={self.data_source}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("is_active", Bool32),
        ("data_source", HandTrackingDataSourceEXT.ctype()),
    ]


class PlaneDetectorEXT_T(Structure):
    pass


class PlaneDetectorEXT(POINTER(PlaneDetectorEXT_T), HandleMixin):
    _type_ = PlaneDetectorEXT_T  # ctypes idiosyncrasy

PlaneDetectionCapabilityFlagsEXTCInt = Flags64

PlaneDetectorFlagsEXTCInt = Flags64


class SystemPlaneDetectionPropertiesEXT(Structure):
    def __init__(
        self,
        supported_features: PlaneDetectionCapabilityFlagsEXT = PlaneDetectionCapabilityFlagsEXT(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_PLANE_DETECTION_PROPERTIES_EXT,
    ) -> None:
        super().__init__(
            supported_features=PlaneDetectionCapabilityFlagsEXT(supported_features).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemPlaneDetectionPropertiesEXT(supported_features={repr(self.supported_features)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemPlaneDetectionPropertiesEXT(supported_features={self.supported_features}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supported_features", PlaneDetectionCapabilityFlagsEXTCInt),
    ]


class PlaneDetectorCreateInfoEXT(Structure):
    def __init__(
        self,
        flags: PlaneDetectorFlagsEXT = PlaneDetectorFlagsEXT(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.PLANE_DETECTOR_CREATE_INFO_EXT,
    ) -> None:
        super().__init__(
            flags=PlaneDetectorFlagsEXT(flags).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PlaneDetectorCreateInfoEXT(flags={repr(self.flags)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PlaneDetectorCreateInfoEXT(flags={self.flags}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", PlaneDetectorFlagsEXTCInt),
    ]


Extent3DfEXT = Extent3Df


class PlaneDetectorBeginInfoEXT(Structure):
    def __init__(
        self,
        base_space: Space = None,
        time: Time = 0,
        orientation_count: Optional[int] = None,
        orientations: ArrayFieldParamType[c_int] = None,
        semantic_type_count: Optional[int] = None,
        semantic_types: ArrayFieldParamType[c_int] = None,
        max_planes: int = 0,
        min_area: float = 0,
        bounding_box_pose: Posef = Posef(),
        bounding_box_extent: Extent3DfEXT = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.PLANE_DETECTOR_BEGIN_INFO_EXT,
    ) -> None:
        orientation_count, orientations = array_field_helper(
            c_int, orientation_count, orientations)
        semantic_type_count, semantic_types = array_field_helper(
            c_int, semantic_type_count, semantic_types)
        super().__init__(
            base_space=base_space,
            time=time,
            orientation_count=orientation_count,
            _orientations=orientations,
            semantic_type_count=semantic_type_count,
            _semantic_types=semantic_types,
            max_planes=max_planes,
            min_area=min_area,
            bounding_box_pose=bounding_box_pose,
            bounding_box_extent=bounding_box_extent,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PlaneDetectorBeginInfoEXT(base_space={repr(self.base_space)}, time={repr(self.time)}, orientation_count={repr(self.orientation_count)}, orientations={repr(self._orientations)}, semantic_type_count={repr(self.semantic_type_count)}, semantic_types={repr(self._semantic_types)}, max_planes={repr(self.max_planes)}, min_area={repr(self.min_area)}, bounding_box_pose={repr(self.bounding_box_pose)}, bounding_box_extent={repr(self.bounding_box_extent)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PlaneDetectorBeginInfoEXT(base_space={self.base_space}, time={self.time}, orientation_count={self.orientation_count}, orientations={self._orientations}, semantic_type_count={self.semantic_type_count}, semantic_types={self._semantic_types}, max_planes={self.max_planes}, min_area={self.min_area:.3f}, bounding_box_pose={self.bounding_box_pose}, bounding_box_extent={self.bounding_box_extent}, next={self.next}, type={self.type})"

    @property
    def orientations(self):
        if self.orientation_count == 0:
            return (c_int * 0)()
        else:
            return (c_int * self.orientation_count).from_address(
                ctypes.addressof(self._orientations.contents))

    @orientations.setter
    def orientations(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.orientation_count, self._orientations = array_field_helper(
            c_int, None, value)

    @property
    def semantic_types(self):
        if self.semantic_type_count == 0:
            return (c_int * 0)()
        else:
            return (c_int * self.semantic_type_count).from_address(
                ctypes.addressof(self._semantic_types.contents))

    @semantic_types.setter
    def semantic_types(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.semantic_type_count, self._semantic_types = array_field_helper(
            c_int, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("base_space", Space),
        ("time", Time),
        ("orientation_count", c_uint32),
        ("_orientations", POINTER(c_int)),
        ("semantic_type_count", c_uint32),
        ("_semantic_types", POINTER(c_int)),
        ("max_planes", c_uint32),
        ("min_area", c_float),
        ("bounding_box_pose", Posef),
        ("bounding_box_extent", Extent3DfEXT),
    ]


class PlaneDetectorGetInfoEXT(Structure):
    def __init__(
        self,
        base_space: Space = None,
        time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.PLANE_DETECTOR_GET_INFO_EXT,
    ) -> None:
        super().__init__(
            base_space=base_space,
            time=time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PlaneDetectorGetInfoEXT(base_space={repr(self.base_space)}, time={repr(self.time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PlaneDetectorGetInfoEXT(base_space={self.base_space}, time={self.time}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("base_space", Space),
        ("time", Time),
    ]


class PlaneDetectorLocationEXT(Structure):
    def __init__(
        self,
        plane_id: int = 0,
        location_flags: SpaceLocationFlags = SpaceLocationFlags(),  # noqa
        pose: Posef = Posef(),
        extents: Extent2Df = None,
        orientation: PlaneDetectorOrientationEXT = PlaneDetectorOrientationEXT(),  # noqa
        semantic_type: PlaneDetectorSemanticTypeEXT = PlaneDetectorSemanticTypeEXT(),  # noqa
        polygon_buffer_count: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.PLANE_DETECTOR_LOCATION_EXT,
    ) -> None:
        if extents is None:
            extents = Extent2Df()
        super().__init__(
            plane_id=plane_id,
            location_flags=SpaceLocationFlags(location_flags).value,
            pose=pose,
            extents=extents,
            orientation=PlaneDetectorOrientationEXT(orientation).value,
            semantic_type=PlaneDetectorSemanticTypeEXT(semantic_type).value,
            polygon_buffer_count=polygon_buffer_count,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PlaneDetectorLocationEXT(plane_id={repr(self.plane_id)}, location_flags={repr(self.location_flags)}, pose={repr(self.pose)}, extents={repr(self.extents)}, orientation={repr(self.orientation)}, semantic_type={repr(self.semantic_type)}, polygon_buffer_count={repr(self.polygon_buffer_count)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PlaneDetectorLocationEXT(plane_id={self.plane_id}, location_flags={self.location_flags}, pose={self.pose}, extents={self.extents}, orientation={self.orientation}, semantic_type={self.semantic_type}, polygon_buffer_count={self.polygon_buffer_count}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("plane_id", c_uint64),
        ("location_flags", SpaceLocationFlagsCInt),
        ("pose", Posef),
        ("extents", Extent2Df),
        ("orientation", PlaneDetectorOrientationEXT.ctype()),
        ("semantic_type", PlaneDetectorSemanticTypeEXT.ctype()),
        ("polygon_buffer_count", c_uint32),
    ]


class PlaneDetectorLocationsEXT(Structure):
    def __init__(
        self,
        plane_location_capacity_input: int = 0,
        plane_location_count_output: int = 0,
        plane_locations: POINTER(PlaneDetectorLocationEXT) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.PLANE_DETECTOR_LOCATIONS_EXT,
    ) -> None:
        super().__init__(
            plane_location_capacity_input=plane_location_capacity_input,
            plane_location_count_output=plane_location_count_output,
            plane_locations=plane_locations,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PlaneDetectorLocationsEXT(plane_location_capacity_input={repr(self.plane_location_capacity_input)}, plane_location_count_output={repr(self.plane_location_count_output)}, plane_locations={repr(self.plane_locations)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PlaneDetectorLocationsEXT(plane_location_capacity_input={self.plane_location_capacity_input}, plane_location_count_output={self.plane_location_count_output}, plane_locations={self.plane_locations}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("plane_location_capacity_input", c_uint32),
        ("plane_location_count_output", c_uint32),
        ("plane_locations", POINTER(PlaneDetectorLocationEXT)),
    ]


class PlaneDetectorPolygonBufferEXT(Structure):
    def __init__(
        self,
        vertex_capacity_input: int = 0,
        vertex_count_output: int = 0,
        vertices: POINTER(Vector2f) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.PLANE_DETECTOR_POLYGON_BUFFER_EXT,
    ) -> None:
        super().__init__(
            vertex_capacity_input=vertex_capacity_input,
            vertex_count_output=vertex_count_output,
            vertices=vertices,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PlaneDetectorPolygonBufferEXT(vertex_capacity_input={repr(self.vertex_capacity_input)}, vertex_count_output={repr(self.vertex_count_output)}, vertices={repr(self.vertices)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PlaneDetectorPolygonBufferEXT(vertex_capacity_input={self.vertex_capacity_input}, vertex_count_output={self.vertex_count_output}, vertices={self.vertices}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("vertex_capacity_input", c_uint32),
        ("vertex_count_output", c_uint32),
        ("vertices", POINTER(Vector2f)),
    ]


PFN_xrCreatePlaneDetectorEXT = CFUNCTYPE(Result.ctype(), Session, POINTER(PlaneDetectorCreateInfoEXT), POINTER(PlaneDetectorEXT))

PFN_xrDestroyPlaneDetectorEXT = CFUNCTYPE(Result.ctype(), PlaneDetectorEXT)

PFN_xrBeginPlaneDetectionEXT = CFUNCTYPE(Result.ctype(), PlaneDetectorEXT, POINTER(PlaneDetectorBeginInfoEXT))

PFN_xrGetPlaneDetectionStateEXT = CFUNCTYPE(Result.ctype(), PlaneDetectorEXT, POINTER(PlaneDetectionStateEXT.ctype()))

PFN_xrGetPlaneDetectionsEXT = CFUNCTYPE(Result.ctype(), PlaneDetectorEXT, POINTER(PlaneDetectorGetInfoEXT), POINTER(PlaneDetectorLocationsEXT))

PFN_xrGetPlanePolygonBufferEXT = CFUNCTYPE(Result.ctype(), PlaneDetectorEXT, c_uint64, c_uint32, POINTER(PlaneDetectorPolygonBufferEXT))

TrackableANDROID = c_uint64


class TrackableTrackerANDROID_T(Structure):
    pass


class TrackableTrackerANDROID(POINTER(TrackableTrackerANDROID_T), HandleMixin):
    _type_ = TrackableTrackerANDROID_T  # ctypes idiosyncrasy


class TrackableTrackerCreateInfoANDROID(Structure):
    def __init__(
        self,
        trackable_type: TrackableTypeANDROID = TrackableTypeANDROID(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.TRACKABLE_TRACKER_CREATE_INFO_ANDROID,
    ) -> None:
        super().__init__(
            trackable_type=TrackableTypeANDROID(trackable_type).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.TrackableTrackerCreateInfoANDROID(trackable_type={repr(self.trackable_type)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.TrackableTrackerCreateInfoANDROID(trackable_type={self.trackable_type}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("trackable_type", TrackableTypeANDROID.ctype()),
    ]


class TrackableGetInfoANDROID(Structure):
    def __init__(
        self,
        trackable: TrackableANDROID = 0,
        base_space: Space = None,
        time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.TRACKABLE_GET_INFO_ANDROID,
    ) -> None:
        super().__init__(
            trackable=trackable,
            base_space=base_space,
            time=time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.TrackableGetInfoANDROID(trackable={repr(self.trackable)}, base_space={repr(self.base_space)}, time={repr(self.time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.TrackableGetInfoANDROID(trackable={self.trackable}, base_space={self.base_space}, time={self.time}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("trackable", TrackableANDROID),
        ("base_space", Space),
        ("time", Time),
    ]


class TrackablePlaneANDROID(Structure):
    def __init__(
        self,
        tracking_state: TrackingStateANDROID = TrackingStateANDROID(),  # noqa
        center_pose: Posef = Posef(),
        extents: Extent2Df = None,
        plane_type: PlaneTypeANDROID = PlaneTypeANDROID(),  # noqa
        plane_label: PlaneLabelANDROID = PlaneLabelANDROID(),  # noqa
        subsumed_by_plane: TrackableANDROID = 0,
        last_updated_time: Time = 0,
        vertex_capacity_input: int = 0,
        vertex_count_output: int = 0,
        vertices: POINTER(Vector2f) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.TRACKABLE_PLANE_ANDROID,
    ) -> None:
        if extents is None:
            extents = Extent2Df()
        super().__init__(
            tracking_state=TrackingStateANDROID(tracking_state).value,
            center_pose=center_pose,
            extents=extents,
            plane_type=PlaneTypeANDROID(plane_type).value,
            plane_label=PlaneLabelANDROID(plane_label).value,
            subsumed_by_plane=subsumed_by_plane,
            last_updated_time=last_updated_time,
            vertex_capacity_input=vertex_capacity_input,
            vertex_count_output=vertex_count_output,
            vertices=vertices,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.TrackablePlaneANDROID(tracking_state={repr(self.tracking_state)}, center_pose={repr(self.center_pose)}, extents={repr(self.extents)}, plane_type={repr(self.plane_type)}, plane_label={repr(self.plane_label)}, subsumed_by_plane={repr(self.subsumed_by_plane)}, last_updated_time={repr(self.last_updated_time)}, vertex_capacity_input={repr(self.vertex_capacity_input)}, vertex_count_output={repr(self.vertex_count_output)}, vertices={repr(self.vertices)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.TrackablePlaneANDROID(tracking_state={self.tracking_state}, center_pose={self.center_pose}, extents={self.extents}, plane_type={self.plane_type}, plane_label={self.plane_label}, subsumed_by_plane={self.subsumed_by_plane}, last_updated_time={self.last_updated_time}, vertex_capacity_input={self.vertex_capacity_input}, vertex_count_output={self.vertex_count_output}, vertices={self.vertices}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("tracking_state", TrackingStateANDROID.ctype()),
        ("center_pose", Posef),
        ("extents", Extent2Df),
        ("plane_type", PlaneTypeANDROID.ctype()),
        ("plane_label", PlaneLabelANDROID.ctype()),
        ("subsumed_by_plane", TrackableANDROID),
        ("last_updated_time", Time),
        ("vertex_capacity_input", c_uint32),
        ("vertex_count_output", c_uint32),
        ("vertices", POINTER(Vector2f)),
    ]


class AnchorSpaceCreateInfoANDROID(Structure):
    def __init__(
        self,
        space: Space = None,
        time: Time = 0,
        pose: Posef = Posef(),
        trackable: TrackableANDROID = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.ANCHOR_SPACE_CREATE_INFO_ANDROID,
    ) -> None:
        super().__init__(
            space=space,
            time=time,
            pose=pose,
            trackable=trackable,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.AnchorSpaceCreateInfoANDROID(space={repr(self.space)}, time={repr(self.time)}, pose={repr(self.pose)}, trackable={repr(self.trackable)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.AnchorSpaceCreateInfoANDROID(space={self.space}, time={self.time}, pose={self.pose}, trackable={self.trackable}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("space", Space),
        ("time", Time),
        ("pose", Posef),
        ("trackable", TrackableANDROID),
    ]


class SystemTrackablesPropertiesANDROID(Structure):
    def __init__(
        self,
        supports_anchor: Bool32 = 0,
        max_anchors: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_TRACKABLES_PROPERTIES_ANDROID,
    ) -> None:
        super().__init__(
            supports_anchor=supports_anchor,
            max_anchors=max_anchors,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemTrackablesPropertiesANDROID(supports_anchor={repr(self.supports_anchor)}, max_anchors={repr(self.max_anchors)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemTrackablesPropertiesANDROID(supports_anchor={self.supports_anchor}, max_anchors={self.max_anchors}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_anchor", Bool32),
        ("max_anchors", c_uint32),
    ]


PFN_xrEnumerateSupportedTrackableTypesANDROID = CFUNCTYPE(Result.ctype(), Instance, SystemId, c_uint32, POINTER(c_uint32), POINTER(TrackableTypeANDROID.ctype()))

PFN_xrEnumerateSupportedAnchorTrackableTypesANDROID = CFUNCTYPE(Result.ctype(), Instance, SystemId, c_uint32, POINTER(c_uint32), POINTER(TrackableTypeANDROID.ctype()))

PFN_xrCreateTrackableTrackerANDROID = CFUNCTYPE(Result.ctype(), Session, POINTER(TrackableTrackerCreateInfoANDROID), POINTER(TrackableTrackerANDROID))

PFN_xrDestroyTrackableTrackerANDROID = CFUNCTYPE(Result.ctype(), TrackableTrackerANDROID)

PFN_xrGetAllTrackablesANDROID = CFUNCTYPE(Result.ctype(), TrackableTrackerANDROID, c_uint32, POINTER(c_uint32), POINTER(TrackableANDROID))

PFN_xrGetTrackablePlaneANDROID = CFUNCTYPE(Result.ctype(), TrackableTrackerANDROID, POINTER(TrackableGetInfoANDROID), POINTER(TrackablePlaneANDROID))

PFN_xrCreateAnchorSpaceANDROID = CFUNCTYPE(Result.ctype(), Session, POINTER(AnchorSpaceCreateInfoANDROID), POINTER(Space))


class DeviceAnchorPersistenceANDROID_T(Structure):
    pass


class DeviceAnchorPersistenceANDROID(POINTER(DeviceAnchorPersistenceANDROID_T), HandleMixin):
    _type_ = DeviceAnchorPersistenceANDROID_T  # ctypes idiosyncrasy


class DeviceAnchorPersistenceCreateInfoANDROID(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.DEVICE_ANCHOR_PERSISTENCE_CREATE_INFO_ANDROID,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.DeviceAnchorPersistenceCreateInfoANDROID(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.DeviceAnchorPersistenceCreateInfoANDROID(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class PersistedAnchorSpaceCreateInfoANDROID(Structure):
    def __init__(
        self,
        anchor_id: UuidEXT = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.PERSISTED_ANCHOR_SPACE_CREATE_INFO_ANDROID,
    ) -> None:
        super().__init__(
            anchor_id=anchor_id,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PersistedAnchorSpaceCreateInfoANDROID(anchor_id={repr(self.anchor_id)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PersistedAnchorSpaceCreateInfoANDROID(anchor_id={self.anchor_id}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("anchor_id", UuidEXT),
    ]


class PersistedAnchorSpaceInfoANDROID(Structure):
    def __init__(
        self,
        anchor: Space = None,
        next: c_void_p = None,
        type: StructureType = StructureType.PERSISTED_ANCHOR_SPACE_INFO_ANDROID,
    ) -> None:
        super().__init__(
            anchor=anchor,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PersistedAnchorSpaceInfoANDROID(anchor={repr(self.anchor)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PersistedAnchorSpaceInfoANDROID(anchor={self.anchor}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("anchor", Space),
    ]


class SystemDeviceAnchorPersistencePropertiesANDROID(Structure):
    def __init__(
        self,
        supports_anchor_persistence: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_DEVICE_ANCHOR_PERSISTENCE_PROPERTIES_ANDROID,
    ) -> None:
        super().__init__(
            supports_anchor_persistence=supports_anchor_persistence,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemDeviceAnchorPersistencePropertiesANDROID(supports_anchor_persistence={repr(self.supports_anchor_persistence)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemDeviceAnchorPersistencePropertiesANDROID(supports_anchor_persistence={self.supports_anchor_persistence}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_anchor_persistence", Bool32),
    ]


PFN_xrEnumerateSupportedPersistenceAnchorTypesANDROID = CFUNCTYPE(Result.ctype(), Instance, SystemId, c_uint32, POINTER(c_uint32), POINTER(TrackableTypeANDROID.ctype()))

PFN_xrCreateDeviceAnchorPersistenceANDROID = CFUNCTYPE(Result.ctype(), Session, POINTER(DeviceAnchorPersistenceCreateInfoANDROID), POINTER(DeviceAnchorPersistenceANDROID))

PFN_xrDestroyDeviceAnchorPersistenceANDROID = CFUNCTYPE(Result.ctype(), DeviceAnchorPersistenceANDROID)

PFN_xrPersistAnchorANDROID = CFUNCTYPE(Result.ctype(), DeviceAnchorPersistenceANDROID, POINTER(PersistedAnchorSpaceInfoANDROID), POINTER(UuidEXT))

PFN_xrGetAnchorPersistStateANDROID = CFUNCTYPE(Result.ctype(), DeviceAnchorPersistenceANDROID, POINTER(Uuid), POINTER(AnchorPersistStateANDROID.ctype()))

PFN_xrCreatePersistedAnchorSpaceANDROID = CFUNCTYPE(Result.ctype(), DeviceAnchorPersistenceANDROID, POINTER(PersistedAnchorSpaceCreateInfoANDROID), POINTER(Space))

PFN_xrEnumeratePersistedAnchorsANDROID = CFUNCTYPE(Result.ctype(), DeviceAnchorPersistenceANDROID, c_uint32, POINTER(c_uint32), POINTER(UuidEXT))

PFN_xrUnpersistAnchorANDROID = CFUNCTYPE(Result.ctype(), DeviceAnchorPersistenceANDROID, POINTER(Uuid))


class SystemPassthroughCameraStatePropertiesANDROID(Structure):
    def __init__(
        self,
        supports_passthrough_camera_state: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_PASSTHROUGH_CAMERA_STATE_PROPERTIES_ANDROID,
    ) -> None:
        super().__init__(
            supports_passthrough_camera_state=supports_passthrough_camera_state,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemPassthroughCameraStatePropertiesANDROID(supports_passthrough_camera_state={repr(self.supports_passthrough_camera_state)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemPassthroughCameraStatePropertiesANDROID(supports_passthrough_camera_state={self.supports_passthrough_camera_state}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_passthrough_camera_state", Bool32),
    ]


class PassthroughCameraStateGetInfoANDROID(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.PASSTHROUGH_CAMERA_STATE_GET_INFO_ANDROID,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PassthroughCameraStateGetInfoANDROID(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PassthroughCameraStateGetInfoANDROID(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


PFN_xrGetPassthroughCameraStateANDROID = CFUNCTYPE(Result.ctype(), Session, POINTER(PassthroughCameraStateGetInfoANDROID), POINTER(PassthroughCameraStateANDROID.ctype()))


class RaycastInfoANDROID(Structure):
    def __init__(
        self,
        max_results: int = 0,
        tracker_count: Optional[int] = None,
        trackers: ArrayFieldParamType[TrackableTrackerANDROID] = None,
        origin: Vector3f = None,
        trajectory: Vector3f = None,
        space: Space = None,
        time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.RAYCAST_INFO_ANDROID,
    ) -> None:
        tracker_count, trackers = array_field_helper(
            TrackableTrackerANDROID, tracker_count, trackers)
        if origin is None:
            origin = Vector3f()
        if trajectory is None:
            trajectory = Vector3f()
        super().__init__(
            max_results=max_results,
            tracker_count=tracker_count,
            _trackers=trackers,
            origin=origin,
            trajectory=trajectory,
            space=space,
            time=time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.RaycastInfoANDROID(max_results={repr(self.max_results)}, tracker_count={repr(self.tracker_count)}, trackers={repr(self._trackers)}, origin={repr(self.origin)}, trajectory={repr(self.trajectory)}, space={repr(self.space)}, time={repr(self.time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.RaycastInfoANDROID(max_results={self.max_results}, tracker_count={self.tracker_count}, trackers={self._trackers}, origin={self.origin}, trajectory={self.trajectory}, space={self.space}, time={self.time}, next={self.next}, type={self.type})"

    @property
    def trackers(self):
        if self.tracker_count == 0:
            return (TrackableTrackerANDROID * 0)()
        else:
            return (TrackableTrackerANDROID * self.tracker_count).from_address(
                ctypes.addressof(self._trackers.contents))

    @trackers.setter
    def trackers(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.tracker_count, self._trackers = array_field_helper(
            TrackableTrackerANDROID, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("max_results", c_uint32),
        ("tracker_count", c_uint32),
        ("_trackers", POINTER(TrackableTrackerANDROID)),
        ("origin", Vector3f),
        ("trajectory", Vector3f),
        ("space", Space),
        ("time", Time),
    ]


class RaycastHitResultANDROID(Structure):
    def __init__(
        self,
        type: TrackableTypeANDROID = TrackableTypeANDROID(),  # noqa
        trackable: TrackableANDROID = 0,
        pose: Posef = Posef(),
    ) -> None:
        super().__init__(
            type=TrackableTypeANDROID(type).value,
            trackable=trackable,
            pose=pose,
        )

    def __repr__(self) -> str:
        return f"xr.RaycastHitResultANDROID(type={repr(self.type)}, trackable={repr(self.trackable)}, pose={repr(self.pose)})"

    def __str__(self) -> str:
        return f"xr.RaycastHitResultANDROID(type={self.type}, trackable={self.trackable}, pose={self.pose})"

    _fields_ = [
        ("type", TrackableTypeANDROID.ctype()),
        ("trackable", TrackableANDROID),
        ("pose", Posef),
    ]


class RaycastHitResultsANDROID(Structure):
    def __init__(
        self,
        results_capacity_input: int = 0,
        results_count_output: int = 0,
        results: POINTER(RaycastHitResultANDROID) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.RAYCAST_HIT_RESULTS_ANDROID,
    ) -> None:
        super().__init__(
            results_capacity_input=results_capacity_input,
            results_count_output=results_count_output,
            results=results,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.RaycastHitResultsANDROID(results_capacity_input={repr(self.results_capacity_input)}, results_count_output={repr(self.results_count_output)}, results={repr(self.results)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.RaycastHitResultsANDROID(results_capacity_input={self.results_capacity_input}, results_count_output={self.results_count_output}, results={self.results}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("results_capacity_input", c_uint32),
        ("results_count_output", c_uint32),
        ("results", POINTER(RaycastHitResultANDROID)),
    ]


PFN_xrEnumerateRaycastSupportedTrackableTypesANDROID = CFUNCTYPE(Result.ctype(), Instance, SystemId, c_uint32, POINTER(c_uint32), POINTER(TrackableTypeANDROID.ctype()))

PFN_xrRaycastANDROID = CFUNCTYPE(Result.ctype(), Session, POINTER(RaycastInfoANDROID), POINTER(RaycastHitResultsANDROID))


class TrackableObjectANDROID(Structure):
    def __init__(
        self,
        tracking_state: TrackingStateANDROID = TrackingStateANDROID(),  # noqa
        center_pose: Posef = Posef(),
        extents: Extent3DfEXT = 0,
        object_label: ObjectLabelANDROID = ObjectLabelANDROID(),  # noqa
        last_updated_time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.TRACKABLE_OBJECT_ANDROID,
    ) -> None:
        super().__init__(
            tracking_state=TrackingStateANDROID(tracking_state).value,
            center_pose=center_pose,
            extents=extents,
            object_label=ObjectLabelANDROID(object_label).value,
            last_updated_time=last_updated_time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.TrackableObjectANDROID(tracking_state={repr(self.tracking_state)}, center_pose={repr(self.center_pose)}, extents={repr(self.extents)}, object_label={repr(self.object_label)}, last_updated_time={repr(self.last_updated_time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.TrackableObjectANDROID(tracking_state={self.tracking_state}, center_pose={self.center_pose}, extents={self.extents}, object_label={self.object_label}, last_updated_time={self.last_updated_time}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("tracking_state", TrackingStateANDROID.ctype()),
        ("center_pose", Posef),
        ("extents", Extent3DfEXT),
        ("object_label", ObjectLabelANDROID.ctype()),
        ("last_updated_time", Time),
    ]


class TrackableObjectConfigurationANDROID(Structure):
    def __init__(
        self,
        label_count: Optional[int] = None,
        active_labels: ArrayFieldParamType[c_int] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.TRACKABLE_OBJECT_CONFIGURATION_ANDROID,
    ) -> None:
        label_count, active_labels = array_field_helper(
            c_int, label_count, active_labels)
        super().__init__(
            label_count=label_count,
            _active_labels=active_labels,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.TrackableObjectConfigurationANDROID(label_count={repr(self.label_count)}, active_labels={repr(self._active_labels)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.TrackableObjectConfigurationANDROID(label_count={self.label_count}, active_labels={self._active_labels}, next={self.next}, type={self.type})"

    @property
    def active_labels(self):
        if self.label_count == 0:
            return (c_int * 0)()
        else:
            return (c_int * self.label_count).from_address(
                ctypes.addressof(self._active_labels.contents))

    @active_labels.setter
    def active_labels(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.label_count, self._active_labels = array_field_helper(
            c_int, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("label_count", c_uint32),
        ("_active_labels", POINTER(c_int)),
    ]


PFN_xrGetTrackableObjectANDROID = CFUNCTYPE(Result.ctype(), TrackableTrackerANDROID, POINTER(TrackableGetInfoANDROID), POINTER(TrackableObjectANDROID))


class FutureCancelInfoEXT(Structure):
    def __init__(
        self,
        future: FutureEXT = None,
        next: c_void_p = None,
        type: StructureType = StructureType.FUTURE_CANCEL_INFO_EXT,
    ) -> None:
        super().__init__(
            future=future,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FutureCancelInfoEXT(future={repr(self.future)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FutureCancelInfoEXT(future={self.future}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("future", FutureEXT),
    ]


class FuturePollInfoEXT(Structure):
    def __init__(
        self,
        future: FutureEXT = None,
        next: c_void_p = None,
        type: StructureType = StructureType.FUTURE_POLL_INFO_EXT,
    ) -> None:
        super().__init__(
            future=future,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FuturePollInfoEXT(future={repr(self.future)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FuturePollInfoEXT(future={self.future}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("future", FutureEXT),
    ]


class FutureCompletionBaseHeaderEXT(Structure):
    def __init__(
        self,
        future_result: Result = Result(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        super().__init__(
            future_result=Result(future_result).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FutureCompletionBaseHeaderEXT(future_result={repr(self.future_result)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FutureCompletionBaseHeaderEXT(future_result={self.future_result}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("future_result", Result.ctype()),
    ]


class FuturePollResultEXT(Structure):
    def __init__(
        self,
        state: FutureStateEXT = FutureStateEXT(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.FUTURE_POLL_RESULT_EXT,
    ) -> None:
        super().__init__(
            state=FutureStateEXT(state).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FuturePollResultEXT(state={repr(self.state)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FuturePollResultEXT(state={self.state}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("state", FutureStateEXT.ctype()),
    ]


PFN_xrPollFutureEXT = CFUNCTYPE(Result.ctype(), Instance, POINTER(FuturePollInfoEXT), POINTER(FuturePollResultEXT))

PFN_xrCancelFutureEXT = CFUNCTYPE(Result.ctype(), Instance, POINTER(FutureCancelInfoEXT))


class EventDataUserPresenceChangedEXT(Structure):
    def __init__(
        self,
        session: Session = None,
        is_user_present: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_USER_PRESENCE_CHANGED_EXT,
    ) -> None:
        super().__init__(
            session=session,
            is_user_present=is_user_present,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataUserPresenceChangedEXT(session={repr(self.session)}, is_user_present={repr(self.is_user_present)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataUserPresenceChangedEXT(session={self.session}, is_user_present={self.is_user_present}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("session", Session),
        ("is_user_present", Bool32),
    ]


class SystemUserPresencePropertiesEXT(Structure):
    def __init__(
        self,
        supports_user_presence: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_USER_PRESENCE_PROPERTIES_EXT,
    ) -> None:
        super().__init__(
            supports_user_presence=supports_user_presence,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemUserPresencePropertiesEXT(supports_user_presence={repr(self.supports_user_presence)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemUserPresencePropertiesEXT(supports_user_presence={self.supports_user_presence}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_user_presence", Bool32),
    ]


class EventDataHeadsetFitChangedML(Structure):
    def __init__(
        self,
        status: HeadsetFitStatusML = HeadsetFitStatusML(),  # noqa
        time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_HEADSET_FIT_CHANGED_ML,
    ) -> None:
        super().__init__(
            status=HeadsetFitStatusML(status).value,
            time=time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataHeadsetFitChangedML(status={repr(self.status)}, time={repr(self.time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataHeadsetFitChangedML(status={self.status}, time={self.time}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("status", HeadsetFitStatusML.ctype()),
        ("time", Time),
    ]


class EventDataEyeCalibrationChangedML(Structure):
    def __init__(
        self,
        status: EyeCalibrationStatusML = EyeCalibrationStatusML(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_EYE_CALIBRATION_CHANGED_ML,
    ) -> None:
        super().__init__(
            status=EyeCalibrationStatusML(status).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataEyeCalibrationChangedML(status={repr(self.status)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataEyeCalibrationChangedML(status={self.status}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("status", EyeCalibrationStatusML.ctype()),
    ]


class UserCalibrationEnableEventsInfoML(Structure):
    def __init__(
        self,
        enabled: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.USER_CALIBRATION_ENABLE_EVENTS_INFO_ML,
    ) -> None:
        super().__init__(
            enabled=enabled,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.UserCalibrationEnableEventsInfoML(enabled={repr(self.enabled)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.UserCalibrationEnableEventsInfoML(enabled={self.enabled}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("enabled", Bool32),
    ]


PFN_xrEnableUserCalibrationEventsML = CFUNCTYPE(Result.ctype(), Instance, POINTER(UserCalibrationEnableEventsInfoML))


class SystemNotificationsSetInfoML(Structure):
    def __init__(
        self,
        suppress_notifications: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_NOTIFICATIONS_SET_INFO_ML,
    ) -> None:
        super().__init__(
            suppress_notifications=suppress_notifications,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemNotificationsSetInfoML(suppress_notifications={repr(self.suppress_notifications)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemNotificationsSetInfoML(suppress_notifications={self.suppress_notifications}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("suppress_notifications", Bool32),
    ]


PFN_xrSetSystemNotificationsML = CFUNCTYPE(Result.ctype(), Instance, POINTER(SystemNotificationsSetInfoML))


class WorldMeshDetectorML_T(Structure):
    pass


class WorldMeshDetectorML(POINTER(WorldMeshDetectorML_T), HandleMixin):
    _type_ = WorldMeshDetectorML_T  # ctypes idiosyncrasy

WorldMeshDetectorFlagsMLCInt = Flags64


class WorldMeshDetectorCreateInfoML(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.WORLD_MESH_DETECTOR_CREATE_INFO_ML,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.WorldMeshDetectorCreateInfoML(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.WorldMeshDetectorCreateInfoML(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class WorldMeshBlockStateML(Structure):
    def __init__(
        self,
        uuid: UuidEXT = 0,
        mesh_bounding_box_center: Posef = Posef(),
        mesh_bounding_box_extents: Extent3DfEXT = 0,
        last_update_time: Time = 0,
        status: WorldMeshBlockStatusML = WorldMeshBlockStatusML(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.WORLD_MESH_BLOCK_STATE_ML,
    ) -> None:
        super().__init__(
            uuid=uuid,
            mesh_bounding_box_center=mesh_bounding_box_center,
            mesh_bounding_box_extents=mesh_bounding_box_extents,
            last_update_time=last_update_time,
            status=WorldMeshBlockStatusML(status).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.WorldMeshBlockStateML(uuid={repr(self.uuid)}, mesh_bounding_box_center={repr(self.mesh_bounding_box_center)}, mesh_bounding_box_extents={repr(self.mesh_bounding_box_extents)}, last_update_time={repr(self.last_update_time)}, status={repr(self.status)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.WorldMeshBlockStateML(uuid={self.uuid}, mesh_bounding_box_center={self.mesh_bounding_box_center}, mesh_bounding_box_extents={self.mesh_bounding_box_extents}, last_update_time={self.last_update_time}, status={self.status}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("uuid", UuidEXT),
        ("mesh_bounding_box_center", Posef),
        ("mesh_bounding_box_extents", Extent3DfEXT),
        ("last_update_time", Time),
        ("status", WorldMeshBlockStatusML.ctype()),
    ]


class WorldMeshStateRequestInfoML(Structure):
    def __init__(
        self,
        base_space: Space = None,
        time: Time = 0,
        bounding_box_center: Posef = Posef(),
        bounding_box_extents: Extent3DfEXT = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.WORLD_MESH_STATE_REQUEST_INFO_ML,
    ) -> None:
        super().__init__(
            base_space=base_space,
            time=time,
            bounding_box_center=bounding_box_center,
            bounding_box_extents=bounding_box_extents,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.WorldMeshStateRequestInfoML(base_space={repr(self.base_space)}, time={repr(self.time)}, bounding_box_center={repr(self.bounding_box_center)}, bounding_box_extents={repr(self.bounding_box_extents)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.WorldMeshStateRequestInfoML(base_space={self.base_space}, time={self.time}, bounding_box_center={self.bounding_box_center}, bounding_box_extents={self.bounding_box_extents}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("base_space", Space),
        ("time", Time),
        ("bounding_box_center", Posef),
        ("bounding_box_extents", Extent3DfEXT),
    ]


class WorldMeshStateRequestCompletionML(Structure):
    def __init__(
        self,
        future_result: Result = Result(),  # noqa
        timestamp: Time = 0,
        mesh_block_state_capacity_input: int = 0,
        mesh_block_state_count_output: int = 0,
        mesh_block_states: POINTER(WorldMeshBlockStateML) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.WORLD_MESH_STATE_REQUEST_COMPLETION_ML,
    ) -> None:
        super().__init__(
            future_result=Result(future_result).value,
            timestamp=timestamp,
            mesh_block_state_capacity_input=mesh_block_state_capacity_input,
            mesh_block_state_count_output=mesh_block_state_count_output,
            mesh_block_states=mesh_block_states,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.WorldMeshStateRequestCompletionML(future_result={repr(self.future_result)}, timestamp={repr(self.timestamp)}, mesh_block_state_capacity_input={repr(self.mesh_block_state_capacity_input)}, mesh_block_state_count_output={repr(self.mesh_block_state_count_output)}, mesh_block_states={repr(self.mesh_block_states)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.WorldMeshStateRequestCompletionML(future_result={self.future_result}, timestamp={self.timestamp}, mesh_block_state_capacity_input={self.mesh_block_state_capacity_input}, mesh_block_state_count_output={self.mesh_block_state_count_output}, mesh_block_states={self.mesh_block_states}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("future_result", Result.ctype()),
        ("timestamp", Time),
        ("mesh_block_state_capacity_input", c_uint32),
        ("mesh_block_state_count_output", c_uint32),
        ("mesh_block_states", POINTER(WorldMeshBlockStateML)),
    ]


class WorldMeshBufferRecommendedSizeInfoML(Structure):
    def __init__(
        self,
        max_block_count: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.WORLD_MESH_BUFFER_RECOMMENDED_SIZE_INFO_ML,
    ) -> None:
        super().__init__(
            max_block_count=max_block_count,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.WorldMeshBufferRecommendedSizeInfoML(max_block_count={repr(self.max_block_count)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.WorldMeshBufferRecommendedSizeInfoML(max_block_count={self.max_block_count}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("max_block_count", c_uint32),
    ]


class WorldMeshBufferSizeML(Structure):
    def __init__(
        self,
        size: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.WORLD_MESH_BUFFER_SIZE_ML,
    ) -> None:
        super().__init__(
            size=size,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.WorldMeshBufferSizeML(size={repr(self.size)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.WorldMeshBufferSizeML(size={self.size}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("size", c_uint32),
    ]


class WorldMeshBufferML(Structure):
    def __init__(
        self,
        buffer_size: int = 0,
        buffer: c_void_p = None,
        next: c_void_p = None,
        type: StructureType = StructureType.WORLD_MESH_BUFFER_ML,
    ) -> None:
        super().__init__(
            buffer_size=buffer_size,
            buffer=buffer,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.WorldMeshBufferML(buffer_size={repr(self.buffer_size)}, buffer={repr(self.buffer)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.WorldMeshBufferML(buffer_size={self.buffer_size}, buffer={self.buffer}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("buffer_size", c_uint32),
        ("buffer", c_void_p),
    ]


class WorldMeshBlockRequestML(Structure):
    def __init__(
        self,
        uuid: UuidEXT = 0,
        lod: WorldMeshDetectorLodML = WorldMeshDetectorLodML(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.WORLD_MESH_BLOCK_REQUEST_ML,
    ) -> None:
        super().__init__(
            uuid=uuid,
            lod=WorldMeshDetectorLodML(lod).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.WorldMeshBlockRequestML(uuid={repr(self.uuid)}, lod={repr(self.lod)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.WorldMeshBlockRequestML(uuid={self.uuid}, lod={self.lod}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("uuid", UuidEXT),
        ("lod", WorldMeshDetectorLodML.ctype()),
    ]


class WorldMeshGetInfoML(Structure):
    def __init__(
        self,
        flags: WorldMeshDetectorFlagsML = WorldMeshDetectorFlagsML(),  # noqa
        fill_hole_length: float = 0,
        disconnected_component_area: float = 0,
        block_count: Optional[int] = None,
        blocks: ArrayFieldParamType[WorldMeshBlockRequestML] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.WORLD_MESH_GET_INFO_ML,
    ) -> None:
        block_count, blocks = array_field_helper(
            WorldMeshBlockRequestML, block_count, blocks)
        super().__init__(
            flags=WorldMeshDetectorFlagsML(flags).value,
            fill_hole_length=fill_hole_length,
            disconnected_component_area=disconnected_component_area,
            block_count=block_count,
            _blocks=blocks,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.WorldMeshGetInfoML(flags={repr(self.flags)}, fill_hole_length={repr(self.fill_hole_length)}, disconnected_component_area={repr(self.disconnected_component_area)}, block_count={repr(self.block_count)}, blocks={repr(self._blocks)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.WorldMeshGetInfoML(flags={self.flags}, fill_hole_length={self.fill_hole_length:.3f}, disconnected_component_area={self.disconnected_component_area:.3f}, block_count={self.block_count}, blocks={self._blocks}, next={self.next}, type={self.type})"

    @property
    def blocks(self):
        if self.block_count == 0:
            return (WorldMeshBlockRequestML * 0)()
        else:
            return (WorldMeshBlockRequestML * self.block_count).from_address(
                ctypes.addressof(self._blocks.contents))

    @blocks.setter
    def blocks(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.block_count, self._blocks = array_field_helper(
            WorldMeshBlockRequestML, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("flags", WorldMeshDetectorFlagsMLCInt),
        ("fill_hole_length", c_float),
        ("disconnected_component_area", c_float),
        ("block_count", c_uint32),
        ("_blocks", POINTER(WorldMeshBlockRequestML)),
    ]


class WorldMeshBlockML(Structure):
    def __init__(
        self,
        uuid: UuidEXT = 0,
        block_result: WorldMeshBlockResultML = WorldMeshBlockResultML(),  # noqa
        lod: WorldMeshDetectorLodML = WorldMeshDetectorLodML(),  # noqa
        flags: WorldMeshDetectorFlagsML = WorldMeshDetectorFlagsML(),  # noqa
        index_count: int = 0,
        index_buffer: POINTER(c_uint16) = None,
        vertex_count: int = 0,
        vertex_buffer: POINTER(Vector3f) = None,
        normal_count: int = 0,
        normal_buffer: POINTER(Vector3f) = None,
        confidence_count: int = 0,
        confidence_buffer: POINTER(c_float) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.WORLD_MESH_BLOCK_ML,
    ) -> None:
        super().__init__(
            uuid=uuid,
            block_result=WorldMeshBlockResultML(block_result).value,
            lod=WorldMeshDetectorLodML(lod).value,
            flags=WorldMeshDetectorFlagsML(flags).value,
            index_count=index_count,
            index_buffer=index_buffer,
            vertex_count=vertex_count,
            vertex_buffer=vertex_buffer,
            normal_count=normal_count,
            normal_buffer=normal_buffer,
            confidence_count=confidence_count,
            confidence_buffer=confidence_buffer,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.WorldMeshBlockML(uuid={repr(self.uuid)}, block_result={repr(self.block_result)}, lod={repr(self.lod)}, flags={repr(self.flags)}, index_count={repr(self.index_count)}, index_buffer={repr(self.index_buffer)}, vertex_count={repr(self.vertex_count)}, vertex_buffer={repr(self.vertex_buffer)}, normal_count={repr(self.normal_count)}, normal_buffer={repr(self.normal_buffer)}, confidence_count={repr(self.confidence_count)}, confidence_buffer={repr(self.confidence_buffer)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.WorldMeshBlockML(uuid={self.uuid}, block_result={self.block_result}, lod={self.lod}, flags={self.flags}, index_count={self.index_count}, index_buffer={self.index_buffer}, vertex_count={self.vertex_count}, vertex_buffer={self.vertex_buffer}, normal_count={self.normal_count}, normal_buffer={self.normal_buffer}, confidence_count={self.confidence_count}, confidence_buffer={self.confidence_buffer}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("uuid", UuidEXT),
        ("block_result", WorldMeshBlockResultML.ctype()),
        ("lod", WorldMeshDetectorLodML.ctype()),
        ("flags", WorldMeshDetectorFlagsMLCInt),
        ("index_count", c_uint32),
        ("index_buffer", POINTER(c_uint16)),
        ("vertex_count", c_uint32),
        ("vertex_buffer", POINTER(Vector3f)),
        ("normal_count", c_uint32),
        ("normal_buffer", POINTER(Vector3f)),
        ("confidence_count", c_uint32),
        ("confidence_buffer", POINTER(c_float)),
    ]


class WorldMeshRequestCompletionInfoML(Structure):
    def __init__(
        self,
        mesh_space: Space = None,
        mesh_space_locate_time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.WORLD_MESH_REQUEST_COMPLETION_INFO_ML,
    ) -> None:
        super().__init__(
            mesh_space=mesh_space,
            mesh_space_locate_time=mesh_space_locate_time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.WorldMeshRequestCompletionInfoML(mesh_space={repr(self.mesh_space)}, mesh_space_locate_time={repr(self.mesh_space_locate_time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.WorldMeshRequestCompletionInfoML(mesh_space={self.mesh_space}, mesh_space_locate_time={self.mesh_space_locate_time}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("mesh_space", Space),
        ("mesh_space_locate_time", Time),
    ]


class WorldMeshRequestCompletionML(Structure):
    def __init__(
        self,
        future_result: Result = Result(),  # noqa
        block_count: Optional[int] = None,
        blocks: ArrayFieldParamType[WorldMeshBlockML] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.WORLD_MESH_REQUEST_COMPLETION_ML,
    ) -> None:
        block_count, blocks = array_field_helper(
            WorldMeshBlockML, block_count, blocks)
        super().__init__(
            future_result=Result(future_result).value,
            block_count=block_count,
            _blocks=blocks,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.WorldMeshRequestCompletionML(future_result={repr(self.future_result)}, block_count={repr(self.block_count)}, blocks={repr(self._blocks)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.WorldMeshRequestCompletionML(future_result={self.future_result}, block_count={self.block_count}, blocks={self._blocks}, next={self.next}, type={self.type})"

    @property
    def blocks(self):
        if self.block_count == 0:
            return (WorldMeshBlockML * 0)()
        else:
            return (WorldMeshBlockML * self.block_count).from_address(
                ctypes.addressof(self._blocks.contents))

    @blocks.setter
    def blocks(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.block_count, self._blocks = array_field_helper(
            WorldMeshBlockML, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("future_result", Result.ctype()),
        ("block_count", c_uint32),
        ("_blocks", POINTER(WorldMeshBlockML)),
    ]


PFN_xrCreateWorldMeshDetectorML = CFUNCTYPE(Result.ctype(), Session, POINTER(WorldMeshDetectorCreateInfoML), POINTER(WorldMeshDetectorML))

PFN_xrDestroyWorldMeshDetectorML = CFUNCTYPE(Result.ctype(), WorldMeshDetectorML)

PFN_xrRequestWorldMeshStateAsyncML = CFUNCTYPE(Result.ctype(), WorldMeshDetectorML, POINTER(WorldMeshStateRequestInfoML), POINTER(FutureEXT))

PFN_xrRequestWorldMeshStateCompleteML = CFUNCTYPE(Result.ctype(), WorldMeshDetectorML, FutureEXT, POINTER(WorldMeshStateRequestCompletionML))

PFN_xrGetWorldMeshBufferRecommendSizeML = CFUNCTYPE(Result.ctype(), WorldMeshDetectorML, POINTER(WorldMeshBufferRecommendedSizeInfoML), POINTER(WorldMeshBufferSizeML))

PFN_xrAllocateWorldMeshBufferML = CFUNCTYPE(Result.ctype(), WorldMeshDetectorML, POINTER(WorldMeshBufferSizeML), POINTER(WorldMeshBufferML))

PFN_xrFreeWorldMeshBufferML = CFUNCTYPE(Result.ctype(), WorldMeshDetectorML, POINTER(WorldMeshBufferML))

PFN_xrRequestWorldMeshAsyncML = CFUNCTYPE(Result.ctype(), WorldMeshDetectorML, POINTER(WorldMeshGetInfoML), POINTER(WorldMeshBufferML), POINTER(FutureEXT))

PFN_xrRequestWorldMeshCompleteML = CFUNCTYPE(Result.ctype(), WorldMeshDetectorML, POINTER(WorldMeshRequestCompletionInfoML), FutureEXT, POINTER(WorldMeshRequestCompletionML))


class FacialExpressionClientML_T(Structure):
    pass


class FacialExpressionClientML(POINTER(FacialExpressionClientML_T), HandleMixin):
    _type_ = FacialExpressionClientML_T  # ctypes idiosyncrasy

FacialExpressionBlendShapePropertiesFlagsMLCInt = Flags64


class SystemFacialExpressionPropertiesML(Structure):
    def __init__(
        self,
        supports_facial_expression: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_FACIAL_EXPRESSION_PROPERTIES_ML,
    ) -> None:
        super().__init__(
            supports_facial_expression=supports_facial_expression,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemFacialExpressionPropertiesML(supports_facial_expression={repr(self.supports_facial_expression)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemFacialExpressionPropertiesML(supports_facial_expression={self.supports_facial_expression}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_facial_expression", Bool32),
    ]


class FacialExpressionClientCreateInfoML(Structure):
    def __init__(
        self,
        requested_count: Optional[int] = None,
        requested_facial_blend_shapes: ArrayFieldParamType[c_int] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.FACIAL_EXPRESSION_CLIENT_CREATE_INFO_ML,
    ) -> None:
        requested_count, requested_facial_blend_shapes = array_field_helper(
            c_int, requested_count, requested_facial_blend_shapes)
        super().__init__(
            requested_count=requested_count,
            _requested_facial_blend_shapes=requested_facial_blend_shapes,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FacialExpressionClientCreateInfoML(requested_count={repr(self.requested_count)}, requested_facial_blend_shapes={repr(self._requested_facial_blend_shapes)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FacialExpressionClientCreateInfoML(requested_count={self.requested_count}, requested_facial_blend_shapes={self._requested_facial_blend_shapes}, next={self.next}, type={self.type})"

    @property
    def requested_facial_blend_shapes(self):
        if self.requested_count == 0:
            return (c_int * 0)()
        else:
            return (c_int * self.requested_count).from_address(
                ctypes.addressof(self._requested_facial_blend_shapes.contents))

    @requested_facial_blend_shapes.setter
    def requested_facial_blend_shapes(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.requested_count, self._requested_facial_blend_shapes = array_field_helper(
            c_int, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("requested_count", c_uint32),
        ("_requested_facial_blend_shapes", POINTER(c_int)),
    ]


class FacialExpressionBlendShapeGetInfoML(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.FACIAL_EXPRESSION_BLEND_SHAPE_GET_INFO_ML,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FacialExpressionBlendShapeGetInfoML(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FacialExpressionBlendShapeGetInfoML(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class FacialExpressionBlendShapePropertiesML(Structure):
    def __init__(
        self,
        requested_facial_blend_shape: FacialBlendShapeML = FacialBlendShapeML(),  # noqa
        weight: float = 0,
        flags: FacialExpressionBlendShapePropertiesFlagsML = FacialExpressionBlendShapePropertiesFlagsML(),  # noqa
        time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.FACIAL_EXPRESSION_BLEND_SHAPE_PROPERTIES_ML,
    ) -> None:
        super().__init__(
            requested_facial_blend_shape=FacialBlendShapeML(requested_facial_blend_shape).value,
            weight=weight,
            flags=FacialExpressionBlendShapePropertiesFlagsML(flags).value,
            time=time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.FacialExpressionBlendShapePropertiesML(requested_facial_blend_shape={repr(self.requested_facial_blend_shape)}, weight={repr(self.weight)}, flags={repr(self.flags)}, time={repr(self.time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.FacialExpressionBlendShapePropertiesML(requested_facial_blend_shape={self.requested_facial_blend_shape}, weight={self.weight:.3f}, flags={self.flags}, time={self.time}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("requested_facial_blend_shape", FacialBlendShapeML.ctype()),
        ("weight", c_float),
        ("flags", FacialExpressionBlendShapePropertiesFlagsMLCInt),
        ("time", Time),
    ]


PFN_xrCreateFacialExpressionClientML = CFUNCTYPE(Result.ctype(), Session, POINTER(FacialExpressionClientCreateInfoML), POINTER(FacialExpressionClientML))

PFN_xrDestroyFacialExpressionClientML = CFUNCTYPE(Result.ctype(), FacialExpressionClientML)

PFN_xrGetFacialExpressionBlendShapePropertiesML = CFUNCTYPE(Result.ctype(), FacialExpressionClientML, POINTER(FacialExpressionBlendShapeGetInfoML), c_uint32, POINTER(FacialExpressionBlendShapePropertiesML))


class SystemSimultaneousHandsAndControllersPropertiesMETA(Structure):
    def __init__(
        self,
        supports_simultaneous_hands_and_controllers: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_SIMULTANEOUS_HANDS_AND_CONTROLLERS_PROPERTIES_META,
    ) -> None:
        super().__init__(
            supports_simultaneous_hands_and_controllers=supports_simultaneous_hands_and_controllers,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemSimultaneousHandsAndControllersPropertiesMETA(supports_simultaneous_hands_and_controllers={repr(self.supports_simultaneous_hands_and_controllers)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemSimultaneousHandsAndControllersPropertiesMETA(supports_simultaneous_hands_and_controllers={self.supports_simultaneous_hands_and_controllers}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_simultaneous_hands_and_controllers", Bool32),
    ]


class SimultaneousHandsAndControllersTrackingResumeInfoMETA(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.SIMULTANEOUS_HANDS_AND_CONTROLLERS_TRACKING_RESUME_INFO_META,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SimultaneousHandsAndControllersTrackingResumeInfoMETA(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SimultaneousHandsAndControllersTrackingResumeInfoMETA(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class SimultaneousHandsAndControllersTrackingPauseInfoMETA(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.SIMULTANEOUS_HANDS_AND_CONTROLLERS_TRACKING_PAUSE_INFO_META,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SimultaneousHandsAndControllersTrackingPauseInfoMETA(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SimultaneousHandsAndControllersTrackingPauseInfoMETA(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


PFN_xrResumeSimultaneousHandsAndControllersTrackingMETA = CFUNCTYPE(Result.ctype(), Session, POINTER(SimultaneousHandsAndControllersTrackingResumeInfoMETA))

PFN_xrPauseSimultaneousHandsAndControllersTrackingMETA = CFUNCTYPE(Result.ctype(), Session, POINTER(SimultaneousHandsAndControllersTrackingPauseInfoMETA))


class ColocationDiscoveryStartInfoMETA(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.COLOCATION_DISCOVERY_START_INFO_META,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ColocationDiscoveryStartInfoMETA(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ColocationDiscoveryStartInfoMETA(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class ColocationDiscoveryStopInfoMETA(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.COLOCATION_DISCOVERY_STOP_INFO_META,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ColocationDiscoveryStopInfoMETA(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ColocationDiscoveryStopInfoMETA(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class ColocationAdvertisementStartInfoMETA(Structure):
    def __init__(
        self,
        buffer_size: int = 0,
        buffer: POINTER(c_uint8) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.COLOCATION_ADVERTISEMENT_START_INFO_META,
    ) -> None:
        super().__init__(
            buffer_size=buffer_size,
            buffer=buffer,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ColocationAdvertisementStartInfoMETA(buffer_size={repr(self.buffer_size)}, buffer={repr(self.buffer)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ColocationAdvertisementStartInfoMETA(buffer_size={self.buffer_size}, buffer={self.buffer}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("buffer_size", c_uint32),
        ("buffer", POINTER(c_uint8)),
    ]


class ColocationAdvertisementStopInfoMETA(Structure):
    def __init__(
        self,
        next: c_void_p = None,
        type: StructureType = StructureType.COLOCATION_ADVERTISEMENT_STOP_INFO_META,
    ) -> None:
        super().__init__(
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ColocationAdvertisementStopInfoMETA(next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ColocationAdvertisementStopInfoMETA(next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
    ]


class EventDataStartColocationAdvertisementCompleteMETA(Structure):
    def __init__(
        self,
        advertisement_request_id: AsyncRequestIdFB = 0,
        result: Result = Result(),  # noqa
        advertisement_uuid: Uuid = None,
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_START_COLOCATION_ADVERTISEMENT_COMPLETE_META,
    ) -> None:
        if advertisement_uuid is None:
            advertisement_uuid = Uuid()
        super().__init__(
            advertisement_request_id=advertisement_request_id,
            result=Result(result).value,
            advertisement_uuid=advertisement_uuid,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataStartColocationAdvertisementCompleteMETA(advertisement_request_id={repr(self.advertisement_request_id)}, result={repr(self.result)}, advertisement_uuid={repr(self.advertisement_uuid)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataStartColocationAdvertisementCompleteMETA(advertisement_request_id={self.advertisement_request_id}, result={self.result}, advertisement_uuid={self.advertisement_uuid}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("advertisement_request_id", AsyncRequestIdFB),
        ("result", Result.ctype()),
        ("advertisement_uuid", Uuid),
    ]


class EventDataStopColocationAdvertisementCompleteMETA(Structure):
    def __init__(
        self,
        request_id: AsyncRequestIdFB = 0,
        result: Result = Result(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_STOP_COLOCATION_ADVERTISEMENT_COMPLETE_META,
    ) -> None:
        super().__init__(
            request_id=request_id,
            result=Result(result).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataStopColocationAdvertisementCompleteMETA(request_id={repr(self.request_id)}, result={repr(self.result)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataStopColocationAdvertisementCompleteMETA(request_id={self.request_id}, result={self.result}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("request_id", AsyncRequestIdFB),
        ("result", Result.ctype()),
    ]


class EventDataColocationAdvertisementCompleteMETA(Structure):
    def __init__(
        self,
        advertisement_request_id: AsyncRequestIdFB = 0,
        result: Result = Result(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_COLOCATION_ADVERTISEMENT_COMPLETE_META,
    ) -> None:
        super().__init__(
            advertisement_request_id=advertisement_request_id,
            result=Result(result).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataColocationAdvertisementCompleteMETA(advertisement_request_id={repr(self.advertisement_request_id)}, result={repr(self.result)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataColocationAdvertisementCompleteMETA(advertisement_request_id={self.advertisement_request_id}, result={self.result}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("advertisement_request_id", AsyncRequestIdFB),
        ("result", Result.ctype()),
    ]


class EventDataStartColocationDiscoveryCompleteMETA(Structure):
    def __init__(
        self,
        discovery_request_id: AsyncRequestIdFB = 0,
        result: Result = Result(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_START_COLOCATION_DISCOVERY_COMPLETE_META,
    ) -> None:
        super().__init__(
            discovery_request_id=discovery_request_id,
            result=Result(result).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataStartColocationDiscoveryCompleteMETA(discovery_request_id={repr(self.discovery_request_id)}, result={repr(self.result)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataStartColocationDiscoveryCompleteMETA(discovery_request_id={self.discovery_request_id}, result={self.result}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("discovery_request_id", AsyncRequestIdFB),
        ("result", Result.ctype()),
    ]


class EventDataColocationDiscoveryResultMETA(Structure):
    def __init__(
        self,
        discovery_request_id: AsyncRequestIdFB = 0,
        advertisement_uuid: Uuid = None,
        buffer_size: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_COLOCATION_DISCOVERY_RESULT_META,
    ) -> None:
        if advertisement_uuid is None:
            advertisement_uuid = Uuid()
        super().__init__(
            discovery_request_id=discovery_request_id,
            advertisement_uuid=advertisement_uuid,
            buffer_size=buffer_size,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataColocationDiscoveryResultMETA(discovery_request_id={repr(self.discovery_request_id)}, advertisement_uuid={repr(self.advertisement_uuid)}, buffer_size={repr(self.buffer_size)}, buffer={repr(self.buffer)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataColocationDiscoveryResultMETA(discovery_request_id={self.discovery_request_id}, advertisement_uuid={self.advertisement_uuid}, buffer_size={self.buffer_size}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("discovery_request_id", AsyncRequestIdFB),
        ("advertisement_uuid", Uuid),
        ("buffer_size", c_uint32),
        ("buffer", (c_uint8 * 1024)),
    ]


class EventDataColocationDiscoveryCompleteMETA(Structure):
    def __init__(
        self,
        discovery_request_id: AsyncRequestIdFB = 0,
        result: Result = Result(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_COLOCATION_DISCOVERY_COMPLETE_META,
    ) -> None:
        super().__init__(
            discovery_request_id=discovery_request_id,
            result=Result(result).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataColocationDiscoveryCompleteMETA(discovery_request_id={repr(self.discovery_request_id)}, result={repr(self.result)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataColocationDiscoveryCompleteMETA(discovery_request_id={self.discovery_request_id}, result={self.result}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("discovery_request_id", AsyncRequestIdFB),
        ("result", Result.ctype()),
    ]


class EventDataStopColocationDiscoveryCompleteMETA(Structure):
    def __init__(
        self,
        request_id: AsyncRequestIdFB = 0,
        result: Result = Result(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_STOP_COLOCATION_DISCOVERY_COMPLETE_META,
    ) -> None:
        super().__init__(
            request_id=request_id,
            result=Result(result).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataStopColocationDiscoveryCompleteMETA(request_id={repr(self.request_id)}, result={repr(self.result)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataStopColocationDiscoveryCompleteMETA(request_id={self.request_id}, result={self.result}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("request_id", AsyncRequestIdFB),
        ("result", Result.ctype()),
    ]


class SystemColocationDiscoveryPropertiesMETA(Structure):
    def __init__(
        self,
        supports_colocation_discovery: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_COLOCATION_DISCOVERY_PROPERTIES_META,
    ) -> None:
        super().__init__(
            supports_colocation_discovery=supports_colocation_discovery,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemColocationDiscoveryPropertiesMETA(supports_colocation_discovery={repr(self.supports_colocation_discovery)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemColocationDiscoveryPropertiesMETA(supports_colocation_discovery={self.supports_colocation_discovery}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_colocation_discovery", Bool32),
    ]


PFN_xrStartColocationDiscoveryMETA = CFUNCTYPE(Result.ctype(), Session, POINTER(ColocationDiscoveryStartInfoMETA), POINTER(AsyncRequestIdFB))

PFN_xrStopColocationDiscoveryMETA = CFUNCTYPE(Result.ctype(), Session, POINTER(ColocationDiscoveryStopInfoMETA), POINTER(AsyncRequestIdFB))

PFN_xrStartColocationAdvertisementMETA = CFUNCTYPE(Result.ctype(), Session, POINTER(ColocationAdvertisementStartInfoMETA), POINTER(AsyncRequestIdFB))

PFN_xrStopColocationAdvertisementMETA = CFUNCTYPE(Result.ctype(), Session, POINTER(ColocationAdvertisementStopInfoMETA), POINTER(AsyncRequestIdFB))


class SystemSpatialEntityGroupSharingPropertiesMETA(Structure):
    def __init__(
        self,
        supports_spatial_entity_group_sharing: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_SPATIAL_ENTITY_GROUP_SHARING_PROPERTIES_META,
    ) -> None:
        super().__init__(
            supports_spatial_entity_group_sharing=supports_spatial_entity_group_sharing,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemSpatialEntityGroupSharingPropertiesMETA(supports_spatial_entity_group_sharing={repr(self.supports_spatial_entity_group_sharing)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemSpatialEntityGroupSharingPropertiesMETA(supports_spatial_entity_group_sharing={self.supports_spatial_entity_group_sharing}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_spatial_entity_group_sharing", Bool32),
    ]


class ShareSpacesRecipientGroupsMETA(Structure):
    def __init__(
        self,
        group_count: Optional[int] = None,
        groups: ArrayFieldParamType[Uuid] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SHARE_SPACES_RECIPIENT_GROUPS_META,
    ) -> None:
        group_count, groups = array_field_helper(
            Uuid, group_count, groups)
        super().__init__(
            group_count=group_count,
            _groups=groups,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.ShareSpacesRecipientGroupsMETA(group_count={repr(self.group_count)}, groups={repr(self._groups)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.ShareSpacesRecipientGroupsMETA(group_count={self.group_count}, groups={self._groups}, next={self.next}, type={self.type})"

    @property
    def groups(self):
        if self.group_count == 0:
            return (Uuid * 0)()
        else:
            return (Uuid * self.group_count).from_address(
                ctypes.addressof(self._groups.contents))

    @groups.setter
    def groups(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.group_count, self._groups = array_field_helper(
            Uuid, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("group_count", c_uint32),
        ("_groups", POINTER(Uuid)),
    ]


class SpaceGroupUuidFilterInfoMETA(Structure):
    def __init__(
        self,
        group_uuid: Uuid = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPACE_GROUP_UUID_FILTER_INFO_META,
    ) -> None:
        if group_uuid is None:
            group_uuid = Uuid()
        super().__init__(
            group_uuid=group_uuid,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpaceGroupUuidFilterInfoMETA(group_uuid={repr(self.group_uuid)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpaceGroupUuidFilterInfoMETA(group_uuid={self.group_uuid}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("group_uuid", Uuid),
    ]


class SystemMarkerTrackingPropertiesANDROID(Structure):
    def __init__(
        self,
        supports_marker_tracking: Bool32 = 0,
        supports_marker_size_estimation: Bool32 = 0,
        max_marker_count: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_MARKER_TRACKING_PROPERTIES_ANDROID,
    ) -> None:
        super().__init__(
            supports_marker_tracking=supports_marker_tracking,
            supports_marker_size_estimation=supports_marker_size_estimation,
            max_marker_count=max_marker_count,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemMarkerTrackingPropertiesANDROID(supports_marker_tracking={repr(self.supports_marker_tracking)}, supports_marker_size_estimation={repr(self.supports_marker_size_estimation)}, max_marker_count={repr(self.max_marker_count)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemMarkerTrackingPropertiesANDROID(supports_marker_tracking={self.supports_marker_tracking}, supports_marker_size_estimation={self.supports_marker_size_estimation}, max_marker_count={self.max_marker_count}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_marker_tracking", Bool32),
        ("supports_marker_size_estimation", Bool32),
        ("max_marker_count", c_uint16),
    ]


class TrackableMarkerDatabaseEntryANDROID(Structure):
    def __init__(
        self,
        id: int = 0,
        edge_size: float = 0,
    ) -> None:
        super().__init__(
            id=id,
            edge_size=edge_size,
        )

    def __repr__(self) -> str:
        return f"xr.TrackableMarkerDatabaseEntryANDROID(id={repr(self.id)}, edge_size={repr(self.edge_size)})"

    def __str__(self) -> str:
        return f"xr.TrackableMarkerDatabaseEntryANDROID(id={self.id}, edge_size={self.edge_size:.3f})"

    _fields_ = [
        ("id", c_int32),
        ("edge_size", c_float),
    ]


class TrackableMarkerDatabaseANDROID(Structure):
    def __init__(
        self,
        dictionary: TrackableMarkerDictionaryANDROID = TrackableMarkerDictionaryANDROID(),  # noqa
        entry_count: int = 0,
        entries: POINTER(TrackableMarkerDatabaseEntryANDROID) = None,
    ) -> None:
        super().__init__(
            dictionary=TrackableMarkerDictionaryANDROID(dictionary).value,
            entry_count=entry_count,
            entries=entries,
        )

    def __repr__(self) -> str:
        return f"xr.TrackableMarkerDatabaseANDROID(dictionary={repr(self.dictionary)}, entry_count={repr(self.entry_count)}, entries={repr(self.entries)})"

    def __str__(self) -> str:
        return f"xr.TrackableMarkerDatabaseANDROID(dictionary={self.dictionary}, entry_count={self.entry_count}, entries={self.entries})"

    _fields_ = [
        ("dictionary", TrackableMarkerDictionaryANDROID.ctype()),
        ("entry_count", c_uint32),
        ("entries", POINTER(TrackableMarkerDatabaseEntryANDROID)),
    ]


class TrackableMarkerConfigurationANDROID(Structure):
    def __init__(
        self,
        tracking_mode: TrackableMarkerTrackingModeANDROID = TrackableMarkerTrackingModeANDROID(),  # noqa
        database_count: Optional[int] = None,
        databases: ArrayFieldParamType[TrackableMarkerDatabaseANDROID] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.TRACKABLE_MARKER_CONFIGURATION_ANDROID,
    ) -> None:
        database_count, databases = array_field_helper(
            TrackableMarkerDatabaseANDROID, database_count, databases)
        super().__init__(
            tracking_mode=TrackableMarkerTrackingModeANDROID(tracking_mode).value,
            database_count=database_count,
            _databases=databases,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.TrackableMarkerConfigurationANDROID(tracking_mode={repr(self.tracking_mode)}, database_count={repr(self.database_count)}, databases={repr(self._databases)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.TrackableMarkerConfigurationANDROID(tracking_mode={self.tracking_mode}, database_count={self.database_count}, databases={self._databases}, next={self.next}, type={self.type})"

    @property
    def databases(self):
        if self.database_count == 0:
            return (TrackableMarkerDatabaseANDROID * 0)()
        else:
            return (TrackableMarkerDatabaseANDROID * self.database_count).from_address(
                ctypes.addressof(self._databases.contents))

    @databases.setter
    def databases(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.database_count, self._databases = array_field_helper(
            TrackableMarkerDatabaseANDROID, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("tracking_mode", TrackableMarkerTrackingModeANDROID.ctype()),
        ("database_count", c_uint32),
        ("_databases", POINTER(TrackableMarkerDatabaseANDROID)),
    ]


class TrackableMarkerANDROID(Structure):
    def __init__(
        self,
        tracking_state: TrackingStateANDROID = TrackingStateANDROID(),  # noqa
        last_updated_time: Time = 0,
        dictionary: TrackableMarkerDictionaryANDROID = TrackableMarkerDictionaryANDROID(),  # noqa
        marker_id: int = 0,
        center_pose: Posef = Posef(),
        extents: Extent2Df = None,
        next: c_void_p = None,
        type: StructureType = StructureType.TRACKABLE_MARKER_ANDROID,
    ) -> None:
        if extents is None:
            extents = Extent2Df()
        super().__init__(
            tracking_state=TrackingStateANDROID(tracking_state).value,
            last_updated_time=last_updated_time,
            dictionary=TrackableMarkerDictionaryANDROID(dictionary).value,
            marker_id=marker_id,
            center_pose=center_pose,
            extents=extents,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.TrackableMarkerANDROID(tracking_state={repr(self.tracking_state)}, last_updated_time={repr(self.last_updated_time)}, dictionary={repr(self.dictionary)}, marker_id={repr(self.marker_id)}, center_pose={repr(self.center_pose)}, extents={repr(self.extents)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.TrackableMarkerANDROID(tracking_state={self.tracking_state}, last_updated_time={self.last_updated_time}, dictionary={self.dictionary}, marker_id={self.marker_id}, center_pose={self.center_pose}, extents={self.extents}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("tracking_state", TrackingStateANDROID.ctype()),
        ("last_updated_time", Time),
        ("dictionary", TrackableMarkerDictionaryANDROID.ctype()),
        ("marker_id", c_int32),
        ("center_pose", Posef),
        ("extents", Extent2Df),
    ]


PFN_xrGetTrackableMarkerANDROID = CFUNCTYPE(Result.ctype(), TrackableTrackerANDROID, POINTER(TrackableGetInfoANDROID), POINTER(TrackableMarkerANDROID))

SpatialEntityIdEXT = c_uint64

SpatialBufferIdEXT = c_uint64


class SpatialEntityEXT_T(Structure):
    pass


class SpatialEntityEXT(POINTER(SpatialEntityEXT_T), HandleMixin):
    _type_ = SpatialEntityEXT_T  # ctypes idiosyncrasy


class SpatialContextEXT_T(Structure):
    pass


class SpatialContextEXT(POINTER(SpatialContextEXT_T), HandleMixin):
    _type_ = SpatialContextEXT_T  # ctypes idiosyncrasy


class SpatialSnapshotEXT_T(Structure):
    pass


class SpatialSnapshotEXT(POINTER(SpatialSnapshotEXT_T), HandleMixin):
    _type_ = SpatialSnapshotEXT_T  # ctypes idiosyncrasy


class SpatialCapabilityComponentTypesEXT(Structure):
    def __init__(
        self,
        component_type_capacity_input: int = 0,
        component_type_count_output: int = 0,
        component_types: POINTER(SpatialComponentTypeEXT.ctype()) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_CAPABILITY_COMPONENT_TYPES_EXT,
    ) -> None:
        super().__init__(
            component_type_capacity_input=component_type_capacity_input,
            component_type_count_output=component_type_count_output,
            component_types=component_types,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialCapabilityComponentTypesEXT(component_type_capacity_input={repr(self.component_type_capacity_input)}, component_type_count_output={repr(self.component_type_count_output)}, component_types={repr(self.component_types)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialCapabilityComponentTypesEXT(component_type_capacity_input={self.component_type_capacity_input}, component_type_count_output={self.component_type_count_output}, component_types={self.component_types}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("component_type_capacity_input", c_uint32),
        ("component_type_count_output", c_uint32),
        ("component_types", POINTER(SpatialComponentTypeEXT.ctype())),
    ]


class SpatialCapabilityConfigurationBaseHeaderEXT(Structure):
    def __init__(
        self,
        capability: SpatialCapabilityEXT = SpatialCapabilityEXT(),  # noqa
        enabled_component_count: Optional[int] = None,
        enabled_components: ArrayFieldParamType[c_int] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.UNKNOWN,
    ) -> None:
        enabled_component_count, enabled_components = array_field_helper(
            c_int, enabled_component_count, enabled_components)
        super().__init__(
            capability=SpatialCapabilityEXT(capability).value,
            enabled_component_count=enabled_component_count,
            _enabled_components=enabled_components,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialCapabilityConfigurationBaseHeaderEXT(capability={repr(self.capability)}, enabled_component_count={repr(self.enabled_component_count)}, enabled_components={repr(self._enabled_components)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialCapabilityConfigurationBaseHeaderEXT(capability={self.capability}, enabled_component_count={self.enabled_component_count}, enabled_components={self._enabled_components}, next={self.next}, type={self.type})"

    @property
    def enabled_components(self):
        if self.enabled_component_count == 0:
            return (c_int * 0)()
        else:
            return (c_int * self.enabled_component_count).from_address(
                ctypes.addressof(self._enabled_components.contents))

    @enabled_components.setter
    def enabled_components(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.enabled_component_count, self._enabled_components = array_field_helper(
            c_int, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("capability", SpatialCapabilityEXT.ctype()),
        ("enabled_component_count", c_uint32),
        ("_enabled_components", POINTER(c_int)),
    ]


class SpatialContextCreateInfoEXT(Structure):
    def __init__(
        self,
        capability_config_count: Optional[int] = None,
        capability_configs: BaseArrayFieldParamType = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_CONTEXT_CREATE_INFO_EXT,
    ) -> None:
        capability_config_count, capability_configs = base_array_field_helper(
            POINTER(SpatialCapabilityConfigurationBaseHeaderEXT), capability_config_count, capability_configs)
        super().__init__(
            capability_config_count=capability_config_count,
            _capability_configs=capability_configs,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialContextCreateInfoEXT(capability_config_count={repr(self.capability_config_count)}, capability_configs={repr(self._capability_configs)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialContextCreateInfoEXT(capability_config_count={self.capability_config_count}, capability_configs={self._capability_configs}, next={self.next}, type={self.type})"

    @property
    def capability_configs(self):
        if self.capability_config_count == 0:
            return (POINTER(SpatialCapabilityConfigurationBaseHeaderEXT) * 0)()
        else:
            return (POINTER(SpatialCapabilityConfigurationBaseHeaderEXT) * self.capability_config_count).from_address(
                ctypes.addressof(self._capability_configs.contents))

    @capability_configs.setter
    def capability_configs(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.capability_config_count, self._capability_configs = base_array_field_helper(
            POINTER(SpatialCapabilityConfigurationBaseHeaderEXT), None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("capability_config_count", c_uint32),
        ("_capability_configs", POINTER(POINTER(SpatialCapabilityConfigurationBaseHeaderEXT))),
    ]


class CreateSpatialContextCompletionEXT(Structure):
    def __init__(
        self,
        future_result: Result = Result(),  # noqa
        spatial_context: SpatialContextEXT = None,
        next: c_void_p = None,
        type: StructureType = StructureType.CREATE_SPATIAL_CONTEXT_COMPLETION_EXT,
    ) -> None:
        super().__init__(
            future_result=Result(future_result).value,
            spatial_context=spatial_context,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CreateSpatialContextCompletionEXT(future_result={repr(self.future_result)}, spatial_context={repr(self.spatial_context)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CreateSpatialContextCompletionEXT(future_result={self.future_result}, spatial_context={self.spatial_context}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("future_result", Result.ctype()),
        ("spatial_context", SpatialContextEXT),
    ]


class SpatialDiscoverySnapshotCreateInfoEXT(Structure):
    def __init__(
        self,
        component_type_count: Optional[int] = None,
        component_types: ArrayFieldParamType[c_int] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_DISCOVERY_SNAPSHOT_CREATE_INFO_EXT,
    ) -> None:
        component_type_count, component_types = array_field_helper(
            c_int, component_type_count, component_types)
        super().__init__(
            component_type_count=component_type_count,
            _component_types=component_types,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialDiscoverySnapshotCreateInfoEXT(component_type_count={repr(self.component_type_count)}, component_types={repr(self._component_types)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialDiscoverySnapshotCreateInfoEXT(component_type_count={self.component_type_count}, component_types={self._component_types}, next={self.next}, type={self.type})"

    @property
    def component_types(self):
        if self.component_type_count == 0:
            return (c_int * 0)()
        else:
            return (c_int * self.component_type_count).from_address(
                ctypes.addressof(self._component_types.contents))

    @component_types.setter
    def component_types(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.component_type_count, self._component_types = array_field_helper(
            c_int, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("component_type_count", c_uint32),
        ("_component_types", POINTER(c_int)),
    ]


class CreateSpatialDiscoverySnapshotCompletionInfoEXT(Structure):
    def __init__(
        self,
        base_space: Space = None,
        time: Time = 0,
        future: FutureEXT = None,
        next: c_void_p = None,
        type: StructureType = StructureType.CREATE_SPATIAL_DISCOVERY_SNAPSHOT_COMPLETION_INFO_EXT,
    ) -> None:
        super().__init__(
            base_space=base_space,
            time=time,
            future=future,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CreateSpatialDiscoverySnapshotCompletionInfoEXT(base_space={repr(self.base_space)}, time={repr(self.time)}, future={repr(self.future)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CreateSpatialDiscoverySnapshotCompletionInfoEXT(base_space={self.base_space}, time={self.time}, future={self.future}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("base_space", Space),
        ("time", Time),
        ("future", FutureEXT),
    ]


class CreateSpatialDiscoverySnapshotCompletionEXT(Structure):
    def __init__(
        self,
        future_result: Result = Result(),  # noqa
        snapshot: SpatialSnapshotEXT = None,
        next: c_void_p = None,
        type: StructureType = StructureType.CREATE_SPATIAL_DISCOVERY_SNAPSHOT_COMPLETION_EXT,
    ) -> None:
        super().__init__(
            future_result=Result(future_result).value,
            snapshot=snapshot,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CreateSpatialDiscoverySnapshotCompletionEXT(future_result={repr(self.future_result)}, snapshot={repr(self.snapshot)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CreateSpatialDiscoverySnapshotCompletionEXT(future_result={self.future_result}, snapshot={self.snapshot}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("future_result", Result.ctype()),
        ("snapshot", SpatialSnapshotEXT),
    ]


class SpatialComponentDataQueryConditionEXT(Structure):
    def __init__(
        self,
        component_type_count: Optional[int] = None,
        component_types: ArrayFieldParamType[c_int] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_COMPONENT_DATA_QUERY_CONDITION_EXT,
    ) -> None:
        component_type_count, component_types = array_field_helper(
            c_int, component_type_count, component_types)
        super().__init__(
            component_type_count=component_type_count,
            _component_types=component_types,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialComponentDataQueryConditionEXT(component_type_count={repr(self.component_type_count)}, component_types={repr(self._component_types)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialComponentDataQueryConditionEXT(component_type_count={self.component_type_count}, component_types={self._component_types}, next={self.next}, type={self.type})"

    @property
    def component_types(self):
        if self.component_type_count == 0:
            return (c_int * 0)()
        else:
            return (c_int * self.component_type_count).from_address(
                ctypes.addressof(self._component_types.contents))

    @component_types.setter
    def component_types(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.component_type_count, self._component_types = array_field_helper(
            c_int, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("component_type_count", c_uint32),
        ("_component_types", POINTER(c_int)),
    ]


class SpatialComponentDataQueryResultEXT(Structure):
    def __init__(
        self,
        entity_id_capacity_input: int = 0,
        entity_id_count_output: int = 0,
        entity_ids: POINTER(SpatialEntityIdEXT) = None,
        entity_state_capacity_input: int = 0,
        entity_state_count_output: int = 0,
        entity_states: POINTER(SpatialEntityTrackingStateEXT.ctype()) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_COMPONENT_DATA_QUERY_RESULT_EXT,
    ) -> None:
        super().__init__(
            entity_id_capacity_input=entity_id_capacity_input,
            entity_id_count_output=entity_id_count_output,
            entity_ids=entity_ids,
            entity_state_capacity_input=entity_state_capacity_input,
            entity_state_count_output=entity_state_count_output,
            entity_states=entity_states,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialComponentDataQueryResultEXT(entity_id_capacity_input={repr(self.entity_id_capacity_input)}, entity_id_count_output={repr(self.entity_id_count_output)}, entity_ids={repr(self.entity_ids)}, entity_state_capacity_input={repr(self.entity_state_capacity_input)}, entity_state_count_output={repr(self.entity_state_count_output)}, entity_states={repr(self.entity_states)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialComponentDataQueryResultEXT(entity_id_capacity_input={self.entity_id_capacity_input}, entity_id_count_output={self.entity_id_count_output}, entity_ids={self.entity_ids}, entity_state_capacity_input={self.entity_state_capacity_input}, entity_state_count_output={self.entity_state_count_output}, entity_states={self.entity_states}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("entity_id_capacity_input", c_uint32),
        ("entity_id_count_output", c_uint32),
        ("entity_ids", POINTER(SpatialEntityIdEXT)),
        ("entity_state_capacity_input", c_uint32),
        ("entity_state_count_output", c_uint32),
        ("entity_states", POINTER(SpatialEntityTrackingStateEXT.ctype())),
    ]


class SpatialBufferEXT(Structure):
    def __init__(
        self,
        buffer_id: SpatialBufferIdEXT = 0,
        buffer_type: SpatialBufferTypeEXT = SpatialBufferTypeEXT(),  # noqa
    ) -> None:
        super().__init__(
            buffer_id=buffer_id,
            buffer_type=SpatialBufferTypeEXT(buffer_type).value,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialBufferEXT(buffer_id={repr(self.buffer_id)}, buffer_type={repr(self.buffer_type)})"

    def __str__(self) -> str:
        return f"xr.SpatialBufferEXT(buffer_id={self.buffer_id}, buffer_type={self.buffer_type})"

    _fields_ = [
        ("buffer_id", SpatialBufferIdEXT),
        ("buffer_type", SpatialBufferTypeEXT.ctype()),
    ]


class SpatialBufferGetInfoEXT(Structure):
    def __init__(
        self,
        buffer_id: SpatialBufferIdEXT = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_BUFFER_GET_INFO_EXT,
    ) -> None:
        super().__init__(
            buffer_id=buffer_id,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialBufferGetInfoEXT(buffer_id={repr(self.buffer_id)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialBufferGetInfoEXT(buffer_id={self.buffer_id}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("buffer_id", SpatialBufferIdEXT),
    ]


class SpatialBounded2DDataEXT(Structure):
    def __init__(
        self,
        center: Posef = Posef(),
        extents: Extent2Df = None,
    ) -> None:
        if extents is None:
            extents = Extent2Df()
        super().__init__(
            center=center,
            extents=extents,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialBounded2DDataEXT(center={repr(self.center)}, extents={repr(self.extents)})"

    def __str__(self) -> str:
        return f"xr.SpatialBounded2DDataEXT(center={self.center}, extents={self.extents})"

    _fields_ = [
        ("center", Posef),
        ("extents", Extent2Df),
    ]


class SpatialComponentBounded2DListEXT(Structure):
    def __init__(
        self,
        bound_count: Optional[int] = None,
        bounds: ArrayFieldParamType[SpatialBounded2DDataEXT] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_COMPONENT_BOUNDED_2D_LIST_EXT,
    ) -> None:
        bound_count, bounds = array_field_helper(
            SpatialBounded2DDataEXT, bound_count, bounds)
        super().__init__(
            bound_count=bound_count,
            _bounds=bounds,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialComponentBounded2DListEXT(bound_count={repr(self.bound_count)}, bounds={repr(self._bounds)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialComponentBounded2DListEXT(bound_count={self.bound_count}, bounds={self._bounds}, next={self.next}, type={self.type})"

    @property
    def bounds(self):
        if self.bound_count == 0:
            return (SpatialBounded2DDataEXT * 0)()
        else:
            return (SpatialBounded2DDataEXT * self.bound_count).from_address(
                ctypes.addressof(self._bounds.contents))

    @bounds.setter
    def bounds(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.bound_count, self._bounds = array_field_helper(
            SpatialBounded2DDataEXT, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("bound_count", c_uint32),
        ("_bounds", POINTER(SpatialBounded2DDataEXT)),
    ]


class SpatialComponentBounded3DListEXT(Structure):
    def __init__(
        self,
        bound_count: Optional[int] = None,
        bounds: ArrayFieldParamType[Boxf] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_COMPONENT_BOUNDED_3D_LIST_EXT,
    ) -> None:
        bound_count, bounds = array_field_helper(
            Boxf, bound_count, bounds)
        super().__init__(
            bound_count=bound_count,
            _bounds=bounds,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialComponentBounded3DListEXT(bound_count={repr(self.bound_count)}, bounds={repr(self._bounds)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialComponentBounded3DListEXT(bound_count={self.bound_count}, bounds={self._bounds}, next={self.next}, type={self.type})"

    @property
    def bounds(self):
        if self.bound_count == 0:
            return (Boxf * 0)()
        else:
            return (Boxf * self.bound_count).from_address(
                ctypes.addressof(self._bounds.contents))

    @bounds.setter
    def bounds(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.bound_count, self._bounds = array_field_helper(
            Boxf, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("bound_count", c_uint32),
        ("_bounds", POINTER(Boxf)),
    ]


class SpatialComponentParentListEXT(Structure):
    def __init__(
        self,
        parent_count: Optional[int] = None,
        parents: ArrayFieldParamType[SpatialEntityIdEXT] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_COMPONENT_PARENT_LIST_EXT,
    ) -> None:
        parent_count, parents = array_field_helper(
            SpatialEntityIdEXT, parent_count, parents)
        super().__init__(
            parent_count=parent_count,
            _parents=parents,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialComponentParentListEXT(parent_count={repr(self.parent_count)}, parents={repr(self._parents)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialComponentParentListEXT(parent_count={self.parent_count}, parents={self._parents}, next={self.next}, type={self.type})"

    @property
    def parents(self):
        if self.parent_count == 0:
            return (SpatialEntityIdEXT * 0)()
        else:
            return (SpatialEntityIdEXT * self.parent_count).from_address(
                ctypes.addressof(self._parents.contents))

    @parents.setter
    def parents(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.parent_count, self._parents = array_field_helper(
            SpatialEntityIdEXT, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("parent_count", c_uint32),
        ("_parents", POINTER(SpatialEntityIdEXT)),
    ]


class SpatialMeshDataEXT(Structure):
    def __init__(
        self,
        origin: Posef = Posef(),
        vertex_buffer: SpatialBufferEXT = None,
        index_buffer: SpatialBufferEXT = None,
    ) -> None:
        if vertex_buffer is None:
            vertex_buffer = SpatialBufferEXT()
        if index_buffer is None:
            index_buffer = SpatialBufferEXT()
        super().__init__(
            origin=origin,
            vertex_buffer=vertex_buffer,
            index_buffer=index_buffer,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialMeshDataEXT(origin={repr(self.origin)}, vertex_buffer={repr(self.vertex_buffer)}, index_buffer={repr(self.index_buffer)})"

    def __str__(self) -> str:
        return f"xr.SpatialMeshDataEXT(origin={self.origin}, vertex_buffer={self.vertex_buffer}, index_buffer={self.index_buffer})"

    _fields_ = [
        ("origin", Posef),
        ("vertex_buffer", SpatialBufferEXT),
        ("index_buffer", SpatialBufferEXT),
    ]


class SpatialComponentMesh3DListEXT(Structure):
    def __init__(
        self,
        mesh_count: Optional[int] = None,
        meshes: ArrayFieldParamType[SpatialMeshDataEXT] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_COMPONENT_MESH_3D_LIST_EXT,
    ) -> None:
        mesh_count, meshes = array_field_helper(
            SpatialMeshDataEXT, mesh_count, meshes)
        super().__init__(
            mesh_count=mesh_count,
            _meshes=meshes,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialComponentMesh3DListEXT(mesh_count={repr(self.mesh_count)}, meshes={repr(self._meshes)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialComponentMesh3DListEXT(mesh_count={self.mesh_count}, meshes={self._meshes}, next={self.next}, type={self.type})"

    @property
    def meshes(self):
        if self.mesh_count == 0:
            return (SpatialMeshDataEXT * 0)()
        else:
            return (SpatialMeshDataEXT * self.mesh_count).from_address(
                ctypes.addressof(self._meshes.contents))

    @meshes.setter
    def meshes(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.mesh_count, self._meshes = array_field_helper(
            SpatialMeshDataEXT, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("mesh_count", c_uint32),
        ("_meshes", POINTER(SpatialMeshDataEXT)),
    ]


class SpatialEntityFromIdCreateInfoEXT(Structure):
    def __init__(
        self,
        entity_id: SpatialEntityIdEXT = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ENTITY_FROM_ID_CREATE_INFO_EXT,
    ) -> None:
        super().__init__(
            entity_id=entity_id,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialEntityFromIdCreateInfoEXT(entity_id={repr(self.entity_id)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialEntityFromIdCreateInfoEXT(entity_id={self.entity_id}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("entity_id", SpatialEntityIdEXT),
    ]


class SpatialUpdateSnapshotCreateInfoEXT(Structure):
    def __init__(
        self,
        entity_count: int = 0,
        entities: POINTER(SpatialEntityEXT) = None,
        component_type_count: Optional[int] = None,
        component_types: ArrayFieldParamType[c_int] = None,
        base_space: Space = None,
        time: Time = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_UPDATE_SNAPSHOT_CREATE_INFO_EXT,
    ) -> None:
        component_type_count, component_types = array_field_helper(
            c_int, component_type_count, component_types)
        super().__init__(
            entity_count=entity_count,
            entities=entities,
            component_type_count=component_type_count,
            _component_types=component_types,
            base_space=base_space,
            time=time,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialUpdateSnapshotCreateInfoEXT(entity_count={repr(self.entity_count)}, entities={repr(self.entities)}, component_type_count={repr(self.component_type_count)}, component_types={repr(self._component_types)}, base_space={repr(self.base_space)}, time={repr(self.time)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialUpdateSnapshotCreateInfoEXT(entity_count={self.entity_count}, entities={self.entities}, component_type_count={self.component_type_count}, component_types={self._component_types}, base_space={self.base_space}, time={self.time}, next={self.next}, type={self.type})"

    @property
    def component_types(self):
        if self.component_type_count == 0:
            return (c_int * 0)()
        else:
            return (c_int * self.component_type_count).from_address(
                ctypes.addressof(self._component_types.contents))

    @component_types.setter
    def component_types(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.component_type_count, self._component_types = array_field_helper(
            c_int, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("entity_count", c_uint32),
        ("entities", POINTER(SpatialEntityEXT)),
        ("component_type_count", c_uint32),
        ("_component_types", POINTER(c_int)),
        ("base_space", Space),
        ("time", Time),
    ]


class EventDataSpatialDiscoveryRecommendedEXT(Structure):
    def __init__(
        self,
        spatial_context: SpatialContextEXT = None,
        next: c_void_p = None,
        type: StructureType = StructureType.EVENT_DATA_SPATIAL_DISCOVERY_RECOMMENDED_EXT,
    ) -> None:
        super().__init__(
            spatial_context=spatial_context,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.EventDataSpatialDiscoveryRecommendedEXT(spatial_context={repr(self.spatial_context)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.EventDataSpatialDiscoveryRecommendedEXT(spatial_context={self.spatial_context}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("spatial_context", SpatialContextEXT),
    ]


class SpatialFilterTrackingStateEXT(Structure):
    def __init__(
        self,
        tracking_state: SpatialEntityTrackingStateEXT = SpatialEntityTrackingStateEXT(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_FILTER_TRACKING_STATE_EXT,
    ) -> None:
        super().__init__(
            tracking_state=SpatialEntityTrackingStateEXT(tracking_state).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialFilterTrackingStateEXT(tracking_state={repr(self.tracking_state)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialFilterTrackingStateEXT(tracking_state={self.tracking_state}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("tracking_state", SpatialEntityTrackingStateEXT.ctype()),
    ]


PFN_xrEnumerateSpatialCapabilitiesEXT = CFUNCTYPE(Result.ctype(), Instance, SystemId, c_uint32, POINTER(c_uint32), POINTER(SpatialCapabilityEXT.ctype()))

PFN_xrEnumerateSpatialCapabilityComponentTypesEXT = CFUNCTYPE(Result.ctype(), Instance, SystemId, SpatialCapabilityEXT.ctype(), POINTER(SpatialCapabilityComponentTypesEXT))

PFN_xrEnumerateSpatialCapabilityFeaturesEXT = CFUNCTYPE(Result.ctype(), Instance, SystemId, SpatialCapabilityEXT.ctype(), c_uint32, POINTER(c_uint32), POINTER(SpatialCapabilityFeatureEXT.ctype()))

PFN_xrCreateSpatialContextAsyncEXT = CFUNCTYPE(Result.ctype(), Session, POINTER(SpatialContextCreateInfoEXT), POINTER(FutureEXT))

PFN_xrCreateSpatialContextCompleteEXT = CFUNCTYPE(Result.ctype(), Session, FutureEXT, POINTER(CreateSpatialContextCompletionEXT))

PFN_xrDestroySpatialContextEXT = CFUNCTYPE(Result.ctype(), SpatialContextEXT)

PFN_xrCreateSpatialDiscoverySnapshotAsyncEXT = CFUNCTYPE(Result.ctype(), SpatialContextEXT, POINTER(SpatialDiscoverySnapshotCreateInfoEXT), POINTER(FutureEXT))

PFN_xrCreateSpatialDiscoverySnapshotCompleteEXT = CFUNCTYPE(Result.ctype(), SpatialContextEXT, POINTER(CreateSpatialDiscoverySnapshotCompletionInfoEXT), POINTER(CreateSpatialDiscoverySnapshotCompletionEXT))

PFN_xrQuerySpatialComponentDataEXT = CFUNCTYPE(Result.ctype(), SpatialSnapshotEXT, POINTER(SpatialComponentDataQueryConditionEXT), POINTER(SpatialComponentDataQueryResultEXT))

PFN_xrDestroySpatialSnapshotEXT = CFUNCTYPE(Result.ctype(), SpatialSnapshotEXT)

PFN_xrCreateSpatialEntityFromIdEXT = CFUNCTYPE(Result.ctype(), SpatialContextEXT, POINTER(SpatialEntityFromIdCreateInfoEXT), POINTER(SpatialEntityEXT))

PFN_xrDestroySpatialEntityEXT = CFUNCTYPE(Result.ctype(), SpatialEntityEXT)

PFN_xrCreateSpatialUpdateSnapshotEXT = CFUNCTYPE(Result.ctype(), SpatialContextEXT, POINTER(SpatialUpdateSnapshotCreateInfoEXT), POINTER(SpatialSnapshotEXT))

PFN_xrGetSpatialBufferStringEXT = CFUNCTYPE(Result.ctype(), SpatialSnapshotEXT, POINTER(SpatialBufferGetInfoEXT), c_uint32, POINTER(c_uint32), c_char_p)

PFN_xrGetSpatialBufferUint8EXT = CFUNCTYPE(Result.ctype(), SpatialSnapshotEXT, POINTER(SpatialBufferGetInfoEXT), c_uint32, POINTER(c_uint32), POINTER(c_uint8))

PFN_xrGetSpatialBufferUint16EXT = CFUNCTYPE(Result.ctype(), SpatialSnapshotEXT, POINTER(SpatialBufferGetInfoEXT), c_uint32, POINTER(c_uint32), POINTER(c_uint16))

PFN_xrGetSpatialBufferUint32EXT = CFUNCTYPE(Result.ctype(), SpatialSnapshotEXT, POINTER(SpatialBufferGetInfoEXT), c_uint32, POINTER(c_uint32), POINTER(c_uint32))

PFN_xrGetSpatialBufferFloatEXT = CFUNCTYPE(Result.ctype(), SpatialSnapshotEXT, POINTER(SpatialBufferGetInfoEXT), c_uint32, POINTER(c_uint32), POINTER(c_float))

PFN_xrGetSpatialBufferVector2fEXT = CFUNCTYPE(Result.ctype(), SpatialSnapshotEXT, POINTER(SpatialBufferGetInfoEXT), c_uint32, POINTER(c_uint32), POINTER(Vector2f))

PFN_xrGetSpatialBufferVector3fEXT = CFUNCTYPE(Result.ctype(), SpatialSnapshotEXT, POINTER(SpatialBufferGetInfoEXT), c_uint32, POINTER(c_uint32), POINTER(Vector3f))


class SpatialCapabilityConfigurationPlaneTrackingEXT(Structure):
    def __init__(
        self,
        capability: SpatialCapabilityEXT = SpatialCapabilityEXT(),  # noqa
        enabled_component_count: Optional[int] = None,
        enabled_components: ArrayFieldParamType[c_int] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_CAPABILITY_CONFIGURATION_PLANE_TRACKING_EXT,
    ) -> None:
        enabled_component_count, enabled_components = array_field_helper(
            c_int, enabled_component_count, enabled_components)
        super().__init__(
            capability=SpatialCapabilityEXT(capability).value,
            enabled_component_count=enabled_component_count,
            _enabled_components=enabled_components,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialCapabilityConfigurationPlaneTrackingEXT(capability={repr(self.capability)}, enabled_component_count={repr(self.enabled_component_count)}, enabled_components={repr(self._enabled_components)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialCapabilityConfigurationPlaneTrackingEXT(capability={self.capability}, enabled_component_count={self.enabled_component_count}, enabled_components={self._enabled_components}, next={self.next}, type={self.type})"

    @property
    def enabled_components(self):
        if self.enabled_component_count == 0:
            return (c_int * 0)()
        else:
            return (c_int * self.enabled_component_count).from_address(
                ctypes.addressof(self._enabled_components.contents))

    @enabled_components.setter
    def enabled_components(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.enabled_component_count, self._enabled_components = array_field_helper(
            c_int, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("capability", SpatialCapabilityEXT.ctype()),
        ("enabled_component_count", c_uint32),
        ("_enabled_components", POINTER(c_int)),
    ]


class SpatialComponentPlaneAlignmentListEXT(Structure):
    def __init__(
        self,
        plane_alignment_count: Optional[int] = None,
        plane_alignments: ArrayFieldParamType[SpatialPlaneAlignmentEXT.ctype()] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_COMPONENT_PLANE_ALIGNMENT_LIST_EXT,
    ) -> None:
        plane_alignment_count, plane_alignments = array_field_helper(
            SpatialPlaneAlignmentEXT.ctype(), plane_alignment_count, plane_alignments)
        super().__init__(
            plane_alignment_count=plane_alignment_count,
            _plane_alignments=plane_alignments,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialComponentPlaneAlignmentListEXT(plane_alignment_count={repr(self.plane_alignment_count)}, plane_alignments={repr(self._plane_alignments)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialComponentPlaneAlignmentListEXT(plane_alignment_count={self.plane_alignment_count}, plane_alignments={self._plane_alignments}, next={self.next}, type={self.type})"

    @property
    def plane_alignments(self):
        if self.plane_alignment_count == 0:
            return (SpatialPlaneAlignmentEXT.ctype() * 0)()
        else:
            return (SpatialPlaneAlignmentEXT.ctype() * self.plane_alignment_count).from_address(
                ctypes.addressof(self._plane_alignments.contents))

    @plane_alignments.setter
    def plane_alignments(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.plane_alignment_count, self._plane_alignments = array_field_helper(
            SpatialPlaneAlignmentEXT.ctype(), None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("plane_alignment_count", c_uint32),
        ("_plane_alignments", POINTER(SpatialPlaneAlignmentEXT.ctype())),
    ]


class SpatialComponentMesh2DListEXT(Structure):
    def __init__(
        self,
        mesh_count: Optional[int] = None,
        meshes: ArrayFieldParamType[SpatialMeshDataEXT] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_COMPONENT_MESH_2D_LIST_EXT,
    ) -> None:
        mesh_count, meshes = array_field_helper(
            SpatialMeshDataEXT, mesh_count, meshes)
        super().__init__(
            mesh_count=mesh_count,
            _meshes=meshes,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialComponentMesh2DListEXT(mesh_count={repr(self.mesh_count)}, meshes={repr(self._meshes)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialComponentMesh2DListEXT(mesh_count={self.mesh_count}, meshes={self._meshes}, next={self.next}, type={self.type})"

    @property
    def meshes(self):
        if self.mesh_count == 0:
            return (SpatialMeshDataEXT * 0)()
        else:
            return (SpatialMeshDataEXT * self.mesh_count).from_address(
                ctypes.addressof(self._meshes.contents))

    @meshes.setter
    def meshes(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.mesh_count, self._meshes = array_field_helper(
            SpatialMeshDataEXT, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("mesh_count", c_uint32),
        ("_meshes", POINTER(SpatialMeshDataEXT)),
    ]


class SpatialPolygon2DDataEXT(Structure):
    def __init__(
        self,
        origin: Posef = Posef(),
        vertex_buffer: SpatialBufferEXT = None,
    ) -> None:
        if vertex_buffer is None:
            vertex_buffer = SpatialBufferEXT()
        super().__init__(
            origin=origin,
            vertex_buffer=vertex_buffer,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialPolygon2DDataEXT(origin={repr(self.origin)}, vertex_buffer={repr(self.vertex_buffer)})"

    def __str__(self) -> str:
        return f"xr.SpatialPolygon2DDataEXT(origin={self.origin}, vertex_buffer={self.vertex_buffer})"

    _fields_ = [
        ("origin", Posef),
        ("vertex_buffer", SpatialBufferEXT),
    ]


class SpatialComponentPolygon2DListEXT(Structure):
    def __init__(
        self,
        polygon_count: Optional[int] = None,
        polygons: ArrayFieldParamType[SpatialPolygon2DDataEXT] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_COMPONENT_POLYGON_2D_LIST_EXT,
    ) -> None:
        polygon_count, polygons = array_field_helper(
            SpatialPolygon2DDataEXT, polygon_count, polygons)
        super().__init__(
            polygon_count=polygon_count,
            _polygons=polygons,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialComponentPolygon2DListEXT(polygon_count={repr(self.polygon_count)}, polygons={repr(self._polygons)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialComponentPolygon2DListEXT(polygon_count={self.polygon_count}, polygons={self._polygons}, next={self.next}, type={self.type})"

    @property
    def polygons(self):
        if self.polygon_count == 0:
            return (SpatialPolygon2DDataEXT * 0)()
        else:
            return (SpatialPolygon2DDataEXT * self.polygon_count).from_address(
                ctypes.addressof(self._polygons.contents))

    @polygons.setter
    def polygons(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.polygon_count, self._polygons = array_field_helper(
            SpatialPolygon2DDataEXT, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("polygon_count", c_uint32),
        ("_polygons", POINTER(SpatialPolygon2DDataEXT)),
    ]


class SpatialComponentPlaneSemanticLabelListEXT(Structure):
    def __init__(
        self,
        semantic_label_count: Optional[int] = None,
        semantic_labels: ArrayFieldParamType[SpatialPlaneSemanticLabelEXT.ctype()] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_COMPONENT_PLANE_SEMANTIC_LABEL_LIST_EXT,
    ) -> None:
        semantic_label_count, semantic_labels = array_field_helper(
            SpatialPlaneSemanticLabelEXT.ctype(), semantic_label_count, semantic_labels)
        super().__init__(
            semantic_label_count=semantic_label_count,
            _semantic_labels=semantic_labels,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialComponentPlaneSemanticLabelListEXT(semantic_label_count={repr(self.semantic_label_count)}, semantic_labels={repr(self._semantic_labels)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialComponentPlaneSemanticLabelListEXT(semantic_label_count={self.semantic_label_count}, semantic_labels={self._semantic_labels}, next={self.next}, type={self.type})"

    @property
    def semantic_labels(self):
        if self.semantic_label_count == 0:
            return (SpatialPlaneSemanticLabelEXT.ctype() * 0)()
        else:
            return (SpatialPlaneSemanticLabelEXT.ctype() * self.semantic_label_count).from_address(
                ctypes.addressof(self._semantic_labels.contents))

    @semantic_labels.setter
    def semantic_labels(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.semantic_label_count, self._semantic_labels = array_field_helper(
            SpatialPlaneSemanticLabelEXT.ctype(), None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("semantic_label_count", c_uint32),
        ("_semantic_labels", POINTER(SpatialPlaneSemanticLabelEXT.ctype())),
    ]


class SpatialCapabilityConfigurationQrCodeEXT(Structure):
    def __init__(
        self,
        capability: SpatialCapabilityEXT = SpatialCapabilityEXT(),  # noqa
        enabled_component_count: Optional[int] = None,
        enabled_components: ArrayFieldParamType[c_int] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_CAPABILITY_CONFIGURATION_QR_CODE_EXT,
    ) -> None:
        enabled_component_count, enabled_components = array_field_helper(
            c_int, enabled_component_count, enabled_components)
        super().__init__(
            capability=SpatialCapabilityEXT(capability).value,
            enabled_component_count=enabled_component_count,
            _enabled_components=enabled_components,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialCapabilityConfigurationQrCodeEXT(capability={repr(self.capability)}, enabled_component_count={repr(self.enabled_component_count)}, enabled_components={repr(self._enabled_components)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialCapabilityConfigurationQrCodeEXT(capability={self.capability}, enabled_component_count={self.enabled_component_count}, enabled_components={self._enabled_components}, next={self.next}, type={self.type})"

    @property
    def enabled_components(self):
        if self.enabled_component_count == 0:
            return (c_int * 0)()
        else:
            return (c_int * self.enabled_component_count).from_address(
                ctypes.addressof(self._enabled_components.contents))

    @enabled_components.setter
    def enabled_components(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.enabled_component_count, self._enabled_components = array_field_helper(
            c_int, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("capability", SpatialCapabilityEXT.ctype()),
        ("enabled_component_count", c_uint32),
        ("_enabled_components", POINTER(c_int)),
    ]


class SpatialCapabilityConfigurationMicroQrCodeEXT(Structure):
    def __init__(
        self,
        capability: SpatialCapabilityEXT = SpatialCapabilityEXT(),  # noqa
        enabled_component_count: Optional[int] = None,
        enabled_components: ArrayFieldParamType[c_int] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_CAPABILITY_CONFIGURATION_MICRO_QR_CODE_EXT,
    ) -> None:
        enabled_component_count, enabled_components = array_field_helper(
            c_int, enabled_component_count, enabled_components)
        super().__init__(
            capability=SpatialCapabilityEXT(capability).value,
            enabled_component_count=enabled_component_count,
            _enabled_components=enabled_components,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialCapabilityConfigurationMicroQrCodeEXT(capability={repr(self.capability)}, enabled_component_count={repr(self.enabled_component_count)}, enabled_components={repr(self._enabled_components)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialCapabilityConfigurationMicroQrCodeEXT(capability={self.capability}, enabled_component_count={self.enabled_component_count}, enabled_components={self._enabled_components}, next={self.next}, type={self.type})"

    @property
    def enabled_components(self):
        if self.enabled_component_count == 0:
            return (c_int * 0)()
        else:
            return (c_int * self.enabled_component_count).from_address(
                ctypes.addressof(self._enabled_components.contents))

    @enabled_components.setter
    def enabled_components(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.enabled_component_count, self._enabled_components = array_field_helper(
            c_int, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("capability", SpatialCapabilityEXT.ctype()),
        ("enabled_component_count", c_uint32),
        ("_enabled_components", POINTER(c_int)),
    ]


class SpatialCapabilityConfigurationArucoMarkerEXT(Structure):
    def __init__(
        self,
        capability: SpatialCapabilityEXT = SpatialCapabilityEXT(),  # noqa
        enabled_component_count: Optional[int] = None,
        enabled_components: ArrayFieldParamType[c_int] = None,
        ar_uco_dict: SpatialMarkerArucoDictEXT = SpatialMarkerArucoDictEXT(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_CAPABILITY_CONFIGURATION_ARUCO_MARKER_EXT,
    ) -> None:
        enabled_component_count, enabled_components = array_field_helper(
            c_int, enabled_component_count, enabled_components)
        super().__init__(
            capability=SpatialCapabilityEXT(capability).value,
            enabled_component_count=enabled_component_count,
            _enabled_components=enabled_components,
            ar_uco_dict=SpatialMarkerArucoDictEXT(ar_uco_dict).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialCapabilityConfigurationArucoMarkerEXT(capability={repr(self.capability)}, enabled_component_count={repr(self.enabled_component_count)}, enabled_components={repr(self._enabled_components)}, ar_uco_dict={repr(self.ar_uco_dict)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialCapabilityConfigurationArucoMarkerEXT(capability={self.capability}, enabled_component_count={self.enabled_component_count}, enabled_components={self._enabled_components}, ar_uco_dict={self.ar_uco_dict}, next={self.next}, type={self.type})"

    @property
    def enabled_components(self):
        if self.enabled_component_count == 0:
            return (c_int * 0)()
        else:
            return (c_int * self.enabled_component_count).from_address(
                ctypes.addressof(self._enabled_components.contents))

    @enabled_components.setter
    def enabled_components(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.enabled_component_count, self._enabled_components = array_field_helper(
            c_int, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("capability", SpatialCapabilityEXT.ctype()),
        ("enabled_component_count", c_uint32),
        ("_enabled_components", POINTER(c_int)),
        ("ar_uco_dict", SpatialMarkerArucoDictEXT.ctype()),
    ]


class SpatialCapabilityConfigurationAprilTagEXT(Structure):
    def __init__(
        self,
        capability: SpatialCapabilityEXT = SpatialCapabilityEXT(),  # noqa
        enabled_component_count: Optional[int] = None,
        enabled_components: ArrayFieldParamType[c_int] = None,
        april_dict: SpatialMarkerAprilTagDictEXT = SpatialMarkerAprilTagDictEXT(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_CAPABILITY_CONFIGURATION_APRIL_TAG_EXT,
    ) -> None:
        enabled_component_count, enabled_components = array_field_helper(
            c_int, enabled_component_count, enabled_components)
        super().__init__(
            capability=SpatialCapabilityEXT(capability).value,
            enabled_component_count=enabled_component_count,
            _enabled_components=enabled_components,
            april_dict=SpatialMarkerAprilTagDictEXT(april_dict).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialCapabilityConfigurationAprilTagEXT(capability={repr(self.capability)}, enabled_component_count={repr(self.enabled_component_count)}, enabled_components={repr(self._enabled_components)}, april_dict={repr(self.april_dict)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialCapabilityConfigurationAprilTagEXT(capability={self.capability}, enabled_component_count={self.enabled_component_count}, enabled_components={self._enabled_components}, april_dict={self.april_dict}, next={self.next}, type={self.type})"

    @property
    def enabled_components(self):
        if self.enabled_component_count == 0:
            return (c_int * 0)()
        else:
            return (c_int * self.enabled_component_count).from_address(
                ctypes.addressof(self._enabled_components.contents))

    @enabled_components.setter
    def enabled_components(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.enabled_component_count, self._enabled_components = array_field_helper(
            c_int, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("capability", SpatialCapabilityEXT.ctype()),
        ("enabled_component_count", c_uint32),
        ("_enabled_components", POINTER(c_int)),
        ("april_dict", SpatialMarkerAprilTagDictEXT.ctype()),
    ]


class SpatialMarkerSizeEXT(Structure):
    def __init__(
        self,
        marker_side_length: float = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_MARKER_SIZE_EXT,
    ) -> None:
        super().__init__(
            marker_side_length=marker_side_length,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialMarkerSizeEXT(marker_side_length={repr(self.marker_side_length)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialMarkerSizeEXT(marker_side_length={self.marker_side_length:.3f}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("marker_side_length", c_float),
    ]


class SpatialMarkerStaticOptimizationEXT(Structure):
    def __init__(
        self,
        optimize_for_static_marker: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_MARKER_STATIC_OPTIMIZATION_EXT,
    ) -> None:
        super().__init__(
            optimize_for_static_marker=optimize_for_static_marker,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialMarkerStaticOptimizationEXT(optimize_for_static_marker={repr(self.optimize_for_static_marker)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialMarkerStaticOptimizationEXT(optimize_for_static_marker={self.optimize_for_static_marker}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("optimize_for_static_marker", Bool32),
    ]


class SpatialMarkerDataEXT(Structure):
    def __init__(
        self,
        capability: SpatialCapabilityEXT = SpatialCapabilityEXT(),  # noqa
        marker_id: int = 0,
        data: SpatialBufferEXT = None,
    ) -> None:
        if data is None:
            data = SpatialBufferEXT()
        super().__init__(
            capability=SpatialCapabilityEXT(capability).value,
            marker_id=marker_id,
            data=data,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialMarkerDataEXT(capability={repr(self.capability)}, marker_id={repr(self.marker_id)}, data={repr(self.data)})"

    def __str__(self) -> str:
        return f"xr.SpatialMarkerDataEXT(capability={self.capability}, marker_id={self.marker_id}, data={self.data})"

    _fields_ = [
        ("capability", SpatialCapabilityEXT.ctype()),
        ("marker_id", c_uint32),
        ("data", SpatialBufferEXT),
    ]


class SpatialComponentMarkerListEXT(Structure):
    def __init__(
        self,
        marker_count: Optional[int] = None,
        markers: ArrayFieldParamType[SpatialMarkerDataEXT] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_COMPONENT_MARKER_LIST_EXT,
    ) -> None:
        marker_count, markers = array_field_helper(
            SpatialMarkerDataEXT, marker_count, markers)
        super().__init__(
            marker_count=marker_count,
            _markers=markers,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialComponentMarkerListEXT(marker_count={repr(self.marker_count)}, markers={repr(self._markers)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialComponentMarkerListEXT(marker_count={self.marker_count}, markers={self._markers}, next={self.next}, type={self.type})"

    @property
    def markers(self):
        if self.marker_count == 0:
            return (SpatialMarkerDataEXT * 0)()
        else:
            return (SpatialMarkerDataEXT * self.marker_count).from_address(
                ctypes.addressof(self._markers.contents))

    @markers.setter
    def markers(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.marker_count, self._markers = array_field_helper(
            SpatialMarkerDataEXT, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("marker_count", c_uint32),
        ("_markers", POINTER(SpatialMarkerDataEXT)),
    ]


class SpatialCapabilityConfigurationAnchorEXT(Structure):
    def __init__(
        self,
        capability: SpatialCapabilityEXT = SpatialCapabilityEXT(),  # noqa
        enabled_component_count: Optional[int] = None,
        enabled_components: ArrayFieldParamType[c_int] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_CAPABILITY_CONFIGURATION_ANCHOR_EXT,
    ) -> None:
        enabled_component_count, enabled_components = array_field_helper(
            c_int, enabled_component_count, enabled_components)
        super().__init__(
            capability=SpatialCapabilityEXT(capability).value,
            enabled_component_count=enabled_component_count,
            _enabled_components=enabled_components,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialCapabilityConfigurationAnchorEXT(capability={repr(self.capability)}, enabled_component_count={repr(self.enabled_component_count)}, enabled_components={repr(self._enabled_components)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialCapabilityConfigurationAnchorEXT(capability={self.capability}, enabled_component_count={self.enabled_component_count}, enabled_components={self._enabled_components}, next={self.next}, type={self.type})"

    @property
    def enabled_components(self):
        if self.enabled_component_count == 0:
            return (c_int * 0)()
        else:
            return (c_int * self.enabled_component_count).from_address(
                ctypes.addressof(self._enabled_components.contents))

    @enabled_components.setter
    def enabled_components(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.enabled_component_count, self._enabled_components = array_field_helper(
            c_int, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("capability", SpatialCapabilityEXT.ctype()),
        ("enabled_component_count", c_uint32),
        ("_enabled_components", POINTER(c_int)),
    ]


class SpatialComponentAnchorListEXT(Structure):
    def __init__(
        self,
        location_count: Optional[int] = None,
        locations: ArrayFieldParamType[Posef] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_COMPONENT_ANCHOR_LIST_EXT,
    ) -> None:
        location_count, locations = array_field_helper(
            Posef, location_count, locations)
        super().__init__(
            location_count=location_count,
            _locations=locations,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialComponentAnchorListEXT(location_count={repr(self.location_count)}, locations={repr(self._locations)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialComponentAnchorListEXT(location_count={self.location_count}, locations={self._locations}, next={self.next}, type={self.type})"

    @property
    def locations(self):
        if self.location_count == 0:
            return (Posef * 0)()
        else:
            return (Posef * self.location_count).from_address(
                ctypes.addressof(self._locations.contents))

    @locations.setter
    def locations(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.location_count, self._locations = array_field_helper(
            Posef, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("location_count", c_uint32),
        ("_locations", POINTER(Posef)),
    ]


class SpatialAnchorCreateInfoEXT(Structure):
    def __init__(
        self,
        base_space: Space = None,
        time: Time = 0,
        pose: Posef = Posef(),
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ANCHOR_CREATE_INFO_EXT,
    ) -> None:
        super().__init__(
            base_space=base_space,
            time=time,
            pose=pose,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialAnchorCreateInfoEXT(base_space={repr(self.base_space)}, time={repr(self.time)}, pose={repr(self.pose)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialAnchorCreateInfoEXT(base_space={self.base_space}, time={self.time}, pose={self.pose}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("base_space", Space),
        ("time", Time),
        ("pose", Posef),
    ]


PFN_xrCreateSpatialAnchorEXT = CFUNCTYPE(Result.ctype(), SpatialContextEXT, POINTER(SpatialAnchorCreateInfoEXT), POINTER(SpatialEntityIdEXT), POINTER(SpatialEntityEXT))


class SpatialPersistenceContextEXT_T(Structure):
    pass


class SpatialPersistenceContextEXT(POINTER(SpatialPersistenceContextEXT_T), HandleMixin):
    _type_ = SpatialPersistenceContextEXT_T  # ctypes idiosyncrasy


class SpatialPersistenceContextCreateInfoEXT(Structure):
    def __init__(
        self,
        scope: SpatialPersistenceScopeEXT = SpatialPersistenceScopeEXT(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_PERSISTENCE_CONTEXT_CREATE_INFO_EXT,
    ) -> None:
        super().__init__(
            scope=SpatialPersistenceScopeEXT(scope).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialPersistenceContextCreateInfoEXT(scope={repr(self.scope)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialPersistenceContextCreateInfoEXT(scope={self.scope}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("scope", SpatialPersistenceScopeEXT.ctype()),
    ]


class CreateSpatialPersistenceContextCompletionEXT(Structure):
    def __init__(
        self,
        future_result: Result = Result(),  # noqa
        create_result: SpatialPersistenceContextResultEXT = SpatialPersistenceContextResultEXT(),  # noqa
        persistence_context: SpatialPersistenceContextEXT = None,
        next: c_void_p = None,
        type: StructureType = StructureType.CREATE_SPATIAL_PERSISTENCE_CONTEXT_COMPLETION_EXT,
    ) -> None:
        super().__init__(
            future_result=Result(future_result).value,
            create_result=SpatialPersistenceContextResultEXT(create_result).value,
            persistence_context=persistence_context,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.CreateSpatialPersistenceContextCompletionEXT(future_result={repr(self.future_result)}, create_result={repr(self.create_result)}, persistence_context={repr(self.persistence_context)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.CreateSpatialPersistenceContextCompletionEXT(future_result={self.future_result}, create_result={self.create_result}, persistence_context={self.persistence_context}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("future_result", Result.ctype()),
        ("create_result", SpatialPersistenceContextResultEXT.ctype()),
        ("persistence_context", SpatialPersistenceContextEXT),
    ]


class SpatialContextPersistenceConfigEXT(Structure):
    def __init__(
        self,
        persistence_context_count: Optional[int] = None,
        persistence_contexts: ArrayFieldParamType[SpatialPersistenceContextEXT] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_CONTEXT_PERSISTENCE_CONFIG_EXT,
    ) -> None:
        persistence_context_count, persistence_contexts = array_field_helper(
            SpatialPersistenceContextEXT, persistence_context_count, persistence_contexts)
        super().__init__(
            persistence_context_count=persistence_context_count,
            _persistence_contexts=persistence_contexts,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialContextPersistenceConfigEXT(persistence_context_count={repr(self.persistence_context_count)}, persistence_contexts={repr(self._persistence_contexts)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialContextPersistenceConfigEXT(persistence_context_count={self.persistence_context_count}, persistence_contexts={self._persistence_contexts}, next={self.next}, type={self.type})"

    @property
    def persistence_contexts(self):
        if self.persistence_context_count == 0:
            return (SpatialPersistenceContextEXT * 0)()
        else:
            return (SpatialPersistenceContextEXT * self.persistence_context_count).from_address(
                ctypes.addressof(self._persistence_contexts.contents))

    @persistence_contexts.setter
    def persistence_contexts(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.persistence_context_count, self._persistence_contexts = array_field_helper(
            SpatialPersistenceContextEXT, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("persistence_context_count", c_uint32),
        ("_persistence_contexts", POINTER(SpatialPersistenceContextEXT)),
    ]


class SpatialDiscoveryPersistenceUuidFilterEXT(Structure):
    def __init__(
        self,
        persisted_uuid_count: Optional[int] = None,
        persisted_uuids: ArrayFieldParamType[Uuid] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_DISCOVERY_PERSISTENCE_UUID_FILTER_EXT,
    ) -> None:
        persisted_uuid_count, persisted_uuids = array_field_helper(
            Uuid, persisted_uuid_count, persisted_uuids)
        super().__init__(
            persisted_uuid_count=persisted_uuid_count,
            _persisted_uuids=persisted_uuids,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialDiscoveryPersistenceUuidFilterEXT(persisted_uuid_count={repr(self.persisted_uuid_count)}, persisted_uuids={repr(self._persisted_uuids)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialDiscoveryPersistenceUuidFilterEXT(persisted_uuid_count={self.persisted_uuid_count}, persisted_uuids={self._persisted_uuids}, next={self.next}, type={self.type})"

    @property
    def persisted_uuids(self):
        if self.persisted_uuid_count == 0:
            return (Uuid * 0)()
        else:
            return (Uuid * self.persisted_uuid_count).from_address(
                ctypes.addressof(self._persisted_uuids.contents))

    @persisted_uuids.setter
    def persisted_uuids(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.persisted_uuid_count, self._persisted_uuids = array_field_helper(
            Uuid, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("persisted_uuid_count", c_uint32),
        ("_persisted_uuids", POINTER(Uuid)),
    ]


class SpatialPersistenceDataEXT(Structure):
    def __init__(
        self,
        persist_uuid: Uuid = None,
        persist_state: SpatialPersistenceStateEXT = SpatialPersistenceStateEXT(),  # noqa
    ) -> None:
        if persist_uuid is None:
            persist_uuid = Uuid()
        super().__init__(
            persist_uuid=persist_uuid,
            persist_state=SpatialPersistenceStateEXT(persist_state).value,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialPersistenceDataEXT(persist_uuid={repr(self.persist_uuid)}, persist_state={repr(self.persist_state)})"

    def __str__(self) -> str:
        return f"xr.SpatialPersistenceDataEXT(persist_uuid={self.persist_uuid}, persist_state={self.persist_state})"

    _fields_ = [
        ("persist_uuid", Uuid),
        ("persist_state", SpatialPersistenceStateEXT.ctype()),
    ]


class SpatialComponentPersistenceListEXT(Structure):
    def __init__(
        self,
        persist_data_count: int = 0,
        persist_data: POINTER(SpatialPersistenceDataEXT) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_COMPONENT_PERSISTENCE_LIST_EXT,
    ) -> None:
        super().__init__(
            persist_data_count=persist_data_count,
            persist_data=persist_data,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialComponentPersistenceListEXT(persist_data_count={repr(self.persist_data_count)}, persist_data={repr(self.persist_data)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialComponentPersistenceListEXT(persist_data_count={self.persist_data_count}, persist_data={self.persist_data}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("persist_data_count", c_uint32),
        ("persist_data", POINTER(SpatialPersistenceDataEXT)),
    ]


PFN_xrEnumerateSpatialPersistenceScopesEXT = CFUNCTYPE(Result.ctype(), Instance, SystemId, c_uint32, POINTER(c_uint32), POINTER(SpatialPersistenceScopeEXT.ctype()))

PFN_xrCreateSpatialPersistenceContextAsyncEXT = CFUNCTYPE(Result.ctype(), Session, POINTER(SpatialPersistenceContextCreateInfoEXT), POINTER(FutureEXT))

PFN_xrCreateSpatialPersistenceContextCompleteEXT = CFUNCTYPE(Result.ctype(), Session, FutureEXT, POINTER(CreateSpatialPersistenceContextCompletionEXT))

PFN_xrDestroySpatialPersistenceContextEXT = CFUNCTYPE(Result.ctype(), SpatialPersistenceContextEXT)


class SpatialEntityPersistInfoEXT(Structure):
    def __init__(
        self,
        spatial_context: SpatialContextEXT = None,
        spatial_entity_id: SpatialEntityIdEXT = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ENTITY_PERSIST_INFO_EXT,
    ) -> None:
        super().__init__(
            spatial_context=spatial_context,
            spatial_entity_id=spatial_entity_id,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialEntityPersistInfoEXT(spatial_context={repr(self.spatial_context)}, spatial_entity_id={repr(self.spatial_entity_id)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialEntityPersistInfoEXT(spatial_context={self.spatial_context}, spatial_entity_id={self.spatial_entity_id}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("spatial_context", SpatialContextEXT),
        ("spatial_entity_id", SpatialEntityIdEXT),
    ]


class PersistSpatialEntityCompletionEXT(Structure):
    def __init__(
        self,
        future_result: Result = Result(),  # noqa
        persist_result: SpatialPersistenceContextResultEXT = SpatialPersistenceContextResultEXT(),  # noqa
        persist_uuid: Uuid = None,
        next: c_void_p = None,
        type: StructureType = StructureType.PERSIST_SPATIAL_ENTITY_COMPLETION_EXT,
    ) -> None:
        if persist_uuid is None:
            persist_uuid = Uuid()
        super().__init__(
            future_result=Result(future_result).value,
            persist_result=SpatialPersistenceContextResultEXT(persist_result).value,
            persist_uuid=persist_uuid,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.PersistSpatialEntityCompletionEXT(future_result={repr(self.future_result)}, persist_result={repr(self.persist_result)}, persist_uuid={repr(self.persist_uuid)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.PersistSpatialEntityCompletionEXT(future_result={self.future_result}, persist_result={self.persist_result}, persist_uuid={self.persist_uuid}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("future_result", Result.ctype()),
        ("persist_result", SpatialPersistenceContextResultEXT.ctype()),
        ("persist_uuid", Uuid),
    ]


class SpatialEntityUnpersistInfoEXT(Structure):
    def __init__(
        self,
        persist_uuid: Uuid = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SPATIAL_ENTITY_UNPERSIST_INFO_EXT,
    ) -> None:
        if persist_uuid is None:
            persist_uuid = Uuid()
        super().__init__(
            persist_uuid=persist_uuid,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SpatialEntityUnpersistInfoEXT(persist_uuid={repr(self.persist_uuid)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SpatialEntityUnpersistInfoEXT(persist_uuid={self.persist_uuid}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("persist_uuid", Uuid),
    ]


class UnpersistSpatialEntityCompletionEXT(Structure):
    def __init__(
        self,
        future_result: Result = Result(),  # noqa
        unpersist_result: SpatialPersistenceContextResultEXT = SpatialPersistenceContextResultEXT(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.UNPERSIST_SPATIAL_ENTITY_COMPLETION_EXT,
    ) -> None:
        super().__init__(
            future_result=Result(future_result).value,
            unpersist_result=SpatialPersistenceContextResultEXT(unpersist_result).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.UnpersistSpatialEntityCompletionEXT(future_result={repr(self.future_result)}, unpersist_result={repr(self.unpersist_result)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.UnpersistSpatialEntityCompletionEXT(future_result={self.future_result}, unpersist_result={self.unpersist_result}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("future_result", Result.ctype()),
        ("unpersist_result", SpatialPersistenceContextResultEXT.ctype()),
    ]


PFN_xrPersistSpatialEntityAsyncEXT = CFUNCTYPE(Result.ctype(), SpatialPersistenceContextEXT, POINTER(SpatialEntityPersistInfoEXT), POINTER(FutureEXT))

PFN_xrPersistSpatialEntityCompleteEXT = CFUNCTYPE(Result.ctype(), SpatialPersistenceContextEXT, FutureEXT, POINTER(PersistSpatialEntityCompletionEXT))

PFN_xrUnpersistSpatialEntityAsyncEXT = CFUNCTYPE(Result.ctype(), SpatialPersistenceContextEXT, POINTER(SpatialEntityUnpersistInfoEXT), POINTER(FutureEXT))

PFN_xrUnpersistSpatialEntityCompleteEXT = CFUNCTYPE(Result.ctype(), SpatialPersistenceContextEXT, FutureEXT, POINTER(UnpersistSpatialEntityCompletionEXT))


class LoaderInitPropertyValueEXT(Structure):
    def __init__(
        self,
        name: str = "",
        value: str = "",
    ) -> None:
        super().__init__(
            _name=name.encode(),
            _value=value.encode(),
        )

    def __repr__(self) -> str:
        return f"xr.LoaderInitPropertyValueEXT(name={repr(self._name)}, value={repr(self._value)})"

    def __str__(self) -> str:
        return f"xr.LoaderInitPropertyValueEXT(name={self._name}, value={self._value})"

    @property
    def name(self) -> str:
        return self._name.decode()
    
    @name.setter
    def name(self, value: str) -> None:
        # noinspection PyAttributeOutsideInit
        self._name = value.encode()

    @property
    def value(self) -> str:
        return self._value.decode()
    
    @value.setter
    def value(self, value: str) -> None:
        # noinspection PyAttributeOutsideInit
        self._value = value.encode()

    _fields_ = [
        ("_name", c_char_p),
        ("_value", c_char_p),
    ]


class LoaderInitInfoPropertiesEXT(Structure):
    def __init__(
        self,
        property_value_count: Optional[int] = None,
        property_values: ArrayFieldParamType[LoaderInitPropertyValueEXT] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.LOADER_INIT_INFO_PROPERTIES_EXT,
    ) -> None:
        property_value_count, property_values = array_field_helper(
            LoaderInitPropertyValueEXT, property_value_count, property_values)
        super().__init__(
            property_value_count=property_value_count,
            _property_values=property_values,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.LoaderInitInfoPropertiesEXT(property_value_count={repr(self.property_value_count)}, property_values={repr(self._property_values)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.LoaderInitInfoPropertiesEXT(property_value_count={self.property_value_count}, property_values={self._property_values}, next={self.next}, type={self.type})"

    @property
    def property_values(self):
        if self.property_value_count == 0:
            return (LoaderInitPropertyValueEXT * 0)()
        else:
            return (LoaderInitPropertyValueEXT * self.property_value_count).from_address(
                ctypes.addressof(self._property_values.contents))

    @property_values.setter
    def property_values(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.property_value_count, self._property_values = array_field_helper(
            LoaderInitPropertyValueEXT, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("property_value_count", c_uint32),
        ("_property_values", POINTER(LoaderInitPropertyValueEXT)),
    ]


__all__ = [
    "Action",
    "ActionCreateInfo",
    "ActionSet",
    "ActionSetCreateInfo",
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
    "ActiveActionSetPrioritiesEXT",
    "ActiveActionSetPriorityEXT",
    "AnchorBD",
    "AnchorBD_T",
    "AnchorSpaceCreateInfoANDROID",
    "AnchorSpaceCreateInfoBD",
    "ApiLayerProperties",
    "ApplicationInfo",
    "AsyncRequestIdFB",
    "BaseInStructure",
    "BaseOutStructure",
    "BindingModificationBaseHeaderKHR",
    "BindingModificationsKHR",
    "BodyJointLocationBD",
    "BodyJointLocationFB",
    "BodyJointLocationHTC",
    "BodyJointLocationsBD",
    "BodyJointLocationsFB",
    "BodyJointLocationsHTC",
    "BodyJointsLocateInfoBD",
    "BodyJointsLocateInfoFB",
    "BodyJointsLocateInfoHTC",
    "BodySkeletonFB",
    "BodySkeletonHTC",
    "BodySkeletonJointFB",
    "BodySkeletonJointHTC",
    "BodyTrackerBD",
    "BodyTrackerBD_T",
    "BodyTrackerCreateInfoBD",
    "BodyTrackerCreateInfoFB",
    "BodyTrackerCreateInfoHTC",
    "BodyTrackerFB",
    "BodyTrackerFB_T",
    "BodyTrackerHTC",
    "BodyTrackerHTC_T",
    "BodyTrackingCalibrationInfoMETA",
    "BodyTrackingCalibrationStatusMETA",
    "Bool32",
    "BoundSourcesForActionEnumerateInfo",
    "Boundary2DFB",
    "Boxf",
    "BoxfKHR",
    "ColocationAdvertisementStartInfoMETA",
    "ColocationAdvertisementStopInfoMETA",
    "ColocationDiscoveryStartInfoMETA",
    "ColocationDiscoveryStopInfoMETA",
    "Color3f",
    "Color3fKHR",
    "Color4f",
    "CompositionLayerAlphaBlendFB",
    "CompositionLayerBaseHeader",
    "CompositionLayerColorScaleBiasKHR",
    "CompositionLayerCubeKHR",
    "CompositionLayerCylinderKHR",
    "CompositionLayerDepthInfoKHR",
    "CompositionLayerDepthTestFB",
    "CompositionLayerDepthTestVARJO",
    "CompositionLayerEquirect2KHR",
    "CompositionLayerEquirectKHR",
    "CompositionLayerFlagsCInt",
    "CompositionLayerImageLayoutFB",
    "CompositionLayerImageLayoutFlagsFBCInt",
    "CompositionLayerPassthroughFB",
    "CompositionLayerPassthroughHTC",
    "CompositionLayerProjection",
    "CompositionLayerProjectionView",
    "CompositionLayerQuad",
    "CompositionLayerReprojectionInfoMSFT",
    "CompositionLayerReprojectionPlaneOverrideMSFT",
    "CompositionLayerSecureContentFB",
    "CompositionLayerSecureContentFlagsFBCInt",
    "CompositionLayerSettingsFB",
    "CompositionLayerSettingsFlagsFBCInt",
    "CompositionLayerSpaceWarpInfoFB",
    "CompositionLayerSpaceWarpInfoFlagsFBCInt",
    "ControllerModelKeyMSFT",
    "ControllerModelKeyStateMSFT",
    "ControllerModelNodePropertiesMSFT",
    "ControllerModelNodeStateMSFT",
    "ControllerModelPropertiesMSFT",
    "ControllerModelStateMSFT",
    "CreateSpatialAnchorsCompletionML",
    "CreateSpatialContextCompletionEXT",
    "CreateSpatialDiscoverySnapshotCompletionEXT",
    "CreateSpatialDiscoverySnapshotCompletionInfoEXT",
    "CreateSpatialPersistenceContextCompletionEXT",
    "DebugUtilsLabelEXT",
    "DebugUtilsMessageSeverityFlagsEXTCInt",
    "DebugUtilsMessageTypeFlagsEXTCInt",
    "DebugUtilsMessengerCallbackDataEXT",
    "DebugUtilsMessengerCreateInfoEXT",
    "DebugUtilsMessengerEXT",
    "DebugUtilsMessengerEXT_T",
    "DebugUtilsObjectNameInfoEXT",
    "DeserializeSceneFragmentMSFT",
    "DeviceAnchorPersistenceANDROID",
    "DeviceAnchorPersistenceANDROID_T",
    "DeviceAnchorPersistenceCreateInfoANDROID",
    "DevicePcmSampleRateGetInfoFB",
    "DevicePcmSampleRateStateFB",
    "DigitalLensControlALMALENCE",
    "DigitalLensControlFlagsALMALENCECInt",
    "Duration",
    "EnvironmentDepthHandRemovalSetInfoMETA",
    "EnvironmentDepthImageAcquireInfoMETA",
    "EnvironmentDepthImageMETA",
    "EnvironmentDepthImageViewMETA",
    "EnvironmentDepthProviderCreateFlagsMETACInt",
    "EnvironmentDepthProviderCreateInfoMETA",
    "EnvironmentDepthProviderMETA",
    "EnvironmentDepthProviderMETA_T",
    "EnvironmentDepthSwapchainCreateFlagsMETACInt",
    "EnvironmentDepthSwapchainCreateInfoMETA",
    "EnvironmentDepthSwapchainMETA",
    "EnvironmentDepthSwapchainMETA_T",
    "EnvironmentDepthSwapchainStateMETA",
    "EventDataBaseHeader",
    "EventDataBuffer",
    "EventDataColocationAdvertisementCompleteMETA",
    "EventDataColocationDiscoveryCompleteMETA",
    "EventDataColocationDiscoveryResultMETA",
    "EventDataDisplayRefreshRateChangedFB",
    "EventDataEventsLost",
    "EventDataEyeCalibrationChangedML",
    "EventDataHeadsetFitChangedML",
    "EventDataInstanceLossPending",
    "EventDataInteractionProfileChanged",
    "EventDataInteractionRenderModelsChangedEXT",
    "EventDataLocalizationChangedML",
    "EventDataMainSessionVisibilityChangedEXTX",
    "EventDataMarkerTrackingUpdateVARJO",
    "EventDataPassthroughLayerResumedMETA",
    "EventDataPassthroughStateChangedFB",
    "EventDataPerfSettingsEXT",
    "EventDataReferenceSpaceChangePending",
    "EventDataSceneCaptureCompleteFB",
    "EventDataSenseDataProviderStateChangedBD",
    "EventDataSenseDataUpdatedBD",
    "EventDataSessionStateChanged",
    "EventDataShareSpacesCompleteMETA",
    "EventDataSpaceEraseCompleteFB",
    "EventDataSpaceListSaveCompleteFB",
    "EventDataSpaceQueryCompleteFB",
    "EventDataSpaceQueryResultsAvailableFB",
    "EventDataSpaceSaveCompleteFB",
    "EventDataSpaceSetStatusCompleteFB",
    "EventDataSpaceShareCompleteFB",
    "EventDataSpacesEraseResultMETA",
    "EventDataSpacesSaveResultMETA",
    "EventDataSpatialAnchorCreateCompleteFB",
    "EventDataSpatialDiscoveryRecommendedEXT",
    "EventDataStartColocationAdvertisementCompleteMETA",
    "EventDataStartColocationDiscoveryCompleteMETA",
    "EventDataStopColocationAdvertisementCompleteMETA",
    "EventDataStopColocationDiscoveryCompleteMETA",
    "EventDataUserPresenceChangedEXT",
    "EventDataVirtualKeyboardBackspaceMETA",
    "EventDataVirtualKeyboardCommitTextMETA",
    "EventDataVirtualKeyboardEnterMETA",
    "EventDataVirtualKeyboardHiddenMETA",
    "EventDataVirtualKeyboardShownMETA",
    "EventDataVisibilityMaskChangedKHR",
    "EventDataViveTrackerConnectedHTCX",
    "ExportedLocalizationMapML",
    "ExportedLocalizationMapML_T",
    "ExtensionProperties",
    "Extent2Df",
    "Extent2Di",
    "Extent3Df",
    "Extent3DfEXT",
    "Extent3DfFB",
    "Extent3DfKHR",
    "ExternalCameraExtrinsicsOCULUS",
    "ExternalCameraIntrinsicsOCULUS",
    "ExternalCameraOCULUS",
    "ExternalCameraStatusFlagsOCULUSCInt",
    "EyeGazeFB",
    "EyeGazeSampleTimeEXT",
    "EyeGazesFB",
    "EyeGazesInfoFB",
    "EyeTrackerCreateInfoFB",
    "EyeTrackerFB",
    "EyeTrackerFB_T",
    "FaceExpressionInfo2FB",
    "FaceExpressionInfoFB",
    "FaceExpressionStatusFB",
    "FaceExpressionWeights2FB",
    "FaceExpressionWeightsFB",
    "FaceTracker2FB",
    "FaceTracker2FB_T",
    "FaceTrackerCreateInfo2FB",
    "FaceTrackerCreateInfoFB",
    "FaceTrackerFB",
    "FaceTrackerFB_T",
    "FacialExpressionBlendShapeGetInfoML",
    "FacialExpressionBlendShapePropertiesFlagsMLCInt",
    "FacialExpressionBlendShapePropertiesML",
    "FacialExpressionClientCreateInfoML",
    "FacialExpressionClientML",
    "FacialExpressionClientML_T",
    "FacialExpressionsHTC",
    "FacialTrackerCreateInfoHTC",
    "FacialTrackerHTC",
    "FacialTrackerHTC_T",
    "Flags64",
    "ForceFeedbackCurlApplyLocationMNDX",
    "ForceFeedbackCurlApplyLocationsMNDX",
    "FoveatedViewConfigurationViewVARJO",
    "FoveationApplyInfoHTC",
    "FoveationConfigurationHTC",
    "FoveationCustomModeInfoHTC",
    "FoveationDynamicFlagsHTCCInt",
    "FoveationDynamicModeInfoHTC",
    "FoveationEyeTrackedProfileCreateFlagsMETACInt",
    "FoveationEyeTrackedProfileCreateInfoMETA",
    "FoveationEyeTrackedStateFlagsMETACInt",
    "FoveationEyeTrackedStateMETA",
    "FoveationLevelProfileCreateInfoFB",
    "FoveationProfileCreateInfoFB",
    "FoveationProfileFB",
    "FoveationProfileFB_T",
    "Fovf",
    "FrameBeginInfo",
    "FrameEndInfo",
    "FrameEndInfoFlagsMLCInt",
    "FrameEndInfoML",
    "FrameState",
    "FrameSynthesisConfigViewEXT",
    "FrameSynthesisInfoEXT",
    "FrameSynthesisInfoFlagsEXTCInt",
    "FrameWaitInfo",
    "Frustumf",
    "FrustumfKHR",
    "FutureCancelInfoEXT",
    "FutureCompletionBaseHeaderEXT",
    "FutureCompletionEXT",
    "FutureEXT",
    "FutureEXT_T",
    "FuturePollInfoEXT",
    "FuturePollResultEXT",
    "FuturePollResultProgressBD",
    "GeometryInstanceCreateInfoFB",
    "GeometryInstanceFB",
    "GeometryInstanceFB_T",
    "GeometryInstanceTransformFB",
    "GlobalDimmerFrameEndInfoFlagsMLCInt",
    "GlobalDimmerFrameEndInfoML",
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
    "HandTrackerEXT",
    "HandTrackerEXT_T",
    "HandTrackingAimFlagsFBCInt",
    "HandTrackingAimStateFB",
    "HandTrackingCapsulesStateFB",
    "HandTrackingDataSourceInfoEXT",
    "HandTrackingDataSourceStateEXT",
    "HandTrackingMeshFB",
    "HandTrackingScaleFB",
    "HapticActionInfo",
    "HapticAmplitudeEnvelopeVibrationFB",
    "HapticBaseHeader",
    "HapticPcmVibrationFB",
    "HapticVibration",
    "InputSourceLocalizedNameFlagsCInt",
    "InputSourceLocalizedNameGetInfo",
    "Instance",
    "InstanceCreateFlagsCInt",
    "InstanceCreateInfo",
    "InstanceProperties",
    "Instance_T",
    "InteractionProfileAnalogThresholdVALVE",
    "InteractionProfileDpadBindingEXT",
    "InteractionProfileState",
    "InteractionProfileSuggestedBinding",
    "InteractionRenderModelIdsEnumerateInfoEXT",
    "InteractionRenderModelSubactionPathInfoEXT",
    "InteractionRenderModelTopLevelUserPathGetInfoEXT",
    "KeyboardSpaceCreateInfoFB",
    "KeyboardTrackingDescriptionFB",
    "KeyboardTrackingFlagsFBCInt",
    "KeyboardTrackingQueryFB",
    "KeyboardTrackingQueryFlagsFBCInt",
    "LoaderInitInfoBaseHeaderKHR",
    "LoaderInitInfoPropertiesEXT",
    "LoaderInitPropertyValueEXT",
    "LocalDimmingFrameEndInfoMETA",
    "LocalizationEnableEventsInfoML",
    "LocalizationMapErrorFlagsMLCInt",
    "LocalizationMapImportInfoML",
    "LocalizationMapML",
    "LocalizationMapQueryInfoBaseHeaderML",
    "MapLocalizationRequestInfoML",
    "MarkerDetectorAprilTagInfoML",
    "MarkerDetectorArucoInfoML",
    "MarkerDetectorCreateInfoML",
    "MarkerDetectorCustomProfileInfoML",
    "MarkerDetectorML",
    "MarkerDetectorML_T",
    "MarkerDetectorSizeInfoML",
    "MarkerDetectorSnapshotInfoML",
    "MarkerDetectorStateML",
    "MarkerML",
    "MarkerSpaceCreateInfoML",
    "MarkerSpaceCreateInfoVARJO",
    "NewSceneComputeInfoMSFT",
    "Offset2Df",
    "Offset2Di",
    "Offset3DfFB",
    "OverlayMainSessionFlagsEXTXCInt",
    "OverlaySessionCreateFlagsEXTXCInt",
    "PFN_xrAcquireEnvironmentDepthImageMETA",
    "PFN_xrAcquireSwapchainImage",
    "PFN_xrAllocateWorldMeshBufferML",
    "PFN_xrApplyForceFeedbackCurlMNDX",
    "PFN_xrApplyFoveationHTC",
    "PFN_xrApplyHapticFeedback",
    "PFN_xrAttachSessionActionSets",
    "PFN_xrBeginFrame",
    "PFN_xrBeginPlaneDetectionEXT",
    "PFN_xrBeginSession",
    "PFN_xrCancelFutureEXT",
    "PFN_xrCaptureSceneAsyncBD",
    "PFN_xrCaptureSceneCompleteBD",
    "PFN_xrChangeVirtualKeyboardTextContextMETA",
    "PFN_xrClearSpatialAnchorStoreMSFT",
    "PFN_xrComputeNewSceneMSFT",
    "PFN_xrCreateAction",
    "PFN_xrCreateActionSet",
    "PFN_xrCreateActionSpace",
    "PFN_xrCreateAnchorSpaceANDROID",
    "PFN_xrCreateAnchorSpaceBD",
    "PFN_xrCreateBodyTrackerBD",
    "PFN_xrCreateBodyTrackerFB",
    "PFN_xrCreateBodyTrackerHTC",
    "PFN_xrCreateDebugUtilsMessengerEXT",
    "PFN_xrCreateDeviceAnchorPersistenceANDROID",
    "PFN_xrCreateEnvironmentDepthProviderMETA",
    "PFN_xrCreateEnvironmentDepthSwapchainMETA",
    "PFN_xrCreateExportedLocalizationMapML",
    "PFN_xrCreateEyeTrackerFB",
    "PFN_xrCreateFaceTracker2FB",
    "PFN_xrCreateFaceTrackerFB",
    "PFN_xrCreateFacialExpressionClientML",
    "PFN_xrCreateFacialTrackerHTC",
    "PFN_xrCreateFoveationProfileFB",
    "PFN_xrCreateGeometryInstanceFB",
    "PFN_xrCreateHandMeshSpaceMSFT",
    "PFN_xrCreateHandTrackerEXT",
    "PFN_xrCreateInstance",
    "PFN_xrCreateKeyboardSpaceFB",
    "PFN_xrCreateMarkerDetectorML",
    "PFN_xrCreateMarkerSpaceML",
    "PFN_xrCreateMarkerSpaceVARJO",
    "PFN_xrCreatePassthroughColorLutMETA",
    "PFN_xrCreatePassthroughFB",
    "PFN_xrCreatePassthroughHTC",
    "PFN_xrCreatePassthroughLayerFB",
    "PFN_xrCreatePersistedAnchorSpaceANDROID",
    "PFN_xrCreatePlaneDetectorEXT",
    "PFN_xrCreateReferenceSpace",
    "PFN_xrCreateRenderModelAssetEXT",
    "PFN_xrCreateRenderModelEXT",
    "PFN_xrCreateRenderModelSpaceEXT",
    "PFN_xrCreateSceneMSFT",
    "PFN_xrCreateSceneObserverMSFT",
    "PFN_xrCreateSenseDataProviderBD",
    "PFN_xrCreateSession",
    "PFN_xrCreateSpaceUserFB",
    "PFN_xrCreateSpatialAnchorAsyncBD",
    "PFN_xrCreateSpatialAnchorCompleteBD",
    "PFN_xrCreateSpatialAnchorEXT",
    "PFN_xrCreateSpatialAnchorFB",
    "PFN_xrCreateSpatialAnchorFromPersistedNameMSFT",
    "PFN_xrCreateSpatialAnchorHTC",
    "PFN_xrCreateSpatialAnchorMSFT",
    "PFN_xrCreateSpatialAnchorSpaceMSFT",
    "PFN_xrCreateSpatialAnchorStoreConnectionMSFT",
    "PFN_xrCreateSpatialAnchorsAsyncML",
    "PFN_xrCreateSpatialAnchorsCompleteML",
    "PFN_xrCreateSpatialAnchorsStorageML",
    "PFN_xrCreateSpatialContextAsyncEXT",
    "PFN_xrCreateSpatialContextCompleteEXT",
    "PFN_xrCreateSpatialDiscoverySnapshotAsyncEXT",
    "PFN_xrCreateSpatialDiscoverySnapshotCompleteEXT",
    "PFN_xrCreateSpatialEntityAnchorBD",
    "PFN_xrCreateSpatialEntityFromIdEXT",
    "PFN_xrCreateSpatialGraphNodeSpaceMSFT",
    "PFN_xrCreateSpatialPersistenceContextAsyncEXT",
    "PFN_xrCreateSpatialPersistenceContextCompleteEXT",
    "PFN_xrCreateSpatialUpdateSnapshotEXT",
    "PFN_xrCreateSwapchain",
    "PFN_xrCreateTrackableTrackerANDROID",
    "PFN_xrCreateTriangleMeshFB",
    "PFN_xrCreateVirtualKeyboardMETA",
    "PFN_xrCreateVirtualKeyboardSpaceMETA",
    "PFN_xrCreateWorldMeshDetectorML",
    "PFN_xrDebugUtilsMessengerCallbackEXT",
    "PFN_xrDeleteSpatialAnchorsAsyncML",
    "PFN_xrDeleteSpatialAnchorsCompleteML",
    "PFN_xrDeserializeSceneMSFT",
    "PFN_xrDestroyAction",
    "PFN_xrDestroyActionSet",
    "PFN_xrDestroyAnchorBD",
    "PFN_xrDestroyBodyTrackerBD",
    "PFN_xrDestroyBodyTrackerFB",
    "PFN_xrDestroyBodyTrackerHTC",
    "PFN_xrDestroyDebugUtilsMessengerEXT",
    "PFN_xrDestroyDeviceAnchorPersistenceANDROID",
    "PFN_xrDestroyEnvironmentDepthProviderMETA",
    "PFN_xrDestroyEnvironmentDepthSwapchainMETA",
    "PFN_xrDestroyExportedLocalizationMapML",
    "PFN_xrDestroyEyeTrackerFB",
    "PFN_xrDestroyFaceTracker2FB",
    "PFN_xrDestroyFaceTrackerFB",
    "PFN_xrDestroyFacialExpressionClientML",
    "PFN_xrDestroyFacialTrackerHTC",
    "PFN_xrDestroyFoveationProfileFB",
    "PFN_xrDestroyGeometryInstanceFB",
    "PFN_xrDestroyHandTrackerEXT",
    "PFN_xrDestroyInstance",
    "PFN_xrDestroyMarkerDetectorML",
    "PFN_xrDestroyPassthroughColorLutMETA",
    "PFN_xrDestroyPassthroughFB",
    "PFN_xrDestroyPassthroughHTC",
    "PFN_xrDestroyPassthroughLayerFB",
    "PFN_xrDestroyPlaneDetectorEXT",
    "PFN_xrDestroyRenderModelAssetEXT",
    "PFN_xrDestroyRenderModelEXT",
    "PFN_xrDestroySceneMSFT",
    "PFN_xrDestroySceneObserverMSFT",
    "PFN_xrDestroySenseDataProviderBD",
    "PFN_xrDestroySenseDataSnapshotBD",
    "PFN_xrDestroySession",
    "PFN_xrDestroySpace",
    "PFN_xrDestroySpaceUserFB",
    "PFN_xrDestroySpatialAnchorMSFT",
    "PFN_xrDestroySpatialAnchorStoreConnectionMSFT",
    "PFN_xrDestroySpatialAnchorsStorageML",
    "PFN_xrDestroySpatialContextEXT",
    "PFN_xrDestroySpatialEntityEXT",
    "PFN_xrDestroySpatialGraphNodeBindingMSFT",
    "PFN_xrDestroySpatialPersistenceContextEXT",
    "PFN_xrDestroySpatialSnapshotEXT",
    "PFN_xrDestroySwapchain",
    "PFN_xrDestroyTrackableTrackerANDROID",
    "PFN_xrDestroyTriangleMeshFB",
    "PFN_xrDestroyVirtualKeyboardMETA",
    "PFN_xrDestroyWorldMeshDetectorML",
    "PFN_xrDownloadSharedSpatialAnchorAsyncBD",
    "PFN_xrDownloadSharedSpatialAnchorCompleteBD",
    "PFN_xrEnableLocalizationEventsML",
    "PFN_xrEnableUserCalibrationEventsML",
    "PFN_xrEndFrame",
    "PFN_xrEndSession",
    "PFN_xrEnumerateApiLayerProperties",
    "PFN_xrEnumerateBoundSourcesForAction",
    "PFN_xrEnumerateColorSpacesFB",
    "PFN_xrEnumerateDisplayRefreshRatesFB",
    "PFN_xrEnumerateEnvironmentBlendModes",
    "PFN_xrEnumerateEnvironmentDepthSwapchainImagesMETA",
    "PFN_xrEnumerateExternalCamerasOCULUS",
    "PFN_xrEnumerateInstanceExtensionProperties",
    "PFN_xrEnumerateInteractionRenderModelIdsEXT",
    "PFN_xrEnumeratePerformanceMetricsCounterPathsMETA",
    "PFN_xrEnumeratePersistedAnchorsANDROID",
    "PFN_xrEnumeratePersistedSpatialAnchorNamesMSFT",
    "PFN_xrEnumerateRaycastSupportedTrackableTypesANDROID",
    "PFN_xrEnumerateReferenceSpaces",
    "PFN_xrEnumerateRenderModelPathsFB",
    "PFN_xrEnumerateRenderModelSubactionPathsEXT",
    "PFN_xrEnumerateReprojectionModesMSFT",
    "PFN_xrEnumerateSceneComputeFeaturesMSFT",
    "PFN_xrEnumerateSpaceSupportedComponentsFB",
    "PFN_xrEnumerateSpatialCapabilitiesEXT",
    "PFN_xrEnumerateSpatialCapabilityComponentTypesEXT",
    "PFN_xrEnumerateSpatialCapabilityFeaturesEXT",
    "PFN_xrEnumerateSpatialEntityComponentTypesBD",
    "PFN_xrEnumerateSpatialPersistenceScopesEXT",
    "PFN_xrEnumerateSupportedAnchorTrackableTypesANDROID",
    "PFN_xrEnumerateSupportedPersistenceAnchorTypesANDROID",
    "PFN_xrEnumerateSupportedTrackableTypesANDROID",
    "PFN_xrEnumerateSwapchainFormats",
    "PFN_xrEnumerateSwapchainImages",
    "PFN_xrEnumerateViewConfigurationViews",
    "PFN_xrEnumerateViewConfigurations",
    "PFN_xrEnumerateViveTrackerPathsHTCX",
    "PFN_xrEraseSpaceFB",
    "PFN_xrEraseSpacesMETA",
    "PFN_xrFreeWorldMeshBufferML",
    "PFN_xrGeometryInstanceSetTransformFB",
    "PFN_xrGetActionStateBoolean",
    "PFN_xrGetActionStateFloat",
    "PFN_xrGetActionStatePose",
    "PFN_xrGetActionStateVector2f",
    "PFN_xrGetAllTrackablesANDROID",
    "PFN_xrGetAnchorPersistStateANDROID",
    "PFN_xrGetAnchorUuidBD",
    "PFN_xrGetBodySkeletonFB",
    "PFN_xrGetBodySkeletonHTC",
    "PFN_xrGetControllerModelKeyMSFT",
    "PFN_xrGetControllerModelPropertiesMSFT",
    "PFN_xrGetControllerModelStateMSFT",
    "PFN_xrGetCurrentInteractionProfile",
    "PFN_xrGetDeviceSampleRateFB",
    "PFN_xrGetDisplayRefreshRateFB",
    "PFN_xrGetEnvironmentDepthSwapchainStateMETA",
    "PFN_xrGetExportedLocalizationMapDataML",
    "PFN_xrGetEyeGazesFB",
    "PFN_xrGetFaceExpressionWeights2FB",
    "PFN_xrGetFaceExpressionWeightsFB",
    "PFN_xrGetFacialExpressionBlendShapePropertiesML",
    "PFN_xrGetFacialExpressionsHTC",
    "PFN_xrGetFoveationEyeTrackedStateMETA",
    "PFN_xrGetHandMeshFB",
    "PFN_xrGetInputSourceLocalizedName",
    "PFN_xrGetInstanceProcAddr",
    "PFN_xrGetInstanceProperties",
    "PFN_xrGetMarkerDetectorStateML",
    "PFN_xrGetMarkerLengthML",
    "PFN_xrGetMarkerNumberML",
    "PFN_xrGetMarkerReprojectionErrorML",
    "PFN_xrGetMarkerSizeVARJO",
    "PFN_xrGetMarkerStringML",
    "PFN_xrGetMarkersML",
    "PFN_xrGetPassthroughCameraStateANDROID",
    "PFN_xrGetPassthroughPreferencesMETA",
    "PFN_xrGetPerformanceMetricsStateMETA",
    "PFN_xrGetPlaneDetectionStateEXT",
    "PFN_xrGetPlaneDetectionsEXT",
    "PFN_xrGetPlanePolygonBufferEXT",
    "PFN_xrGetQueriedSenseDataBD",
    "PFN_xrGetRecommendedLayerResolutionMETA",
    "PFN_xrGetReferenceSpaceBoundsRect",
    "PFN_xrGetRenderModelAssetDataEXT",
    "PFN_xrGetRenderModelAssetPropertiesEXT",
    "PFN_xrGetRenderModelPoseTopLevelUserPathEXT",
    "PFN_xrGetRenderModelPropertiesEXT",
    "PFN_xrGetRenderModelPropertiesFB",
    "PFN_xrGetRenderModelStateEXT",
    "PFN_xrGetSceneComponentsMSFT",
    "PFN_xrGetSceneComputeStateMSFT",
    "PFN_xrGetSceneMarkerDecodedStringMSFT",
    "PFN_xrGetSceneMarkerRawDataMSFT",
    "PFN_xrGetSceneMeshBuffersMSFT",
    "PFN_xrGetSenseDataProviderStateBD",
    "PFN_xrGetSerializedSceneFragmentDataMSFT",
    "PFN_xrGetSpaceBoundary2DFB",
    "PFN_xrGetSpaceBoundingBox2DFB",
    "PFN_xrGetSpaceBoundingBox3DFB",
    "PFN_xrGetSpaceComponentStatusFB",
    "PFN_xrGetSpaceContainerFB",
    "PFN_xrGetSpaceRoomLayoutFB",
    "PFN_xrGetSpaceSemanticLabelsFB",
    "PFN_xrGetSpaceTriangleMeshMETA",
    "PFN_xrGetSpaceUserIdFB",
    "PFN_xrGetSpaceUuidFB",
    "PFN_xrGetSpatialAnchorNameHTC",
    "PFN_xrGetSpatialAnchorStateML",
    "PFN_xrGetSpatialBufferFloatEXT",
    "PFN_xrGetSpatialBufferStringEXT",
    "PFN_xrGetSpatialBufferUint16EXT",
    "PFN_xrGetSpatialBufferUint32EXT",
    "PFN_xrGetSpatialBufferUint8EXT",
    "PFN_xrGetSpatialBufferVector2fEXT",
    "PFN_xrGetSpatialBufferVector3fEXT",
    "PFN_xrGetSpatialEntityComponentDataBD",
    "PFN_xrGetSpatialEntityUuidBD",
    "PFN_xrGetSpatialGraphNodeBindingPropertiesMSFT",
    "PFN_xrGetSwapchainStateFB",
    "PFN_xrGetSystem",
    "PFN_xrGetSystemProperties",
    "PFN_xrGetTrackableMarkerANDROID",
    "PFN_xrGetTrackableObjectANDROID",
    "PFN_xrGetTrackablePlaneANDROID",
    "PFN_xrGetViewConfigurationProperties",
    "PFN_xrGetVirtualKeyboardDirtyTexturesMETA",
    "PFN_xrGetVirtualKeyboardModelAnimationStatesMETA",
    "PFN_xrGetVirtualKeyboardScaleMETA",
    "PFN_xrGetVirtualKeyboardTextureDataMETA",
    "PFN_xrGetVisibilityMaskKHR",
    "PFN_xrGetWorldMeshBufferRecommendSizeML",
    "PFN_xrImportLocalizationMapML",
    "PFN_xrInitializeLoaderKHR",
    "PFN_xrLoadControllerModelMSFT",
    "PFN_xrLoadRenderModelFB",
    "PFN_xrLocateBodyJointsBD",
    "PFN_xrLocateBodyJointsFB",
    "PFN_xrLocateBodyJointsHTC",
    "PFN_xrLocateHandJointsEXT",
    "PFN_xrLocateSceneComponentsMSFT",
    "PFN_xrLocateSpace",
    "PFN_xrLocateSpaces",
    "PFN_xrLocateSpacesKHR",
    "PFN_xrLocateViews",
    "PFN_xrPassthroughLayerPauseFB",
    "PFN_xrPassthroughLayerResumeFB",
    "PFN_xrPassthroughLayerSetKeyboardHandsIntensityFB",
    "PFN_xrPassthroughLayerSetStyleFB",
    "PFN_xrPassthroughPauseFB",
    "PFN_xrPassthroughStartFB",
    "PFN_xrPathToString",
    "PFN_xrPauseSimultaneousHandsAndControllersTrackingMETA",
    "PFN_xrPerfSettingsSetPerformanceLevelEXT",
    "PFN_xrPersistAnchorANDROID",
    "PFN_xrPersistSpatialAnchorAsyncBD",
    "PFN_xrPersistSpatialAnchorCompleteBD",
    "PFN_xrPersistSpatialAnchorMSFT",
    "PFN_xrPersistSpatialEntityAsyncEXT",
    "PFN_xrPersistSpatialEntityCompleteEXT",
    "PFN_xrPollEvent",
    "PFN_xrPollFutureEXT",
    "PFN_xrPublishSpatialAnchorsAsyncML",
    "PFN_xrPublishSpatialAnchorsCompleteML",
    "PFN_xrQueryLocalizationMapsML",
    "PFN_xrQueryPerformanceMetricsCounterMETA",
    "PFN_xrQuerySenseDataAsyncBD",
    "PFN_xrQuerySenseDataCompleteBD",
    "PFN_xrQuerySpacesFB",
    "PFN_xrQuerySpatialAnchorsAsyncML",
    "PFN_xrQuerySpatialAnchorsCompleteML",
    "PFN_xrQuerySpatialComponentDataEXT",
    "PFN_xrQuerySystemTrackedKeyboardFB",
    "PFN_xrRaycastANDROID",
    "PFN_xrReleaseSwapchainImage",
    "PFN_xrRequestDisplayRefreshRateFB",
    "PFN_xrRequestExitSession",
    "PFN_xrRequestMapLocalizationML",
    "PFN_xrRequestSceneCaptureFB",
    "PFN_xrRequestWorldMeshAsyncML",
    "PFN_xrRequestWorldMeshCompleteML",
    "PFN_xrRequestWorldMeshStateAsyncML",
    "PFN_xrRequestWorldMeshStateCompleteML",
    "PFN_xrResetBodyTrackingCalibrationMETA",
    "PFN_xrResultToString",
    "PFN_xrResumeSimultaneousHandsAndControllersTrackingMETA",
    "PFN_xrRetrieveSpaceQueryResultsFB",
    "PFN_xrSaveSpaceFB",
    "PFN_xrSaveSpaceListFB",
    "PFN_xrSaveSpacesMETA",
    "PFN_xrSendVirtualKeyboardInputMETA",
    "PFN_xrSessionBeginDebugUtilsLabelRegionEXT",
    "PFN_xrSessionEndDebugUtilsLabelRegionEXT",
    "PFN_xrSessionInsertDebugUtilsLabelEXT",
    "PFN_xrSetColorSpaceFB",
    "PFN_xrSetDebugUtilsObjectNameEXT",
    "PFN_xrSetDigitalLensControlALMALENCE",
    "PFN_xrSetEnvironmentDepthEstimationVARJO",
    "PFN_xrSetEnvironmentDepthHandRemovalMETA",
    "PFN_xrSetInputDeviceActiveEXT",
    "PFN_xrSetInputDeviceLocationEXT",
    "PFN_xrSetInputDeviceStateBoolEXT",
    "PFN_xrSetInputDeviceStateFloatEXT",
    "PFN_xrSetInputDeviceStateVector2fEXT",
    "PFN_xrSetMarkerTrackingPredictionVARJO",
    "PFN_xrSetMarkerTrackingTimeoutVARJO",
    "PFN_xrSetMarkerTrackingVARJO",
    "PFN_xrSetPerformanceMetricsStateMETA",
    "PFN_xrSetSpaceComponentStatusFB",
    "PFN_xrSetSystemNotificationsML",
    "PFN_xrSetTrackingOptimizationSettingsHintQCOM",
    "PFN_xrSetViewOffsetVARJO",
    "PFN_xrSetVirtualKeyboardModelVisibilityMETA",
    "PFN_xrShareSpacesFB",
    "PFN_xrShareSpacesMETA",
    "PFN_xrShareSpatialAnchorAsyncBD",
    "PFN_xrShareSpatialAnchorCompleteBD",
    "PFN_xrSnapshotMarkerDetectorML",
    "PFN_xrStartColocationAdvertisementMETA",
    "PFN_xrStartColocationDiscoveryMETA",
    "PFN_xrStartEnvironmentDepthProviderMETA",
    "PFN_xrStartSenseDataProviderAsyncBD",
    "PFN_xrStartSenseDataProviderCompleteBD",
    "PFN_xrStopColocationAdvertisementMETA",
    "PFN_xrStopColocationDiscoveryMETA",
    "PFN_xrStopEnvironmentDepthProviderMETA",
    "PFN_xrStopHapticFeedback",
    "PFN_xrStopSenseDataProviderBD",
    "PFN_xrStringToPath",
    "PFN_xrStructureTypeToString",
    "PFN_xrStructureTypeToString2KHR",
    "PFN_xrSubmitDebugUtilsMessageEXT",
    "PFN_xrSuggestBodyTrackingCalibrationOverrideMETA",
    "PFN_xrSuggestInteractionProfileBindings",
    "PFN_xrSuggestVirtualKeyboardLocationMETA",
    "PFN_xrSyncActions",
    "PFN_xrThermalGetTemperatureTrendEXT",
    "PFN_xrTriangleMeshBeginUpdateFB",
    "PFN_xrTriangleMeshBeginVertexBufferUpdateFB",
    "PFN_xrTriangleMeshEndUpdateFB",
    "PFN_xrTriangleMeshEndVertexBufferUpdateFB",
    "PFN_xrTriangleMeshGetIndexBufferFB",
    "PFN_xrTriangleMeshGetVertexBufferFB",
    "PFN_xrTryCreateSpatialGraphStaticNodeBindingMSFT",
    "PFN_xrUnpersistAnchorANDROID",
    "PFN_xrUnpersistSpatialAnchorAsyncBD",
    "PFN_xrUnpersistSpatialAnchorCompleteBD",
    "PFN_xrUnpersistSpatialAnchorMSFT",
    "PFN_xrUnpersistSpatialEntityAsyncEXT",
    "PFN_xrUnpersistSpatialEntityCompleteEXT",
    "PFN_xrUpdateHandMeshMSFT",
    "PFN_xrUpdatePassthroughColorLutMETA",
    "PFN_xrUpdateSpatialAnchorsExpirationAsyncML",
    "PFN_xrUpdateSpatialAnchorsExpirationCompleteML",
    "PFN_xrUpdateSwapchainFB",
    "PFN_xrVoidFunction",
    "PFN_xrWaitFrame",
    "PFN_xrWaitSwapchainImage",
    "PassthroughBrightnessContrastSaturationFB",
    "PassthroughCameraStateGetInfoANDROID",
    "PassthroughCapabilityFlagsFBCInt",
    "PassthroughColorHTC",
    "PassthroughColorLutCreateInfoMETA",
    "PassthroughColorLutDataMETA",
    "PassthroughColorLutMETA",
    "PassthroughColorLutMETA_T",
    "PassthroughColorLutUpdateInfoMETA",
    "PassthroughColorMapInterpolatedLutMETA",
    "PassthroughColorMapLutMETA",
    "PassthroughColorMapMonoToMonoFB",
    "PassthroughColorMapMonoToRgbaFB",
    "PassthroughCreateInfoFB",
    "PassthroughCreateInfoHTC",
    "PassthroughFB",
    "PassthroughFB_T",
    "PassthroughFlagsFBCInt",
    "PassthroughHTC",
    "PassthroughHTC_T",
    "PassthroughKeyboardHandsIntensityFB",
    "PassthroughLayerCreateInfoFB",
    "PassthroughLayerFB",
    "PassthroughLayerFB_T",
    "PassthroughMeshTransformInfoHTC",
    "PassthroughPreferenceFlagsMETACInt",
    "PassthroughPreferencesMETA",
    "PassthroughStateChangedFlagsFBCInt",
    "PassthroughStyleFB",
    "Path",
    "PerformanceMetricsCounterFlagsMETACInt",
    "PerformanceMetricsCounterMETA",
    "PerformanceMetricsStateMETA",
    "PersistSpatialEntityCompletionEXT",
    "PersistedAnchorSpaceCreateInfoANDROID",
    "PersistedAnchorSpaceInfoANDROID",
    "PlaneDetectionCapabilityFlagsEXTCInt",
    "PlaneDetectorBeginInfoEXT",
    "PlaneDetectorCreateInfoEXT",
    "PlaneDetectorEXT",
    "PlaneDetectorEXT_T",
    "PlaneDetectorFlagsEXTCInt",
    "PlaneDetectorGetInfoEXT",
    "PlaneDetectorLocationEXT",
    "PlaneDetectorLocationsEXT",
    "PlaneDetectorPolygonBufferEXT",
    "Posef",
    "Quaternionf",
    "QueriedSenseDataBD",
    "QueriedSenseDataGetInfoBD",
    "RaycastHitResultANDROID",
    "RaycastHitResultsANDROID",
    "RaycastInfoANDROID",
    "RecommendedLayerResolutionGetInfoMETA",
    "RecommendedLayerResolutionMETA",
    "Rect2Df",
    "Rect2Di",
    "Rect3DfFB",
    "ReferenceSpaceCreateInfo",
    "RenderModelAssetCreateInfoEXT",
    "RenderModelAssetDataEXT",
    "RenderModelAssetDataGetInfoEXT",
    "RenderModelAssetEXT",
    "RenderModelAssetEXT_T",
    "RenderModelAssetNodePropertiesEXT",
    "RenderModelAssetPropertiesEXT",
    "RenderModelAssetPropertiesGetInfoEXT",
    "RenderModelBufferFB",
    "RenderModelCapabilitiesRequestFB",
    "RenderModelCreateInfoEXT",
    "RenderModelEXT",
    "RenderModelEXT_T",
    "RenderModelFlagsFBCInt",
    "RenderModelIdEXT",
    "RenderModelKeyFB",
    "RenderModelLoadInfoFB",
    "RenderModelNodeStateEXT",
    "RenderModelPathInfoFB",
    "RenderModelPropertiesEXT",
    "RenderModelPropertiesFB",
    "RenderModelPropertiesGetInfoEXT",
    "RenderModelSpaceCreateInfoEXT",
    "RenderModelStateEXT",
    "RenderModelStateGetInfoEXT",
    "RoomLayoutFB",
    "SceneBoundsMSFT",
    "SceneCaptureInfoBD",
    "SceneCaptureRequestInfoFB",
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
    "SceneMSFT",
    "SceneMSFT_T",
    "SceneMarkerMSFT",
    "SceneMarkerQRCodeMSFT",
    "SceneMarkerQRCodesMSFT",
    "SceneMarkerTypeFilterMSFT",
    "SceneMarkersMSFT",
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
    "SceneObserverMSFT",
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
    "SemanticLabelsFB",
    "SemanticLabelsSupportFlagsFBCInt",
    "SemanticLabelsSupportInfoFB",
    "SenseDataFilterPlaneOrientationBD",
    "SenseDataFilterSemanticBD",
    "SenseDataFilterUuidBD",
    "SenseDataProviderBD",
    "SenseDataProviderBD_T",
    "SenseDataProviderCreateInfoBD",
    "SenseDataProviderCreateInfoSpatialMeshBD",
    "SenseDataProviderStartInfoBD",
    "SenseDataQueryCompletionBD",
    "SenseDataQueryInfoBD",
    "SenseDataSnapshotBD",
    "SenseDataSnapshotBD_T",
    "SerializedSceneFragmentDataGetInfoMSFT",
    "Session",
    "SessionActionSetsAttachInfo",
    "SessionBeginInfo",
    "SessionCreateFlagsCInt",
    "SessionCreateInfo",
    "SessionCreateInfoOverlayEXTX",
    "Session_T",
    "ShareSpacesInfoMETA",
    "ShareSpacesRecipientBaseHeaderMETA",
    "ShareSpacesRecipientGroupsMETA",
    "SharedSpatialAnchorDownloadInfoBD",
    "SimultaneousHandsAndControllersTrackingPauseInfoMETA",
    "SimultaneousHandsAndControllersTrackingResumeInfoMETA",
    "Space",
    "SpaceComponentFilterInfoFB",
    "SpaceComponentStatusFB",
    "SpaceComponentStatusSetInfoFB",
    "SpaceContainerFB",
    "SpaceEraseInfoFB",
    "SpaceFilterInfoBaseHeaderFB",
    "SpaceGroupUuidFilterInfoMETA",
    "SpaceListSaveInfoFB",
    "SpaceLocation",
    "SpaceLocationData",
    "SpaceLocationDataKHR",
    "SpaceLocationFlagsCInt",
    "SpaceLocations",
    "SpaceLocationsKHR",
    "SpaceQueryInfoBaseHeaderFB",
    "SpaceQueryInfoFB",
    "SpaceQueryResultFB",
    "SpaceQueryResultsFB",
    "SpaceSaveInfoFB",
    "SpaceShareInfoFB",
    "SpaceStorageLocationFilterInfoFB",
    "SpaceTriangleMeshGetInfoMETA",
    "SpaceTriangleMeshMETA",
    "SpaceUserCreateInfoFB",
    "SpaceUserFB",
    "SpaceUserFB_T",
    "SpaceUserIdFB",
    "SpaceUuidFilterInfoFB",
    "SpaceVelocities",
    "SpaceVelocitiesKHR",
    "SpaceVelocity",
    "SpaceVelocityData",
    "SpaceVelocityDataKHR",
    "SpaceVelocityFlagsCInt",
    "Space_T",
    "SpacesEraseInfoMETA",
    "SpacesLocateInfo",
    "SpacesLocateInfoKHR",
    "SpacesSaveInfoMETA",
    "SpatialAnchorCompletionResultML",
    "SpatialAnchorCreateCompletionBD",
    "SpatialAnchorCreateInfoBD",
    "SpatialAnchorCreateInfoEXT",
    "SpatialAnchorCreateInfoFB",
    "SpatialAnchorCreateInfoHTC",
    "SpatialAnchorCreateInfoMSFT",
    "SpatialAnchorFromPersistedAnchorCreateInfoMSFT",
    "SpatialAnchorMSFT",
    "SpatialAnchorMSFT_T",
    "SpatialAnchorNameHTC",
    "SpatialAnchorPersistInfoBD",
    "SpatialAnchorPersistenceInfoMSFT",
    "SpatialAnchorPersistenceNameMSFT",
    "SpatialAnchorShareInfoBD",
    "SpatialAnchorSpaceCreateInfoMSFT",
    "SpatialAnchorStateML",
    "SpatialAnchorStoreConnectionMSFT",
    "SpatialAnchorStoreConnectionMSFT_T",
    "SpatialAnchorUnpersistInfoBD",
    "SpatialAnchorsCreateInfoBaseHeaderML",
    "SpatialAnchorsCreateInfoFromPoseML",
    "SpatialAnchorsCreateInfoFromUuidsML",
    "SpatialAnchorsCreateStorageInfoML",
    "SpatialAnchorsDeleteCompletionDetailsML",
    "SpatialAnchorsDeleteCompletionML",
    "SpatialAnchorsDeleteInfoML",
    "SpatialAnchorsPublishCompletionDetailsML",
    "SpatialAnchorsPublishCompletionML",
    "SpatialAnchorsPublishInfoML",
    "SpatialAnchorsQueryCompletionML",
    "SpatialAnchorsQueryInfoBaseHeaderML",
    "SpatialAnchorsQueryInfoRadiusML",
    "SpatialAnchorsStorageML",
    "SpatialAnchorsStorageML_T",
    "SpatialAnchorsUpdateExpirationCompletionDetailsML",
    "SpatialAnchorsUpdateExpirationCompletionML",
    "SpatialAnchorsUpdateExpirationInfoML",
    "SpatialBounded2DDataEXT",
    "SpatialBufferEXT",
    "SpatialBufferGetInfoEXT",
    "SpatialBufferIdEXT",
    "SpatialCapabilityComponentTypesEXT",
    "SpatialCapabilityConfigurationAnchorEXT",
    "SpatialCapabilityConfigurationAprilTagEXT",
    "SpatialCapabilityConfigurationArucoMarkerEXT",
    "SpatialCapabilityConfigurationBaseHeaderEXT",
    "SpatialCapabilityConfigurationMicroQrCodeEXT",
    "SpatialCapabilityConfigurationPlaneTrackingEXT",
    "SpatialCapabilityConfigurationQrCodeEXT",
    "SpatialComponentAnchorListEXT",
    "SpatialComponentBounded2DListEXT",
    "SpatialComponentBounded3DListEXT",
    "SpatialComponentDataQueryConditionEXT",
    "SpatialComponentDataQueryResultEXT",
    "SpatialComponentMarkerListEXT",
    "SpatialComponentMesh2DListEXT",
    "SpatialComponentMesh3DListEXT",
    "SpatialComponentParentListEXT",
    "SpatialComponentPersistenceListEXT",
    "SpatialComponentPlaneAlignmentListEXT",
    "SpatialComponentPlaneSemanticLabelListEXT",
    "SpatialComponentPolygon2DListEXT",
    "SpatialContextCreateInfoEXT",
    "SpatialContextEXT",
    "SpatialContextEXT_T",
    "SpatialContextPersistenceConfigEXT",
    "SpatialDiscoveryPersistenceUuidFilterEXT",
    "SpatialDiscoverySnapshotCreateInfoEXT",
    "SpatialEntityAnchorCreateInfoBD",
    "SpatialEntityComponentDataBaseHeaderBD",
    "SpatialEntityComponentDataBoundingBox2DBD",
    "SpatialEntityComponentDataBoundingBox3DBD",
    "SpatialEntityComponentDataLocationBD",
    "SpatialEntityComponentDataPlaneOrientationBD",
    "SpatialEntityComponentDataPolygonBD",
    "SpatialEntityComponentDataSemanticBD",
    "SpatialEntityComponentDataTriangleMeshBD",
    "SpatialEntityComponentGetInfoBD",
    "SpatialEntityEXT",
    "SpatialEntityEXT_T",
    "SpatialEntityFromIdCreateInfoEXT",
    "SpatialEntityIdBD",
    "SpatialEntityIdEXT",
    "SpatialEntityLocationGetInfoBD",
    "SpatialEntityPersistInfoEXT",
    "SpatialEntityStateBD",
    "SpatialEntityUnpersistInfoEXT",
    "SpatialFilterTrackingStateEXT",
    "SpatialGraphNodeBindingMSFT",
    "SpatialGraphNodeBindingMSFT_T",
    "SpatialGraphNodeBindingPropertiesGetInfoMSFT",
    "SpatialGraphNodeBindingPropertiesMSFT",
    "SpatialGraphNodeSpaceCreateInfoMSFT",
    "SpatialGraphStaticNodeBindingCreateInfoMSFT",
    "SpatialMarkerDataEXT",
    "SpatialMarkerSizeEXT",
    "SpatialMarkerStaticOptimizationEXT",
    "SpatialMeshConfigFlagsBDCInt",
    "SpatialMeshDataEXT",
    "SpatialPersistenceContextCreateInfoEXT",
    "SpatialPersistenceContextEXT",
    "SpatialPersistenceContextEXT_T",
    "SpatialPersistenceDataEXT",
    "SpatialPolygon2DDataEXT",
    "SpatialSnapshotEXT",
    "SpatialSnapshotEXT_T",
    "SpatialUpdateSnapshotCreateInfoEXT",
    "Spheref",
    "SpherefKHR",
    "Swapchain",
    "SwapchainCreateFlagsCInt",
    "SwapchainCreateFoveationFlagsFBCInt",
    "SwapchainCreateInfo",
    "SwapchainCreateInfoFoveationFB",
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
    "SystemAnchorPropertiesHTC",
    "SystemBodyTrackingPropertiesBD",
    "SystemBodyTrackingPropertiesFB",
    "SystemBodyTrackingPropertiesHTC",
    "SystemColocationDiscoveryPropertiesMETA",
    "SystemColorSpacePropertiesFB",
    "SystemDeviceAnchorPersistencePropertiesANDROID",
    "SystemEnvironmentDepthPropertiesMETA",
    "SystemEyeGazeInteractionPropertiesEXT",
    "SystemEyeTrackingPropertiesFB",
    "SystemFaceTrackingProperties2FB",
    "SystemFaceTrackingPropertiesFB",
    "SystemFacialExpressionPropertiesML",
    "SystemFacialTrackingPropertiesHTC",
    "SystemForceFeedbackCurlPropertiesMNDX",
    "SystemFoveatedRenderingPropertiesVARJO",
    "SystemFoveationEyeTrackedPropertiesMETA",
    "SystemGetInfo",
    "SystemGraphicsProperties",
    "SystemHandTrackingMeshPropertiesMSFT",
    "SystemHandTrackingPropertiesEXT",
    "SystemHeadsetIdPropertiesMETA",
    "SystemId",
    "SystemKeyboardTrackingPropertiesFB",
    "SystemMarkerTrackingPropertiesANDROID",
    "SystemMarkerTrackingPropertiesVARJO",
    "SystemMarkerUnderstandingPropertiesML",
    "SystemNotificationsSetInfoML",
    "SystemPassthroughCameraStatePropertiesANDROID",
    "SystemPassthroughColorLutPropertiesMETA",
    "SystemPassthroughProperties2FB",
    "SystemPassthroughPropertiesFB",
    "SystemPlaneDetectionPropertiesEXT",
    "SystemProperties",
    "SystemPropertiesBodyTrackingCalibrationMETA",
    "SystemPropertiesBodyTrackingFullBodyMETA",
    "SystemRenderModelPropertiesFB",
    "SystemSimultaneousHandsAndControllersPropertiesMETA",
    "SystemSpacePersistencePropertiesMETA",
    "SystemSpaceWarpPropertiesFB",
    "SystemSpatialAnchorPropertiesBD",
    "SystemSpatialAnchorSharingPropertiesBD",
    "SystemSpatialEntityGroupSharingPropertiesMETA",
    "SystemSpatialEntityPropertiesFB",
    "SystemSpatialEntitySharingPropertiesMETA",
    "SystemSpatialMeshPropertiesBD",
    "SystemSpatialPlanePropertiesBD",
    "SystemSpatialScenePropertiesBD",
    "SystemSpatialSensingPropertiesBD",
    "SystemTrackablesPropertiesANDROID",
    "SystemTrackingProperties",
    "SystemUserPresencePropertiesEXT",
    "SystemVirtualKeyboardPropertiesMETA",
    "Time",
    "TrackableANDROID",
    "TrackableGetInfoANDROID",
    "TrackableMarkerANDROID",
    "TrackableMarkerConfigurationANDROID",
    "TrackableMarkerDatabaseANDROID",
    "TrackableMarkerDatabaseEntryANDROID",
    "TrackableObjectANDROID",
    "TrackableObjectConfigurationANDROID",
    "TrackablePlaneANDROID",
    "TrackableTrackerANDROID",
    "TrackableTrackerANDROID_T",
    "TrackableTrackerCreateInfoANDROID",
    "TriangleMeshCreateInfoFB",
    "TriangleMeshFB",
    "TriangleMeshFB_T",
    "TriangleMeshFlagsFBCInt",
    "UnpersistSpatialEntityCompletionEXT",
    "UserCalibrationEnableEventsInfoML",
    "Uuid",
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
    "VirtualKeyboardAnimationStateMETA",
    "VirtualKeyboardCreateInfoMETA",
    "VirtualKeyboardInputInfoMETA",
    "VirtualKeyboardInputStateFlagsMETACInt",
    "VirtualKeyboardLocationInfoMETA",
    "VirtualKeyboardMETA",
    "VirtualKeyboardMETA_T",
    "VirtualKeyboardModelAnimationStatesMETA",
    "VirtualKeyboardModelVisibilitySetInfoMETA",
    "VirtualKeyboardSpaceCreateInfoMETA",
    "VirtualKeyboardTextContextChangeInfoMETA",
    "VirtualKeyboardTextureDataMETA",
    "VisibilityMaskKHR",
    "VisualMeshComputeLodInfoMSFT",
    "ViveTrackerPathsHTCX",
    "WorldMeshBlockML",
    "WorldMeshBlockRequestML",
    "WorldMeshBlockStateML",
    "WorldMeshBufferML",
    "WorldMeshBufferRecommendedSizeInfoML",
    "WorldMeshBufferSizeML",
    "WorldMeshDetectorCreateInfoML",
    "WorldMeshDetectorFlagsMLCInt",
    "WorldMeshDetectorML",
    "WorldMeshDetectorML_T",
    "WorldMeshGetInfoML",
    "WorldMeshRequestCompletionInfoML",
    "WorldMeshRequestCompletionML",
    "WorldMeshStateRequestCompletionML",
    "WorldMeshStateRequestInfoML",
]
