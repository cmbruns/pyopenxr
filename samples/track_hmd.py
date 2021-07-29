import ctypes
import os

# TODO: loader submodule
os.add_dll_directory(os.path.dirname(__file__))
_openxr_loader = ctypes.cdll.LoadLibrary("openxr_loader.dll")
print(_openxr_loader)

# TODO: finish initial api call around line 350 of
# https://github.com/jherico/OpenXR-Samples/blob/master/src/examples/sdl2_gl_single_file_example_c.cpp

# TODO: constants submodule
XR_MAX_EXTENSION_NAME_SIZE = 128


# TODO: structures submodule
XrStructureType = ctypes.c_int  # Well enum actually
XR_TYPE_EXTENSION_PROPERTIES = 2


class XrExtensionProperties(ctypes.Structure):
    _fields_ = [
        ("type", XrStructureType),
        ("next", ctypes.c_void_p),
        ("extensionName", ctypes.c_char * XR_MAX_EXTENSION_NAME_SIZE),
        ("extensionVersion", ctypes.c_uint32),
    ]


# TODO: raw function properties submodule
fn = _openxr_loader.xrEnumerateInstanceExtensionProperties
fn.restype = ctypes.c_int  # Actually an enum
property_count_output = ctypes.c_uint32()  # XrResult
fn.argtypes = [
    ctypes.c_char_p,  # layerName
    ctypes.c_uint32,  # propertyCapacityInput
    ctypes.POINTER(ctypes.c_uint32),  # propertyCountOutput
    ctypes.c_void_p,  # properties  # pointer to array of structs
]
print(fn)

extension_count = ctypes.c_uint32()
result = fn(None, 0, ctypes.byref(extension_count), None)
print(result)
print(extension_count)

properties_type = XrExtensionProperties * extension_count.value
properties = properties_type()

# TODO: automatically initialize?
for p in properties:
    p.type = XR_TYPE_EXTENSION_PROPERTIES

# TODO: populate initial values...
result2 = fn(None, extension_count, ctypes.byref(extension_count), ctypes.byref(properties))
print(result2)
print(extension_count)
