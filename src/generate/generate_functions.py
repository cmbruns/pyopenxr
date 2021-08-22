"""
File: generate_functions.py
Code generator script creates an updated version of xr/functions.py.
"""

import inspect

from clang.cindex import CursorKind

import xrg


def main():
    functions = xrg.CodeGenerator(
        [
            CursorKind.FUNCTION_DECL,
        ]
    )

    print("from __future__ import annotations  # To support python 3.9+ style array type annotations")
    functions.print_header(api=xrg.Api.PYTHON)
    print("")

    print(
        inspect.cleandoc(
            '''
        """
        File xr.functions.py
        
        Defines high-level pythonic function definitions for pyopenxr.
        """
        
        from ctypes import Array, byref, create_string_buffer
        
        from . import raw_functions
        from .enums import *
        from .exceptions import check_result
        from .typedefs import *
    '''
        )
    )

    for fn in functions.items:
        print("\n")
        print(fn.code(api=xrg.Api.PYTHON))
    functions.print_all_list(api=xrg.Api.PYTHON)


if __name__ == "__main__":
    main()
