# This script creates an updated version of xr/platform/windows.py

import inspect

import xrg


def main():
    compiler_args = [
        "-DWIN32_LEAN_AND_MEAN",
        "-DXR_USE_PLATFORM_WIN32",
        "-DXR_USE_GRAPHICS_API_OPENGL",
        "-DXR_USE_GRAPHICS_API_VULKAN",
        "-DXR_USE_GRAPHICS_API_D3D11",
        "-DXR_USE_GRAPHICS_API_D3D12",
        "-DXR_USE_TIMESPEC",
    ]
    cg = xrg.CodeGenerator(
        header=xrg.Header.PLATFORM,
        compiler_args=compiler_args,
        header_preamble=inspect.cleandoc("""
            #include <Windows.h>
        """),
    )
    cg.ctypes_names.add("c_ulong")
    cg.ctypes_names.add("c_long")
    cg.ctypes_names.add("c_longlong")

    cg.print_header()
    print(inspect.cleandoc("""
        import ctypes
        from typing import Optional

        from OpenGL import WGL
        
        from ..array_field import *
        from ..enums import *
        from ..typedefs import *
        from ..version import *

        
        class _LUID(ctypes.Structure):
            _fields_ = [
                ("low_part", c_ulong),
                ("high_part", c_long),
            ]

        
        _LARGE_INTEGER = c_longlong
    """))
    print("")
    cg.print_items()
    cg.print_all_list()


if __name__ == "__main__":
    main()
