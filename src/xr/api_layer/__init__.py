import os
import platform

from .layer_path import add_folder_to_api_layer_path, expose_packaged_api_layers

from .loader_interfaces import *
from .dynamic_api_layer_base import *
from . import loader_interfaces, dynamic_api_layer_base  # For __all__ handling

# Expose symbolic names for packaged api layers
LUNARG_api_dump_APILAYER_NAME = "XR_APILAYER_LUNARG_api_dump"
LUNARG_core_validation_APILAYER_NAME = "XR_APILAYER_LUNARG_core_validation"
KHRONOS_best_practices_validation_APILAYER_NAME = "XR_APILAYER_KHRONOS_best_practices_validation"

# Automatically expose packaged API layers for supported platforms
if platform.system() in ["Windows"] or platform.machine() in ["aarch64", "x86_64"]:
    expose_packaged_api_layers()


def activate_best_practices_validation_layer() -> bool:
    """
    Activate the best practices validation layer
    :return:
    """
    layers = os.environ.get("XR_ENABLE_API_LAYERS", default="").split(os.pathsep)
    if KHRONOS_best_practices_validation_APILAYER_NAME not in layers:
        layers.append(KHRONOS_best_practices_validation_APILAYER_NAME)
    layers = [x for x in layers if x != ""]
    os.environ["XR_ENABLE_API_LAYERS"] = os.pathsep.join(layers)
    return True


def activate_core_validation_layer() -> bool:
    """
    Activate the core validation layer
    :return:
    """
    layers = os.environ.get("XR_ENABLE_API_LAYERS", default="").split(os.pathsep)
    if LUNARG_core_validation_APILAYER_NAME not in layers:
        layers.append(LUNARG_core_validation_APILAYER_NAME)
    layers = [x for x in layers if x != ""]
    os.environ["XR_ENABLE_API_LAYERS"] = os.pathsep.join(layers)
    os.environ["XR_CORE_VALIDATION_EXPORT_TYPE"] = "text"  # Default to stdout reporting
    return True


__all__ = [
    "activate_best_practices_validation_layer",
    "activate_core_validation_layer",
    "expose_packaged_api_layers",
    "LUNARG_api_dump_APILAYER_NAME",
    "LUNARG_core_validation_APILAYER_NAME",
]
__all__ += loader_interfaces.__all__
__all__ += dynamic_api_layer_base.__all__
