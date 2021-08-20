import platform

__all__ = []

if platform.system() == "Windows":
    from .windows import *
    from . import windows
    __all__ += windows.__all__
# TODO: Linux, Mac, Android?
