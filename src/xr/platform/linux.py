# Warning: this file is auto-generated. Do not edit.

from ctypes import (
    CFUNCTYPE, POINTER, Structure, byref, c_char_p, c_float, c_int, c_long,
    c_longlong, c_uint32, c_void_p, cast, create_string_buffer,
)

import ctypes
from typing import Optional

import OpenGL.platform as _plat
from OpenGL.platform.glx import GLXPlatform
if not isinstance(_plat.PLATFORM, GLXPlatform):
    _plat.PLATFORM = GLXPlatform()  # override auto-selection
from OpenGL import GLX

try:
    from OpenGL.EGL import EGLConfig, EGLContext, EGLDisplay, EGLSurface
except (AttributeError, ImportError):
    EGLConfig = c_void_p
    EGLContext = c_void_p
    EGLDisplay = c_void_p
    EGLSurface = c_void_p
EGLenum = ctypes.c_uint

from ..array_field import array_field_helper, ArrayFieldParamType, next_field_helper
from ..enums import EnumBase, FlagBase, Result, StructureType
from ..typedefs import *
from ..version import Version
from ..exception import check_result
from ..functions import get_instance_proc_addr


# Forward declaration of a Wayland structure
class wl_display(Structure):
    pass
    

# Forward declaration of an Android structure
class AIBinder(Structure):
    pass


class timespec(Structure):
    _fields_ = [
        ("tv_sec", c_longlong),  # TODO: is this the correct type?
        ("tv_nsec", c_long),
    ]
    

class _HandleBase(Structure):
    pass


VkInstance = POINTER(_HandleBase)
VkDevice = POINTER(_HandleBase)
VkImage = POINTER(_HandleBase)
VkPhysicalDevice = POINTER(_HandleBase)
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
KHR_opengl_enable = 1
KHR_opengl_enable_SPEC_VERSION = 11
KHR_OPENGL_ENABLE_EXTENSION_NAME = "XR_KHR_opengl_enable"
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


def set_android_application_thread_khr(
    session: Session,
    thread_type: AndroidThreadTypeKHR,
    thread_id: int,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrSetAndroidApplicationThreadKHR"),
        PFN_xrSetAndroidApplicationThreadKHR,
    )
    result = check_result(fxn(
        session,
        thread_type,
        thread_id,
    ))
    if result.is_exception():
        raise result


PFN_xrCreateSwapchainAndroidSurfaceKHR = CFUNCTYPE(Result.ctype(), Session, POINTER(SwapchainCreateInfo), POINTER(Swapchain), POINTER(c_int))


def create_swapchain_android_surface_khr(
    session: Session,
    info: POINTER(SwapchainCreateInfo),
) -> (Swapchain, int):
    swapchain = Swapchain()
    surface = c_int()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrCreateSwapchainAndroidSurfaceKHR"),
        PFN_xrCreateSwapchainAndroidSurfaceKHR,
    )
    result = check_result(fxn(
        session,
        info,
        byref(swapchain),
        byref(surface),
    ))
    if result.is_exception():
        raise result
    return swapchain, surface


class InstanceCreateInfoAndroidKHR(Structure):
    def __init__(
        self,
        application_vm: c_void_p = None,
        application_activity: c_void_p = None,
        next=None,
        type: StructureType = StructureType.INSTANCE_CREATE_INFO_ANDROID_KHR,
    ) -> None:
        super().__init__(
            application_vm=application_vm,
            application_activity=application_activity,
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.InstanceCreateInfoAndroidKHR(application_vm={repr(self.application_vm)}, application_activity={repr(self.application_activity)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.InstanceCreateInfoAndroidKHR(application_vm={self.application_vm}, application_activity={self.application_activity}, next={self._next}, type={self.type})"

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
        ("application_vm", c_void_p),
        ("application_activity", c_void_p),
    ]


class VulkanSwapchainFormatListCreateInfoKHR(Structure):
    def __init__(
        self,
        view_format_count: Optional[int] = None,
        view_formats: ArrayFieldParamType[c_int] = None,
        next=None,
        type: StructureType = StructureType.VULKAN_SWAPCHAIN_FORMAT_LIST_CREATE_INFO_KHR,
    ) -> None:
        view_format_count, view_formats = array_field_helper(
            c_int, view_format_count, view_formats)
        super().__init__(
            view_format_count=view_format_count,
            _view_formats=view_formats,
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.VulkanSwapchainFormatListCreateInfoKHR(view_format_count={repr(self.view_format_count)}, view_formats={repr(self._view_formats)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.VulkanSwapchainFormatListCreateInfoKHR(view_format_count={self.view_format_count}, view_formats={self._view_formats}, next={self._next}, type={self.type})"

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

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
        ("view_format_count", c_uint32),
        ("_view_formats", POINTER(c_int)),
    ]


class GraphicsBindingOpenGLXlibKHR(Structure):
    def __init__(
        self,
        x_display: POINTER(GLX.Display) = None,
        visualid: int = 0,
        glx_fbconfig: GLX.GLXFBConfig = None,
        glx_drawable: GLX.GLXDrawable = 0,
        glx_context: GLX.GLXContext = None,
        next=None,
        type: StructureType = StructureType.GRAPHICS_BINDING_OPENGL_XLIB_KHR,
    ) -> None:
        super().__init__(
            x_display=x_display,
            visualid=visualid,
            glx_fbconfig=glx_fbconfig,
            glx_drawable=glx_drawable,
            glx_context=glx_context,
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.GraphicsBindingOpenGLXlibKHR(x_display={repr(self.x_display)}, visualid={repr(self.visualid)}, glx_fbconfig={repr(self.glx_fbconfig)}, glx_drawable={repr(self.glx_drawable)}, glx_context={repr(self.glx_context)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.GraphicsBindingOpenGLXlibKHR(x_display={self.x_display}, visualid={self.visualid}, glx_fbconfig={self.glx_fbconfig}, glx_drawable={self.glx_drawable}, glx_context={self.glx_context}, next={self._next}, type={self.type})"

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
        ("x_display", POINTER(GLX.Display)),
        ("visualid", c_uint32),
        ("glx_fbconfig", GLX.GLXFBConfig),
        ("glx_drawable", GLX.GLXDrawable),
        ("glx_context", GLX.GLXContext),
    ]


class GraphicsBindingOpenGLXcbKHR(Structure):
    def __init__(
        self,
        connection: POINTER(c_int) = None,
        screen_number: int = 0,
        fbconfigid: int = 0,
        visualid: int = 0,
        glx_drawable: int = 0,
        glx_context: int = 0,
        next=None,
        type: StructureType = StructureType.GRAPHICS_BINDING_OPENGL_XCB_KHR,
    ) -> None:
        super().__init__(
            connection=connection,
            screen_number=screen_number,
            fbconfigid=fbconfigid,
            visualid=visualid,
            glx_drawable=glx_drawable,
            glx_context=glx_context,
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.GraphicsBindingOpenGLXcbKHR(connection={repr(self.connection)}, screen_number={repr(self.screen_number)}, fbconfigid={repr(self.fbconfigid)}, visualid={repr(self.visualid)}, glx_drawable={repr(self.glx_drawable)}, glx_context={repr(self.glx_context)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.GraphicsBindingOpenGLXcbKHR(connection={self.connection}, screen_number={self.screen_number}, fbconfigid={self.fbconfigid}, visualid={self.visualid}, glx_drawable={self.glx_drawable}, glx_context={self.glx_context}, next={self._next}, type={self.type})"

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
        ("connection", POINTER(c_int)),
        ("screen_number", c_uint32),
        ("fbconfigid", c_int),
        ("visualid", c_int),
        ("glx_drawable", c_int),
        ("glx_context", c_int),
    ]


class GraphicsBindingOpenGLWaylandKHR(Structure):
    def __init__(
        self,
        display: POINTER(wl_display) = None,
        next=None,
        type: StructureType = StructureType.GRAPHICS_BINDING_OPENGL_WAYLAND_KHR,
    ) -> None:
        super().__init__(
            display=display,
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.GraphicsBindingOpenGLWaylandKHR(display={repr(self.display)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.GraphicsBindingOpenGLWaylandKHR(display={self.display}, next={self._next}, type={self.type})"

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
        ("display", POINTER(wl_display)),
    ]


class SwapchainImageOpenGLKHR(Structure):
    def __init__(
        self,
        image: int = 0,
        next=None,
        type: StructureType = StructureType.SWAPCHAIN_IMAGE_OPENGL_KHR,
    ) -> None:
        super().__init__(
            image=image,
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainImageOpenGLKHR(image={repr(self.image)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageOpenGLKHR(image={self.image}, next={self._next}, type={self.type})"

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
        ("image", c_uint32),
    ]


class GraphicsRequirementsOpenGLKHR(Structure):
    def __init__(
        self,
        min_api_version_supported: Version = Version(),
        max_api_version_supported: Version = Version(),
        next=None,
        type: StructureType = StructureType.GRAPHICS_REQUIREMENTS_OPENGL_KHR,
    ) -> None:
        super().__init__(
            _min_api_version_supported=min_api_version_supported.number(),
            _max_api_version_supported=max_api_version_supported.number(),
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.GraphicsRequirementsOpenGLKHR(min_api_version_supported={repr(self._min_api_version_supported)}, max_api_version_supported={repr(self._max_api_version_supported)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.GraphicsRequirementsOpenGLKHR(min_api_version_supported={self._min_api_version_supported}, max_api_version_supported={self._max_api_version_supported}, next={self._next}, type={self.type})"

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

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
        ("_min_api_version_supported", VersionNumber),
        ("_max_api_version_supported", VersionNumber),
    ]


PFN_xrGetOpenGLGraphicsRequirementsKHR = CFUNCTYPE(Result.ctype(), Instance, SystemId, POINTER(GraphicsRequirementsOpenGLKHR))


def get_opengl_graphics_requirements_khr(
    instance: Instance,
    system_id: SystemId,
) -> GraphicsRequirementsOpenGLKHR:
    graphics_requirements = GraphicsRequirementsOpenGLKHR()
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrGetOpenGLGraphicsRequirementsKHR"),
        PFN_xrGetOpenGLGraphicsRequirementsKHR,
    )
    result = check_result(fxn(
        instance,
        system_id,
        byref(graphics_requirements),
    ))
    if result.is_exception():
        raise result
    return graphics_requirements


class GraphicsBindingOpenGLESAndroidKHR(Structure):
    def __init__(
        self,
        display: EGLDisplay = 0,
        config: EGLConfig = 0,
        context: EGLContext = 0,
        next=None,
        type: StructureType = StructureType.GRAPHICS_BINDING_OPENGL_ES_ANDROID_KHR,
    ) -> None:
        super().__init__(
            display=display,
            config=config,
            context=context,
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.GraphicsBindingOpenGLESAndroidKHR(display={repr(self.display)}, config={repr(self.config)}, context={repr(self.context)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.GraphicsBindingOpenGLESAndroidKHR(display={self.display}, config={self.config}, context={self.context}, next={self._next}, type={self.type})"

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
        ("display", EGLDisplay),
        ("config", EGLConfig),
        ("context", EGLContext),
    ]


class SwapchainImageOpenGLESKHR(Structure):
    def __init__(
        self,
        image: int = 0,
        next=None,
        type: StructureType = StructureType.SWAPCHAIN_IMAGE_OPENGL_ES_KHR,
    ) -> None:
        super().__init__(
            image=image,
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainImageOpenGLESKHR(image={repr(self.image)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageOpenGLESKHR(image={self.image}, next={self._next}, type={self.type})"

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
        ("image", c_uint32),
    ]


class GraphicsRequirementsOpenGLESKHR(Structure):
    def __init__(
        self,
        min_api_version_supported: Version = Version(),
        max_api_version_supported: Version = Version(),
        next=None,
        type: StructureType = StructureType.GRAPHICS_REQUIREMENTS_OPENGL_ES_KHR,
    ) -> None:
        super().__init__(
            _min_api_version_supported=min_api_version_supported.number(),
            _max_api_version_supported=max_api_version_supported.number(),
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.GraphicsRequirementsOpenGLESKHR(min_api_version_supported={repr(self._min_api_version_supported)}, max_api_version_supported={repr(self._max_api_version_supported)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.GraphicsRequirementsOpenGLESKHR(min_api_version_supported={self._min_api_version_supported}, max_api_version_supported={self._max_api_version_supported}, next={self._next}, type={self.type})"

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

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
        ("_min_api_version_supported", VersionNumber),
        ("_max_api_version_supported", VersionNumber),
    ]


PFN_xrGetOpenGLESGraphicsRequirementsKHR = CFUNCTYPE(Result.ctype(), Instance, SystemId, POINTER(GraphicsRequirementsOpenGLESKHR))


def get_opengl_es_graphics_requirements_khr(
    instance: Instance,
    system_id: SystemId,
) -> GraphicsRequirementsOpenGLESKHR:
    graphics_requirements = GraphicsRequirementsOpenGLESKHR()
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrGetOpenGLESGraphicsRequirementsKHR"),
        PFN_xrGetOpenGLESGraphicsRequirementsKHR,
    )
    result = check_result(fxn(
        instance,
        system_id,
        byref(graphics_requirements),
    ))
    if result.is_exception():
        raise result
    return graphics_requirements


class GraphicsBindingVulkanKHR(Structure):
    def __init__(
        self,
        instance: VkInstance = None,
        physical_device: VkPhysicalDevice = None,
        device: VkDevice = None,
        queue_family_index: int = 0,
        queue_index: int = 0,
        next=None,
        type: StructureType = StructureType.GRAPHICS_BINDING_VULKAN_KHR,
    ) -> None:
        super().__init__(
            instance=instance,
            physical_device=physical_device,
            device=device,
            queue_family_index=queue_family_index,
            queue_index=queue_index,
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.GraphicsBindingVulkanKHR(instance={repr(self.instance)}, physical_device={repr(self.physical_device)}, device={repr(self.device)}, queue_family_index={repr(self.queue_family_index)}, queue_index={repr(self.queue_index)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.GraphicsBindingVulkanKHR(instance={self.instance}, physical_device={self.physical_device}, device={self.device}, queue_family_index={self.queue_family_index}, queue_index={self.queue_index}, next={self._next}, type={self.type})"

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
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
        next=None,
        type: StructureType = StructureType.SWAPCHAIN_IMAGE_VULKAN_KHR,
    ) -> None:
        super().__init__(
            image=image,
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainImageVulkanKHR(image={repr(self.image)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageVulkanKHR(image={self.image}, next={self._next}, type={self.type})"

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
        ("image", VkImage),
    ]


class GraphicsRequirementsVulkanKHR(Structure):
    def __init__(
        self,
        min_api_version_supported: Version = Version(),
        max_api_version_supported: Version = Version(),
        next=None,
        type: StructureType = StructureType.GRAPHICS_REQUIREMENTS_VULKAN_KHR,
    ) -> None:
        super().__init__(
            _min_api_version_supported=min_api_version_supported.number(),
            _max_api_version_supported=max_api_version_supported.number(),
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.GraphicsRequirementsVulkanKHR(min_api_version_supported={repr(self._min_api_version_supported)}, max_api_version_supported={repr(self._max_api_version_supported)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.GraphicsRequirementsVulkanKHR(min_api_version_supported={self._min_api_version_supported}, max_api_version_supported={self._max_api_version_supported}, next={self._next}, type={self.type})"

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

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
        ("_min_api_version_supported", VersionNumber),
        ("_max_api_version_supported", VersionNumber),
    ]


PFN_xrGetVulkanInstanceExtensionsKHR = CFUNCTYPE(Result.ctype(), Instance, SystemId, c_uint32, POINTER(c_uint32), c_char_p)


def get_vulkan_instance_extensions_khr(
    instance: Instance,
    system_id: SystemId,
) -> str:
    buffer_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrGetVulkanInstanceExtensionsKHR"),
        PFN_xrGetVulkanInstanceExtensionsKHR,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        instance,
        system_id,
        0,
        byref(buffer_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    buffer = create_string_buffer(buffer_capacity_input)
    result = check_result(fxn(
        instance,
        system_id,
        buffer_capacity_input,
        byref(buffer_capacity_input),
        buffer,
    ))
    if result.is_exception():
        raise result
    return buffer.decode()


PFN_xrGetVulkanDeviceExtensionsKHR = CFUNCTYPE(Result.ctype(), Instance, SystemId, c_uint32, POINTER(c_uint32), c_char_p)


def get_vulkan_device_extensions_khr(
    instance: Instance,
    system_id: SystemId,
) -> str:
    buffer_capacity_input = c_uint32(0)
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrGetVulkanDeviceExtensionsKHR"),
        PFN_xrGetVulkanDeviceExtensionsKHR,
    )
    # First call of two, to retrieve buffer sizes
    result = check_result(fxn(
        instance,
        system_id,
        0,
        byref(buffer_capacity_input),
        None,
    ))
    if result.is_exception():
        raise result
    buffer = create_string_buffer(buffer_capacity_input)
    result = check_result(fxn(
        instance,
        system_id,
        buffer_capacity_input,
        byref(buffer_capacity_input),
        buffer,
    ))
    if result.is_exception():
        raise result
    return buffer.decode()


PFN_xrGetVulkanGraphicsDeviceKHR = CFUNCTYPE(Result.ctype(), Instance, SystemId, VkInstance, POINTER(VkPhysicalDevice))


def get_vulkan_graphics_device_khr(
    instance: Instance,
    system_id: SystemId,
    vk_instance: VkInstance,
) -> VkPhysicalDevice:
    vk_physical_device = VkPhysicalDevice()
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrGetVulkanGraphicsDeviceKHR"),
        PFN_xrGetVulkanGraphicsDeviceKHR,
    )
    result = check_result(fxn(
        instance,
        system_id,
        vk_instance,
        byref(vk_physical_device),
    ))
    if result.is_exception():
        raise result
    return vk_physical_device


PFN_xrGetVulkanGraphicsRequirementsKHR = CFUNCTYPE(Result.ctype(), Instance, SystemId, POINTER(GraphicsRequirementsVulkanKHR))


def get_vulkan_graphics_requirements_khr(
    instance: Instance,
    system_id: SystemId,
) -> GraphicsRequirementsVulkanKHR:
    graphics_requirements = GraphicsRequirementsVulkanKHR()
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrGetVulkanGraphicsRequirementsKHR"),
        PFN_xrGetVulkanGraphicsRequirementsKHR,
    )
    result = check_result(fxn(
        instance,
        system_id,
        byref(graphics_requirements),
    ))
    if result.is_exception():
        raise result
    return graphics_requirements


PFN_xrConvertTimespecTimeToTimeKHR = CFUNCTYPE(Result.ctype(), Instance, POINTER(timespec), POINTER(Time))


def convert_timespec_time_to_time_khr(
    instance: Instance,
    timespec_time: timespec,
) -> Time:
    time = Time()
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrConvertTimespecTimeToTimeKHR"),
        PFN_xrConvertTimespecTimeToTimeKHR,
    )
    result = check_result(fxn(
        instance,
        timespec_time,
        byref(time),
    ))
    if result.is_exception():
        raise result
    return time


PFN_xrConvertTimeToTimespecTimeKHR = CFUNCTYPE(Result.ctype(), Instance, Time, POINTER(timespec))


def convert_time_to_timespec_time_khr(
    instance: Instance,
    time: Time,
) -> timespec:
    timespec_time = timespec()
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrConvertTimeToTimespecTimeKHR"),
        PFN_xrConvertTimeToTimespecTimeKHR,
    )
    result = check_result(fxn(
        instance,
        time,
        byref(timespec_time),
    ))
    if result.is_exception():
        raise result
    return timespec_time


class LoaderInitInfoAndroidKHR(Structure):
    def __init__(
        self,
        application_vm: c_void_p = None,
        application_context: c_void_p = None,
        next=None,
        type: StructureType = StructureType.LOADER_INIT_INFO_ANDROID_KHR,
    ) -> None:
        super().__init__(
            application_vm=application_vm,
            application_context=application_context,
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.LoaderInitInfoAndroidKHR(application_vm={repr(self.application_vm)}, application_context={repr(self.application_context)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.LoaderInitInfoAndroidKHR(application_vm={self.application_vm}, application_context={self.application_context}, next={self._next}, type={self.type})"

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
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
        next=None,
        type: StructureType = StructureType.VULKAN_INSTANCE_CREATE_INFO_KHR,
    ) -> None:
        super().__init__(
            system_id=system_id,
            create_flags=VulkanInstanceCreateFlagsKHR(create_flags),
            pfn_get_instance_proc_addr=pfn_get_instance_proc_addr,
            vulkan_create_info=vulkan_create_info,
            vulkan_allocator=vulkan_allocator,
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.VulkanInstanceCreateInfoKHR(system_id={repr(self.system_id)}, create_flags={repr(self.create_flags)}, pfn_get_instance_proc_addr={repr(self.pfn_get_instance_proc_addr)}, vulkan_create_info={repr(self.vulkan_create_info)}, vulkan_allocator={repr(self.vulkan_allocator)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.VulkanInstanceCreateInfoKHR(system_id={self.system_id}, create_flags={self.create_flags}, pfn_get_instance_proc_addr={self.pfn_get_instance_proc_addr}, vulkan_create_info={self.vulkan_create_info}, vulkan_allocator={self.vulkan_allocator}, next={self._next}, type={self.type})"

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
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
        next=None,
        type: StructureType = StructureType.VULKAN_DEVICE_CREATE_INFO_KHR,
    ) -> None:
        super().__init__(
            system_id=system_id,
            create_flags=VulkanDeviceCreateFlagsKHR(create_flags),
            pfn_get_instance_proc_addr=pfn_get_instance_proc_addr,
            vulkan_physical_device=vulkan_physical_device,
            vulkan_create_info=vulkan_create_info,
            vulkan_allocator=vulkan_allocator,
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.VulkanDeviceCreateInfoKHR(system_id={repr(self.system_id)}, create_flags={repr(self.create_flags)}, pfn_get_instance_proc_addr={repr(self.pfn_get_instance_proc_addr)}, vulkan_physical_device={repr(self.vulkan_physical_device)}, vulkan_create_info={repr(self.vulkan_create_info)}, vulkan_allocator={repr(self.vulkan_allocator)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.VulkanDeviceCreateInfoKHR(system_id={self.system_id}, create_flags={self.create_flags}, pfn_get_instance_proc_addr={self.pfn_get_instance_proc_addr}, vulkan_physical_device={self.vulkan_physical_device}, vulkan_create_info={self.vulkan_create_info}, vulkan_allocator={self.vulkan_allocator}, next={self._next}, type={self.type})"

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
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
        next=None,
        type: StructureType = StructureType.VULKAN_GRAPHICS_DEVICE_GET_INFO_KHR,
    ) -> None:
        super().__init__(
            system_id=system_id,
            vulkan_instance=vulkan_instance,
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.VulkanGraphicsDeviceGetInfoKHR(system_id={repr(self.system_id)}, vulkan_instance={repr(self.vulkan_instance)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.VulkanGraphicsDeviceGetInfoKHR(system_id={self.system_id}, vulkan_instance={self.vulkan_instance}, next={self._next}, type={self.type})"

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
        ("system_id", SystemId),
        ("vulkan_instance", VkInstance),
    ]


SwapchainImageVulkan2KHR = SwapchainImageVulkanKHR

GraphicsRequirementsVulkan2KHR = GraphicsRequirementsVulkanKHR

PFN_xrCreateVulkanInstanceKHR = CFUNCTYPE(Result.ctype(), Instance, POINTER(VulkanInstanceCreateInfoKHR), POINTER(VkInstance), POINTER(c_int))


def create_vulkan_instance_khr(
    instance: Instance,
    create_info: VulkanInstanceCreateInfoKHR = None,
) -> (VkInstance, c_int):
    if create_info is None:
        create_info = VulkanInstanceCreateInfoKHR()
    vulkan_instance = VkInstance()
    vulkan_result = c_int()
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrCreateVulkanInstanceKHR"),
        PFN_xrCreateVulkanInstanceKHR,
    )
    result = check_result(fxn(
        instance,
        create_info,
        byref(vulkan_instance),
        byref(vulkan_result),
    ))
    if result.is_exception():
        raise result
    return vulkan_instance, vulkan_result


PFN_xrCreateVulkanDeviceKHR = CFUNCTYPE(Result.ctype(), Instance, POINTER(VulkanDeviceCreateInfoKHR), POINTER(VkDevice), POINTER(c_int))


def create_vulkan_device_khr(
    instance: Instance,
    create_info: VulkanDeviceCreateInfoKHR = None,
) -> (VkDevice, c_int):
    if create_info is None:
        create_info = VulkanDeviceCreateInfoKHR()
    vulkan_device = VkDevice()
    vulkan_result = c_int()
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrCreateVulkanDeviceKHR"),
        PFN_xrCreateVulkanDeviceKHR,
    )
    result = check_result(fxn(
        instance,
        create_info,
        byref(vulkan_device),
        byref(vulkan_result),
    ))
    if result.is_exception():
        raise result
    return vulkan_device, vulkan_result


PFN_xrGetVulkanGraphicsDevice2KHR = CFUNCTYPE(Result.ctype(), Instance, POINTER(VulkanGraphicsDeviceGetInfoKHR), POINTER(VkPhysicalDevice))


def get_vulkan_graphics_device2_khr(
    instance: Instance,
    get_info: VulkanGraphicsDeviceGetInfoKHR,
) -> VkPhysicalDevice:
    vulkan_physical_device = VkPhysicalDevice()
    fxn = cast(
        get_instance_proc_addr(instance.instance, "xrGetVulkanGraphicsDevice2KHR"),
        PFN_xrGetVulkanGraphicsDevice2KHR,
    )
    result = check_result(fxn(
        instance,
        get_info,
        byref(vulkan_physical_device),
    ))
    if result.is_exception():
        raise result
    return vulkan_physical_device


PFN_xrGetVulkanGraphicsRequirements2KHR = CFUNCTYPE(Result.ctype(), Instance, SystemId, POINTER(GraphicsRequirementsVulkanKHR))

PFN_xrEglGetProcAddressMNDX = CFUNCTYPE(PFN_xrVoidFunction, c_char_p)


class GraphicsBindingEGLMNDX(Structure):
    def __init__(
        self,
        get_proc_address: PFN_xrEglGetProcAddressMNDX = cast(None, PFN_xrEglGetProcAddressMNDX),
        display: EGLDisplay = None,
        config: EGLConfig = None,
        context: EGLContext = None,
        next=None,
        type: StructureType = StructureType.GRAPHICS_BINDING_EGL_MNDX,
    ) -> None:
        super().__init__(
            get_proc_address=get_proc_address,
            display=display,
            config=config,
            context=context,
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.GraphicsBindingEGLMNDX(get_proc_address={repr(self.get_proc_address)}, display={repr(self.display)}, config={repr(self.config)}, context={repr(self.context)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.GraphicsBindingEGLMNDX(get_proc_address={self.get_proc_address}, display={self.display}, config={self.config}, context={self.context}, next={self._next}, type={self.type})"

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
        ("get_proc_address", PFN_xrEglGetProcAddressMNDX),
        ("display", EGLDisplay),
        ("config", EGLConfig),
        ("context", EGLContext),
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
        next=None,
        type: StructureType = StructureType.ANDROID_SURFACE_SWAPCHAIN_CREATE_INFO_FB,
    ) -> None:
        super().__init__(
            create_flags=AndroidSurfaceSwapchainFlagsFB(create_flags),
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.AndroidSurfaceSwapchainCreateInfoFB(create_flags={repr(self.create_flags)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.AndroidSurfaceSwapchainCreateInfoFB(create_flags={self.create_flags}, next={self._next}, type={self.type})"

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
        ("create_flags", AndroidSurfaceSwapchainFlagsFBCInt),
    ]


class SwapchainImageFoveationVulkanFB(Structure):
    def __init__(
        self,
        image: VkImage = None,
        width: int = 0,
        height: int = 0,
        next=None,
        type: StructureType = StructureType.SWAPCHAIN_IMAGE_FOVEATION_VULKAN_FB,
    ) -> None:
        super().__init__(
            image=image,
            width=width,
            height=height,
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainImageFoveationVulkanFB(image={repr(self.image)}, width={repr(self.width)}, height={repr(self.height)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainImageFoveationVulkanFB(image={self.image}, width={self.width}, height={self.height}, next={self._next}, type={self.type})"

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
        ("image", VkImage),
        ("width", c_uint32),
        ("height", c_uint32),
    ]


class SwapchainStateAndroidSurfaceDimensionsFB(Structure):
    def __init__(
        self,
        width: int = 0,
        height: int = 0,
        next=None,
        type: StructureType = StructureType.SWAPCHAIN_STATE_ANDROID_SURFACE_DIMENSIONS_FB,
    ) -> None:
        super().__init__(
            width=width,
            height=height,
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainStateAndroidSurfaceDimensionsFB(width={repr(self.width)}, height={repr(self.height)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainStateAndroidSurfaceDimensionsFB(width={self.width}, height={self.height}, next={self._next}, type={self.type})"

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
        ("width", c_uint32),
        ("height", c_uint32),
    ]


class SwapchainStateSamplerOpenGLESFB(Structure):
    def __init__(
        self,
        min_filter: EGLenum = 0,
        mag_filter: EGLenum = 0,
        wrap_mode_s: EGLenum = 0,
        wrap_mode_t: EGLenum = 0,
        swizzle_red: EGLenum = 0,
        swizzle_green: EGLenum = 0,
        swizzle_blue: EGLenum = 0,
        swizzle_alpha: EGLenum = 0,
        max_anisotropy: float = 0,
        border_color: Color4f = None,
        next=None,
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
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainStateSamplerOpenGLESFB(min_filter={repr(self.min_filter)}, mag_filter={repr(self.mag_filter)}, wrap_mode_s={repr(self.wrap_mode_s)}, wrap_mode_t={repr(self.wrap_mode_t)}, swizzle_red={repr(self.swizzle_red)}, swizzle_green={repr(self.swizzle_green)}, swizzle_blue={repr(self.swizzle_blue)}, swizzle_alpha={repr(self.swizzle_alpha)}, max_anisotropy={repr(self.max_anisotropy)}, border_color={repr(self.border_color)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainStateSamplerOpenGLESFB(min_filter={self.min_filter}, mag_filter={self.mag_filter}, wrap_mode_s={self.wrap_mode_s}, wrap_mode_t={self.wrap_mode_t}, swizzle_red={self.swizzle_red}, swizzle_green={self.swizzle_green}, swizzle_blue={self.swizzle_blue}, swizzle_alpha={self.swizzle_alpha}, max_anisotropy={self.max_anisotropy:.3f}, border_color={self.border_color}, next={self._next}, type={self.type})"

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
        ("min_filter", EGLenum),
        ("mag_filter", EGLenum),
        ("wrap_mode_s", EGLenum),
        ("wrap_mode_t", EGLenum),
        ("swizzle_red", EGLenum),
        ("swizzle_green", EGLenum),
        ("swizzle_blue", EGLenum),
        ("swizzle_alpha", EGLenum),
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
        next=None,
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
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SwapchainStateSamplerVulkanFB(min_filter={repr(self.min_filter)}, mag_filter={repr(self.mag_filter)}, mipmap_mode={repr(self.mipmap_mode)}, wrap_mode_s={repr(self.wrap_mode_s)}, wrap_mode_t={repr(self.wrap_mode_t)}, swizzle_red={repr(self.swizzle_red)}, swizzle_green={repr(self.swizzle_green)}, swizzle_blue={repr(self.swizzle_blue)}, swizzle_alpha={repr(self.swizzle_alpha)}, max_anisotropy={repr(self.max_anisotropy)}, border_color={repr(self.border_color)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SwapchainStateSamplerVulkanFB(min_filter={self.min_filter}, mag_filter={self.mag_filter}, mipmap_mode={self.mipmap_mode}, wrap_mode_s={self.wrap_mode_s}, wrap_mode_t={self.wrap_mode_t}, swizzle_red={self.swizzle_red}, swizzle_green={self.swizzle_green}, swizzle_blue={self.swizzle_blue}, swizzle_alpha={self.swizzle_alpha}, max_anisotropy={self.max_anisotropy:.3f}, border_color={self.border_color}, next={self._next}, type={self.type})"

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
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
        next=None,
        type: StructureType = StructureType.VULKAN_SWAPCHAIN_CREATE_INFO_META,
    ) -> None:
        super().__init__(
            additional_create_flags=additional_create_flags,
            additional_usage_flags=additional_usage_flags,
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.VulkanSwapchainCreateInfoMETA(additional_create_flags={repr(self.additional_create_flags)}, additional_usage_flags={repr(self.additional_usage_flags)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.VulkanSwapchainCreateInfoMETA(additional_create_flags={self.additional_create_flags}, additional_usage_flags={self.additional_usage_flags}, next={self._next}, type={self.type})"

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
        ("additional_create_flags", c_uint32),
        ("additional_usage_flags", c_uint32),
    ]


class AnchorSharingInfoANDROID(Structure):
    def __init__(
        self,
        anchor: Space = None,
        next=None,
        type: StructureType = StructureType.ANCHOR_SHARING_INFO_ANDROID,
    ) -> None:
        super().__init__(
            anchor=anchor,
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.AnchorSharingInfoANDROID(anchor={repr(self.anchor)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.AnchorSharingInfoANDROID(anchor={self.anchor}, next={self._next}, type={self.type})"

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
        ("anchor", Space),
    ]


class AnchorSharingTokenANDROID(Structure):
    def __init__(
        self,
        token: POINTER(AIBinder) = None,
        next=None,
        type: StructureType = StructureType.ANCHOR_SHARING_TOKEN_ANDROID,
    ) -> None:
        super().__init__(
            token=token,
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.AnchorSharingTokenANDROID(token={repr(self.token)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.AnchorSharingTokenANDROID(token={self.token}, next={self._next}, type={self.type})"

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
        ("token", POINTER(AIBinder)),
    ]


class SystemAnchorSharingExportPropertiesANDROID(Structure):
    def __init__(
        self,
        supports_anchor_sharing_export: Bool32 = 0,
        next=None,
        type: StructureType = StructureType.SYSTEM_ANCHOR_SHARING_EXPORT_PROPERTIES_ANDROID,
    ) -> None:
        super().__init__(
            supports_anchor_sharing_export=supports_anchor_sharing_export,
            _next=next_field_helper(next),
            type=type,
        )

    def __repr__(self) -> str:
        return f"xr.SystemAnchorSharingExportPropertiesANDROID(supports_anchor_sharing_export={repr(self.supports_anchor_sharing_export)}, next={repr(self._next)}, type={repr(self.type)})"

    def __str__(self) -> str:
        return f"xr.SystemAnchorSharingExportPropertiesANDROID(supports_anchor_sharing_export={self.supports_anchor_sharing_export}, next={self._next}, type={self.type})"

    @property
    def next(self) -> c_void_p:
        return self._next
    
    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("type", StructureType.ctype()),
        ("_next", c_void_p),
        ("supports_anchor_sharing_export", Bool32),
    ]


PFN_xrShareAnchorANDROID = CFUNCTYPE(Result.ctype(), Session, POINTER(AnchorSharingInfoANDROID), POINTER(AnchorSharingTokenANDROID))


def share_anchor_android(
    session: Session,
    sharing_info: POINTER(AnchorSharingInfoANDROID),
) -> AnchorSharingTokenANDROID:
    anchor_token = AnchorSharingTokenANDROID()
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrShareAnchorANDROID"),
        PFN_xrShareAnchorANDROID,
    )
    result = check_result(fxn(
        session,
        sharing_info,
        byref(anchor_token),
    ))
    if result.is_exception():
        raise result
    return anchor_token


PFN_xrUnshareAnchorANDROID = CFUNCTYPE(Result.ctype(), Session, Space)


def unshare_anchor_android(
    session: Session,
    anchor: Space,
) -> None:
    fxn = cast(
        get_instance_proc_addr(session.instance, "xrUnshareAnchorANDROID"),
        PFN_xrUnshareAnchorANDROID,
    )
    result = check_result(fxn(
        session,
        anchor,
    ))
    if result.is_exception():
        raise result


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
    "GraphicsBindingOpenGLWaylandKHR",
    "GraphicsBindingOpenGLXcbKHR",
    "GraphicsBindingOpenGLXlibKHR",
    "GraphicsBindingVulkan2KHR",
    "GraphicsBindingVulkanKHR",
    "GraphicsRequirementsOpenGLESKHR",
    "GraphicsRequirementsOpenGLKHR",
    "GraphicsRequirementsVulkan2KHR",
    "GraphicsRequirementsVulkanKHR",
    "InstanceCreateInfoAndroidKHR",
    "KHR_ANDROID_CREATE_INSTANCE_EXTENSION_NAME",
    "KHR_ANDROID_SURFACE_SWAPCHAIN_EXTENSION_NAME",
    "KHR_ANDROID_THREAD_SETTINGS_EXTENSION_NAME",
    "KHR_CONVERT_TIMESPEC_TIME_EXTENSION_NAME",
    "KHR_LOADER_INIT_ANDROID_EXTENSION_NAME",
    "KHR_OPENGL_ENABLE_EXTENSION_NAME",
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
    "KHR_opengl_enable",
    "KHR_opengl_enable_SPEC_VERSION",
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
    "PFN_xrGetOpenGLGraphicsRequirementsKHR",
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
    "SwapchainImageOpenGLKHR",
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
    "convert_time_to_timespec_time_khr",
    "convert_timespec_time_to_time_khr",
    "create_swapchain_android_surface_khr",
    "create_vulkan_device_khr",
    "create_vulkan_instance_khr",
    "get_opengl_es_graphics_requirements_khr",
    "get_opengl_graphics_requirements_khr",
    "get_vulkan_device_extensions_khr",
    "get_vulkan_graphics_device2_khr",
    "get_vulkan_graphics_device_khr",
    "get_vulkan_graphics_requirements_khr",
    "get_vulkan_instance_extensions_khr",
    "set_android_application_thread_khr",
    "share_anchor_android",
    "timespec",
    "unshare_anchor_android",
]
