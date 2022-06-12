import xr
from xr.api_layer.loader_interfaces import ILoaderDynamicApiLayer, NegotiateLoaderInfo, NegotiateApiLayerRequest


class DynamicLayerExample(ILoaderDynamicApiLayer):
    def __init__(self, name):
        super().__init__(name)

    def negotiate_loader_api_layer_interface(
            self,
            loader_info: NegotiateLoaderInfo,
            layer_name: str,
            api_layer_request: NegotiateApiLayerRequest,
    ) -> xr.ResultException:
        print(loader_info)
        print(f"The loader called my negotiate function! '{layer_name}'")
        print(f"{api_layer_request}")
        return xr.Result.ERROR_INITIALIZATION_FAILED
