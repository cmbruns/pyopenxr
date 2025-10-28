# This script creates an updated version of xr/platform/android.py

import inspect

import xrg


def main():
    compiler_args = [
        "-DXR_USE_PLATFORM_EGL",
        "-DXR_USE_PLATFORM_ANDROID",
        "-DXR_USE_GRAPHICS_API_OPENGL_ES",
        "-DXR_USE_GRAPHICS_API_VULKAN",
        "-DXR_USE_TIMESPEC",
        "-DXR_CPP_NULLPTR_SUPPORTED",
    ]
    cg = xrg.CodeGenerator(
        header=xrg.Header.PLATFORM,
        compiler_args=compiler_args,
        header_preamble=inspect.cleandoc("""
            #include <GLES3/gl3.h>              // OpenGL ES 3.x API
            #include <EGL/egl.h>                // EGL core
            #include <vulkan/vulkan.h>
            // #include <android/native_window.h>  // ANativeWindow for swapchain integration
            // #include <android/binder_ibinder.h> // AIBinder definition
        """),
    )
    cg.ctypes_names.add("byref")
    cg.ctypes_names.add("cast")
    cg.ctypes_names.add("create_string_buffer")

    cg.print_header()
    print(inspect.cleandoc("""
        import ctypes
        from typing import Optional

        try:
            from OpenGL.EGL import EGLConfig, EGLContext, EGLDisplay, EGLSurface
        except (AttributeError, ImportError):
            EGLConfig = c_void_p
            EGLContext = c_void_p
            EGLDisplay = c_void_p
            EGLSurface = c_void_p
        EGLenum = ctypes.c_uint

        from ..field_helper import *
        from ..enums import EnumBase, FlagBase, Result, StructureType
        from ..typedefs import *
        from ..version import Version
        from ..exception import check_result
        from ..functions import get_instance_proc_addr
        
        
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
    """))
    print("")
    print("")
    cg.print_items()
    cg.print_all_list()


if __name__ == "__main__":
    main()
