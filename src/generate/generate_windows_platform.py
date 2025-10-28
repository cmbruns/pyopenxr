# This script creates an updated version of xr/platform/windows.py

import inspect

import xrg


def main():
    compiler_args = [
        # On Windows we define EVERYTHING, so that unified docs can be introspected here
        "-DWIN32_LEAN_AND_MEAN",
        "-DXR_USE_PLATFORM_WIN32",
        "-DXR_USE_PLATFORM_EGL",
        "-DXR_USE_PLATFORM_WAYLAND",
        "-DXR_USE_PLATFORM_XCB",
        "-DXR_USE_PLATFORM_XLIB",
        "-DXR_USE_PLATFORM_ANDROID",
        "-DXR_USE_PLATFORM_ML",
        "-DXR_USE_GRAPHICS_API_OPENGL_ES",
        "-DXR_USE_GRAPHICS_API_OPENGL",
        "-DXR_USE_GRAPHICS_API_VULKAN",
        "-DXR_USE_GRAPHICS_API_D3D11",
        "-DXR_USE_GRAPHICS_API_D3D12",
        "-DXR_USE_GRAPHICS_API_METAL",
        "-DXR_USE_TIMESPEC",
        "-DXR_CPP_NULLPTR_SUPPORTED",
    ]
    cg = xrg.CodeGenerator(
        header=xrg.Header.PLATFORM,
        compiler_args=compiler_args,
        header_preamble=inspect.cleandoc("""
            #include <Windows.h>
            #include <EGL/egl.h>
            #include <vulkan/vulkan.h>
        """),
    )
    cg.ctypes_names.add("byref")
    cg.ctypes_names.add("c_ulong")
    cg.ctypes_names.add("c_long")
    cg.ctypes_names.add("c_longlong")
    cg.ctypes_names.add("cast")
    cg.ctypes_names.add("create_string_buffer")

    cg.print_header()
    print(inspect.cleandoc("""
        import ctypes
        from typing import Optional

        from OpenGL import WGL

        try:
            from OpenGL.EGL import EGLConfig, EGLContext, EGLDisplay, EGLSurface
        except (AttributeError, ImportError):
            EGLConfig = c_void_p
            EGLContext = c_void_p
            EGLDisplay = c_void_p
            EGLSurface = c_void_p
        EGLenum = ctypes.c_uint

        from ..field_helper import (
            array_field_helper, 
            ArrayFieldParamType, 
            enum_field_helper,
            next_field_helper,
        )
        from ..base_struct import BaseXrStructure
        from ..enums import EnumBase, FlagBase, Result, StructureType
        from ..typedefs import *
        from ..version import Version
        from ..exception import check_result
        from ..functions import get_instance_proc_addr
        
        
        class _LUID(ctypes.Structure):
            _fields_ = [
                ("low_part", c_ulong),
                ("high_part", c_long),
            ]


        # Forward declaration of a Wayland structure
        class wl_display(Structure):
            pass


        # Forward declaration of an Android structure
        class AIBinder(Structure):
            pass
    

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

                
        _LARGE_INTEGER = c_longlong
    """))
    print("")
    cg.print_items()
    cg.print_all_list()


if __name__ == "__main__":
    main()
