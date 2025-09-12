"""
Python bindings for the `XR_MNDX_egl_enable` instance extension.

This module provides Python wrappers for OpenXR functions defined in the
`XR_MNDX_egl_enable` specification. These wrappers expose runtime diagnostics,
object naming, and other extension-specific features.

To enable this extension, include `"XR_MNDX_egl_enable"` in your
`enabled_extension_names` when calling :func:`xr.create_instance`.

See the Khronos registry for full specification:
https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_MNDX_egl_enable
"""

__all__ = [
    "EXTENSION_NAME",
    "GraphicsBinding",
    "SPEC_VERSION",
    "VENDOR_TAG",
]

import xr

EXTENSION_NAME = "XR_MNDX_egl_enable"
SPEC_VERSION = 2
VENDOR_TAG = "MNDX"

# Aliases for xr core types
GraphicsBinding = xr.GraphicsBindingEGLMNDX
