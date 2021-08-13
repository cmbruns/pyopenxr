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

    functions.print_header(api=xrg.Api.PYTHON)
    print("")

    print(
        inspect.cleandoc(
            '''
    """
    File xr.functions.py
    
    Defines high-level pythonic function definitions for pyopenxr.
    """
    '''
        )
    )

    print("")

    for fn in functions.items:
        print("")
        print(fn.code(api=xrg.Api.PYTHON))
    functions.print_all_list(api=xrg.Api.PYTHON)


if __name__ == "__main__":
    main()
