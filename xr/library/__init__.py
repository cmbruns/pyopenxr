import ctypes
import os

# TODO: loader submodule
os.add_dll_directory(os.path.dirname(__file__))
openxr_loader_library = ctypes.cdll.LoadLibrary("openxr_loader.dll")
print(openxr_loader_library)

__all__ = [
    "openxr_loader_library",
]