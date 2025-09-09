"""
Python bindings for the `XR_KHR_opengl_enable` instance extension.

This extension provides access to OpenGL-specific graphics requirements via OpenXR.
It wraps `xrGetOpenGLGraphicsRequirementsKHR`, allowing applications to query the
minimum and maximum supported OpenGL versions for a given system.

To enable this extension, include `"XR_KHR_opengl_enable"` in your
`enabled_extension_names` when calling :func:`xr.create_instance`.

See the Khronos registry for full specification:
https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_opengl_enable
"""

__all__ = [
    "EXTENSION_NAME",
    "GraphicsBindingESAndroid",
    "GraphicsBindingWayland",
    "GraphicsBindingWin32",
    "GraphicsBindingXcb",
    "GraphicsBindingXlib",
    "GraphicsRequirements",
    "GraphicsRequirementsES",
    "SPEC_VERSION",
    "SwapchainImage",
    "SwapchainImageES",
    "SwapchainStateSamplerESFB",
    "VENDOR_TAG",
    "get_graphics_requirements",
]

from ctypes import byref, cast

import xr

EXTENSION_NAME = "XR_KHR_opengl_enable"
SPEC_VERSION = 11
VENDOR_TAG = "KHR"

# Aliases for xr core types
GraphicsBindingESAndroid = xr.GraphicsBindingOpenGLESAndroidKHR
GraphicsBindingWayland = xr.GraphicsBindingOpenGLWaylandKHR
GraphicsBindingWin32 = xr.GraphicsBindingOpenGLWin32KHR
GraphicsBindingXcb = xr.GraphicsBindingOpenGLXcbKHR
GraphicsBindingXlib = xr.GraphicsBindingOpenGLXlibKHR
GraphicsRequirements = xr.GraphicsRequirementsOpenGLKHR
GraphicsRequirementsES = xr.GraphicsRequirementsOpenGLESKHR
SwapchainImage = xr.SwapchainImageOpenGLKHR
SwapchainImageES = xr.SwapchainImageOpenGLESKHR
SwapchainStateSamplerESFB = xr.SwapchainStateSamplerOpenGLESFB


def get_graphics_requirements(
    instance: xr.Instance,
    system_id: xr.SystemId,
) -> GraphicsRequirements:
    """
    Query the OpenGL graphics requirements for a given system.

    This function wraps `xrGetOpenGLGraphicsRequirementsKHR`, returning the minimum and
    maximum OpenGL versions supported by the runtime for the specified system. It is
    typically called before creating a graphics context to ensure compatibility.

    :param instance: The OpenXR instance.
    :type instance: xr.Instance
    :param system_id: The system identifier obtained via `xr.get_system()`.
    :type system_id: xr.SystemId
    :return: A structure containing the OpenGL graphics requirements.
    :rtype: xr.GraphicsRequirementsOpenGLKHR
    :raises xr.FunctionUnsupportedError: If the extension function is unavailable.
    :raises xr.HandleInvalidError: If the instance handle is invalid.
    :raises xr.SystemInvalidError: If the system ID is not recognized.
    :raises xr.InstanceLossPendingError: If the instance is in a loss-pending state.
    :seealso: :class:`xr.GraphicsRequirementsOpenGLKHR`
    :see: https://registry.khronos.org/OpenXR/specs/1.1/man/html/xrGetOpenGLGraphicsRequirementsKHR.html
    """
    pfn = cast(
        xr.get_instance_proc_addr(instance, "xrGetOpenGLGraphicsRequirementsKHR"),
        xr.PFN_xrGetOpenGLGraphicsRequirementsKHR,
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
