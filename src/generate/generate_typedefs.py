# This script creates an updated version of xr/typedefs.py

import inspect
from clang.cindex import CursorKind
import xrg


def main():
    cg = xrg.CodeGenerator(
        [
            CursorKind.STRUCT_DECL,
            CursorKind.TYPEDEF_DECL,
        ]
    )

    cg.ctypes_names.add("addressof")
    cg.ctypes_names.add("byref")
    cg.ctypes_names.add("cast")
    cg.print_header()
    print(inspect.cleandoc("""
        import ctypes
        
        import os
        import sys
        from typing import Generator, Optional
        
        import numpy
        
        from .array_field import *
        from .enums import *
        from .version import *
        from .handle import HandleMixin
    """))

    cg.print_items()
    cg.print_all_list()


if __name__ == "__main__":
    main()
