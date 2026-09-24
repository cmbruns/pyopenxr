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


def _insert_layer(layer_name: str) -> bool:
    layers = os.environ.get("XR_ENABLE_API_LAYERS", default="").split(os.pathsep)
    if layer_name not in layers:
        layers.append(layer_name)
    layers = [x for x in layers if x != ""]
    os.environ["XR_ENABLE_API_LAYERS"] = os.pathsep.join(layers)
    return True


def activate_api_dump_layer(file_path: str, export_type: str = "text") -> bool:
    os.environ["XR_API_DUMP_FILE_NAME"] = file_path
    os.environ["XR_CORE_VALIDATION_EXPORT_TYPE"] = export_type  # Default to stdout reporting
    return _insert_layer(LUNARG_api_dump_APILAYER_NAME)


def activate_best_practices_validation_layer() -> bool:
    """
    Activate the best practices validation layer
    :return:
    """
    return _insert_layer(KHRONOS_best_practices_validation_APILAYER_NAME)


def activate_core_validation_layer() -> bool:
    """
    Activate the core validation layer
    :return:
    """
    os.environ["XR_CORE_VALIDATION_EXPORT_TYPE"] = "text"  # Default to stdout reporting
    return _insert_layer(LUNARG_core_validation_APILAYER_NAME)


__all__ = [
    "activate_best_practices_validation_layer",
    "activate_core_validation_layer",
    "expose_packaged_api_layers",
    "LUNARG_api_dump_APILAYER_NAME",
    "LUNARG_core_validation_APILAYER_NAME",
]
__all__ += loader_interfaces.__all__
__all__ += dynamic_api_layer_base.__all__
