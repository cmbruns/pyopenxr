# This script creates an updated version of xr/enums.py

from clang.cindex import CursorKind

import xrg


def main():
    cg = xrg.CodeGenerator(
        [
            CursorKind.ENUM_DECL,
        ]
    )
    cg.print_header()
    print("import enum")
    cg.print_items()
    cg.print_all_list()


if __name__ == "__main__":
    main()
