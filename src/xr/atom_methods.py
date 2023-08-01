"""
This module injects instance methods into OpenXR atom types (e.g. xr.Instance etc.)
These methods are injected late, at function definition time, due to
complex definition order dependencies.

# Certain pythonic
# method implementations are injected here, long after the initial
# class declarations.
"""

from ctypes import byref
from typing import Optional, Union

from .exception import check_result
from . import raw_functions
from .typedefs import *


class instance_method_of:
    """
    Decorator class to help inject new instance methods into an already defined class.
    https://stackoverflow.com/q/61956610/146574
    """
    def __init__(self, cls, name=None):
        self.cls = cls
        self.name = name

    def __call__(self, func):
        if self.name is not None:
            func.__name__ = self.name
        func.__qualname__ = f"{self.cls.__qualname__}.{func.__name__}"
        func.__module__ = self.cls.__module__
        setattr(self.cls, func.__name__, func)
        return func


def inject_atom_methods():
    ############
    # Instance #
    ############

    @instance_method_of(Instance)
    def __init__(self: Instance, create_info: Optional[InstanceCreateInfo] = InstanceCreateInfo()) -> None:
        """
        Call Instance(None) to construct an uninitialized Instance.
        """
        # super().__init__()  # Triggers a problem in ctypes "RuntimeError: super(): __class__ cell not found"
        if create_info is None:
            return
        result = check_result(raw_functions.xrCreateInstance(
            create_info,
            byref(self),
        ))
        if result.is_exception():
            raise result

    @instance_method_of(Instance)
    def __enter__(self: Instance) -> Instance:
        return self

    @instance_method_of(Instance)
    def __exit__(self, _exc_type, _exc_val, _exc_tb) -> None:
        result = check_result(raw_functions.xrDestroyInstance(self))
        if result.is_exception():
            raise result

    ############
    # SystemId #
    ############
    # (SystemId is not actually an atom)

    @instance_method_of(SystemId)
    def __init__(self, instance: Optional[Instance], get_info: SystemGetInfo = SystemGetInfo()) -> None:
        # super().__init__()
        self.instance = instance
        if instance is None:
            return
        result = check_result(raw_functions.xrGetSystem(
            instance,
            get_info,
            byref(self),
        ))
        if result.is_exception():
            raise result

    @instance_method_of(SystemId)
    def __enter__(self):
        return self

    @instance_method_of(SystemId)
    def __exit__(self, _exc_type, _exc_val, _exc_tb):
        self.instance = None

    ###########
    # Session #
    ###########

    @instance_method_of(Session)
    def __init__(self, instance: Optional[Instance], create_info: "SessionCreateInfo" = None) -> None:
        # super().__init__()
        self.instance = instance
        if instance is None:
            return
        result = check_result(raw_functions.xrCreateSession(
            instance,
            create_info,
            byref(self),
        ))
        if result.is_exception():
            raise result

    @instance_method_of(Session)
    def __enter__(self):
        return self

    @instance_method_of(Session)
    def __exit__(self, _exc_type, _exc_val, _exc_tb):
        result = check_result(raw_functions.xrDestroySession(self))
        if result.is_exception():
            raise result
        self.instance = None

    #########
    # Space #
    #########

    @instance_method_of(Space)
    def __init__(self, session: Optional[Session],
                 create_info: Union[ReferenceSpaceCreateInfo, ActionSpaceCreateInfo] = None
                 ) -> None:
        # super().__init__()
        self.session = session
        if session is None:
            return
        result = None
        if isinstance(create_info, ReferenceSpaceCreateInfo):
            result = check_result(raw_functions.xrCreateReferenceSpace(
                session,
                create_info,
                byref(self),
            ))
        elif isinstance(create_info, ActionSpaceCreateInfo):
            result = check_result(raw_functions.xrCreateActionSpace(
                session,
                create_info,
                byref(self),
            ))
        else:
            raise NotImplementedError
        if result.is_exception():
            raise result

    @instance_method_of(Space)
    def __enter__(self):
        return self

    @instance_method_of(Space)
    def __exit__(self, _exc_type, _exc_val, _exc_tb):
        result = check_result(raw_functions.xrDestroySpace(self))
        if result.is_exception():
            raise result
        self.session = None

    ##########
    # Action #
    ##########

    @instance_method_of(Action)
    def __init__(self, action_set: Optional[ActionSet], create_info: "ActionCreateInfo" = None) -> None:
        # super().__init__()
        self.action_set = action_set
        if action_set is None:
            return
        result = check_result(raw_functions.xrCreateAction(
            action_set,
            create_info,
            byref(self),
        ))
        if result.is_exception():
            raise result

    @instance_method_of(Action)
    def __enter__(self):
        return self

    @instance_method_of(Action)
    def __exit__(self, _exc_type, _exc_val, _exc_tb):
        result = check_result(raw_functions.xrDestroyAction(self))
        if result.is_exception():
            raise result
        self.action_set = None

    #############
    # ActionSet #
    #############

    @instance_method_of(ActionSet)
    def __init__(self, instance: Optional[Instance], create_info: "ActionSetCreateInfo" = None) -> None:
        # super().__init__()
        self.instance = instance
        if instance is None:
            return
        result = check_result(raw_functions.xrCreateActionSet(
            instance,
            create_info,
            byref(self),
        ))
        if result.is_exception():
            raise result

    @instance_method_of(ActionSet)
    def __enter__(self):
        return self

    @instance_method_of(ActionSet)
    def __exit__(self, _exc_type, _exc_val, _exc_tb):
        result = check_result(raw_functions.xrDestroyActionSet(self))
        if result.is_exception():
            raise result
        self.instance = None

    #############
    # Swapchain #
    #############

    @instance_method_of(Swapchain)
    def __init__(self, session: Optional[Session], create_info: "SwapchainCreateInfo" = None) -> None:
        # super().__init__()
        self.session = session
        if session is None:
            return
        result = check_result(raw_functions.xrCreateSwapchain(
            session,
            create_info,
            byref(self),
        ))
        if result.is_exception():
            raise result

    @instance_method_of(Swapchain)
    def __enter__(self):
        return self

    @instance_method_of(Swapchain)
    def __exit__(self, _exc_type, _exc_val, _exc_tb):
        result = check_result(raw_functions.xrDestroySwapchain(self))
        if result.is_exception():
            raise result
        self.session = None


__all__ = [
    "inject_atom_methods"
]
