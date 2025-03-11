from ctypes import byref, c_void_p, cast, pointer
from typing import Tuple

from . import raw_functions
from .exception import check_result
from .typedefs import *


def locate_space_with_velocity(
    space: Space,
    base_space: Space,
    time: Time,
) -> Tuple[SpaceLocation, SpaceVelocity]:
    """"""
    velocity = SpaceVelocity()
    location = SpaceLocation(
        next=cast(pointer(velocity), c_void_p)
    )
    fxn = raw_functions.xrLocateSpace
    result = check_result(
        fxn(
            space,
            base_space,
            time,
            byref(location),
        )
    )
    if result.is_exception():
        raise result
    return location, velocity


__all__ = [
    "locate_space_with_velocity",
]
