# This script creates an updated version of xr/enums.py
import inspect

from clang.cindex import CursorKind

import xrg
from xrg.declarations import FlagsItem


def main():
    cg = xrg.CodeGenerator(
        [
            CursorKind.ENUM_DECL,
        ]
    )
    cg.ctypes_names.add("c_uint64")
    cg.print_header()
    print(inspect.cleandoc('''
    import enum


    class DefaultEnumMeta(enum.EnumMeta):
        """
        Metaclass to allow default values in enumerations.
    
        https://stackoverflow.com/questions/44867597/is-there-a-way-to-specify-a-default-value-for-python-enums
        """
        default = object()
    
        def __call__(cls, value=default, *args, **kwargs):
            if value is DefaultEnumMeta.default:
                # Assume the first enum is default
                return next(iter(cls))
            return super().__call__(value, *args, **kwargs)


    class EnumBase(enum.Enum, metaclass=DefaultEnumMeta):
        @staticmethod
        def ctype():
            return c_int
            

    class FlagBase(enum.Flag, metaclass=DefaultEnumMeta):
        @staticmethod
        def ctype():
            return c_uint64
    '''))
    cg.print_items()

    # Flag types
    cg2 = xrg.CodeGenerator([
        CursorKind.TYPEDEF_DECL,
        CursorKind.VAR_DECL,
    ])
    for item in cg2.items:
        if not isinstance(item, FlagsItem):
            continue
        print("\n")
        print(item.code())
        cg.all_list.add(item.name())

    cg.all_list.add("EnumBase")
    cg.all_list.add("FlagBase")
    cg.print_all_list()


if __name__ == "__main__":
    main()
