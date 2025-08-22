import inspect

class_docstrings = {
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
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrInstance.html"
    }
}
