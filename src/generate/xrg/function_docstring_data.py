import inspect

function_docstrings = {
    "xr.DynamicApiLayerBase.negotiate_loader_api_layer_interface": {
        "docstring": inspect.cleandoc("""

                    Override this method in a derived class to create your own temporary dynamic OpenXR API layer.

                    If this layer is able to support the request, it must: return xr.Result.SUCCESS and:
                        Fill in pname:layerRequest→pname:layerInterfaceVersion with the API layer interface version it desires to support.
                        Fill in pname:layerRequest→pname:layerApiVersion with the API version of OpenXR it will execute under.
                        Fill in pname:layerRequest→pname:getInstanceProcAddr with a valid function pointer so that the loader can query function pointers to the remaining OpenXR commands supported by the API layer.
                        Fill in pname:layerRequest→pname:createLayerInstance with a valid function pointer so that the loader can create the instance through the API layer call chain.

                    Otherwise, it must: return XR_ERROR_INITIALIZATION_FAILED

                    :param: loader_info: must be a valid pointer to a constant xr.NegotiateLoaderInfo structure.
                    :param: layer_name: must be a string listing the name of an API layer which the loader is attempting to negotiate with.
                    :param: api_layer_request: must be a valid pointer to a xr.NegotiateApiLayerRequest structure.
                    :return: xr.Result.SUCCESS or xr.Result.ERROR_INITIALIZATION_FAILED
        
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/xrNegotiateLoaderApiLayerInterface.html",
    },
    "xr.Version.number": {
        "docstring": inspect.cleandoc("""
            Packed xr.VersionNumber
        """),
    },
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
    },
    "xr.expose_packaged_api_layers": {
        "docstring": inspect.cleandoc("""

                Make pre-packaged layers available to the openxr loader
    
        """),
    },
    "xr.ext.EXT.debug_utils.create_messenger": {
        "docstring": inspect.cleandoc("""

                Create a debug messenger for the given instance.

                Thin wrapper over `xr.DebugUtilsMessengerEXT`. If `create_info` is omitted,
                defaults will enable all severities/types and route messages to the Python logger.

                :param instance: The OpenXR instance.
                :type instance: xr.Instance
                :param create_info: Optional create-info descriptor.
                :type create_info: xr.DebugUtilsMessengerCreateInfoEXT or None

                :returns: A new `DebugUtilsMessengerEXT` handle.
                :rtype: xr.DebugUtilsMessengerEXT

                :raises xr.FunctionUnsupportedError: If the extension isn’t enabled.
                :raises xr.ValidationFailureError: If parameters are rejected by the runtime.
                :raises xr.RuntimeFailureError: On internal runtime errors.
                :raises xr.OutOfMemoryError: If allocation fails.
                :raises xr.LimitReachedError: If no more messengers can be created.

                :see: https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrCreateDebugUtilsMessengerEXT.html
    
        """),
    },
    "xr.ext.EXT.debug_utils.destroy_messenger": {
        "docstring": inspect.cleandoc("""

                Destroy a debug messenger, releasing its native resources.

                :param messenger: The messenger to destroy.
                :type messenger: xr.DebugUtilsMessengerEXT

                :raises xr.FunctionUnsupportedError: If the function is unavailable.
                :raises xr.HandleInvalidError: If `messenger` is not a valid handle.

                :see: https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrDestroyDebugUtilsMessengerEXT.html
    
        """),
    },
    "xr.ext.EXT.debug_utils.log_level_for_severity": {
        "docstring": inspect.cleandoc("""

                Convert OpenXR message severities to Python logging levels.

                :param severity_flags: Bitmask of message severity flags.
                :type severity_flags: xr.DebugUtilsMessageSeverityFlagsEXT
                :returns: One of logging.DEBUG, INFO, WARNING, or ERROR.
    
        """),
    },
    "xr.ext.EXT.debug_utils.session_begin_label_region": {
        "docstring": inspect.cleandoc("""

                Begin a labeled debug region in the specified session.

                This marks the start of a profiling or annotation region in the runtime.

                :param session: The OpenXR session.
                :type session: xr.Session
                :param label_info: A `DebugUtilsLabelEXT` structure describing the region.
                :type label_info: xr.DebugUtilsLabelEXT

                :raises xr.FunctionUnsupportedError: If the function is unavailable.
                :raises xr.HandleInvalidError: If `session` is not a valid handle.
                :raises xr.InstanceLostError: If the session’s instance has been lost.

                :see: https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrSessionBeginDebugUtilsLabelRegionEXT.html
    
        """),
    },
    "xr.ext.EXT.debug_utils.session_end_label_region": {
        "docstring": inspect.cleandoc("""

                End the current labeled debug region in the specified session.

                :param session: The OpenXR session.
                :type session: xr.Session

                :raises xr.FunctionUnsupportedError: If the function is unavailable.
                :raises xr.HandleInvalidError: If `session` is not a valid handle.
                :raises xr.InstanceLostError: If the session’s instance has been lost.

                :see: https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrSessionEndDebugUtilsLabelRegionEXT.html
    
        """),
    },
    "xr.ext.EXT.debug_utils.session_insert_label": {
        "docstring": inspect.cleandoc("""

                Insert a single debug label into the command stream.

                Use this for point-in-time annotations rather than begin/end regions.

                :param session: The OpenXR session.
                :type session: xr.Session
                :param label_info: A `DebugUtilsLabelEXT` structure with the label text.
                :type label_info: xr.DebugUtilsLabelEXT

                :raises xr.FunctionUnsupportedError: If the function is unavailable.
                :raises xr.HandleInvalidError: If `session` is not a valid handle.
                :raises xr.InstanceLostError: If the session’s instance has been lost.

                :see: https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrSessionInsertDebugUtilsLabelEXT.html
    
        """),
    },
    "xr.ext.EXT.debug_utils.set_object_name": {
        "docstring": inspect.cleandoc("""

                Assign a human-readable name to an OpenXR object.

                :param instance: The OpenXR instance.
                :type instance: xr.Instance
                :param name_info: A `DebugUtilsObjectNameInfoEXT` structure.
                :type name_info: xr.DebugUtilsObjectNameInfoEXT

                :raises xr.FunctionUnsupportedError: If the function is unavailable.
                :raises xr.HandleInvalidError: If `name_info.objectHandle` is invalid.

                :see: https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrSetDebugUtilsObjectNameEXT.html
    
        """),
    },
    "xr.ext.EXT.debug_utils.submit_message": {
        "docstring": inspect.cleandoc("""

                Submit a user-generated debug message to the runtime.

                :param instance: The OpenXR instance.
                :type instance: xr.Instance
                :param message_severity: Severity bitmask for this message.
                :type message_severity: xr.DebugUtilsMessageSeverityFlagsEXT
                :param message_type: Type bitmask for this message.
                :type message_type: xr.DebugUtilsMessageTypeFlagsEXT
                :param callback_data: Prepopulated callback data structure.
                :type callback_data: xr.DebugUtilsMessengerCallbackDataEXT

                :raises xr.FunctionUnsupportedError: If the function is unavailable.
                :raises xr.RuntimeFailureError: On internal runtime errors.
                :raises xr.OutOfMemoryError: If allocation fails.

                :see: https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrSubmitDebugUtilsMessageEXT.html
    
        """),
    },
    "xr.ext.KHR.opengl_enable.get_opengl_graphics_requirements": {
        "docstring": inspect.cleandoc("""

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
    
        """),
    },
    "xr.ext.KhrOpenGLEnable.get_opengl_graphics_requirements": {
        "docstring": inspect.cleandoc("""
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
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/xrGetOpenGLGraphicsRequirementsKHR.html",
    },
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
    },
}

__all__ = [
    "function_docstrings",
]
