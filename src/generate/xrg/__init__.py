"""
File xrg.__init__.py

This module contains code to help generate the code in pyopenxr.
"""

# TODO:
#  * generate docstrings

import os
import pkg_resources
from typing import Generator, List

import clang.cindex
from clang.cindex import Cursor, CursorKind, Index, TranslationUnit

from .types import *
from .declarations import *

# NOTE: some of these files should have been copied here by cmake...
OPENXR_HEADER = pkg_resources.resource_filename("xrg", "headers/openxr.h")

LIBCLANG_SHARED_LIBRARY = pkg_resources.resource_filename("xrg", "libclang.dll")  # TODO: Linux, Mac
if os.path.isfile(LIBCLANG_SHARED_LIBRARY):
    clang.cindex.Config.set_library_file(LIBCLANG_SHARED_LIBRARY)


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

    @staticmethod
    def platform_items(compiler_args) -> list[CodeItem]:
        return list(generate_platform_code_items(compiler_args))

    def print_all_platform_list(self, compiler_args) -> None:
        print("\n\n__all__ = [")
        for t in self.platform_items(compiler_args):
            print(f'    "{t.name(Api.PYTHON)}",')
        print("]")

    def print_all_list(self, api=Api.PYTHON) -> None:
        print("\n\n__all__ = [")
        for t in self.items:
            print(f'    "{t.name(api)}",')
        print("]")

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

    def print_platform_items(self, compiler_args: List[str]) -> None:
        blanks2 = 0
        for t in self.platform_items(compiler_args):
            blanks1 = t.blank_lines_before()
            for b in range(max(blanks1, blanks2)):
                print("")
            print(t.code(Api.PYTHON))
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


def generate_platform_cursors(compiler_args=[]) -> Generator[Cursor, None, None]:
    package_header = pkg_resources.resource_filename("xrg", "headers/openxr_platform.h")
    tu = Index.create().parse(
        path=package_header,
        args=compiler_args,
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
    CursorKind.INCLUSION_DIRECTIVE: None,
    CursorKind.MACRO_DEFINITION: DefinitionItem,
    CursorKind.MACRO_INSTANTIATION: None,
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


def generate_platform_code_items(
    compiler_args,
) -> Generator[CodeItem, None, None]:
    for cursor in generate_platform_cursors(compiler_args):
        try:
            handler = _CursorHandlers[cursor.kind]
            if handler is not None:
                yield handler(cursor)
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
