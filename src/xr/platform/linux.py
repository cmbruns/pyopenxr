# Warning: this file is auto-generated. Do not edit.

from ctypes import CFUNCTYPE, POINTER, Structure, c_char_p, c_float, c_int, c_uint32, c_void_p
from ..enums import *
from ..typedefs import *


# Forward declaration of a Wayland structure
class wl_display(Structure):
    pass


KHR_vulkan_swapchain_format_list = 1
KHR_vulkan_swapchain_format_list_SPEC_VERSION = 4
KHR_VULKAN_SWAPCHAIN_FORMAT_LIST_EXTENSION_NAME = "XR_KHR_vulkan_swapchain_format_list"
KHR_opengl_enable = 1
KHR_opengl_enable_SPEC_VERSION = 9
KHR_OPENGL_ENABLE_EXTENSION_NAME = "XR_KHR_opengl_enable"
KHR_vulkan_enable = 1
KHR_vulkan_enable_SPEC_VERSION = 8
KHR_VULKAN_ENABLE_EXTENSION_NAME = "XR_KHR_vulkan_enable"
KHR_convert_timespec_time = 1
KHR_convert_timespec_time_SPEC_VERSION = 1
KHR_CONVERT_TIMESPEC_TIME_EXTENSION_NAME = "XR_KHR_convert_timespec_time"
KHR_vulkan_enable2 = 1
KHR_vulkan_enable2_SPEC_VERSION = 2
KHR_VULKAN_ENABLE2_EXTENSION_NAME = "XR_KHR_vulkan_enable2"
FB_foveation_vulkan = 1
FB_foveation_vulkan_SPEC_VERSION = 1
FB_FOVEATION_VULKAN_EXTENSION_NAME = "XR_FB_foveation_vulkan"
FB_swapchain_update_state_vulkan = 1
FB_swapchain_update_state_vulkan_SPEC_VERSION = 1
FB_SWAPCHAIN_UPDATE_STATE_VULKAN_EXTENSION_NAME = "XR_FB_swapchain_update_state_vulkan"


class VulkanSwapchainFormatListCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.VULKAN_SWAPCHAIN_FORMAT_LIST_CREATE_INFO_KHR.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("view_format_count", c_uint32),
        ("view_formats", POINTER(c_int)),
    ]


class GraphicsBindingOpenGLXlibKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.GRAPHICS_BINDING_OPENGL_XLIB_KHR.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("x_display", POINTER(c_int)),
        ("visualid", c_uint32),
        ("glx_fbconfig", c_int),
        ("glx_drawable", c_int),
        ("glx_context", c_int),
    ]


class GraphicsBindingOpenGLXcbKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.GRAPHICS_BINDING_OPENGL_XCB_KHR.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("connection", POINTER(c_int)),
        ("screen_number", c_uint32),
        ("fbconfigid", c_int),
        ("visualid", c_int),
        ("glx_drawable", c_int),
        ("glx_context", c_int),
    ]


class GraphicsBindingOpenGLWaylandKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.GRAPHICS_BINDING_OPENGL_WAYLAND_KHR.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("display", POINTER(wl_display)),
    ]


class SwapchainImageOpenGLKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SWAPCHAIN_IMAGE_OPENGL_KHR.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("image", c_uint32),
    ]


class GraphicsRequirementsOpenGLKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.GRAPHICS_REQUIREMENTS_OPENGL_KHR.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("min_api_version_supported", Version),
        ("max_api_version_supported", Version),
    ]


PFN_xrGetOpenGLGraphicsRequirementsKHR = CFUNCTYPE(Result.ctype(), InstanceHandle, SystemId, POINTER(GraphicsRequirementsOpenGLKHR))


class GraphicsBindingVulkanKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.GRAPHICS_BINDING_VULKAN_KHR.value,
            *args, **kwargs,
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
            StructureType.SWAPCHAIN_IMAGE_VULKAN_KHR.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("image", c_int),
    ]


class GraphicsRequirementsVulkanKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.GRAPHICS_REQUIREMENTS_VULKAN_KHR.value,
            *args, **kwargs,
        )            

    _fields_ = [
        ("type", StructureType.ctype()),
        ("next", c_void_p),
        ("min_api_version_supported", Version),
        ("max_api_version_supported", Version),
    ]


PFN_xrGetVulkanInstanceExtensionsKHR = CFUNCTYPE(Result.ctype(), InstanceHandle, SystemId, c_uint32, POINTER(c_uint32), c_char_p)

PFN_xrGetVulkanDeviceExtensionsKHR = CFUNCTYPE(Result.ctype(), InstanceHandle, SystemId, c_uint32, POINTER(c_uint32), c_char_p)

PFN_xrGetVulkanGraphicsDeviceKHR = CFUNCTYPE(Result.ctype(), InstanceHandle, SystemId, c_int, POINTER(c_int))

PFN_xrGetVulkanGraphicsRequirementsKHR = CFUNCTYPE(Result.ctype(), InstanceHandle, SystemId, POINTER(GraphicsRequirementsVulkanKHR))


class timespec(Structure):
    pass


PFN_xrConvertTimespecTimeToTimeKHR = CFUNCTYPE(Result.ctype(), InstanceHandle, POINTER(timespec), POINTER(Time))


class timespec(Structure):
    pass


PFN_xrConvertTimeToTimespecTimeKHR = CFUNCTYPE(Result.ctype(), InstanceHandle, Time, POINTER(timespec))

VulkanInstanceCreateFlagsKHR = Flags64

VulkanDeviceCreateFlagsKHR = Flags64


class VulkanInstanceCreateInfoKHR(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.VULKAN_INSTANCE_CREATE_INFO_KHR.value,
            *args, **kwargs,
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
            StructureType.VULKAN_DEVICE_CREATE_INFO_KHR.value,
            *args, **kwargs,
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
            StructureType.VULKAN_GRAPHICS_DEVICE_GET_INFO_KHR.value,
            *args, **kwargs,
        )            

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


class SwapchainImageFoveationVulkanFB(Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.SWAPCHAIN_IMAGE_FOVEATION_VULKAN_FB.value,
            *args, **kwargs,
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
            StructureType.SWAPCHAIN_STATE_SAMPLER_VULKAN_FB.value,
            *args, **kwargs,
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
    "KHR_convert_timespec_time",
    "KHR_convert_timespec_time_SPEC_VERSION",
    "KHR_CONVERT_TIMESPEC_TIME_EXTENSION_NAME",
    "KHR_vulkan_enable2",
    "KHR_vulkan_enable2_SPEC_VERSION",
    "KHR_VULKAN_ENABLE2_EXTENSION_NAME",
    "FB_foveation_vulkan",
    "FB_foveation_vulkan_SPEC_VERSION",
    "FB_FOVEATION_VULKAN_EXTENSION_NAME",
    "FB_swapchain_update_state_vulkan",
    "FB_swapchain_update_state_vulkan_SPEC_VERSION",
    "FB_SWAPCHAIN_UPDATE_STATE_VULKAN_EXTENSION_NAME",
    "VulkanSwapchainFormatListCreateInfoKHR",
    "GraphicsBindingOpenGLXlibKHR",
    "GraphicsBindingOpenGLXcbKHR",
    "GraphicsBindingOpenGLWaylandKHR",
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
    "SwapchainImageFoveationVulkanFB",
    "SwapchainStateSamplerVulkanFB",
]
