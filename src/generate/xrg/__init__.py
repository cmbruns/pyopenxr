"""
File xrg.__init__.py

This module contains code to help generate the code in pyopenxr.
"""

# TODO:
#  * generate docstrings

import enum
import os
import platform
from typing import Generator

import clang.cindex
from clang.cindex import Cursor, CursorKind, Index, TranslationUnit, TypeKind

from .resources import resource_filename, resource_string
from .xrtypes import *
from .declarations import *


if platform.system() == "Windows":
    lib_clang = resource_filename("xrg", "libclang.dll")
elif platform.system() == "Linux":
    # TODO: don't hardcode this file name
    lib_clang = resource_filename("xrg", "libclang-14.so")
else:
    raise NotImplementedError
if os.path.isfile(lib_clang):
    clang.cindex.Config.set_library_file(lib_clang)


class Header(enum.Enum):
    OPENXR = "openxr.h",
    PLATFORM = "openxr_platform.h",

    def file_name(self) -> str:
        return self.value[0]


class CodeGenerator(object):
    def __init__(
            self,
            kinds: list[CursorKind] = None,
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
        self.all_list = set()
        self._flag_types = {}

    @property
    def items(self) -> list[CodeItem]:
        if self._items is None:  # Populate list just in time
            self._items = list(generate_code_items(
                kinds=self.cursor_kinds,
                header=self.header,
                compiler_args=self.compiler_args,
                header_preamble=self.header_preamble,
            ))
        return self._items

    def print_all_list(self, api=Api.PYTHON) -> None:
        for t in self.items:
            self.all_list.add(t.name(api))
        print("\n\n__all__ = [")
        for t in sorted(self.all_list):
            print(f'    "{t}",')
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
    header_file_name = resource_filename("xrg.headers", f"{header.value[0]}")
    header_text = resource_string("xrg.headers", f"{header.value[0]}")
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
    kinds: list[CursorKind] = None,
    header: Header = Header.OPENXR,
    compiler_args=None,
    header_preamble=None,
) -> Generator[CodeItem, None, None]:
    # Separate pass to assemble Flag types
    flag_types = {}
    # Which are accumulated from TYPEDEF and VAR_DECL cursors
    if kinds is None or len(kinds) == 0 or (
            CursorKind.TYPEDEF_DECL in kinds
            and CursorKind.VAR_DECL in kinds):
        for cursor in generate_cursors(
                header=header,
                compiler_args=compiler_args,
                header_preamble=header_preamble,
        ):
            if cursor.kind == CursorKind.TYPEDEF_DECL:
                ut = cursor.underlying_typedef_type
                if ut.spelling != "XrFlags64":
                    continue
                flag_types[cursor.spelling] = FlagsItem(cursor)
            elif cursor.kind == CursorKind.VAR_DECL:
                ct = cursor.type
                if ct.kind == TypeKind.ELABORATED:
                    ct = ct.get_named_type()  # unpack elaborated type, whatever that is
                if ct.kind != TypeKind.TYPEDEF:
                    continue
                ut = ct.get_declaration().underlying_typedef_type
                if ut.spelling != "XrFlags64":
                    continue
                flags_type_name = ct.spelling.replace("const ", "")
                flag_types[flags_type_name].add_value(cursor)
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
            item = handler(cursor)
            yield item
            if cursor.kind == CursorKind.TYPEDEF_DECL:
                if cursor.underlying_typedef_type.spelling == "XrFlags64":
                    if cursor.spelling in flag_types:
                        yield flag_types[cursor.spelling]
        except SkippableCodeItemException:
            continue


def get_header_as_string(header: Header = Header.OPENXR) -> str:
    header_file = resource_filename("xrg", f"headers/{header.value[0]}")
    with open(header_file) as f:
        file_string = f.read()
    return file_string


__all__ = [
    "Api",
    "CodeGenerator",
    "get_header_as_string",
    "Header",
]
