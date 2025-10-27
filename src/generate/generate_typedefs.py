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
    cg.ctypes_names.add("py_object")
    cg.print_header()
    print(inspect.cleandoc("""
        import ctypes
        
        import os
        import sys
        from typing import Any, Generator, Optional
        
        import numpy

        from .base_struct import BaseXrStructure
        from .callback import *
        from .enums import *
        from .field_helper import *
        from .handle import HandleMixin
        from .version import *
    """))

    cg.print_items()
    cg.print_all_list()


if __name__ == "__main__":
    main()
