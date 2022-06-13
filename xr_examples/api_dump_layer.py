import os

import xr

foo_layer = xr.SteamVrLinuxDestroyInstanceLayer()

# 1) Setting/clearing the environment from python does affect the layers
del os.environ["XR_API_LAYER_PATH"]
assert len(xr.enumerate_api_layer_properties()) == 0

os.environ["XR_API_LAYER_PATH"] = "C:/Program Files (x86)/OPENXR/bin/api_layers"
assert len(xr.enumerate_api_layer_properties()) >= 2

del os.environ["XR_API_LAYER_PATH"]
assert len(xr.enumerate_api_layer_properties()) == 0

xr.api_layer.layer_path.expose_packaged_api_layers()
assert len(xr.enumerate_api_layer_properties()) >= 2

print(len(xr.enumerate_api_layer_properties()))

# 2) The choice of layers can be specified in the instance constructor
instance_handle = xr.create_instance(create_info=xr.InstanceCreateInfo(
    enabled_api_layer_names=[
        xr.api_layer.XR_APILAYER_LUNARG_core_validation_NAME,
        # "XR_APILAYER_LUNARG_api_dump",
    ],))

print(*xr.enumerate_instance_extension_properties())
