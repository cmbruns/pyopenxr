"""
file array_field.py

Helper functions for Structures containing arrays specified as length/pointer pairs.
"""
import ctypes
from ctypes import POINTER
from typing import TypeVar, Union, Sequence, Optional


E = TypeVar("E")
ArrayFieldParamType = Union[
    None,
    ctypes.POINTER,
    E,
    ctypes.Array,
    Sequence[E],
]


def array_field_helper(
        element_type: type,
        count: Optional[int] = None,
        array: ArrayFieldParamType["element_type"] = None,
) -> (int, ctypes.POINTER):
    """Helper function for pythonic interface to sequence fields"""
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
        array = ctypes.pointer(array)
    elif isinstance(array, ctypes.Array):
        count = len(array)
    else:
        # Copy array into a ctypes array
        count = len(array)
        array = (element_type * count)(*array)
    return count, array


__all__ = [
    "array_field_helper",
    "ArrayFieldParamType"
]
