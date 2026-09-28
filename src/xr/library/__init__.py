import ctypes

from ..resources import resource_filename
from ..platform_folder import platform_folder


folder, suffix = platform_folder()
library_path = resource_filename(f"xr.library.{folder}", f"openxr_loader.{suffix}")
openxr_loader_library = ctypes.cdll.LoadLibrary(library_path)

__all__ = [
    "openxr_loader_library",
]
