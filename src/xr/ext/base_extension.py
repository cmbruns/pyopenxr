from ctypes import cast

import xr


class BaseExtension:
    def __init__(self, instance):
        self.instance = instance

    def _call_raw(self, name: str, *args, **kwargs) -> None:
        """Instantiate an extension function; call it; and check the result"""
        pfn = cast(
            xr.get_instance_proc_addr(self.instance, name),
            getattr(xr, f"PFN_{name}")
        )
        result = pfn(*args, **kwargs)
        checked = xr.check_result(xr.Result(result))
        if checked.is_exception():
            raise checked
