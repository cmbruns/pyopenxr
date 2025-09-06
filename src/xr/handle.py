import ctypes
from ctypes import c_void_p, cast, Structure


def xr_handle(pointee: Structure):
    """
    Decorator for pyopenxr Handle classes.

    :see: https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-handles
    """
    def wrapper(cls):
        def __init__(self):
            # self.instance to be later set in an xr.create_<handle>() function
            self.instance = None

        def __enter__(self) -> cls.__class__:
            return self

        def __eq__(self, other) -> bool:
            sv = cast(self, c_void_p).value
            if other is None and sv is None:
                return True
            try:
                ov = cast(other, c_void_p).value
                return sv == ov
            except ctypes.ArgumentError:
                return super().__eq__(other)

        def __exit__(self, _exc_type, _exc_val, _exc_tb) -> None:
            if not self:
                return
            if not self.instance:
                return
            import xr  # Just-in-time to avoid initialization order problems
            destroy_name = f"xrDestroy{self.__class__.__name__}"
            destroy_fn_type = getattr(xr, f"PFN_{destroy_name}")
            destroy_fn = cast(
                xr.get_instance_proc_addr(self.instance, destroy_name),
                destroy_fn_type,
            )
            result = destroy_fn(self)
            checked = xr.check_result(xr.Result(result))
            if checked.is_exception():
                raise checked
            self.instance = None
            cast(self, c_void_p).value = None
            assert not self

        def __repr__(self):
            return f"<xr.{self.__class__.__name__} handle at {ctypes.cast(self, ctypes.c_void_p).value:#x}>"

        cls._type_ = pointee
        cls.__init__ = __init__
        cls.__enter__ = __enter__
        cls.__eq__ = __eq__
        cls.__exit__ = __exit__
        cls.__repr__ = __repr__
    return wrapper


__all__ = [
    "xr_handle",
]
