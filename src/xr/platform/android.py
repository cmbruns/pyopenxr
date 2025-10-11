# Warning: this file is auto-generated. Do not edit.

from ctypes import (
    CFUNCTYPE, POINTER, Structure, c_char_p, c_float, c_int, c_uint32, c_void_p,
    cast,
)
import ctypes
from typing import Optional

from ..array_field import *
from ..enums import *
from ..typedefs import *
from ..version import *


# Forward declaration of an Android structure
class AIBinder(Structure):
    pass
    

VkInstance = POINTER(Structure)
VkDevice = POINTER(Structure)
VkImage = POINTER(Structure)
VkPhysicalDevice = POINTER(Structure)
PFN_vkVoidFunction = CFUNCTYPE(None)
PFN_vkGetInstanceProcAddr = CFUNCTYPE(PFN_vkVoidFunction, VkInstance, c_char_p)


class VkInstanceCreateInfo(Structure): 
    pass

        
class VkAllocationCallbacks(Structure): 
    pass
    

class VkDeviceCreateInfo(Structure): 
    pass

KHR_android_thread_settings = 1
KHR_android_thread_settings_SPEC_VERSION = 6
KHR_ANDROID_THREAD_SETTINGS_EXTENSION_NAME = "XR_KHR_android_thread_settings"
KHR_android_surface_swapchain = 1
KHR_android_surface_swapchain_SPEC_VERSION = 4
KHR_ANDROID_SURFACE_SWAPCHAIN_EXTENSION_NAME = "XR_KHR_android_surface_swapchain"
KHR_android_create_instance = 1
KHR_android_create_instance_SPEC_VERSION = 3
KHR_ANDROID_CREATE_INSTANCE_EXTENSION_NAME = "XR_KHR_android_create_instance"
KHR_vulkan_swapchain_format_list = 1
KHR_vulkan_swapchain_format_list_SPEC_VERSION = 5
KHR_VULKAN_SWAPCHAIN_FORMAT_LIST_EXTENSION_NAME = "XR_KHR_vulkan_swapchain_format_list"
KHR_opengl_es_enable = 1
KHR_opengl_es_enable_SPEC_VERSION = 9
KHR_OPENGL_ES_ENABLE_EXTENSION_NAME = "XR_KHR_opengl_es_enable"
KHR_vulkan_enable = 1
KHR_vulkan_enable_SPEC_VERSION = 9
KHR_VULKAN_ENABLE_EXTENSION_NAME = "XR_KHR_vulkan_enable"
KHR_convert_timespec_time = 1
KHR_convert_timespec_time_SPEC_VERSION = 1
KHR_CONVERT_TIMESPEC_TIME_EXTENSION_NAME = "XR_KHR_convert_timespec_time"
KHR_loader_init_android = 1
KHR_loader_init_android_SPEC_VERSION = 1
KHR_LOADER_INIT_ANDROID_EXTENSION_NAME = "XR_KHR_loader_init_android"
KHR_vulkan_enable2 = 1
KHR_vulkan_enable2_SPEC_VERSION = 3
KHR_VULKAN_ENABLE2_EXTENSION_NAME = "XR_KHR_vulkan_enable2"
MNDX_egl_enable = 1
MNDX_egl_enable_SPEC_VERSION = 2
MNDX_EGL_ENABLE_EXTENSION_NAME = "XR_MNDX_egl_enable"
FB_android_surface_swapchain_create = 1
FB_android_surface_swapchain_create_SPEC_VERSION = 1
FB_ANDROID_SURFACE_SWAPCHAIN_CREATE_EXTENSION_NAME = "XR_FB_android_surface_swapchain_create"
FB_foveation_vulkan = 1
FB_foveation_vulkan_SPEC_VERSION = 1
FB_FOVEATION_VULKAN_EXTENSION_NAME = "XR_FB_foveation_vulkan"
FB_swapchain_update_state_android_surface = 1
FB_swapchain_update_state_android_surface_SPEC_VERSION = 1
FB_SWAPCHAIN_UPDATE_STATE_ANDROID_SURFACE_EXTENSION_NAME = "XR_FB_swapchain_update_state_android_surface"
FB_swapchain_update_state_opengl_es = 1
FB_swapchain_update_state_opengl_es_SPEC_VERSION = 1
FB_SWAPCHAIN_UPDATE_STATE_OPENGL_ES_EXTENSION_NAME = "XR_FB_swapchain_update_state_opengl_es"
FB_swapchain_update_state_vulkan = 1
FB_swapchain_update_state_vulkan_SPEC_VERSION = 1
FB_SWAPCHAIN_UPDATE_STATE_VULKAN_EXTENSION_NAME = "XR_FB_swapchain_update_state_vulkan"
META_vulkan_swapchain_create_info = 1
META_vulkan_swapchain_create_info_SPEC_VERSION = 1
META_VULKAN_SWAPCHAIN_CREATE_INFO_EXTENSION_NAME = "XR_META_vulkan_swapchain_create_info"
ANDROID_anchor_sharing_export = 1
ANDROID_anchor_sharing_export_SPEC_VERSION = 1
ANDROID_ANCHOR_SHARING_EXPORT_EXTENSION_NAME = "XR_ANDROID_anchor_sharing_export"


class AndroidThreadTypeKHR(EnumBase):
    APPLICATION_MAIN = 1
    APPLICATION_WORKER = 2
    RENDERER_MAIN = 3
    RENDERER_WORKER = 4


PFN_xrSetAndroidApplicationThreadKHR = CFUNCTYPE(Result.ctype(), Session, AndroidThreadTypeKHR.ctype(), c_uint32)

PFN_xrCreateSwapchainAndroidSurfaceKHR = CFUNCTYPE(Result.ctype(), Session, POINTER(SwapchainCreateInfo), POINTER(Swapchain), POINTER(c_int))


class InstanceCreateInfoAndroidKHR(Structure):
    def __init__(
        self,
        application_vm: c_void_p = None,
        application_activity: c_void_p = None,
        next: c_void_p = None,
        type: StructureType = StructureType.INSTANCE_CREATE_INFO_ANDROID_KHR,
    ) -> None:
        super().__init__(
            application_vm=application_vm,
            application_activity=application_activity,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.InstanceCreateInfoAndroidKHR(application_vm={repr(self.application_vm)}, application_activity={repr(self.application_activity)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.InstanceCreateInfoAndroidKHR(application_vm={self.application_vm}, application_activity={self.application_activity}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("application_vm", c_void_p),
        ("application_activity", c_void_p),
    ]


class VulkanSwapchainFormatListCreateInfoKHR(Structure):
    def __init__(
        self,
        view_format_count: Optional[int] = None,
        view_formats: ArrayFieldParamType[c_int] = None,
        next: c_void_p = None,
        type: StructureType = StructureType.VULKAN_SWAPCHAIN_FORMAT_LIST_CREATE_INFO_KHR,
    ) -> None:
        view_format_count, view_formats = array_field_helper(
            c_int, view_format_count, view_formats)
        super().__init__(
            view_format_count=view_format_count,
            _view_formats=view_formats,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.VulkanSwapchainFormatListCreateInfoKHR(view_format_count={repr(self.view_format_count)}, view_formats={repr(self._view_formats)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.VulkanSwapchainFormatListCreateInfoKHR(view_format_count={self.view_format_count}, view_formats={self._view_formats}, next={self.next}, type={self.type})"

    @property
    def view_formats(self):
        if self.view_format_count == 0:
            return (c_int * 0)()
        else:
            return (c_int * self.view_format_count).from_address(
                ctypes.addressof(self._view_formats.contents))

    @view_formats.setter
    def view_formats(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self.view_format_count, self._view_formats = array_field_helper(
            c_int, None, value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_format_count", c_uint32),
        ("_view_formats", POINTER(c_int)),
    ]


class GraphicsBindingOpenGLESAndroidKHR(Structure):
    def __init__(
        self,
        display: c_void_p = None,
        config: c_void_p = None,
        context: c_void_p = None,
        next: c_void_p = None,
        type: StructureType = StructureType.GRAPHICS_BINDING_OPENGL_ES_ANDROID_KHR,
    ) -> None:
        super().__init__(
            display=display,
            config=config,
            context=context,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.GraphicsBindingOpenGLESAndroidKHR(display={repr(self.display)}, config={repr(self.config)}, context={repr(self.context)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.GraphicsBindingOpenGLESAndroidKHR(display={self.display}, config={self.config}, context={self.context}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("display", c_void_p),
        ("config", c_void_p),
        ("context", c_void_p),
    ]


class SwapchainImageOpenGLESKHR(Structure):
    def __init__(
        self,
        image: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SWAPCHAIN_IMAGE_OPENGL_ES_KHR,
    ) -> None:
        super().__init__(
            image=image,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainImageOpenGLESKHR(image={repr(self.image)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageOpenGLESKHR(image={self.image}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("image", c_uint32),
    ]


class GraphicsRequirementsOpenGLESKHR(Structure):
    def __init__(
        self,
        min_api_version_supported: Version = Version(),
        max_api_version_supported: Version = Version(),
        next: c_void_p = None,
        type: StructureType = StructureType.GRAPHICS_REQUIREMENTS_OPENGL_ES_KHR,
    ) -> None:
        super().__init__(
            _min_api_version_supported=min_api_version_supported.number(),
            _max_api_version_supported=max_api_version_supported.number(),
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.GraphicsRequirementsOpenGLESKHR(min_api_version_supported={repr(self._min_api_version_supported)}, max_api_version_supported={repr(self._max_api_version_supported)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.GraphicsRequirementsOpenGLESKHR(min_api_version_supported={self._min_api_version_supported}, max_api_version_supported={self._max_api_version_supported}, next={self.next}, type={self.type})"

    @property
    def min_api_version_supported(self) -> Version:
        return Version(self._min_api_version_supported)
    
    @min_api_version_supported.setter
    def min_api_version_supported(self, value: Version) -> None:
        if hasattr(value, 'number'):
            # noinspection PyAttributeOutsideInit
            self._min_api_version_supported = value.number()
        else:
            # noinspection PyAttributeOutsideInit
            self._min_api_version_supported = value

    @property
    def max_api_version_supported(self) -> Version:
        return Version(self._max_api_version_supported)
    
    @max_api_version_supported.setter
    def max_api_version_supported(self, value: Version) -> None:
        if hasattr(value, 'number'):
            # noinspection PyAttributeOutsideInit
            self._max_api_version_supported = value.number()
        else:
            # noinspection PyAttributeOutsideInit
            self._max_api_version_supported = value

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("_min_api_version_supported", VersionNumber),
        ("_max_api_version_supported", VersionNumber),
    ]


PFN_xrGetOpenGLESGraphicsRequirementsKHR = CFUNCTYPE(Result.ctype(), Instance, SystemId, POINTER(GraphicsRequirementsOpenGLESKHR))


class GraphicsBindingVulkanKHR(Structure):
    def __init__(
        self,
        instance: VkInstance = None,
        physical_device: VkPhysicalDevice = None,
        device: VkDevice = None,
        queue_family_index: int = 0,
        queue_index: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.GRAPHICS_BINDING_VULKAN_KHR,
    ) -> None:
        super().__init__(
            instance=instance,
            physical_device=physical_device,
            device=device,
            queue_family_index=queue_family_index,
            queue_index=queue_index,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.GraphicsBindingVulkanKHR(instance={repr(self.instance)}, physical_device={repr(self.physical_device)}, device={repr(self.device)}, queue_family_index={repr(self.queue_family_index)}, queue_index={repr(self.queue_index)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.GraphicsBindingVulkanKHR(instance={self.instance}, physical_device={self.physical_device}, device={self.device}, queue_family_index={self.queue_family_index}, queue_index={self.queue_index}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("instance", VkInstance),
        ("physical_device", VkPhysicalDevice),
        ("device", VkDevice),
        ("queue_family_index", c_uint32),
        ("queue_index", c_uint32),
    ]


class SwapchainImageVulkanKHR(Structure):
    def __init__(
        self,
        image: VkImage = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SWAPCHAIN_IMAGE_VULKAN_KHR,
    ) -> None:
        super().__init__(
            image=image,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainImageVulkanKHR(image={repr(self.image)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageVulkanKHR(image={self.image}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("image", VkImage),
    ]


class GraphicsRequirementsVulkanKHR(Structure):
    def __init__(
        self,
        min_api_version_supported: Version = Version(),
        max_api_version_supported: Version = Version(),
        next: c_void_p = None,
        type: StructureType = StructureType.GRAPHICS_REQUIREMENTS_VULKAN_KHR,
    ) -> None:
        super().__init__(
            _min_api_version_supported=min_api_version_supported.number(),
            _max_api_version_supported=max_api_version_supported.number(),
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.GraphicsRequirementsVulkanKHR(min_api_version_supported={repr(self._min_api_version_supported)}, max_api_version_supported={repr(self._max_api_version_supported)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.GraphicsRequirementsVulkanKHR(min_api_version_supported={self._min_api_version_supported}, max_api_version_supported={self._max_api_version_supported}, next={self.next}, type={self.type})"

    @property
    def min_api_version_supported(self) -> Version:
        return Version(self._min_api_version_supported)
    
    @min_api_version_supported.setter
    def min_api_version_supported(self, value: Version) -> None:
        if hasattr(value, 'number'):
            # noinspection PyAttributeOutsideInit
            self._min_api_version_supported = value.number()
        else:
            # noinspection PyAttributeOutsideInit
            self._min_api_version_supported = value

    @property
    def max_api_version_supported(self) -> Version:
        return Version(self._max_api_version_supported)
    
    @max_api_version_supported.setter
    def max_api_version_supported(self, value: Version) -> None:
        if hasattr(value, 'number'):
            # noinspection PyAttributeOutsideInit
            self._max_api_version_supported = value.number()
        else:
            # noinspection PyAttributeOutsideInit
            self._max_api_version_supported = value

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("_min_api_version_supported", VersionNumber),
        ("_max_api_version_supported", VersionNumber),
    ]


PFN_xrGetVulkanInstanceExtensionsKHR = CFUNCTYPE(Result.ctype(), Instance, SystemId, c_uint32, POINTER(c_uint32), c_char_p)

PFN_xrGetVulkanDeviceExtensionsKHR = CFUNCTYPE(Result.ctype(), Instance, SystemId, c_uint32, POINTER(c_uint32), c_char_p)

PFN_xrGetVulkanGraphicsDeviceKHR = CFUNCTYPE(Result.ctype(), Instance, SystemId, VkInstance, POINTER(VkPhysicalDevice))

PFN_xrGetVulkanGraphicsRequirementsKHR = CFUNCTYPE(Result.ctype(), Instance, SystemId, POINTER(GraphicsRequirementsVulkanKHR))


class timespec(Structure):
    pass


PFN_xrConvertTimespecTimeToTimeKHR = CFUNCTYPE(Result.ctype(), Instance, POINTER(timespec), POINTER(Time))


class timespec(Structure):
    pass


PFN_xrConvertTimeToTimespecTimeKHR = CFUNCTYPE(Result.ctype(), Instance, Time, POINTER(timespec))


class LoaderInitInfoAndroidKHR(Structure):
    def __init__(
        self,
        application_vm: c_void_p = None,
        application_context: c_void_p = None,
        next: c_void_p = None,
        type: StructureType = StructureType.LOADER_INIT_INFO_ANDROID_KHR,
    ) -> None:
        super().__init__(
            application_vm=application_vm,
            application_context=application_context,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.LoaderInitInfoAndroidKHR(application_vm={repr(self.application_vm)}, application_context={repr(self.application_context)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.LoaderInitInfoAndroidKHR(application_vm={self.application_vm}, application_context={self.application_context}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("application_vm", c_void_p),
        ("application_context", c_void_p),
    ]


VulkanInstanceCreateFlagsKHRCInt = Flags64


class VulkanInstanceCreateFlagsKHR(FlagBase):
    NONE = 0x00000000
    ALL = NONE


VulkanDeviceCreateFlagsKHRCInt = Flags64


class VulkanDeviceCreateFlagsKHR(FlagBase):
    NONE = 0x00000000
    ALL = NONE


class VulkanInstanceCreateInfoKHR(Structure):
    def __init__(
        self,
        system_id: SystemId = 0,
        create_flags: VulkanInstanceCreateFlagsKHR = VulkanInstanceCreateFlagsKHR(),  # noqa
        pfn_get_instance_proc_addr: PFN_vkGetInstanceProcAddr = 0,
        vulkan_create_info: POINTER(VkInstanceCreateInfo) = None,
        vulkan_allocator: POINTER(VkAllocationCallbacks) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.VULKAN_INSTANCE_CREATE_INFO_KHR,
    ) -> None:
        super().__init__(
            system_id=system_id,
            create_flags=VulkanInstanceCreateFlagsKHR(create_flags).value,
            pfn_get_instance_proc_addr=pfn_get_instance_proc_addr,
            vulkan_create_info=vulkan_create_info,
            vulkan_allocator=vulkan_allocator,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.VulkanInstanceCreateInfoKHR(system_id={repr(self.system_id)}, create_flags={repr(self.create_flags)}, pfn_get_instance_proc_addr={repr(self.pfn_get_instance_proc_addr)}, vulkan_create_info={repr(self.vulkan_create_info)}, vulkan_allocator={repr(self.vulkan_allocator)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.VulkanInstanceCreateInfoKHR(system_id={self.system_id}, create_flags={self.create_flags}, pfn_get_instance_proc_addr={self.pfn_get_instance_proc_addr}, vulkan_create_info={self.vulkan_create_info}, vulkan_allocator={self.vulkan_allocator}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("system_id", SystemId),
        ("create_flags", VulkanInstanceCreateFlagsKHRCInt),
        ("pfn_get_instance_proc_addr", PFN_vkGetInstanceProcAddr),
        ("vulkan_create_info", POINTER(VkInstanceCreateInfo)),
        ("vulkan_allocator", POINTER(VkAllocationCallbacks)),
    ]


class VulkanDeviceCreateInfoKHR(Structure):
    def __init__(
        self,
        system_id: SystemId = 0,
        create_flags: VulkanDeviceCreateFlagsKHR = VulkanDeviceCreateFlagsKHR(),  # noqa
        pfn_get_instance_proc_addr: PFN_vkGetInstanceProcAddr = 0,
        vulkan_physical_device: VkPhysicalDevice = None,
        vulkan_create_info: POINTER(VkDeviceCreateInfo) = None,
        vulkan_allocator: POINTER(VkAllocationCallbacks) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.VULKAN_DEVICE_CREATE_INFO_KHR,
    ) -> None:
        super().__init__(
            system_id=system_id,
            create_flags=VulkanDeviceCreateFlagsKHR(create_flags).value,
            pfn_get_instance_proc_addr=pfn_get_instance_proc_addr,
            vulkan_physical_device=vulkan_physical_device,
            vulkan_create_info=vulkan_create_info,
            vulkan_allocator=vulkan_allocator,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.VulkanDeviceCreateInfoKHR(system_id={repr(self.system_id)}, create_flags={repr(self.create_flags)}, pfn_get_instance_proc_addr={repr(self.pfn_get_instance_proc_addr)}, vulkan_physical_device={repr(self.vulkan_physical_device)}, vulkan_create_info={repr(self.vulkan_create_info)}, vulkan_allocator={repr(self.vulkan_allocator)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.VulkanDeviceCreateInfoKHR(system_id={self.system_id}, create_flags={self.create_flags}, pfn_get_instance_proc_addr={self.pfn_get_instance_proc_addr}, vulkan_physical_device={self.vulkan_physical_device}, vulkan_create_info={self.vulkan_create_info}, vulkan_allocator={self.vulkan_allocator}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("system_id", SystemId),
        ("create_flags", VulkanDeviceCreateFlagsKHRCInt),
        ("pfn_get_instance_proc_addr", PFN_vkGetInstanceProcAddr),
        ("vulkan_physical_device", VkPhysicalDevice),
        ("vulkan_create_info", POINTER(VkDeviceCreateInfo)),
        ("vulkan_allocator", POINTER(VkAllocationCallbacks)),
    ]


GraphicsBindingVulkan2KHR = GraphicsBindingVulkanKHR


class VulkanGraphicsDeviceGetInfoKHR(Structure):
    def __init__(
        self,
        system_id: SystemId = 0,
        vulkan_instance: VkInstance = None,
        next: c_void_p = None,
        type: StructureType = StructureType.VULKAN_GRAPHICS_DEVICE_GET_INFO_KHR,
    ) -> None:
        super().__init__(
            system_id=system_id,
            vulkan_instance=vulkan_instance,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.VulkanGraphicsDeviceGetInfoKHR(system_id={repr(self.system_id)}, vulkan_instance={repr(self.vulkan_instance)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.VulkanGraphicsDeviceGetInfoKHR(system_id={self.system_id}, vulkan_instance={self.vulkan_instance}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("system_id", SystemId),
        ("vulkan_instance", VkInstance),
    ]


SwapchainImageVulkan2KHR = SwapchainImageVulkanKHR

GraphicsRequirementsVulkan2KHR = GraphicsRequirementsVulkanKHR

PFN_xrCreateVulkanInstanceKHR = CFUNCTYPE(Result.ctype(), Instance, POINTER(VulkanInstanceCreateInfoKHR), POINTER(VkInstance), POINTER(c_int))

PFN_xrCreateVulkanDeviceKHR = CFUNCTYPE(Result.ctype(), Instance, POINTER(VulkanDeviceCreateInfoKHR), POINTER(VkDevice), POINTER(c_int))

PFN_xrGetVulkanGraphicsDevice2KHR = CFUNCTYPE(Result.ctype(), Instance, POINTER(VulkanGraphicsDeviceGetInfoKHR), POINTER(VkPhysicalDevice))

PFN_xrGetVulkanGraphicsRequirements2KHR = CFUNCTYPE(Result.ctype(), Instance, SystemId, POINTER(GraphicsRequirementsVulkanKHR))

PFN_xrEglGetProcAddressMNDX = CFUNCTYPE(PFN_xrVoidFunction, c_char_p)


class GraphicsBindingEGLMNDX(Structure):
    def __init__(
        self,
        get_proc_address: PFN_xrEglGetProcAddressMNDX = cast(None, PFN_xrEglGetProcAddressMNDX),
        display: c_void_p = None,
        config: c_void_p = None,
        context: c_void_p = None,
        next: c_void_p = None,
        type: StructureType = StructureType.GRAPHICS_BINDING_EGL_MNDX,
    ) -> None:
        super().__init__(
            get_proc_address=get_proc_address,
            display=display,
            config=config,
            context=context,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.GraphicsBindingEGLMNDX(get_proc_address={repr(self.get_proc_address)}, display={repr(self.display)}, config={repr(self.config)}, context={repr(self.context)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.GraphicsBindingEGLMNDX(get_proc_address={self.get_proc_address}, display={self.display}, config={self.config}, context={self.context}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("get_proc_address", PFN_xrEglGetProcAddressMNDX),
        ("display", c_void_p),
        ("config", c_void_p),
        ("context", c_void_p),
    ]


AndroidSurfaceSwapchainFlagsFBCInt = Flags64


class AndroidSurfaceSwapchainFlagsFB(FlagBase):
    NONE = 0x00000000
    SYNCHRONOUS_BIT = 0x00000001
    USE_TIMESTAMPS_BIT = 0x00000002
    ALL = SYNCHRONOUS_BIT | USE_TIMESTAMPS_BIT


ANDROID_SURFACE_SWAPCHAIN_SYNCHRONOUS_BIT_FB = 0x00000001
ANDROID_SURFACE_SWAPCHAIN_USE_TIMESTAMPS_BIT_FB = 0x00000002


class AndroidSurfaceSwapchainCreateInfoFB(Structure):
    def __init__(
        self,
        create_flags: AndroidSurfaceSwapchainFlagsFB = AndroidSurfaceSwapchainFlagsFB(),  # noqa
        next: c_void_p = None,
        type: StructureType = StructureType.ANDROID_SURFACE_SWAPCHAIN_CREATE_INFO_FB,
    ) -> None:
        super().__init__(
            create_flags=AndroidSurfaceSwapchainFlagsFB(create_flags).value,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.AndroidSurfaceSwapchainCreateInfoFB(create_flags={repr(self.create_flags)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.AndroidSurfaceSwapchainCreateInfoFB(create_flags={self.create_flags}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("create_flags", AndroidSurfaceSwapchainFlagsFBCInt),
    ]


class SwapchainImageFoveationVulkanFB(Structure):
    def __init__(
        self,
        image: VkImage = None,
        width: int = 0,
        height: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SWAPCHAIN_IMAGE_FOVEATION_VULKAN_FB,
    ) -> None:
        super().__init__(
            image=image,
            width=width,
            height=height,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainImageFoveationVulkanFB(image={repr(self.image)}, width={repr(self.width)}, height={repr(self.height)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageFoveationVulkanFB(image={self.image}, width={self.width}, height={self.height}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("image", VkImage),
        ("width", c_uint32),
        ("height", c_uint32),
    ]


class SwapchainStateAndroidSurfaceDimensionsFB(Structure):
    def __init__(
        self,
        width: int = 0,
        height: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SWAPCHAIN_STATE_ANDROID_SURFACE_DIMENSIONS_FB,
    ) -> None:
        super().__init__(
            width=width,
            height=height,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainStateAndroidSurfaceDimensionsFB(width={repr(self.width)}, height={repr(self.height)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainStateAndroidSurfaceDimensionsFB(width={self.width}, height={self.height}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("width", c_uint32),
        ("height", c_uint32),
    ]


class SwapchainStateSamplerOpenGLESFB(Structure):
    def __init__(
        self,
        min_filter: int = 0,
        mag_filter: int = 0,
        wrap_mode_s: int = 0,
        wrap_mode_t: int = 0,
        swizzle_red: int = 0,
        swizzle_green: int = 0,
        swizzle_blue: int = 0,
        swizzle_alpha: int = 0,
        max_anisotropy: float = 0,
        border_color: Color4f = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SWAPCHAIN_STATE_SAMPLER_OPENGL_ES_FB,
    ) -> None:
        if border_color is None:
            border_color = Color4f()
        super().__init__(
            min_filter=min_filter,
            mag_filter=mag_filter,
            wrap_mode_s=wrap_mode_s,
            wrap_mode_t=wrap_mode_t,
            swizzle_red=swizzle_red,
            swizzle_green=swizzle_green,
            swizzle_blue=swizzle_blue,
            swizzle_alpha=swizzle_alpha,
            max_anisotropy=max_anisotropy,
            border_color=border_color,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainStateSamplerOpenGLESFB(min_filter={repr(self.min_filter)}, mag_filter={repr(self.mag_filter)}, wrap_mode_s={repr(self.wrap_mode_s)}, wrap_mode_t={repr(self.wrap_mode_t)}, swizzle_red={repr(self.swizzle_red)}, swizzle_green={repr(self.swizzle_green)}, swizzle_blue={repr(self.swizzle_blue)}, swizzle_alpha={repr(self.swizzle_alpha)}, max_anisotropy={repr(self.max_anisotropy)}, border_color={repr(self.border_color)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainStateSamplerOpenGLESFB(min_filter={self.min_filter}, mag_filter={self.mag_filter}, wrap_mode_s={self.wrap_mode_s}, wrap_mode_t={self.wrap_mode_t}, swizzle_red={self.swizzle_red}, swizzle_green={self.swizzle_green}, swizzle_blue={self.swizzle_blue}, swizzle_alpha={self.swizzle_alpha}, max_anisotropy={self.max_anisotropy:.3f}, border_color={self.border_color}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("min_filter", c_int),
        ("mag_filter", c_int),
        ("wrap_mode_s", c_int),
        ("wrap_mode_t", c_int),
        ("swizzle_red", c_int),
        ("swizzle_green", c_int),
        ("swizzle_blue", c_int),
        ("swizzle_alpha", c_int),
        ("max_anisotropy", c_float),
        ("border_color", Color4f),
    ]


class SwapchainStateSamplerVulkanFB(Structure):
    def __init__(
        self,
        min_filter: c_int = 0,
        mag_filter: c_int = 0,
        mipmap_mode: c_int = 0,
        wrap_mode_s: c_int = 0,
        wrap_mode_t: c_int = 0,
        swizzle_red: c_int = 0,
        swizzle_green: c_int = 0,
        swizzle_blue: c_int = 0,
        swizzle_alpha: c_int = 0,
        max_anisotropy: float = 0,
        border_color: Color4f = None,
        next: c_void_p = None,
        type: StructureType = StructureType.SWAPCHAIN_STATE_SAMPLER_VULKAN_FB,
    ) -> None:
        if border_color is None:
            border_color = Color4f()
        super().__init__(
            min_filter=min_filter,
            mag_filter=mag_filter,
            mipmap_mode=mipmap_mode,
            wrap_mode_s=wrap_mode_s,
            wrap_mode_t=wrap_mode_t,
            swizzle_red=swizzle_red,
            swizzle_green=swizzle_green,
            swizzle_blue=swizzle_blue,
            swizzle_alpha=swizzle_alpha,
            max_anisotropy=max_anisotropy,
            border_color=border_color,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainStateSamplerVulkanFB(min_filter={repr(self.min_filter)}, mag_filter={repr(self.mag_filter)}, mipmap_mode={repr(self.mipmap_mode)}, wrap_mode_s={repr(self.wrap_mode_s)}, wrap_mode_t={repr(self.wrap_mode_t)}, swizzle_red={repr(self.swizzle_red)}, swizzle_green={repr(self.swizzle_green)}, swizzle_blue={repr(self.swizzle_blue)}, swizzle_alpha={repr(self.swizzle_alpha)}, max_anisotropy={repr(self.max_anisotropy)}, border_color={repr(self.border_color)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainStateSamplerVulkanFB(min_filter={self.min_filter}, mag_filter={self.mag_filter}, mipmap_mode={self.mipmap_mode}, wrap_mode_s={self.wrap_mode_s}, wrap_mode_t={self.wrap_mode_t}, swizzle_red={self.swizzle_red}, swizzle_green={self.swizzle_green}, swizzle_blue={self.swizzle_blue}, swizzle_alpha={self.swizzle_alpha}, max_anisotropy={self.max_anisotropy:.3f}, border_color={self.border_color}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("min_filter", c_int),
        ("mag_filter", c_int),
        ("mipmap_mode", c_int),
        ("wrap_mode_s", c_int),
        ("wrap_mode_t", c_int),
        ("swizzle_red", c_int),
        ("swizzle_green", c_int),
        ("swizzle_blue", c_int),
        ("swizzle_alpha", c_int),
        ("max_anisotropy", c_float),
        ("border_color", Color4f),
    ]


class VulkanSwapchainCreateInfoMETA(Structure):
    def __init__(
        self,
        additional_create_flags: int = 0,
        additional_usage_flags: int = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.VULKAN_SWAPCHAIN_CREATE_INFO_META,
    ) -> None:
        super().__init__(
            additional_create_flags=additional_create_flags,
            additional_usage_flags=additional_usage_flags,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.VulkanSwapchainCreateInfoMETA(additional_create_flags={repr(self.additional_create_flags)}, additional_usage_flags={repr(self.additional_usage_flags)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.VulkanSwapchainCreateInfoMETA(additional_create_flags={self.additional_create_flags}, additional_usage_flags={self.additional_usage_flags}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("additional_create_flags", c_uint32),
        ("additional_usage_flags", c_uint32),
    ]


class AnchorSharingInfoANDROID(Structure):
    def __init__(
        self,
        anchor: Space = None,
        next: c_void_p = None,
        type: StructureType = StructureType.ANCHOR_SHARING_INFO_ANDROID,
    ) -> None:
        super().__init__(
            anchor=anchor,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.AnchorSharingInfoANDROID(anchor={repr(self.anchor)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.AnchorSharingInfoANDROID(anchor={self.anchor}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("anchor", Space),
    ]


class AnchorSharingTokenANDROID(Structure):
    def __init__(
        self,
        token: POINTER(AIBinder) = None,
        next: c_void_p = None,
        type: StructureType = StructureType.ANCHOR_SHARING_TOKEN_ANDROID,
    ) -> None:
        super().__init__(
            token=token,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.AnchorSharingTokenANDROID(token={repr(self.token)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.AnchorSharingTokenANDROID(token={self.token}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("token", POINTER(AIBinder)),
    ]


class SystemAnchorSharingExportPropertiesANDROID(Structure):
    def __init__(
        self,
        supports_anchor_sharing_export: Bool32 = 0,
        next: c_void_p = None,
        type: StructureType = StructureType.SYSTEM_ANCHOR_SHARING_EXPORT_PROPERTIES_ANDROID,
    ) -> None:
        super().__init__(
            supports_anchor_sharing_export=supports_anchor_sharing_export,
            next=next,
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemAnchorSharingExportPropertiesANDROID(supports_anchor_sharing_export={repr(self.supports_anchor_sharing_export)}, next={repr(self.next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemAnchorSharingExportPropertiesANDROID(supports_anchor_sharing_export={self.supports_anchor_sharing_export}, next={self.next}, type={self.type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("supports_anchor_sharing_export", Bool32),
    ]


PFN_xrShareAnchorANDROID = CFUNCTYPE(Result.ctype(), Session, POINTER(AnchorSharingInfoANDROID), POINTER(AnchorSharingTokenANDROID))

PFN_xrUnshareAnchorANDROID = CFUNCTYPE(Result.ctype(), Session, Space)


__all__ = [
    "ANDROID_ANCHOR_SHARING_EXPORT_EXTENSION_NAME",
    "ANDROID_SURFACE_SWAPCHAIN_SYNCHRONOUS_BIT_FB",
    "ANDROID_SURFACE_SWAPCHAIN_USE_TIMESTAMPS_BIT_FB",
    "ANDROID_anchor_sharing_export",
    "ANDROID_anchor_sharing_export_SPEC_VERSION",
    "AnchorSharingInfoANDROID",
    "AnchorSharingTokenANDROID",
    "AndroidSurfaceSwapchainCreateInfoFB",
    "AndroidSurfaceSwapchainFlagsFB",
    "AndroidSurfaceSwapchainFlagsFBCInt",
    "AndroidThreadTypeKHR",
    "FB_ANDROID_SURFACE_SWAPCHAIN_CREATE_EXTENSION_NAME",
    "FB_FOVEATION_VULKAN_EXTENSION_NAME",
    "FB_SWAPCHAIN_UPDATE_STATE_ANDROID_SURFACE_EXTENSION_NAME",
    "FB_SWAPCHAIN_UPDATE_STATE_OPENGL_ES_EXTENSION_NAME",
    "FB_SWAPCHAIN_UPDATE_STATE_VULKAN_EXTENSION_NAME",
    "FB_android_surface_swapchain_create",
    "FB_android_surface_swapchain_create_SPEC_VERSION",
    "FB_foveation_vulkan",
    "FB_foveation_vulkan_SPEC_VERSION",
    "FB_swapchain_update_state_android_surface",
    "FB_swapchain_update_state_android_surface_SPEC_VERSION",
    "FB_swapchain_update_state_opengl_es",
    "FB_swapchain_update_state_opengl_es_SPEC_VERSION",
    "FB_swapchain_update_state_vulkan",
    "FB_swapchain_update_state_vulkan_SPEC_VERSION",
    "GraphicsBindingEGLMNDX",
    "GraphicsBindingOpenGLESAndroidKHR",
    "GraphicsBindingVulkan2KHR",
    "GraphicsBindingVulkanKHR",
    "GraphicsRequirementsOpenGLESKHR",
    "GraphicsRequirementsVulkan2KHR",
    "GraphicsRequirementsVulkanKHR",
    "InstanceCreateInfoAndroidKHR",
    "KHR_ANDROID_CREATE_INSTANCE_EXTENSION_NAME",
    "KHR_ANDROID_SURFACE_SWAPCHAIN_EXTENSION_NAME",
    "KHR_ANDROID_THREAD_SETTINGS_EXTENSION_NAME",
    "KHR_CONVERT_TIMESPEC_TIME_EXTENSION_NAME",
    "KHR_LOADER_INIT_ANDROID_EXTENSION_NAME",
    "KHR_OPENGL_ES_ENABLE_EXTENSION_NAME",
    "KHR_VULKAN_ENABLE2_EXTENSION_NAME",
    "KHR_VULKAN_ENABLE_EXTENSION_NAME",
    "KHR_VULKAN_SWAPCHAIN_FORMAT_LIST_EXTENSION_NAME",
    "KHR_android_create_instance",
    "KHR_android_create_instance_SPEC_VERSION",
    "KHR_android_surface_swapchain",
    "KHR_android_surface_swapchain_SPEC_VERSION",
    "KHR_android_thread_settings",
    "KHR_android_thread_settings_SPEC_VERSION",
    "KHR_convert_timespec_time",
    "KHR_convert_timespec_time_SPEC_VERSION",
    "KHR_loader_init_android",
    "KHR_loader_init_android_SPEC_VERSION",
    "KHR_opengl_es_enable",
    "KHR_opengl_es_enable_SPEC_VERSION",
    "KHR_vulkan_enable",
    "KHR_vulkan_enable2",
    "KHR_vulkan_enable2_SPEC_VERSION",
    "KHR_vulkan_enable_SPEC_VERSION",
    "KHR_vulkan_swapchain_format_list",
    "KHR_vulkan_swapchain_format_list_SPEC_VERSION",
    "LoaderInitInfoAndroidKHR",
    "META_VULKAN_SWAPCHAIN_CREATE_INFO_EXTENSION_NAME",
    "META_vulkan_swapchain_create_info",
    "META_vulkan_swapchain_create_info_SPEC_VERSION",
    "MNDX_EGL_ENABLE_EXTENSION_NAME",
    "MNDX_egl_enable",
    "MNDX_egl_enable_SPEC_VERSION",
    "PFN_xrConvertTimeToTimespecTimeKHR",
    "PFN_xrConvertTimespecTimeToTimeKHR",
    "PFN_xrCreateSwapchainAndroidSurfaceKHR",
    "PFN_xrCreateVulkanDeviceKHR",
    "PFN_xrCreateVulkanInstanceKHR",
    "PFN_xrEglGetProcAddressMNDX",
    "PFN_xrGetOpenGLESGraphicsRequirementsKHR",
    "PFN_xrGetVulkanDeviceExtensionsKHR",
    "PFN_xrGetVulkanGraphicsDevice2KHR",
    "PFN_xrGetVulkanGraphicsDeviceKHR",
    "PFN_xrGetVulkanGraphicsRequirements2KHR",
    "PFN_xrGetVulkanGraphicsRequirementsKHR",
    "PFN_xrGetVulkanInstanceExtensionsKHR",
    "PFN_xrSetAndroidApplicationThreadKHR",
    "PFN_xrShareAnchorANDROID",
    "PFN_xrUnshareAnchorANDROID",
    "SwapchainImageFoveationVulkanFB",
    "SwapchainImageOpenGLESKHR",
    "SwapchainImageVulkan2KHR",
    "SwapchainImageVulkanKHR",
    "SwapchainStateAndroidSurfaceDimensionsFB",
    "SwapchainStateSamplerOpenGLESFB",
    "SwapchainStateSamplerVulkanFB",
    "SystemAnchorSharingExportPropertiesANDROID",
    "VulkanDeviceCreateFlagsKHR",
    "VulkanDeviceCreateFlagsKHRCInt",
    "VulkanDeviceCreateInfoKHR",
    "VulkanGraphicsDeviceGetInfoKHR",
    "VulkanInstanceCreateFlagsKHR",
    "VulkanInstanceCreateFlagsKHRCInt",
    "VulkanInstanceCreateInfoKHR",
    "VulkanSwapchainCreateInfoMETA",
    "VulkanSwapchainFormatListCreateInfoKHR",
    "timespec",
]
