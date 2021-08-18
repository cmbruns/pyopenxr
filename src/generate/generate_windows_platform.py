# This script creates an updated version of xr/platform/windows.py

import inspect

import xrg


def main():
    cg = xrg.CodeGenerator()
    compiler_args = [
        "-DXR_USE_PLATFORM_WIN32",
        "-DXR_USE_GRAPHICS_API_OPENGL",
        "-DXR_USE_GRAPHICS_API_VULKAN",
        "-DXR_USE_GRAPHICS_API_D3D11",
        "-DXR_USE_GRAPHICS_API_D3D12",
        "-DXR_USE_TIMESPEC",
    ]
    print(inspect.cleandoc("""
        from ctypes import c_char_p, c_float, c_int, c_uint32, c_void_p, CFUNCTYPE, POINTER, Structure
        
        from ..enums import *
        from ..typedefs import *
    """))
    print("")
    cg.print_platform_items(compiler_args=compiler_args)
    cg.print_all_platform_list(compiler_args=compiler_args)


if __name__ == "__main__":
    main()
