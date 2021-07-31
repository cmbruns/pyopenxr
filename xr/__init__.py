from . import version, constants, functions

from .version import *
from .constants import *
from .functions import *

__all__ = []
for subpackage in version, constants, functions:
    __all__ += subpackage.__all__

__version__ = version.PYOPENXR_VERSION  # Not in __all__, right?
