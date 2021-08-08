"""
File xrg.__init__.py

This module contains code to help generate the code in pyopenxr.
"""

# TODO:
#  * generate docstrings

from abc import ABC, abstractmethod
import clang.cindex
from clang.cindex import Cursor, CursorKind, Index, TranslationUnit, TypeKind
import os
import re
from typing import Generator

# These variables are filled in by CMake during the configure_file process
OPENXR_HEADER = "@OPENXR_INCLUDE_FILE@"
if os.path.isfile("@LIBCLANG_SHARED_LIBRARY@"):
    clang.cindex.Config.set_library_file("@LIBCLANG_SHARED_LIBRARY@")

##############
# Exceptions #
##############


class SkippableCodeItemException(Exception):
    pass


################
# Type classes #
################


class TypeBase(ABC):
    def __init__(self, clang_type: clang.cindex.Type):
        self.clang_type = clang_type

    @abstractmethod
    def capi_string(self) -> str:
        pass

    @abstractmethod
    def py_string(self) -> str:
        pass

    @abstractmethod
    def used_ctypes(self) -> set[str]:
        pass


class ArrayType(TypeBase):
    def __init__(self, clang_type: clang.cindex.Type):
        super().__init__(clang_type)
        assert clang_type.kind == TypeKind.CONSTANTARRAY
        self.element_type = parse_type(clang_type.element_type)
        self.count = clang_type.element_count

    def capi_string(self) -> str:
        return f"({self.element_type.capi_string()} * {self.count})"

    def py_string(self) -> str:
        return f"({self.element_type.py_string()} * {self.count})"

    def used_ctypes(self) -> set[str]:
        return self.element_type.used_ctypes()


class EnumType(TypeBase):
    def __init__(self, clang_type: clang.cindex.Type):
        super().__init__(clang_type)
        assert clang_type.kind == TypeKind.ENUM
        self._capi_name = "c_uint32"  # TODO we could use the actual name if we had the enums loaded
        self._py_name = "c_uint32"

    def capi_string(self) -> str:
        return self._capi_name

    def py_string(self) -> str:
        return self._py_name

    def used_ctypes(self) -> set[str]:
        return {"c_uint32", }


class FunctionPointerType(TypeBase):
    def __init__(self, clang_type: clang.cindex.Type):
        super().__init__(clang_type)
        assert clang_type.kind == TypeKind.POINTER
        pt = clang_type.get_pointee()
        assert pt.kind == TypeKind.FUNCTIONPROTO
        self.result_type = parse_type(pt.get_result())
        self.arg_types = [parse_type(t) for t in pt.argument_types()]
        c_arg_string = ", ".join(a.capi_string() for a in [self.result_type, *self.arg_types])
        py_arg_string = ", ".join(a.py_string() for a in [self.result_type, *self.arg_types])
        self._capi_string = f"CFUNCTYPE({c_arg_string})"
        self._py_string = f"CFUNCTYPE({py_arg_string})"

    def capi_string(self) -> str:
        return self._capi_string

    def py_string(self) -> str:
        return self._py_string

    def used_ctypes(self) -> set[str]:
        result = {"CFUNCTYPE", }
        result.update(self.result_type.used_ctypes())
        result.update(self.result_type.used_ctypes())
        for a in self.arg_types:
            result.update(a.used_ctypes())
        return result


class PointerType(TypeBase):
    def __init__(self, clang_type: clang.cindex.Type):
        super().__init__(clang_type)
        assert clang_type.kind == TypeKind.POINTER
        pt = clang_type.get_pointee()
        assert pt.kind != TypeKind.VOID
        assert pt.kind != TypeKind.FUNCTIONPROTO
        self.pointee = parse_type(pt)

    def capi_string(self) -> str:
        return f"POINTER({self.pointee.capi_string()})"

    def py_string(self) -> str:
        return f"POINTER({self.pointee.py_string()})"

    def used_ctypes(self) -> set[str]:
        result = self.pointee.used_ctypes()
        result.add("POINTER")
        return result


class PrimitiveType(TypeBase):
    def __init__(self, clang_type: clang.cindex.Type):
        super().__init__(clang_type)
        self._capi_name = capi_type_name(clang_type.spelling)
        m = re.match(r"(u?int(?:8|16|32|64))_t", self._capi_name)
        if clang_type.kind == TypeKind.CHAR_S:
            self._capi_name = "c_char"
        elif clang_type.kind == TypeKind.FLOAT:
            self._capi_name = "c_float"
        elif m is not None:
            self._capi_name = f"c_{m.group(1)}"
        self._py_name = py_type_name(self._capi_name)

    def capi_string(self) -> str:
        return self._capi_name

    def py_string(self) -> str:
        return self._py_name

    def used_ctypes(self) -> set[str]:
        if self._capi_name.startswith("c_"):
            return {self._capi_name, }
        return set()


class RecordType(TypeBase):
    def __init__(self, clang_type: clang.cindex.Type):
        super().__init__(clang_type)
        assert clang_type.kind == TypeKind.RECORD
        self._capi_name = capi_type_name(clang_type.get_declaration().spelling)
        self._py_name = py_type_name(self._capi_name)

    def capi_string(self) -> str:
        return self._capi_name

    def py_string(self) -> str:
        return self._py_name

    def used_ctypes(self) -> set[str]:
        return set()


class TypedefType(TypeBase):
    def __init__(self, clang_type: clang.cindex.Type):
        super().__init__(clang_type)
        assert clang_type.kind == TypeKind.TYPEDEF
        self._capi_name = capi_type_name(clang_type.spelling)
        self._py_name = py_type_name(self._capi_name)

    def capi_string(self) -> str:
        return self._capi_name

    def py_string(self) -> str:
        return self._py_name

    def used_ctypes(self) -> set[str]:
        if self._capi_name.startswith("c_"):
            return {self._capi_name, }
        return set()


class VoidPointerType(TypeBase):
    def __init__(self, clang_type: clang.cindex.Type):
        super().__init__(clang_type)
        assert clang_type.kind == TypeKind.POINTER
        pt = clang_type.get_pointee()
        assert pt.kind == TypeKind.VOID

    def capi_string(self) -> str:
        return "c_void_p"

    def py_string(self) -> str:
        return "c_void_p"

    def used_ctypes(self) -> set[str]:
        return {"c_void_p", }


class VoidType(TypeBase):
    def __init__(self, clang_type: clang.cindex.Type):
        super().__init__(clang_type)
        assert clang_type.kind == TypeKind.VOID

    def capi_string(self) -> str:
        return "None"

    def py_string(self) -> str:
        return "None"

    def used_ctypes(self) -> set[str]:
        return {"c_void_p", }


####################
# CodeItem classes #
####################

class CodeItem(ABC):
    def __init__(self, cursor: Cursor) -> None:
        self.cursor = cursor

    @staticmethod
    def blank_lines_before() -> int:
        return 1

    @staticmethod
    def blank_lines_after() -> int:
        return 1

    @abstractmethod
    def capi_name(self) -> str:
        pass

    @abstractmethod
    def capi_string(self) -> str:
        pass

    @abstractmethod
    def py_name(self) -> str:
        pass

    @abstractmethod
    def py_string(self) -> str:
        pass

    @abstractmethod
    def used_ctypes(self) -> set[str]:
        pass


class DefinitionItem(CodeItem):
    def __init__(self, cursor: Cursor) -> None:
        super().__init__(cursor)
        assert cursor.kind == CursorKind.MACRO_DEFINITION
        self._capi_name = cursor.spelling
        if self._capi_name.endswith("_"):
            raise SkippableCodeItemException  # OPENVR_H_
        tokens = list(cursor.get_tokens())[1:]
        if len(tokens) > 1:
            raise SkippableCodeItemException  # We only want simple #define values
        self.value = tokens[0].spelling
        if self.value is None:
            raise SkippableCodeItemException  # #define with no value
        assert self._capi_name.startswith("XR_")
        self._py_name = self._capi_name[3:]
        if self.value.endswith("LL"):
            self.value = self.value[:-2]

    @staticmethod
    def blank_lines_before():
        return 0

    @staticmethod
    def blank_lines_after():
        return 0

    def capi_name(self) -> str:
        return self._capi_name

    def capi_string(self) -> str:
        return f"{self.capi_name()} = {self.value}"

    def py_name(self) -> str:
        return self._py_name

    def py_string(self) -> str:
        return f"{self.py_name()} = {self.value}"

    def used_ctypes(self) -> set[str]:
        return set()


class StructFieldItem(CodeItem):
    def __init__(self, cursor: Cursor) -> None:
        super().__init__(cursor)
        assert cursor.kind == CursorKind.FIELD_DECL
        self._capi_name = cursor.spelling
        self.type = parse_type(cursor.type)

    def capi_name(self) -> str:
        return self._capi_name

    def capi_string(self) -> str:
        return f'\n        ("{self.capi_name()}", {self.type.capi_string()}),'

    def py_name(self) -> str:
        return self.capi_name()

    def py_string(self) -> str:
        return f'\n        ("{self.py_name()}", {self.type.py_string()}),'

    def used_ctypes(self) -> set[str]:
        return self.type.used_ctypes()


class StructItem(CodeItem):
    def __init__(self, cursor: Cursor):
        super().__init__(cursor)
        assert cursor.kind == CursorKind.STRUCT_DECL
        self.c_name = cursor.spelling
        self._capi_name = capi_type_name(self.c_name)
        self._py_name = py_type_name(self._capi_name)
        self.fields = []
        for c in cursor.get_children():
            if c.kind == CursorKind.FIELD_DECL:
                self.fields.append(StructFieldItem(c))
            elif c.kind == CursorKind.UNEXPOSED_ATTR:
                pass  # something about the typedef?
            else:
                assert False
        self.is_recursive = False
        for f in self.fields:
            m = re.search(fr"\b{self._capi_name}\b", f.type.capi_string())
            if m:
                self.is_recursive = True

    @staticmethod
    def blank_lines_before():
        return 2

    @staticmethod
    def blank_lines_after():
        return 2

    def capi_name(self) -> str:
        return self._capi_name

    def capi_string(self) -> str:
        result = f"class {self.capi_name()}(Structure):"
        if self.is_recursive:
            result += "\n    pass"
            result += f"\n\n\n{self.capi_name()}._fields_ = ["
        else:
            result += "\n    _fields_ = ["
        result += "".join([f.capi_string() for f in self.fields])
        result += "\n    ]"
        return result

    def py_name(self) -> str:
        return self._py_name

    def py_string(self) -> str:
        result = f"class {self.py_name()}(Structure):"
        if self.is_recursive:
            result += "\n    pass"
            result += f"\n\n\n{self.py_name()}._fields_ = ["
        else:
            result += "\n    _fields_ = ["
        result += "".join([f.py_string() for f in self.fields])
        result += "\n    ]"
        return result

    def used_ctypes(self) -> set[str]:
        result = {"Structure", }
        for f in self.fields:
            result.update(f.used_ctypes())
        return result


class TypeDefItem(CodeItem):
    def __init__(self, cursor: Cursor):
        super().__init__(cursor)
        assert cursor.kind == CursorKind.TYPEDEF_DECL
        self._capi_name = cursor.spelling
        self._py_name = py_type_name(self._capi_name)
        self.type = parse_type(cursor.underlying_typedef_type)
        if self._capi_name == self.type.capi_string():
            raise SkippableCodeItemException  # Nonsense A = A typedef

    def capi_name(self) -> str:
        return self._capi_name

    def capi_string(self) -> str:
        return f"{self.capi_name()} = {self.type.capi_string()}"

    def py_name(self) -> str:
        return self._py_name

    def py_string(self) -> str:
        return f"{self.py_name()} = {self.type.py_string()}"

    def used_ctypes(self) -> set[str]:
        return self.type.used_ctypes()


class VariableItem(CodeItem):
    def __init__(self, cursor: Cursor) -> None:
        super().__init__(cursor)
        assert cursor.kind == CursorKind.VAR_DECL
        self._capi_name = cursor.spelling
        assert self._capi_name.startswith("XR_")
        self._py_name = self._capi_name[3:]
        self.type = None
        for e in cursor.get_children():
            if e.kind == CursorKind.TYPE_REF:
                self.type = parse_type(e.type)
            elif e.kind == CursorKind.UNEXPOSED_EXPR:
                value_cursor = list(e.get_children())[0]
                tokens = list(value_cursor.get_tokens())
                assert len(tokens) == 1
                self.value = tokens[0].spelling
        if self.value.endswith("LL"):
            self.value = self.value[:-2]

    @staticmethod
    def blank_lines_before():
        return 0

    @staticmethod
    def blank_lines_after():
        return 0

    def capi_name(self) -> str:
        return self._capi_name

    def capi_string(self) -> str:
        return f"{self.capi_name()} = {self.value}"

    def py_name(self) -> str:
        return self._py_name

    def py_string(self) -> str:
        return f"{self.py_name()} = {self.value}"

    def used_ctypes(self) -> set[str]:
        return set()


class CodeGenerator(object):
    def __init__(self, kinds: list[CursorKind] = None):
        self.cursor_kinds = kinds
        self._items = None

    @property
    def items(self) -> list[CodeItem]:
        if self._items is None:  # Populate list just in time
            self._items = list(generate_code_items(self.cursor_kinds))
        return self._items

    def print_all_list(self, py=True) -> None:
        print("\n\n__all__ = [")
        for t in self.items:
            if py:
                print(f'    "{t.py_name()}",')
            else:
                print(f'    "{t.capi_name()}",')
        print("]")

    def print_header(self) -> None:
        ctypes_names = set()
        for t in self.items:
            ctypes_names.update(t.used_ctypes())
        print("""# Warning: this file is auto-generated. Do not edit.""")
        print("")
        if len(ctypes_names) > 0:
            print(f"from ctypes import {', '.join(sorted(ctypes_names))}")

    def print_items(self, py=True) -> None:
        blanks2 = 0
        for t in self.items:
            blanks1 = t.blank_lines_before()
            for b in range(max(blanks1, blanks2)):
                print("")
            if py:
                print(t.py_string())
            else:
                print(t.capi_string())
            blanks2 = t.blank_lines_after()


#############
# functions #
#############

def capi_type_name(c_type_name: str) -> str:
    """The low level C-like api uses the exact same names as in C"""
    s = re.sub(r"\b(?:const|volatile)\s+", "", c_type_name)  # But without const
    return s


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


def generate_code_items(kinds: list[CursorKind] = None) -> Generator[CodeItem, None, None]:
    for cursor in generate_cursors():
        if kinds is not None and cursor.kind not in kinds:
            continue
        try:
            if cursor.kind == CursorKind.TYPEDEF_DECL:
                yield TypeDefItem(cursor)
            elif cursor.kind == CursorKind.STRUCT_DECL:
                yield StructItem(cursor)
            elif cursor.kind == CursorKind.MACRO_DEFINITION:
                yield DefinitionItem(cursor)
            elif cursor.kind == CursorKind.VAR_DECL:
                yield VariableItem(cursor)
            else:
                assert False  # Did we find a new top level clang cursor?
        except SkippableCodeItemException:
            continue


def parse_type(clang_type: clang.cindex.Type) -> TypeBase:
    m = re.match(r"(?:const )?(u?int(?:8|16|32|64))_t", clang_type.spelling)
    if m:
        return PrimitiveType(clang_type)
    elif clang_type.kind == TypeKind.CHAR_S:
        return PrimitiveType(clang_type)
    elif clang_type.kind == TypeKind.CONSTANTARRAY:
        return ArrayType(clang_type)
    elif clang_type.kind == TypeKind.ELABORATED:
        return parse_type(clang_type.get_named_type())
    elif clang_type.kind == TypeKind.ENUM:
        return EnumType(clang_type)
    elif clang_type.kind == TypeKind.FLOAT:
        return PrimitiveType(clang_type)
    elif clang_type.kind == TypeKind.POINTER:
        pt = clang_type.get_pointee()
        if pt.kind == TypeKind.FUNCTIONPROTO:
            return FunctionPointerType(clang_type)
        elif pt.kind == TypeKind.VOID:
            return VoidPointerType(clang_type)
        else:
            return PointerType(clang_type)
    elif clang_type.kind == TypeKind.RECORD:
        return RecordType(clang_type)
    elif clang_type.kind == TypeKind.TYPEDEF:
        return TypedefType(clang_type)
    elif clang_type.kind == TypeKind.VOID:
        return VoidType(clang_type)
    else:
        assert False


def py_type_name(capi_type: str) -> str:
    s = capi_type
    if s.startswith("Xr"):
        s = s[2:]
    return s


__all__ = [
    "CodeGenerator",
]
