import abc
import ctypes
from typing import List, Union

import xr


class Cube(ctypes.Structure):
    _fields_ = [
        ("Pose", xr.Posef),
        ("Scale", xr.Vector3f),
    ]


class IGraphicsPlugin(abc.ABC):
    """Wraps a graphics API so the main openxr program can be graphics API-independent."""

    @abc.abstractmethod
    def __enter__(self):
        pass

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Clean up graphics resources."""

    """
    AllocateSwapchainImageStructs is not implemented in python.
    Because unlike C++, we can use the swapchain_image_type property.
    """

    @abc.abstractmethod
    def get_supported_swapchain_sample_count(self, xr_view_configuration_view: xr.ViewConfigurationView) -> int:
        """
        Get recommended number of sub-data element samples in view (recommendedSwapchainSampleCount)
        if supported by the graphics plugin. A supported value otherwise.
        """

    @property
    @abc.abstractmethod
    def graphics_binding(self) -> ctypes.Structure:
        """Get the graphics binding header for session creation."""

    @abc.abstractmethod
    def initialize_device(self, instance: xr.Instance, system_id: xr.SystemId) -> None:
        """Create an instance of this graphics api for the provided instance and systemId."""

    @property
    @abc.abstractmethod
    def instance_extensions(self) -> List[str]:
        """OpenXR extensions required by this graphics API."""

    @abc.abstractmethod
    def poll_events(self) -> bool:
        """"""

    @abc.abstractmethod
    def render_view(self, layer_view: xr.CompositionLayerProjectionView, swapchain_image: xr.SwapchainImageBaseHeader,
                    swapchain_format: int, cubes: List[Cube], mirror=False):
        """Render to a swapchain image for a projection view."""

    @abc.abstractmethod
    def select_color_swapchain_format(self, runtime_formats: Union[List[int], ctypes.Array]) -> int:
        """Select the preferred swapchain format from the list of available formats."""

    @property
    @abc.abstractmethod
    def swapchain_image_type(self):
        """The type of xr swapchain image used by this graphics plugin."""

    @abc.abstractmethod
    def update_options(self, options) -> None:
        pass
