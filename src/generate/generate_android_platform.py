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
            #include <EGL/eglext.h>             // EGL extensions
            // #include <android/native_window.h>  // ANativeWindow for swapchain integration
            // #include <android/binder_ibinder.h> // AIBinder definition
        """),
    )
    cg.ctypes_names.add("c_ulong")
    cg.ctypes_names.add("cast")

    cg.print_header()
    print(inspect.cleandoc("""
        import ctypes
        from typing import Optional

        from ..array_field import *
        from ..enums import *
        from ..typedefs import *
        from ..version import *
        
        
        # Forward declaration of an Android structure
        class AIBinder(Structure):
            pass
    """))
    print("")
    cg.print_items()
    cg.print_all_list()


if __name__ == "__main__":
    main()
