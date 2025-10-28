import inspect

module_docstrings = {
    "xr": {
        "docstring": inspect.cleandoc("""
            `xr` is the root module of pyopenxr, an unofficial Python binding for the OpenXR SDK.

            It provides low-level access to the core OpenXR API for interacting with VR and AR runtimes,
            including system queries, session management, and extension dispatch. This module wraps the
            standard C interface in a Pythonic structure while preserving fidelity to the original spec.

            For high-level utilities and ergonomic abstractions, see submodules and helper packages.
        """),
    },
    "xr.ext.EXT.debug_utils": {
        "docstring": inspect.cleandoc("""
            Python bindings for the `XR_EXT_debug_utils` instance extension.

            This module provides Python wrappers for OpenXR functions defined in the
            `XR_EXT_debug_utils` specification. These wrappers expose runtime diagnostics,
            object naming, and other extension-specific features.

            To enable this extension, include `"XR_EXT_debug_utils"` in your
            `enabled_extension_names` when calling :func:`xr.create_instance`.

            See the Khronos registry for full specification:
            https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_debug_utils
        """),
    },
    "xr.ext.HTCX.vive_tracker_interaction": {
        "docstring": inspect.cleandoc("""
            Python bindings for the `XR_HTCX_vive_tracker_interaction` extension.

            This extension enables interaction with VIVE Tracker devices via OpenXR.
            It defines symbolic paths and event structures for tracker identification and role assignment,
            but does not currently expose any functions or structures for direct use in Python.

            This stub provides metadata and symbolic access to the extension name for use during
            instance creation. Future versions may wrap `xrEnumerateViveTrackerPathsHTCX` or related
            functionality if deemed useful.

            See the Khronos registry for full specification:
            https://registry.khronos.org/OpenXR/specs/1.1/man/html/XR_HTCX_vive_tracker_interaction.html
        """),
    },
    "xr.ext.KHR.opengl_enable": {
        "docstring": inspect.cleandoc("""
            Python bindings for the `XR_KHR_opengl_enable` instance extension.

            This extension provides access to OpenGL-specific graphics requirements via OpenXR.
            It wraps `xrGetOpenGLGraphicsRequirementsKHR`, allowing applications to query the
            minimum and maximum supported OpenGL versions for a given system.

            To enable this extension, include `"XR_KHR_opengl_enable"` in your
            `enabled_extension_names` when calling :func:`xr.create_instance`.

            See the Khronos registry for full specification:
            https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_opengl_enable
        """),
    },
    "xr.ext.KHR.opengl_es_enable": {
        "docstring": inspect.cleandoc("""
            Python bindings for the `XR_KHR_opengl_es_enable` instance extension.

            This module provides Python wrappers for OpenXR functions defined in the
            `XR_KHR_opengl_es_enable` specification. These wrappers expose runtime diagnostics,
            object naming, and other extension-specific features.

            To enable this extension, include `"XR_KHR_opengl_es_enable"` in your
            `enabled_extension_names` when calling :func:`xr.create_instance`.

            See the Khronos registry for full specification:
            https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_opengl_es_enable
        """),
    },
    "xr.ext.MND.headless": {
        "docstring": inspect.cleandoc("""
            Python bindings for the `XR_MND_headless` instance extension.

            This extension enables OpenXR runtimes to operate without presenting rendered frames
            to a display. It is useful for automated testing, simulation, or server-side applications
            where visual output is unnecessary.

            The extension does not define any new functions or structures. Its presence is indicated
            by the string `"XR_MND_headless"` in the list of enabled extensions during instance creation.

            To enable headless mode, include `"XR_MND_headless"` in the `enabled_extension_names` list
            when calling :func:`xr.create_instance`.

            See the Khronos registry for full specification:
            https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_MND_headless
        """),
    },
}

__all__ = [
    "module_docstrings",
]
