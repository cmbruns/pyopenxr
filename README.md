# pyopenxr
### Unofficial python bindings for the [OpenXR SDK](https://github.com/KhronosGroup/OpenXR-SDK) to access VR and AR devices

pyopenxr is a python developer SDK with features for device tracking and rapid virtual reality prototyping using the headset-agnostic OpenXR API.

![Build Status](https://github.com/cmbruns/pyopenxr/actions/workflows/python-package.yml/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/pyopenxr/badge/?version=latest)](https://pyopenxr.readthedocs.io/en/latest/?badge=latest)

![hello_xr1](https://user-images.githubusercontent.com/2649705/172025969-5cf276bd-2a6c-42a2-852a-0605fe72a716.PNG)


## Installing pyopenxr

``pip install pyopenxr``

## Using pyopenxr

```python
import xr

# Query the available VR/AR extensions
available = xr.enumerate_instance_extension_properties()

# Replace with whatever extensions are required for your
# particular application...
required = [xr.KHR_OPENGL_ENABLE_EXTENSION_NAME, ]
for prop in required:
    assert prop in available
```

Study the complete working `hello_xr.py` example at https://github.com/cmbruns/pyopenxr_examples

## Pythonic naming conventions in pyopenxr

| symbol      | Python example                       | C example                             |
| ----------- | ------------------------------------ | ------------------------------------- |
| function    | `xr.create_instance(...)`            | `xrCreateInstance(...)`               |
| constant    | `xr.MAX_SYSTEM_NAME_SIZE`            | `XR_MAX_SYSTEM_NAME_SIZE`             |
| struct name | `xr.ExtensionProperties`             | `XrExtensionProperties`               |
| type alias  | `xr.Version`                         | `XrVersion`                           |
| enum type   | `xr.FormFactor`                      | `xrFormFactor`                        |
| enum value  | `xr.FormFactor.HEAD_MOUNTED_DISPLAY` | `XR_FORM_FACTOR_HEAD_MOUNTED_DISPLAY` |
| handle      | `xr.Instance`                        | `XrInstance`                          |


