# This script creates an updated version of xr/enums.py
import inspect

from clang.cindex import CursorKind

import xrg


def main():
    cg = xrg.CodeGenerator(
        [
            CursorKind.ENUM_DECL,
        ]
    )
    cg.print_header()
    print(inspect.cleandoc("""
    import enum


    class EnumBase(enum.Enum):
        @staticmethod
        def ctype():
            return c_int
    """))
    cg.print_items()
    cg.print_all_list()


if __name__ == "__main__":
    main()
