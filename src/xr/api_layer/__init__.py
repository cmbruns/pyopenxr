import platform

from .layer_path import add_folder_to_api_layer_path, expose_packaged_api_layers

from .loader_interfaces import *
from .py_layer_base import *
from . import loader_interfaces, py_layer_base  # For __all__ handling

# Expose symbolic names for packaged api layers
XR_APILAYER_LUNARG_api_dump_NAME = "XR_APILAYER_LUNARG_api_dump"
XR_APILAYER_LUNARG_core_validation_NAME = "XR_APILAYER_LUNARG_core_validation"

# Automatically expose packaged API layers for supported platforms
if platform.system() in ["Windows", ]:
    expose_packaged_api_layers()


__all__ = [
]
__all__ += loader_interfaces.__all__
__all__ += py_layer_base.__all__
