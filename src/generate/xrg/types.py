import enum
import re
from abc import ABC, abstractmethod

import clang.cindex
from clang.cindex import TypeKind


class Api(enum.Enum):
    C = 1,  # C language symbols and code from the original C file
    CTYPES = 2,  # Python code with maximum similarity to C code
    PYTHON = 3,  # High-level pythonic interface symbols and code


class TypeBase(ABC):
    def __init__(self, clang_type: clang.cindex.Type):
        self.clang_type = clang_type

    @abstractmethod
    def code(self, api=Api.PYTHON) -> str:
        pass

    @abstractmethod
    def used_ctypes(self, api=Api.PYTHON) -> set[str]:
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

    def used_ctypes(self, api=Api.PYTHON) -> set[str]:
        return self.element_type.used_ctypes(api)


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

    def used_ctypes(self, api=Api.PYTHON) -> set[str]:
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

    def used_ctypes(self, api=Api.PYTHON) -> set[str]:
        result = {
            "CFUNCTYPE",
        }
        result.update(self.result_type.used_ctypes(api))
        result.update(self.result_type.used_ctypes(api))
        for a in self.arg_types:
            result.update(a.used_ctypes(api))
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

    def used_ctypes(self, api=Api.PYTHON) -> set[str]:
        result = self.pointee.used_ctypes(api)
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

    def used_ctypes(self, api=Api.PYTHON) -> set[str]:
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

    def used_ctypes(self, api=Api.PYTHON) -> set[str]:
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

    def used_ctypes(self, api=Api.PYTHON) -> set[str]:
        if api == Api.C:
            return set()
        elif self._capi_name.startswith("c_"):
            return {
                self._capi_name,
            }
        else:
            return set()


class VoidType(TypeBase):
    def __init__(self, clang_type: clang.cindex.Type):
        super().__init__(clang_type)
        assert clang_type.kind == TypeKind.VOID

    def code(self, api=Api.PYTHON) -> str:
        if api == Api.C:
            return "void"
        else:
            return "None"

    def used_ctypes(self, api=Api.PYTHON) -> set[str]:
        return set()


def capi_type_name(c_type_name: str) -> str:
    """The low level C-like api uses the exact same names as in C"""
    s = re.sub(r"\b(?:const|volatile)\s+", "", c_type_name)  # But without const
    return s


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
    "ArrayType",
    "capi_type_name",
    "EnumType",
    "FunctionPointerType",
    "PointerType",
    "parse_type",
    "PrimitiveCTypesType",
    "py_type_name",
    "RecordType",
    "TypeBase",
    "TypedefType",
    "VoidType",
]
