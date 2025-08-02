import inspect

# Docstrings for OpenXR Python API functions, indexed by fully-qualified name.
# Strings are cleaned using inspect.cleandoc() to normalize indentation.

function_docstrings = {
    "xr.create_instance": {
        "docstring": inspect.cleandoc("""
            Create a new OpenXR instance.

            This function wraps the native :func:`xrCreateInstance` call, establishing a connection
            between the application and the OpenXR runtime. It enables requested API layers and
            extensions, and returns an opaque handle to the newly created instance.

            If `create_info` is not provided, a default :class:`xr.InstanceCreateInfo` will be used.

            :param create_info: Optional descriptor specifying application info, enabled extensions,
                                and platform-specific parameters.
            :type create_info: xr.InstanceCreateInfo or None
            :return: A newly created OpenXR instance handle.
            :rtype: xr.Instance
            :raises xr.ValidationFailureError: If validation layers reject the configuration.
            :raises xr.RuntimeFailureError: If the runtime fails to initialize.
            :raises xr.OutOfMemoryError: If memory allocation fails.
            :raises xr.LimitReachedError: If the runtime cannot support additional instances.
            :raises xr.RuntimeUnavailableError: If no runtime is available.
            :raises xr.NameInvalidError: If the application name is empty.
            :raises xr.InitializationFailedError: If platform-specific initialization fails.
            :raises xr.ExtensionNotPresentError: If a requested extension is missing.
            :raises xr.ExtensionDependencyNotEnabledError: If an extension dependency is missing.
            :raises xr.ApiVersionUnsupportedError: If the requested API version is not supported.
            :raises xr.ApiLayerNotPresentError: If a requested API layer is missing.
            :seealso: :class:`xr.Instance`, :class:`xr.InstanceCreateInfo`
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/xrCreateInstance.html",
    }
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
    "xr.Instance.__init__": {
        "docstring": inspect.cleandoc("""
            Construct and initialize an OpenXR instance.
    
            This constructor wraps the native :func:`xrCreateInstance` call, creating a new
            OpenXR instance and binding it to this object. If `create_info` is not provided,
            a default descriptor will be used.
    
            Initialization is performed lazily, with runtime bindings imported just-in-time
            to avoid circular dependencies and ordering issues. This object supports context
            management for automatic teardown via :func:`xr.destroy_instance`.
    
            :param create_info: Optional descriptor specifying application info, enabled extensions,
                                and platform-specific parameters.
            :type create_info: xr.InstanceCreateInfo or None
            :raises xr.ValidationFailureError: If validation layers reject the configuration.
            :raises xr.RuntimeFailureError: If the runtime fails to initialize.
            :raises xr.OutOfMemoryError: If memory allocation fails.
            :raises xr.LimitReachedError: If the runtime cannot support additional instances.
            :raises xr.RuntimeUnavailableError: If no runtime is available.
            :raises xr.NameInvalidError: If the application name is empty.
            :raises xr.InitializationFailedError: If platform-specific initialization fails.
            :raises xr.ExtensionNotPresentError: If a requested extension is missing.
            :raises xr.ExtensionDependencyNotEnabledError: If an extension dependency is missing.
            :raises xr.ApiVersionUnsupportedError: If the requested API version is not supported.
            :raises xr.ApiLayerNotPresentError: If a requested API layer is missing.
            :seealso: :func:`xr.create_instance`, :func:`xr.destroy_instance`, :class:`xr.InstanceCreateInfo`
    """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/xrCreateInstance.html",
    }
}
