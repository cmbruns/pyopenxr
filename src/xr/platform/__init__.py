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
else:
    raise NotImplementedError
