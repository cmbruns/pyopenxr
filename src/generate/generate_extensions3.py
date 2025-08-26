import inspect
from xml.etree.ElementTree import Element

from generate.xrg.declarations import camel_from_snake, snake_from_camel
from xrg.registry import xr_registry


class CommandParameterItem:
    def __init__(self, element, extension):
        assert element.tag == "param"
        self.c_name = element.find("name").text
        self.py_name = snake_from_camel(self.c_name)
        self.type_c_name = element.find("type").text
        # TODO: look up extension aliases
        if self.type_c_name in extension.aliases:
            alias = extension.aliases[self.type_c_name]
            self.type_py_name = alias.alias
        else:
            assert self.type_c_name.startswith("Xr")
            self.type_py_name = "xr." + self.type_c_name[len("Xr"):]
        full_text = "".join(element.itertext())
        self.is_pointer = "*" in full_text
        self.is_const = "const" in full_text.split(self.type_c_name)[0]
        self.is_output = False  # might be overwritten in a moment...


class ExtensionCommandItem:
    def __init__(self, name, extension):
        self.c_name = name  # e.g. 'xrSetDebugUtilsObjectNameEXT'
        py_name = self.c_name
        prefix = f"xr"
        assert py_name.startswith(prefix)
        py_name = py_name[len(prefix):]
        suffix = extension.vendor_tag
        assert py_name.endswith(suffix)
        py_name = py_name[:-len(suffix)]
        assert extension.camel_short_name in py_name
        py_name = py_name.replace(extension.camel_short_name, "")
        py_name = snake_from_camel(py_name)
        self.py_name = py_name
        command = None
        for commands in xr_registry.findall("commands"):
            assert commands
            command = None
            for cmd in commands.findall("command"):
                pn = cmd.find("proto/name")
                if pn is None:
                    continue
                if pn.text == self.c_name:
                    command = cmd
                    break
            if command is not None:
                break
        assert command is not None
        proto = command.find("proto")
        assert proto.find("type").text == "XrResult"
        self.parameters = []  # list because order matters
        for param in command.findall("param"):
            self.parameters.append(CommandParameterItem(param, extension))
        # Look for output parameter
        self.return_type = "None"
        if len(self.parameters) > 0:
            final = self.parameters[-1]
            if final.is_pointer and not final.is_const:
                final.is_output = True
                self.return_type = final.type_py_name

    def __lt__(self, other):
        return self.py_name < other.py_name

    def code(self) -> str:
        result = ""
        result += inspect.cleandoc(f"""
        def {self.py_name}(
        ) -> {self.return_type}:
            pass
        """)
        return result


class ExtensionModuleItem:
    def __init__(self, element: Element) -> None:
        assert element.tag == "extension"
        self.name = element.attrib["name"]
        assert self.name.startswith("XR_")  # e.g. "XR_EXT_debug_utils"
        short_name = element.attrib["name"][len("XR_"):]
        self.vendor_tag = short_name.split("_")[0]  # e.g. "EXT"
        self.short_name = short_name[len(self.vendor_tag) + 1:]  # e.g "debug_utils"
        self.camel_short_name = camel_from_snake(self.short_name)  # e.g. "DebugUtils"
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
            assert type_name.startswith(f"Xr{self.camel_short_name}")
            assert type_name.endswith(self.vendor_tag)
            alias = ExtensionTypeAliasItem(type_name, self)
            self.aliases[alias.c_name] = alias
        # 2) Find more extension object types in the enum area
        for ext_type in require.findall("enum[@extends='XrObjectType']"):
            alias = ExtensionTypeAliasItem(ext_type.attrib["comment"], self)
            self.aliases[alias.c_name] = alias
        for alias in self.aliases.values():
            self.all.add(alias.alias)
        # TODO: extension function pointers
        self.commands = set()
        for command in require.findall("command"):
            cmd = ExtensionCommandItem(command.attrib["name"], self)
            self.commands.add(cmd)
            self.all.add(cmd.py_name)
        self.ctypes_types = set()

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

            import xr

            EXTENSION_NAME = "{self.name}"
            SPEC_VERSION = {self.version}
            VENDOR_TAG = "{self.vendor_tag}"
        ''')
        if len(self.aliases) > 0:
            result += "\n\n# Aliases for xr core types\n"
            for alias in sorted(self.aliases.values()):
                result += f"{alias.code()}\n"
        if len(self.commands) > 0:
            for command in sorted(self.commands):
                result += f"\n\n{command.code()}"
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
        assert alias.endswith(extension.vendor_tag)
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


def generate_extensions():
    # Enumerate wrappable OpenXR extensions
    extension_entities = xr_registry.find("extensions")
    assert extension_entities
    for ext in extension_entities.findall("extension"):
        if ext.attrib["supported"] != "openxr":
            continue
        assert ext.attrib["type"] == "instance"
        # Over-filter for initial development TODO: remove this for production
        if ext.attrib["name"] not in ["XR_EXT_debug_utils"]:  # for starters
            continue
        extension = ExtensionModuleItem(ext)
        print(extension.code())


if __name__ == "__main__":
    generate_extensions()
