"""
xr.ext.base_extension — Base class for Pythonic OpenXR extensions

This module defines the BaseExtension class, which provides common utilities
for resolving and invoking OpenXR instance-bound functions in extension
implementations. It centralizes boilerplate around function lookup,
casting, and result checking, speeding manual development while retaining
the option to inline calls later for simpler tracebacks.
"""

from ctypes import cast

import xr


class BaseExtension:
    """
    Base class for Pythonic OpenXR extension implementations.

    Provides a helper for calling extension entry points obtained via
    :func:`xr.get_instance_proc_addr`, casting them to the correct
    function-pointer type, invoking with the supplied arguments, and
    checking the :class:`xr.Result`.

    :param instance: The OpenXR instance to which this extension is bound.
    :type instance: xr.Instance
    """

    def __init__(self, instance):
        self.instance = instance

    def _call_raw(self, name: str, *args, **kwargs) -> None:
        """
        Resolve, invoke, and check an OpenXR entry-point function.

        This helper performs three steps:

        1. Queries the raw function pointer for the given `name` via
           :func:`xr.get_instance_proc_addr`.
        2. Casts the pointer to the matching PFN type (e.g.
           :class:`xr.PFN_xrCreateDebugUtilsMessengerEXT`).
        3. Calls the function with `*args` and `**kwargs`, then checks the
           returned :class:`xr.Result`, raising its corresponding exception
           on error.

        :param name: Name of the OpenXR function to call
                     (e.g. ``"xrCreateDebugUtilsMessengerEXT"``).
        :type name: str
        :param args: Positional arguments to pass into the OpenXR function.
        :param kwargs: Keyword arguments to pass into the OpenXR function.
        :raises xr.Error: If the OpenXR call returns an error code.
        """

        # Lookup and cast the raw function pointer
        pfn_type = getattr(xr, f"PFN_{name}")
        pfn = cast(
            xr.get_instance_proc_addr(self.instance, name),
            pfn_type
        )

        # Invoke the function and retrieve the raw integer result
        result_code = pfn(*args, **kwargs)

        # Convert to xr.Result, check for errors, and raise on failure
        checked = xr.check_result(xr.Result(result_code))
        if checked.is_exception():
            raise checked


__all__ = [
    "BaseExtension",
]
