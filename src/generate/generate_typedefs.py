# This script creates an updated version of xr/typedefs.py

from clang.cindex import CursorKind
import xrg


def main():
    cg = xrg.CodeGenerator([
        CursorKind.STRUCT_DECL,
        CursorKind.TYPEDEF_DECL,
    ])
    cg.print_header()

    # Generate custom enum declarations, not exposed in __all__
    print("")
    print("# Enum aliases")
    enums = xrg.CodeGenerator([CursorKind.ENUM_DECL, ])
    for enum in enums.items:
        assert isinstance(enum, xrg.EnumItem)
        print(f"{enum.py_name()} = c_int")

    cg.print_items(py=True)
    cg.print_all_list(py=True)


if __name__ == "__main__":
    main()
