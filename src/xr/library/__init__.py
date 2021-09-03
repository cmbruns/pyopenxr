import atexit
from contextlib import ExitStack
import ctypes
import importlib.resources
import platform

if platform.system() == "Windows":
    library_name = "openxr_loader.dll"
elif platform.system() == "Linux":
    library_name = "libopenxr_loader.so"
else:
    raise NotImplementedError

lib_manager = ExitStack()
atexit.register(lib_manager.close)
lib_ref = importlib.resources.files("xr.library") / library_name
library_path = lib_manager.enter_context(importlib.resources.as_file(lib_ref))
openxr_loader_library = ctypes.cdll.LoadLibrary(str(library_path))

__all__ = [
    "openxr_loader_library",
]
