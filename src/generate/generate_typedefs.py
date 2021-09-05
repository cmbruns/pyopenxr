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

    cg.print_header()
    print("from typing import Generator\n")
    print("import numpy\n")
    print("from .enums import *")

    cg.print_items()
    cg.print_all_list()


if __name__ == "__main__":
    main()
