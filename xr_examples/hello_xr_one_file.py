"""
File hello_xr_one_file.py

This example uses only core functions.
It is mostly only one long procedure.
The only abstraction is the SessionStateEventHandler class,
which avoids some code duplication between the core loop
and the cleanup code.
"""

from contextlib import ExitStack
import ctypes
from ctypes import byref, c_void_p, cast, POINTER, pointer, sizeof, string_at
import enum
import inspect
import logging
import sys
import time

import numpy
from OpenGL import GL
if sys.platform == "android":
    from OpenGL import GLES3
import xr
from xr.utils import Matrix4x4f, GraphicsAPI

logging.basicConfig(
    format="%(asctime)s.%(msecs)03d %(module)s %(levelname)s: %(message)s",
    datefmt='%m/%d/%y %I:%M:%S',
    level=logging.DEBUG,
)

logger = logging.getLogger("hello_xr_one_file")
logger.setLevel(logging.DEBUG)
xr_logger = logging.getLogger("xr")
xr_logger.setLevel(logging.DEBUG)

GL_ENUMS = {}
GL_NAMES = {}
for e in dir(GL):
    if e.startswith('GL_'):
        GL_ENUMS[getattr(GL, e)] = e
        GL_NAMES[e] = getattr(GL, e)


def main():
    logger.info("Starting function main...")
    extension_names = set()
    instance_create_next = None
    if sys.platform == "android":
        import android
        xr.initialize_loader_khr(xr.LoaderInitInfoAndroidKHR(
            application_vm=android.get_vm(),
            application_context=android.get_activity(),
        ))
        extension_names.add(xr.KHR_ANDROID_CREATE_INSTANCE_EXTENSION_NAME)
        instance_create_next = xr.InstanceCreateInfoAndroidKHR(
            application_vm=android.get_vm(),
            application_activity=android.get_activity(),
            next=instance_create_next,
        )
    # Log extensions and layers
    extension_properties = xr.enumerate_instance_extension_properties()
    logger.debug(f"Available Extensions ({len(extension_properties)})")
    for extension in extension_properties:
        logger.debug(
            f"  Name={extension.extension_name.decode()} SpecVersion={extension.extension_version}")
    layers = xr.enumerate_api_layer_properties()
    logger.info(f"Available Layers: ({len(layers)})")
    for layer in layers:
        logger.debug(
            f"  Name={layer.layer_name.decode()} "
            f"SpecVersion={xr.XR_CURRENT_API_VERSION} "
            f"LayerVersion={layer.layer_version} "
            f"Description={layer.description.decode()}")
        # TODO: properties for layer_name and other c_char arrays
        layer_extension_properties = xr.enumerate_instance_extension_properties(layer.layer_name.decode())
        logger.debug(f"    Available Extensions ({len(layer_extension_properties)})")
        for extension in layer_extension_properties:
            logger.debug(
                f"      Name={extension.extension_name.decode()} SpecVersion={extension.extension_version}")

    if sys.platform in ["win32", "linux"]:
        extension_names.add(xr.KHR_OPENGL_ENABLE_EXTENSION_NAME)
    else:
        assert sys.platform == "android"
        extension_names.add(xr.KHR_OPENGL_ES_ENABLE_EXTENSION_NAME)
    # Initialize OpenXR loader (android only)

    # Prepare to allow debug messages during create_instance and destroy_instance
    # by chaining messenger_create_info into "next"
    if xr.EXT_DEBUG_UTILS_EXTENSION_NAME in extension_properties:
        extension_names.add(xr.EXT_DEBUG_UTILS_EXTENSION_NAME)
        messenger_create_info = xr.DebugUtilsMessengerCreateInfoEXT(
            message_severities=xr.DebugUtilsMessageSeverityFlagsEXT.ALL,
            message_types=xr.DebugUtilsMessageTypeFlagsEXT.ALL,
            user_callback=xr_debug_callback,
            next=instance_create_next,
        )
        instance_create_next = messenger_create_info

    with ExitStack() as exit_stack:  # noqa
        # Create OpenXR instance
        instance = exit_stack.enter_context(xr.create_instance(
            create_info=xr.InstanceCreateInfo(
                next=instance_create_next,
                enabled_extension_names=list(extension_names))))
        instance_properties = xr.get_instance_properties(instance)
        logger.info(
            f"Instance RuntimeName={instance_properties.runtime_name.decode()} "
            f"RuntimeVersion={xr.Version(instance_properties.runtime_version)}")
        # messenger = None  # Redundant...
        # if xr.EXT_DEBUG_UTILS_EXTENSION_NAME in extension_properties:
        #     messenger = exit_stack.enter_context(xr.create_debug_utils_messenger_ext(
        #         instance=instance,
        #         create_info=messenger_create_info,
        #     ))
        xr.submit_debug_utils_message_ext(
            instance,
            xr.DebugUtilsMessageSeverityFlagsEXT.VERBOSE_BIT,
            xr.DebugUtilsMessageTypeFlagsEXT.GENERAL_BIT,
            xr.DebugUtilsMessengerCallbackDataEXT(
                function_name="main",
                message="Test of debug utils messenger...",
            ),
        )
        # Create system
        form_factor = xr.FormFactor.HEAD_MOUNTED_DISPLAY
        system_id = xr.get_system(instance, xr.SystemGetInfo(
            form_factor=form_factor))
        logger.debug(f"Using system {hex(system_id.value)} for form factor {str(form_factor)}")
        # blend mode
        environment_blend_mode = xr.EnvironmentBlendMode.OPAQUE
        if environment_blend_mode == xr.EnvironmentBlendMode.ADDITIVE:
            background_clear_color = (0, 0, 0, 1)  # black
        elif environment_blend_mode == xr.EnvironmentBlendMode.ALPHA_BLEND:
            background_clear_color = (0, 0, 0, 0)  # transparent black
        else:
            background_clear_color = (0.184313729, 0.309803933, 0.309803933, 1.0)  # slate grey
        # view configurations
        view_configuration_type = xr.ViewConfigurationType.PRIMARY_STEREO
        view_config_types = xr.enumerate_view_configurations(instance, system_id)
        assert len(view_config_types) > 0
        logger.info(f"Available View Configuration Types: ({len(view_config_types)})")
        for view_config_type_value in view_config_types:
            vc_type = xr.ViewConfigurationType(view_config_type_value)
            logger.debug(
                f"  View Configuration Type: {str(vc_type)} "
                f"{'(Selected)' if vc_type == view_configuration_type else ''}")
            view_config_properties = xr.get_view_configuration_properties(
                instance=instance,
                system_id=system_id,
                view_configuration_type=vc_type,
            )
            logger.debug(f"  View configuration FovMutable={bool(view_config_properties.fov_mutable)}")
            configuration_views = xr.enumerate_view_configuration_views(
                instance,
                system_id,
                view_configuration_type,
            )
            if configuration_views is None or len(configuration_views) < 1:
                logger.error(f"Empty view configuration type")
            else:
                for i, view in enumerate(configuration_views):
                    logger.debug(
                        f"    View [{i}]: Recommended Width={view.recommended_image_rect_width} "
                        f"Height={view.recommended_image_rect_height} "
                        f"SampleCount={view.recommended_swapchain_sample_count}")
                    logger.debug(
                        f"    View [{i}]:     Maximum Width={view.max_image_rect_width} "
                        f"Height={view.max_image_rect_height} "
                        f"SampleCount={view.max_swapchain_sample_count}")
            blend_modes = xr.enumerate_environment_blend_modes(instance, system_id, vc_type)
            logger.info(f"   Available Environment Blend Mode count : ({len(blend_modes)})")
            blend_mode_found = False
            for mode_value in blend_modes:
                mode = xr.EnvironmentBlendMode(mode_value)
                blend_mode_match = mode == environment_blend_mode
                logger.info(f"      Environment Blend Mode ({str(mode)}) : "
                            f"{'(Selected)' if blend_mode_match else ''}")
                blend_mode_found |= blend_mode_match
            assert blend_mode_found
        # Create OpenGL context
        if sys.platform in ["win32", "linux"]:
            # graphics requirement
            graphics_requirements = xr.get_opengl_graphics_requirements_khr(
                instance=instance,
                system_id=system_id)
            # context
            import glfw
            if not glfw.init():
                raise RuntimeError("Failed to initialize GLFW")
            # hidden, single‐buffered context
            glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
            glfw.window_hint(glfw.DOUBLEBUFFER, glfw.FALSE)
            glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
            glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 6)
            glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
            glfw.window_hint(glfw.OPENGL_DEBUG_CONTEXT, True)  # TODO: make optional
            # tiny 1×1 window just to get a context
            window = glfw.create_window(1, 1, "GLFW Window", None, None)
            if window is None:
                glfw.terminate()
                raise RuntimeError("Failed to create hidden GLFW window")
            glfw.make_context_current(window)
            major = GL.glGetIntegerv(GL.GL_MAJOR_VERSION)
            minor = GL.glGetIntegerv(GL.GL_MINOR_VERSION)
            logger.debug(f"OpenGL version {major}.{minor}")
            desired_api_version = xr.Version(major, minor, 0)
            if graphics_requirements.min_api_version_supported > desired_api_version.number():
                ms = xr.Version(graphics_requirements.min_api_version_supported).number()
                raise xr.XrException(f"Runtime does not support desired Graphics API and/or version {hex(ms)}")
            # graphics binding
            if sys.platform == "win32":
                from OpenGL import WGL
                graphics_binding = xr.GraphicsBindingOpenGLWin32KHR(
                    h_dc=WGL.wglGetCurrentDC(),
                    h_glrc=WGL.wglGetCurrentContext(),
                )
            else:
                from OpenGL import GLX
                graphics_binding = xr.GraphicsBindingOpenGLXlibKHR(
                    x_display=GLX.glXGetCurrentDisplay(),
                    glx_context=GLX.glXGetCurrentContext(),
                    glx_drawable=GLX.glXGetCurrentDrawable(),
                )
            vertex_shader_glsl = inspect.cleandoc("""
                #version 410

                in vec3 VertexPos;
                in vec3 VertexColor;

                out vec3 PSVertexColor;

                uniform mat4 ModelViewProjection;
                uniform bool isSRGB = false;

                void main() {
                   gl_Position = ModelViewProjection * vec4(VertexPos, 1.0);
                   PSVertexColor = VertexColor;
                   if (isSRGB) PSVertexColor = sqrt(PSVertexColor);
                }
            """)
            fragment_shader_glsl = inspect.cleandoc("""
                #version 410

                in vec3 PSVertexColor;
                out vec4 FragColor;

                void main() {
                   FragColor = vec4(PSVertexColor, 1);
                }
            """)
        else:
            assert sys.platform == "android"
            graphics_requirements = xr.get_opengl_es_graphics_requirements_khr(
                instance=instance,
                system_id=system_id)
            from OpenGL import EGL
            display = EGL.eglGetDisplay(EGL.EGL_DEFAULT_DISPLAY)
            assert display != EGL.EGL_NO_DISPLAY
            major, minor = EGL.EGLint(), EGL.EGLint()
            assert EGL.eglInitialize(display, major, minor)
            config_attributes = [
                EGL.EGL_RENDERABLE_TYPE, EGL.EGL_OPENGL_ES3_BIT,
                EGL.EGL_SURFACE_TYPE, EGL.EGL_PBUFFER_BIT,
                EGL.EGL_RED_SIZE, 8, EGL.EGL_GREEN_SIZE, 8, EGL.EGL_BLUE_SIZE, 8,
                EGL.EGL_ALPHA_SIZE, 8, EGL.EGL_DEPTH_SIZE, 24,
                EGL.EGL_NONE]
            num_configs = EGL.EGLint()
            configs = (EGL.EGLConfig * 1)()
            assert EGL.eglChooseConfig(display, config_attributes, configs, 1, num_configs)
            assert num_configs.value > 0
            config = configs[0]
            pbuffer_attributes = [
                EGL.EGL_WIDTH, 1,
                EGL.EGL_HEIGHT, 1,
                EGL.EGL_NONE]
            surface = EGL.eglCreatePbufferSurface(display, config, pbuffer_attributes)
            assert surface != EGL.EGL_NO_SURFACE
            context_attributes = [
                EGL.EGL_CONTEXT_MAJOR_VERSION, 3,
                EGL.EGL_CONTEXT_MINOR_VERSION, 2,
                EGL.EGL_CONTEXT_OPENGL_DEBUG, EGL.EGL_TRUE,  # TODO: make optional
                EGL.EGL_NONE
            ]
            context = EGL.eglCreateContext(display, config, EGL.EGL_NO_CONTEXT, context_attributes)
            assert context != EGL.EGL_NO_CONTEXT
            assert EGL.eglMakeCurrent(display, surface, surface, context)
            major = GL.glGetIntegerv(GL.GL_MAJOR_VERSION)
            minor = GL.glGetIntegerv(GL.GL_MINOR_VERSION)
            logger.debug(f"OpenGLES version {major}.{minor}")
            desired_api_version = xr.Version(major, minor, 0)
            if graphics_requirements.min_api_version_supported > desired_api_version.number():
                ms = xr.Version(graphics_requirements.min_api_version_supported).number()
                raise xr.XrException(f"Runtime does not support desired Graphics API and/or version {hex(ms)}")
            # Graphics binding
            graphics_binding = xr.GraphicsBindingOpenGLESAndroidKHR(
                display=display,
                context=context,
                config=config,
            )
            vertex_shader_glsl = inspect.cleandoc("""
                #version 320 es
            
                in vec3 VertexPos;
                in vec3 VertexColor;
            
                out vec3 PSVertexColor;
            
                uniform mat4 ModelViewProjection;
                uniform bool isSRGB;
            
                void main() {
                   gl_Position = ModelViewProjection * vec4(VertexPos, 1.0);
                   PSVertexColor = VertexColor;
                   if (isSRGB) PSVertexColor = sqrt(PSVertexColor);
                }
            """)
            fragment_shader_glsl = inspect.cleandoc("""
                #version 320 es

                in lowp vec3 PSVertexColor;
                out lowp vec4 FragColor;
            
                void main() {
                   FragColor = vec4(PSVertexColor, 1);
                }
            """)
        print(f"Graphics requirements  min: {graphics_requirements.min_api_version_supported}, "
              f"max: {graphics_requirements.max_api_version_supported}")
        # OpenGL debug logging
        GL.glEnable(GL.GL_DEBUG_OUTPUT)
        # Store the debug callback function pointer, so it won't get garbage collected;
        # ...otherwise mysterious GL crashes will ensue.
        debug_message_proc = GL.GLDEBUGPROC(opengl_debug_message_callback)
        GL.glDebugMessageCallback(debug_message_proc, None)
        # GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, 73)  # bogus call for testing
        # framebuffer
        swapchain_framebuffer = GL.glGenFramebuffers(1)
        GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, swapchain_framebuffer)
        color_to_depth_map = dict()
        # shaders
        from OpenGL.GL.shaders import compileProgram, compileShader
        shader_program = compileProgram(
            compileShader(vertex_shader_glsl, GL.GL_VERTEX_SHADER),
            compileShader(fragment_shader_glsl, GL.GL_FRAGMENT_SHADER),
        )
        model_view_projection_uniform_location = GL.glGetUniformLocation(shader_program, "ModelViewProjection")
        is_rgb_location = GL.glGetUniformLocation(shader_program, "isSRGB")
        vertex_attrib_coords = GL.glGetAttribLocation(shader_program, "VertexPos")
        vertex_attrib_color = GL.glGetAttribLocation(shader_program, "VertexColor")
        # Vertices
        cube_vertex_buffer = GL.glGenBuffers(1)
        # Vertices for a 1x1x1 meter cube. (Left/Right, Top/Bottom, Front/Back)
        LBB = numpy.array([-0.5, -0.5, -0.5], dtype=numpy.float32)
        LBF = numpy.array([-0.5, -0.5, 0.5], dtype=numpy.float32)
        LTB = numpy.array([-0.5, 0.5, -0.5], dtype=numpy.float32)
        LTF = numpy.array([-0.5, 0.5, 0.5], dtype=numpy.float32)
        RBB = numpy.array([0.5, -0.5, -0.5], dtype=numpy.float32)
        RBF = numpy.array([0.5, -0.5, 0.5], dtype=numpy.float32)
        RTB = numpy.array([0.5, 0.5, -0.5], dtype=numpy.float32)
        RTF = numpy.array([0.5, 0.5, 0.5], dtype=numpy.float32)
        def cube_side(v1, v2, v3, v4, v5, v6, color):
            return numpy.array([
                [v1, color], [v2, color], [v3, color], [v4, color], [v5, color], [v6, color],
            ], dtype=numpy.float32)
        Red = numpy.array([1, 0, 0], dtype=numpy.float32)
        DarkRed = numpy.array([0.25, 0, 0], dtype=numpy.float32)
        Green = numpy.array([0, 1, 0], dtype=numpy.float32)
        DarkGreen = numpy.array([0, 0.25, 0], dtype=numpy.float32)
        Blue = numpy.array([0, 0, 1], dtype=numpy.float32)
        DarkBlue = numpy.array([0, 0, 0.25], dtype=numpy.float32)
        c_cubeVertices = numpy.array([
            cube_side(LTB, LBF, LBB, LTB, LTF, LBF, DarkRed),  # -X
            cube_side(RTB, RBB, RBF, RTB, RBF, RTF, Red),  # +X
            cube_side(LBB, LBF, RBF, LBB, RBF, RBB, DarkGreen),  # -Y
            cube_side(LTB, RTB, RTF, LTB, RTF, LTF, Green),  # +Y
            cube_side(LBB, RBB, RTB, LBB, RTB, LTB, DarkBlue),  # -Z
            cube_side(LBF, LTF, RTF, LBF, RTF, RBF, Blue),  # +Z
        ], dtype=numpy.float32)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, cube_vertex_buffer)
        GL.glBufferData(GL.GL_ARRAY_BUFFER, c_cubeVertices, GL.GL_STATIC_DRAW)
        cube_index_buffer = GL.glGenBuffers(1)
        GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, cube_index_buffer)
        # Winding order is clockwise. Each side uses a different color.
        c_cubeIndices = numpy.array([
            0, 1, 2, 3, 4, 5,  # -X
            6, 7, 8, 9, 10, 11,  # +X
            12, 13, 14, 15, 16, 17,  # -Y
            18, 19, 20, 21, 22, 23,  # +Y
            24, 25, 26, 27, 28, 29,  # -Z
            30, 31, 32, 33, 34, 35,  # +Z
        ], dtype=numpy.uint16)
        GL.glBufferData(GL.GL_ELEMENT_ARRAY_BUFFER, c_cubeIndices, GL.GL_STATIC_DRAW)
        vao = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(vao)
        GL.glEnableVertexAttribArray(vertex_attrib_coords)
        GL.glEnableVertexAttribArray(vertex_attrib_color)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, cube_vertex_buffer)
        GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, cube_index_buffer)
        class Vertex(ctypes.Structure):
            _fields_ = [
                ("position", xr.Vector3f),
                ("color", xr.Vector3f),
            ]
        GL.glVertexAttribPointer(vertex_attrib_coords, 3, GL.GL_FLOAT, False,
                                 sizeof(Vertex), cast(0, c_void_p))
        GL.glVertexAttribPointer(vertex_attrib_color, 3, GL.GL_FLOAT, False,
                                 sizeof(Vertex),
                                 cast(sizeof(xr.Vector3f), c_void_p))
        # create OpenXR session
        session = exit_stack.enter_context(xr.create_session(
            instance,
            xr.SessionCreateInfo(
                system_id=system_id,
                next=graphics_binding,
            ),
        ))
        # log reference spaces
        spaces = xr.enumerate_reference_spaces(session)
        logger.info(f"Available reference spaces: {len(spaces)}")
        for space in spaces:
            logger.debug(f"  Name: {str(xr.ReferenceSpaceType(space))}")
        # action set
        action_set = exit_stack.enter_context(xr.create_action_set(
            instance=instance,
            create_info=xr.ActionSetCreateInfo(
                action_set_name="gameplay",
                localized_action_set_name="Gameplay",
                priority=0,
            ),
        ))
        # Actions
        hand_scale = [1.0, 1.0]
        hand_subaction_path = [
            xr.string_to_path(instance, "/user/hand/left"),
            xr.string_to_path(instance, "/user/hand/right"),
        ]
        # Create actions
        # Create an input action for grabbing objects with the left and right hands.
        grab_action = xr.create_action(
            action_set=action_set,
            create_info=xr.ActionCreateInfo(
                action_type=xr.ActionType.FLOAT_INPUT,
                action_name="grab_object",
                localized_action_name="Grab Object",
                count_subaction_paths=len(hand_subaction_path),
                subaction_paths=hand_subaction_path,
            ),
        )
        # Create an input action getting the left and right hand poses.
        pose_action = xr.create_action(
            action_set=action_set,
            create_info=xr.ActionCreateInfo(
                action_type=xr.ActionType.POSE_INPUT,
                action_name="hand_pose",
                localized_action_name="Hand Pose",
                count_subaction_paths=len(hand_subaction_path),
                subaction_paths=hand_subaction_path,
            ),
        )
        # Create output actions for vibrating the left and right controller.
        vibrate_action = xr.create_action(
            action_set=action_set,
            create_info=xr.ActionCreateInfo(
                action_type=xr.ActionType.VIBRATION_OUTPUT,
                action_name="vibrate_hand",
                localized_action_name="Vibrate Hand",
                count_subaction_paths=len(hand_subaction_path),
                subaction_paths=hand_subaction_path,
            ),
        )
        # Create input actions for quitting the session using the left and right controller.
        # Since it doesn't matter which hand did this, we do not specify subaction paths for it.
        # We will just suggest bindings for both hands, where possible.
        quit_action = xr.create_action(
            action_set=action_set,
            create_info=xr.ActionCreateInfo(
                action_type=xr.ActionType.BOOLEAN_INPUT,
                action_name="quit_session",
                localized_action_name="Quit Session",
                count_subaction_paths=0,
                subaction_paths=None,
            ),
        )
        select_path = [
            xr.string_to_path(instance, "/user/hand/left/input/select/click"),
            xr.string_to_path(instance, "/user/hand/right/input/select/click")]
        _squeeze_value_path = [
            xr.string_to_path(instance, "/user/hand/left/input/squeeze/value"),
            xr.string_to_path(instance, "/user/hand/right/input/squeeze/value")]
        _squeeze_force_path = [
            xr.string_to_path(instance, "/user/hand/left/input/squeeze/force"),
            xr.string_to_path(instance, "/user/hand/right/input/squeeze/force")]
        _squeeze_click_path = [
            xr.string_to_path(instance, "/user/hand/left/input/squeeze/click"),
            xr.string_to_path(instance, "/user/hand/right/input/squeeze/click")]
        pose_path = [
            xr.string_to_path(instance, "/user/hand/left/input/grip/pose"),
            xr.string_to_path(instance, "/user/hand/right/input/grip/pose")]
        haptic_path = [
            xr.string_to_path(instance, "/user/hand/left/output/haptic"),
            xr.string_to_path(instance, "/user/hand/right/output/haptic")]
        menu_click_path = [
            xr.string_to_path(instance, "/user/hand/left/input/menu/click"),
            xr.string_to_path(instance, "/user/hand/right/input/menu/click")]
        _b_click_path = [
            xr.string_to_path(instance, "/user/hand/left/input/b/click"),
            xr.string_to_path(instance, "/user/hand/right/input/b/click")]
        squeeze_value_path = [
            xr.string_to_path(instance, "/user/hand/left/input/squeeze/value"),
            xr.string_to_path(instance, "/user/hand/right/input/squeeze/value")]
        trigger_value_path = [
            xr.string_to_path(instance, "/user/hand/left/input/trigger/value"),
            xr.string_to_path(instance, "/user/hand/right/input/trigger/value")]
        # Suggest bindings for KHR Simple.

        class Side(enum.IntEnum):
            LEFT = 0
            RIGHT = 1

        khr_bindings = [
            # Fall back to a click input for the grab action.
            xr.ActionSuggestedBinding(grab_action, select_path[Side.LEFT]),
            xr.ActionSuggestedBinding(grab_action, select_path[Side.RIGHT]),
            xr.ActionSuggestedBinding(pose_action, pose_path[Side.LEFT]),
            xr.ActionSuggestedBinding(pose_action, pose_path[Side.RIGHT]),
            xr.ActionSuggestedBinding(quit_action, menu_click_path[Side.LEFT]),
            xr.ActionSuggestedBinding(quit_action, menu_click_path[Side.RIGHT]),
            xr.ActionSuggestedBinding(vibrate_action, haptic_path[Side.LEFT]),
            xr.ActionSuggestedBinding(vibrate_action, haptic_path[Side.RIGHT]),
        ]
        xr.suggest_interaction_profile_bindings(
            instance=instance,
            suggested_bindings=xr.InteractionProfileSuggestedBinding(
                interaction_profile=xr.string_to_path(
                    instance,
                    "/interaction_profiles/khr/simple_controller",
                ),
                count_suggested_bindings=len(khr_bindings),
                suggested_bindings=(xr.ActionSuggestedBinding * len(khr_bindings))(*khr_bindings),
            ),
        )
        # Suggest bindings for the Vive Controller.
        vive_bindings = [
            xr.ActionSuggestedBinding(grab_action, trigger_value_path[Side.LEFT]),
            xr.ActionSuggestedBinding(grab_action, trigger_value_path[Side.RIGHT]),
            xr.ActionSuggestedBinding(pose_action, pose_path[Side.LEFT]),
            xr.ActionSuggestedBinding(pose_action, pose_path[Side.RIGHT]),
            xr.ActionSuggestedBinding(quit_action, menu_click_path[Side.LEFT]),
            xr.ActionSuggestedBinding(quit_action, menu_click_path[Side.RIGHT]),
            xr.ActionSuggestedBinding(vibrate_action, haptic_path[Side.LEFT]),
            xr.ActionSuggestedBinding(vibrate_action, haptic_path[Side.RIGHT]),
        ]
        xr.suggest_interaction_profile_bindings(
            instance=instance,
            suggested_bindings=xr.InteractionProfileSuggestedBinding(
                interaction_profile=xr.string_to_path(
                    instance,
                    "/interaction_profiles/htc/vive_controller",
                ),
                count_suggested_bindings=len(vive_bindings),
                suggested_bindings=(xr.ActionSuggestedBinding * len(vive_bindings))(*vive_bindings),
            ),
        )
        # Suggest bindings for the Oculus Touch.
        touch_bindings = [
            xr.ActionSuggestedBinding(grab_action, squeeze_value_path[Side.LEFT]),
            xr.ActionSuggestedBinding(grab_action, squeeze_value_path[Side.RIGHT]),
            xr.ActionSuggestedBinding(pose_action, pose_path[Side.LEFT]),
            xr.ActionSuggestedBinding(pose_action, pose_path[Side.RIGHT]),
            xr.ActionSuggestedBinding(quit_action, menu_click_path[Side.LEFT]),
            xr.ActionSuggestedBinding(quit_action, menu_click_path[Side.RIGHT]),
            xr.ActionSuggestedBinding(vibrate_action, haptic_path[Side.LEFT]),
            xr.ActionSuggestedBinding(vibrate_action, haptic_path[Side.RIGHT]),
        ]
        try:
            xr.suggest_interaction_profile_bindings(
                instance=instance,
                suggested_bindings=xr.InteractionProfileSuggestedBinding(
                    interaction_profile=xr.string_to_path(
                        instance,
                        "/interaction_profiles/oculus/touch_controller",
                    ),
                    count_suggested_bindings=len(touch_bindings),
                    suggested_bindings=(xr.ActionSuggestedBinding * len(touch_bindings))(*touch_bindings),
                ),
            )
        except xr.PathUnsupportedError:
            pass
        # TODO: the other controller types in openxr_programs.cpp

        hand_space = [
            xr.create_action_space(session, xr.ActionSpaceCreateInfo(
                action=pose_action,
                subaction_path=hand_subaction_path[Side.LEFT],
            )),
            xr.create_action_space(session, xr.ActionSpaceCreateInfo(
                action=pose_action,
                subaction_path=hand_subaction_path[Side.RIGHT],
            )),
        ]
        xr.attach_session_action_sets(
            session=session,
            attach_info=xr.SessionActionSetsAttachInfo(
                count_action_sets=1,
                action_sets=pointer(action_set),
            ),
        )
        # spaces
        visualized_spaces = [
            # ViewFront
            xr.create_reference_space(session, xr.ReferenceSpaceCreateInfo(
                # TODO: property for Vector3f conversion
                pose_in_reference_space=xr.Posef(position=xr.Vector3f(0, 0, -2)),
                reference_space_type=xr.ReferenceSpaceType.VIEW,
            )),
            # Local
            xr.create_reference_space(session, xr.ReferenceSpaceCreateInfo(
                reference_space_type=xr.ReferenceSpaceType.LOCAL,
            )),
            # Stage
            xr.create_reference_space(session, xr.ReferenceSpaceCreateInfo(
                reference_space_type=xr.ReferenceSpaceType.STAGE,
            )),
            # StageLeft
            xr.create_reference_space(session, xr.ReferenceSpaceCreateInfo(
                pose_in_reference_space=xr.Posef(position=xr.Vector3f(-2, 0, -2)),
                reference_space_type=xr.ReferenceSpaceType.STAGE,
            )),
            # ViewFront
            xr.create_reference_space(session, xr.ReferenceSpaceCreateInfo(
                pose_in_reference_space=xr.Posef(position=xr.Vector3f(2, 0, -2)),
                reference_space_type=xr.ReferenceSpaceType.STAGE,
            )),
        ]
        app_space_type = xr.ReferenceSpaceType.STAGE  # TODO: parse option
        app_space = exit_stack.enter_context(xr.create_reference_space(
            session,
            xr.ReferenceSpaceCreateInfo(app_space_type)
        ))
        # swapchains
        # Read graphics properties for preferred swapchain length and logging.
        system_properties = xr.get_system_properties(instance, system_id)
        # Log system properties
        logger.info("System Properties: "
                    f"Name={system_properties.system_name.decode()} "
                    f"VendorId={system_properties.vendor_id}")
        logger.info("System Graphics Properties: "
                    f"MaxWidth={system_properties.graphics_properties.max_swapchain_image_width} "
                    f"MaxHeight={system_properties.graphics_properties.max_swapchain_image_height} "
                    f"MaxLayers={system_properties.graphics_properties.max_layer_count}")
        logger.info("System Tracking Properties: "
                    f"OrientationTracking={bool(system_properties.tracking_properties.orientation_tracking)} "
                    f"PositionTracking={bool(system_properties.tracking_properties.position_tracking)}")
        # Note: No other view configurations exist at the time this (C++) code was written. If this
        # condition is not met, the project will need to be audited to see how support should be
        # added.
        if view_configuration_type != xr.ViewConfigurationType.PRIMARY_STEREO:
            raise RuntimeError("Unsupported view configuration type")
        color_swapchain_format = None
        swapchain_formats = xr.enumerate_swapchain_formats(session)
        is_srgb = False
        for sf in [
            GL.GL_RGB10_A2,
            GL.GL_RGBA16F,
            GL.GL_RGBA16,
            GL.GL_RGBA8,
            GL.GL_RGBA8_SNORM,
            GL.GL_SRGB8_ALPHA8,
            GL.GL_SRGB8,
        ]:
            if sf in swapchain_formats:
                color_swapchain_format = sf
                if "SRGB" in str(sf):
                    is_srgb = True
                break
        print(is_srgb)
        assert color_swapchain_format is not None
        # Print swapchain formats and the selected one.
        formats_string = ""
        for sc_format in swapchain_formats:
            selected = sc_format == color_swapchain_format
            formats_string += " "
            if selected:
                formats_string += "["
                formats_string += f"{str(color_swapchain_format)}({sc_format})"
                formats_string += "]"
            else:
                try:
                    formats_string += f"{GL_ENUMS[sc_format]}({sc_format})"
                except KeyError:
                    formats_string += f"{sc_format}"
        logger.debug(f"Swapchain Formats: {formats_string}")
        # create a swapchain for each view
        swapchains = []
        swapchain_images = []
        swapchain_sizes = []
        swapchain_image_ptr_buffers = []
        # views (usually two: one for the left eye; one for the right)
        config_views = xr.enumerate_view_configuration_views(
            instance=instance,
            system_id=system_id,
            view_configuration_type=view_configuration_type,
        )
        for v in config_views:
            swapchains.append(xr.create_swapchain(session, xr.SwapchainCreateInfo(
                array_size=1,
                format=color_swapchain_format,
                width=v.recommended_image_rect_width,
                height=v.recommended_image_rect_height,
                mip_count=1,
                face_count=1,
                sample_count=1,
                usage_flags=xr.SwapchainUsageFlags.SAMPLED_BIT | xr.SwapchainUsageFlags.COLOR_ATTACHMENT_BIT,
            )))
            swapchain_images.append(xr.enumerate_swapchain_images(
                swapchain=swapchains[-1], element_type=xr.SwapchainImageOpenGLESKHR))
            swapchain_sizes.append((v.recommended_image_rect_width, v.recommended_image_rect_height))
            num_images = len(swapchain_images[-1])
            swapchain_image_ptr_buffer = (POINTER(xr.SwapchainImageBaseHeader) * num_images)()
            for ix in range(num_images):
                swapchain_image_ptr_buffer[ix] = cast(
                    byref(swapchain_images[-1][ix]),
                    POINTER(xr.SwapchainImageBaseHeader))
            swapchain_image_ptr_buffers.append(swapchain_image_ptr_buffer)
        # begin frame/render loop
        session_state_event_handler = SessionStateEventHandler(session, view_configuration_type)
        # for _ in range(1000):
        while True:
            # TODO: poll android events
            # Poll session state events
            while True:
                try:
                    event_buffer = xr.poll_event(instance)
                    session_state_event_handler.handle_event(event_buffer)
                except xr.EventUnavailable:
                    break
            if session_state_event_handler.exit_render_loop:
                break
            if (session_state_event_handler.session_is_running and
                session_state_event_handler.session_state in (
                    xr.SessionState.READY,
                    xr.SessionState.SYNCHRONIZED,
                    xr.SessionState.VISIBLE,
                    xr.SessionState.FOCUSED,
                        )):
                if session_state_event_handler.session_state == xr.SessionState.FOCUSED:
                    # Sync actions
                    active_action_set = xr.ActiveActionSet(action_set, xr.NULL_PATH)
                    xr.sync_actions(
                        session,
                        xr.ActionsSyncInfo(
                            count_active_action_sets=1,
                            active_action_sets=pointer(active_action_set)
                        ),
                    )
                    # Get pose and grab action state and start haptic vibrate when hand is 90% squeezed.
                    for hand in Side:
                        grab_value = xr.get_action_state_float(
                            session,
                            xr.ActionStateGetInfo(
                                action=grab_action,
                                subaction_path=hand_subaction_path[hand],
                            ),
                        )
                        if grab_value.is_active:
                            # Scale the rendered hand by 1.0f (open) to 0.5f (fully squeezed).
                            hand_scale[hand] = 1 - 0.5 * grab_value.current_state
                            if grab_value.current_state > 0.9:
                                vibration = xr.HapticVibration(
                                    amplitude=0.5,
                                    duration=xr.MIN_HAPTIC_DURATION,
                                    frequency=xr.FREQUENCY_UNSPECIFIED,
                                )
                                xr.apply_haptic_feedback(
                                    session=session,
                                    haptic_action_info=xr.HapticActionInfo(
                                        action=vibrate_action,
                                        subaction_path=hand_subaction_path[hand],
                                    ),
                                    haptic_feedback=cast(byref(vibration), POINTER(xr.HapticBaseHeader)).contents,
                                )
                        pose_state = xr.get_action_state_pose(
                            session=session,
                            get_info=xr.ActionStateGetInfo(
                                action=pose_action,
                                subaction_path=hand_subaction_path[hand],
                            ),
                        )
                    # There were no subaction paths specified for the quit action, because we don't care which hand did it.
                    quit_value = xr.get_action_state_boolean(
                        session=session,
                        get_info=xr.ActionStateGetInfo(
                            action=quit_action,
                            subaction_path=xr.NULL_PATH,
                        ),
                    )
                    if quit_value.is_active and quit_value.changed_since_last_sync and quit_value.current_state:
                        xr.request_exit_session(session)
                frame_state = xr.wait_frame(session)
                xr.begin_frame(session)
                layers = []
                if frame_state.should_render:
                    layer = xr.CompositionLayerProjection(space=app_space)
                    view_state, views = xr.locate_views(session, xr.ViewLocateInfo(
                        view_configuration_type=view_configuration_type,
                        display_time=frame_state.predicted_display_time,
                        space=app_space,
                    ))
                    projection_layer_views = tuple(xr.CompositionLayerProjectionView() for _ in range(len(views)))
                    vsf = view_state.view_state_flags
                    poses_are_valid = (vsf & xr.VIEW_STATE_POSITION_VALID_BIT) and (vsf & xr.VIEW_STATE_ORIENTATION_VALID_BIT)
                    if poses_are_valid:

                        # For each locatable space that we want to visualize, render a 25cm cube.
                        cubes = []
                        for visualized_space in visualized_spaces:
                            # TODO: sometimes xr.locate_space() raises xr.exception.TimeInvalidError
                            # Maybe try skipping a few frames instead of crashing
                            space_location = xr.locate_space(
                                space=visualized_space,
                                base_space=app_space,
                                time=frame_state.predicted_display_time,
                            )
                            loc_flags = space_location.location_flags
                            if (loc_flags & xr.SPACE_LOCATION_POSITION_VALID_BIT != 0
                                    and loc_flags & xr.SPACE_LOCATION_ORIENTATION_VALID_BIT != 0):
                                cubes.append((space_location.pose, xr.Vector3f(0.25, 0.25, 0.25)))
                        # Render a 10cm cube scaled by grabAction for each hand. Note renderHand will only be
                        # true when the application has focus.
                        for hand in Side:
                            space_location = xr.locate_space(
                                space=hand_space[hand],
                                base_space=app_space,
                                time=frame_state.predicted_display_time,
                            )
                            loc_flags = space_location.location_flags
                            if (loc_flags & xr.SPACE_LOCATION_POSITION_VALID_BIT != 0
                                    and loc_flags & xr.SPACE_LOCATION_ORIENTATION_VALID_BIT != 0):
                                scale = 0.1 * hand_scale[hand]
                                cubes.append((space_location.pose, xr.Vector3f(scale, scale, scale)))

                        for view_index, view in enumerate(views):
                            assert GL.glGetError() == GL.GL_NO_ERROR
                            swapchain = swapchains[view_index]
                            swapchain_image_index = xr.acquire_swapchain_image(
                                swapchain=swapchain,
                                acquire_info=xr.SwapchainImageAcquireInfo(),
                            )
                            xr.wait_swapchain_image(
                                swapchain=swapchain,
                                wait_info=xr.SwapchainImageWaitInfo(timeout=xr.INFINITE_DURATION),
                            )
                            layer_view = projection_layer_views[view_index]
                            assert layer_view.type == xr.StructureType.COMPOSITION_LAYER_PROJECTION_VIEW
                            layer_view.pose = view.pose
                            layer_view.fov = view.fov
                            layer_view.sub_image.swapchain = swapchain
                            layer_view.sub_image.image_rect.offset[:] = [0, 0]
                            layer_view.sub_image.image_rect.extent[:] = [*swapchain_sizes[view_index]]
                            swapchain_image_ptr = swapchain_image_ptr_buffers[view_index][swapchain_image_index]
                            swapchain_image = cast(swapchain_image_ptr, POINTER(xr.SwapchainImageOpenGLESKHR)).contents
                            assert layer_view.sub_image.image_array_index == 0  # texture arrays not supported.
                            color_texture = swapchain_image.image
                            # graphics begin frame
                            GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, swapchain_framebuffer)
                            GL.glViewport(layer_view.sub_image.image_rect.offset.x,
                                          layer_view.sub_image.image_rect.offset.y,
                                          layer_view.sub_image.image_rect.extent.width,
                                          layer_view.sub_image.image_rect.extent.height)
                            if color_texture in color_to_depth_map:
                                depth_texture = color_to_depth_map[color_texture]
                            else:
                                GL.glBindTexture(GL.GL_TEXTURE_2D, color_texture)
                                width = GL.glGetTexLevelParameteriv(GL.GL_TEXTURE_2D, 0, GL.GL_TEXTURE_WIDTH)
                                height = GL.glGetTexLevelParameteriv(GL.GL_TEXTURE_2D, 0, GL.GL_TEXTURE_HEIGHT)
                                depth_texture = GL.glGenTextures(1)
                                GL.glBindTexture(GL.GL_TEXTURE_2D, depth_texture)
                                GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_NEAREST)
                                GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_NEAREST)
                                GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_CLAMP_TO_EDGE)
                                GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_CLAMP_TO_EDGE)
                                if sys.platform == "android":  # or OpenGLES really
                                    depth_component = GL.GL_DEPTH_COMPONENT24
                                else:
                                    depth_component = GL.GL_DEPTH_COMPONENT32
                                GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, depth_component, width, height, 0,
                                                GL.GL_DEPTH_COMPONENT, GL.GL_UNSIGNED_INT, None)
                                color_to_depth_map[color_texture] = depth_texture
                            GL.glFramebufferTexture2D(GL.GL_FRAMEBUFFER, GL.GL_COLOR_ATTACHMENT0, GL.GL_TEXTURE_2D,
                                                      color_texture, 0)
                            GL.glFramebufferTexture2D(GL.GL_FRAMEBUFFER, GL.GL_DEPTH_ATTACHMENT, GL.GL_TEXTURE_2D,
                                                      depth_texture, 0)

                            # Render scene
                            GL.glFrontFace(GL.GL_CW)
                            GL.glCullFace(GL.GL_BACK)
                            GL.glEnable(GL.GL_CULL_FACE)
                            GL.glEnable(GL.GL_DEPTH_TEST)
                            # SRGB swapchain format correction
                            bg_col = background_clear_color
                            if (is_srgb):
                                bg_col = [c ** 0.5 for c in background_clear_color]
                            GL.glClearColor(*bg_col)
                            if sys.platform == "android":
                                GLES3.glClearDepthf(1.0)
                            else:
                                GL.glClearDepth(1.0)
                            GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT | GL.GL_STENCIL_BUFFER_BIT)
                            GL.glUseProgram(shader_program)
                            pose = layer_view.pose
                            proj = Matrix4x4f.create_projection_fov(GraphicsAPI.OPENGL, layer_view.fov, 0.05, 100.0)
                            scale = xr.Vector3f(1, 1, 1)
                            to_view = Matrix4x4f.create_translation_rotation_scale(pose.position, pose.orientation,
                                                                                   scale)
                            view = Matrix4x4f.invert_rigid_body(to_view)
                            vp = proj @ view
                            # Set cube primitive data.
                            GL.glBindVertexArray(vao)
                            # Render each cube
                            for cube in cubes:
                                # Compute the model-view-projection transform and set it.
                                pose, scale = cube
                                model = Matrix4x4f.create_translation_rotation_scale(pose.position,
                                                                                     pose.orientation, scale)
                                mvp = vp @ model
                                GL.glUniformMatrix4fv(model_view_projection_uniform_location, 1, True,
                                                      mvp.as_numpy())
                                GL.glUniform1i(is_rgb_location, True)
                                # Draw the cube.
                                GL.glDrawElements(GL.GL_TRIANGLES, len(c_cubeIndices), GL.GL_UNSIGNED_SHORT, None)

                            GL.glBindVertexArray(0)
                            GL.glUseProgram(0)

                            # end frame
                            GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, 0)
                            xr.release_swapchain_image(
                                swapchain=swapchain,
                                release_info=xr.SwapchainImageReleaseInfo())
                        layer.views = projection_layer_views
                        layers.append(byref(layer))
                assert GL.glGetError() == GL.GL_NO_ERROR  # Prepare to avoid Linux SteamVR bug
                xr.end_frame(session, xr.FrameEndInfo(
                    display_time=frame_state.predicted_display_time,
                    environment_blend_mode=environment_blend_mode,
                    layers=layers,
                ))
                GL.glGetError()  # Clear GL error state to avoid Linux SteamVR bug
            else:
                # throttle loop since xr.wait_frame() won't be called
                time.sleep(0.250)
        # end of frame loop
        # wind down session state
        try:
            xr.request_exit_session(session)
        except xr.SessionNotRunningError:
            pass
        for _ in range(20):
            while True:
                try:
                    event_buffer = xr.poll_event(instance)
                    session_state_event_handler.handle_event(event_buffer)
                except xr.EventUnavailable:
                    break
            if session_state_event_handler.exit_render_loop:
                break
            if (session_state_event_handler.session_is_running and
                    session_state_event_handler.session_state in (
                            xr.SessionState.READY,
                            xr.SessionState.SYNCHRONIZED,
                            xr.SessionState.VISIBLE,
                            xr.SessionState.FOCUSED,
                    )):
                frame_state = xr.wait_frame(session)
                xr.begin_frame(session)
                time.sleep(0.050)  # Yield time for other subsystems
                xr.end_frame(
                    session,
                    frame_end_info=xr.FrameEndInfo(
                        display_time=frame_state.predicted_display_time,
                        environment_blend_mode=environment_blend_mode,
                        layers=[],
                    )
                )
        # TODO: destroy objects not destroyed by exit_stack...


class SessionStateEventHandler:
    def __init__(self, session, view_configuration_type: xr.ViewConfigurationType):
        self.session = session
        self.view_configuration_type = view_configuration_type
        self.exit_render_loop = False
        self.request_restart = False
        self.session_state = xr.SessionState.IDLE
        self.session_is_running = False

    def handle_event(self, event_buffer: xr.EventDataBuffer):
        event_type = xr.StructureType(event_buffer.type)
        if event_type == xr.StructureType.EVENT_DATA_INSTANCE_LOSS_PENDING:
            self.exit_render_loop = True
            self.request_restart = True
        elif event_type == xr.StructureType.EVENT_DATA_SESSION_STATE_CHANGED:
            event = cast(
                byref(event_buffer),
                POINTER(xr.EventDataSessionStateChanged)
            ).contents
            self.session_state = xr.SessionState(event.state)
            print(f"OpenXR session state changed to {self.session_state.name}")
            if self.session_state == xr.SessionState.READY:
                xr.begin_session(
                    session=self.session,
                    begin_info=xr.SessionBeginInfo(self.view_configuration_type)
                )
                self.session_is_running = True
            elif self.session_state == xr.SessionState.STOPPING:
                self.session_is_running = False
                xr.end_session(self.session)
            elif self.session_state in (xr.SessionState.EXITING, xr.SessionState.LOSS_PENDING):
                self.exit_render_loop = True
                self.request_restart = (self.session_state == xr.SessionState.LOSS_PENDING)


def xr_debug_callback(
        severity: xr.DebugUtilsMessageSeverityFlagsEXT,
        type_flags: xr.DebugUtilsMessageTypeFlagsEXT,
        callback_data: xr.DebugUtilsMessengerCallbackDataEXT,
        _user_data: c_void_p,
) -> bool:
    if severity & xr.DEBUG_UTILS_MESSAGE_SEVERITY_ERROR_BIT_EXT:
        level = logging.ERROR
    elif severity & xr.DEBUG_UTILS_MESSAGE_SEVERITY_WARNING_BIT_EXT:
        level = logging.WARNING
    elif severity & xr.DEBUG_UTILS_MESSAGE_SEVERITY_INFO_BIT_EXT:
        level = logging.INFO
    else:
        level = logging.DEBUG
    d = callback_data
    xr_logger.log(level, f"OpenXR: {d.function_name}: {d.message}")
    return False


def opengl_debug_message_callback(source, msg_type, msg_id, severity, length, raw, _user):
    """Redirect OpenGL debug messages"""
    def fmt(enum):
        try:
            return GL_ENUMS[enum].removeprefix("GL_DEBUG_").removesuffix("_KHR").removesuffix("_ARB")
        except:
            return "(format error)"
    log_level = {
        GL.GL_DEBUG_SEVERITY_HIGH: logging.ERROR,
        GL.GL_DEBUG_SEVERITY_MEDIUM: logging.WARNING,
        GL.GL_DEBUG_SEVERITY_LOW: logging.INFO,
        GL.GL_DEBUG_SEVERITY_NOTIFICATION: logging.DEBUG,
    }.get(severity, logging.INFO)
    msg = f"OpenGL ({msg_id}): {fmt(msg_type)} {fmt(source)} {string_at(raw, length).decode()}"
    logger.log(log_level, msg)


if __name__ == "__main__":
    main()
