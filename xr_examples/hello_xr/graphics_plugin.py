import abc
import ctypes
from typing import Dict, List, Sequence

import xr


class Cube(ctypes.Structure):
    _fields_ = [
        ("Pose", xr.Posef),
        ("Scale", xr.Vector3f),
    ]


class SwapchainImageData(abc.ABC):
    """Per-swapchain image record.

    Mirrors Khronos SwapchainImageDataBase: owns the enumerated color images,
    the optional runtime depth swapchain (handle + enumerated depth images),
    and the color-index -> waited-depth-index association (used as a FIFO,
    like Khronos DepthSwapchainHandling::m_colorToAcquiredDepthIndices).
    Plugin subclasses provide the fallback depth texture used when no runtime
    depth swapchain is in play (mirrors GetFallbackDepthSwapchainImage).
    """

    def __init__(self, color_images, width: int, height: int, array_size: int, sample_count: int,
                 depth_swapchain: xr.Swapchain = None, depth_images=None):
        self.color_images = color_images
        self.width = width
        self.height = height
        self.array_size = array_size
        self.sample_count = sample_count
        self.depth_swapchain = depth_swapchain
        self.depth_images = depth_images
        self._color_to_depth_indices: Dict[int, int] = {}

    @property
    def depth_swapchain_enabled(self) -> bool:
        return self.depth_swapchain is not None

    def acquire_and_wait_depth_image(self, color_image_index: int) -> None:
        """Mirrors Khronos DepthSwapchainHandling::AcquireAndWaitDepthSwapchainImage."""
        if not self.depth_swapchain_enabled:
            return
        depth_image_index = xr.acquire_swapchain_image(
            swapchain=self.depth_swapchain,
            acquire_info=xr.SwapchainImageAcquireInfo(),
        )
        xr.wait_swapchain_image(
            swapchain=self.depth_swapchain,
            wait_info=xr.SwapchainImageWaitInfo(timeout=xr.INFINITE_DURATION),
        )
        self._color_to_depth_indices[color_image_index] = depth_image_index

    def release_depth_image(self) -> None:
        """Mirrors Khronos DepthSwapchainHandling::ReleaseDepthSwapchainImage."""
        if not self.depth_swapchain_enabled:
            return
        if not self._color_to_depth_indices:
            # over-releasing?
            return
        xr.release_swapchain_image(
            swapchain=self.depth_swapchain,
            release_info=xr.SwapchainImageReleaseInfo(),
        )
        # FIFO: drop the oldest color -> depth association.
        oldest_color_index = next(iter(self._color_to_depth_indices))
        del self._color_to_depth_indices[oldest_color_index]

    def get_depth_image_for_color_index(self, color_image_index: int):
        """Mirrors Khronos SwapchainImageDataBase::GetDepthImageForColorIndex."""
        if self.depth_swapchain_enabled:
            if color_image_index not in self._color_to_depth_indices:
                raise RuntimeError("No depth image waited and associated with this color image!")
            return self.depth_images[self._color_to_depth_indices[color_image_index]]
        return self.get_fallback_depth_image(color_image_index)

    @abc.abstractmethod
    def get_fallback_depth_image(self, color_image_index: int):
        """Plugin-allocated fallback depth texture for one color image.

        Mirrors Khronos SwapchainImageDataBase::GetFallbackDepthSwapchainImage.
        """

    def destroy(self) -> None:
        """Delete plugin-allocated fallback depth textures (call with GL context current)."""


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
    def select_depth_swapchain_format(self, runtime_formats: Sequence[int]) -> int:
        """Select the preferred depth swapchain format, or -1 if none is suitable.

        Mirrors Khronos SelectDepthSwapchainFormat(false, ...) — never throws.
        """

    @abc.abstractmethod
    def allocate_swapchain_image_data(
            self, color_images, color_create_info: xr.SwapchainCreateInfo) -> SwapchainImageData:
        """Allocate the per-swapchain image record (mirrors Khronos AllocateSwapchainImageData).

        The plugin owns the record (mirrors Khronos Adopt); the program keeps
        an observing reference keyed by swapchain handle.
        """

    @abc.abstractmethod
    def allocate_swapchain_image_data_with_depth_swapchain(
            self, color_images, color_create_info: xr.SwapchainCreateInfo,
            depth_swapchain: xr.Swapchain, depth_images) -> SwapchainImageData:
        """Allocate the per-swapchain image record plus runtime depth swapchain
        (mirrors Khronos AllocateSwapchainImageDataWithDepthSwapchain)."""

    @abc.abstractmethod
    def render_view(self, layer_view: xr.CompositionLayerProjectionView, color_image: xr.SwapchainImageBaseHeader,
                    depth_image: xr.SwapchainImageBaseHeader, swapchain_format: int, cubes: List[Cube], mirror=False):
        """Render to a swapchain image for a projection view.

        color_image/depth_image are the plugin's typed swapchain image structs
        (e.g. XrSwapchainImageOpenGLKHR); the depth image comes from the runtime
        depth swapchain when available, otherwise a plugin fallback depth
        texture (mirrors Khronos RenderView).
        """

    @abc.abstractmethod
    def select_color_swapchain_format(self, runtime_formats: Sequence[int]) -> int:
        """Select the preferred swapchain format from the list of available formats."""

    @property
    @abc.abstractmethod
    def swapchain_image_type(self):
        """The type of xr swapchain image used by this graphics plugin."""

    @abc.abstractmethod
    def update_options(self, options) -> None:
        pass
