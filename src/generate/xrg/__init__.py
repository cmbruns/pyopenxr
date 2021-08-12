"""
File xrg.__init__.py

This module contains code to help generate the code in pyopenxr.
"""

# TODO:
#  * generate docstrings

import os
from typing import Generator

import clang.cindex
from clang.cindex import Cursor, CursorKind, Index, TranslationUnit

from .types import *
from .declarations import *

# These variables are filled in by CMake during the configure step
# OPENXR_HEADER = "@OPENXR_INCLUDE_FILE@"
# if os.path.isfile("@LIBCLANG_SHARED_LIBRARY@"):
#     clang.cindex.Config.set_library_file("@LIBCLANG_SHARED_LIBRARY@")

# TODO: remove hard-coded versions
OPENXR_HEADER = "C:/Program Files/OPENXR/include/openxr/openxr.h"
if os.path.isfile("C:/Program Files/LLVM/bin/libclang.dll"):
    clang.cindex.Config.set_library_file("C:/Program Files/LLVM/bin/libclang.dll")


class CodeGenerator(object):
    def __init__(self, kinds: list[CursorKind] = None):
        self.cursor_kinds = kinds
        self._items = None
        self.ctypes_names = set()

    @property
    def items(self) -> list[CodeItem]:
        if self._items is None:  # Populate list just in time
            self._items = list(generate_code_items(self.cursor_kinds))
        return self._items

    def print_all_list(self, api=Api.PYTHON) -> None:
        print("\n\n__all__ = [")
        for t in self.items:
            print(f'    "{t.name(api)}",')
        print("]")

    @staticmethod
    def print_enum_aliases() -> None:
        print("# Enum aliases (not exposed in __all__)")
        enums = CodeGenerator(
            [
                CursorKind.ENUM_DECL,
            ]
        )
        for e in enums.items:
            assert isinstance(e, EnumItem)
            print(f"{e.name(Api.PYTHON)} = c_int")

    def print_header(self, api=Api.PYTHON) -> None:
        for t in self.items:
            self.ctypes_names.update(t.used_ctypes(api))
        print("""# Warning: this file is auto-generated. Do not edit.""")
        print("")
        if len(self.ctypes_names) > 0:
            print(f"from ctypes import {', '.join(sorted(self.ctypes_names))}")

    def print_items(self, api=Api.PYTHON) -> None:
        blanks2 = 0
        for t in self.items:
            blanks1 = t.blank_lines_before()
            for b in range(max(blanks1, blanks2)):
                print("")
            print(t.code(api))
            blanks2 = t.blank_lines_after()


def generate_cursors() -> Generator[Cursor, None, None]:
    tu = Index.create().parse(
        path=OPENXR_HEADER,
        options=TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD,
    )
    tu_file_name = str(tu.cursor.spelling)
    for child in tu.cursor.get_children():
        if not str(child.location.file) == tu_file_name:
            continue  # Don't leave this file
        yield child


_CursorHandlers = {
    CursorKind.ENUM_DECL: EnumItem,
    CursorKind.FUNCTION_DECL: FunctionItem,
    CursorKind.MACRO_DEFINITION: DefinitionItem,
    CursorKind.TYPEDEF_DECL: TypeDefItem,
    CursorKind.STRUCT_DECL: StructItem,
    CursorKind.VAR_DECL: VariableItem,
}


def generate_code_items(
    kinds: list[CursorKind] = None,
) -> Generator[CodeItem, None, None]:
    for cursor in generate_cursors():
        if kinds is not None and cursor.kind not in kinds:
            continue
        try:
            yield _CursorHandlers[cursor.kind](cursor)
        except SkippableCodeItemException:
            continue


def get_header_as_string() -> str:
    with open(OPENXR_HEADER) as f:
        file_string = f.read()
    return file_string


__all__ = [
    "Api",
    "get_header_as_string",
    "CodeGenerator",
]
