# pyopenxr
### Unofficial python bindings for the [OpenXR SDK](https://github.com/KhronosGroup/OpenXR-SDK) to access VR and AR devices

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

## Pythonic naming conventions in pyopenxr

| symbol      | Python example                       | C example                             |
| ----------- | ------------------------------------ | ------------------------------------- |
| function    | `xr.create_instance(...)`            | `xrCreateInstance(...)`               |
| constant    | `xr.MAX_SYSTEM_NAME_SIZE`            | `XR_MAX_SYSTEM_NAME_SIZE`             |
| struct name | `xr.ExtensionProperties`             | `XrExtensionProperties`               |
| type alias  | `xr.Version`                         | `XrVersion`                           |
| enum type   | `xr.FormFactor`                      | `xrFormFactor`                        |
| enum value  | `xr.FormFactor.HEAD_MOUNTED_DISPLAY` | `XR_FORM_FACTOR_HEAD_MOUNTED_DISPLAY` |
| handle      | `xr.InstanceHandle`                  | `XrInstance`                          |
