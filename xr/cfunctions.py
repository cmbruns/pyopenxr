import ctypes
from .library import openxr_loader_library

fn1 = openxr_loader_library.xrEnumerateInstanceExtensionProperties
fn1.restype = ctypes.c_int  # Actually an enum
fn1.argtypes = [
    ctypes.c_char_p,  # layerName
    ctypes.c_uint32,  # propertyCapacityInput
    ctypes.POINTER(ctypes.c_uint32),  # propertyCountOutput
    ctypes.c_void_p,  # properties  # pointer to array of structs
]


