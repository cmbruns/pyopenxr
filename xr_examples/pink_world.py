"""
pyopenxr example program pink_world.py
This example renders a solid pink field to each eye.
"""

from OpenGL import GL
import xr
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
    for frame_index, frame_state in enumerate(context.frame_loop()):
        for view in context.view_loop(frame_state):
            GL.glClearColor(1, 0.7, 0.7, 1)  # pink
            GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        if frame_index > 500:  # Don't run forever
            break
