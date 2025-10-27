from ctypes import c_int, c_void_p, cast, pointer, Structure

import xr
from xr.field_helper import enum_field_helper


class SomeStruct(Structure):
    def __init__(self, type: xr.StructureType = xr.StructureType.UNKNOWN):
        super().__init__(
            _type=enum_field_helper(type),
        )

    @property
    def type(self) -> xr.StructureType:
        return xr.StructureType(self._type)

    @type.setter
    def type(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._type = enum_field_helper(value)

    _fields_ = [
        ("_type", c_int),
    ]


def test_field_next():
    # Default construct
    s = SomeStruct()
    assert s.type == xr.StructureType.UNKNOWN

    s = SomeStruct(type=xr.StructureType.API_LAYER_PROPERTIES)
    assert s.type == xr.StructureType.API_LAYER_PROPERTIES

    s.type = 3
    assert s.type == xr.StructureType.INSTANCE_CREATE_INFO

    # Set to None
    try:
        s.type = None  # set
        assert False
    except TypeError:
        pass


if __name__ == "__main__":
    test_field_next()
