import xr

# TODO: finish initial api call around line 350 of
# https://github.com/jherico/OpenXR-Samples/blob/master/src/examples/sdl2_gl_single_file_example_c.cpp

props = xr.enumerate_instance_extension_properties()
print(len(props))
for p in props:
    print(p.extension_name)
