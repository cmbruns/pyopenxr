import ctypes
import platform

from ..resources import resource_filename

if platform.system() == "Windows":
    library_path = resource_filename("xr.library.win32", "openxr_loader.dll")
elif platform.machine() == "x86_64":
    library_path = resource_filename("xr.library.x86_64", "openxr_loader.so")
elif platform.machine() == "aarch64":
    library_path = resource_filename("xr.library.aarch64", "openxr_loader.so")
else:
    print(f"platform.system() = '{platform.system()}'; platform.machine() = '{platform.machine()}'")
    raise NotImplementedError

openxr_loader_library = ctypes.cdll.LoadLibrary(library_path)

__all__ = [
    "openxr_loader_library",
]
