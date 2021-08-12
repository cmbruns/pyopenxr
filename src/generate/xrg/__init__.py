"""
File xrg.__init__.py

This module contains code to help generate the code in pyopenxr.
"""

# TODO:
#  * generate docstrings

from abc import ABC, abstractmethod
import enum
import inspect
import os
import re
from typing import Generator

import clang.cindex
from clang.cindex import Cursor, CursorKind, Index, TranslationUnit, TypeKind

# These variables are filled in by CMake during the configure step
# OPENXR_HEADER = "@OPENXR_INCLUDE_FILE@"
# if os.path.isfile("@LIBCLANG_SHARED_LIBRARY@"):
#     clang.cindex.Config.set_library_file("@LIBCLANG_SHARED_LIBRARY@")

# TODO: remove hard-coded versions
OPENXR_HEADER = "C:/Program Files/OPENXR/include/openxr/openxr.h"
if os.path.isfile("C:/Program Files/LLVM/bin/libclang.dll"):
    clang.cindex.Config.set_library_file("C:/Program Files/LLVM/bin/libclang.dll")

##############
# Exceptions #
##############


class SkippableCodeItemException(Exception):
    pass


################
# Type classes #
################


class Api(enum.Enum):
    C = 1,  # symbols and code from the original C file
    CTYPES = 2,  #
    PYTHON = 3,  # High level pythonic interface symbols


class TypeBase(ABC):
    def __init__(self, clang_type: clang.cindex.Type):
        self.clang_type = clang_type

    @abstractmethod
    def code(self, api=Api.PYTHON) -> str:
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

    def code(self, api=Api.PYTHON) -> str:
        if api == Api.C:
            return f"{self.element_type.code(api)}[{self.count}]"
        else:
            return f"({self.element_type.code(api)} * {self.count})"

    def used_ctypes(self) -> set[str]:
        return self.element_type.used_ctypes()


class EnumType(TypeBase):
    def __init__(self, clang_type: clang.cindex.Type):
        super().__init__(clang_type)
        assert clang_type.kind == TypeKind.ENUM

    def code(self, api=Api.PYTHON) -> str:
        if api == Api.C:
            return self.clang_type.spelling
        elif api == Api.CTYPES:
            return "c_int"
        else:
            return "c_int"  # TODO we could use the actual name if we had the enums loaded

    def used_ctypes(self) -> set[str]:
        return {
            "c_int",
        }


class FunctionPointerType(TypeBase):
    def __init__(self, clang_type: clang.cindex.Type):
        super().__init__(clang_type)
        assert clang_type.kind == TypeKind.POINTER
        pt = clang_type.get_pointee()
        assert pt.kind == TypeKind.FUNCTIONPROTO
        self.result_type = parse_type(pt.get_result())
        self.arg_types = [parse_type(t) for t in pt.argument_types()]

    def code(self, api=Api.PYTHON) -> str:
        if api == api.C:
            return self.clang_type.spelling
        else:
            arg_string = ", ".join(
                a.code(api) for a in [self.result_type, *self.arg_types]
            )
            return f"CFUNCTYPE({arg_string})"

    def used_ctypes(self) -> set[str]:
        result = {
            "CFUNCTYPE",
        }
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

    def code(self, api=Api.PYTHON) -> str:
        if api == Api.C:
            return self.clang_type.spelling
        else:
            return f"POINTER({self.pointee.code(api)})"

    def used_ctypes(self) -> set[str]:
        result = self.pointee.used_ctypes()
        result.add("POINTER")
        return result


class PrimitiveCTypesType(TypeBase):
    def __init__(self, clang_type: clang.cindex.Type, ctypes_type: str):
        super().__init__(clang_type)
        self.name = ctypes_type

    def code(self, api=Api.PYTHON) -> str:
        if api == Api.C:
            return self.clang_type.spelling
        else:
            return self.name

    def used_ctypes(self) -> set[str]:
        return {
            self.name,
        }


class RecordType(TypeBase):
    def __init__(self, clang_type: clang.cindex.Type):
        super().__init__(clang_type)
        assert clang_type.kind == TypeKind.RECORD
        self._capi_name = capi_type_name(clang_type.get_declaration().spelling)
        self._py_name = py_type_name(self._capi_name)

    def code(self, api=Api.PYTHON) -> str:
        if api == Api.C:
            return self.clang_type.spelling
        elif api == Api.CTYPES:
            return self._capi_name
        elif api == Api.PYTHON:
            return self._py_name
        else:
            raise NotImplementedError

    def used_ctypes(self) -> set[str]:
        return set()


class TypedefType(TypeBase):
    def __init__(self, clang_type: clang.cindex.Type):
        super().__init__(clang_type)
        assert clang_type.kind == TypeKind.TYPEDEF
        type_name = clang_type.spelling
        m = re.match(r"(?:const )?(u?int(?:8|16|32|64))_t", type_name)
        if m:
            type_name = f"c_{m.group(1)}"
        self._capi_name = capi_type_name(type_name)
        self._py_name = py_type_name(self._capi_name)
        self.underlying_type = parse_type(
            clang_type.get_declaration().underlying_typedef_type
        )

    def code(self, api=Api.PYTHON) -> str:
        if api == Api.C:
            return self.clang_type.spelling
        elif api == Api.CTYPES:
            return self._capi_name
        elif api == Api.PYTHON:
            return self._py_name
        else:
            raise NotImplementedError

    def used_ctypes(self) -> set[str]:
        if self._capi_name.startswith("c_"):
            return {
                self._capi_name,
            }
        else:
            return self.underlying_type.used_ctypes()


class VoidType(TypeBase):
    def __init__(self, clang_type: clang.cindex.Type):
        super().__init__(clang_type)
        assert clang_type.kind == TypeKind.VOID

    def code(self, api=Api.PYTHON) -> str:
        if api == Api.C:
            return "void"
        else:
            return "None"

    def used_ctypes(self) -> set[str]:
        return set()


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
    def name(self, api=Api.PYTHON) -> str:
        pass

    @abstractmethod
    def code(self, api=Api.PYTHON) -> str:
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
        self.c_value = tokens[0].spelling
        self.value = self.c_value
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

    def name(self, api=Api.PYTHON) -> str:
        if api == api.PYTHON:
            return self._py_name
        elif api == api.C:
            return self._capi_name
        elif api == api.CTYPES:
            return self._capi_name
        else:
            raise NotImplementedError

    def code(self, api=Api.PYTHON) -> str:
        if api == api.C:
            return f"#define {self.name(api)} {self.c_value}"
        return f"{self.name(api)} = {self.value}"

    def used_ctypes(self) -> set[str]:
        return set()


class EnumItem(CodeItem):
    def __init__(self, cursor: Cursor) -> None:
        super().__init__(cursor)
        assert cursor.kind == CursorKind.ENUM_DECL
        self._capi_name = cursor.spelling
        self._py_name = py_type_name(self._capi_name)
        self.values = []
        for v in cursor.get_children():
            assert v.kind == CursorKind.ENUM_CONSTANT_DECL
            self.values.append(EnumValueItem(cursor=v, parent=self))

    @staticmethod
    def blank_lines_before():
        return 2

    @staticmethod
    def blank_lines_after():
        return 1

    def name(self, api=Api.PYTHON) -> str:
        if api == api.PYTHON:
            return self._py_name
        elif api == api.C:
            return self._capi_name
        elif api == api.CTYPES:
            return self._capi_name
        else:
            raise NotImplementedError

    def code(self, api=Api.PYTHON) -> str:
        if api == api.CTYPES:
            result = f"{self.name(api)} = c_int"
            for v in self.values:
                result += f"\n{v.code(api)}"
            return result
        elif api == api.PYTHON:
            result = f"class {self.name(api)}(enum.Enum):"
            value_count = 0
            for v in self.values:
                if v.name(api) == "_MAX_ENUM":
                    continue
                result += v.code(api)
                value_count += 1
            if value_count < 1:
                result += "\n    pass"
            return result
        elif api == api.C:
            # TODO: this is probably not tested...
            result = f"{self.name(api)} {{"  # Q: does this already have "enum" at the beginning?
            for v in self.values:
                result += f"    \n{v.code(api)}"
            result += "\n}"
            return result

    def used_ctypes(self) -> set[str]:
        return {
            "c_int",
        }


class EnumValueItem(CodeItem):
    # Certain enums name their values differently than others
    _PREFIX_TABLE = {
        "RESULT_": "",
        "STRUCTURE_TYPE_": "TYPE_",
        "PERF_SETTINGS_NOTIFICATION_LEVEL_": "PERF_SETTINGS_NOTIF_LEVEL_",
    }

    def __init__(self, cursor: Cursor, parent: EnumItem) -> None:
        super().__init__(cursor)
        assert cursor.kind == CursorKind.ENUM_CONSTANT_DECL
        self.parent = parent
        self._capi_name = cursor.spelling
        self._py_name = self._make_py_name()
        self.value = self.cursor.enum_value

    def _make_py_name(self):
        # Compute pythonic name...
        n = self._capi_name
        assert n.startswith("XR_")
        n = n[3:]  # Strip off initial "XR_"
        prefix = self.parent.name(Api.PYTHON)
        postfix = ""
        for postfix1 in ["EXT", "FB", "KHR", "MSFT"]:
            if prefix.endswith(postfix1):
                prefix = prefix[: -len(postfix1)]
                postfix = f"_{postfix1}"
                break
        prefix = (
            re.sub(r"(?<!^)(?=[A-Z])", "_", prefix).upper() + "_"
        )  # snake from camel
        if n == f"{prefix}MAX_ENUM{postfix}":
            return f"_MAX_ENUM"  # private enum value
        if prefix in self._PREFIX_TABLE:
            prefix = self._PREFIX_TABLE[prefix]
        assert n.startswith(prefix)
        n = n[len(prefix):]
        if len(postfix) > 0:
            n = n[: -len(postfix)]  # It's already in the parent enum name
        return n

    @staticmethod
    def blank_lines_before():
        return 0

    @staticmethod
    def blank_lines_after():
        return 0

    def name(self, api=Api.PYTHON) -> str:
        if api == api.PYTHON:
            return self._py_name
        elif api == api.C:
            return self._capi_name
        elif api == api.CTYPES:
            return self._capi_name
        else:
            raise NotImplementedError

    def code(self, api=Api.PYTHON) -> str:
        line_end = ""
        line_indent = "    "
        if api == Api.C:
            line_end = ","  # TODO: but not the last one, right?
        elif api == Api.CTYPES:
            line_indent = ""
        return f"\n{line_indent}{self.name(api)} = {self.value}{line_end}"

    def used_ctypes(self) -> set[str]:
        return {
            "c_int",
        }


class FunctionItem(CodeItem):
    def __init__(self, cursor: Cursor) -> None:
        super().__init__(cursor)
        assert cursor.kind == CursorKind.FUNCTION_DECL
        self._capi_name = cursor.spelling
        self._py_name = self._py_function_name(self._capi_name)
        self.parameters = []
        self.return_type = None
        for c in cursor.get_children():
            if c.kind == CursorKind.TYPE_REF:
                assert self.return_type is None
                self.return_type = parse_type(c.type)
            elif c.kind == CursorKind.PARM_DECL:
                self.parameters.append(FunctionParameterItem(c))
            else:
                assert False

    @staticmethod
    def _py_function_name(capi_name: str) -> str:
        # TODO: snake case
        s = capi_name
        if s.startswith("xr"):
            s = s[2:]
        return s

    @staticmethod
    def blank_lines_before():
        return 2

    @staticmethod
    def blank_lines_after():
        return 2

    def name(self, api=Api.PYTHON) -> str:
        if api == api.PYTHON:
            return self._py_name
        elif api == api.C:
            return self._capi_name
        elif api == api.CTYPES:
            return self._capi_name
        else:
            raise NotImplementedError

    def code(self, api=Api.PYTHON) -> str:
        if api == Api.CTYPES:
            # ctypes raw function definition
            result = inspect.cleandoc(
                f"""
                {self.name(Api.C)} = openxr_loader_library.{self.name(Api.C)}
                {self.name(Api.C)}.restype = {self.return_type.code(Api.PYTHON)}
                {self.name(Api.C)}.argtypes = [
                """)
            for p in self.parameters:
                result += f"\n    {p.type.code(Api.PYTHON)},  # {p.name(Api.PYTHON)}"
            result += "\n]"
            return result
        elif api == Api.PYTHON:
            # TODO: python functions are pretty complicated
            return f"def {self.name(api)}() -> :\n    pass"
        elif api == Api.C:
            raise NotImplementedError

    def used_ctypes(self) -> set[str]:
        result = self.return_type.used_ctypes()
        for p in self.parameters:
            result.update(p.used_ctypes())
        return result


class FunctionParameterItem(CodeItem):
    def __init__(self, cursor: Cursor):
        super().__init__(cursor)
        assert cursor.kind == CursorKind.PARM_DECL
        self._capi_name = cursor.spelling
        self._py_name = re.sub(
            r"(?<!^)(?=[A-Z])", "_", self._capi_name
        ).lower()  # snake from camel
        self.type = parse_type(cursor.type)

    def name(self, api=Api.PYTHON) -> str:
        if api == api.PYTHON:
            return self._py_name
        elif api == api.C:
            return self._capi_name
        elif api == api.CTYPES:
            return self._capi_name
        else:
            raise NotImplementedError

    def code(self, api=Api.PYTHON) -> str:
        pass

    def used_ctypes(self) -> set[str]:
        return self.type.used_ctypes()


class StructFieldItem(CodeItem):
    def __init__(self, cursor: Cursor) -> None:
        super().__init__(cursor)
        assert cursor.kind == CursorKind.FIELD_DECL
        self._capi_name = cursor.spelling
        self._py_name = re.sub(
            r"(?<!^)(?=[A-Z])", "_", self._capi_name
        ).lower()  # snake from camel
        self.type = parse_type(cursor.type)

    def name(self, api=Api.PYTHON) -> str:
        if api == api.PYTHON:
            return self._py_name
        elif api == api.C:
            return self._capi_name
        elif api == api.CTYPES:
            return self._capi_name
        else:
            raise NotImplementedError

    def code(self, api=Api.PYTHON) -> str:
        if api == Api.C:
            raise NotImplementedError
        return f'\n        ("{self.name(api)}", {self.type.code(api)}),'

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
            m = re.search(fr"\b{self.name(Api.CTYPES)}\b", f.type.code(Api.CTYPES))
            if m:
                self.is_recursive = True

    @staticmethod
    def blank_lines_before():
        return 2

    @staticmethod
    def blank_lines_after():
        return 2

    def name(self, api=Api.PYTHON) -> str:
        if api == api.PYTHON:
            return self._py_name
        elif api == api.C:
            return self._capi_name
        elif api == api.CTYPES:
            return self._capi_name
        else:
            raise NotImplementedError

    def code(self, api=Api.PYTHON) -> str:
        if api == Api.C:
            raise NotImplementedError
        result = f"class {self.name(api)}(Structure):"
        if len(self.fields) == 0:
            # Empty structure
            result += "\n    pass"
            return result
        if self.is_recursive:
            # Structure containing self-reference must be declared in two stanzas
            result += "\n    pass"
            result += f"\n\n\n{self.name(api)}._fields_ = ["
        else:
            result += "\n    _fields_ = ["
        result += "".join([f.code(api) for f in self.fields])
        result += "\n    ]"
        return result

    def used_ctypes(self) -> set[str]:
        result = {
            "Structure",
        }
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
        if self.type.clang_type.kind == TypeKind.ENUM:
            raise SkippableCodeItemException  # Keep enum typedefs out of typedefs.py
        if self._capi_name == self.type.code(Api.CTYPES):
            raise SkippableCodeItemException  # Nonsense A = A typedef

    def name(self, api=Api.PYTHON) -> str:
        if api == api.PYTHON:
            return self._py_name
        elif api == api.C:
            return self._capi_name
        elif api == api.CTYPES:
            return self._capi_name
        else:
            raise NotImplementedError

    def code(self, api=Api.PYTHON) -> str:
        if api == Api.C:
            raise NotImplementedError
        return f"{self.name(api)} = {self.type.code(api)}"

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

    def name(self, api=Api.PYTHON) -> str:
        if api == api.PYTHON:
            return self._py_name
        elif api == api.C:
            return self._capi_name
        elif api == api.CTYPES:
            return self._capi_name
        else:
            raise NotImplementedError

    def code(self, api=Api.PYTHON) -> str:
        if api == Api.C:
            raise NotImplementedError
        return f"{self.name(api)} = {self.value}"

    def used_ctypes(self) -> set[str]:
        return set()


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

    def print_header(self) -> None:
        for t in self.items:
            self.ctypes_names.update(t.used_ctypes())
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


def parse_type(clang_type: clang.cindex.Type) -> TypeBase:
    if clang_type.kind == TypeKind.CHAR_S:
        return PrimitiveCTypesType(clang_type, "c_char")
    elif clang_type.kind == TypeKind.CONSTANTARRAY:
        return ArrayType(clang_type)
    elif clang_type.kind == TypeKind.ELABORATED:
        return parse_type(clang_type.get_named_type())
    elif clang_type.kind == TypeKind.ENUM:
        return EnumType(clang_type)
    elif clang_type.kind == TypeKind.FLOAT:
        return PrimitiveCTypesType(clang_type, "c_float")
    elif clang_type.kind == TypeKind.INT:
        return PrimitiveCTypesType(clang_type, "c_int")
    elif clang_type.kind == TypeKind.LONGLONG:
        return PrimitiveCTypesType(clang_type, "c_longlong")
    elif clang_type.kind == TypeKind.POINTER:
        pt = clang_type.get_pointee()
        if pt.kind == TypeKind.CHAR_S:
            # But this works ONLY if these are always null terminated strings
            return PrimitiveCTypesType(clang_type, "c_char_p")
        elif pt.kind == TypeKind.FUNCTIONPROTO:
            return FunctionPointerType(clang_type)
        elif pt.kind == TypeKind.VOID:
            return PrimitiveCTypesType(clang_type, "c_void_p")
        else:
            return PointerType(clang_type)
    elif clang_type.kind == TypeKind.RECORD:
        return RecordType(clang_type)
    elif clang_type.kind == TypeKind.TYPEDEF:
        return TypedefType(clang_type)
    elif clang_type.kind == TypeKind.UCHAR:
        return PrimitiveCTypesType(clang_type, "c_uchar")
    elif clang_type.kind == TypeKind.UINT:
        return PrimitiveCTypesType(clang_type, "c_uint")
    elif clang_type.kind == TypeKind.ULONGLONG:
        return PrimitiveCTypesType(clang_type, "c_ulonglong")
    elif clang_type.kind == TypeKind.USHORT:
        return PrimitiveCTypesType(clang_type, "c_ushort")
    elif clang_type.kind == TypeKind.VOID:
        return VoidType(clang_type)

    m = re.match(r"(?:const )?(u?int(?:8|16|32|64))_t", clang_type.spelling)
    if m:
        return PrimitiveCTypesType(clang_type, f"c_{m.group(1)}")

    assert False


def py_type_name(capi_type: str) -> str:
    s = capi_type
    if s.startswith("Xr"):
        s = s[2:]
    return s


__all__ = [
    "Api",
    "get_header_as_string",
    "CodeGenerator",
    "CodeItem",
    "EnumItem",
    "FunctionItem",
]
