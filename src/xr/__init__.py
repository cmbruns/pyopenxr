"""
`xr` is the root module of pyopenxr, an unofficial Python binding for the OpenXR SDK.

It provides low-level access to the core OpenXR API for interacting with VR and AR runtimes,
including system queries, session management, and extension dispatch. This module wraps the
standard C interface in a Pythonic structure while preserving fidelity to the original spec.

For high-level utilities and ergonomic abstractions, see submodules and helper packages.
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
)

from .version import *
from .constants import *
from .enums import *
from .typedefs import *
from .functions import *
from .custom_functions import *
from .platform import *
from .exception import *
from .api_layer import *


__all__ = [
]

for subpackage in (
    version,
    constants,
    enums,
    typedefs,
    functions,
    custom_functions,
    platform,
    api_layer,
):
    __all__ += subpackage.__all__

__version__ = version.PYOPENXR_VERSION  # Not in __all__, right?
