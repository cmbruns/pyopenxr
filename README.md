# pyopenxr
### Unofficial python bindings for the OpenXR SDK to access VR and AR devices

This is a work in progress. Stay tuned.

## Installation

``pip install pyopenxr``

## Use

```python
import xr

# Query the available VR/AR capabilities
for prop in xr.enumerate_instance_extension_properties():
    print(prop.extension_name.decode())
```
