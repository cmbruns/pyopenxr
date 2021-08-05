# pyopenxr
### Unofficial python bindings for the OpenXR SDK to access VR and AR devices

This is a work in progress. Stay tuned.

## Installation

``pip install pyopenxr``

## Use

Simple test:

```python
import xr

# The very first step when using OpenXR is to query the available VR/AR capabilities
for prop in xr.enumerate_instance_extension_properties():
    print(prop.extension_name)
```
