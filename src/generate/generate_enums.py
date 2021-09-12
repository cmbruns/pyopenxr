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
    
    
    class SpaceVelocityFlags(enum.Flag, metaclass=DefaultEnumMeta):
        NONE = 0x00000000
        LINEAR_VALID = 0x00000001
        ANGULAR_VALID = 0x00000002


    class EnumBase(enum.Enum):
        @staticmethod
        def ctype():
            return c_int
    '''))
    cg.print_items()
    cg.print_all_list()


if __name__ == "__main__":
    main()
