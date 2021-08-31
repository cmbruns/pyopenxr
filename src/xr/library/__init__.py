import ctypes
import pkg_resources
import platform

if platform.system() == "Windows":
    library_name = "openxr_loader.dll"
elif platform.system() == "Linux":
    library_name = "libopenxr_loader.so"
else:
    raise NotImplementedError

library_path = pkg_resources.resource_filename("xr.library", library_name)
openxr_loader_library = ctypes.cdll.LoadLibrary(library_path)

__all__ = [
    "openxr_loader_library",
]
