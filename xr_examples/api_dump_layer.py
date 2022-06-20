import os

import xr

# Turn on extra debugging messages in the OpenXR Loader
# os.environ["XR_LOADER_DEBUG"] = "all"
# os.environ["LD_BIND_NOW"] = "1"

print(os.environ["XR_API_LAYER_PATH"])
print(len(xr.enumerate_api_layer_properties()))
print(*xr.enumerate_api_layer_properties())

# 1) Setting/clearing the environment from python does affect the layers
os.environ.pop("XR_API_LAYER_PATH", None)
print(len(xr.enumerate_api_layer_properties()))
print(*xr.enumerate_api_layer_properties())

xr.expose_packaged_api_layers()
print(len(xr.enumerate_api_layer_properties()))
print(*xr.enumerate_api_layer_properties())

foo_layer = xr.SteamVrLinuxDestroyInstanceLayer()
print(foo_layer.name)

# 2) The choice of layers can be specified in the instance constructor
instance_handle = xr.create_instance(create_info=xr.InstanceCreateInfo(
    enabled_api_layer_names=[
        xr.LUNARG_api_dump_APILAYER_NAME,
        foo_layer.name,
        # xr.LUNARG_core_validation_APILAYER_NAME,
        # xr.LUNARG_api_dump_APILAYER_NAME,
    ],))

xr.destroy_instance(instance_handle)
