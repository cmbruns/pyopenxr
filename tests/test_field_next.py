from ctypes import c_void_p, cast, pointer, Structure

from xr.field_helper import next_field_helper


class SomeStruct(Structure):
    def __init__(self, next=None):
        super().__init__(
            _next=next_field_helper(next),
        )

    @property
    def next(self) -> c_void_p:
        return self._next

    @next.setter
    def next(self, value) -> None:
        # noinspection PyAttributeOutsideInit
        self._next = next_field_helper(value)

    _fields_ = [
        ("_next", c_void_p),
    ]


def test_field_next():
    # Default construct
    s = SomeStruct()
    assert s.next is None

    # Set to None
    s.next = None  # set
    assert s.next is None
    s = SomeStruct(next=None)  # constructor
    assert s.next is None
    s.next = None  # setter

    # Set to c_void_p()
    s = SomeStruct(next=c_void_p())  # constructor
    assert s.next is None
    s.next = c_void_p()  # setter
    assert s.next is None

    # Set to cast pointer; traditional usual value
    s2 = SomeStruct()
    ps2 = cast(pointer(s2), c_void_p)
    s = SomeStruct(next=ps2)  # constructor
    assert s.next is not None
    s.next = None
    assert s.next is None
    s.next = ps2  # setter
    assert s.next is not None

    # Set to struct; this is the case we want the helper to help
    s.next = None
    assert s.next is None
    s = SomeStruct(next=s2)  # Constructor
    assert s.next is not None
    s.next = None
    assert s.next is None
    s.next = s2  # setter
    assert s.next is not None

    # Set to pointer to struct, but not cast yet
    s = SomeStruct(next=pointer(s2))
    assert s.next is not None
    s.next = None
    assert s.next is None
    s.next = pointer(s2)  # setter
    assert s.next is not None

    # Set to value that should not work
    try:
        s = SomeStruct(next="foo")
        assert False
    except TypeError:
        pass
    try:
        s.next = "foo"
        assert False
    except TypeError:
        pass

    s.next = 5


if __name__ == "__main__":
    test_field_next()
