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
        

        # Create a separate class for SystemId,
        # because we will inject methods into it later
        class SystemId(c_uint64):
            def __init__(self, instance: Optional["Instance"], get_info: "SystemGetInfo") -> None:
                # This method will be overwritten at function definition time
                raise NotImplementedError


    """))

    cg.print_items()
    cg.all_list.add("SystemId")
    cg.print_all_list()


if __name__ == "__main__":
    main()
