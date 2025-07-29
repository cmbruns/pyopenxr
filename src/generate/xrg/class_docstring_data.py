import inspect


class Instance:
    """
    Opaque handle to an OpenXR instance object.

    An `xr.Instance` represents a connection between an OpenXR application and the
    OpenXR runtime. It encapsulates all runtime-managed state and serves as the root
    object for most OpenXR operations, including system queries, session creation,
    and extension dispatch.

    Instances are created via :func:`xr.create_instance`, and may be destroyed using
    :func:`xr.destroy_instance`. The runtime guarantees support for at least one
    instance per process, though multiple instances may be allowed depending on
    implementation.

    This object is opaque and cannot be directly inspected or modified. All interaction
    must occur through OpenXR API functions.

    :seealso: :func:`xr.create_instance`, :func:`xr.destroy_instance`, :class:`xr.InstanceCreateInfo`
    """


class_docstrings = {
    "xr.Instance": {
        "docstring": inspect.cleandoc("""
            Opaque handle to an OpenXR instance object.

            An `xr.Instance` represents a connection between an OpenXR application and the
            OpenXR runtime. It encapsulates all runtime-managed state and serves as the root
            object for most OpenXR operations, including system queries, session creation,
            and extension dispatch.

            Instances are created via :func:`xr.create_instance`, and may be destroyed using
            :func:`xr.destroy_instance`. The runtime guarantees support for at least one
            instance per process, though multiple instances may be allowed depending on
            implementation.

            This object is opaque and cannot be directly inspected or modified. All interaction
            must occur through OpenXR API functions.

            :seealso: :func:`xr.create_instance`, :func:`xr.destroy_instance`, :class:`xr.InstanceCreateInfo`
        """),
        "spec_url": "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrInstance.html"
    }
}
