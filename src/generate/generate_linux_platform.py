# This script creates an updated version of xr/platform/windows.py

import inspect

import xrg


def main():
    compiler_args = [
        "-DXR_USE_GRAPHICS_API_OPENGL",
        "-DXR_USE_GRAPHICS_API_VULKAN",
        "-DXR_USE_PLATFORM_EGL",
        "-DXR_USE_PLATFORM_WAYLAND",
        "-DXR_USE_PLATFORM_XCB",
        "-DXR_USE_PLATFORM_XLIB",
        "-DXR_USE_TIMESPEC",
    ]
    cg = xrg.CodeGenerator(
        header=xrg.Header.PLATFORM,
        compiler_args=compiler_args,
        header_preamble=inspect.cleandoc("""
            #include <GL/gl.h>
            #include <GL/glx.h>
            #include <EGL/egl.h>
            #include <EGL/eglext.h>
            #include <EGL/eglplatform.h
        """),
    )

    cg.ctypes_names.add("c_long")
    cg.ctypes_names.add("c_longlong")
    cg.ctypes_names.add("cast")
    cg.ctypes_names.add("c_ulong")
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
            
        from ..array_field import *
        from ..enums import *
        from ..typedefs import *
        from ..version import *


        # Forward declaration of a Wayland structure
        class wl_display(Structure):
            pass
            

        class timespec(Structure):
            _fields_ = [
                ("tv_sec", c_longlong),  # TODO: is this the correct type?
                ("tv_nsec", c_long),
            ]
    """))
    print("\n")
    cg.print_items()
    cg.all_list.add("timespec")
    cg.print_all_list()


if __name__ == "__main__":
    main()
