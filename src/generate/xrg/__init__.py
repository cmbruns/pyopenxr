"""
File xrg.__init__.py

This module contains code to help generate the code in pyopenxr.
"""

# TODO:
#  * generate docstrings

import enum
import os
import pkg_resources
import platform
from typing import Generator, List

import clang.cindex
from clang.cindex import Cursor, CursorKind, Index, TranslationUnit

from .types import *
from .declarations import *

LIBCLANG_SHARED_LIBRARY = ""
if platform.system() == "Windows":
    LIBCLANG_SHARED_LIBRARY = pkg_resources.resource_filename("xrg", "libclang.dll")  # TODO: Linux, Mac
elif platform.system() == "Linux":
    # TODO: don't hardcode this path
    LIBCLANG_SHARED_LIBRARY = pkg_resources.resource_filename("xrg", "libclang-10.so")
if os.path.isfile(LIBCLANG_SHARED_LIBRARY):
    clang.cindex.Config.set_library_file(LIBCLANG_SHARED_LIBRARY)


class Header(enum.Enum):
    OPENXR = "openxr.h",
    PLATFORM = "openxr_platform.h",

    def file_name(self) -> str:
        return self.value[0]


class CodeGenerator(object):
    def __init__(
            self,
            kinds: List[CursorKind] = None,
            header: Header = Header.OPENXR,
            compiler_args=None,
            header_preamble: str = None,
    ):
        self.cursor_kinds = kinds
        self._items = None
        self.header = header
        self.compiler_args = compiler_args
        self.ctypes_names = set()
        self.header_preamble = header_preamble

    @property
    def items(self) -> List[CodeItem]:
        if self._items is None:  # Populate list just in time
            self._items = list(generate_code_items(
                kinds=self.cursor_kinds,
                header=self.header,
                compiler_args=self.compiler_args,
                header_preamble=self.header_preamble,
            ))
        return self._items

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


def generate_cursors(
        header: Header = Header.OPENXR,
        compiler_args=None,
        header_preamble=None,
) -> Generator[Cursor, None, None]:
    header_file_name = pkg_resources.resource_filename("xrg", f"headers/{header.value[0]}")
    header_text = pkg_resources.resource_string("xrg", f"headers/{header.value[0]}")
    if header_preamble is not None:
        header_text = f"{header_preamble}\n" + header_text.decode()
    if compiler_args is None:
        compiler_args = []
    tu = Index.create().parse(
        path=header_file_name,
        unsaved_files=((header_file_name, header_text), ),
        options=TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD,
        args=compiler_args,
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
    kinds: List[CursorKind] = None,
    header: Header = Header.OPENXR,
    compiler_args=None,
    header_preamble=None,
) -> Generator[CodeItem, None, None]:
    for cursor in generate_cursors(
            header=header,
            compiler_args=compiler_args,
            header_preamble=header_preamble,
    ):
        if kinds is not None and cursor.kind not in kinds:
            continue
        handler = _CursorHandlers[cursor.kind]
        if handler is None:
            continue
        try:
            yield handler(cursor)
        except SkippableCodeItemException:
            continue


def get_header_as_string(header: Header = Header.OPENXR) -> str:
    header_file = pkg_resources.resource_filename("xrg", f"headers/{header.value[0]}")
    with open(header_file) as f:
        file_string = f.read()
    return file_string


__all__ = [
    "Api",
    "CodeGenerator",
    "get_header_as_string",
    "Header",
]
