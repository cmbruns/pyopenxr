"""
`xr` is the top level module of the pyopenxr unofficial python bindings for the
OpenXR SDK to access VR and AR devices.
"""

from . import (
    version,
    constants,
    enums,
    typedefs,
    functions,
    custom_functions,
    platform,
    exception,
    classes,
    api_layer,
    context_object,
    opengl_graphics,
    matrix4x4f,
    extension,
)

from .version import *
from .constants import *
from .enums import *
from .typedefs import *
from .functions import *
from .custom_functions import *
from .platform import *
from .exception import *
from .classes import *
from .api_layer import *
from .context_object import *
from .opengl_graphics import *
from .matrix4x4f import *


# from .experiment import *

__all__ = [
    "extension",
]

for subpackage in (
    version,
    constants,
    enums,
    typedefs,
    functions,
    custom_functions,
    platform,
    exception,
    classes,
    api_layer,
    context_object,
    opengl_graphics,
    matrix4x4f,
):
    __all__ += subpackage.__all__

from .api_layer.steamvr_linux_destroyinstance_layer import SteamVrLinuxDestroyInstanceLayer
__all__ += "SteamVrLinuxDestroyInstanceLayer"

__version__ = version.PYOPENXR_VERSION  # Not in __all__, right?
