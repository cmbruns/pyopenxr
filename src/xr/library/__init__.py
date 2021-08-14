import ctypes
import pkg_resources

library_name = "openxr_loader.dll"  # TODO: Mac and Linux
library_path = pkg_resources.resource_filename("xr.library", library_name)
openxr_loader_library = ctypes.cdll.LoadLibrary(library_path)

__all__ = [
    "openxr_loader_library",
]
