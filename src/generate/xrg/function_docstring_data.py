import inspect

# Docstrings for OpenXR Python API functions, indexed by fully-qualified name.
# Strings are cleaned using inspect.cleandoc() to normalize indentation.

function_docstrings = {
    "xr.get_instance_proc_addr": {
        "docstring": inspect.cleandoc("""
            Retrieve a function pointer for an OpenXR core or extension function.
    
            This function wraps the native `xrGetInstanceProcAddr` call, allowing dynamic access
            to OpenXR API functions. It returns a raw function pointer that must be cast to the
            appropriate callable type before use.
    
            If `instance` is `None`, only a limited set of functions may be queried:
            - `xrEnumerateInstanceExtensionProperties`
            - `xrEnumerateApiLayerProperties`
            - `xrCreateInstance`
    
            For extension functions, the corresponding extension must have been enabled during
            instance creation via `enabled_extension_names`.
    
            :param instance: The OpenXR instance handle, or `None` for pre-instance functions.
            :type instance: xr.Instance
            :param name: The name of the function to query (e.g. "xrCreateSession").
            :type name: str
            :return: A raw function pointer (`PFN_xrVoidFunction`) to the requested API function.
            :rtype: xr.PFN_xrVoidFunction
            :raises xr.FunctionUnsupportedError: If the function name is not recognized or not supported.
            :raises xr.HandleInvalidError: If the provided instance handle is invalid.
            :raises xr.InstanceLossPendingError: If the instance is in a loss-pending state.
            :raises xr.InitializationFailedError: If the runtime failed to initialize the query.
            :raises xr.RuntimeFailureError: For general runtime failure not covered by other error codes.
            :seealso: :class:`xr.PFN_xrVoidFunction`
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/xrGetInstanceProcAddr.html",
    }
}
