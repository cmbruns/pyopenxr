import inspect

class_docstrings = {
    "xr.ActionTypeMismatchError": {
        "docstring": inspect.cleandoc("""
            The API used to retrieve an action's state does not match the action's type.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.ActionsetNotAttachedError": {
        "docstring": inspect.cleandoc("""
            A referenced action set is not attached to the session.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.ActionsetsAlreadyAttachedError": {
        "docstring": inspect.cleandoc("""
            The session already has attached action sets.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.ApiLayerNotPresentError": {
        "docstring": inspect.cleandoc("""
            A requested API layer is not present or could not be loaded.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.ApiVersionUnsupportedError": {
        "docstring": inspect.cleandoc("""
            The runtime does not support the requested API version.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.CallOrderInvalidError": {
        "docstring": inspect.cleandoc("""
            The call was made without having made a previously required call.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.DynamicApiLayerBase": {
        "docstring": inspect.cleandoc("""
            Base class for temporary dynamic runtime python OpenXR API layers.
        """),
    },
    "xr.EnvironmentBlendModeUnsupportedError": {
        "docstring": inspect.cleandoc("""
            The specified environment blend mode is not supported by the runtime or platform.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.ErrorResult": {
        "docstring": inspect.cleandoc("""
            Error during OpenXR function call.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.EventUnavailable": {
        "docstring": inspect.cleandoc("""
            No event was available.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.ExtensionNotPresentError": {
        "docstring": inspect.cleandoc("""
            A requested extension is not supported.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.FeatureUnsupportedError": {
        "docstring": inspect.cleandoc("""
            The requested feature is not supported.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.FileAccessErrorError": {
        "docstring": inspect.cleandoc("""
            The file could not be accessed.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.FileContentsInvalidError": {
        "docstring": inspect.cleandoc("""
            The file's contents were invalid.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.FormFactorUnavailableError": {
        "docstring": inspect.cleandoc("""
            The specified form factor is supported, but the device is currently not available, e.g. not plugged in or powered off.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.FormFactorUnsupportedError": {
        "docstring": inspect.cleandoc("""
            The specified form factor is not supported by the current runtime or platform.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.FrameDiscarded": {
        "docstring": inspect.cleandoc("""
            A frame has been discarded from composition.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.FunctionUnsupportedError": {
        "docstring": inspect.cleandoc("""
            The requested function was not found or is otherwise unsupported.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.GraphicsDeviceInvalidError": {
        "docstring": inspect.cleandoc("""
            The given graphics device is not in a valid state. The graphics device could be lost or initialized without meeting graphics requirements.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.GraphicsRequirementsCallMissingError": {
        "docstring": inspect.cleandoc("""
            The fname:xrGetGraphicsRequirements* call was not made before calling fname:xrCreateSession.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.HandleInvalidError": {
        "docstring": inspect.cleandoc("""
            A supplied object handle was invalid.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.IndexOutOfRangeError": {
        "docstring": inspect.cleandoc("""
            The supplied index was outside the range of valid indices.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.InitializationFailedError": {
        "docstring": inspect.cleandoc("""
            Initialization of object could not be completed.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.Instance": {
        "docstring": inspect.cleandoc("""

                Opaque handle to an OpenXR instance object.

                An `xr.Instance` represents a connection between an OpenXR application and the
                OpenXR runtime. It encapsulates all runtime-managed state and serves as the root
                object for most OpenXR operations, including system queries, session creation,
                and extension dispatch.

                This object may be instantiated directly with an optional `xr.InstanceCreateInfo`
                descriptor. If none is provided, a default descriptor will be used. Initialization
                is performed lazily, with runtime bindings deferred to minimize import-time overhead
                and avoid ordering issues.

                `Instance` supports context management protocols and may be used in a `with` block
                for automatic cleanup:

                .. code-block:: python

                    with xr.Instance(...) as instance:
                        ...

                Internally, this object wraps a pointer to the OpenXR instance and delegates all
                interactions to the runtime via raw API functions. It is opaque and cannot be
                directly inspected or modified.

                :seealso: :func:`xr.create_instance`, :func:`xr.destroy_instance`, :class:`xr.InstanceCreateInfo`
    
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrInstance.html",
    },
    "xr.InstanceLostError": {
        "docstring": inspect.cleandoc("""
            The slink:XrInstance was lost or could not be found. It will need to be destroyed and optionally recreated.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.LayerInvalidError": {
        "docstring": inspect.cleandoc("""
            The layer was NULL or otherwise invalid.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.LayerLimitExceededError": {
        "docstring": inspect.cleandoc("""
            The number of specified layers is greater than the supported number.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.LimitReachedError": {
        "docstring": inspect.cleandoc("""
            The runtime supports no more of the requested resource.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.LocalizedNameDuplicatedError": {
        "docstring": inspect.cleandoc("""
            The localized name provided was a duplicate of an already-existing resource.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.LocalizedNameInvalidError": {
        "docstring": inspect.cleandoc("""
            The localized name provided was invalid.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.NameDuplicatedError": {
        "docstring": inspect.cleandoc("""
            The name provided was a duplicate of an already-existing resource.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.NameInvalidError": {
        "docstring": inspect.cleandoc("""
            The name provided was invalid.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.OutOfMemoryError": {
        "docstring": inspect.cleandoc("""
            A memory allocation has failed.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.PathCountExceededError": {
        "docstring": inspect.cleandoc("""
            The maximum number of supported semantic paths has been reached.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.PathFormatInvalidError": {
        "docstring": inspect.cleandoc("""
            The semantic path character format is invalid.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.PathInvalidError": {
        "docstring": inspect.cleandoc("""
            The provided basetype:XrPath was not valid.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.PathUnsupportedError": {
        "docstring": inspect.cleandoc("""
            The semantic path is unsupported.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.PoseInvalidError": {
        "docstring": inspect.cleandoc("""
            The supplied pose was invalid with respect to the requirements.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.QualifiedSuccessResult": {
        "docstring": inspect.cleandoc("""
            An OpenXR function returned a non-error status other than SUCCESS
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.ReferenceSpaceUnsupportedError": {
        "docstring": inspect.cleandoc("""
            The specified reference space is not supported by the runtime or system.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.ResultException": {
        "docstring": inspect.cleandoc("""
            Exception related to return value of and OpenXR function.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.RuntimeFailureError": {
        "docstring": inspect.cleandoc("""
            The runtime failed to handle the function in an unexpected way that is not covered by another error result. 
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.RuntimeUnavailableError": {
        "docstring": inspect.cleandoc("""
            The loader was unable to find or load a runtime.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.SessionLossPending": {
        "docstring": inspect.cleandoc("""
            The session will be lost soon.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.SessionLostError": {
        "docstring": inspect.cleandoc("""
            The slink:XrSession was lost. It will need to be destroyed and optionally recreated.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.SessionNotFocused": {
        "docstring": inspect.cleandoc("""
            The session is not in the focused state.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.SessionNotReadyError": {
        "docstring": inspect.cleandoc("""
            The session is not in the ready state.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.SessionNotRunningError": {
        "docstring": inspect.cleandoc("""
            The session <<session-not-running, is not yet running>>.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.SessionNotStoppingError": {
        "docstring": inspect.cleandoc("""
            The session is not in the stopping state.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.SessionRunningError": {
        "docstring": inspect.cleandoc("""
            The session <<session-running, is already running>>.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.SizeInsufficientError": {
        "docstring": inspect.cleandoc("""
            The supplied size was smaller than required.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.SpaceBoundsUnavailable": {
        "docstring": inspect.cleandoc("""
            The space's bounds are not known at the moment.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.Success": {
        "docstring": inspect.cleandoc("""
            Function successfully completed.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.SwapchainFormatUnsupportedError": {
        "docstring": inspect.cleandoc("""
            The image format is not supported by the runtime or platform.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.SwapchainRectInvalidError": {
        "docstring": inspect.cleandoc("""
            The image rect was negatively sized or otherwise invalid.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.SystemInvalidError": {
        "docstring": inspect.cleandoc("""
            The provided basetype:XrSystemId was invalid.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.TimeInvalidError": {
        "docstring": inspect.cleandoc("""
            The provided basetype:XrTime was zero, negative, or out of range.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.TimeoutExpired": {
        "docstring": inspect.cleandoc("""
            The specified timeout time occurred before the operation could complete.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.ValidationFailureError": {
        "docstring": inspect.cleandoc("""
            The function usage was invalid in some way.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.ViewConfigurationTypeUnsupportedError": {
        "docstring": inspect.cleandoc("""
            The specified view configuration type is not supported by the runtime or platform.
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html",
    },
    "xr.XrException": {
        "docstring": inspect.cleandoc("""
            Base class for all OpenXR exceptions.
        """),
    },
    "xr.ext.InstanceExtension": {
        "docstring": inspect.cleandoc("""

                Base class for Pythonic OpenXR extension implementations.

                Provides a helper for calling extension entry points obtained via
                :func:`xr.get_instance_proc_addr`, casting them to the correct
                function-pointer type, invoking with the supplied arguments, and
                checking the :class:`xr.Result`.

                :param instance: The OpenXR instance to which this extension is bound.
                :type instance: xr.Instance
    
        """),
    },
}

__all__ = [
    "class_docstrings",
]
