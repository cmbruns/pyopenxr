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
    api_layer,
    extension,
)
from .utils import classes, context_object, matrix4x4f, opengl_graphics

from .version import *
from .constants import *
from .enums import *
from .typedefs import *
from .functions import *
from .custom_functions import *
from .platform import *
from .exception import *
from xr.utils.classes import *
from .api_layer import *
from xr.utils.context_object import *
from xr.utils.opengl_graphics import *
from xr.utils.matrix4x4f import *


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
    api_layer,
):
    __all__ += subpackage.__all__

__version__ = version.PYOPENXR_VERSION  # Not in __all__, right?
