# This script creates an updated version of xr/typedefs.py

from clang.cindex import CursorKind
import xrg


def main():
    cg = xrg.CodeGenerator([
        CursorKind.STRUCT_DECL,
        CursorKind.TYPEDEF_DECL,
    ])

    cg.ctypes_names.add("c_int")  # Because print_enum_aliases() below
    cg.print_header()

    # Generate local ctypes enum symbol declarations, not exposed in __all__
    print("")
    cg.print_enum_aliases()

    cg.print_items(py=True)
    cg.print_all_list(py=True)


if __name__ == "__main__":
    main()
