from ctypes import byref, c_void_p, cast, sizeof, POINTER, Structure
import inspect
import logging
import platform
from typing import Dict, List, Optional

import numpy
from OpenGL import GL

from .graphics_plugin import Cube, IGraphicsPlugin

if platform.system() == "Windows":
    from OpenGL import WGL
elif platform.system() == "Linux":
    from OpenGL import GLX
import glfw

import xr

from .geometry import c_cubeVertices, c_cubeIndices, Vertex
from .linear import GraphicsAPI, Matrix4x4f
from .options import Options

logger = logging.getLogger("hello_xr.graphics_plugin_opengl")


dark_slate_gray = numpy.array([0.184313729, 0.309803933, 0.309803933, 1.0], dtype=numpy.float32)

vertex_shader_glsl = inspect.cleandoc("""
    #version 410

    in vec3 VertexPos;
    in vec3 VertexColor;

    out vec3 PSVertexColor;

    uniform mat4 ModelViewProjection;

    void main() {
       gl_Position = ModelViewProjection * vec4(VertexPos, 1.0);
       PSVertexColor = VertexColor;
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


class OpenGLGraphicsPlugin(IGraphicsPlugin):
    def __init__(self, options: Options):
        super().__init__()
        self.window = None

        self.background_clear_color = options.background_clear_color
        if platform.system() == "Windows":
            self._graphics_binding = xr.GraphicsBindingOpenGLWin32KHR()
        elif platform.system() == "Linux":
            # TODO more nuance on Linux: Xlib, Xcb, Wayland
            self._graphics_binding = xr.GraphicsBindingOpenGLXlibKHR()
        self.swapchain_image_buffers: List[xr.SwapchainImageOpenGLKHR] = []  # To keep the swapchain images alive
        self.swapchain_framebuffer: Optional[int] = None
        self.program = None
        self.model_view_projection_uniform_location = 0
        self.vertex_attrib_coords = 0
        self.vertex_attrib_color = 0
        self.vao = None
        self.cube_vertex_buffer = None
        self.cube_index_buffer = None
        # Map color buffer to associated depth buffer. This map is populated on demand.
        self.color_to_depth_map: Dict[int, int] = {}
        self.debug_message_proc = None  # To keep the callback alive

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.window:
            glfw.make_context_current(self.window)
        if self.swapchain_framebuffer is not None:
            GL.glDeleteFramebuffers(1, [self.swapchain_framebuffer])
        if self.program is not None:
            GL.glDeleteProgram(self.program)
        if self.vao is not None:
            GL.glDeleteVertexArrays(1, [self.vao])
        if self.cube_vertex_buffer is not None:
            GL.glDeleteBuffers(1, [self.cube_vertex_buffer])
        if self.cube_index_buffer is not None:
            GL.glDeleteBuffers(1, [self.cube_index_buffer])
        self.swapchain_framebuffer = None
        self.program = None
        self.vao = None
        self.cube_vertex_buffer = None
        self.cube_index_buffer = None
        for color, depth in self.color_to_depth_map.items():
            if depth is not None:
                GL.glDeleteTextures(1, [depth])
        self.color_to_depth_map = {}
        if self.window is not None:
            glfw.destroy_window(self.window)
            self.window = None
        glfw.terminate()

    @staticmethod
    def check_shader(shader):
        result = GL.glGetShaderiv(shader, GL.GL_COMPILE_STATUS)
        if not result:
            raise RuntimeError(f"Compile shader failed: {GL.glGetShaderInfoLog(shader)}")

    @staticmethod
    def check_program(prog):
        result = GL.glGetProgramiv(prog, GL.GL_LINK_STATUS)
        if not result:
            raise RuntimeError(f"Link program failed: {GL.glGetProgramInfoLog(prog)}")

    @staticmethod
    def opengl_debug_message_callback(_source, _msg_type, _msg_id, severity, length, raw, _user):
        """Redirect OpenGL debug messages"""
        log_level = {
            GL.GL_DEBUG_SEVERITY_HIGH: logging.ERROR,
            GL.GL_DEBUG_SEVERITY_MEDIUM: logging.WARNING,
            GL.GL_DEBUG_SEVERITY_LOW: logging.INFO,
            GL.GL_DEBUG_SEVERITY_NOTIFICATION: logging.DEBUG,
        }[severity]
        logger.log(log_level, f"OpenGL Message: {raw[0:length].decode()}")

    def focus_window(self):
        glfw.focus_window(self.window)
        glfw.make_context_current(self.window)

    def get_depth_texture(self, color_texture) -> int:
        # If a depth-stencil view has already been created for this back-buffer, use it.
        if color_texture in self.color_to_depth_map:
            return self.color_to_depth_map[color_texture]
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
        GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_DEPTH_COMPONENT32, width, height, 0, GL.GL_DEPTH_COMPONENT, GL.GL_FLOAT, None)
        self.color_to_depth_map[color_texture] = depth_texture
        return depth_texture

    def get_supported_swapchain_sample_count(self, _xr_view_configuration_view: xr.ViewConfigurationView):
        return 1

    @property
    def instance_extensions(self) -> List[str]:
        return [xr.KHR_OPENGL_ENABLE_EXTENSION_NAME]

    @property
    def swapchain_image_type(self):
        return xr.SwapchainImageOpenGLKHR

    @property
    def graphics_binding(self) -> Structure:
        return self._graphics_binding

    def initialize_device(self, instance: xr.Instance, system_id: xr.SystemId):
        # extension function must be loaded by name
        pfn_get_open_gl_graphics_requirements_khr = cast(
            xr.get_instance_proc_addr(
                instance,
                "xrGetOpenGLGraphicsRequirementsKHR",
            ),
            xr.PFN_xrGetOpenGLGraphicsRequirementsKHR
        )
        graphics_requirements = xr.GraphicsRequirementsOpenGLKHR()
        result = pfn_get_open_gl_graphics_requirements_khr(instance, system_id, byref(graphics_requirements))
        result = xr.check_result(xr.Result(result))
        if result.is_exception():
            raise result
        # Initialize the gl extensions. Note we have to open a window.
        if not glfw.init():
            raise xr.XrException("GLFW initialization failed")
        glfw.window_hint(glfw.DOUBLEBUFFER, False)
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 5)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        self.window = glfw.create_window(640, 480, "GLFW Window", None, None)
        if self.window is None:
            raise xr.XrException("Failed to create GLFW window")
        glfw.make_context_current(self.window)
        glfw.show_window(self.window)
        glfw.swap_interval(0)
        glfw.focus_window(self.window)
        major = GL.glGetIntegerv(GL.GL_MAJOR_VERSION)
        minor = GL.glGetIntegerv(GL.GL_MINOR_VERSION)
        logger.debug(f"OpenGL version {major}.{minor}")
        desired_api_version = xr.Version(major, minor, 0)
        if graphics_requirements.min_api_version_supported > desired_api_version.number():
            ms = xr.Version(graphics_requirements.min_api_version_supported).number()
            raise xr.XrException(f"Runtime does not support desired Graphics API and/or version {hex(ms)}")
        if platform.system() == "Windows":
            self._graphics_binding.h_dc = WGL.wglGetCurrentDC()
            self._graphics_binding.h_glrc = WGL.wglGetCurrentContext()
        elif platform.system() == "Linux":
            # TODO more nuance on Linux: Xlib, Xcb, Wayland
            self._graphics_binding.x_display = GLX.glXGetCurrentDisplay()
            self._graphics_binding.glx_drawable = GLX.glXGetCurrentDrawable()
            self._graphics_binding.glx_context = GLX.glXGetCurrentContext()
        GL.glEnable(GL.GL_DEBUG_OUTPUT)
        # Store the debug callback function pointer, so it won't get garbage collected;
        # ...otherwise mysterious GL crashes will ensue.
        self.debug_message_proc = GL.GLDEBUGPROC(self.opengl_debug_message_callback)
        GL.glDebugMessageCallback(self.debug_message_proc, None)
        self.initialize_resources()

    def initialize_resources(self):
        self.swapchain_framebuffer = GL.glGenFramebuffers(1)
        vertex_shader = GL.glCreateShader(GL.GL_VERTEX_SHADER)
        GL.glShaderSource(vertex_shader, vertex_shader_glsl)
        GL.glCompileShader(vertex_shader)
        self.check_shader(vertex_shader)
        fragment_shader = GL.glCreateShader(GL.GL_FRAGMENT_SHADER)
        GL.glShaderSource(fragment_shader, fragment_shader_glsl)
        GL.glCompileShader(fragment_shader)
        self.check_shader(fragment_shader)
        self.program = GL.glCreateProgram()
        GL.glAttachShader(self.program, vertex_shader)
        GL.glAttachShader(self.program, fragment_shader)
        GL.glLinkProgram(self.program)
        self.check_program(self.program)
        GL.glDeleteShader(vertex_shader)
        GL.glDeleteShader(fragment_shader)
        self.model_view_projection_uniform_location = GL.glGetUniformLocation(self.program, "ModelViewProjection")
        self.vertex_attrib_coords = GL.glGetAttribLocation(self.program, "VertexPos")
        self.vertex_attrib_color = GL.glGetAttribLocation(self.program, "VertexColor")
        self.cube_vertex_buffer = GL.glGenBuffers(1)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.cube_vertex_buffer)
        GL.glBufferData(GL.GL_ARRAY_BUFFER, c_cubeVertices, GL.GL_STATIC_DRAW)
        self.cube_index_buffer = GL.glGenBuffers(1)
        GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, self.cube_index_buffer)
        GL.glBufferData(GL.GL_ELEMENT_ARRAY_BUFFER, c_cubeIndices, GL.GL_STATIC_DRAW)
        self.vao = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao)
        GL.glEnableVertexAttribArray(self.vertex_attrib_coords)
        GL.glEnableVertexAttribArray(self.vertex_attrib_color)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.cube_vertex_buffer)
        GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, self.cube_index_buffer)
        GL.glVertexAttribPointer(self.vertex_attrib_coords, 3, GL.GL_FLOAT, False,
                                 sizeof(Vertex), cast(0, c_void_p))
        GL.glVertexAttribPointer(self.vertex_attrib_color, 3, GL.GL_FLOAT, False,
                                 sizeof(Vertex),
                                 cast(sizeof(xr.Vector3f), c_void_p))

    def poll_events(self) -> bool:
        glfw.poll_events()
        return glfw.window_should_close(self.window)

    def render_view(
            self,
            layer_view: xr.CompositionLayerProjectionView,
            swapchain_image_base_ptr: POINTER(xr.SwapchainImageBaseHeader),
            _swapchain_format: int,
            cubes: List[Cube],
            mirror=False,
    ):
        assert layer_view.sub_image.image_array_index == 0  # texture arrays not supported.
        # UNUSED_PARM(swapchain_format)                    # not used in this function for now.
        glfw.make_context_current(self.window)
        GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, self.swapchain_framebuffer)
        swapchain_image = cast(swapchain_image_base_ptr, POINTER(xr.SwapchainImageOpenGLKHR)).contents
        color_texture = swapchain_image.image
        GL.glViewport(layer_view.sub_image.image_rect.offset.x,
                      layer_view.sub_image.image_rect.offset.y,
                      layer_view.sub_image.image_rect.extent.width,
                      layer_view.sub_image.image_rect.extent.height)
        GL.glFrontFace(GL.GL_CW)
        GL.glCullFace(GL.GL_BACK)
        GL.glEnable(GL.GL_CULL_FACE)
        GL.glEnable(GL.GL_DEPTH_TEST)
        depth_texture = self.get_depth_texture(color_texture)
        GL.glFramebufferTexture2D(GL.GL_FRAMEBUFFER, GL.GL_COLOR_ATTACHMENT0, GL.GL_TEXTURE_2D, color_texture, 0)
        GL.glFramebufferTexture2D(GL.GL_FRAMEBUFFER, GL.GL_DEPTH_ATTACHMENT, GL.GL_TEXTURE_2D, depth_texture, 0)
        # Clear swapchain and depth buffer.
        GL.glClearColor(*self.background_clear_color)
        GL.glClearDepth(1.0)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT | GL.GL_STENCIL_BUFFER_BIT)
        # Set shaders and uniform variables.
        GL.glUseProgram(self.program)
        pose = layer_view.pose
        proj = Matrix4x4f.create_projection_fov(GraphicsAPI.OPENGL, layer_view.fov, 0.05, 100.0)
        scale = xr.Vector3f(1, 1, 1)
        to_view = Matrix4x4f.create_translation_rotation_scale(pose.position, pose.orientation, scale)
        view = Matrix4x4f.invert_rigid_body(to_view)
        vp = proj @ view
        # Set cube primitive data.
        GL.glBindVertexArray(self.vao)
        # Render each cube
        for cube in cubes:
            # Compute the model-view-projection transform and set it.
            model = Matrix4x4f.create_translation_rotation_scale(cube.Pose.position, cube.Pose.orientation, cube.Scale)
            mvp = vp @ model
            GL.glUniformMatrix4fv(self.model_view_projection_uniform_location, 1, False, mvp.as_numpy())
            # Draw the cube.
            GL.glDrawElements(GL.GL_TRIANGLES, len(c_cubeIndices), GL.GL_UNSIGNED_SHORT, None)

        if mirror:
            # fast blit from the fbo to the window surface
            GL.glBindFramebuffer(GL.GL_DRAW_FRAMEBUFFER, 0)
            w, h = layer_view.sub_image.image_rect.extent.width, layer_view.sub_image.image_rect.extent.height
            GL.glBlitFramebuffer(
                0, 0, w, h, 0, 0,
                640, 480,
                GL.GL_COLOR_BUFFER_BIT,
                GL.GL_NEAREST
            )

        GL.glBindVertexArray(0)
        GL.glUseProgram(0)
        GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, 0)

    def select_color_swapchain_format(self, runtime_formats):
        # List of supported color swapchain formats.
        supported_color_swapchain_formats = [
            GL.GL_RGB10_A2,
            GL.GL_RGBA16F,
            # The two below should only be used as a fallback, as they are linear color formats without enough bits for color
            # depth, thus leading to banding.
            GL.GL_RGBA8,
            GL.GL_RGBA8_SNORM,
            # These two below are the only color formats reported by Steam VR beta 1.24.2
            GL.GL_SRGB8,
            GL.GL_SRGB8_ALPHA8,
        ]
        for rf in runtime_formats:
            for sf in supported_color_swapchain_formats:
                if rf == sf:
                    return sf
        raise RuntimeError("No runtime swapchain format supported for color swapchain")

    def update_options(self, options) -> None:
        self.background_clear_color = options.background_clear_color

    def window_should_close(self):
        return glfw.window_should_close(self.window)
