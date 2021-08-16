import xr

# Query the available VR/AR capabilities
eprops = xr.enumerate_instance_extension_properties()
for p in eprops:
    print(p)
assert "XR_KHR_opengl_enable" in eprops
