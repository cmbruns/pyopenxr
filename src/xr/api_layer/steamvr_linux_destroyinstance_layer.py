from ctypes import byref, c_char_p, cast, memmove, POINTER, pointer, sizeof
import platform
import xr
from xr.raw_functions import xrGetInstanceProperties


class SteamVrLinuxDestroyInstanceLayer(xr.DynamicApiLayerBase):
    """
    Pure-python OpenXR API layer.
    Designed to work around SteamVR linux bug.
    https://steamcommunity.com/app/250820/discussions/8/3114772813482874960/
    https://github.com/cmbruns/pyopenxr/pull/66
    """
    def __init__(self):
        super().__init__(name="XR_APILAYER_PYOPENXR_Example_Layer")
        # Store function pointers to keep them alive
        self.p_xrGetInstanceProcAddr = xr.PFN_xrGetInstanceProcAddr(self.get_instance_proc_addr)
        self.p_xrCreateApiLayerInstance = xr.PFN_xrCreateApiLayerInstance(self.create_api_layer_instance)
        self.nextXrGetInstanceProcAddr = None
        self.nextXrDestroyInstance = xr.PFN_xrDestroyInstance()
        self.p_xrDestroyInstance = xr.PFN_xrDestroyInstance(self.destroy_instance)
        self.is_steamvr = False

    def create_api_layer_instance(
        self,
        info: POINTER(xr.InstanceCreateInfo),
        api_layer_info: POINTER(xr.ApiLayerCreateInfo),
        instance: xr.Instance,
    ) -> xr.Result:
        # Dereference the next_info field for easier calling.
        next_info = api_layer_info.contents.next_info.contents
        self.nextXrGetInstanceProcAddr = next_info.next_get_instance_proc_addr
        # Let the instance be created.
        result = next_info.next_create_api_layer_instance(info, api_layer_info, instance)
        if xr.failed(result):
            return result
        # Remember the subsequent layer's xrDestroyInstance() function
        fn = xr.PFN_xrVoidFunction()
        result = self.nextXrGetInstanceProcAddr(
            instance,
            b"xrDestroyInstance",  # Use bytes object not string because this is low level C API.
            pointer(fn),
        )
        self.nextXrDestroyInstance = cast(fn, xr.PFN_xrDestroyInstance)
        if xr.failed(result):
            return result
        #
        return result

    def get_instance_proc_addr(
        self,
        instance: xr.Instance,
        name: c_char_p,
        function: POINTER(xr.PFN_xrVoidFunction),
    ) -> xr.Result:
        # Intercept calls to xrDestroyInstance
        if name == b"xrDestroyInstance":
            # TODO: Is there a neater way than memmove?
            memmove(function, byref(self.p_xrDestroyInstance), sizeof(xr.PFN_xrVoidFunction))
            return xr.Result.SUCCESS
        # Delegate all other function calls to the subsequent API layer
        return self.nextXrGetInstanceProcAddr(instance, name, function)

    # Signature must exactly match the low-level signature of xrDestroyInstance
    def destroy_instance(self, instance: xr.Instance) -> xr.Result:
        instance_properties = xr.InstanceProperties()
        xrGetInstanceProperties(instance, byref(instance_properties))
        is_steam_vr = instance_properties.runtime_name == b"SteamVR/OpenXR"
        if is_steam_vr and platform.system() == "Linux":
            return xr.Result.SUCCESS  # Elide call to xrDestroyInstance
        # Propagate function call down into to the next API layer
        return self.nextXrDestroyInstance(instance)

    def negotiate_loader_api_layer_interface(
            self,
            loader_info: xr.NegotiateLoaderInfo,
            layer_name: str,
            api_layer_request: xr.NegotiateApiLayerRequest,
    ) -> xr.Result:
        """
        Set up our layer to intercept OpenXR function calls.
        :param loader_info:
        :param layer_name: The name of an API layer which the loader is attempting to negotiate with.
        :param api_layer_request: Fill in this information.
        :return: xr.Result.SUCCESS or xr.Result.ERROR_INITIALIZATION_FAILED
        """
        # TODO: compare versions in loader_info
        api_layer_request.layer_interface_version = xr.CURRENT_LOADER_API_LAYER_VERSION
        api_layer_request.layer_api_version = xr.XR_CURRENT_API_VERSION
        api_layer_request.get_instance_proc_addr = self.p_xrGetInstanceProcAddr
        api_layer_request.create_api_layer_instance = self.p_xrCreateApiLayerInstance
        return xr.Result.SUCCESS


if __name__ == "__main__":
    dle = SteamVrLinuxDestroyInstanceLayer()
    assert dle.name in xr.enumerate_api_layer_properties()
    instance_handle = xr.create_instance(xr.InstanceCreateInfo(
        enabled_api_layer_names=[
            # xr.XR_APILAYER_LUNARG_api_dump_NAME,
            # xr.XR_APILAYER_LUNARG_core_validation_NAME,
            dle.name,
            # TODO: adding layers after causes problems
            # xr.XR_APILAYER_LUNARG_core_validation_NAME,
            # xr.XR_APILAYER_LUNARG_api_dump_NAME,
        ],
    ))
    xr.destroy_instance(instance_handle)  # Should be no-op on Linux/SteamVR with layer active


__all__ = [
    "SteamVrLinuxDestroyInstanceLayer",
]
