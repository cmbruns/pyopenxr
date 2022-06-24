import ctypes
from ctypes import c_char, c_char_p, c_uint32, c_void_p, CFUNCTYPE, POINTER, c_size_t

from ..enums import EnumBase, Result
from ..typedefs import (
    InstanceCreateInfo,
    Instance,
    PFN_xrGetInstanceProcAddr,
    VersionNumber
)
from ..version import Version

# TODO: generate the header information from C automatically

# Loader/API Layer Interface versions
#  1 - First version, introduces negotiation structure and functions
CURRENT_LOADER_API_LAYER_VERSION = 1

MAX_API_LAYER_NAME_SIZE = 256
API_LAYER_MAX_SETTINGS_PATH_SIZE = 512


# Version negotiation values
class LoaderInterfaceStructs(EnumBase):
    UNINITIALIZED = 0,  # corrected spelling error in the C API.
    LOADER_INFO = 1,
    API_LAYER_REQUEST = 2,
    RUNTIME_REQUEST = 3,
    API_LAYER_CREATE_INFO = 4,
    API_LAYER_NEXT_INFO = 5,

    def __str__(self):
        return f"xr.{super().__str__()}"


class NegotiateLoaderInfo(ctypes.Structure):
    _fields_ = [
        ("struct_type", LoaderInterfaceStructs.ctype()),  # XR_LOADER_INTERFACE_STRUCT_LOADER_INFO
        ("struct_version", c_uint32),  # XR_LOADER_INFO_STRUCT_VERSION
        ("struct_size", c_size_t),  # sizeof(XrNegotiateLoaderInfo)
        ("min_interface_version", c_uint32),
        ("max_interface_version", c_uint32),
        ("min_api_version", VersionNumber),
        ("max_api_version", VersionNumber),
    ]

    def __str__(self) -> str:
        return ("NegotiateLoaderInfo("
                # Skipping the type enum, which is redundant
                f"struct_version={Version(self.struct_version)}"
                f", struct_size={self.struct_size}"
                f", min_interface_version={self.min_interface_version}"
                f", max_interface_version={self.max_interface_version}"
                f", min_api_version={Version(self.min_api_version)}"
                f", max_api_version={Version(self.max_api_version)}"
                ")")


# "forward" declaration
class ApiLayerNextInfo(ctypes.Structure):
    pass  # Fields are defined further below, for self-reference and declaration order reasons


class ApiLayerCreateInfo(ctypes.Structure):
    _fields_ = [
        ("struct_type", LoaderInterfaceStructs.ctype()),  # XR_LOADER_INTERFACE_STRUCT_API_LAYER_CREATE_INFO
        ("struct_version", c_uint32),  # XR_API_LAYER_CREATE_INFO_STRUCT_VERSION
        ("struct_size", c_size_t),  # sizeof(XrApiLayerCreateInfo)
        ("loader_instance", c_void_p),  # Pointer to the LoaderInstance class
        ("settings_file_location", c_char * API_LAYER_MAX_SETTINGS_PATH_SIZE),  # Location to the found settings file (or empty '\0')
        ("next_info", POINTER(ApiLayerNextInfo)),
    ]


PFN_xrCreateApiLayerInstance = CFUNCTYPE(
    Result.ctype(),  # return value
    POINTER(InstanceCreateInfo),  # info
    POINTER(ApiLayerCreateInfo),  # apiLayerInfo
    Instance,  # instance
)


# ApiLayerNextInfo class was "forward" declared earlier
ApiLayerNextInfo._fields_ = [
    ("struct_type", LoaderInterfaceStructs.ctype()),                # XR_LOADER_INTERFACE_STRUCT_API_LAYER_NEXT_INFO
    ("struct_version", c_uint32),                                   # XR_API_LAYER_NEXT_INFO_STRUCT_VERSION
    ("struct_size", c_size_t),                                      # sizeof(XrApiLayerNextInfo)
    ("layer_name", c_char * MAX_API_LAYER_NAME_SIZE),               # Name of API layer which should receive this info
    ("next_get_instance_proc_addr", PFN_xrGetInstanceProcAddr),        # Pointer to next API layer's xrGetInstanceProcAddr
    ("next_create_api_layer_instance", PFN_xrCreateApiLayerInstance),  # Pointer to next API layer's xrCreateApiLayerInstance
    ("next", POINTER(ApiLayerNextInfo)),                           # Pointer to the next API layer info in the sequence
]


class NegotiateApiLayerRequest(ctypes.Structure):
    _fields_ = [
        ("struct_type", LoaderInterfaceStructs.ctype()),   # XR_LOADER_INTERFACE_STRUCT_API_LAYER_REQUEST
        ("struct_version", c_uint32),                # XR_API_LAYER_INFO_STRUCT_VERSION
        ("struct_size", c_size_t),                   # sizeof(XrNegotiateApiLayerRequest)
        ("layer_interface_version", c_uint32),        # CURRENT_LOADER_API_LAYER_VERSION
        ("layer_api_version", VersionNumber),
        ("get_instance_proc_addr", PFN_xrGetInstanceProcAddr),
        ("create_api_layer_instance", PFN_xrCreateApiLayerInstance),
    ]

    def __str__(self) -> str:
        return ("NegotiateApiLayerRequest("
                # Skipping the type enum, which is redundant
                f"struct_version={Version(self.struct_version)}"
                f", struct_size={self.struct_size}"
                f", layer_interface_version={Version(self.layer_interface_version)}"
                f", layer_api_version={Version(self.layer_api_version)}"
                # Skip the function pointers when printing...
                ")")


PFN_xrNegotiateLoaderApiLayerInterface = CFUNCTYPE(
    Result.ctype(),  # return value
    POINTER(NegotiateLoaderInfo),  # loader_info
    c_char_p,  # api_layer_name
    POINTER(NegotiateApiLayerRequest),  # api_layer_request
)

__all__ = [
    "ApiLayerCreateInfo",
    "CURRENT_LOADER_API_LAYER_VERSION",
    "NegotiateLoaderInfo",
    "NegotiateApiLayerRequest",
    "PFN_xrCreateApiLayerInstance",
    "PFN_xrNegotiateLoaderApiLayerInterface",
]
