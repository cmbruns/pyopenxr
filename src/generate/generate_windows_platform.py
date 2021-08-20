# This script creates an updated version of xr/platform/windows.py

import inspect

import xrg


def main():
    compiler_args = [
        "-DXR_USE_PLATFORM_WIN32",
        "-DXR_USE_GRAPHICS_API_OPENGL",
        "-DXR_USE_GRAPHICS_API_VULKAN",
        "-DXR_USE_GRAPHICS_API_D3D11",
        "-DXR_USE_GRAPHICS_API_D3D12",
        "-DXR_USE_TIMESPEC",
    ]
    cg = xrg.CodeGenerator(header=xrg.Header.PLATFORM, compiler_args=compiler_args)

    cg.print_header()
    print(inspect.cleandoc("""
        from ..enums import *
        from ..typedefs import *
    """))
    print("")
    cg.print_items()
    cg.print_all_list()


if __name__ == "__main__":
    main()
