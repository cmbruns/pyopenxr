import ctypes
import platform

from ..resources import resource_filename

if platform.system() == "Windows":
    library_name = "openxr_loader.dll"
elif platform.system() == "Linux" or platform.system() == "Android":
    library_name = "libopenxr_loader.so"
else:
    print(f"platform.system() = '{platform.system()}'")
    raise NotImplementedError

if platform.system() == "Android":
    library_path = library_name  # Library should have been pre-loaded on android
else:
    library_path = resource_filename("xr.library", library_name)

openxr_loader_library = ctypes.cdll.LoadLibrary(library_path)

__all__ = [
    "openxr_loader_library",
]
