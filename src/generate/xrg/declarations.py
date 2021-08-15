from abc import ABC, abstractmethod
import inspect
import re
from typing import Generator

from clang.cindex import Cursor, CursorKind, TokenKind, TypeKind

from .types import Api, py_type_name, parse_type, capi_type_name, StringType
from .registry import xr_registry


class SkippableCodeItemException(Exception):
    pass


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
    def used_ctypes(self, api=Api.PYTHON) -> set[str]:
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

    def used_ctypes(self, api=Api.PYTHON) -> set[str]:
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
            return self._py_name
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

    def used_ctypes(self, api=Api.PYTHON) -> set[str]:
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
        prefix = snake_from_camel(prefix).upper() + "_"
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

    def used_ctypes(self, api=Api.PYTHON) -> set[str]:
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
        s = capi_name
        if s.startswith("xr"):
            s = s[2:]
        return snake_from_camel(s)

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
                {self.name(Api.C)}.restype = {self.return_type.name(Api.PYTHON)}
                {self.name(Api.C)}.argtypes = [
                """)
            for p in self.parameters:
                result += f"\n    {p.type.name(api)},  # {p.name(Api.PYTHON)}"
            result += "\n]"
            return result
        elif api == Api.PYTHON:
            return str(FunctionCoder(self))
        elif api == Api.C:
            raise NotImplementedError

    def used_ctypes(self, api=Api.PYTHON) -> set[str]:
        result = self.return_type.used_ctypes(api)
        for p in self.parameters:
            result.update(p.used_ctypes(api))
        return result


class FunctionParameterItem(CodeItem):
    def __init__(self, cursor: Cursor):
        super().__init__(cursor)
        assert cursor.kind == CursorKind.PARM_DECL
        self._capi_name = cursor.spelling
        self._py_name = snake_from_camel(self._capi_name)
        self.type = parse_type(cursor.type)
        self._optional = False
        # Query xr registry to see if this parameter is optional
        if xr_registry:
            function_c_name = cursor.semantic_parent.spelling
            try:
                command = xr_registry.find(f'commands/command/proto[name="{function_c_name}"]/..')
                this_param = command.find(f'param[name="{self._capi_name}"]')
                self._optional = this_param.attrib["optional"] == "true"
            except Exception as exc:
                pass

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

    def is_optional(self) -> bool:
        return self._optional

    def used_ctypes(self, api=Api.PYTHON) -> set[str]:
        return self.type.used_ctypes(api)


class StructFieldItem(CodeItem):
    def __init__(self, cursor: Cursor) -> None:
        super().__init__(cursor)
        assert cursor.kind == CursorKind.FIELD_DECL
        self._capi_name = cursor.spelling
        self._py_name = snake_from_camel(self._capi_name)
        self.type = parse_type(cursor.type)

    def name(self, api=Api.PYTHON) -> str:
        if api == api.PYTHON:
            return self._py_name
        elif api == api.C:
            return self._capi_name
        elif api == api.CTYPES:
            return self._py_name
        else:
            raise NotImplementedError

    def code(self, api=Api.PYTHON) -> str:
        if api == Api.C:
            raise NotImplementedError
        return f'\n        ("{self.name(api)}", {self.type.name(api)}),'

    def used_ctypes(self, api=Api.PYTHON) -> set[str]:
        return self.type.used_ctypes(api)


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
            m = re.search(fr"\b{self.name(Api.CTYPES)}\b", f.type.name(Api.CTYPES))
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
            return self._py_name
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
        result += "".join([f.code(Api.CTYPES) for f in self.fields])
        result += "\n    ]"
        return result

    def used_ctypes(self, api=Api.PYTHON) -> set[str]:
        result = {
            "Structure",
        }
        for f in self.fields:
            result.update(f.used_ctypes(Api.CTYPES))
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
        if self._py_name == self.type.name(Api.CTYPES):
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
        return f"{self.name(api)} = {self.type.name(Api.CTYPES)}"

    def used_ctypes(self, api=Api.PYTHON) -> set[str]:
        return self.type.used_ctypes(Api.CTYPES)


class VariableItem(CodeItem):
    def __init__(self, cursor: Cursor) -> None:
        super().__init__(cursor)
        assert cursor.kind == CursorKind.VAR_DECL
        self._capi_name = cursor.spelling
        if not self._capi_name.startswith("XR_"):
            assert False
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
            elif e.kind == CursorKind.INTEGER_LITERAL:
                tokens = list(e.get_tokens())
                assert tokens[0].kind == TokenKind.LITERAL
                self.value = tokens[0].spelling
            else:
                assert False
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

    def used_ctypes(self, api=Api.PYTHON) -> set[str]:
        return set()


class ParameterCoderBase(object):
    def __init__(self, parameter: FunctionParameterItem):
        self.parameter = parameter

    @staticmethod
    def declaration_code(api=Api.PYTHON) -> Generator[str, None, None]:
        yield from []

    def main_call_code(self, api=Api.PYTHON) -> Generator[str, None, None]:
        yield f"{self.parameter.name(api)}"

    @staticmethod
    def pre_body_code(api=Api.PYTHON) -> Generator[str, None, None]:
        yield from []

    @staticmethod
    def result_code(api=Api.PYTHON) -> Generator[str, None, None]:
        yield from []


class BufferCapacityInputParameterCoder(ParameterCoderBase):
    def pre_body_code(self, api=Api.PYTHON) -> Generator[str, None, None]:
        yield f"{self.parameter.name(api)} = {self.parameter.type.name(Api.CTYPES)}(0)"


class BufferCountOutputParameterCoder(ParameterCoderBase):
    pass


class BufferOutputArrayCoder(ParameterCoderBase):
    def result_code(self, api=Api.PYTHON) -> Generator[str, None, None]:
        if self.parameter.type.clang_type.spelling == "char *":  # string case
            assert not self.parameter.type.clang_type.get_pointee().is_const_qualified()
            yield "str"
        else:  # array case
            yield f"Array[{self.parameter.type.pointee.name()}]"


class InputParameterCoder(ParameterCoderBase):
    def declaration_code(self, api=Api.PYTHON) -> Generator[str, None, None]:
        # TODO: default value (from docstring?) e.g. None for string that can be empty
        p = self.parameter
        yield f"{p.name(api)}: {p.type.name(Api.PYTHON)}"


# TODO: use this new class
class StringInputParameterCoder(InputParameterCoder):
    def pre_body_code(self, api=Api.PYTHON) -> Generator[str, None, None]:
        yield f"ubx_{self.parameter.name(api)} = None"
        yield f"if {self.parameter.name(api)} is not None:"
        yield f"    ubx_{self.parameter.name(api)} = {self.parameter.name(api)}.encode()"


class FunctionCoder(object):
    def __init__(self, function: FunctionItem):
        self.function = function
        # TODO: categorize parameters finely
        # TODO: buffer size parameters
        self.param_coders = [[p, None] for p in self.function.parameters]
        # First pass: Buffer size arguments
        for ix, pc in enumerate(self.param_coders):
            p, c = pc
            if p.name().endswith("_capacity_input"):
                # OpenXR buffer size parameters consist of three consecutive parameters
                assert "int" in p.type.name()
                self.param_coders[ix][1] = BufferCapacityInputParameterCoder(p)
                p2 = self.param_coders[ix + 1][0]
                assert p2.name().endswith("_count_output")
                assert p2.type.clang_type.kind == TypeKind.POINTER
                assert "int" in p2.type.pointee.name()
                self.param_coders[ix + 1][1] = BufferCountOutputParameterCoder(p2)
                p3 = self.param_coders[ix + 2][0]
                assert p2.type.clang_type.kind == TypeKind.POINTER
                self.param_coders[ix + 2][1] = BufferOutputArrayCoder(p3)
        # Assume remainder are simple inputs
        for ix, pc in enumerate(self.param_coders):
            p, c = pc
            if c is not None:
                continue
            if isinstance(p.type, StringType):
                pc[1] = StringInputParameterCoder(p)
                continue
            pc[1] = InputParameterCoder(p)

    def declaration_code(self, api=Api.PYTHON) -> str:
        params = ""
        result_types = []
        for p, c in self.param_coders:
            for s in c.declaration_code(api):
                params += f"\n{' ' * 16}{s},"
            for r in c.result_code(Api.PYTHON):
                result_types.append(r)
        if len(result_types) == 0:
            result = "None"
        elif len(result_types) == 1:
            result = result_types[0]
        else:
            result = f"({', '.join(result_types)})"
        return inspect.cleandoc(f"""
            def {self.function.name(api)}({params}
            ) -> {result}:
        """)

    def __str__(self, api=Api.PYTHON):
        result = self.declaration_code(api)
        docstring = ""
        result += f'\n    """{docstring}"""'
        for p, c in self.param_coders:
            for line in c.pre_body_code():
                result += f"\n    {line}"
        result += f"\n    fxn = raw_functions.{self.function.name(Api.CTYPES)}"
        result += f"\n    result = check_result(fxn("
        result += f"\n    ))"
        result += f"\n    if result.is_exception():"
        result += f"\n        raise result"
        return result


def snake_from_camel(camel: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", camel).lower()


__all__ = [
    "CodeItem",
    "DefinitionItem",
    "EnumItem",
    "FunctionItem",
    "SkippableCodeItemException",
    "StructItem",
    "TypeDefItem",
    "VariableItem",
]
