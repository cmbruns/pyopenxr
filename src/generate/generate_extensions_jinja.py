from jinja2 import Environment, FileSystemLoader

from xrg.declarations import camel_from_snake, snake_from_camel
from xrg.registry import xr_registry


class Extension:
    pass


class Command:
    pass


# Enumerate OpenXR extensions
extension_entities = xr_registry.find("extensions")
assert extension_entities
extensions = []
for ext in extension_entities.findall("extension"):
    # Filter for extensions worth wrapping
    assert ext.attrib["name"].startswith("XR_")  # e.g. XR_EXT_debug_utils
    short_name = ext.attrib["name"][len("XR_"):]
    vendor_tag = short_name.split("_")[0]  # e.g. EXT
    short_name = short_name[len(vendor_tag) + 1:]  # e.g debug_utils
    if ext.attrib["supported"] != "openxr":
        continue
    assert ext.attrib["type"] == "instance"
    if ext.attrib["name"] not in ["XR_EXT_debug_utils"]:  # for starters
        continue
    extension = Extension()
    extension.name = ext.attrib["name"]
    extension.short_name = short_name
    extension.vendor_tag = vendor_tag
    extension.short_camel_name = camel_from_snake(extension.short_name)
    extensions.append(extension)
    print(ext.attrib["name"], vendor_tag, short_name)
    require = ext.find("require")
    for enum in require.findall("enum"):
        n = enum.attrib["name"]
        if n.startswith(extension.name) and n.endswith("_SPEC_VERSION"):
            extension.version = enum.attrib["value"]
    # Commands
    extension.commands = []
    for command_entity in require.findall("command"):
        command = Command()
        # Transform C function name to python function name
        command.c_name = command_entity.attrib["name"]
        py_name = command.c_name
        # Strip off initial "xr"
        assert py_name.startswith("xr")
        py_name = py_name[len("xr"):]
        # Strip off final "EXT"
        assert py_name.endswith(vendor_tag)
        py_name = py_name[:-len(vendor_tag)]
        # Elide internal extension name substring
        assert extension.short_camel_name in py_name
        py_name = py_name.replace(extension.short_camel_name, "")
        py_name = snake_from_camel(py_name)
        command.py_name = py_name
        extension.commands.append(command)
        print(command.c_name, command.py_name)


functions = [
    {
        "name": "xrSubmitDebugUtilsMessageEXT",
        "alias": "submit_message",
        "params": ["instance", "message_severity", "message_type", "callback_data"],
        "return_type": "XrResult",
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrSubmitDebugUtilsMessageEXT.html",
        "raises": [
            "xr.FunctionUnsupportedError",
            "xr.RuntimeFailureError",
            "xr.OutOfMemoryError",
        ]
    },
    ...
]

extension = {
    "name": "XR_EXT_debug_utils",
    "version": 5,
    "vendor_tag": "EXT",
    "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_debug_utils",
}

env = Environment(
    loader=FileSystemLoader("templates"),
    trim_blocks=True,
    lstrip_blocks=True,
)
template = env.get_template("extension_module.py.j2")
rendered = template.render(functions=functions, extension=extensions[0])
print(rendered)
