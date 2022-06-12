import abc
import ctypes
from ctypes import c_char, c_char_p, c_int, c_uint32, c_void_p, CFUNCTYPE, POINTER, c_size_t
import pkg_resources
import platform

from ..enums import EnumBase
from ..exception import InitializationFailedError, ResultException, Result
from ..typedefs import (
    InstanceCreateInfo,
    InstanceHandle,
    PFN_xrGetInstanceProcAddr,
    VersionNumber
)
from ..version import Version


def _load_python_layer_library():
    if platform.system() == "Windows":
        package = "xr.api_layer.windows"
        name = "XrApiLayer_python.dll"
    elif platform.system() == "Linux":
        package = "xr.api_layer.linux"
        name = "XrApiLayer_python.so"
    else:
        raise NotImplementedError
    path = pkg_resources.resource_filename(package, name)
    library = ctypes.cdll.LoadLibrary(path)
    return library


_python_layer_library = _load_python_layer_library()


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


# "forward" declaration
class ApiLayerNextInfo(ctypes.Structure):
    pass  # Fields are defined further below, for self-reference and declaration order reasons


class ApiLayerCreateInfo(ctypes.Structure):
    _fields_ = [
        ("structType", LoaderInterfaceStructs.ctype()),  # XR_LOADER_INTERFACE_STRUCT_API_LAYER_CREATE_INFO
        ("structVersion", c_uint32),  # XR_API_LAYER_CREATE_INFO_STRUCT_VERSION
        ("structSize", c_size_t),  # sizeof(XrApiLayerCreateInfo)
        ("loaderInstance", c_void_p),  # Pointer to the LoaderInstance class
        ("settings_file_location", c_char * API_LAYER_MAX_SETTINGS_PATH_SIZE),  # Location to the found settings file (or empty '\0')
        ("nextInfo", POINTER(ApiLayerNextInfo)),
    ]


PFN_xrCreateApiLayerInstance = CFUNCTYPE(
    Result.ctype(),  # return value
    POINTER(InstanceCreateInfo),  # info
    POINTER(ApiLayerCreateInfo),  # apiLayerInfo
    InstanceHandle,  # instance
)


# ApiLayerNextInfo class was "forward" declared earlier
ApiLayerNextInfo._fields_ = [
    ("structType", LoaderInterfaceStructs.ctype()),                # XR_LOADER_INTERFACE_STRUCT_API_LAYER_NEXT_INFO
    ("structVersion", c_uint32),                                   # XR_API_LAYER_NEXT_INFO_STRUCT_VERSION
    ("structSize", c_size_t),                                      # sizeof(XrApiLayerNextInfo)
    ("layerName", c_char * MAX_API_LAYER_NAME_SIZE),               # Name of API layer which should receive this info
    ("nextGetInstanceProcAddr", PFN_xrGetInstanceProcAddr),        # Pointer to next API layer's xrGetInstanceProcAddr
    ("nextCreateApiLayerInstance", PFN_xrCreateApiLayerInstance),  # Pointer to next API layer's xrCreateApiLayerInstance
    ("next", POINTER(ApiLayerNextInfo)),                           # Pointer to the next API layer info in the sequence
]


class NegotiateApiLayerRequest(ctypes.Structure):
    _fields_ = [
        ("structType", LoaderInterfaceStructs.ctype()),   # XR_LOADER_INTERFACE_STRUCT_API_LAYER_REQUEST
        ("structVersion", c_uint32),                # XR_API_LAYER_INFO_STRUCT_VERSION
        ("structSize", c_size_t),                   # sizeof(XrNegotiateApiLayerRequest)
        ("layerInterfaceVersion", c_uint32),        # CURRENT_LOADER_API_LAYER_VERSION
        ("layerApiVersion", VersionNumber),
        ("getInstanceProcAddr", PFN_xrGetInstanceProcAddr),
        ("createApiLayerInstance", PFN_xrCreateApiLayerInstance),
    ]

    def __str__(self) -> str:
        return ("NegotiateApiLayerRequest("f"{LoaderInterfaceStructs(self.structType)}"
                f", {Version(self.structVersion)}"
                f", {self.structSize}"
                f", {Version(self.layerInterfaceVersion)}"
                f", {Version(self.layerApiVersion)}"
                # Skip the function pointers when printing...
                ")")


PFN_xrNegotiateLoaderApiLayerInterface = CFUNCTYPE(
    Result.ctype(),  # return value
    POINTER(NegotiateLoaderInfo),  # loader_info
    c_char_p,  # api_layer_name
    POINTER(NegotiateApiLayerRequest),  # api_layer_request
)


# TODO: is this needed?
xrNegotiateLoaderApiLayerInterface = _python_layer_library.xrNegotiateLoaderApiLayerInterface
xrNegotiateLoaderApiLayerInterface.restype = Result
xrNegotiateLoaderApiLayerInterface.argtypes = [
    POINTER(NegotiateLoaderInfo),  # loaderInfo
    c_char_p,  # layerName
    POINTER(NegotiateApiLayerRequest),  # apiLayerRequest
]

insertXrApiLayer = _python_layer_library.insertXrApiLayer
insertXrApiLayer.restype = None
insertXrApiLayer.argtypes = [
    c_char_p,  # pName
    c_int,  # nameLength
    PFN_xrNegotiateLoaderApiLayerInterface,  # negotiateFunction
]


class ILoaderDynamicApiLayer(abc.ABC):
    """Base class for temporary dynamic runtime python OpenXR API layers."""

    def __init__(self, name: str) -> None:
        self._name = name
        # store pointer to keep it alive
        self.p_negotiate_fn = PFN_xrNegotiateLoaderApiLayerInterface(
            self._negotiate_loader_api_layer_interface)
        print(self.p_negotiate_fn)
        insertXrApiLayer(self.name.encode(), len(self.name), self.p_negotiate_fn)
        # TODO: store json file

    @property
    def name(self) -> str:
        return self._name

    def _negotiate_loader_api_layer_interface(
            self,
            loader_info: NegotiateLoaderInfo,
            layer_name: c_char_p,
            api_layer_request: POINTER(NegotiateApiLayerRequest),
    ) -> int:
        """Lower-level function that will be passed to the C loader library."""
        result = self.negotiate_loader_api_layer_interface(
            loader_info,
            layer_name.decode(),
            api_layer_request.contents,
        )
        return result.get_result_enum().value

    @abc.abstractmethod
    def negotiate_loader_api_layer_interface(
            self,
            loader_info: NegotiateLoaderInfo,
            layer_name: str,
            api_layer_request: NegotiateApiLayerRequest,
    ) -> Result:
        """
        Override this method in a derived class to create your own temporary dynamic OpenXR API layer.

        If this layer is able to support the request, it must: return xr.Result.SUCCESS and:
            Fill in pname:layerRequest→pname:layerInterfaceVersion with the API layer interface version it desires to support.
            Fill in pname:layerRequest→pname:layerApiVersion with the API version of OpenXR it will execute under.
            Fill in pname:layerRequest→pname:getInstanceProcAddr with a valid function pointer so that the loader can query function pointers to the remaining OpenXR commands supported by the API layer.
            Fill in pname:layerRequest→pname:createLayerInstance with a valid function pointer so that the loader can create the instance through the API layer call chain.

        Otherwise, it must: return XR_ERROR_INITIALIZATION_FAILED

        :param loader_info: must be a valid pointer to a constant xr.NegotiateLoaderInfo structure.
        :param layer_name: must be a string listing the name of an API layer which the loader is attempting to negotiate with.
        :param api_layer_request: must be a valid pointer to a xr.NegotiateApiLayerRequest structure.
        :return: xr.Result.SUCCESS or xr.Result.ERROR_INITIALIZATION_FAILED
        """
        return Result.ERROR_INITIALIZATION_FAILED


__all__ = [
    "ILoaderDynamicApiLayer",
]
