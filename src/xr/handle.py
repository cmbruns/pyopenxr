import ctypes
from ctypes import c_void_p, cast, POINTER, Structure


class HandleMixin:
    """
    Mixin class for pyopenxr Handle classes.

    :see: https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#fundamentals-handles
    """

    def __enter__(self):
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

    def __repr__(self):
        return f"<xr.{self.__class__.__name__} handle at {cast(self, ctypes.c_void_p).value:#x}>"

    @property
    def instance(self):
        if self.__class__.__name__ == "Instance":
            return self
        try:
            return self._instance
        except AttributeError:
            return None

    @instance.setter
    def instance(self, instance: "xr.Instance"):
        self._instance = instance

__all__ = [
    "HandleMixin",
]
