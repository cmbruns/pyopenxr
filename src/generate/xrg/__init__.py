"""
File xrg.__init__.py

This module contains code to help generate the code in pyopenxr.
"""

import clang.cindex
from clang.cindex import TypeKind
import os
import re

# These variables are filled in by cmake's configure_file process
# OPENXR_HEADER = "@OPENXR_INCLUDE_FILE@"
# if os.path.isfile("@LIBCLANG_SHARED_LIBRARY@"):
#     clang.cindex.Config.set_library_file("@LIBCLANG_SHARED_LIBRARY@")

# TODO: remove hard-coded versions
OPENXR_HEADER = "C:/Program Files/OPENXR/include/openxr/openxr.h"
if os.path.isfile("C:/Program Files/LLVM/bin/libclang.dll"):
    clang.cindex.Config.set_library_file("C:/Program Files/LLVM/bin/libclang.dll")


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
    def capi_type_name(c_type_name: str, snake=False) -> str:
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
    def pyapi_type_name(c_type_name: str, snake=False) -> str:
        """Convert raw C symbol name to pythonic name"""
        s = TypeNameMapper.capi_type_name(c_type_name)
        s = re.sub(r"\bXr", "", s)
        return s


__all__ = [
    "TypeNameMapper",
]
