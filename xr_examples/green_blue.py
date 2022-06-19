"""
pyopenxr example program green_blue.py

Different way to get similar display to the venerable gl_example.py

TODO: why are both eye views blue?
The same problem happens in hello_xr if you try difference glClearColors in each view.
"""

from ctypes import byref, c_void_p, cast, c_int32, POINTER, Structure
import time

from OpenGL import GL

import xr


class Swapchain(Structure):
    _fields_ = [
        ("handle", xr.SwapchainHandle),
        ("width", c_int32),
        ("height", c_int32),
    ]


# ContextObject is a high level pythonic class meant to keep simple cases simple.
with xr.ContextObject(
    instance_create_info=xr.InstanceCreateInfo(
        enabled_extension_names=[
            # A graphics extension is mandatory (without a headless extension)
            xr.KHR_OPENGL_ENABLE_EXTENSION_NAME,
        ],
    ),
) as context:
    #
    eye_colors = [
        (0, 1, 0, 1),  # Left eye green
        (0, 0, 1, 1),  # Right eye blue
        (1, 0, 0, 1),  # Right eye blue
    ]

    context.graphics.make_current()
    # Create swapchains
    config_views = xr.enumerate_view_configuration_views(
        instance=context.instance,
        system_id=context.system_id,
        view_configuration_type=context.view_configuration_type,
    )
    swapchain_framebuffer = GL.glGenFramebuffers(1)
    swapchain_formats = xr.enumerate_swapchain_formats(context.session)
    color_swapchain_format = context.graphics.select_color_swapchain_format(swapchain_formats)
    # Create a swapchain for each view.
    swapchains = []
    swapchain_image_buffers = []
    swapchain_image_ptr_buffers = []
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
                session=context.session,
                create_info=swapchain_create_info,
            ),
            swapchain_create_info.width,
            swapchain_create_info.height,
        )
        swapchains.append(swapchain)
        swapchain_image_buffer = xr.enumerate_swapchain_images(
            swapchain=swapchain.handle,
            element_type=context.graphics.swapchain_image_type,
        )
        # Keep the buffer alive by moving it into the list of buffers.
        swapchain_image_buffers.append(swapchain_image_buffer)
        capacity = len(swapchain_image_buffer)
        swapchain_image_ptr_buffer = (POINTER(xr.SwapchainImageBaseHeader) * capacity)()
        for ix in range(capacity):
            swapchain_image_ptr_buffer[ix] = cast(
                byref(swapchain_image_buffer[ix]),
                POINTER(xr.SwapchainImageBaseHeader))
        swapchain_image_ptr_buffers.append(swapchain_image_ptr_buffer)

    # Loop over the render frames
    for frame_index, frame_state in enumerate(context.frame_loop()):
        if frame_state.should_render:
            layer = xr.CompositionLayerProjection(space=context.space)
            projection_layer_views = [xr.CompositionLayerProjectionView()] * 2
            view_state, views = xr.locate_views(
                session=context.session,
                view_locate_info=xr.ViewLocateInfo(
                    view_configuration_type=context.view_configuration_type,
                    display_time=frame_state.predicted_display_time,
                    space=context.space,
                )
            )
            vsf = view_state.view_state_flags
            if (vsf & xr.VIEW_STATE_POSITION_VALID_BIT == 0
                    or vsf & xr.VIEW_STATE_ORIENTATION_VALID_BIT == 0):
                continue  # There are no valid tracking poses for the views.
            for view_index, view in enumerate(views):
                view_swapchain = swapchains[view_index]
                swapchain_image_index = xr.acquire_swapchain_image(
                    swapchain=view_swapchain.handle,
                    acquire_info=xr.SwapchainImageAcquireInfo(),
                )
                xr.wait_swapchain_image(
                    swapchain=view_swapchain.handle,
                    wait_info=xr.SwapchainImageWaitInfo(timeout=xr.INFINITE_DURATION),
                )
                layer_view = projection_layer_views[view_index]
                assert layer_view.structure_type == xr.StructureType.COMPOSITION_LAYER_PROJECTION_VIEW
                layer_view.pose = view.pose
                layer_view.fov = view.fov
                layer_view.sub_image.swapchain = view_swapchain.handle
                layer_view.sub_image.image_rect.offset[:] = [0, 0]
                layer_view.sub_image.image_rect.extent[:] = [
                    view_swapchain.width, view_swapchain.height, ]
                swapchain_image_ptr = swapchain_image_ptr_buffers[view_index][swapchain_image_index]
                swapchain_image = cast(swapchain_image_ptr, POINTER(xr.SwapchainImageOpenGLKHR)).contents

                assert layer_view.sub_image.image_array_index == 0  # texture arrays not supported.
                # UNUSED_PARM(swapchain_format)                    # not used in this function for now.
                context.graphics.make_current()
                GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, swapchain_framebuffer)
                GL.glViewport(layer_view.sub_image.image_rect.offset.x,
                              layer_view.sub_image.image_rect.offset.y,
                              layer_view.sub_image.image_rect.extent.width,
                              layer_view.sub_image.image_rect.extent.height)
                color_texture = swapchain_image.image
                GL.glFramebufferTexture2D(GL.GL_FRAMEBUFFER, GL.GL_COLOR_ATTACHMENT0, GL.GL_TEXTURE_2D, color_texture, 0)

                # set each eye to a different color
                GL.glClearColor(*eye_colors[view_index])
                GL.glClear(GL.GL_COLOR_BUFFER_BIT)

                GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, 0)
                xr.release_swapchain_image(
                    swapchain=view_swapchain.handle,
                    release_info=xr.SwapchainImageReleaseInfo()
                )
            layer.views = projection_layer_views
            context.render_layers.append(byref(layer))

            # Slow things down
            time.sleep(0.020)
            # Don't run forever
            if frame_index > 200:
                break
