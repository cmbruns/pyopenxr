import platform

from .layer_path import add_folder_to_api_layer_path, expose_packaged_api_layers

from .loader_interfaces import *
from .dynamic_api_layer_base import *
from . import loader_interfaces, dynamic_api_layer_base  # For __all__ handling

# Expose symbolic names for packaged api layers
LUNARG_api_dump_APILAYER_NAME = "XR_APILAYER_LUNARG_api_dump"
LUNARG_core_validation_APILAYER_NAME = "XR_APILAYER_LUNARG_core_validation"

# Automatically expose packaged API layers for supported platforms
if platform.system() in ["Windows", "Linux"]:
    expose_packaged_api_layers()


__all__ = [
    "expose_packaged_api_layers",
    "LUNARG_api_dump_APILAYER_NAME",
    "LUNARG_core_validation_APILAYER_NAME",
]
__all__ += loader_interfaces.__all__
__all__ += dynamic_api_layer_base.__all__
