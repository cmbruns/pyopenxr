# This script creates an updated version of xr/typedefs.py

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
    print("import ctypes\n")
    print("import os")
    print("import sys")
    print("from typing import Generator, Sequence\n")
    print("import numpy\n")
    print("from .enums import *")
    print("from .version import *")

    cg.print_items()
    cg.print_all_list()


if __name__ == "__main__":
    main()
