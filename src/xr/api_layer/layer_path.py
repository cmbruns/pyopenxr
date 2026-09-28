import os
import platform

from ..resources import resource_filename
from ..platform_folder import platform_folder


def add_folder_to_api_layer_path(folder_name: str):
    starting_api_path = os.getenv("XR_API_LAYER_PATH")
    if starting_api_path is None or len(starting_api_path) < 1:
        os.environ["XR_API_LAYER_PATH"] = folder_name
    elif folder_name in starting_api_path.split(os.pathsep):
        pass  # It's already there
    else:
        # pro-tip: os.pathsep is very different from os.path.sep
        os.environ["XR_API_LAYER_PATH"] += f"{os.pathsep}{folder_name}"


def expose_packaged_api_layers():
    """
    Make pre-packaged layers available to the openxr loader
    """
    arch, _suffix = platform_folder()
    local_path = os.path.abspath(resource_filename("xr.api_layer", arch))
    add_folder_to_api_layer_path(local_path)


def py_layer_library_path() -> str:
    """Path to a shared library file used for dynamic API layer dispatch."""
    arch, suffix = platform_folder()
    package = f"xr.api_layer.{arch}"
    name = f"XrApiLayer_python.{suffix}"
    if not arch.lower().startswith("win"):
        name = f"lib{name}"  # e.g. libXrApiLayer_python.so
    path = resource_filename(package, name)
    return path


__all__ = [
    "add_folder_to_api_layer_path",
    "expose_packaged_api_layers",
    "py_layer_library_path",
]
