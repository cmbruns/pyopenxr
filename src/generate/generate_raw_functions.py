"""
File: generate_raw_functions.py
Code generator script creates an updated version of xr/raw_functions.py.
"""

import inspect
import typing

from clang.cindex import CursorKind

import xrg


def main():
    functions = xrg.CodeGenerator(
        [
            CursorKind.FUNCTION_DECL,
        ]
    )

    functions.ctypes_names.add("c_int")  # because of enum aliases, below
    functions.print_header()
    print("")

    print(
        inspect.cleandoc(
            '''
    """
    File xr.raw_function.py
    
    Defines low-level ctypes function definitions for use by
    higher-level pythonic functions in pyopenxr.
    """
    '''
        )
    )

    print("")
    print("from .library import openxr_loader_library")
    print("from .typedefs import *")
    print("")

    # Generate custom enum declarations, not exposed in __all__
    functions.print_enum_aliases()

    print("\n# ctypes Function definitions")

    for fn in functions.items:
        assert isinstance(fn, xrg.FunctionItem)
        fn = typing.cast(xrg.FunctionItem, fn)
        print("")
        print(fn.code(api=xrg.Api.CTYPES))
    functions.print_all_list(api=xrg.Api.CTYPES)


if __name__ == "__main__":
    main()
