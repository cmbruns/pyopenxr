import platform

__all__ = []

if platform.system() == "Windows":
    from .windows import *
    from . import windows
    __all__ += windows.__all__
elif platform.system() == "Linux":
    from .linux import *
    from . import linux
    __all__ += linux.__all__
elif platform.system() == "Android":
    from .android import *
    from . import android
    __all__ += android.__all__
else:
    raise NotImplementedError
