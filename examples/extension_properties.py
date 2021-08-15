import xr

# Query the available VR/AR capabilities
for prop in xr.enumerate_instance_extension_properties():
    print(prop.extension_name.decode())
