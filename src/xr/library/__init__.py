import ctypes
import pkg_resources
import platform

library_name = "openxr_loader.dll"  # TODO: Mac
if platform.system() == "Linux":
    library_name = "libopenxr_loader.so"
library_path = pkg_resources.resource_filename("xr.library", library_name)
openxr_loader_library = ctypes.cdll.LoadLibrary(library_path)

__all__ = [
    "openxr_loader_library",
]
