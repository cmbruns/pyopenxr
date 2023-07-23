from ctypes import byref

from .exception import check_result
from . import raw_functions
from .typedefs import *


class _InstanceImplementation(Instance):
    """
    Implementation of context manager methods for Instance class.
    """
    def __init__(self, create_info: InstanceCreateInfo = InstanceCreateInfo()) -> None:
        result = check_result(raw_functions.xrCreateInstance(
            create_info,
            byref(self),
        ))
        if result.is_exception():
            raise result

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        result = check_result(raw_functions.xrDestroyInstance(self))
        if result.is_exception():
            raise result


# Add context manager methods to Instance class
Instance.__init__ = _InstanceImplementation.__init__
Instance.__enter__ = _InstanceImplementation.__enter__
Instance.__exit__ = _InstanceImplementation.__exit__


class _SystemIdImplementation(SystemId):
    def __init__(self, instance: Instance, get_info: SystemGetInfo = SystemGetInfo()) -> None:
        result = check_result(raw_functions.xrGetSystem(
            instance,
            get_info,
            byref(self),
        ))
        if result.is_exception():
            raise result

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


SystemId.__init__ = _SystemIdImplementation.__init__
SystemId.__enter__ = _SystemIdImplementation.__enter__
SystemId.__exit__ = _SystemIdImplementation.__exit__


class _SessionImplementation(Session):
    def __init__(self, instance: Instance, create_info: "SessionCreateInfo" = None) -> None:
        result = check_result(raw_functions.xrCreateSession(
            instance,
            create_info,
            byref(self),
        ))
        if result.is_exception():
            raise result

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        result = check_result(raw_functions.xrDestroySession(self))
        if result.is_exception():
            raise result


Session.__init__ = _SessionImplementation.__init__
Session.__enter__ = _SessionImplementation.__enter__
Session.__exit__ = _SessionImplementation.__exit__


__all__ = []  # side effects only...
