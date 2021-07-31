import ctypes
import os

os.add_dll_directory(os.path.dirname(__file__))
openxr_loader_library = ctypes.cdll.LoadLibrary("openxr_loader")

__all__ = [
    "openxr_loader_library",
]
