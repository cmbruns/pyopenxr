import xr

for prop in xr.enumerate_instance_extension_properties():
    print(prop.extension_name)
