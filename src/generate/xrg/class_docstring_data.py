import inspect

class_docstrings = {
    "xr.ActionTypeMismatchError": {
        "docstring": inspect.cleandoc("""
            The API used to retrieve an action's state does not match the action's type.
        """),
    },
    "xr.ActionsetNotAttachedError": {
        "docstring": inspect.cleandoc("""
            A referenced action set is not attached to the session.
        """),
    },
    "xr.ActionsetsAlreadyAttachedError": {
        "docstring": inspect.cleandoc("""
            The session already has attached action sets.
        """),
    },
    "xr.ApiLayerNotPresentError": {
        "docstring": inspect.cleandoc("""
            A requested API layer is not present or could not be loaded.
        """),
    },
    "xr.ApiVersionUnsupportedError": {
        "docstring": inspect.cleandoc("""
            The runtime does not support the requested API version.
        """),
    },
    "xr.CallOrderInvalidError": {
        "docstring": inspect.cleandoc("""
            The call was made without having made a previously required call.
        """),
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
    },
    "xr.ErrorResult": {
        "docstring": inspect.cleandoc("""
            Error during OpenXR function call.
        """),
    },
    "xr.EventUnavailable": {
        "docstring": inspect.cleandoc("""
            No event was available.
        """),
    },
    "xr.ExtensionNotPresentError": {
        "docstring": inspect.cleandoc("""
            A requested extension is not supported.
        """),
    },
    "xr.FeatureUnsupportedError": {
        "docstring": inspect.cleandoc("""
            The requested feature is not supported.
        """),
    },
    "xr.FileAccessErrorError": {
        "docstring": inspect.cleandoc("""
            The file could not be accessed.
        """),
    },
    "xr.FileContentsInvalidError": {
        "docstring": inspect.cleandoc("""
            The file's contents were invalid.
        """),
    },
    "xr.FormFactorUnavailableError": {
        "docstring": inspect.cleandoc("""
            The specified form factor is supported, but the device is currently not available, e.g. not plugged in or powered off.
        """),
    },
    "xr.FormFactorUnsupportedError": {
        "docstring": inspect.cleandoc("""
            The specified form factor is not supported by the current runtime or platform.
        """),
    },
    "xr.FrameDiscarded": {
        "docstring": inspect.cleandoc("""
            A frame has been discarded from composition.
        """),
    },
    "xr.FunctionUnsupportedError": {
        "docstring": inspect.cleandoc("""
            The requested function was not found or is otherwise unsupported.
        """),
    },
    "xr.GraphicsDeviceInvalidError": {
        "docstring": inspect.cleandoc("""
            The given graphics device is not in a valid state. The graphics device could be lost or initialized without meeting graphics requirements.
        """),
    },
    "xr.GraphicsRequirementsCallMissingError": {
        "docstring": inspect.cleandoc("""
            The fname:xrGetGraphicsRequirements* call was not made before calling fname:xrCreateSession.
        """),
    },
    "xr.HandleInvalidError": {
        "docstring": inspect.cleandoc("""
            A supplied object handle was invalid.
        """),
    },
    "xr.IndexOutOfRangeError": {
        "docstring": inspect.cleandoc("""
            The supplied index was outside the range of valid indices.
        """),
    },
    "xr.InitializationFailedError": {
        "docstring": inspect.cleandoc("""
            Initialization of object could not be completed.
        """),
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
    },
    "xr.LayerInvalidError": {
        "docstring": inspect.cleandoc("""
            The layer was NULL or otherwise invalid.
        """),
    },
    "xr.LayerLimitExceededError": {
        "docstring": inspect.cleandoc("""
            The number of specified layers is greater than the supported number.
        """),
    },
    "xr.LimitReachedError": {
        "docstring": inspect.cleandoc("""
            The runtime supports no more of the requested resource.
        """),
    },
    "xr.LocalizedNameDuplicatedError": {
        "docstring": inspect.cleandoc("""
            The localized name provided was a duplicate of an already-existing resource.
        """),
    },
    "xr.LocalizedNameInvalidError": {
        "docstring": inspect.cleandoc("""
            The localized name provided was invalid.
        """),
    },
    "xr.NameDuplicatedError": {
        "docstring": inspect.cleandoc("""
            The name provided was a duplicate of an already-existing resource.
        """),
    },
    "xr.NameInvalidError": {
        "docstring": inspect.cleandoc("""
            The name provided was invalid.
        """),
    },
    "xr.OutOfMemoryError": {
        "docstring": inspect.cleandoc("""
            A memory allocation has failed.
        """),
    },
    "xr.PathCountExceededError": {
        "docstring": inspect.cleandoc("""
            The maximum number of supported semantic paths has been reached.
        """),
    },
    "xr.PathFormatInvalidError": {
        "docstring": inspect.cleandoc("""
            The semantic path character format is invalid.
        """),
    },
    "xr.PathInvalidError": {
        "docstring": inspect.cleandoc("""
            The provided basetype:XrPath was not valid.
        """),
    },
    "xr.PathUnsupportedError": {
        "docstring": inspect.cleandoc("""
            The semantic path is unsupported.
        """),
    },
    "xr.PoseInvalidError": {
        "docstring": inspect.cleandoc("""
            The supplied pose was invalid with respect to the requirements.
        """),
    },
    "xr.QualifiedSuccessResult": {
        "docstring": inspect.cleandoc("""
            An OpenXR function returned a non-error status other than SUCCESS
        """),
    },
    "xr.ReferenceSpaceUnsupportedError": {
        "docstring": inspect.cleandoc("""
            The specified reference space is not supported by the runtime or system.
        """),
    },
    "xr.ResultException": {
        "docstring": inspect.cleandoc("""
            Exception related to return value of and OpenXR function.
        """),
    },
    "xr.RuntimeFailureError": {
        "docstring": inspect.cleandoc("""
            The runtime failed to handle the function in an unexpected way that is not covered by another error result. 
        """),
    },
    "xr.RuntimeUnavailableError": {
        "docstring": inspect.cleandoc("""
            The loader was unable to find or load a runtime.
        """),
    },
    "xr.SessionLossPending": {
        "docstring": inspect.cleandoc("""
            The session will be lost soon.
        """),
    },
    "xr.SessionLostError": {
        "docstring": inspect.cleandoc("""
            The slink:XrSession was lost. It will need to be destroyed and optionally recreated.
        """),
    },
    "xr.SessionNotFocused": {
        "docstring": inspect.cleandoc("""
            The session is not in the focused state.
        """),
    },
    "xr.SessionNotReadyError": {
        "docstring": inspect.cleandoc("""
            The session is not in the ready state.
        """),
    },
    "xr.SessionNotRunningError": {
        "docstring": inspect.cleandoc("""
            The session <<session-not-running, is not yet running>>.
        """),
    },
    "xr.SessionNotStoppingError": {
        "docstring": inspect.cleandoc("""
            The session is not in the stopping state.
        """),
    },
    "xr.SessionRunningError": {
        "docstring": inspect.cleandoc("""
            The session <<session-running, is already running>>.
        """),
    },
    "xr.SizeInsufficientError": {
        "docstring": inspect.cleandoc("""
            The supplied size was smaller than required.
        """),
    },
    "xr.SpaceBoundsUnavailable": {
        "docstring": inspect.cleandoc("""
            The space's bounds are not known at the moment.
        """),
    },
    "xr.Success": {
        "docstring": inspect.cleandoc("""
            Function successfully completed.
        """),
    },
    "xr.SwapchainFormatUnsupportedError": {
        "docstring": inspect.cleandoc("""
            The image format is not supported by the runtime or platform.
        """),
    },
    "xr.SwapchainRectInvalidError": {
        "docstring": inspect.cleandoc("""
            The image rect was negatively sized or otherwise invalid.
        """),
    },
    "xr.SystemInvalidError": {
        "docstring": inspect.cleandoc("""
            The provided basetype:XrSystemId was invalid.
        """),
    },
    "xr.TimeInvalidError": {
        "docstring": inspect.cleandoc("""
            The provided basetype:XrTime was zero, negative, or out of range.
        """),
    },
    "xr.TimeoutExpired": {
        "docstring": inspect.cleandoc("""
            The specified timeout time occurred before the operation could complete.
        """),
    },
    "xr.ValidationFailureError": {
        "docstring": inspect.cleandoc("""
            The function usage was invalid in some way.
        """),
    },
    "xr.ViewConfigurationTypeUnsupportedError": {
        "docstring": inspect.cleandoc("""
            The specified view configuration type is not supported by the runtime or platform.
        """),
    },
    "xr.XrException": {
        "docstring": inspect.cleandoc("""
            Base class for all OpenXR exceptions.
        """),
    },
}

__all__ = [
    "class_docstrings",
]
