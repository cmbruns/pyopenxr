import xr

# TODO: finish initial api call around line 350 of
# https://github.com/jherico/OpenXR-Samples/blob/master/src/examples/sdl2_gl_single_file_example_c.cpp

props = xr.enumerate_instance_extension_properties()
assert "XR_KHR_opengl_enable" in props  # TODO: where is symbol XR_KHR_OPENGL_ENABLE_EXTENSION_NAME
requested_extensions = ["XR_KHR_opengl_enable"]
