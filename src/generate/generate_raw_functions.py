"""
File: generate_raw_functions.py
Code generator script creates an updated version of xr/raw_functions.py.
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

    functions.print_header(api=xrg.Api.CTYPES)
    print("")

    print(
        inspect.cleandoc(
            '''
    """
    File xr.raw_functions.py
    
    Defines low-level ctypes function definitions for use by
    higher-level pythonic functions in pyopenxr.
    """
    '''
        )
    )

    print("")
    print("from .library import openxr_loader_library")
    print("from .enums import *")
    print("from .typedefs import *")
    print("")

    print("\n# ctypes Function definitions")

    all_list = set()
    for fn in functions.items:
        try:
            s = fn.code(api=xrg.Api.CTYPES)
        except Exception as exc:
            continue
        print("")
        print(s)
        all_list.add(fn.name(api=xrg.Api.CTYPES))
    print("\n\n__all__ = [")
    for t in sorted(all_list):
        print(f'    "{t}",')
    print("]")


if __name__ == "__main__":
    main()
