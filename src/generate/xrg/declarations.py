from abc import ABC, abstractmethod
import inspect
import re
import textwrap
from typing import Generator, Set

from clang.cindex import Cursor, CursorKind, TokenKind, TypeKind

from .types import *
from .registry import xr_registry
from .vendor_tags import vendor_tags


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
    def used_ctypes(self, api=Api.PYTHON) -> Set[str]:
        pass


class DefinitionItem(CodeItem):
    def __init__(self, cursor: Cursor) -> None:
        super().__init__(cursor)
        assert cursor.kind == CursorKind.MACRO_DEFINITION
        self._capi_name = cursor.spelling
        if self._capi_name.endswith("_"):
            raise SkippableCodeItemException  # OPENVR_H_
        tokens = list(cursor.get_tokens())[1:]
        self.c_value = tokens[0].spelling
        if len(tokens) > 1:
            if tokens[0].spelling == "-" and len(tokens) == 2:
                self.c_value += tokens[1].spelling  # Don't skip simple negative values
            else:
                raise SkippableCodeItemException  # We only want simple #define values
        self.value = self.c_value
        if self.value is None:
            raise SkippableCodeItemException  # #define with no value
        assert self._capi_name.startswith("XR_")
        self._py_name = self._capi_name[3:]
        if self.value.endswith("LL"):
            self.value = self.value[:-2]
        if self.value.startswith("XR_"):
            self.value = self.value[3:]

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

    def used_ctypes(self, api=Api.PYTHON) -> Set[str]:
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
            result = f"class {self.name(api)}(EnumBase):"
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

    def used_ctypes(self, api=Api.PYTHON) -> Set[str]:
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
        for postfix1 in vendor_tags:
            if prefix.endswith(postfix1):
                prefix = prefix[: -len(postfix1)]
                postfix = f"_{postfix1}"
                break
        prefix = snake_from_camel(prefix).upper() + "_"
        if n == f"{prefix}MAX_ENUM{postfix}":
            return f"_MAX_ENUM"  # private enum value
        if prefix in self._PREFIX_TABLE:
            prefix = self._PREFIX_TABLE[prefix]
        if not n.startswith(prefix):
            assert False  # We might need to add a new vendor tag to vendor_tags.py
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

    def used_ctypes(self, api=Api.PYTHON) -> Set[str]:
        return {
            "c_int",
        }


class FlagsItem(CodeItem):
    def __init__(self, cursor: Cursor) -> None:
        super().__init__(cursor)
        assert cursor.kind == CursorKind.TYPEDEF_DECL
        self._capi_name = cursor.spelling
        self._py_name = py_type_name(self._capi_name)
        match = re.match(r"^Xr(\S+)Flags(\S*)$", self._capi_name)
        assert match
        self.core_name = match.group(1)
        self.vendor = match.group(2)
        self.value_prefix = snake_from_camel(self.core_name).upper() + "_"
        self.values = []

    def add_value(self, cursor: Cursor) -> None:
        assert cursor.kind == CursorKind.VAR_DECL
        item = VariableItem(cursor)
        assert item.name().startswith(self.value_prefix)
        item_name = item.name()[len(self.value_prefix):]
        if len(self.vendor) > 0:
            assert item_name.endswith("_" + self.vendor)
            item_name = item_name[:-len(self.vendor) - 1]
        self.values.append([item_name, item.value])

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
            raise NotImplementedError
        elif api == api.PYTHON:
            result = f"class {self.name(api)}(FlagBase):\n    NONE = 0x00000000"
            for name, value in self.values:
                result += f"\n    {name} = {value}"
            return result
        elif api == api.C:
            raise NotImplementedError

    def used_ctypes(self, api=Api.PYTHON) -> Set[str]:
        return set()


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

    def used_ctypes(self, api=Api.PYTHON) -> Set[str]:
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
            except Exception:
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

    @staticmethod
    def default_value() -> str:
        """Only applies if is_optional() is True"""
        return "None"

    def is_optional(self) -> bool:
        return self._optional

    def used_ctypes(self, api=Api.PYTHON) -> Set[str]:
        return self.type.used_ctypes(api)


class StructFieldItem(CodeItem):
    def __init__(self, cursor: Cursor) -> None:
        super().__init__(cursor)
        assert cursor.kind == CursorKind.FIELD_DECL
        self._capi_name = cursor.spelling
        self._py_name = snake_from_camel(self._capi_name)
        if False and self.cursor.type.kind == TypeKind.INT:
            possible_type = tuple(self.cursor.get_tokens())[0].spelling
            if possible_type in PlatformType.type_map:
                self._py_name = PlatformType.type_map[possible_type]
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

    def used_ctypes(self, api=Api.PYTHON) -> Set[str]:
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
            elif c.kind == CursorKind.STRUCT_DECL:
                pass  # Probably just a structure pointer, right?
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

    def _sequence_code(self) -> str:
        # Add special container methods for structures whose fields are all floats or ints
        result = ""
        if len(self.fields) < 2:
            return ""  # One field is not enough for a sequence
        field_ctype = None
        if self.fields[0].type.name(Api.CTYPES) == "c_float":
            field_ctype = "c_float"
            field_pytype = "float"
        elif self.fields[0].type.name(Api.CTYPES) == "c_int32":
            field_ctype = "c_int32"
            field_pytype = "int"
        for field in self.fields:
            if field.type.name(Api.CTYPES) != field_ctype:
                return ""  # All fields must be the same type
        # Finish constructor
        result += "        self._numpy = None\n"
        # Iterator
        result += f"\n    def __iter__(self) -> Generator[{field_pytype}, None, None]:\n"
        for f in self.fields:
            result += f"        yield self.{f.name()}\n"
        result += "\n"
        # Other container methods
        result += textwrap.indent(inspect.cleandoc(f"""
            def __getitem__(self, key):
                return tuple(self)[key]

            def __setitem__(self, key, value):
                self.as_numpy()[key] = value

            def __len__(self) -> int:
                return {len(self.fields)}

            def as_numpy(self):
                if not hasattr(self, "_numpy") or self._numpy is None:
                    # Just in time construction
                    buffer = ({field_ctype} * len(self)).from_address(addressof(self))
                    buffer._wrapper = self  # To link lifetime of buffer to self
                    self._numpy = numpy.ctypeslib.as_array(buffer)
                return self._numpy
        """), "    ")
        result += "\n"
        return result

    def code(self, api=Api.PYTHON) -> str:
        if api == Api.C:
            raise NotImplementedError
        result = f"class {self.name(api)}(Structure):"
        if len(self.fields) == 0:
            # Empty structure
            result += "\n    pass"
            return result
        structure_coder = StructureCoder(self)
        result += structure_coder.generate_constructor()
        result += self._sequence_code()
        result += "\n"
        # Hard code this for now, generalize later if needed
        if self.name() == "ExtensionProperties":
            # This structure is sort of equivalent to a string
            string_field = "extension_name"
            result += textwrap.indent(inspect.cleandoc(f"""
                def __bytes__(self):
                    return self.extension_name
            
                def __eq__(self, other):
                    try:
                        if other.type != self.type:
                            return False
                    except AttributeError:
                        pass  # That's OK, objects without those attributes can use string comparison
                    return str(other) == str(self)
            
                def __str__(self):
                    return self.{string_field}.decode()      
            """), "    ")
            result += "\n"
        else:
            result += structure_coder.generate_repr_str()
        result += structure_coder.generate_properties()
        # Recursive structures require two separate stanzas
        if self.is_recursive:
            # Structure containing self-reference must be declared in two stanzas
            result += "\n    pass"
            result += f"\n\n\n{self.name(api)}._fields_ = ["
        else:
            result += "\n    _fields_ = ["
        result += "".join([f.code(Api.CTYPES) for f in self.fields])
        result += "\n    ]"
        return result

    def used_ctypes(self, api=Api.PYTHON) -> Set[str]:
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
        self._ctypes_name = self._capi_name
        self._py_name = py_type_name(self._capi_name)
        self.type = parse_type(cursor.underlying_typedef_type)
        if self.type.clang_type.kind == TypeKind.ENUM:
            raise SkippableCodeItemException  # Keep enum typedefs out of typedefs.py
        if self._py_name == self.type.name(Api.CTYPES):
            raise SkippableCodeItemException  # Nonsense A = A typedef
        # Rename xr "Handle" types
        if cursor.underlying_typedef_type.kind == TypeKind.POINTER:
            pointee = cursor.underlying_typedef_type.get_pointee()
            if pointee.kind == TypeKind.ELABORATED:
                if pointee.spelling.endswith("_T"):
                    # This is a HANDLE type
                    self._py_name += "Handle"  # To distinguish Instance from InstanceHandle
                    self._ctypes_name = self._py_name
        if self.type.name() == "Flags64":
            self._py_name = self._ctypes_name = self._py_name + "CInt"
        if self._py_name == "Version":
            self._py_name = self._ctypes_name = "VersionNumber"

    def name(self, api=Api.PYTHON) -> str:
        if api == api.PYTHON:
            return self._py_name
        elif api == api.C:
            return self._capi_name
        elif api == api.CTYPES:
            return self._ctypes_name
        else:
            raise NotImplementedError

    def code(self, api=Api.PYTHON) -> str:
        if api == Api.C:
            raise NotImplementedError
        return f"{self.name(api)} = {self.type.name(Api.CTYPES)}"

    def used_ctypes(self, api=Api.PYTHON) -> Set[str]:
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

    def used_ctypes(self, api=Api.PYTHON) -> Set[str]:
        return set()


class NothingParameterCoder(object):
    """Parameter that generates no code. Used as a base for other parameter types."""
    def __init__(self, parameter: FunctionParameterItem):
        self.parameter = parameter

    @staticmethod
    def declaration_code(api=Api.PYTHON) -> Generator[str, None, None]:
        yield from []

    def main_call_code(self, api=Api.PYTHON) -> Generator[str, None, None]:
        yield from []

    def buffer_call_code(self, api=Api.PYTHON) -> Generator[str, None, None]:
        yield from self.main_call_code()

    @staticmethod
    def mid_body_code(api=Api.PYTHON) -> Generator[str, None, None]:
        yield from []

    @staticmethod
    def pre_body_code(api=Api.PYTHON) -> Generator[str, None, None]:
        yield from []

    @staticmethod
    def result_type_code(api=Api.PYTHON) -> Generator[str, None, None]:
        yield from []

    def result_value_code(self, api=Api.PYTHON) -> Generator[str, None, None]:
        yield from []


class ParameterCoderBase(NothingParameterCoder):
    def main_call_code(self, api=Api.PYTHON) -> Generator[str, None, None]:
        yield f"{self.parameter.name(api)}"


class InputParameterCoder(ParameterCoderBase):
    def declaration_code(self, api=Api.PYTHON) -> Generator[str, None, None]:
        p = self.parameter
        type_string = p.type.name(Api.PYTHON)
        # Pass structure types directly, even if C API says pointer
        if isinstance(p.type, PointerType):
            pt = p.type.pointee
            if pt.clang_type.kind == TypeKind.RECORD:  # struct
                type_string = pt.name(Api.PYTHON)
        yield f"{p.name(api)}: {type_string}"


class EnumParameterCoder(InputParameterCoder):
    def main_call_code(self, api=Api.PYTHON) -> Generator[str, None, None]:
        yield f"{self.parameter.name(api)}.value"


class StringInputParameterCoder(InputParameterCoder):
    def pre_body_code(self, api=Api.PYTHON) -> Generator[str, None, None]:
        yield f"if {self.parameter.name(api)} is not None:"
        yield f"    {self.parameter.name(api)} = {self.parameter.name(api)}.encode()"


class OutputParameterCoder(ParameterCoderBase):
    def result_type_code(self, api=Api.PYTHON) -> Generator[str, None, None]:
        rtype = self.parameter.type.pointee
        yield f"{rtype.name(api)}"

    def pre_body_code(self, api=Api.PYTHON) -> Generator[str, None, None]:
        rtype = self.parameter.type.pointee
        yield f"{self.parameter.name(api)} = {rtype.name(Api.CTYPES)}()"

    def main_call_code(self, api=Api.PYTHON) -> Generator[str, None, None]:
        yield f"byref({self.parameter.name(api)})"

    def result_value_code(self, api=Api.PYTHON) -> Generator[str, None, None]:
        rtype = self.parameter.type.pointee
        if rtype.name(Api.PYTHON) == "int":
            yield f"{self.parameter.name(api)}.value"
        else:
            yield f"{self.parameter.name(api)}"


class BufferCoder(ParameterCoderBase):
    """
    Output array parameter designed to use the two-call idiom in C.
    Be we want to use just one call in python.
    https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#buffer-size-parameters
    """
    def __init__(
            self,
            cap_in: FunctionParameterItem,
            count_out: FunctionParameterItem,
            array: FunctionParameterItem,
            use_element_type_arg: bool = False
    ):
        super().__init__(count_out)  # Not cap_in because it's optional
        self.cap_in = cap_in
        self.count_out = count_out
        self.array = array
        self.use_element_type_arg = use_element_type_arg
        if self.array.type.clang_type.spelling == "char *":  # string case
            assert not self.array.type.clang_type.get_pointee().is_const_qualified()
            self.array_type_name = "str"
        else:
            self.array_type = self.array.type.pointee
            self.array_type_name: str = self.array_type.name(Api.CTYPES)
        if self.use_element_type_arg:
            self.array_type_name_internal = "element_type"
        else:
            self.array_type_name_internal = self.array_type_name

    def declaration_code(self, api=Api.PYTHON) -> Generator[str, None, None]:
        if self.use_element_type_arg:
            yield f"element_type: type"

    def pre_body_code(self, api=Api.PYTHON) -> Generator[str, None, None]:
        yield f"{self.cap_in.name(api)} = {self.cap_in.type.name(Api.CTYPES)}(0)"

    def buffer_call_code(self, api=Api.PYTHON) -> Generator[str, None, None]:
        yield "0"
        yield f"byref({self.cap_in.name(api)})"
        yield "None"

    def mid_body_code(self, api=Api.PYTHON) -> Generator[str, None, None]:
        name = f"{self.array.name()}"
        n = f"{self.cap_in.name(api)}.value"
        etype = self.array_type_name_internal
        if self.array_type_name == "str":
            yield f"{name} = create_string_buffer({n})"
        else:
            # Use the default constructor to initialize each array member
            # initialized_array = (MyStructure * N)(*([MyStructure()] * N))
            yield f"{name} = ({etype} * {n})(*([{etype}()] * {n}))"

    def main_call_code(self, api=Api.PYTHON) -> Generator[str, None, None]:
        yield f"{self.cap_in.name(api)}"
        yield f"byref({self.cap_in.name(api)})"
        if self.use_element_type_arg:
            yield f"cast({self.array.name(api)}, POINTER({self.array_type_name}))"
        else:
            yield f"{self.array.name(api)}"

    def result_type_code(self, api=Api.PYTHON) -> Generator[str, None, None]:
        if self.array_type_name == "str":
            yield "str"
        else:  # array case
            yield f"Array[{self.array_type_name}]"

    def result_value_code(self, api=Api.PYTHON) -> Generator[str, None, None]:
        if self.array_type_name == "str":
            yield f"{self.array.name(api)}.value.decode()"
        else:  # array case
            yield f"{self.array.name(api)}"


class FunctionCoder(object):
    def __init__(self, function: FunctionItem):
        self.function = function
        self.param_coders = [[p, None] for p in self.function.parameters]
        # One pass to find buffer-size arguments
        # https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#buffer-size-parameters
        self._needs_two_calls = False
        for ix, pc in enumerate(self.param_coders):
            p, c = pc
            if p.name().endswith("_capacity_input"):
                # OpenXR buffer size parameters consist of three consecutive parameters
                assert "int" in p.type.name()
                p2 = self.param_coders[ix + 1][0]
                assert p2.name().endswith("_count_output")
                assert p2.type.clang_type.kind == TypeKind.POINTER
                assert "int" in p2.type.pointee.name()
                p3 = self.param_coders[ix + 2][0]
                assert p2.type.clang_type.kind == TypeKind.POINTER
                add_element_type_arg = self.function.name() in ["enumerate_swapchain_images", ]
                self.param_coders[ix][1] = NothingParameterCoder(p)
                self.param_coders[ix + 1][1] = BufferCoder(p, p2, p3, add_element_type_arg)
                self.param_coders[ix + 2][1] = NothingParameterCoder(p3)
                self._needs_two_calls = True
        # Assume remainder are simple inputs
        for ix, pc in enumerate(self.param_coders):
            p, c = pc
            if c is not None:
                continue
            if isinstance(p.type, StringType):
                pc[1] = StringInputParameterCoder(p)
                continue
            ct = p.type.clang_type
            if ct.kind == TypeKind.POINTER and not ct.get_pointee().is_const_qualified():
                pc[1] = OutputParameterCoder(p)
                continue
            if ct.kind == TypeKind.TYPEDEF:
                ut = ct.get_declaration().underlying_typedef_type
                if ut.kind == TypeKind.ELABORATED:
                    pc[1] = EnumParameterCoder(p)
                    continue
            pc[1] = InputParameterCoder(p)

    def declaration_code(self, api=Api.PYTHON) -> str:
        result_types = []
        for p, c in self.param_coders:
            for r in c.result_type_code(Api.PYTHON):
                result_types.append(r)
        # Don't show default value for any parameter that appears before required parameters
        can_haz_default = True
        param_strings = []
        for p, c in reversed(self.param_coders):
            for s in c.declaration_code(api):
                default = ","
                if p.is_optional() and can_haz_default:
                    default = f" = {p.default_value()},"
                if not p.is_optional():
                    can_haz_default = False
                param_strings.append(f"\n{' ' * 16}{s}{default}")
        params = "".join(reversed(param_strings))
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
        if self._needs_two_calls:
            result += f"\n    # First call of two, to retrieve buffer sizes"
            result += f"\n    result = check_result(fxn("
            for p, c in self.param_coders:
                for param_name in c.buffer_call_code():
                    result += f"\n        {param_name},"
            result += f"\n    ))"
            result += f"\n    if result.is_exception():"
            result += f"\n        raise result"
        for p, c in self.param_coders:
            for line in c.mid_body_code():
                result += f"\n    {line}"
        result += f"\n    result = check_result(fxn("
        for p, c in self.param_coders:
            for param_name in c.main_call_code():
                result += f"\n        {param_name},"
        result += f"\n    ))"
        result += f"\n    if result.is_exception():"
        result += f"\n        raise result"
        result_values = []
        for p, c in self.param_coders:
            for r in c.result_value_code(Api.PYTHON):
                result_values.append(r)
        if len(result_values) > 0:
            result += f"\n    return {', '.join(result_values)}"
        return result


class FieldCoder(object):
    """Code generator helper for a single field in a ctypes.Structure constructor"""
    def __init__(self, field: StructFieldItem, default=0, rename=None):
        self.field = field
        self.name = self.field.name(Api.PYTHON)
        self.inner_name = self.name
        if rename is not None:
            self.name = rename
        self.default = default

    def param_code(self) -> Generator[str, None, None]:
        yield f"{self.name}: {self.field.type.name(Api.PYTHON)} = {self.default}"

    @staticmethod
    def pre_call_code() -> Generator[str, None, None]:
        yield from []

    def call_code(self) -> Generator[str, None, None]:
        yield f"{self.field.name()}={self.name}"

    def property_code(self) -> Generator[str, None, None]:
        if self.inner_name != self.name:
            # getter
            yield "@property"
            yield f"def {self.name}(self):"
            yield f"    return self.{self.inner_name}"
            # setter
            yield ""
            yield f"@{self.name}.setter"
            yield f"def {self.name}(self, value):"
            yield f"    self.{self.inner_name} = value"

    def str_code(self) -> Generator[str, None, None]:
        if self.field.type.name(Api.CTYPES) == "c_float":
            value = f"{{self.{self.inner_name}:.3f}}"
        else:
            value = f"{{self.{self.inner_name}}}"
        yield f"{self.name}={value}"

    def repr_code(self) -> Generator[str, None, None]:
        yield f"{self.name}={{repr(self.{self.inner_name})}}"


class ArrayCountFieldCoder(FieldCoder):
    """
    Collapse count/pointer field pairs into a single sequence constructor parameter.
    """
    def __init__(self, count_field: StructFieldItem, array_field: StructFieldItem):
        super().__init__(count_field)
        self.array_field = array_field

    def param_code(self) -> Generator[str, None, None]:
        yield from []  # Exclude count field from constructor

    def call_code(self) -> Generator[str, None, None]:
        yield f"{self.field.name()}=len({self.array_field.name()})"


class ArrayPointerFieldCoder(FieldCoder):
    """
    Collapse count/pointer field pairs into a single sequence constructor parameter.
    """
    def __init__(self, count_field: StructFieldItem, array_field: StructFieldItem):
        super().__init__(array_field)
        self.element_type_name = self.field.type.pointee.name(Api.PYTHON)

    def param_code(self) -> Generator[str, None, None]:
        yield f"{self.name}: Sequence[{self.field.type.pointee.name(Api.PYTHON)}] = []"

    def call_code(self) -> Generator[str, None, None]:
        if self.field.type.pointee.name(Api.PYTHON) == "str":
            yield f"{self.field.name()}=(c_char_p * len({self.name}))(*[s.encode() for s in {self.name}])"
        else:
            yield f"{self.field.name()}=({self.field.type.pointee.name(Api.CTYPES)} * len({self.name}))(*{self.name})"


class EnumFieldCoder(FieldCoder):
    def param_code(self) -> Generator[str, None, None]:
        enum_name = self.field.type.name(Api.PYTHON)
        yield f"{self.name}: {enum_name} = {enum_name}()"

    def call_code(self) -> Generator[str, None, None]:
        enum_name = self.field.type.name(Api.PYTHON)
        yield f"{self.field.name()}={enum_name}({self.name}).value"


class FunctionPointerFieldCoder(FieldCoder):
    def param_code(self) -> Generator[str, None, None]:
        fn_type = self.field.type.name(Api.PYTHON)
        yield f"{self.name}: {fn_type} = cast(None, {fn_type})"


class NoDefaultFieldCoder(FieldCoder):
    """There is no reasonable default"""
    def param_code(self) -> Generator[str, None, None]:
        yield f"{self.name}: {self.field.type.name(Api.PYTHON)}"


class ArrayFieldCoder(FieldCoder):
    """We should not pass EventDataBuffer.varying in the constructor"""
    def param_code(self) -> Generator[str, None, None]:
        yield from []

    @staticmethod
    def pre_call_code() -> Generator[str, None, None]:
        yield from []

    def call_code(self) -> Generator[str, None, None]:
        yield from []

    def str_code(self) -> Generator[str, None, None]:
        yield from []

    def repr_code(self) -> Generator[str, None, None]:
        yield f"{self.field.name()}={{repr(self.{self.name})}}"


class NextFieldCoder(FieldCoder):
    def __init__(self, *args, **kwargs):
        super().__init__(rename="next_structure", *args, **kwargs)

    def param_code(self) -> Generator[str, None, None]:
        # Avoid self reference in BaseInStructure
        yield f"next_structure: c_void_p = None"


class VoidPointerFieldCoder(FieldCoder):
    def param_code(self) -> Generator[str, None, None]:
        yield f"{self.name}: {self.field.type.name(Api.CTYPES)} = None"


class StringFieldCoder(FieldCoder):
    def param_code(self) -> Generator[str, None, None]:
        yield f'{self.name}: str = ""'

    def call_code(self) -> Generator[str, None, None]:
        yield f"{self.field.name()}={self.name}.encode()"


class VersionFieldCoder(FieldCoder):
    def param_code(self) -> Generator[str, None, None]:
        yield f'{self.name}: Version = Version()'

    def call_code(self) -> Generator[str, None, None]:
        yield f"{self.field.name()}={self.name}.number()"


class StructureFieldCoder(FieldCoder):
    def pre_call_code(self) -> Generator[str, None, None]:
        yield f"if {self.name} is None:"
        yield f"    {self.name} = {self.field.type.name(Api.PYTHON)}()"


class StructureTypeFieldCoder(FieldCoder):
    def __init__(self, field, struct):
        super().__init__(field)
        self.struct = struct
        self.name = "structure_type"

    def param_code(self) -> Generator[str, None, None]:
        type_enum_name = structure_type_enum_name(self.struct)
        yield f"structure_type: {self.field.type.name(Api.PYTHON)} = StructureType.{type_enum_name}"

    def call_code(self) -> Generator[str, None, None]:
        yield f"{self.field.name()}=structure_type.value"


class BaseStructureTypeFieldCoder(FieldCoder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "structure_type"

    def param_code(self) -> Generator[str, None, None]:
        yield f"structure_type: {self.field.type.name(Api.PYTHON)} = StructureType.UNKNOWN"

    def call_code(self) -> Generator[str, None, None]:
        yield f"{self.field.name()}=structure_type.value"


class StructureCoder(object):
    def __init__(self, struct: StructItem):
        self.struct = struct
        self.field_coders = []
        skip_next_field = False
        for ix, field in enumerate(self.struct.fields):
            if skip_next_field:
                skip_next_field = False
                continue
            if field.name() == "next":
                self.field_coders.append(NextFieldCoder(field))
            elif field.type.name(Api.CTYPES) == "c_void_p":
                self.field_coders.append(VoidPointerFieldCoder(field))
            elif field.type.name(Api.PYTHON) == "StructureType":
                if "Base" in struct.name():
                    self.field_coders.append(BaseStructureTypeFieldCoder(field))
                else:
                    self.field_coders.append(StructureTypeFieldCoder(field, struct))
            elif field.type.name(Api.PYTHON) == "str":
                self.field_coders.append(StringFieldCoder(field))
            elif field.type.name(Api.PYTHON).startswith("(c_char * "):
                self.field_coders.append(StringFieldCoder(field))
            elif field.type.name(Api.CTYPES) == "VersionNumber":
                self.field_coders.append(VersionFieldCoder(field))
            elif struct.name() == "Quaternionf" and field.name() == "w":
                self.field_coders.append(FieldCoder(field, default=1))
            elif isinstance(field.type, TypedefType) and isinstance(field.type.underlying_type, RecordType):
                self.field_coders.append(StructureFieldCoder(field, None))
            elif re.match(r"^\(\S+ \* \d+\)$", field.type.name()):
                self.field_coders.append(ArrayFieldCoder(field))
            elif field.type.name().endswith("Handle"):
                self.field_coders.append(FieldCoder(field, default=None))
            elif field.type.name().startswith("PFN_xr"):
                self.field_coders.append(FunctionPointerFieldCoder(field))
            elif field.type.name().startswith("POINTER("):
                self.field_coders.append(FieldCoder(field, default=None))
            elif field.type.name().endswith("GLXFBConfig"):
                self.field_coders.append(FieldCoder(field, default=None))
            elif field.type.name().endswith("GLXContext"):
                self.field_coders.append(FieldCoder(field, default=None))
            elif (field.name().endswith("_count")  # e.g. "enabled_api_layer_count"
                and field.type.name(Api.PYTHON) == "int"
                and ix + 1 < len(struct.fields)  # not the final field
            ):
                # this field might be an input array pointer size
                stem = field.name()[:6]  # e.g. "enabled_api_layer"
                f2 = struct.fields[ix + 1]
                f2n = f2.name()  # e.g. "enabled_api_layers"
                if stem in f2n and f2n.endswith("s") and f2.type.name().startswith("POINTER("):
                    skip_next_field = True
                    self.field_coders.append(ArrayCountFieldCoder(count_field=field, array_field=f2))
                    self.field_coders.append(ArrayPointerFieldCoder(count_field=field, array_field=f2))
                else:
                    self.field_coders.append(FieldCoder(field))
            elif isinstance(field.type, TypedefType) and isinstance(field.type.underlying_type, EnumType):
                self.field_coders.append(EnumFieldCoder(field))
            elif isinstance(field.type, TypedefType) and field.type.underlying_type.name() == "Flags64":
                self.field_coders.append(EnumFieldCoder(field))
            else:
                self.field_coders.append(FieldCoder(field))
        # Rearrange arguments of Typed Structures
        fields = self.struct.fields
        if len(fields) > 1 and fields[0].name() == "type" and fields[1].name() == "next":
            assert fields[0].type.name() == "StructureType"
            n1 = fields[1].type.name(Api.CTYPES)
            assert n1 == "c_void_p" or n1.startswith("POINTER(Base")
            self.field_coders = self.field_coders[2:] + [self.field_coders[1]] + [self.field_coders[0]]
            x = 3

    """Creates __init__(...) method for Structure types"""
    def generate_constructor(self) -> str:
        # Special cases for default values
        # TODO: box/unbox enums
        # TODO: use None as default for pointer fields
        # TODO: create another method for str and repr
        i4 = "    "
        i8 = "        "
        i12 = "            "
        result = ""
        result += f"\n{i4}def __init__(\n{i8}self,\n"
        for fc in self.field_coders:
            for s in fc.param_code():
                result += f"{i8}{s},\n"
        result += f"{i4}) -> None:\n"
        for fc in self.field_coders:
            for s in fc.pre_call_code():
                result += f"{i8}{s}\n"
        result += f"{i8}super().__init__(\n"
        for fc in self.field_coders:
            for s in fc.call_code():
                result += f"{i12}{s},\n"
        result += f"{i8})\n"
        return result

    def generate_properties(self) -> str:
        result = ""
        for fc in self.field_coders:
            prop_strings = []
            for s in fc.property_code():
                prop_strings.append(s)
            if len(prop_strings) > 0:
                result += "\n"
                for s in prop_strings:
                    result += f"    {s}\n"
        return result

    def generate_repr_str(self) -> str:
        class_name = self.struct.name()
        repr_strings = []
        str_strings = []
        for fc in self.field_coders:
            for s in fc.repr_code():
                repr_strings.append(s)
            for s in fc.str_code():
                str_strings.append(s)
        field_reprs = ", ".join(repr_strings)
        field_strs = ", ".join(str_strings)
        first = f"xr.{class_name}"
        # Short string version of classes that look more like tuples
        if class_name in ["Quaternionf", "Vector3f", "Posef", ]:
            first = ""
        result = ""
        result += textwrap.indent(inspect.cleandoc(f"""
            def __repr__(self) -> str:
                return f"xr.{class_name}({field_reprs})"

            def __str__(self) -> str:
                return f"{first}({field_strs})"
        """), "    ")
        result += "\n"
        return result


def snake_from_camel(camel: str) -> str:
    snake = f"{camel}"
    snake = re.sub(r"([^A-Z])([A-Z])", r"\1_\2", snake)
    snake = snake.lower()
    snake = re.sub(r"open_gl", "opengl_", snake)
    return snake


def structure_type_enum_name(struct: StructItem):
    type_enum_name = snake_from_camel(struct.name()).upper()
    type_enum_name = type_enum_name.replace("D3_D", "D3D")
    return type_enum_name


__all__ = [
    "CodeItem",
    "DefinitionItem",
    "EnumItem",
    "FlagsItem",
    "FunctionItem",
    "SkippableCodeItemException",
    "snake_from_camel",
    "StructItem",
    "TypeDefItem",
    "VariableItem",
]
