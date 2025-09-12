"""
Python bindings for the `XR_KHR_opengl_es_enable` instance extension.

This module provides Python wrappers for OpenXR functions defined in the
`XR_KHR_opengl_es_enable` specification. These wrappers expose runtime diagnostics,
object naming, and other extension-specific features.

To enable this extension, include `"XR_KHR_opengl_es_enable"` in your
`enabled_extension_names` when calling :func:`xr.create_instance`.

See the Khronos registry for full specification:
https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_opengl_es_enable
"""

__all__ = [
    "EXTENSION_NAME",
    "GraphicsBindingAndroid",
    "GraphicsRequirements",
    "SPEC_VERSION",
    "SwapchainImage",
    "SwapchainStateSamplerFB",
    "VENDOR_TAG",
    "get_graphics_requirements",
]

from ctypes import byref, cast

import xr

EXTENSION_NAME = "XR_KHR_opengl_es_enable"
SPEC_VERSION = 9
VENDOR_TAG = "KHR"

# Aliases for xr core types
GraphicsBindingAndroid = xr.GraphicsBindingOpenGLESAndroidKHR
GraphicsRequirements = xr.GraphicsRequirementsOpenGLESKHR
SwapchainImage = xr.SwapchainImageOpenGLESKHR
SwapchainStateSamplerFB = xr.SwapchainStateSamplerOpenGLESFB


def get_graphics_requirements(
    instance: xr.Instance,
    system_id: xr.SystemId,
) -> GraphicsRequirements:
    pfn = cast(
        xr.get_instance_proc_addr(instance, "xrGetOpenGLESGraphicsRequirementsKHR"),
        xr.PFN_xrGetOpenGLESGraphicsRequirementsKHR,
    )        
    graphics_requirements = GraphicsRequirements()
    result_code = pfn(
        instance,
        system_id,
        byref(graphics_requirements),
    )
    checked = xr.check_result(xr.Result(result_code))
    if checked.is_exception():
        raise checked
    return graphics_requirements
