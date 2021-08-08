# This script creates an updated version of xr/enums.py

import inspect
import os
from typing import Generator

import clang.cindex
from clang.cindex import CursorKind, Index

from xrg import *

# These variables are filled in by CMake during the configure_file process
# OPENXR_HEADER = "@OPENXR_INCLUDE_FILE@"
# clang.cindex.Config.set_library_file("@LIBCLANG_SHARED_LIBRARY@")

# TODO: remove hard-coded versions
OPENXR_HEADER = "C:/Program Files/OPENXR/include/openxr/openxr.h"
if os.path.isfile("C:/Program Files/LLVM/bin/libclang.dll"):
    clang.cindex.Config.set_library_file("C:/Program Files/LLVM/bin/libclang.dll")


type_name_mapper = TypeNameMapper()


def generate_typedefs() -> Generator[CodeItem, None, None]:
    tu = Index.create().parse(
        path=OPENXR_HEADER,
    )
    tu_file_name = str(tu.cursor.spelling)
    for child in tu.cursor.get_children():
        if not str(child.location.file) == tu_file_name:
            continue  # Don't leave this file
        if child.kind in (
            CursorKind.ENUM_DECL,
            CursorKind.FUNCTION_DECL,
            CursorKind.INCLUSION_DIRECTIVE,
            # CursorKind.STRUCT_DECL,
            # CursorKind.TYPEDEF_DECL,
            CursorKind.VAR_DECL,
        ):
            continue
        try:
            if child.kind == CursorKind.TYPEDEF_DECL:
                yield TypeDefItem(child)
            elif child.kind == CursorKind.STRUCT_DECL:
                yield StructItem(child)
            else:
                assert False  # Did we find a new top level clang cursor?
        except SkippableCodeItemException:
            continue


def main():
    typedefs = list(generate_typedefs())
    ctypes_names = set()
    for t in typedefs:
        ctypes_names.update(t.used_ctypes())

    print(inspect.cleandoc(
        """
        # Warning: this file is auto-generated. Do not edit.
        """))
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
