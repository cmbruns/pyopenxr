# This script creates an updated version of xr/enums.py

# TODO:
#  * docstrings

import inspect
import re
from typing import Generator

import clang.cindex
from clang.cindex import CursorKind, Index, Type, TypeKind

# These variables are filled in by cmake's configure_file process
# OPENXR_HEADER = "@OPENXR_INCLUDE_FILE@"
# clang.cindex.Config.set_library_file("@LIBCLANG_SHARED_LIBRARY@")

# TODO:
OPENXR_HEADER = "C:/Program Files/OPENXR/include/openxr/openxr.h"
clang.cindex.Config.set_library_file("C:/Program Files/LLVM/bin/libclang.dll")

ctypes_imports = {"POINTER", "CFUNCTYPE", "Structure", "c_float", "c_char"}

# TODO: Create fake pointed-to structs
# TODO: Import enums
# TODO: Strip const


def ctype_from_clang_type(c_type: Type) -> str:
    m = re.match(r"(u?int(?:32|64))_t", c_type.spelling)
    if m:
        t = f"c_{m.group(1)}"
        ctypes_imports.add(t)
        return t
    elif c_type.kind == TypeKind.CHAR_S:
        return "c_char"
    elif c_type.kind == TypeKind.CONSTANTARRAY:
        return f"({sx(c_type.element_type)} * {c_type.element_count})"
    elif c_type.kind == TypeKind.ELABORATED:
        return sx(c_type.get_named_type())
    elif c_type.kind == TypeKind.ENUM:
        return c_type.get_declaration().spelling
    elif c_type.kind == TypeKind.FLOAT:
        return "c_float"
    elif c_type.kind == TypeKind.POINTER:
        pt = c_type.get_pointee()
        if pt.kind == TypeKind.FUNCTIONPROTO:
            args = [pt.get_result(), *(pt.argument_types())]
            arg_string = ", ".join([sx(a) for a in args])
            return f"CFUNCTYPE({arg_string})"
        else:
            return f"POINTER({sx(pt)})"
    elif c_type.kind == TypeKind.RECORD:
        return c_type.get_declaration().spelling
    elif c_type.kind == TypeKind.TYPEDEF:
        return c_type.spelling
    elif c_type.kind == TypeKind.VOID:
        return "None"
    else:
        assert(False)


# Strip off initial "Xr"
def ss(s: str) -> str:
    if s.startswith("Xr"):
        return s[2:]
    return s


def sx(t: Type) -> str:
    return ss(ctype_from_clang_type(t))


class CTypedef(object):
    def __init__(self, cursor):
        self.cursor = cursor
        self.new_type = ss(cursor.spelling)
        clang_type = cursor.underlying_typedef_type
        self.c_type = clang_type.spelling
        self.ctypes_type = sx(clang_type)


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
            CursorKind.STRUCT_DECL,
            # CursorKind.TYPEDEF_DECL,
            CursorKind.VAR_DECL,
        ):
            continue
        assert child.kind == CursorKind.TYPEDEF_DECL
        t = CTypedef(cursor=child)
        if t.new_type != t.ctypes_type:  # ignore typedef struct t {} t; etc.
            yield t


def main():
    typedefs = list(generate_typedefs())

    print(inspect.cleandoc(
        """
        # Warning: this file is auto-generated. Do not edit.
        """))
    print("")
    print("from ctypes import " + ", ".join(sorted(ctypes_imports)))
    print("")
    for t in typedefs:
        print(f"{t.new_type} = {t.ctypes_type}")
    print("\n\n__all__ = [")
    for t in typedefs:
        print(f'    "{t.new_type}",')
    print("]")


if __name__ == "__main__":
    main()
