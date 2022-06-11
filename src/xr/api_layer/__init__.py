import os
import pkg_resources
import platform

# Expose symbolic names for packaged api layers
XR_APILAYER_LUNARG_api_dump_NAME = "XR_APILAYER_LUNARG_api_dump"
XR_APILAYER_LUNARG_core_validation_NAME = "XR_APILAYER_LUNARG_core_validation"


def expose_packaged_api_layers():
    """
    Make pre-packaged layers available to the openxr loader
    """
    if platform.system() == "Windows":
        local_path = os.path.abspath(pkg_resources.resource_filename(__name__, "windows"))
    else:
        raise NotImplementedError
    starting_api_path = os.getenv("XR_API_LAYER_PATH")
    if starting_api_path is None or len(starting_api_path) < 1:
        os.environ["XR_API_LAYER_PATH"] = local_path
    elif local_path in starting_api_path:
        pass  # It's already there
    else:
        # pro-tip: os.pathsep is very different from os.path.sep
        os.environ["XR_API_LAYER_PATH"] += f"{os.pathsep}{local_path}"


# Automatically expose packaged API layers for supported platforms
if platform.system() in ["Windows", ]:
    expose_packaged_api_layers()


__all__ = [
    "expose_packaged_api_layers",
]
