"""
Internal module: xr.base_structs

Provides passthrough base classes to support type inference in struct fields and function parameters.
Avoids direct inheritance from platform-specific XrFooBaseHeader classes and sidesteps upfront Union bookkeeping.

Intended for internal use in type annotations and dynamic dispatch.
"""

__all__ = [
    "BaseLoaderInitInfo"
]

from ctypes import Structure


class BaseLoaderInitInfo(Structure):
    """
    Passthrough base class for:
        LoaderInitInfoBaseHeaderKHR
        LoaderInitInfoAndroidKHR
        LoaderInitInfoPropertiesEXT

    Used for type inference and dispatch without declaring fields.
    """
    _fields_ = []  # Explicitly empty to signal passthrough intent
