# This script creates an updated version of xr/enums.py

# TODO:
#  * docstrings

import inspect
import os
import re
from typing import Generator

import clang.cindex
from clang.cindex import CursorKind, Index, Type, TypeKind

from xrg import TypeNameMapper

# These variables are filled in by cmake's configure_file process
OPENXR_HEADER = "@OPENXR_INCLUDE_FILE@"
clang.cindex.Config.set_library_file("@LIBCLANG_SHARED_LIBRARY@")

# TODO: remove hard-coded versions
OPENXR_HEADER = "C:/Program Files/OPENXR/include/openxr/openxr.h"
if os.path.isfile("C:/Program Files/LLVM/bin/libclang.dll"):
    clang.cindex.Config.set_library_file("C:/Program Files/LLVM/bin/libclang.dll")

ctypes_imports = {"POINTER", "CFUNCTYPE", "Structure"}


type_name_mapper = TypeNameMapper()


class CStructField(object):
    def __init__(self, cursor):
        self.cursor = cursor
        self.name = cursor.spelling
        self.ctypes_type = type_name_mapper.api_type(cursor.type)

    def __str__(self):
        return f'\n        ("{self.name}", {self.ctypes_type}),'


class CStruct(object):
    def __init__(self, cursor):
        self.cursor = cursor
        self.name = type_name_mapper.api_type_string(cursor.spelling)
        self.fields = []
        for c in cursor.get_children():
            if c.kind == CursorKind.FIELD_DECL:
                self.fields.append(CStructField(c))
            elif c.kind == CursorKind.UNEXPOSED_ATTR:
                pass  # something about the typedef?
            else:
                assert False
        self.is_recursive = False
        for f in self.fields:
            m = re.search(fr"\b{self.name}\b", f.ctypes_type)
            if m:
                self.is_recursive = True

    def __str__(self):
        result = f"class {self.name}(Structure):"
        if self.is_recursive:
            result += "\n    pass"
            result += f"\n\n\n{self.name}._fields_ = ["
        else:
            result += "\n    _fields_ = ["
        result += "".join([str(p) for p in self.fields])
        result += "\n    ]"
        return result

    @staticmethod
    def blank_lines_before():
        return 2

    @staticmethod
    def blank_lines_after():
        return 2


class CTypedef(object):
    def __init__(self, cursor):
        self.cursor = cursor
        self.new_type = type_name_mapper.api_type_string(cursor.spelling)
        self.name = self.new_type
        clang_type = cursor.underlying_typedef_type
        self.c_type = clang_type.spelling
        self.ctypes_type = type_name_mapper.api_type(clang_type)

    def __str__(self) -> str:
        return f"{self.new_type} = {self.ctypes_type}"

    @staticmethod
    def blank_lines_before():
        return 1

    @staticmethod
    def blank_lines_after():
        return 1


def generate_typedefs() -> Generator[CTypedef, None, None]:
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
        if child.kind == CursorKind.TYPEDEF_DECL:
            t = CTypedef(cursor=child)
            if t.new_type != t.ctypes_type:  # ignore typedef struct t {} t; etc.
                yield t
        elif child.kind == CursorKind.STRUCT_DECL:
            t = CStruct(cursor=child)
            yield t
        else:
            assert False


def main():
    typedefs = list(generate_typedefs())

    print(inspect.cleandoc(
        """
        # Warning: this file is auto-generated. Do not edit.
        """))
    print("")
    print(type_name_mapper.ctypes_import())
    blanks1 = 0
    blanks2 = 0
    for t in typedefs:
        blanks1 = t.blank_lines_before()
        for b in range(max(blanks1, blanks2)):
            print("")
        print(t)
        blanks2 = t.blank_lines_after()
    print("\n\n__all__ = [")
    for t in typedefs:
        print(f'    "{t.name}",')
    print("]")


if __name__ == "__main__":
    main()
