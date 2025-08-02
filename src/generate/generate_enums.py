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


    def succeeded(result) -> bool:
        return result >= 0
    
    
    def failed(result) -> bool:
        return result < 0
    
    
    def unqualified_success(result) -> bool:
        return result == 0


    class DefaultEnumMeta(enum.EnumMeta):
        """
        Metaclass to allow default values in enumerations.
    
        https://stackoverflow.com/questions/44867597/is-there-a-way-to-specify-a-default-value-for-python-enums
        """
        default = object()
    
        def __call__(cls, value=default, *args, **kwargs):
            if value is DefaultEnumMeta.default:
                # Enums with a zero should default to zero
                try:
                    result = cls(0)
                except ValueError:
                    # Otherwise assume the first enum is default
                    result = next(iter(cls))
                return result
            return super().__call__(value, *args, **kwargs)


    class EnumBase(enum.IntEnum, metaclass=DefaultEnumMeta):
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

    cg.all_list.update([
        "succeeded",
        "failed",
        "unqualified_success",
        "EnumBase",
        "FlagBase",
    ])
    cg.all_list.add("EnumBase")
    cg.all_list.add("FlagBase")
    cg.print_all_list()


if __name__ == "__main__":
    main()
