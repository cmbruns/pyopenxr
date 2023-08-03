# Warning: this file is automatically generated. Do not edit.

# pyopenxr version is based on openxr version...
# except the patch number is:
#   100 * openxr patch number + pyopenxr patch number
import functools

XR_VERSION_MAJOR = 1
XR_VERSION_MINOR = 0
XR_VERSION_PATCH = 28
XR_CURRENT_API_VERSION_STRING = "1.0.28"

PYOPENXR_VERSION_MAJOR = 1
PYOPENXR_VERSION_MINOR = 0
PYOPENXR_VERSION_PATCH = 2802
PYOPENXR_VERSION_PATCH_INCREMENTAL = 2
PYOPENXR_VERSION_SUFFIX = ""
PYOPENXR_VERSION = "1.0.2802"


@functools.total_ordering
class Version(object):
    def __init__(self, major: int = 0, minor: int = None, patch: int = None):
        if minor is None and patch is None:
            if hasattr(major, "number"):  # Copy constructor
                major = major.number()
            if major > 0xffff:
                # major argument is actually a packed xr.VersionNumber
                patch = major & 0xffffffff
                minor = (major >> 32) & 0xffff
                major = (major >> 48) & 0xffff
        if minor is None:
            minor = 0
        if patch is None:
            patch = 0
        self.major = major
        self.minor = minor
        self.patch = patch

    def __eq__(self, other):
        return int(self) == int(other)

    def __index__(self) -> int:
        """Packed xr.VersionNumber"""
        return (((int(self.major) & 0xffff) << 48) 
                | ((int(self.minor) & 0xffff) << 32) 
                | (int(self.patch) & 0xffffffff))

    def __int__(self) -> int:
        return self.__index__()

    def __lt__(self, other):
        return int(self) < int(other)

    def number(self) -> int:
        """Packed xr.VersionNumber"""
        return self.__index__()

    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"


def pack_32_bit_version(major: int, minor: int, patch: int) -> int:
    if not 0 <= major < 2**8:
        raise RuntimeError("major version out of range")
    if not 0 <= minor < 2**8:
        raise RuntimeError("minor version out of range")
    if not 0 <= patch < 2**16:
        raise RuntimeError("patch version out of range")
    return (((int(major) & 0xff) << 24)
            | ((int(minor) & 0xff) << 16)
            | (int(patch) & 0xffff))


XR_CURRENT_API_VERSION = Version(XR_VERSION_MAJOR, XR_VERSION_MINOR, XR_VERSION_PATCH)
PYOPENXR_CURRENT_API_VERSION = pack_32_bit_version(
    PYOPENXR_VERSION_MAJOR,
    PYOPENXR_VERSION_MINOR,
    PYOPENXR_VERSION_PATCH
)


__version__ = PYOPENXR_VERSION

__all__ = [
    "PYOPENXR_CURRENT_API_VERSION",
    "PYOPENXR_VERSION_MAJOR",
    "PYOPENXR_VERSION_MINOR",
    "PYOPENXR_VERSION_PATCH",
    "PYOPENXR_VERSION_PATCH_INCREMENTAL",
    "PYOPENXR_VERSION_SUFFIX",
    "PYOPENXR_VERSION",
    "Version",
    "XR_CURRENT_API_VERSION",
    "XR_VERSION_MAJOR",
    "XR_VERSION_MINOR",
    "XR_VERSION_PATCH",
]
