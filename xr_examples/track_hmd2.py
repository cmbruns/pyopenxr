"""
pyopenxr example program track_hmd2.py

Prints the position of your head-mounted display for 30 frames.
"""

import time
import xr.utils

# ContextObject is a high level pythonic class meant to keep simple cases simple.
with xr.utils.ContextObject(
    instance_create_info=xr.InstanceCreateInfo(
        enabled_extension_names=[
            # A graphics extension is mandatory (without a headless extension)
            xr.KHR_OPENGL_ENABLE_EXTENSION_NAME,
        ],
    ),
) as context:
    # Loop over the render frames
    for frame_index, frame_state in enumerate(context.frame_loop()):
        view_state, views = xr.locate_views(
            session=context.session,
            view_locate_info=xr.ViewLocateInfo(
                view_configuration_type=context.view_configuration_type,
                display_time=frame_state.predicted_display_time,
                space=context.space,
            )
        )
        flags = xr.ViewStateFlags(view_state.view_state_flags)
        if flags & xr.ViewStateFlags.POSITION_VALID_BIT:
            view = views[xr.utils.Eye.LEFT]
            print(view.pose, flush=True)
        else:
            print("pose not valid")
        # Slow things down, especially since we are not rendering anything
        time.sleep(0.5)
        # Don't run forever
        if frame_index > 30:
            break
