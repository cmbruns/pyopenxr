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
            :param message_types: Type bitmask for this message.
            :type message_types: xr.DebugUtilsMessageTypeFlagsEXT
            :param callback_data: Prepopulated callback data structure.
            :type callback_data: xr.DebugUtilsMessengerCallbackDataEXT

            :raises xr.FunctionUnsupportedError: If the function is unavailable.
            :raises xr.RuntimeFailureError: On internal runtime errors.
            :raises xr.OutOfMemoryError: If allocation fails.

            :see: https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrSubmitDebugUtilsMessageEXT.html
        """),
    },
    "xr.ext.KHR.opengl_enable.get_graphics_requirements": {
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
    "xr.raw_functions.xrAcquireSwapchainImage": {
        "docstring": inspect.cleandoc("""
            Acquire a swapchain image.
        """),
    },
    "xr.raw_functions.xrApplyHapticFeedback": {
        "docstring": inspect.cleandoc("""
            Apply haptic feedback.
        """),
    },
    "xr.raw_functions.xrAttachSessionActionSets": {
        "docstring": inspect.cleandoc("""
            Attaches action sets to a given session.
        """),
    },
    "xr.raw_functions.xrBeginFrame": {
        "docstring": inspect.cleandoc("""
            Marks a frame.
        """),
    },
    "xr.raw_functions.xrBeginSession": {
        "docstring": inspect.cleandoc("""
            Begins an XrSession.
        """),
    },
    "xr.raw_functions.xrCreateAction": {
        "docstring": inspect.cleandoc("""
            Creates an XrAction.
        """),
    },
    "xr.raw_functions.xrCreateActionSet": {
        "docstring": inspect.cleandoc("""
            Creates an XrActionSet.
        """),
    },
    "xr.raw_functions.xrCreateActionSpace": {
        "docstring": inspect.cleandoc("""
            Creates a space based on a pose action.
        """),
    },
    "xr.raw_functions.xrCreateInstance": {
        "docstring": inspect.cleandoc("""
            Creates an OpenXR Instance.
        """),
    },
    "xr.raw_functions.xrCreateReferenceSpace": {
        "docstring": inspect.cleandoc("""
            Creates a reference space.
        """),
    },
    "xr.raw_functions.xrCreateSession": {
        "docstring": inspect.cleandoc("""
            Creates an XrSession.
        """),
    },
    "xr.raw_functions.xrCreateSwapchain": {
        "docstring": inspect.cleandoc("""
            Creates an XrSwapchain.
        """),
    },
    "xr.raw_functions.xrDestroyAction": {
        "docstring": inspect.cleandoc("""
            Destroys an XrAction.
        """),
    },
    "xr.raw_functions.xrDestroyActionSet": {
        "docstring": inspect.cleandoc("""
            Destroys an XrActionSet.
        """),
    },
    "xr.raw_functions.xrDestroyInstance": {
        "docstring": inspect.cleandoc("""
            Destroy an instance of OpenXR.
        """),
    },
    "xr.raw_functions.xrDestroySession": {
        "docstring": inspect.cleandoc("""
            Destroys an XrSession.
        """),
    },
    "xr.raw_functions.xrDestroySpace": {
        "docstring": inspect.cleandoc("""
            Destroys an XrSpace.
        """),
    },
    "xr.raw_functions.xrDestroySwapchain": {
        "docstring": inspect.cleandoc("""
            Destroys an XrSwapchain.
        """),
    },
    "xr.raw_functions.xrEndFrame": {
        "docstring": inspect.cleandoc("""
            Marks a frame.
        """),
    },
    "xr.raw_functions.xrEndSession": {
        "docstring": inspect.cleandoc("""
            Ends an XrSession.
        """),
    },
    "xr.raw_functions.xrEnumerateApiLayerProperties": {
        "docstring": inspect.cleandoc("""
            Returns up to requested number of global layer properties.
        """),
    },
    "xr.raw_functions.xrEnumerateBoundSourcesForAction": {
        "docstring": inspect.cleandoc("""
            Queries the bound input sources for an action.
        """),
    },
    "xr.raw_functions.xrEnumerateEnvironmentBlendModes": {
        "docstring": inspect.cleandoc("""
            Lists environment blend modes.
        """),
    },
    "xr.raw_functions.xrEnumerateInstanceExtensionProperties": {
        "docstring": inspect.cleandoc("""
            Returns properties of available instance extensions.
        """),
    },
    "xr.raw_functions.xrEnumerateReferenceSpaces": {
        "docstring": inspect.cleandoc("""
            Enumerate available reference spaces.
        """),
    },
    "xr.raw_functions.xrEnumerateSwapchainFormats": {
        "docstring": inspect.cleandoc("""
            Enumerates swapchain formats.
        """),
    },
    "xr.raw_functions.xrEnumerateSwapchainImages": {
        "docstring": inspect.cleandoc("""
            Gets images from an XrSwapchain.
        """),
    },
    "xr.raw_functions.xrEnumerateViewConfigurationViews": {
        "docstring": inspect.cleandoc("""
            Gets view configuration views.
        """),
    },
    "xr.raw_functions.xrEnumerateViewConfigurations": {
        "docstring": inspect.cleandoc("""
            Enumerates supported view configurations.
        """),
    },
    "xr.raw_functions.xrGetActionStateBoolean": {
        "docstring": inspect.cleandoc("""
            Gets boolean action state.
        """),
    },
    "xr.raw_functions.xrGetActionStateFloat": {
        "docstring": inspect.cleandoc("""
            Gets a floating point action state.
        """),
    },
    "xr.raw_functions.xrGetActionStatePose": {
        "docstring": inspect.cleandoc("""
            Gets metadata from a pose action.
        """),
    },
    "xr.raw_functions.xrGetActionStateVector2f": {
        "docstring": inspect.cleandoc("""
            Gets 2D float vector action state.
        """),
    },
    "xr.raw_functions.xrGetCurrentInteractionProfile": {
        "docstring": inspect.cleandoc("""
            Gets the current interaction profile for a top level user paths.
        """),
    },
    "xr.raw_functions.xrGetInputSourceLocalizedName": {
        "docstring": inspect.cleandoc("""
            Gets a localized source name.
        """),
    },
    "xr.raw_functions.xrGetInstanceProcAddr": {
        "docstring": inspect.cleandoc("""
            Gets a function pointer for an OpenXR function.
        """),
    },
    "xr.raw_functions.xrGetInstanceProperties": {
        "docstring": inspect.cleandoc("""
            Gets information about the instance.
        """),
    },
    "xr.raw_functions.xrGetReferenceSpaceBoundsRect": {
        "docstring": inspect.cleandoc("""
            Gets the bounds rectangle of a reference space.
        """),
    },
    "xr.raw_functions.xrGetSystem": {
        "docstring": inspect.cleandoc("""
            Gets a system identifier.
        """),
    },
    "xr.raw_functions.xrGetSystemProperties": {
        "docstring": inspect.cleandoc("""
            Gets the properties of a particular system.
        """),
    },
    "xr.raw_functions.xrGetViewConfigurationProperties": {
        "docstring": inspect.cleandoc("""
            Gets information for a view configuration.
        """),
    },
    "xr.raw_functions.xrLocateSpace": {
        "docstring": inspect.cleandoc("""
            Locates a space with reference to another space.
        """),
    },
    "xr.raw_functions.xrLocateSpaces": {
        "docstring": inspect.cleandoc("""
            Locate an array of spaces.
        """),
    },
    "xr.raw_functions.xrLocateViews": {
        "docstring": inspect.cleandoc("""
            Gets view and projection info.
        """),
    },
    "xr.raw_functions.xrPathToString": {
        "docstring": inspect.cleandoc("""
            Converts a semantic path to a string.
        """),
    },
    "xr.raw_functions.xrPollEvent": {
        "docstring": inspect.cleandoc("""
            Polls for events.
        """),
    },
    "xr.raw_functions.xrReleaseSwapchainImage": {
        "docstring": inspect.cleandoc("""
            Release a swapchain image.
        """),
    },
    "xr.raw_functions.xrRequestExitSession": {
        "docstring": inspect.cleandoc("""
            Request to exit a running session.
        """),
    },
    "xr.raw_functions.xrResultToString": {
        "docstring": inspect.cleandoc("""
            Converts an XrResult to a UTF-8 string.
        """),
    },
    "xr.raw_functions.xrStopHapticFeedback": {
        "docstring": inspect.cleandoc("""
            Stop haptic feedback.
        """),
    },
    "xr.raw_functions.xrStringToPath": {
        "docstring": inspect.cleandoc("""
            Converts a string to a semantic path.
        """),
    },
    "xr.raw_functions.xrStructureTypeToString": {
        "docstring": inspect.cleandoc("""
            Converts an XrStructureType to a UTF-8 string.
        """),
    },
    "xr.raw_functions.xrSuggestInteractionProfileBindings": {
        "docstring": inspect.cleandoc("""
            Sets the application-suggested bindings for the interaction
            profile.
        """),
    },
    "xr.raw_functions.xrSyncActions": {
        "docstring": inspect.cleandoc("""
            Updates the current state of input actions.
        """),
    },
    "xr.raw_functions.xrWaitFrame": {
        "docstring": inspect.cleandoc("""
            Frame timing function.
        """),
    },
    "xr.raw_functions.xrWaitSwapchainImage": {
        "docstring": inspect.cleandoc("""
            Wait for a swapchain image to be available.
        """),
    },
}

__all__ = [
    "function_docstrings",
]
