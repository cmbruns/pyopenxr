from . import version, constants, enums, typedefs, functions, platform, exception, api_layer

from .version import *
from .constants import *
from .enums import *
from .typedefs import *
from .functions import *
from .platform import *
from .exception import *
from .classes import *
from .api_layer import *
from .context_object import *

# Use submodule name for extension
import xr.extension as extension

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
    platform,
    exception,
    classes,
    api_layer,
    context_object,
):
    __all__ += subpackage.__all__

from .api_layer.steamvr_linux_destroyinstance_layer import SteamVrLinuxDestroyInstanceLayer
__all__ += "SteamVrLinuxDestroyInstanceLayer"

__version__ = version.PYOPENXR_VERSION  # Not in __all__, right?
