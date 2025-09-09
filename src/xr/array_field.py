"""
file array_field.py

Helper functions for OpenXR-style ctypes Structures containing array fields
defined as (count, pointer) pairs. Supports automatic conversion from Python
sequences, single elements, or ctypes pointers, with optional encoding flavors.
"""

import enum
from ctypes import Array, c_char_p, cast, POINTER, pointer
from typing import TypeVar, Union, Sequence, Tuple, Optional


E = TypeVar("E")
ArrayFieldParamType = Union[
    None,
    POINTER,
    E,
    Array,
    Sequence[E],
]

BaseArrayFieldParamType = Union[
    None,
    POINTER,
    Array,
    Sequence,
]

StringArrayFieldParamType = Union[
    None,
    POINTER(c_char_p),
    c_char_p,
    Array,
    Sequence[str],
]


class ArrayFlavor(enum.Enum):
    ARRAY = 1
    STRING = 2
    BASE_HEADER = 3


def array_field_helper(
        element_type: type,
        count: Optional[int] = None,
        array: ArrayFieldParamType["element_type"] = None,
        flavor: ArrayFlavor = ArrayFlavor.ARRAY
) -> Tuple[int, POINTER]:
    """
    Helper function for pythonic interface to sequence fields.

    Accepts any Python sequence (not just lists) that supports `len()` and iteration.
    Handles conversion to ctypes arrays or pointers, depending on the specified flavor.

    :param element_type: The ctypes type of each element.
    :param count: Optional explicit count; inferred from array if not provided.
    :param array: A sequence, pointer, or single element to be normalized.
    :param flavor: Specifies how the array should be encoded (raw, string, header).
    :return: A tuple of (count, ctypes pointer to array).
    """
    # Default construction yields a null pointer and a zero length
    if array is None:
        count = 0
    # Construction from pointer usually requires an explicit length.
    # ...but default to 1 if length is not provided.
    elif isinstance(array, POINTER(element_type)):
        if count is None:
            count = 1
    elif isinstance(array, element_type):
        count = 1
        array = pointer(array)
    elif isinstance(array, Array):
        count = len(array)
    else:
        # Copy array into a ctypes array
        count = len(array)
        if flavor == ArrayFlavor.ARRAY:
            array = (element_type * count)(*array)  # noqa
        elif flavor == ArrayFlavor.STRING:
            array = (element_type * count)(*[s.encode() for s in array])  # noqa
        elif flavor == ArrayFlavor.BASE_HEADER:
            array = (element_type * count)(*[cast(p, element_type) for p in array])  # noqa
        else:
            raise NotImplementedError  # Is there a new flavor?
    array = cast(array, POINTER(element_type))
    return count, array


def base_array_field_helper(
        element_type: type,
        count: Optional[int] = None,
        array: BaseArrayFieldParamType = None,
) -> Tuple[int, POINTER]:
    """Helper function for pythonic interface to sequence fields"""
    return array_field_helper(element_type, count, array, flavor=ArrayFlavor.BASE_HEADER)


def string_array_field_helper(
        count: Optional[int] = None,
        array: StringArrayFieldParamType = None,
) -> Tuple[int, POINTER(c_char_p)]:
    """Helper function for pythonic interface to sequence fields"""
    return array_field_helper(c_char_p, count, array, flavor=ArrayFlavor.STRING)


__all__ = [
    "array_field_helper",
    "ArrayFieldParamType",
    "base_array_field_helper",
    "BaseArrayFieldParamType",
    "string_array_field_helper",
    "StringArrayFieldParamType",
]
