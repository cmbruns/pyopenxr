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
KHR_opengl_enable_SPEC_VERSION = 9
KHR_OPENGL_ENABLE_EXTENSION_NAME = "XR_KHR_opengl_enable"
KHR_vulkan_enable = 1
KHR_vulkan_enable_SPEC_VERSION = 8
KHR_VULKAN_ENABLE_EXTENSION_NAME = "XR_KHR_vulkan_enable"
KHR_D3D11_enable = 1
KHR_D3D11_enable_SPEC_VERSION = 5
KHR_D3D11_ENABLE_EXTENSION_NAME = "XR_KHR_D3D11_enable"
KHR_D3D12_enable = 1
KHR_D3D12_enable_SPEC_VERSION = 7
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
        return f"xr.VulkanSwapchainFormatListCreateInfoKHR(type={repr(self.type)}, next={repr(self.next)}, view_format_count={repr(self.view_format_count)}, view_formats={repr(self.view_formats)})"

    def __str__(self) -> str:
        return f"xr.VulkanSwapchainFormatListCreateInfoKHR(type={str(self.type)}, next={str(self.next)}, view_format_count={str(self.view_format_count)}, view_formats={str(self.view_formats)})"

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
        return f"xr.GraphicsBindingOpenGLWin32KHR(type={repr(self.type)}, next={repr(self.next)}, h_dc={repr(self.h_dc)}, h_glrc={repr(self.h_glrc)})"

    def __str__(self) -> str:
        return f"xr.GraphicsBindingOpenGLWin32KHR(type={str(self.type)}, next={str(self.next)}, h_dc={str(self.h_dc)}, h_glrc={str(self.h_glrc)})"

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
        return f"xr.SwapchainImageOpenGLKHR(type={repr(self.type)}, next={repr(self.next)}, image={repr(self.image)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageOpenGLKHR(type={str(self.type)}, next={str(self.next)}, image={str(self.image)})"

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
        return f"xr.GraphicsRequirementsOpenGLKHR(type={repr(self.type)}, next={repr(self.next)}, min_api_version_supported={repr(self.min_api_version_supported)}, max_api_version_supported={repr(self.max_api_version_supported)})"

    def __str__(self) -> str:
        return f"xr.GraphicsRequirementsOpenGLKHR(type={str(self.type)}, next={str(self.next)}, min_api_version_supported={str(self.min_api_version_supported)}, max_api_version_supported={str(self.max_api_version_supported)})"

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
        return f"xr.GraphicsBindingVulkanKHR(type={repr(self.type)}, next={repr(self.next)}, instance={repr(self.instance)}, physical_device={repr(self.physical_device)}, device={repr(self.device)}, queue_family_index={repr(self.queue_family_index)}, queue_index={repr(self.queue_index)})"

    def __str__(self) -> str:
        return f"xr.GraphicsBindingVulkanKHR(type={str(self.type)}, next={str(self.next)}, instance={str(self.instance)}, physical_device={str(self.physical_device)}, device={str(self.device)}, queue_family_index={str(self.queue_family_index)}, queue_index={str(self.queue_index)})"

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
        return f"xr.SwapchainImageVulkanKHR(type={repr(self.type)}, next={repr(self.next)}, image={repr(self.image)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageVulkanKHR(type={str(self.type)}, next={str(self.next)}, image={str(self.image)})"

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
        return f"xr.GraphicsRequirementsVulkanKHR(type={repr(self.type)}, next={repr(self.next)}, min_api_version_supported={repr(self.min_api_version_supported)}, max_api_version_supported={repr(self.max_api_version_supported)})"

    def __str__(self) -> str:
        return f"xr.GraphicsRequirementsVulkanKHR(type={str(self.type)}, next={str(self.next)}, min_api_version_supported={str(self.min_api_version_supported)}, max_api_version_supported={str(self.max_api_version_supported)})"

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
        return f"xr.GraphicsBindingD3D11KHR(type={repr(self.type)}, next={repr(self.next)}, device={repr(self.device)})"

    def __str__(self) -> str:
        return f"xr.GraphicsBindingD3D11KHR(type={str(self.type)}, next={str(self.next)}, device={str(self.device)})"

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
        return f"xr.SwapchainImageD3D11KHR(type={repr(self.type)}, next={repr(self.next)}, texture={repr(self.texture)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageD3D11KHR(type={str(self.type)}, next={str(self.next)}, texture={str(self.texture)})"

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
        return f"xr.GraphicsRequirementsD3D11KHR(type={repr(self.type)}, next={repr(self.next)}, adapter_luid={repr(self.adapter_luid)}, min_feature_level={repr(self.min_feature_level)})"

    def __str__(self) -> str:
        return f"xr.GraphicsRequirementsD3D11KHR(type={str(self.type)}, next={str(self.next)}, adapter_luid={str(self.adapter_luid)}, min_feature_level={str(self.min_feature_level)})"

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
        return f"xr.GraphicsBindingD3D12KHR(type={repr(self.type)}, next={repr(self.next)}, device={repr(self.device)}, queue={repr(self.queue)})"

    def __str__(self) -> str:
        return f"xr.GraphicsBindingD3D12KHR(type={str(self.type)}, next={str(self.next)}, device={str(self.device)}, queue={str(self.queue)})"

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
        return f"xr.SwapchainImageD3D12KHR(type={repr(self.type)}, next={repr(self.next)}, texture={repr(self.texture)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageD3D12KHR(type={str(self.type)}, next={str(self.next)}, texture={str(self.texture)})"

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
        return f"xr.GraphicsRequirementsD3D12KHR(type={repr(self.type)}, next={repr(self.next)}, adapter_luid={repr(self.adapter_luid)}, min_feature_level={repr(self.min_feature_level)})"

    def __str__(self) -> str:
        return f"xr.GraphicsRequirementsD3D12KHR(type={str(self.type)}, next={str(self.next)}, adapter_luid={str(self.adapter_luid)}, min_feature_level={str(self.min_feature_level)})"

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

VulkanInstanceCreateFlagsKHR = Flags64

VulkanDeviceCreateFlagsKHR = Flags64


class VulkanInstanceCreateInfoKHR(Structure):
    def __init__(
        self,
        system_id: SystemId = 0,
        create_flags: VulkanInstanceCreateFlagsKHR = 0,
        pfn_get_instance_proc_addr: int = 0,
        vulkan_create_info: POINTER(c_int) = None,
        vulkan_allocator: POINTER(c_int) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.VULKAN_INSTANCE_CREATE_INFO_KHR,
    ) -> None:
        super().__init__(
            system_id=system_id,
            create_flags=create_flags,
            pfn_get_instance_proc_addr=pfn_get_instance_proc_addr,
            vulkan_create_info=vulkan_create_info,
            vulkan_allocator=vulkan_allocator,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.VulkanInstanceCreateInfoKHR(type={repr(self.type)}, next={repr(self.next)}, system_id={repr(self.system_id)}, create_flags={repr(self.create_flags)}, pfn_get_instance_proc_addr={repr(self.pfn_get_instance_proc_addr)}, vulkan_create_info={repr(self.vulkan_create_info)}, vulkan_allocator={repr(self.vulkan_allocator)})"

    def __str__(self) -> str:
        return f"xr.VulkanInstanceCreateInfoKHR(type={str(self.type)}, next={str(self.next)}, system_id={str(self.system_id)}, create_flags={str(self.create_flags)}, pfn_get_instance_proc_addr={str(self.pfn_get_instance_proc_addr)}, vulkan_create_info={str(self.vulkan_create_info)}, vulkan_allocator={str(self.vulkan_allocator)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("system_id", SystemId),
        ("create_flags", VulkanInstanceCreateFlagsKHR),
        ("pfn_get_instance_proc_addr", c_int),
        ("vulkan_create_info", POINTER(c_int)),
        ("vulkan_allocator", POINTER(c_int)),
    ]


class VulkanDeviceCreateInfoKHR(Structure):
    def __init__(
        self,
        system_id: SystemId = 0,
        create_flags: VulkanDeviceCreateFlagsKHR = 0,
        pfn_get_instance_proc_addr: int = 0,
        vulkan_physical_device: int = 0,
        vulkan_create_info: POINTER(c_int) = None,
        vulkan_allocator: POINTER(c_int) = None,
        next_structure: c_void_p = None,
        structure_type: StructureType = StructureType.VULKAN_DEVICE_CREATE_INFO_KHR,
    ) -> None:
        super().__init__(
            system_id=system_id,
            create_flags=create_flags,
            pfn_get_instance_proc_addr=pfn_get_instance_proc_addr,
            vulkan_physical_device=vulkan_physical_device,
            vulkan_create_info=vulkan_create_info,
            vulkan_allocator=vulkan_allocator,
            next=next_structure,
            type=structure_type.value,
        )

    def __repr__(self) -> str:
        return f"xr.VulkanDeviceCreateInfoKHR(type={repr(self.type)}, next={repr(self.next)}, system_id={repr(self.system_id)}, create_flags={repr(self.create_flags)}, pfn_get_instance_proc_addr={repr(self.pfn_get_instance_proc_addr)}, vulkan_physical_device={repr(self.vulkan_physical_device)}, vulkan_create_info={repr(self.vulkan_create_info)}, vulkan_allocator={repr(self.vulkan_allocator)})"

    def __str__(self) -> str:
        return f"xr.VulkanDeviceCreateInfoKHR(type={str(self.type)}, next={str(self.next)}, system_id={str(self.system_id)}, create_flags={str(self.create_flags)}, pfn_get_instance_proc_addr={str(self.pfn_get_instance_proc_addr)}, vulkan_physical_device={str(self.vulkan_physical_device)}, vulkan_create_info={str(self.vulkan_create_info)}, vulkan_allocator={str(self.vulkan_allocator)})"

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("system_id", SystemId),
        ("create_flags", VulkanDeviceCreateFlagsKHR),
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
        return f"xr.VulkanGraphicsDeviceGetInfoKHR(type={repr(self.type)}, next={repr(self.next)}, system_id={repr(self.system_id)}, vulkan_instance={repr(self.vulkan_instance)})"

    def __str__(self) -> str:
        return f"xr.VulkanGraphicsDeviceGetInfoKHR(type={str(self.type)}, next={str(self.next)}, system_id={str(self.system_id)}, vulkan_instance={str(self.vulkan_instance)})"

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
        return f"xr.HolographicWindowAttachmentMSFT(type={repr(self.type)}, next={repr(self.next)}, holographic_space={repr(self.holographic_space)}, core_window={repr(self.core_window)})"

    def __str__(self) -> str:
        return f"xr.HolographicWindowAttachmentMSFT(type={str(self.type)}, next={str(self.next)}, holographic_space={str(self.holographic_space)}, core_window={str(self.core_window)})"

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
        return f"xr.SwapchainImageFoveationVulkanFB(type={repr(self.type)}, next={repr(self.next)}, image={repr(self.image)}, width={repr(self.width)}, height={repr(self.height)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageFoveationVulkanFB(type={str(self.type)}, next={str(self.next)}, image={str(self.image)}, width={str(self.width)}, height={str(self.height)})"

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
        return f"xr.SwapchainStateSamplerVulkanFB(type={repr(self.type)}, next={repr(self.next)}, min_filter={repr(self.min_filter)}, mag_filter={repr(self.mag_filter)}, mipmap_mode={repr(self.mipmap_mode)}, wrap_mode_s={repr(self.wrap_mode_s)}, wrap_mode_t={repr(self.wrap_mode_t)}, swizzle_red={repr(self.swizzle_red)}, swizzle_green={repr(self.swizzle_green)}, swizzle_blue={repr(self.swizzle_blue)}, swizzle_alpha={repr(self.swizzle_alpha)}, max_anisotropy={repr(self.max_anisotropy)}, border_color={repr(self.border_color)})"

    def __str__(self) -> str:
        return f"xr.SwapchainStateSamplerVulkanFB(type={str(self.type)}, next={str(self.next)}, min_filter={str(self.min_filter)}, mag_filter={str(self.mag_filter)}, mipmap_mode={str(self.mipmap_mode)}, wrap_mode_s={str(self.wrap_mode_s)}, wrap_mode_t={str(self.wrap_mode_t)}, swizzle_red={str(self.swizzle_red)}, swizzle_green={str(self.swizzle_green)}, swizzle_blue={str(self.swizzle_blue)}, swizzle_alpha={str(self.swizzle_alpha)}, max_anisotropy={str(self.max_anisotropy)}, border_color={str(self.border_color)})"

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
    "KHR_vulkan_swapchain_format_list",
    "KHR_vulkan_swapchain_format_list_SPEC_VERSION",
    "KHR_VULKAN_SWAPCHAIN_FORMAT_LIST_EXTENSION_NAME",
    "KHR_opengl_enable",
    "KHR_opengl_enable_SPEC_VERSION",
    "KHR_OPENGL_ENABLE_EXTENSION_NAME",
    "KHR_vulkan_enable",
    "KHR_vulkan_enable_SPEC_VERSION",
    "KHR_VULKAN_ENABLE_EXTENSION_NAME",
    "KHR_D3D11_enable",
    "KHR_D3D11_enable_SPEC_VERSION",
    "KHR_D3D11_ENABLE_EXTENSION_NAME",
    "KHR_D3D12_enable",
    "KHR_D3D12_enable_SPEC_VERSION",
    "KHR_D3D12_ENABLE_EXTENSION_NAME",
    "KHR_win32_convert_performance_counter_time",
    "KHR_win32_convert_performance_counter_time_SPEC_VERSION",
    "KHR_WIN32_CONVERT_PERFORMANCE_COUNTER_TIME_EXTENSION_NAME",
    "KHR_convert_timespec_time",
    "KHR_convert_timespec_time_SPEC_VERSION",
    "KHR_CONVERT_TIMESPEC_TIME_EXTENSION_NAME",
    "KHR_vulkan_enable2",
    "KHR_vulkan_enable2_SPEC_VERSION",
    "KHR_VULKAN_ENABLE2_EXTENSION_NAME",
    "MSFT_perception_anchor_interop",
    "MSFT_perception_anchor_interop_SPEC_VERSION",
    "MSFT_PERCEPTION_ANCHOR_INTEROP_EXTENSION_NAME",
    "MSFT_holographic_window_attachment",
    "MSFT_holographic_window_attachment_SPEC_VERSION",
    "MSFT_HOLOGRAPHIC_WINDOW_ATTACHMENT_EXTENSION_NAME",
    "OCULUS_audio_device_guid",
    "OCULUS_audio_device_guid_SPEC_VERSION",
    "OCULUS_AUDIO_DEVICE_GUID_EXTENSION_NAME",
    "MAX_AUDIO_DEVICE_STR_SIZE_OCULUS",
    "FB_foveation_vulkan",
    "FB_foveation_vulkan_SPEC_VERSION",
    "FB_FOVEATION_VULKAN_EXTENSION_NAME",
    "FB_swapchain_update_state_vulkan",
    "FB_swapchain_update_state_vulkan_SPEC_VERSION",
    "FB_SWAPCHAIN_UPDATE_STATE_VULKAN_EXTENSION_NAME",
    "VulkanSwapchainFormatListCreateInfoKHR",
    "GraphicsBindingOpenGLWin32KHR",
    "SwapchainImageOpenGLKHR",
    "GraphicsRequirementsOpenGLKHR",
    "PFN_xrGetOpenGLGraphicsRequirementsKHR",
    "GraphicsBindingVulkanKHR",
    "SwapchainImageVulkanKHR",
    "GraphicsRequirementsVulkanKHR",
    "PFN_xrGetVulkanInstanceExtensionsKHR",
    "PFN_xrGetVulkanDeviceExtensionsKHR",
    "PFN_xrGetVulkanGraphicsDeviceKHR",
    "PFN_xrGetVulkanGraphicsRequirementsKHR",
    "GraphicsBindingD3D11KHR",
    "SwapchainImageD3D11KHR",
    "GraphicsRequirementsD3D11KHR",
    "PFN_xrGetD3D11GraphicsRequirementsKHR",
    "GraphicsBindingD3D12KHR",
    "SwapchainImageD3D12KHR",
    "GraphicsRequirementsD3D12KHR",
    "PFN_xrGetD3D12GraphicsRequirementsKHR",
    "PFN_xrConvertWin32PerformanceCounterToTimeKHR",
    "PFN_xrConvertTimeToWin32PerformanceCounterKHR",
    "timespec",
    "PFN_xrConvertTimespecTimeToTimeKHR",
    "timespec",
    "PFN_xrConvertTimeToTimespecTimeKHR",
    "VulkanInstanceCreateFlagsKHR",
    "VulkanDeviceCreateFlagsKHR",
    "VulkanInstanceCreateInfoKHR",
    "VulkanDeviceCreateInfoKHR",
    "GraphicsBindingVulkan2KHR",
    "VulkanGraphicsDeviceGetInfoKHR",
    "SwapchainImageVulkan2KHR",
    "GraphicsRequirementsVulkan2KHR",
    "PFN_xrCreateVulkanInstanceKHR",
    "PFN_xrCreateVulkanDeviceKHR",
    "PFN_xrGetVulkanGraphicsDevice2KHR",
    "PFN_xrGetVulkanGraphicsRequirements2KHR",
    "PFN_xrCreateSpatialAnchorFromPerceptionAnchorMSFT",
    "PFN_xrTryGetPerceptionAnchorFromSpatialAnchorMSFT",
    "HolographicWindowAttachmentMSFT",
    "PFN_xrGetAudioOutputDeviceGuidOculus",
    "PFN_xrGetAudioInputDeviceGuidOculus",
    "SwapchainImageFoveationVulkanFB",
    "SwapchainStateSamplerVulkanFB",
]
