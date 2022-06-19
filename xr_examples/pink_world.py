"""
pyopenxr example program pink_world.py

This example renders a solid pink field to each eye.
"""

import time
from OpenGL import GL
import xr


# ContextObject is a high level pythonic class meant to keep simple cases simple.
with xr.ContextObject(
    instance_create_info=xr.InstanceCreateInfo(
        enabled_extension_names=[
            # A graphics extension is mandatory (without a headless extension)
            xr.KHR_OPENGL_ENABLE_EXTENSION_NAME,
        ],
    ),
) as context:
    for frame_index, (view_index, view) in enumerate(context.render_loop()):
        # set each eye to a different color (not working yet...)
        GL.glClearColor(1, 0.7, 0.7, 1)  # pink
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        # Slow things down
        time.sleep(0.010)
        # Don't run forever
        if frame_index > 2000:
            break
