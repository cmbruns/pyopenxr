import inspect
import os
import textwrap
from typing import Optional
from xml.etree.ElementTree import Element

from xrg.declarations import camel_from_snake, snake_from_camel
from xrg.function_docstring_data import function_docstrings
from xrg.registry import xr_registry


class ParameterType:
    def __init__(
            self,
            c_name: str,
            name: str,
            is_pointer: bool = False,
            is_const: bool = False,
            default: Optional[str] = None,
    ) -> None:
        self.c_name = c_name
        self.name = name
        self.is_pointer = is_pointer
        self.is_const = is_const
        self.default = default

    @classmethod
    def from_xml(
            cls,
            parameter_element,
            extension: Optional["ExtensionModuleItem"],
    ) -> "ParameterType":
        assert parameter_element.tag == "param"
        c_name = parameter_element.find("type").text
        if c_name in extension.aliases:
            name = f"{extension.aliases[c_name].alias}"  # TODO: prepend extension module name?
        else:
            assert c_name.startswith("Xr")
            name = f'xr.{c_name[len("Xr"):]}'
        full_text = "".join(parameter_element.itertext())
        is_pointer = "*" in full_text
        is_const = "const" in full_text.split(c_name)[0]
        default_value = None
        if c_name in type_index:
            xr_type = type_index[c_name]
            if xr_type.attrib["category"] == "struct":
                default_value = f"{name}()"
        return cls(c_name, name, is_pointer, is_const, default=default_value)

    def __str__(self):
        return self.name


class CommandParameterItem:
    def __init__(self, c_name, parameter_type: ParameterType):
        self.c_name = c_name
        self.type = parameter_type
        self.py_name = snake_from_camel(self.c_name)
        self.default = parameter_type.default

    @classmethod
    def from_xml(
            cls,
            parameter_element,
            extension: Optional["ExtensionModuleItem"],
    ) -> "CommandParameterItem":
        assert parameter_element.tag == "param"
        c_name = parameter_element.find("name").text
        parameter_type = ParameterType.from_xml(parameter_element, extension)
        return cls(c_name, parameter_type)


class ExtensionCommandItem:
    def __init__(self, c_name: str, py_name: str, parameters, module_name: str = "xr") -> None:
        self.c_name = c_name  # e.g. 'xrSetDebugUtilsObjectNameEXT'
        self.py_name = py_name
        self.parameters = parameters
        self.module_name = module_name
        self.parameter_index = {parameter.py_name: parameter for parameter in self.parameters}
        # Look for output parameter
        self.return_type = "None"
        if len(self.parameters) > 0:
            final = self.parameters[-1]
            if final.type.is_pointer and not final.type.is_const:
                self.return_type = final.type

    @classmethod
    def from_xml(cls, command_entity, extension: Optional["ExtensionModuleItem"]) -> "ExtensionCommandItem":
        c_name = command_entity.attrib["name"]
        py_name = c_name
        prefix = f"xr"
        assert py_name.startswith(prefix)
        py_name = py_name[len(prefix):]
        suffix = extension.vendor_tag
        assert py_name.endswith(suffix)
        py_name = py_name[:-len(suffix)]
        assert extension.camel_short_name in py_name
        py_name = py_name.replace(extension.camel_short_name, "")
        py_name = snake_from_camel(py_name)
        py_name = py_name
        command = None
        for commands in xr_registry.findall("commands"):
            assert commands
            command = None
            for cmd in commands.findall("command"):
                pn = cmd.find("proto/name")
                if pn is None:
                    continue
                if pn.text == c_name:
                    command = cmd
                    break
            if command is not None:
                break
        assert command is not None
        proto = command.find("proto")
        assert proto.find("type").text == "XrResult"
        parameters = []  # list because order matters
        for param in command.findall("param"):
            parameters.append(CommandParameterItem.from_xml(param, extension))
        return cls(c_name, py_name, parameters, extension.module_name)

    def __lt__(self, other):
        return self.py_name < other.py_name

    def code(self) -> str:
        result = ""
        result += f"def {self.py_name}("
        decl_param_count = 0
        output_parameters = []
        for param_ix, param in enumerate(self.parameters):
            is_output = (
                param.type.is_pointer
                and not param.type.is_const
                and param_ix == len(self.parameters) - 1
            )
            if is_output:
                output_parameters.append(param)
                continue
            # TODO: default value
            default = ""
            if param.default is not None:
                default = f" = {param.default}"
            result += f"\n    {param.py_name}: {param.type}{default},"
            decl_param_count += 1
        if decl_param_count > 0:
            result += "\n"
        result += f") -> {self.return_type}:\n"
        if f"{self.module_name}.{self.py_name}" in function_docstrings:
            fd = function_docstrings[f"{self.module_name}.{self.py_name}"]
            docstring = fd["docstring"]
            assert len(docstring) > 0
            docstring = f'"""\n{docstring}\n"""\n'
            docstring = textwrap.indent(docstring, " " * 4)
            result += docstring
        # Where to get instance for get_instance_proc_addr?
        instance_name = "instance"
        if "instance" not in self.parameter_index:
            # Presume the first argument is a handle with an instance attribute
            instance_name = f"{self.parameters[0].py_name}.instance"
        result += textwrap.indent(inspect.cleandoc(f"""
            pfn = cast(
                xr.get_instance_proc_addr({instance_name}, "{self.c_name}"),
                xr.PFN_{self.c_name},
            )        
        """), "    ") + "\n"
        for param in output_parameters:
            result += f"    {param.py_name} = {param.type}()\n"
        # Is this a xrCreate<Handle> method? If so, cache the instance.
        if (
                self.py_name.startswith("create_")
                and len(output_parameters) == 1
        ):
            result += f"    {param.py_name}.instance = {instance_name}\n"
            # Does the create_info argument have a callback parameter?
            # If so, cache the callback, to avoid early gc
            # (This is very specific to debug_utils.MessengerCreateInfo)
            if len(self.parameters) > 1 and self.parameters[1].py_name == "create_info":
                p = self.parameters[1]
                x = 3
                tcn = p.type.c_name
                for types in xr_registry.findall("types"):
                    for type in types.findall("type"):
                        if type.attrib.get("name", None) == tcn:
                            for field in type.findall("member"):
                                field_type_name = field.find("type").text
                                if field_type_name.startswith("PFN_"):
                                    field_name = snake_from_camel(field.find("name").text)
                                    result += f"    # tie callback lifetime to that of the new handle\n"
                                    result += f"    {param.py_name}._callback = create_info.{field_name}\n"
        result += "    result_code = pfn(\n"
        for param in self.parameters:
            if param.type.is_pointer:
                result += f"        byref({param.py_name}),\n"
            else:
                result += f"        {param.py_name},\n"
        result += textwrap.indent(inspect.cleandoc(f"""
            )
            checked = xr.check_result(xr.Result(result_code))
            if checked.is_exception():
                raise checked
        """), "    ")
        if len(output_parameters) > 0:
            result += f"\n    return {','.join([p.py_name for p in output_parameters])}"
        return result


class ExtensionModuleItem:
    def __init__(self, element: Element) -> None:
        assert element.tag == "extension"
        self.name = element.attrib["name"]
        assert self.name.startswith("XR_")  # e.g. "XR_EXT_debug_utils"
        short_name = element.attrib["name"][len("XR_"):]
        self.vendor_tag = short_name.split("_")[0]  # e.g. "EXT"
        self.short_name = short_name[len(self.vendor_tag) + 1:]  # e.g "debug_utils"
        self.module_name = f"xr.ext.{self.vendor_tag}.{self.short_name}"
        self.camel_short_name = camel_from_snake(self.short_name)  # e.g. "DebugUtils"
        if self.camel_short_name.endswith("Enable"):  # e.g. opengl_enable
            self.camel_short_name = self.camel_short_name[:-len("Enable")]
        require = element.find("require")
        version = require.find(f"enum[@name='{self.name}_SPEC_VERSION']")
        self.version = version.attrib["value"]
        self.all = {"EXTENSION_NAME", "SPEC_VERSION", "VENDOR_TAG"}
        self.aliases = {}
        # 1) Find extension object types in the main non-extension types area
        xr_types = xr_registry.find("types")
        assert xr_types
        for xr_type in xr_types.findall("type"):
            if xr_type.tag != "type":
                continue
            try:
                type_name = xr_type.attrib["name"]
            except KeyError:
                type_name = xr_type.find("name").text
            if self.camel_short_name not in type_name:
                continue
            if type_name.startswith(f"PFN_xr{self.camel_short_name}"):
                continue  # TODO: function pointers
            # assert type_name.startswith(f"Xr{self.camel_short_name}")  # not XrGraphicsBindingOpenGLWin32KHR
            # assert type_name.endswith(self.vendor_tag)  # not XrSwapchainStateSamplerOpenGLESFB
            if type_name.endswith(f"FlagBits{self.vendor_tag}"):
                continue
            alias = ExtensionTypeAliasItem(type_name, self)
            self.aliases[alias.c_name] = alias
        # 2) Find more extension object types in the enum area
        for ext_type in require.findall("enum[@extends='XrObjectType']"):
            alias = ExtensionTypeAliasItem(ext_type.attrib["comment"], self)
            self.aliases[alias.c_name] = alias
        for alias in self.aliases.values():
            self.all.add(alias.alias)
        # TODO: extension function pointers
        self.ctypes_types = set()
        self.commands = set()
        for command in require.findall("command"):
            self.ctypes_types.add("cast")
            cmd = ExtensionCommandItem.from_xml(command, self)
            self.commands.add(cmd)
            self.all.add(cmd.py_name)
            for param in cmd.parameters:
                if param.type.is_pointer:
                    self.ctypes_types.add("byref")

    def code(self) -> str:
        result = ""
        indent1 = " " * 12
        indent2 = " " * 16
        sorted_all = "".join([f'\n{indent2}"{a}",' for a in sorted(self.all)])
        result += inspect.cleandoc(f'''
            """
            Python bindings for the `{self.name}` instance extension.

            This module provides Python wrappers for OpenXR functions defined in the
            `{self.name}` specification. These wrappers expose runtime diagnostics,
            object naming, and other extension-specific features.

            To enable this extension, include `"{self.name}"` in your
            `enabled_extension_names` when calling :func:`xr.create_instance`.

            See the Khronos registry for full specification:
            https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#{self.name}
            """

            __all__ = [
        ''')
        if len(self.all) > 0:
            for all_item in sorted(self.all):
                result += f'\n    "{all_item}",'
            result += "\n"
        result += inspect.cleandoc(f'''
            ]
        ''') + "\n\n"
        if len(self.ctypes_types) > 0:
            result += f"from ctypes import {', '.join([c for c in sorted(self.ctypes_types)])}\n\n"
        result += inspect.cleandoc(f'''
            import xr

            EXTENSION_NAME = "{self.name}"
            SPEC_VERSION = {self.version}
            VENDOR_TAG = "{self.vendor_tag}"
        ''') + "\n"
        if len(self.aliases) > 0:
            result += "\n# Aliases for xr core types\n"
            for alias in sorted(self.aliases.values()):
                result += f"{alias.code()}\n"
        if len(self.commands) > 0:
            for command in sorted(self.commands):
                result += f"\n\n{command.code()}\n"
        return result


class ExtensionTypeAliasItem:
    def __init__(self, type_name: str, extension: ExtensionModuleItem):
        self.c_name = type_name
        # core_name is the type name in the top level xr namespace
        core_name = self.c_name
        assert core_name.startswith("Xr") or core_name.startswith("PFN_xr")
        if core_name.startswith("Xr"):
            core_name = core_name[len("Xr"):]  # e.g. "DebugUtilsObjectNameInfoEXT"
        self.core_name = core_name
        # alias is the local in-extension type name alias
        alias = core_name  # e.g. "DebugUtilsObjectNameInfoEXT"
        # assert alias.endswith(extension.vendor_tag)  # not SwapchainStateSamplerOpenGLESFB
        if alias.endswith(extension.vendor_tag):
            alias = alias[:-len(extension.vendor_tag)]  # e.g. "DebugUtilsObjectNameInfo"
        assert extension.camel_short_name in alias
        alias = alias.replace(extension.camel_short_name, "")  # e.g. "ObjectNameInfo"
        if alias.startswith("PFN_xr"):
            alias = f"PFN_{alias[len('PFN_xr'):]}"
        self.alias = alias

    def __eq__(self, other):
        return self.c_name == other.c_name

    def __hash__(self):
        return hash(self.c_name)

    def __lt__(self, other):
        return self.alias < other.alias

    def code(self) -> str:
        return f"{self.alias} = xr.{self.core_name}"


def index_types():
    # Enumerate all types to help with parameter default values
    index = {}
    xr_types = xr_registry.find("types")
    assert xr_types
    for xr_type in xr_types.findall("type"):
        if xr_type.tag != "type":
            continue
        try:
            type_name = xr_type.attrib["name"]
        except KeyError:
            type_name = xr_type.find("name").text
        index[type_name] = xr_type
    return index


type_index = {}


def generate_extensions():
    global type_index
    type_index = index_types()
    # Enumerate wrappable OpenXR extensions
    extension_entities = xr_registry.find("extensions")
    assert extension_entities
    for ext in extension_entities.findall("extension"):
        if ext.attrib["supported"] != "openxr":
            continue
        assert ext.attrib["type"] == "instance"
        # Over-filter for initial development TODO: remove this for production
        if ext.attrib["name"] not in ["XR_KHR_opengl_enable"]:  # for starters
            continue
        extension = ExtensionModuleItem(ext)
        do_write = True
        if do_write:
            f_name = f"../xr/ext/{extension.vendor_tag}/{extension.short_name}.py"
            assert os.path.exists(f_name)
            with open(f_name, "w", encoding="utf-8") as f:
                f.write(extension.code())
        else:
            print(extension.code())


if __name__ == "__main__":
    generate_extensions()
