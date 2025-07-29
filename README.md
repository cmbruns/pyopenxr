# pyopenxr
### Unofficial Python bindings for the [OpenXR SDK](https://github.com/KhronosGroup/OpenXR-SDK) to access VR and AR devices

**pyopenxr** is a Python developer SDK for device tracking and rapid virtual reality prototyping using the headset-agnostic OpenXR API. It provides a clean, Pythonic interface to the OpenXR runtime, enabling cross-platform AR/VR development with minimal boilerplate.

![Build Status](https://github.com/cmbruns/pyopenxr/actions/workflows/python-package.yml/badge.svg)
[![Pages Doc Status](https://github.com/cmbruns/pyopenxr/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/cmbruns/pyopenxr/actions/workflows/pages/pages-build-deployment)
[![Documentation](https://img.shields.io/badge/docs-pyopenxr-blue)](https://cmbruns.github.io/pyopenxr/)
![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)

![hello_xr1](https://user-images.githubusercontent.com/2649705/172025969-5cf276bd-2a6c-42a2-852a-0605fe72a716.PNG)

---

## 🚀 Installation

```bash
pip install pyopenxr
```

## 🧪 Quick Start
```python
import xr

# Query the available VR/AR extensions
available = xr.enumerate_instance_extension_properties()

# Replace with whatever extensions are required for your application...
required = [xr.KHR_OPENGL_ENABLE_EXTENSION_NAME]
for prop in required:
    assert prop in available
```

Explore the complete working example 
[`hello_xr.py`](https://github.com/cmbruns/pyopenxr_examples/examples)
for a hands-on introduction.

## Pythonic naming conventions

| symbol      | Python example                       | C example                             |
| ----------- | ------------------------------------ | ------------------------------------- |
| function    | `xr.create_instance(...)`            | `xrCreateInstance(...)`               |
| constant    | `xr.MAX_SYSTEM_NAME_SIZE`            | `XR_MAX_SYSTEM_NAME_SIZE`             |
| struct name | `xr.ExtensionProperties`             | `XrExtensionProperties`               |
| type alias  | `xr.Version`                         | `XrVersion`                           |
| enum type   | `xr.FormFactor`                      | `xrFormFactor`                        |
| enum value  | `xr.FormFactor.HEAD_MOUNTED_DISPLAY` | `XR_FORM_FACTOR_HEAD_MOUNTED_DISPLAY` |
| handle      | `xr.Instance`                        | `XrInstance`                          |

## 📚 Documentation
Full API reference and guides are [available](https://cmbruns.github.io/pyopenxr/)

## 📦 License
This project is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

Copyright © 2021 Christopher Bruns.
