import ctypes

from .library import openxr_loader_library
from . import cfunctions  # Side effect of defining low-level c signatures
from .constants import *
from .enums import *

XrStructureType = ctypes.c_int  # Well enum actually


class XrExtensionProperties(ctypes.Structure):
    _fields_ = [
        ("type", XrStructureType),
        ("next", ctypes.c_void_p),
        ("extension_name", ctypes.c_char * MAX_EXTENSION_NAME_SIZE),
        ("extension_version", ctypes.c_uint32),
    ]


# function transformations:
#  * snake_case_from_camel_case (for function name and parameter names)
#  * remove_xr_prefix
#  * ctypes_type_for_c_type
#  * pytype_for_c_type
#  * brief docstring
#  * parameter docstring
#  * exception docstring
#  * output_array_parameters
#  * check result
#  * string input parameter


def enumerate_instance_extension_properties(
    layer_name: str = None,
) -> ctypes.Array[XrExtensionProperties]:
    """
    Returns properties of available instance extensions

    :param layer_name: is either NULL or a pointer to a string naming the API layer to retrieve extensions from,
        as returned by xrEnumerateApiLayerProperties.
    :return: an array of XrExtensionProperties

    On failure, this command raises
        XR_ERROR_VALIDATION_FAILURE
        XR_ERROR_RUNTIME_FAILURE
        XR_ERROR_OUT_OF_MEMORY
        XR_ERROR_SIZE_INSUFFICIENT
        XR_ERROR_RUNTIME_UNAVAILABLE
        XR_ERROR_API_LAYER_NOT_PRESENT
    """
    # First call returns the item count
    if layer_name is not None:
        layer_name = layer_name.encode()

    extension_count = ctypes.c_uint32(0)
    fn = openxr_loader_library.xrEnumerateInstanceExtensionProperties
    result = fn(layer_name, 0, ctypes.byref(extension_count), None)
    # TODO: check results

    properties_type = XrExtensionProperties * extension_count.value
    properties = properties_type()

    # TODO: automatically initialize?
    for p in properties:
        p.type = StructureType.EXTENSION_PROPERTIES.value

    result2 = fn(
        layer_name,
        extension_count,
        ctypes.byref(extension_count),
        ctypes.byref(properties),
    )
    return properties


__all__ = [
    "enumerate_instance_extension_properties",
]
