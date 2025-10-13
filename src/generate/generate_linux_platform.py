# This script creates an updated version of xr/platform/linux.py

import inspect

import xrg


def main():
    compiler_args = [
        "-DXR_USE_PLATFORM_EGL",
        "-DXR_USE_PLATFORM_WAYLAND",
        "-DXR_USE_PLATFORM_XCB",
        "-DXR_USE_PLATFORM_XLIB",
        "-DXR_USE_GRAPHICS_API_OPENGL_ES",
        "-DXR_USE_GRAPHICS_API_OPENGL",
        "-DXR_USE_GRAPHICS_API_VULKAN",
        "-DXR_USE_TIMESPEC",
        "-DXR_CPP_NULLPTR_SUPPORTED",
    ]
    cg = xrg.CodeGenerator(
        header=xrg.Header.PLATFORM,
        compiler_args=compiler_args,
        header_preamble=inspect.cleandoc("""
            #include <GL/gl.h>
            #include <GL/glx.h>
            #include <GLES3/gl3.h>              // OpenGL ES 3.x API
            #include <EGL/egl.h>
            #include <vulkan/vulkan.h>
        """),
    )

    cg.ctypes_names.add("byref")
    cg.ctypes_names.add("c_long")
    cg.ctypes_names.add("c_longlong")
    cg.ctypes_names.add("cast")
    cg.ctypes_names.add("create_string_buffer")
    cg.print_header()
    print("")
    print(inspect.cleandoc("""
        import ctypes
        from typing import Optional

        import OpenGL.platform as _plat
        from OpenGL.platform.glx import GLXPlatform
        if not isinstance(_plat.PLATFORM, GLXPlatform):
            _plat.PLATFORM = GLXPlatform()  # override auto-selection
        from OpenGL import GLX

        try:
            from OpenGL.EGL import EGLConfig, EGLContext, EGLDisplay, EGLSurface, EGLenum
        except (AttributeError, ImportError):
            EGLConfig = c_void_p
            EGLContext = c_void_p
            EGLDisplay = c_void_p
            EGLSurface = c_void_p
            EGLenum = int

        from ..array_field import array_field_helper, ArrayFieldParamType, next_field_helper
        from ..enums import FlagBase, Result, StructureType
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
    """))
    print("\n")
    cg.print_items()
    cg.all_list.add("timespec")
    cg.print_all_list()


if __name__ == "__main__":
    main()
