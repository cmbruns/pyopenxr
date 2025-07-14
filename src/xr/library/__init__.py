import ctypes
import platform

from ..resources import resource_filename

if platform.system() == "Windows":
    library_name = "openxr_loader.dll"
elif platform.system() == "Linux":
    library_name = "libopenxr_loader.so"
else:
    raise NotImplementedError

library_path = resource_filename("xr.library", library_name)
openxr_loader_library = ctypes.cdll.LoadLibrary(library_path)

__all__ = [
    "openxr_loader_library",
]
