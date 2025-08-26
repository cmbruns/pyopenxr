from jinja2 import Environment, FileSystemLoader

from xrg.registry import xr_registry

# Enumerate OpenXR extensions
extensions = xr_registry.find("extensions")
assert extensions
for ext in extensions.findall("extension"):
    # Filter for extensions worth wrapping
    assert ext.attrib["name"].startswith("XR_")  # e.g. XR_EXT_debug_utils
    ext_short_name = ext.attrib["name"][len("XR_"):]
    vendor_tag = ext_short_name.split("_")[0]  # e.g. EXT
    ext_short_name = ext_short_name[len(vendor_tag) + 1:]  # e.g debug_utils
    if ext.attrib["supported"] != "openxr":
        continue
    assert ext.attrib["type"] == "instance"
    if ext.attrib["name"] not in ["XR_EXT_debug_utils"]:  # for starters
        continue
    print(ext.attrib["name"], vendor_tag, ext_short_name)
    # Commands
    for require in ext.findall("require"):
        for command in require.findall("command"):
            # Transform C function name to python function name
            c_name = command.attrib["name"]
            assert c_name.startswith("xr")
            py_name = c_name[len("xr"):]
            assert py_name.endswith(vendor_tag)
            py_name = py_name[:-len(vendor_tag)]
            print(c_name, py_name)


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
            "xr.OutOfMemoryError"
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
rendered = template.render(functions=functions, extension=extension)
print(rendered)
