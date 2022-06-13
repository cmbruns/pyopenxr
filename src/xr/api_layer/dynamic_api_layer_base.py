import abc
import json
import os
import tempfile
from ctypes import c_char_p, POINTER

from ..enums import Result
from .layer_path import add_folder_to_api_layer_path, py_layer_library_path
from .loader_interfaces import PFN_xrNegotiateLoaderApiLayerInterface, NegotiateLoaderInfo, \
    NegotiateApiLayerRequest
from .raw_functions import insertXrApiLayer


class DynamicApiLayerBase(abc.ABC):
    """Base class for temporary dynamic runtime python OpenXR API layers."""

    def __init__(self, name: str, description: str = "", json_path=None) -> None:
        self._name = name
        self.description = description
        self.json_path = json_path
        # store pointer to keep it alive
        self.p_negotiate_fn = PFN_xrNegotiateLoaderApiLayerInterface(
            self._negotiate_loader_api_layer_interface)
        insertXrApiLayer(self.name.encode(), len(self.name), self.p_negotiate_fn)
        # Store json file in temporary folder
        if self.json_path is None:
            self.json_dir = tempfile.TemporaryDirectory()
            self.json_dir.cleanup()  # So it will be deleted later  TODO: those folders remain
            self.json_path = self.json_dir.name
        os.mkdir(self.json_path)
        add_folder_to_api_layer_path(self.json_path)
        json_file_name = f"{self.json_path}/{self.name}.json"
        with open(json_file_name, "w") as layer_json:
            layer_json.write(json.dumps(
                {
                    "file_format_version": "1.0.0",
                    "api_layer": {
                        "name": f"{self.name}",
                        "library_path": f"{py_layer_library_path()}",
                        "api_version": "1.0",
                        "implementation_version": "1",
                        "description": f"{self.description}"
                    }
                }, indent=4))
            layer_json.write("\n")

    @property
    def name(self) -> str:
        return self._name

    def _negotiate_loader_api_layer_interface(
            self,
            loader_info: NegotiateLoaderInfo,
            layer_name: c_char_p,
            api_layer_request: POINTER(NegotiateApiLayerRequest),
    ) -> int:
        """Lower-level function that will be passed to the C loader library."""
        try:
            # noinspection PyUnresolvedReferences
            result = self.negotiate_loader_api_layer_interface(
                loader_info.contents,
                layer_name.decode(),
                api_layer_request.contents,
            )
            return result.value
        except Exception:
            return Result.ERROR_INITIALIZATION_FAILED.value

    @abc.abstractmethod
    def negotiate_loader_api_layer_interface(
            self,
            loader_info: NegotiateLoaderInfo,
            layer_name: str,
            api_layer_request: NegotiateApiLayerRequest,
    ) -> Result:
        """
        Override this method in a derived class to create your own temporary dynamic OpenXR API layer.

        If this layer is able to support the request, it must: return xr.Result.SUCCESS and:
            Fill in pname:layerRequest→pname:layerInterfaceVersion with the API layer interface version it desires to support.
            Fill in pname:layerRequest→pname:layerApiVersion with the API version of OpenXR it will execute under.
            Fill in pname:layerRequest→pname:getInstanceProcAddr with a valid function pointer so that the loader can query function pointers to the remaining OpenXR commands supported by the API layer.
            Fill in pname:layerRequest→pname:createLayerInstance with a valid function pointer so that the loader can create the instance through the API layer call chain.

        Otherwise, it must: return XR_ERROR_INITIALIZATION_FAILED

        :param: loader_info: must be a valid pointer to a constant xr.NegotiateLoaderInfo structure.
        :param: layer_name: must be a string listing the name of an API layer which the loader is attempting to negotiate with.
        :param: api_layer_request: must be a valid pointer to a xr.NegotiateApiLayerRequest structure.
        :return: xr.Result.SUCCESS or xr.Result.ERROR_INITIALIZATION_FAILED
        """
        return Result.ERROR_INITIALIZATION_FAILED


__all__ = [
    "DynamicApiLayerBase",
]
