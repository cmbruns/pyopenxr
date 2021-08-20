# Warning: this file is auto-generated. Do not edit.

from ctypes import CFUNCTYPE, POINTER, Structure, c_char_p, c_float, c_int, c_uint32, c_void_p, c_wchar
from ..enums import *
from ..typedefs import *

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
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.VULKAN_SWAPCHAIN_FORMAT_LIST_CREATE_INFO_K_H_R.value,
            None, *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_format_count", c_uint32),
        ("view_formats", POINTER(c_int)),
    ]


class GraphicsBindingOpenGLWin32KHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.GRAPHICS_BINDING_OPEN_G_L_WIN32_K_H_R.value,
            None, *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("h_d_c", c_int),
        ("h_g_l_r_c", c_int),
    ]


class SwapchainImageOpenGLKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SWAPCHAIN_IMAGE_OPEN_G_L_K_H_R.value,
            None, *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("image", c_uint32),
    ]


class GraphicsRequirementsOpenGLKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.GRAPHICS_REQUIREMENTS_OPEN_G_L_K_H_R.value,
            None, *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("min_api_version_supported", Version),
        ("max_api_version_supported", Version),
    ]


PFN_xrGetOpenGLGraphicsRequirementsKHR = CFUNCTYPE(Result.ctype(), Instance, SystemId, POINTER(GraphicsRequirementsOpenGLKHR))


class GraphicsBindingVulkanKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.GRAPHICS_BINDING_VULKAN_K_H_R.value,
            None, *args, **kwargs,
        )            

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
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SWAPCHAIN_IMAGE_VULKAN_K_H_R.value,
            None, *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("image", c_int),
    ]


class GraphicsRequirementsVulkanKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.GRAPHICS_REQUIREMENTS_VULKAN_K_H_R.value,
            None, *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("min_api_version_supported", Version),
        ("max_api_version_supported", Version),
    ]


PFN_xrGetVulkanInstanceExtensionsKHR = CFUNCTYPE(Result.ctype(), Instance, SystemId, c_uint32, POINTER(c_uint32), c_char_p)

PFN_xrGetVulkanDeviceExtensionsKHR = CFUNCTYPE(Result.ctype(), Instance, SystemId, c_uint32, POINTER(c_uint32), c_char_p)

PFN_xrGetVulkanGraphicsDeviceKHR = CFUNCTYPE(Result.ctype(), Instance, SystemId, c_int, POINTER(c_int))

PFN_xrGetVulkanGraphicsRequirementsKHR = CFUNCTYPE(Result.ctype(), Instance, SystemId, POINTER(GraphicsRequirementsVulkanKHR))


class GraphicsBindingD3D11KHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.GRAPHICS_BINDING_D3_D11_K_H_R.value,
            None, *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("device", POINTER(c_int)),
    ]


class SwapchainImageD3D11KHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SWAPCHAIN_IMAGE_D3_D11_K_H_R.value,
            None, *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("texture", POINTER(c_int)),
    ]


class GraphicsRequirementsD3D11KHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.GRAPHICS_REQUIREMENTS_D3_D11_K_H_R.value,
            None, *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("adapter_luid", c_int),
        ("min_feature_level", c_int),
    ]


PFN_xrGetD3D11GraphicsRequirementsKHR = CFUNCTYPE(Result.ctype(), Instance, SystemId, POINTER(GraphicsRequirementsD3D11KHR))


class GraphicsBindingD3D12KHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.GRAPHICS_BINDING_D3_D12_K_H_R.value,
            None, *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("device", POINTER(c_int)),
        ("queue", POINTER(c_int)),
    ]


class SwapchainImageD3D12KHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SWAPCHAIN_IMAGE_D3_D12_K_H_R.value,
            None, *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("texture", POINTER(c_int)),
    ]


class GraphicsRequirementsD3D12KHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.GRAPHICS_REQUIREMENTS_D3_D12_K_H_R.value,
            None, *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("adapter_luid", c_int),
        ("min_feature_level", c_int),
    ]


PFN_xrGetD3D12GraphicsRequirementsKHR = CFUNCTYPE(Result.ctype(), Instance, SystemId, POINTER(GraphicsRequirementsD3D12KHR))

PFN_xrConvertWin32PerformanceCounterToTimeKHR = CFUNCTYPE(Result.ctype(), Instance, POINTER(c_int), POINTER(Time))

PFN_xrConvertTimeToWin32PerformanceCounterKHR = CFUNCTYPE(Result.ctype(), Instance, Time, POINTER(c_int))


class timespec(Structure):
    pass


PFN_xrConvertTimespecTimeToTimeKHR = CFUNCTYPE(Result.ctype(), Instance, POINTER(timespec), POINTER(Time))


class timespec(Structure):
    pass


PFN_xrConvertTimeToTimespecTimeKHR = CFUNCTYPE(Result.ctype(), Instance, Time, POINTER(timespec))

VulkanInstanceCreateFlagsKHR = Flags64

VulkanDeviceCreateFlagsKHR = Flags64


class VulkanInstanceCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.VULKAN_INSTANCE_CREATE_INFO_K_H_R.value,
            None, *args, **kwargs,
        )            

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
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.VULKAN_DEVICE_CREATE_INFO_K_H_R.value,
            None, *args, **kwargs,
        )            

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
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.VULKAN_GRAPHICS_DEVICE_GET_INFO_K_H_R.value,
            None, *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("system_id", SystemId),
        ("vulkan_instance", c_int),
    ]


SwapchainImageVulkan2KHR = SwapchainImageVulkanKHR

GraphicsRequirementsVulkan2KHR = GraphicsRequirementsVulkanKHR

PFN_xrCreateVulkanInstanceKHR = CFUNCTYPE(Result.ctype(), Instance, POINTER(VulkanInstanceCreateInfoKHR), POINTER(c_int), POINTER(c_int))

PFN_xrCreateVulkanDeviceKHR = CFUNCTYPE(Result.ctype(), Instance, POINTER(VulkanDeviceCreateInfoKHR), POINTER(c_int), POINTER(c_int))

PFN_xrGetVulkanGraphicsDevice2KHR = CFUNCTYPE(Result.ctype(), Instance, POINTER(VulkanGraphicsDeviceGetInfoKHR), POINTER(c_int))

PFN_xrGetVulkanGraphicsRequirements2KHR = CFUNCTYPE(Result.ctype(), Instance, SystemId, POINTER(GraphicsRequirementsVulkanKHR))

PFN_xrCreateSpatialAnchorFromPerceptionAnchorMSFT = CFUNCTYPE(Result.ctype(), Session, POINTER(c_int), POINTER(SpatialAnchorMSFT))

PFN_xrTryGetPerceptionAnchorFromSpatialAnchorMSFT = CFUNCTYPE(Result.ctype(), Session, SpatialAnchorMSFT, POINTER(POINTER(c_int)))


class HolographicWindowAttachmentMSFT(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.HOLOGRAPHIC_WINDOW_ATTACHMENT_M_S_F_T.value,
            None, *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("holographic_space", POINTER(c_int)),
        ("core_window", POINTER(c_int)),
    ]


PFN_xrGetAudioOutputDeviceGuidOculus = CFUNCTYPE(Result.ctype(), Instance, (c_wchar * 128))

PFN_xrGetAudioInputDeviceGuidOculus = CFUNCTYPE(Result.ctype(), Instance, (c_wchar * 128))


class SwapchainImageFoveationVulkanFB(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SWAPCHAIN_IMAGE_FOVEATION_VULKAN_F_B.value,
            None, *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("image", c_int),
        ("width", c_uint32),
        ("height", c_uint32),
    ]


class SwapchainStateSamplerVulkanFB(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SWAPCHAIN_STATE_SAMPLER_VULKAN_F_B.value,
            None, *args, **kwargs,
        )            

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
