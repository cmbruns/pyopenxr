import ctypes

from .layer_path import py_layer_library_path
from ..exception import Result
from .loader_interfaces import NegotiateLoaderInfo, NegotiateApiLayerRequest, PFN_xrNegotiateLoaderApiLayerInterface

_python_layer_library = ctypes.cdll.LoadLibrary(py_layer_library_path())

xrNegotiateLoaderApiLayerInterface = _python_layer_library.xrNegotiateLoaderApiLayerInterface
xrNegotiateLoaderApiLayerInterface.restype = Result
xrNegotiateLoaderApiLayerInterface.argtypes = [
    ctypes.POINTER(NegotiateLoaderInfo),  # loaderInfo
    ctypes.c_char_p,  # layerName
    ctypes.POINTER(NegotiateApiLayerRequest),  # apiLayerRequest
]

insertXrApiLayer = _python_layer_library.insertXrApiLayer
insertXrApiLayer.restype = None
insertXrApiLayer.argtypes = [
    ctypes.c_char_p,  # pName
    ctypes.c_int,  # nameLength
    PFN_xrNegotiateLoaderApiLayerInterface,  # negotiateFunction
]
