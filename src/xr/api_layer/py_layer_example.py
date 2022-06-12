import ctypes
import xr


class DynamicLayerExample(xr.ILoaderDynamicApiLayer):
    def __init__(self):
        super().__init__(name="XR_APILAYER_PYOPENXR_Example_Layer")
        # Store function pointers to keep them alive
        self.p_xrGetInstanceProcAddr = xr.PFN_xrGetInstanceProcAddr(self.get_instance_proc_addr)
        self.p_xrCreateApiLayerInstance = xr.PFN_xrCreateApiLayerInstance(self.create_api_layer_instance)
        self.nextXrGetInstanceProcAddr = None

    def create_api_layer_instance(
        self,
        info: ctypes.POINTER(xr.InstanceCreateInfo),
        api_layer_info: ctypes.POINTER(xr.ApiLayerCreateInfo),
        instance: xr.InstanceHandle,
    ) -> xr.Result:
        print("create_api_layer_instance")
        next_info = api_layer_info.contents.next_info.contents
        self.nextXrGetInstanceProcAddr = next_info.next_get_instance_proc_addr
        result = next_info.next_create_api_layer_instance(info, api_layer_info, instance)
        if xr.failed(result):
            return result
        # TODO: intercept something
        return result

    def get_instance_proc_addr(
        self,
        instance: xr.InstanceHandle,
        name: ctypes.c_char_p,
        function: xr.PFN_xrVoidFunction,
    ) -> xr.Result:
        # TODO: intercept something
        print(f"get_instance_prod_addr {name.decode()}")
        return self.nextXrGetInstanceProcAddr(instance, name, function)

    def negotiate_loader_api_layer_interface(
            self,
            loader_info: xr.NegotiateLoaderInfo,
            layer_name: str,
            api_layer_request: xr.NegotiateApiLayerRequest,
    ) -> xr.Result:
        """
        Override this method in a derived class to create your own temporary dynamic OpenXR API layer.

        If this layer is able to support the request, it must: return xr.Result.SUCCESS and:
            Fill in pname:layerRequest→pname:layerInterfaceVersion with the API layer interface version it desires to support.
            Fill in pname:layerRequest→pname:layerApiVersion with the API version of OpenXR it will execute under.
            Fill in pname:layerRequest→pname:getInstanceProcAddr with a valid function pointer so that the loader can query function pointers to the remaining OpenXR commands supported by the API layer.
            Fill in pname:layerRequest→pname:createLayerInstance with a valid function pointer so that the loader can create the instance through the API layer call chain.

        Otherwise, it must: return XR_ERROR_INITIALIZATION_FAILED

        :param loader_info: must be a valid pointer to a constant xr.NegotiateLoaderInfo structure.
        :param layer_name: must be a string listing the name of an API layer which the loader is attempting to negotiate with.
        :param api_layer_request: must be a valid pointer to a xr.NegotiateApiLayerRequest structure.
        :return: xr.Result.SUCCESS or xr.Result.ERROR_INITIALIZATION_FAILED
        """
        print("negotiating")

        # Set up our layer to intercept OpenXR calls.
        api_layer_request.layer_interface_version = xr.CURRENT_LOADER_API_LAYER_VERSION
        api_layer_request.layer_api_version = xr.XR_CURRENT_API_VERSION
        # These function pointers were created in __init__
        api_layer_request.get_instance_proc_addr = self.p_xrGetInstanceProcAddr
        api_layer_request.create_api_layer_instance = self.p_xrCreateApiLayerInstance

        return xr.Result.SUCCESS


if __name__ == "__main__":
    dle = DynamicLayerExample()
    for layer in xr.enumerate_api_layer_properties():
        print(layer)
    assert dle.name in xr.enumerate_api_layer_properties()
    xr.create_instance(xr.InstanceCreateInfo(
        enabled_api_layer_names=[dle.name],
    ))
