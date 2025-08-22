"""
xr.ext — Python bindings for OpenXR extensions

This package provides Pythonic access to selected OpenXR extensions, enabling modular and explicit integration of optional runtime features. Each extension is exposed either as a submodule or an object, depending on its structure and usage patterns. The goal is to preserve fidelity to the OpenXR specification while offering ergonomic access for Python developers.

Extensions currently supported include:
- :mod:`xr.ext.KHR.opengl_enable` — OpenGL graphics requirements
- :mod:`xr.ext.MND.headless` — Headless runtime support
- :mod:`xr.ext.EXT.debug_utils` — Debug utilities for naming and tagging objects
- :mod:`xr.ext.HTCX.vive_tracker_interaction` — Vive tracker input support

Each extension module may expose:
- Python wrappers for extension-specific functions
- Constants and enumerations defined by the extension
- Optional helper classes or objects for runtime interaction

To use an extension, ensure its name (e.g. `"XR_EXT_debug_utils"`) is included in the `enabled_extension_names` list during instance creation. Extension functions are only available if the corresponding extension has been enabled.

:seealso: https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#extensions
"""

from . import (
    ext_debug_utils,
    htcx_vive_tracker_interaction,
    khr_opengl_enable,
    mnd_headless,
)

from .ext_debug_utils import *
from .htcx_vive_tracker_interaction import *
from .khr_opengl_enable import *
from .mnd_headless import *

__all__ = []

for subpackage in (
        ext_debug_utils,
        htcx_vive_tracker_interaction,
        khr_opengl_enable,
        mnd_headless,
):
    __all__.extend(subpackage.__all__)
