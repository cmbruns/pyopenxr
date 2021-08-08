"""
File xrg.__init__.py

This module contains code to help generate the code in pyopenxr.
"""

from abc import ABC, abstractmethod
import clang.cindex
from clang.cindex import CursorKind, TypeKind
import os
import re

# These variables are filled in by CMake during the configure_file process
# OPENXR_HEADER = "@OPENXR_INCLUDE_FILE@"
# if os.path.isfile("@LIBCLANG_SHARED_LIBRARY@"):
#     clang.cindex.Config.set_library_file("@LIBCLANG_SHARED_LIBRARY@")

# TODO: remove hard-coded versions
OPENXR_HEADER = "C:/Program Files/OPENXR/include/openxr/openxr.h"
if os.path.isfile("C:/Program Files/LLVM/bin/libclang.dll"):
    clang.cindex.Config.set_library_file("C:/Program Files/LLVM/bin/libclang.dll")

################


class SkippableCodeItemException(Exception):
    pass

################
# Type objects #
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


class VoidType(TypeBase):
    def __init__(self, clang_type: clang.cindex.Type):
        super().__init__(clang_type)
        assert clang_type.kind == TypeKind.VOID

    def capi_string(self) -> str:
        return "None"

    def py_string(self) -> str:
        return "None"


####################
# CodeItem objects #
####################

class CodeItem(ABC):
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


class TypeDefItem(CodeItem):
    def __init__(self, cursor: clang.cindex.Cursor):
        assert cursor.kind == CursorKind.TYPEDEF_DECL
        self._capi_name = cursor.spelling
        self._py_name = py_type_name(self._capi_name)
        self.type = parse_type(cursor.underlying_typedef_type)
        if self._capi_name == self.type.capi_string():
            raise SkippableCodeItemException  # Nonsense A = A typedef
        self.name = self._py_name  # TODO: remove

    # TODO: remove
    def __str__(self):
        return self.py_string()

    def capi_name(self) -> str:
        return self._capi_name

    def capi_string(self) -> str:
        return f"{self.capi_name()} = {self.type.capi_string()}"

    def py_name(self) -> str:
        return self._py_name

    def py_string(self) -> str:
        return f"{self.py_name()} = {self.type.py_string()}"


##########################

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


def capi_type_name(c_type_name: str) -> str:
    """The low level C-like api uses the exact same names as in C"""
    s = re.sub(r"\b(?:const|volatile)\s+", "", c_type_name)  # But without const
    return s


def py_type_name(capi_type: str) -> str:
    s = capi_type
    if s.startswith("Xr"):
        s = s[2:]
    return s


# TODO: remove below here
class TypeNameMapper(object):
    def __init__(self, use_pyapi=True):
        # remember names of ctypes types used, for use in import statement
        self.ctypes_cache = {"POINTER", "CFUNCTYPE", "Structure"}
        self.use_pyapi = use_pyapi

    def _ctypes_cache(self, ctypes_name: str) -> str:
        """Remember a ctypes type name in the cache then return it"""
        self.ctypes_cache.add(ctypes_name)
        return ctypes_name

    def api_type_string(self, c_type_name: str) -> str:
        if self.use_pyapi:
            return self.pyapi_type_name(c_type_name)
        else:
            return self.capi_type_name(c_type_name)

    def api_type(self, clang_type: clang.cindex.Type) -> str:
        """Return API-specific (either pythonic or C-like) type name corresponding to parsed clang type"""
        return self.api_type_string(self.ctypes_name(clang_type))

    @staticmethod
    def capi_type_name(c_type_name: str) -> str:
        """The low level C-like api uses the exact same names as in C"""
        s = re.sub(r"\b(?:const|volatile)\s+", "", c_type_name)  # But without const
        return s

    def ctypes_import(self) -> str:
        """Return import statement for used ctypes types"""
        return f"from ctypes import {', '.join(sorted(self.ctypes_cache))}"

    def ctypes_name(self, clang_type: clang.cindex.Type) -> str:
        """Return the ctypes type name corresponding to a parsed clang type."""
        m = re.match(r"(?:const )?(u?int(?:8|16|32|64))_t", clang_type.spelling)
        if m:
            return self._ctypes_cache(f"c_{m.group(1)}")
        elif clang_type.kind == TypeKind.CHAR_S:
            return self._ctypes_cache("c_char")
        elif clang_type.kind == TypeKind.CONSTANTARRAY:
            return f"({self.api_type(clang_type.element_type)} * {clang_type.element_count})"
        elif clang_type.kind == TypeKind.ELABORATED:
            return self.api_type(clang_type.get_named_type())
        elif clang_type.kind == TypeKind.ENUM:
            return self._ctypes_cache("c_uint32")
        elif clang_type.kind == TypeKind.FLOAT:
            return self._ctypes_cache("c_float")
        elif clang_type.kind == TypeKind.POINTER:
            pt = clang_type.get_pointee()
            if pt.kind == TypeKind.FUNCTIONPROTO:
                args = [pt.get_result(), *(pt.argument_types())]
                arg_string = ", ".join([self.api_type(a) for a in args])
                return f"CFUNCTYPE({arg_string})"
            elif pt.kind == TypeKind.VOID:
                return self._ctypes_cache("c_void_p")
            else:
                return f"POINTER({self.api_type(pt)})"
        elif clang_type.kind == TypeKind.RECORD:
            return clang_type.get_declaration().spelling
        elif clang_type.kind == TypeKind.TYPEDEF:
            return clang_type.spelling
        elif clang_type.kind == TypeKind.VOID:
            return "None"
        else:
            assert False

    @staticmethod
    def pyapi_type_name(c_type_name: str) -> str:
        """Convert raw C symbol name to pythonic name"""
        s = TypeNameMapper.capi_type_name(c_type_name)
        s = re.sub(r"\bXr", "", s)
        return s


__all__ = [
    "parse_type",
    "TypeDefItem",
    "TypeNameMapper",
    "SkippableCodeItemException",
]
