"""
Python bindings for the `XR_KHR_opengl_enable` extension.

This extension provides access to OpenGL-specific graphics requirements via OpenXR.
It wraps `xrGetOpenGLGraphicsRequirementsKHR`, allowing applications to query the
minimum and maximum supported OpenGL versions for a given system.

To use this extension, include `"XR_KHR_opengl_enable"` in the list of enabled
extensions during instance creation.

See the Khronos registry for full specification:
https://registry.khronos.org/OpenXR/specs/1.1/man/html/XR_KHR_opengl_enable.html
"""

from ctypes import byref, cast
import xr

EXTENSION_NAME = "XR_KHR_opengl_enable"
SPEC_VERSION = 11
VENDOR_TAG = "KHR"


def get_opengl_graphics_requirements(
        instance: xr.Instance,
        system_id: xr.SystemId,
) -> xr.GraphicsRequirementsOpenGLKHR:
    """
    Query the OpenGL graphics requirements for a given system.

    This function wraps `xrGetOpenGLGraphicsRequirementsKHR`, returning the minimum and
    maximum OpenGL versions supported by the runtime for the specified system. It is
    typically called before creating a graphics context to ensure compatibility.

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
        xr.get_instance_proc_addr(
            instance=instance,
            name="xrGetOpenGLGraphicsRequirementsKHR",
        ),
        xr.PFN_xrGetOpenGLGraphicsRequirementsKHR
    )
    graphics_requirements = xr.GraphicsRequirementsOpenGLKHR()
    result = pfn(
        instance,
        system_id,
        byref(graphics_requirements))
    result = xr.check_result(xr.Result(result))
    if result.is_exception():
        raise result
    return graphics_requirements


__all__ = [
    "EXTENSION_NAME",
    "SPEC_VERSION",
    "VENDOR_TAG",
    "get_opengl_graphics_requirements",
]
