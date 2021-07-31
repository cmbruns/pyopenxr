import xr

# The very first step when using OpenXR is to query the available VR/AR capabilities
for prop in xr.enumerate_instance_extension_properties():
    print(prop.extension_name)
