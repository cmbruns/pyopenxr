import ctypes
import platform

from ..resources import resource_filename


def platform_folder() -> tuple[str, str]:
    if platform.system() == "Windows":
        return "win32", "dll"
    if platform.machine() == "x86_64":
        return "x86_64", "so"
    elif platform.machine() == "aarch64":
        return "aarch64", "so"
    else:
        print(f"platform.system() = '{platform.system()}'; platform.machine() = '{platform.machine()}'")
        raise NotImplementedError


folder, suffix = platform_folder()
library_path = resource_filename(f"xr.library.{folder}", f"openxr_loader.{suffix}")
openxr_loader_library = ctypes.cdll.LoadLibrary(library_path)

__all__ = [
    "openxr_loader_library",
]
