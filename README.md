# pyopenxr_examples

Sample programs using the pyopenxr python AR/VR bindings from https://github.com/cmbruns/pyopenxr

1. `hello_xr.py`: This is a faithful translation into python of the hello_xr example from https://github.com/KhronosGroup/OpenXR-SDK-Source/tree/main/src/tests/hello_xr . Watch the colorful cubes attached to various spatial frames, and squeeze the controller triggers to experience an effect. This is a multi-source-file example, because the original C source also spans multiple files. <img src="https://user-images.githubusercontent.com/2649705/172025969-5cf276bd-2a6c-42a2-852a-0605fe72a716.PNG" alt="hello_xr screen shot" width="150"/>
2. `color_cube.py`: This is a one-file example showing a large cube on the floor in the center of your VR space. This example uses a high-level `xr.ContextObject` instance to help keep the example compact. <img src="https://user-images.githubusercontent.com/2649705/174684258-0f464c91-f10d-44e5-a247-f38a2c1307b5.PNG" alt="color_cube.py screen shot" width="150"/>
3. `debug_all_the_things.py`: Combines seven different ways to add logging messages to help debug `pyopenxr` programs.
4. `pink_world.py`: The simplest opengl rendering example. The whole universe is a uniform pink.
5. `track_hmd2.py` : Prints the location of the headset to the console.
6. `track_controller.py`: Prints the location of the motion controllers to the console.
7. `vive_tracker.py` : Print the locations of Vive Tracker devices. But not if they are assigned "handheld_object" role for some reason.
