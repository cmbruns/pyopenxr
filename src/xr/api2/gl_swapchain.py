from ctypes import byref, cast, POINTER
from typing import Dict

from OpenGL import GL

import xr
from .glfw_context import *


class GLSwapchainFramebuffer(object):
    def __init__(
            self,
            context: IGLContext,
    ):
        self.context = context
        self.context.make_current()
        self.framebuffer = GL.glGenFramebuffers(1)
        self._color_to_depth_map: Dict[int, int] = {}

    def __enter__(self):
        return self

    def __exit__(self, _exc_type, _exc_val, _exc_tb):
        self.destroy()

    def begin_frame(self, layer_view, color_texture):
        self.context.make_current()
        GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, self.framebuffer)
        GL.glViewport(layer_view.sub_image.image_rect.offset.x,
                      layer_view.sub_image.image_rect.offset.y,
                      layer_view.sub_image.image_rect.extent.width,
                      layer_view.sub_image.image_rect.extent.height)
        depth_texture = self.get_depth_texture(color_texture)
        GL.glFramebufferTexture2D(GL.GL_FRAMEBUFFER, GL.GL_COLOR_ATTACHMENT0, GL.GL_TEXTURE_2D, color_texture, 0)
        GL.glFramebufferTexture2D(GL.GL_FRAMEBUFFER, GL.GL_DEPTH_ATTACHMENT, GL.GL_TEXTURE_2D, depth_texture, 0)

    def destroy(self):
        self.context.make_current()
        GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, 0)
        if self.framebuffer is not None:
            GL.glDeleteFramebuffers(1, [self.framebuffer, ])
            self.framebuffer = None
        self.context = None

    @staticmethod
    def end_frame():
        GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, 0)

    def get_depth_texture(self, color_texture) -> int:
        # If a depth-stencil view has already been created for this back-buffer, use it.
        if color_texture in self._color_to_depth_map:
            return self._color_to_depth_map[color_texture]
        # This back-buffer has no corresponding depth-stencil texture, so create one with matching dimensions.
        GL.glBindTexture(GL.GL_TEXTURE_2D, color_texture)
        width = GL.glGetTexLevelParameteriv(GL.GL_TEXTURE_2D, 0, GL.GL_TEXTURE_WIDTH)
        height = GL.glGetTexLevelParameteriv(GL.GL_TEXTURE_2D, 0, GL.GL_TEXTURE_HEIGHT)

        depth_texture = GL.glGenTextures(1)
        GL.glBindTexture(GL.GL_TEXTURE_2D, depth_texture)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_NEAREST)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_NEAREST)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_CLAMP_TO_EDGE)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_CLAMP_TO_EDGE)
        GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_DEPTH_COMPONENT32, width, height, 0, GL.GL_DEPTH_COMPONENT,
                        GL.GL_FLOAT, None)
        self._color_to_depth_map[color_texture] = depth_texture
        return depth_texture

    @staticmethod
    def select_color_swapchain_format(runtime_formats):
        # List of supported color swapchain formats.
        supported_color_swapchain_formats = [
            GL.GL_RGB10_A2,
            GL.GL_RGBA16F,
            # The two below should only be used as a fallback, as they are linear color formats without enough bits for color
            # depth, thus leading to banding.
            GL.GL_RGBA8,
            GL.GL_RGBA8_SNORM,
            #
            GL.GL_SRGB8,  # Linux SteamVR beta 1.24.2 has only these...
            GL.GL_SRGB8_ALPHA8,
        ]
        for rf in runtime_formats:
            for sf in supported_color_swapchain_formats:
                if rf == sf:
                    return sf
        raise RuntimeError("No runtime swapchain format supported for color swapchain")

    @property
    def swapchain_image_type(self):
        return xr.SwapchainImageOpenGLKHR


class Swapchain(object):
    def __init__(self, swapchain: xr.Swapchain, width: int, height: int):
        self.handle = swapchain
        self.width = width
        self.height = height


class XrSwapchains(object):
    """
    Maybe no GL calls inside this class...?
    """
    def __init__(
            self,
            instance: xr.Instance,
            system_id: xr.SystemId,
            session: xr.Session,
            context: IGLContext,
            view_configuration_type: xr.ViewConfigurationType,
    ):
        self.session = session
        self.view_configuration_type = view_configuration_type
        self.context = context
        self.framebuffer = GLSwapchainFramebuffer(context=self.context)
        self.render_layers = []
        self.app_space = xr.create_reference_space(
            session=session,
            create_info=xr.ReferenceSpaceCreateInfo(
                reference_space_type=xr.ReferenceSpaceType.LOCAL,  # right?
            ),
        )
        # Create swapchains
        config_views = xr.enumerate_view_configuration_views(
            instance=instance,
            system_id=system_id,
            view_configuration_type=view_configuration_type,
        )
        self.view_count = len(config_views)
        self.context.make_current()
        swapchain_formats = xr.enumerate_swapchain_formats(session)
        color_swapchain_format = self.framebuffer.select_color_swapchain_format(swapchain_formats)
        # Create a swapchain for each view.
        self.swapchains = []
        self.swapchain_image_buffers = []
        self.swapchain_image_ptr_buffers = []
        for vp in config_views:
            # Create the swapchain.
            swapchain_create_info = xr.SwapchainCreateInfo(
                array_size=1,
                format=color_swapchain_format,
                width=vp.recommended_image_rect_width,
                height=vp.recommended_image_rect_height,
                mip_count=1,
                face_count=1,
                sample_count=vp.recommended_swapchain_sample_count,
                usage_flags=xr.SwapchainUsageFlags.SAMPLED_BIT | xr.SwapchainUsageFlags.COLOR_ATTACHMENT_BIT,
            )
            swapchain = Swapchain(
                xr.create_swapchain(
                    session=session,
                    create_info=swapchain_create_info,
                ),
                swapchain_create_info.width,
                swapchain_create_info.height,
            )
            self.swapchains.append(swapchain)
            swapchain_image_buffer = xr.enumerate_swapchain_images(
                swapchain=swapchain.handle,
                element_type=self.framebuffer.swapchain_image_type,
            )
            # Keep the buffer alive by moving it into the list of buffers.
            self.swapchain_image_buffers.append(swapchain_image_buffer)
            capacity = len(swapchain_image_buffer)
            swapchain_image_ptr_buffer = (POINTER(xr.SwapchainImageBaseHeader) * capacity)()
            for ix in range(capacity):
                swapchain_image_ptr_buffer[ix] = cast(
                    byref(swapchain_image_buffer[ix]),
                    POINTER(xr.SwapchainImageBaseHeader))
            self.swapchain_image_ptr_buffers.append(swapchain_image_ptr_buffer)

    def __enter__(self):
        return self

    def __exit__(self, _exc_type, _exc_val, _exc_tb):
        self.destroy()

    def destroy(self):
        if self.framebuffer is not None:
            self.framebuffer.destroy()
        self.framebuffer = None

    def views(self, frame_state: xr.FrameState, render_layers):
        layer = xr.CompositionLayerProjection(space=self.app_space)
        projection_layer_views = (xr.CompositionLayerProjectionView * self.view_count)(
            *([xr.CompositionLayerProjectionView() for _ in range(self.view_count)])
        )
        view_state, views = xr.locate_views(
            session=self.session,
            view_locate_info=xr.ViewLocateInfo(
                view_configuration_type=self.view_configuration_type,
                display_time=frame_state.predicted_display_time,
                space=self.app_space,
            )
        )
        vsf = view_state.view_state_flags
        if (vsf & xr.VIEW_STATE_POSITION_VALID_BIT == 0
                or vsf & xr.VIEW_STATE_ORIENTATION_VALID_BIT == 0):
            return  # There are no valid tracking poses for the views.
        for view_index, view in enumerate(views):
            view_swapchain = self.swapchains[view_index]
            swapchain_image_index = xr.acquire_swapchain_image(
                swapchain=view_swapchain.handle,
                acquire_info=xr.SwapchainImageAcquireInfo(),
            )
            xr.wait_swapchain_image(
                swapchain=view_swapchain.handle,
                wait_info=xr.SwapchainImageWaitInfo(timeout=xr.INFINITE_DURATION),
            )
            layer_view = projection_layer_views[view_index]
            assert layer_view.type == xr.StructureType.COMPOSITION_LAYER_PROJECTION_VIEW
            layer_view.pose = view.pose
            layer_view.fov = view.fov
            layer_view.sub_image.swapchain = view_swapchain.handle
            layer_view.sub_image.image_rect.offset[:] = [0, 0]
            layer_view.sub_image.image_rect.extent[:] = [
                view_swapchain.width, view_swapchain.height, ]
            swapchain_image_ptr = self.swapchain_image_ptr_buffers[view_index][swapchain_image_index]
            swapchain_image = cast(swapchain_image_ptr, POINTER(xr.SwapchainImageOpenGLKHR)).contents
            assert layer_view.sub_image.image_array_index == 0  # texture arrays not supported.
            color_texture = swapchain_image.image
            self.framebuffer.begin_frame(layer_view, color_texture)

            yield view

            self.framebuffer.end_frame()
            xr.release_swapchain_image(
                swapchain=view_swapchain.handle,
                release_info=xr.SwapchainImageReleaseInfo()
            )
        layer.views = projection_layer_views
        render_layers.append(byref(layer))


__all__ = [
    "XrSwapchains",
]
