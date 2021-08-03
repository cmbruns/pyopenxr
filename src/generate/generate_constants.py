# This script creates an updated version of xr/constants.py

import typing
from typing import Optional

import clang.cindex
from clang.cindex import Cursor, CursorKind, Index, TranslationUnit

# These variables are filled in by cmake's configure_file process
OPENXR_HEADER = "@OPENXR_INCLUDE_FILE@"
clang.cindex.Config.set_library_file("@LIBCLANG_SHARED_LIBRARY@")


class Constant(object):
    def __init__(self, cursor: Cursor, cname: str, value: str, ctype: str = None):
        self.cursor = cursor
        self.cname = cname
        self.value = value
        self.ctype = ctype
        assert self.cname.startswith("XR_")
        self.pyname = self.cname[3:]
        self.pyvalue = value
        if self.pyvalue.endswith("LL"):
            self.pyvalue = self.pyvalue[:-2]


def parse_macro_definition(cursor: Cursor, lines: list[str]) -> Optional[Constant]:
    if cursor.kind == CursorKind.MACRO_DEFINITION:
        if str(cursor.spelling).endswith("_"):  # e.g. "OPENXR_H_" header guard
            return None
        cname = cursor.spelling
        tokens = list(cursor.get_tokens())[1:]
        if len(tokens) > 1:
            return None  # We only want simple #define values
        value = tokens[0].spelling
        if value is None:
            return None
        # TODO: return a constant object, name, value, cursor
        return Constant(cursor=cursor, cname=cname, value=value)


def generate_constants() -> typing.Generator[Constant, None, None]:
    with open(OPENXR_HEADER) as f:
        file_lines = f.read().split("\n")
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
            CursorKind.MACRO_INSTANTIATION,  # TODO: use XR_DEFINE... for typedefs
        ):
            continue
        if child.kind == CursorKind.MACRO_DEFINITION:
            constant = parse_macro_definition(child, file_lines)
            if constant is not None:
                yield constant
            continue
        elif child.kind == CursorKind.VAR_DECL:
            cname = child.spelling
            ctype = child.type.spelling
            for e in child.get_children():
                if e.kind == CursorKind.TYPE_REF:
                    ctype = e.spelling  # without the const
                elif e.kind == CursorKind.UNEXPOSED_EXPR:
                    value_cursor = list(e.get_children())[0]
                    tokens = list(value_cursor.get_tokens())
                    assert len(tokens) == 1
                    value = tokens[0].spelling
            yield Constant(child, cname, value, ctype)
            continue
        assert False


def main():
    print("# Warning: this file is auto-generated. Do not edit.\n")
    constants = list(generate_constants())
    for constant in constants:
        print(f"{constant.pyname} = {constant.pyvalue}")
    print("\n\n__all__ = [")
    for c in constants:
        print(f'    "{c.pyname}",')
    print("]")


if __name__ == "__main__":
    main()
