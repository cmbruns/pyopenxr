import os
import pkg_resources
import platform

# Expose symbolic names for packaged api layers
from .layer_path import add_folder_to_api_layer_path

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
    add_folder_to_api_layer_path(local_path)


# Automatically expose packaged API layers for supported platforms
if platform.system() in ["Windows", ]:
    expose_packaged_api_layers()


__all__ = [
    "expose_packaged_api_layers",
]
