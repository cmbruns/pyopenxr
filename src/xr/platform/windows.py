# Warning: this file is auto-generated. Do not edit.

from ctypes import CFUNCTYPE, POINTER, Structure, c_char_p, c_float, c_int, c_long, c_longlong, c_uint32, c_ulong, c_void_p, c_wchar, wintypes
import ctypes

from OpenGL import WGL

from ..enums import *
from ..typedefs import *
from ..version import *


class _LUID(ctypes.Structure):
    _fields_ = [
        ("low_part", c_ulong),
        ("high_part", c_long),
    ]


_LARGE_INTEGER = c_longlong

KHR_vulkan_swapchain_format_list = 1
KHR_vulkan_swapchain_format_list_SPEC_VERSION = 4
KHR_VULKAN_SWAPCHAIN_FORMAT_LIST_EXTENSION_NAME = "XR_KHR_vulkan_swapchain_format_list"
KHR_opengl_enable = 1
KHR_opengl_enable_SPEC_VERSION = 10
KHR_OPENGL_ENABLE_EXTENSION_NAME = "XR_KHR_opengl_enable"
KHR_vulkan_enable = 1
KHR_vulkan_enable_SPEC_VERSION = 8
KHR_VULKAN_ENABLE_EXTENSION_NAME = "XR_KHR_vulkan_enable"
KHR_D3D11_enable = 1
KHR_D3D11_enable_SPEC_VERSION = 8
KHR_D3D11_ENABLE_EXTENSION_NAME = "XR_KHR_D3D11_enable"
KHR_D3D12_enable = 1
KHR_D3D12_enable_SPEC_VERSION = 8
KHR_D3D12_ENABLE_EXTENSION_NAME = "XR_KHR_D3D12_enable"
KHR_win32_convert_performance_counter_time = 1
KHR_win32_convert_performance_counter_time_SPEC_VERSION = 1
KHR_WIN32_CONVERT_PERFORMANCE_COUNTER_TIME_EXTENSION_NAME = "XR_KHR_win32_convert_performance_counter_time"
KHR_convert_timespec_time = 1
KHR_convert_timespec_time_SPEC_VERSION = 1
KHR_CONVERT_TIMESPEC_TIME_EXTENSION_NAME = "XR_KHR_convert_timespec_time"
KHR_vulkan_enable2 = 1
KHR_vulkan_enable2_SPEC_VERSION = 2
KHR_VULKAN_ENABLE2_EXTENSION_NAME = "XR_KHR_vulkan_enable2"
MSFT_perception_anchor_interop = 1
MSFT_perception_anchor_interop_SPEC_VERSION = 1
MSFT_PERCEPTION_ANCHOR_INTEROP_EXTENSION_NAME = "XR_MSFT_perception_anchor_interop"
MSFT_holographic_window_attachment = 1
MSFT_holographic_window_attachment_SPEC_VERSION = 1
MSFT_HOLOGRAPHIC_WINDOW_ATTACHMENT_EXTENSION_NAME = "XR_MSFT_holographic_window_attachment"
OCULUS_audio_device_guid = 1
OCULUS_audio_device_guid_SPEC_VERSION = 1
OCULUS_AUDIO_DEVICE_GUID_EXTENSION_NAME = "XR_OCULUS_audio_device_guid"
MAX_AUDIO_DEVICE_STR_SIZE_OCULUS = 128
FB_foveation_vulkan = 1
FB_foveation_vulkan_SPEC_VERSION = 1
FB_FOVEATION_VULKAN_EXTENSION_NAME = "XR_FB_foveation_vulkan"
FB_swapchain_update_state_vulkan = 1
FB_swapchain_update_state_vulkan_SPEC_VERSION = 1
FB_SWAPCHAIN_UPDATE_STATE_VULKAN_EXTENSION_NAME = "XR_FB_swapchain_update_state_vulkan"


class VulkanSwapchainFormatListCreateInfoKHR(Structure):
    def __init__(
        self,
        view_format_count: int = 0,
        view_formats: POINTER(c_int) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.VULKAN_SWAPCHAIN_FORMAT_LIST_CREATE_INFO_KHR,
    ) -> None:
        super().__init__(
            view_format_count=view_format_count,
            view_formats=view_formats,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.VulkanSwapchainFormatListCreateInfoKHR(view_format_count={repr(self.view_format_count)}, view_formats={repr(self.view_formats)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.VulkanSwapchainFormatListCreateInfoKHR(view_format_count={self.view_format_count}, view_formats={self.view_formats}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_format_count", c_uint32),
        ("view_formats", POINTER(c_int)),
    ]


class GraphicsBindingOpenGLWin32KHR(Structure):
    def __init__(
        self,
        h_dc: wintypes.HDC = 0,
        h_glrc: WGL.HGLRC = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.GRAPHICS_BINDING_OPENGL_WIN32_KHR,
    ) -> None:
        super().__init__(
            h_dc=h_dc,
            h_glrc=h_glrc,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.GraphicsBindingOpenGLWin32KHR(h_dc={repr(self.h_dc)}, h_glrc={repr(self.h_glrc)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.GraphicsBindingOpenGLWin32KHR(h_dc={self.h_dc}, h_glrc={self.h_glrc}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("h_dc", wintypes.HDC),
        ("h_glrc", WGL.HGLRC),
    ]


class SwapchainImageOpenGLKHR(Structure):
    def __init__(
        self,
        image: int = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SWAPCHAIN_IMAGE_OPENGL_KHR,
    ) -> None:
        super().__init__(
            image=image,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainImageOpenGLKHR(image={repr(self.image)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageOpenGLKHR(image={self.image}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("image", c_uint32),
    ]


class GraphicsRequirementsOpenGLKHR(Structure):
    def __init__(
        self,
        min_api_version_supported: Version = Version(),
        max_api_version_supported: Version = Version(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.GRAPHICS_REQUIREMENTS_OPENGL_KHR,
    ) -> None:
        super().__init__(
            min_api_version_supported=min_api_version_supported.number(),
            max_api_version_supported=max_api_version_supported.number(),
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.GraphicsRequirementsOpenGLKHR(min_api_version_supported={repr(self.min_api_version_supported)}, max_api_version_supported={repr(self.max_api_version_supported)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.GraphicsRequirementsOpenGLKHR(min_api_version_supported={self.min_api_version_supported}, max_api_version_supported={self.max_api_version_supported}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("min_api_version_supported", VersionNumber),
        ("max_api_version_supported", VersionNumber),
    ]


PFN_xrGetOpenGLGraphicsRequirementsKHR = CFUNCTYPE(Result.ctype(), InstanceHandle, SystemId, POINTER(GraphicsRequirementsOpenGLKHR))


class GraphicsBindingVulkanKHR(Structure):
    def __init__(
        self,
        instance: int = 0,
        physical_device: int = 0,
        device: int = 0,
        queue_family_index: int = 0,
        queue_index: int = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.GRAPHICS_BINDING_VULKAN_KHR,
    ) -> None:
        super().__init__(
            instance=instance,
            physical_device=physical_device,
            device=device,
            queue_family_index=queue_family_index,
            queue_index=queue_index,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.GraphicsBindingVulkanKHR(instance={repr(self.instance)}, physical_device={repr(self.physical_device)}, device={repr(self.device)}, queue_family_index={repr(self.queue_family_index)}, queue_index={repr(self.queue_index)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.GraphicsBindingVulkanKHR(instance={self.instance}, physical_device={self.physical_device}, device={self.device}, queue_family_index={self.queue_family_index}, queue_index={self.queue_index}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("instance", c_int),
        ("physical_device", c_int),
        ("device", c_int),
        ("queue_family_index", c_uint32),
        ("queue_index", c_uint32),
    ]


class SwapchainImageVulkanKHR(Structure):
    def __init__(
        self,
        image: int = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SWAPCHAIN_IMAGE_VULKAN_KHR,
    ) -> None:
        super().__init__(
            image=image,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainImageVulkanKHR(image={repr(self.image)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageVulkanKHR(image={self.image}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("image", c_int),
    ]


class GraphicsRequirementsVulkanKHR(Structure):
    def __init__(
        self,
        min_api_version_supported: Version = Version(),
        max_api_version_supported: Version = Version(),
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.GRAPHICS_REQUIREMENTS_VULKAN_KHR,
    ) -> None:
        super().__init__(
            min_api_version_supported=min_api_version_supported.number(),
            max_api_version_supported=max_api_version_supported.number(),
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.GraphicsRequirementsVulkanKHR(min_api_version_supported={repr(self.min_api_version_supported)}, max_api_version_supported={repr(self.max_api_version_supported)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.GraphicsRequirementsVulkanKHR(min_api_version_supported={self.min_api_version_supported}, max_api_version_supported={self.max_api_version_supported}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("min_api_version_supported", VersionNumber),
        ("max_api_version_supported", VersionNumber),
    ]


PFN_xrGetVulkanInstanceExtensionsKHR = CFUNCTYPE(Result.ctype(), InstanceHandle, SystemId, c_uint32, POINTER(c_uint32), c_char_p)

PFN_xrGetVulkanDeviceExtensionsKHR = CFUNCTYPE(Result.ctype(), InstanceHandle, SystemId, c_uint32, POINTER(c_uint32), c_char_p)

PFN_xrGetVulkanGraphicsDeviceKHR = CFUNCTYPE(Result.ctype(), InstanceHandle, SystemId, c_int, POINTER(c_int))

PFN_xrGetVulkanGraphicsRequirementsKHR = CFUNCTYPE(Result.ctype(), InstanceHandle, SystemId, POINTER(GraphicsRequirementsVulkanKHR))


class GraphicsBindingD3D11KHR(Structure):
    def __init__(
        self,
        device: POINTER(c_int) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.GRAPHICS_BINDING_D3D11_KHR,
    ) -> None:
        super().__init__(
            device=device,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.GraphicsBindingD3D11KHR(device={repr(self.device)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.GraphicsBindingD3D11KHR(device={self.device}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("device", POINTER(c_int)),
    ]


class SwapchainImageD3D11KHR(Structure):
    def __init__(
        self,
        texture: POINTER(c_int) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SWAPCHAIN_IMAGE_D3D11_KHR,
    ) -> None:
        super().__init__(
            texture=texture,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainImageD3D11KHR(texture={repr(self.texture)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageD3D11KHR(texture={self.texture}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("texture", POINTER(c_int)),
    ]


class GraphicsRequirementsD3D11KHR(Structure):
    def __init__(
        self,
        adapter_luid: _LUID = 0,
        min_feature_level: int = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.GRAPHICS_REQUIREMENTS_D3D11_KHR,
    ) -> None:
        super().__init__(
            adapter_luid=adapter_luid,
            min_feature_level=min_feature_level,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.GraphicsRequirementsD3D11KHR(adapter_luid={repr(self.adapter_luid)}, min_feature_level={repr(self.min_feature_level)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.GraphicsRequirementsD3D11KHR(adapter_luid={self.adapter_luid}, min_feature_level={self.min_feature_level}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("adapter_luid", _LUID),
        ("min_feature_level", c_int),
    ]


PFN_xrGetD3D11GraphicsRequirementsKHR = CFUNCTYPE(Result.ctype(), InstanceHandle, SystemId, POINTER(GraphicsRequirementsD3D11KHR))


class GraphicsBindingD3D12KHR(Structure):
    def __init__(
        self,
        device: POINTER(c_int) = None,
        queue: POINTER(c_int) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.GRAPHICS_BINDING_D3D12_KHR,
    ) -> None:
        super().__init__(
            device=device,
            queue=queue,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.GraphicsBindingD3D12KHR(device={repr(self.device)}, queue={repr(self.queue)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.GraphicsBindingD3D12KHR(device={self.device}, queue={self.queue}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("device", POINTER(c_int)),
        ("queue", POINTER(c_int)),
    ]


class SwapchainImageD3D12KHR(Structure):
    def __init__(
        self,
        texture: POINTER(c_int) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SWAPCHAIN_IMAGE_D3D12_KHR,
    ) -> None:
        super().__init__(
            texture=texture,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainImageD3D12KHR(texture={repr(self.texture)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageD3D12KHR(texture={self.texture}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("texture", POINTER(c_int)),
    ]


class GraphicsRequirementsD3D12KHR(Structure):
    def __init__(
        self,
        adapter_luid: _LUID = 0,
        min_feature_level: int = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.GRAPHICS_REQUIREMENTS_D3D12_KHR,
    ) -> None:
        super().__init__(
            adapter_luid=adapter_luid,
            min_feature_level=min_feature_level,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.GraphicsRequirementsD3D12KHR(adapter_luid={repr(self.adapter_luid)}, min_feature_level={repr(self.min_feature_level)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.GraphicsRequirementsD3D12KHR(adapter_luid={self.adapter_luid}, min_feature_level={self.min_feature_level}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("adapter_luid", _LUID),
        ("min_feature_level", c_int),
    ]


PFN_xrGetD3D12GraphicsRequirementsKHR = CFUNCTYPE(Result.ctype(), InstanceHandle, SystemId, POINTER(GraphicsRequirementsD3D12KHR))

PFN_xrConvertWin32PerformanceCounterToTimeKHR = CFUNCTYPE(Result.ctype(), InstanceHandle, POINTER(_LARGE_INTEGER), POINTER(Time))

PFN_xrConvertTimeToWin32PerformanceCounterKHR = CFUNCTYPE(Result.ctype(), InstanceHandle, Time, POINTER(_LARGE_INTEGER))


class timespec(Structure):
    pass


PFN_xrConvertTimespecTimeToTimeKHR = CFUNCTYPE(Result.ctype(), InstanceHandle, POINTER(timespec), POINTER(Time))


class timespec(Structure):
    pass


PFN_xrConvertTimeToTimespecTimeKHR = CFUNCTYPE(Result.ctype(), InstanceHandle, Time, POINTER(timespec))

VulkanInstanceCreateFlagsKHRCInt = Flags64

class VulkanInstanceCreateFlagsKHR(FlagBase):
    NONE = 0x00000000

VulkanDeviceCreateFlagsKHRCInt = Flags64

class VulkanDeviceCreateFlagsKHR(FlagBase):
    NONE = 0x00000000


class VulkanInstanceCreateInfoKHR(Structure):
    def __init__(
        self,
        system_id: SystemId = 0,
        create_flags: VulkanInstanceCreateFlagsKHR = VulkanInstanceCreateFlagsKHR(),
        pfn_get_instance_proc_addr: int = 0,
        vulkan_create_info: POINTER(c_int) = None,
        vulkan_allocator: POINTER(c_int) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.VULKAN_INSTANCE_CREATE_INFO_KHR,
    ) -> None:
        super().__init__(
            system_id=system_id,
            create_flags=VulkanInstanceCreateFlagsKHR(create_flags).value,
            pfn_get_instance_proc_addr=pfn_get_instance_proc_addr,
            vulkan_create_info=vulkan_create_info,
            vulkan_allocator=vulkan_allocator,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.VulkanInstanceCreateInfoKHR(system_id={repr(self.system_id)}, create_flags={repr(self.create_flags)}, pfn_get_instance_proc_addr={repr(self.pfn_get_instance_proc_addr)}, vulkan_create_info={repr(self.vulkan_create_info)}, vulkan_allocator={repr(self.vulkan_allocator)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.VulkanInstanceCreateInfoKHR(system_id={self.system_id}, create_flags={self.create_flags}, pfn_get_instance_proc_addr={self.pfn_get_instance_proc_addr}, vulkan_create_info={self.vulkan_create_info}, vulkan_allocator={self.vulkan_allocator}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("system_id", SystemId),
        ("create_flags", VulkanInstanceCreateFlagsKHRCInt),
        ("pfn_get_instance_proc_addr", c_int),
        ("vulkan_create_info", POINTER(c_int)),
        ("vulkan_allocator", POINTER(c_int)),
    ]


class VulkanDeviceCreateInfoKHR(Structure):
    def __init__(
        self,
        system_id: SystemId = 0,
        create_flags: VulkanDeviceCreateFlagsKHR = VulkanDeviceCreateFlagsKHR(),
        pfn_get_instance_proc_addr: int = 0,
        vulkan_physical_device: int = 0,
        vulkan_create_info: POINTER(c_int) = None,
        vulkan_allocator: POINTER(c_int) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.VULKAN_DEVICE_CREATE_INFO_KHR,
    ) -> None:
        super().__init__(
            system_id=system_id,
            create_flags=VulkanDeviceCreateFlagsKHR(create_flags).value,
            pfn_get_instance_proc_addr=pfn_get_instance_proc_addr,
            vulkan_physical_device=vulkan_physical_device,
            vulkan_create_info=vulkan_create_info,
            vulkan_allocator=vulkan_allocator,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.VulkanDeviceCreateInfoKHR(system_id={repr(self.system_id)}, create_flags={repr(self.create_flags)}, pfn_get_instance_proc_addr={repr(self.pfn_get_instance_proc_addr)}, vulkan_physical_device={repr(self.vulkan_physical_device)}, vulkan_create_info={repr(self.vulkan_create_info)}, vulkan_allocator={repr(self.vulkan_allocator)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.VulkanDeviceCreateInfoKHR(system_id={self.system_id}, create_flags={self.create_flags}, pfn_get_instance_proc_addr={self.pfn_get_instance_proc_addr}, vulkan_physical_device={self.vulkan_physical_device}, vulkan_create_info={self.vulkan_create_info}, vulkan_allocator={self.vulkan_allocator}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("system_id", SystemId),
        ("create_flags", VulkanDeviceCreateFlagsKHRCInt),
        ("pfn_get_instance_proc_addr", c_int),
        ("vulkan_physical_device", c_int),
        ("vulkan_create_info", POINTER(c_int)),
        ("vulkan_allocator", POINTER(c_int)),
    ]


GraphicsBindingVulkan2KHR = GraphicsBindingVulkanKHR


class VulkanGraphicsDeviceGetInfoKHR(Structure):
    def __init__(
        self,
        system_id: SystemId = 0,
        vulkan_instance: int = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.VULKAN_GRAPHICS_DEVICE_GET_INFO_KHR,
    ) -> None:
        super().__init__(
            system_id=system_id,
            vulkan_instance=vulkan_instance,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.VulkanGraphicsDeviceGetInfoKHR(system_id={repr(self.system_id)}, vulkan_instance={repr(self.vulkan_instance)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.VulkanGraphicsDeviceGetInfoKHR(system_id={self.system_id}, vulkan_instance={self.vulkan_instance}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("system_id", SystemId),
        ("vulkan_instance", c_int),
    ]


SwapchainImageVulkan2KHR = SwapchainImageVulkanKHR

GraphicsRequirementsVulkan2KHR = GraphicsRequirementsVulkanKHR

PFN_xrCreateVulkanInstanceKHR = CFUNCTYPE(Result.ctype(), InstanceHandle, POINTER(VulkanInstanceCreateInfoKHR), POINTER(c_int), POINTER(c_int))

PFN_xrCreateVulkanDeviceKHR = CFUNCTYPE(Result.ctype(), InstanceHandle, POINTER(VulkanDeviceCreateInfoKHR), POINTER(c_int), POINTER(c_int))

PFN_xrGetVulkanGraphicsDevice2KHR = CFUNCTYPE(Result.ctype(), InstanceHandle, POINTER(VulkanGraphicsDeviceGetInfoKHR), POINTER(c_int))

PFN_xrGetVulkanGraphicsRequirements2KHR = CFUNCTYPE(Result.ctype(), InstanceHandle, SystemId, POINTER(GraphicsRequirementsVulkanKHR))

PFN_xrCreateSpatialAnchorFromPerceptionAnchorMSFT = CFUNCTYPE(Result.ctype(), SessionHandle, POINTER(c_int), POINTER(SpatialAnchorMSFTHandle))

PFN_xrTryGetPerceptionAnchorFromSpatialAnchorMSFT = CFUNCTYPE(Result.ctype(), SessionHandle, SpatialAnchorMSFTHandle, POINTER(POINTER(c_int)))


class HolographicWindowAttachmentMSFT(Structure):
    def __init__(
        self,
        holographic_space: POINTER(c_int) = None,
        core_window: POINTER(c_int) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.HOLOGRAPHIC_WINDOW_ATTACHMENT_MSFT,
    ) -> None:
        super().__init__(
            holographic_space=holographic_space,
            core_window=core_window,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.HolographicWindowAttachmentMSFT(holographic_space={repr(self.holographic_space)}, core_window={repr(self.core_window)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.HolographicWindowAttachmentMSFT(holographic_space={self.holographic_space}, core_window={self.core_window}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("holographic_space", POINTER(c_int)),
        ("core_window", POINTER(c_int)),
    ]


PFN_xrGetAudioOutputDeviceGuidOculus = CFUNCTYPE(Result.ctype(), InstanceHandle, (c_wchar * 128))

PFN_xrGetAudioInputDeviceGuidOculus = CFUNCTYPE(Result.ctype(), InstanceHandle, (c_wchar * 128))


class SwapchainImageFoveationVulkanFB(Structure):
    def __init__(
        self,
        image: int = 0,
        width: int = 0,
        height: int = 0,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SWAPCHAIN_IMAGE_FOVEATION_VULKAN_FB,
    ) -> None:
        super().__init__(
            image=image,
            width=width,
            height=height,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainImageFoveationVulkanFB(image={repr(self.image)}, width={repr(self.width)}, height={repr(self.height)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageFoveationVulkanFB(image={self.image}, width={self.width}, height={self.height}, next_structure={self.next_structure}, structure_type={self.structure_type})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("image", c_int),
        ("width", c_uint32),
        ("height", c_uint32),
    ]


class SwapchainStateSamplerVulkanFB(Structure):
    def __init__(
        self,
        min_filter: int = 0,
        mag_filter: int = 0,
        mipmap_mode: int = 0,
        wrap_mode_s: int = 0,
        wrap_mode_t: int = 0,
        swizzle_red: int = 0,
        swizzle_green: int = 0,
        swizzle_blue: int = 0,
        swizzle_alpha: int = 0,
        max_anisotropy: float = 0,
        border_color: Color4f = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.SWAPCHAIN_STATE_SAMPLER_VULKAN_FB,
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
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainStateSamplerVulkanFB(min_filter={repr(self.min_filter)}, mag_filter={repr(self.mag_filter)}, mipmap_mode={repr(self.mipmap_mode)}, wrap_mode_s={repr(self.wrap_mode_s)}, wrap_mode_t={repr(self.wrap_mode_t)}, swizzle_red={repr(self.swizzle_red)}, swizzle_green={repr(self.swizzle_green)}, swizzle_blue={repr(self.swizzle_blue)}, swizzle_alpha={repr(self.swizzle_alpha)}, max_anisotropy={repr(self.max_anisotropy)}, border_color={repr(self.border_color)}, next_structure={repr(self.next_structure)}, structure_type={repr(self.structure_type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainStateSamplerVulkanFB(min_filter={self.min_filter}, mag_filter={self.mag_filter}, mipmap_mode={self.mipmap_mode}, wrap_mode_s={self.wrap_mode_s}, wrap_mode_t={self.wrap_mode_t}, swizzle_red={self.swizzle_red}, swizzle_green={self.swizzle_green}, swizzle_blue={self.swizzle_blue}, swizzle_alpha={self.swizzle_alpha}, max_anisotropy={self.max_anisotropy:.3f}, border_color={self.border_color}, next_structure={self.next_structure}, structure_type={self.structure_type})"

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


__all__ = [
    "FB_FOVEATION_VULKAN_EXTENSION_NAME",
    "FB_SWAPCHAIN_UPDATE_STATE_VULKAN_EXTENSION_NAME",
    "FB_foveation_vulkan",
    "FB_foveation_vulkan_SPEC_VERSION",
    "FB_swapchain_update_state_vulkan",
    "FB_swapchain_update_state_vulkan_SPEC_VERSION",
    "GraphicsBindingD3D11KHR",
    "GraphicsBindingD3D12KHR",
    "GraphicsBindingOpenGLWin32KHR",
    "GraphicsBindingVulkan2KHR",
    "GraphicsBindingVulkanKHR",
    "GraphicsRequirementsD3D11KHR",
    "GraphicsRequirementsD3D12KHR",
    "GraphicsRequirementsOpenGLKHR",
    "GraphicsRequirementsVulkan2KHR",
    "GraphicsRequirementsVulkanKHR",
    "HolographicWindowAttachmentMSFT",
    "KHR_CONVERT_TIMESPEC_TIME_EXTENSION_NAME",
    "KHR_D3D11_ENABLE_EXTENSION_NAME",
    "KHR_D3D11_enable",
    "KHR_D3D11_enable_SPEC_VERSION",
    "KHR_D3D12_ENABLE_EXTENSION_NAME",
    "KHR_D3D12_enable",
    "KHR_D3D12_enable_SPEC_VERSION",
    "KHR_OPENGL_ENABLE_EXTENSION_NAME",
    "KHR_VULKAN_ENABLE2_EXTENSION_NAME",
    "KHR_VULKAN_ENABLE_EXTENSION_NAME",
    "KHR_VULKAN_SWAPCHAIN_FORMAT_LIST_EXTENSION_NAME",
    "KHR_WIN32_CONVERT_PERFORMANCE_COUNTER_TIME_EXTENSION_NAME",
    "KHR_convert_timespec_time",
    "KHR_convert_timespec_time_SPEC_VERSION",
    "KHR_opengl_enable",
    "KHR_opengl_enable_SPEC_VERSION",
    "KHR_vulkan_enable",
    "KHR_vulkan_enable2",
    "KHR_vulkan_enable2_SPEC_VERSION",
    "KHR_vulkan_enable_SPEC_VERSION",
    "KHR_vulkan_swapchain_format_list",
    "KHR_vulkan_swapchain_format_list_SPEC_VERSION",
    "KHR_win32_convert_performance_counter_time",
    "KHR_win32_convert_performance_counter_time_SPEC_VERSION",
    "MAX_AUDIO_DEVICE_STR_SIZE_OCULUS",
    "MSFT_HOLOGRAPHIC_WINDOW_ATTACHMENT_EXTENSION_NAME",
    "MSFT_PERCEPTION_ANCHOR_INTEROP_EXTENSION_NAME",
    "MSFT_holographic_window_attachment",
    "MSFT_holographic_window_attachment_SPEC_VERSION",
    "MSFT_perception_anchor_interop",
    "MSFT_perception_anchor_interop_SPEC_VERSION",
    "OCULUS_AUDIO_DEVICE_GUID_EXTENSION_NAME",
    "OCULUS_audio_device_guid",
    "OCULUS_audio_device_guid_SPEC_VERSION",
    "PFN_xrConvertTimeToTimespecTimeKHR",
    "PFN_xrConvertTimeToWin32PerformanceCounterKHR",
    "PFN_xrConvertTimespecTimeToTimeKHR",
    "PFN_xrConvertWin32PerformanceCounterToTimeKHR",
    "PFN_xrCreateSpatialAnchorFromPerceptionAnchorMSFT",
    "PFN_xrCreateVulkanDeviceKHR",
    "PFN_xrCreateVulkanInstanceKHR",
    "PFN_xrGetAudioInputDeviceGuidOculus",
    "PFN_xrGetAudioOutputDeviceGuidOculus",
    "PFN_xrGetD3D11GraphicsRequirementsKHR",
    "PFN_xrGetD3D12GraphicsRequirementsKHR",
    "PFN_xrGetOpenGLGraphicsRequirementsKHR",
    "PFN_xrGetVulkanDeviceExtensionsKHR",
    "PFN_xrGetVulkanGraphicsDevice2KHR",
    "PFN_xrGetVulkanGraphicsDeviceKHR",
    "PFN_xrGetVulkanGraphicsRequirements2KHR",
    "PFN_xrGetVulkanGraphicsRequirementsKHR",
    "PFN_xrGetVulkanInstanceExtensionsKHR",
    "PFN_xrTryGetPerceptionAnchorFromSpatialAnchorMSFT",
    "SwapchainImageD3D11KHR",
    "SwapchainImageD3D12KHR",
    "SwapchainImageFoveationVulkanFB",
    "SwapchainImageOpenGLKHR",
    "SwapchainImageVulkan2KHR",
    "SwapchainImageVulkanKHR",
    "SwapchainStateSamplerVulkanFB",
    "VulkanDeviceCreateFlagsKHR",
    "VulkanDeviceCreateFlagsKHRCInt",
    "VulkanDeviceCreateInfoKHR",
    "VulkanGraphicsDeviceGetInfoKHR",
    "VulkanInstanceCreateFlagsKHR",
    "VulkanInstanceCreateFlagsKHRCInt",
    "VulkanInstanceCreateInfoKHR",
    "VulkanSwapchainFormatListCreateInfoKHR",
    "timespec",
]
