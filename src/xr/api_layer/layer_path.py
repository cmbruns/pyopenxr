import os
import pkg_resources
import platform


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
    if platform.system() == "Windows":
        local_path = os.path.abspath(pkg_resources.resource_filename(__name__, "windows"))
    elif platform.system() == "Linux":
        local_path = os.path.abspath(pkg_resources.resource_filename(__name__, "linux"))
    else:
        raise NotImplementedError
    add_folder_to_api_layer_path(local_path)


def py_layer_library_path() -> str:
    """Path to a shared library file used for dynamic API layer dispatch."""
    if platform.system() == "Windows":
        package = "xr.api_layer.windows"
        name = "XrApiLayer_python.dll"
    elif platform.system() == "Linux":
        package = "xr.api_layer.linux"
        name = "libXrApiLayer_python.so"
    else:
        raise NotImplementedError
    path = pkg_resources.resource_filename(package, name)
    return path


__all__ = [
    "add_folder_to_api_layer_path",
    "expose_packaged_api_layers",
    "py_layer_library_path",
]
