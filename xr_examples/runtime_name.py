import xr

instance = xr.create_instance(create_info=xr.InstanceCreateInfo())
instance_props = xr.get_instance_properties(instance)
print(f"The current active OpenXR runtime is: {instance_props.runtime_name.decode()}")
