import ctypes

from . import raw_functions  # Side effect of defining low-level c signatures
from .enums import *
from .typedefs import *


# function transformations:
#  * brief docstring
#  * parameter docstring
#  * exception docstring
#  * output_array_parameters
#  * check result
#  * string input parameter


def enumerate_instance_extension_properties(
    layer_name: str = None,
) -> ctypes.Array[ExtensionProperties]:
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
    fn = raw_functions.xrEnumerateInstanceExtensionProperties
    result = fn(layer_name, 0, ctypes.byref(extension_count), None)
    # TODO: check results

    properties_type = ExtensionProperties * extension_count.value
    properties = properties_type()

    # TODO: automatically initialize?
    for p in properties:
        p.type = StructureType.EXTENSION_PROPERTIES.value

    result2 = fn(
        layer_name,
        extension_count,
        ctypes.byref(extension_count),
        properties,  # Don't use byref for arrays...
    )
    return properties


__all__ = [
    "enumerate_instance_extension_properties",
]
