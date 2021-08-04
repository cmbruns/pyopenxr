# This script creates an updated version of xr/enums.py

# TODO:
#  * docstrings

import inspect
import re
from typing import Generator

import clang.cindex
from clang.cindex import Cursor, CursorKind, Index, TranslationUnit

# These variables are filled in by cmake's configure_file process
OPENXR_HEADER = "@OPENXR_INCLUDE_FILE@"
clang.cindex.Config.set_library_file("@LIBCLANG_SHARED_LIBRARY@")


class CEnum(object):
    def __init__(self, cursor: Cursor):
        self.cursor = cursor
        self.values = []
        for v in cursor.get_children():
            assert v.kind == CursorKind.ENUM_CONSTANT_DECL
            self.values.append(CEnumValue(parent=self, cursor=v))

    @property
    def cname(self):
        return self.cursor.spelling

    @property
    def pyname(self):
        cn = self.cname
        assert cn.startswith("Xr")
        return cn[2:]


class CEnumValue(object):
    def __init__(self, parent: CEnum, cursor: Cursor):
        self.parent = parent
        self.cursor = cursor

    @property
    def cname(self) -> str:
        return self.cursor.spelling

    @property
    def cvalue(self) -> str:
        return self.cursor.enum_value

    # Certain enums name their values differently than others
    _PREFIX_TABLE = {
        "RESULT_": "",
        "STRUCTURE_TYPE_": "TYPE_",
        "PERF_SETTINGS_NOTIFICATION_LEVEL_": "PERF_SETTINGS_NOTIF_LEVEL_",
    }

    @property
    def pyname(self):
        n = self.cname
        assert n.startswith("XR_")
        n = n[3:]  # Strip off initial "XR_"
        prefix = self.parent.pyname
        postfix = ""
        for postfix1 in ["EXT", "FB", "KHR", "MSFT"]:
            if prefix.endswith(postfix1):
                prefix = prefix[:-len(postfix1)]
                postfix = f"_{postfix1}"
                break
        prefix = re.sub(r"(?<!^)(?=[A-Z])", "_", prefix).upper() + "_"  # snake from camel
        if n == f"{prefix}MAX_ENUM{postfix}":
            return f"_MAX_ENUM"  # private enum value
        if prefix in self._PREFIX_TABLE:
            prefix = self._PREFIX_TABLE[prefix]
        assert n.startswith(prefix)
        n = n[len(prefix):]
        if len(postfix) > 0:
            n = n[:-len(postfix)]  # It's already in the parent enum name
        return n  # TODO:

    def __str__(self):
        return f"    {self.pyname} = {self.cvalue}"


def generate_enums() -> Generator[CEnum, None, None]:
    tu = Index.create().parse(path=OPENXR_HEADER)
    tu_file_name = str(tu.cursor.spelling)
    for child in tu.cursor.get_children():
        if not str(child.location.file) == tu_file_name:
            continue  # Don't leave this file
        if child.kind in (
            CursorKind.FUNCTION_DECL,
            CursorKind.INCLUSION_DIRECTIVE,
            CursorKind.STRUCT_DECL,
            CursorKind.TYPEDEF_DECL,
            CursorKind.VAR_DECL,
        ):
            continue
        assert child.kind == CursorKind.ENUM_DECL
        yield CEnum(cursor=child)


def main():
    enums = list(generate_enums())

    print(inspect.cleandoc(
        """
        # Warning: this file is auto-generated. Do not edit.
        
        import enum
        """))
    for c_enum in enums:
        print("\n")
        print(f"class {c_enum.pyname}(enum.Enum):")
        for v in c_enum.values:
            if v.pyname == "_MAX_ENUM":
                continue  # Skip these
            print(v)
    print("\n\n__all__ = [")
    for e in enums:
        print(f'    "{e.pyname}",')
    print("]")


if __name__ == "__main__":
    main()
