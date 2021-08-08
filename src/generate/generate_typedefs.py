# This script creates an updated version of xr/enums.py

from clang.cindex import CursorKind
import xrg


def main():
    typedefs = list(xrg.generate_code_items([
        CursorKind.STRUCT_DECL,
        CursorKind.TYPEDEF_DECL,
    ]))

    ctypes_names = set()
    for t in typedefs:
        ctypes_names.update(t.used_ctypes())

    print("""# Warning: this file is auto-generated. Do not edit.""")
    print("")
    print(f"from ctypes import {', '.join(sorted(ctypes_names))}")

    blanks2 = 0
    for t in typedefs:
        blanks1 = t.blank_lines_before()
        for b in range(max(blanks1, blanks2)):
            print("")
        print(t.py_string())
        blanks2 = t.blank_lines_after()

    print("\n\n__all__ = [")
    for t in typedefs:
        print(f'    "{t.py_name()}",')
    print("]")


if __name__ == "__main__":
    main()
