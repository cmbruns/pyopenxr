# This script creates an updated version of xr/constants.py

from clang.cindex import CursorKind
import xrg


def main():
    cg = xrg.CodeGenerator(
        [
            CursorKind.MACRO_DEFINITION,
            CursorKind.VAR_DECL,
        ]
    )
    cg.print_header()
    cg.print_items(py=True)
    cg.print_all_list(py=True)


if __name__ == "__main__":
    main()
