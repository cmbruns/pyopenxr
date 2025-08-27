"""
xr.ext — Python bindings for OpenXR extensions

This package provides Pythonic access to selected OpenXR extensions, enabling modular and explicit integration of optional runtime features. Each extension is exposed either as a submodule or an object, depending on its structure and usage patterns. The goal is to preserve fidelity to the OpenXR specification while offering ergonomic access for Python developers.

Each extension module may expose:
- Python wrappers for extension-specific functions
- Constants and enumerations defined by the extension
- Optional helper classes or objects for runtime interaction

To use an extension, ensure its name (e.g. `"XR_EXT_debug_utils"`) is included in the `enabled_extension_names` list during instance creation. Extension functions are only available if the corresponding extension has been enabled.

:seealso: https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#extensions
"""
