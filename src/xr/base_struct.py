__all__ = [
    "BaseXrStructure"
]

from ctypes import c_void_p, Structure
from .enums import StructureType
from .field_helper import enum_field_helper, FieldNextType, next_field_helper


class BaseXrStructure(Structure):
    """
    Base class for PyOpenXR Structures
    """

    def __repr__(self) -> str:
        return f"xr.{self.__class__.__name__}(type={repr(self.type)}, next={repr(self.next)})"

    def __str__(self) -> str:
        return f"xr.{self.__class__.__name__}(type={self.type}, next={self.next})"

    @property
    def next(self) -> c_void_p:
        """Pointer to the next structure in a pNext chain."""
        return self._next

    @next.setter
    def next(self, value: FieldNextType) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    @property
    def type(self) -> StructureType:
        return StructureType(self._type)

    @type.setter
    def type(self, value: StructureType) -> None:
        # noinspection PyAttributeOutsideInit
        self._type = enum_field_helper(value)

    _fields_ = [
        ("_type", StructureType.ctype()),
        ("_next", c_void_p),
    ]
