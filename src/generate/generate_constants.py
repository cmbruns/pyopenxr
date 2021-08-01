# This script creates an updated version of xr/constants.py

import typing

import clang.cindex
from clang.cindex import Cursor, CursorKind, Index, TranslationUnit

# These variables are filled in by cmake's configure_file process
# TODO: replace with symbolic file path
OPENXR_HEADER = "C:/Program Files/OPENXR/include/openxr/openxr.h"
# OPENXR_HEADER = "@OPENXR_INCLUDE_FILE@"
clang.cindex.Config.set_library_file("C:/Program Files/LLVM/bin/libclang.dll")


class Constant(object):
    def __init__(self, cursor: Cursor, name: str, value: str):
        self.cursor = cursor
        self.name = name
        self.value = value


def generate_constants() -> typing.Generator[Cursor, None, None]:
    tu = Index.create().parse(
        path=OPENXR_HEADER,
        options=TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD,
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
            CursorKind.TYPEDEF_DECL,
        ):
            continue
        yield child
        continue


def main():
    for node in generate_constants():
        # TODO: VAR_DECLS probably need to come after type definitions
        #
        print(node.kind, node.spelling)


if __name__ == "__main__":
    main()
