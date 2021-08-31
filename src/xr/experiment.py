from ctypes import Array, byref, c_char, c_int, c_uint32, c_void_p, Structure
import ctypes

from . import raw_functions  # Side effect of defining low-level c signatures
from .enums import *
from .exception import check_result
from .typedefs import *


class ExtensionProperties(Structure):
    _fields_ = [
        ("type", c_int),  #  StructureType),
        ("next", c_void_p),
        ("extension_name", (c_char * 128)),
        ("extension_version", c_uint32),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(
            StructureType.EXTENSION_PROPERTIES.value,
            None,
            *args, **kwargs,
        )

    def __bytes__(self):
        return self.extension_name

    def __eq__(self, other):
        try:
            if other.type != self.type:
                return False
            if other.extension_version != self.extension_version:
                return False
        except AttributeError as exc:
            pass  # That's OK, objects without those attributes can use string comparison
        return str(other) == str(self)

    def __str__(self):
        return self.extension_name.decode()

    @classmethod
    def make_array(cls, element_count: int):
        result = (cls * element_count)()
        for element in result:
            element.type = StructureType.EXTENSION_PROPERTIES.value
        return result


if False:
    raw_functions.xrEnumerateInstanceExtensionProperties.argtypes = [
        ctypes.c_char_p,  # layer_name
        c_uint32,  # property_capacity_input
        ctypes.POINTER(c_uint32),  # property_count_output
        ctypes.POINTER(ExtensionProperties),  # properties
    ]


# function transformations:
#  * brief docstring
#  * parameter docstring
#  * exception docstring
#  * output_array_parameters
#  * check result
#  * string input parameter


def enumerate_instance_extension_properties(
    layer_name: str = None,
) -> Array[ExtensionProperties]:
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

    extension_count = c_uint32(0)
    fn = raw_functions.xrEnumerateInstanceExtensionProperties
    result = check_result(fn(layer_name, 0, byref(extension_count), None))
    if result.is_exception():
        raise result

    properties = ExtensionProperties.make_array(extension_count.value)

    # TODO: automatically initialize?
    # for p in properties:
    #     p.type = StructureType.EXTENSION_PROPERTIES.value

    result = check_result(
        fn(
            layer_name,
            extension_count,
            byref(extension_count),
            properties,  # Don't use byref for arrays...
        )
    )
    if result.is_exception():
        raise result

    return properties


__all__ = [
    # "enumerate_instance_extension_properties",
    # "ExtensionProperties",
]
