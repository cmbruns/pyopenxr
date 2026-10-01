from ctypes import c_void_p, cast, sizeof, string_at, Structure
import inspect
import logging
import platform
import sys
from typing import Dict, List, Optional, Sequence

import numpy
from OpenGL import GL
from OpenGL import EGL
if sys.platform == "android":
    from OpenGL import GLES3

from .graphics_plugin import Cube, IGraphicsPlugin, SwapchainImageData

import xr

from .geometry import c_cubeVertices, c_cubeIndices, Vertex
from .linear import GraphicsAPI, Matrix4x4f
from .options import Options

logger = logging.getLogger("hello_xr.graphics_plugin_opengles")


dark_slate_gray = numpy.array([0.184313729, 0.309803933, 0.309803933, 1.0], dtype=numpy.float32)

vertex_shader_glsl = inspect.cleandoc("""
    #version 320 es

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
    #version 320 es

    in lowp vec3 PSVertexColor;
    out lowp vec4 FragColor;

    void main() {
       FragColor = vec4(PSVertexColor, 1);
    }
""")


class OpenGLESGraphicsPlugin(IGraphicsPlugin):
    def __init__(self, options: Options):
        super().__init__()

        self.background_clear_color = options.background_clear_color
        if platform.system() == "Windows":
            self._graphics_binding = xr.GraphicsBindingOpenGLESWin32KHR()
        elif platform.system() == "Linux":
            # TODO more nuance on Linux: Xlib, Xcb, Wayland
            self._graphics_binding = xr.GraphicsBindingOpenGLESXlibKHR()
        elif sys.platform == "android":
            self._graphics_binding = None  # Fill in later
        self.swapchain_framebuffer: Optional[int] = None
        self.program = None
        self.model_view_projection_uniform_location = 0
        self.vertex_attrib_coords = 0
        self.vertex_attrib_color = 0
        self.vao = None
        self.cube_vertex_buffer = None
        self.cube_index_buffer = None
        self.context_api_major_version = 0
        # Plugin-owned swapchain image records (mirrors Khronos m_swapchainImageDataMap).
        self._swapchain_image_records: List[SwapchainImageData] = []
        self.debug_message_proc = None  # To keep the callback alive
        # EGL things
        self.config = None
        self.context = None
        self.display = None
        self.surface = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
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
        # Delete plugin-owned fallback depth textures (mirrors Khronos ~OpenGLESPlugin).
        for record in self._swapchain_image_records:
            record.destroy()
        self._swapchain_image_records.clear()

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
        }.get(severity, logging.INFO)
        logger.log(log_level, f"OpenGL Message: {string_at(raw, length).decode()}")

    def focus_window(self):
        self.make_current()

    def get_supported_swapchain_sample_count(self, _xr_view_configuration_view: xr.ViewConfigurationView):
        return 1

    @property
    def instance_extensions(self) -> List[str]:
        return [xr.KHR_OPENGL_ES_ENABLE_EXTENSION_NAME]

    @property
    def swapchain_image_type(self):
        return xr.SwapchainImageOpenGLESKHR

    @property
    def graphics_binding(self) -> Structure:
        return self._graphics_binding

    def make_current(self):
        assert EGL.eglMakeCurrent(self.display, self.surface, self.surface, self.context)

    def initialize_device(self, instance: xr.Instance, system_id: xr.SystemId):
        # extension function must be loaded by name
        graphics_requirements = xr.get_opengl_es_graphics_requirements_khr(instance, system_id)

        # Create OpenGLES context
        self.display = EGL.eglGetDisplay(EGL.EGL_DEFAULT_DISPLAY)
        assert self.display != EGL.EGL_NO_DISPLAY
        major, minor = EGL.EGLint(), EGL.EGLint()
        assert EGL.eglInitialize(self.display, major, minor)
        config_attributes = [
            EGL.EGL_RENDERABLE_TYPE, EGL.EGL_OPENGL_ES3_BIT,
            EGL.EGL_SURFACE_TYPE, EGL.EGL_PBUFFER_BIT,
            EGL.EGL_RED_SIZE, 8, EGL.EGL_GREEN_SIZE, 8, EGL.EGL_BLUE_SIZE, 8,
            EGL.EGL_ALPHA_SIZE, 8, EGL.EGL_DEPTH_SIZE, 24,
            EGL.EGL_SAMPLES, 1,
            EGL.EGL_NONE]
        num_configs = EGL.EGLint()
        configs = (EGL.EGLConfig * 1)()
        assert EGL.eglChooseConfig(self.display, config_attributes, configs, 1, num_configs)
        assert num_configs.value > 0
        self.config = configs[0]
        pbuffer_attributes = [
            EGL.EGL_WIDTH, 640,
            EGL.EGL_HEIGHT, 480,
            EGL.EGL_NONE]
        self.surface = EGL.eglCreatePbufferSurface(self.display, self.config, pbuffer_attributes)
        assert self.surface != EGL.EGL_NO_SURFACE
        context_attributes = [
            EGL.EGL_CONTEXT_MAJOR_VERSION, 3,
            EGL.EGL_CONTEXT_MINOR_VERSION, 2,
            EGL.EGL_CONTEXT_OPENGL_DEBUG, EGL.EGL_TRUE,
            EGL.EGL_NONE
        ]

        self.context = EGL.eglCreateContext(self.display, self.config, EGL.EGL_NO_CONTEXT, context_attributes)
        assert self.context != EGL.EGL_NO_CONTEXT
        self.make_current()

        major = GL.glGetIntegerv(GL.GL_MAJOR_VERSION)
        minor = GL.glGetIntegerv(GL.GL_MINOR_VERSION)
        logger.debug(f"OpenGL ES version {major}.{minor}")
        desired_api_version = xr.Version(major, minor, 0)
        if graphics_requirements.min_api_version_supported > desired_api_version.number():
            ms = xr.Version(graphics_requirements.min_api_version_supported).number()
            raise xr.XrException(f"Runtime does not support desired Graphics API and/or version {hex(ms)}")

        self.context_api_major_version = major

        if platform.system() == "Windows":
            from OpenGL import WGL
            self._graphics_binding.h_dc = WGL.wglGetCurrentDC()
            self._graphics_binding.h_glrc = WGL.wglGetCurrentContext()
        elif platform.system() == "Linux":
            # TODO more nuance on Linux: Xlib, Xcb, Wayland
            from OpenGL import GLX
            self._graphics_binding.x_display = GLX.glXGetCurrentDisplay()
            self._graphics_binding.glx_drawable = GLX.glXGetCurrentDrawable()
            self._graphics_binding.glx_context = GLX.glXGetCurrentContext()
        elif sys.platform == "android":
            self._graphics_binding = xr.GraphicsBindingOpenGLESAndroidKHR(
                display=self.display,
                context=self.context,
                config=self.config,
            )

        GL.glEnable(GL.GL_DEBUG_OUTPUT)
        # Store the debug callback function pointer, so it won't get garbage collected;
        # otherwise mysterious GL crashes will ensue.
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
        pass

    def render_view(
            self,
            layer_view: xr.CompositionLayerProjectionView,
            color_image: xr.SwapchainImageOpenGLESKHR,
            depth_image: xr.SwapchainImageOpenGLESKHR,
            _swapchain_format: int,
            cubes: List[Cube],
            mirror=False,
    ):
        assert layer_view.sub_image.image_array_index == 0  # texture arrays not supported.
        # UNUSED_PARM(swapchain_format)                    # not used in this function for now.
        self.make_current()
        GL.glGetError()  # workaround SteamVR Linux problem
        GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, self.swapchain_framebuffer)
        color_texture = color_image.image
        depth_texture = depth_image.image
        GL.glViewport(layer_view.sub_image.image_rect.offset.x,
                      layer_view.sub_image.image_rect.offset.y,
                      layer_view.sub_image.image_rect.extent.width,
                      layer_view.sub_image.image_rect.extent.height)
        GL.glFrontFace(GL.GL_CW)
        GL.glCullFace(GL.GL_BACK)
        GL.glEnable(GL.GL_CULL_FACE)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glFramebufferTexture2D(GL.GL_FRAMEBUFFER, GL.GL_COLOR_ATTACHMENT0, GL.GL_TEXTURE_2D, color_texture, 0)
        GL.glFramebufferTexture2D(GL.GL_FRAMEBUFFER, GL.GL_DEPTH_ATTACHMENT, GL.GL_TEXTURE_2D, depth_texture, 0)
        # Clear swapchain and depth buffer.
        GL.glClearColor(*self.background_clear_color)
        if sys.platform == "android":
            # glClearDepth does not exist in OpenGL ES (debugged on Quest 3).
            GLES3.glClearDepthf(1.0)
        else:
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

    def select_color_swapchain_format(self, runtime_formats: Sequence[int]):
        # List of supported color swapchain formats.
        supported_color_swapchain_formats = [
            GL.GL_RGBA8,
            GL.GL_RGBA8_SNORM,
        ]
        if self.context_api_major_version >= 3:
            supported_color_swapchain_formats.append(GL.GL_SRGB8_ALPHA8)
        for rf in runtime_formats:
            for sf in supported_color_swapchain_formats:
                if rf == sf:
                    return sf
        raise RuntimeError("No runtime swapchain format supported for color swapchain")

    def select_depth_swapchain_format(self, runtime_formats: Sequence[int]) -> int:
        # List of supported depth swapchain formats (Khronos graphicsplugin_opengles.cpp preference order).
        supported_depth_swapchain_formats = [
            GL.GL_DEPTH24_STENCIL8,
            GL.GL_DEPTH_COMPONENT24,
            GL.GL_DEPTH_COMPONENT16,
            GL.GL_DEPTH_COMPONENT32F,
        ]
        for rf in runtime_formats:
            for sf in supported_depth_swapchain_formats:
                if rf == sf:
                    return sf
        # Return -1 rather than throwing (mirrors Khronos SelectDepthSwapchainFormat(false, ...)).
        return -1

    def allocate_swapchain_image_data(
            self, color_images, color_create_info: xr.SwapchainCreateInfo) -> SwapchainImageData:
        record = OpenGLESSwapchainImageData(
            color_images,
            width=color_create_info.width,
            height=color_create_info.height,
            array_size=color_create_info.array_size,
            sample_count=color_create_info.sample_count,
        )
        # The plugin owns the record (mirrors Khronos Adopt).
        self._swapchain_image_records.append(record)
        return record

    def allocate_swapchain_image_data_with_depth_swapchain(
            self, color_images, color_create_info: xr.SwapchainCreateInfo,
            depth_swapchain: xr.Swapchain, depth_images) -> SwapchainImageData:
        record = OpenGLESSwapchainImageData(
            color_images,
            width=color_create_info.width,
            height=color_create_info.height,
            array_size=color_create_info.array_size,
            sample_count=color_create_info.sample_count,
            depth_swapchain=depth_swapchain,
            depth_images=depth_images,
        )
        # The plugin owns the record (mirrors Khronos Adopt).
        self._swapchain_image_records.append(record)
        return record

    def update_options(self, options) -> None:
        self.background_clear_color = options.background_clear_color

    def window_should_close(self):
        return False


class OpenGLESSwapchainImageData(SwapchainImageData):
    """Per-swapchain image record for the OpenGL ES plugin (mirrors Khronos OpenGLESSwapchainImageData)."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Lazily allocated fallback depth textures, keyed by color image index
        # (mirrors Khronos OpenGLESFallbackDepthTexture allocation on demand).
        self._fallback_depth_textures: Dict[int, int] = {}

    def get_fallback_depth_image(self, color_image_index: int) -> xr.SwapchainImageOpenGLESKHR:
        if color_image_index not in self._fallback_depth_textures:
            self._fallback_depth_textures[color_image_index] = self._allocate_fallback_depth_texture()
        return xr.SwapchainImageOpenGLESKHR(image=self._fallback_depth_textures[color_image_index])

    def _allocate_fallback_depth_texture(self) -> int:
        # Mirrors Khronos OpenGLESFallbackDepthTexture::Allocate (GL_DEPTH_COMPONENT24, array aware).
        is_array = self.array_size > 1
        target = GL.GL_TEXTURE_2D_ARRAY if is_array else GL.GL_TEXTURE_2D
        texture = GL.glGenTextures(1)
        GL.glBindTexture(target, texture)
        GL.glTexParameteri(target, GL.GL_TEXTURE_MAG_FILTER, GL.GL_NEAREST)
        GL.glTexParameteri(target, GL.GL_TEXTURE_MIN_FILTER, GL.GL_NEAREST)
        GL.glTexParameteri(target, GL.GL_TEXTURE_WRAP_S, GL.GL_CLAMP_TO_EDGE)
        GL.glTexParameteri(target, GL.GL_TEXTURE_WRAP_T, GL.GL_CLAMP_TO_EDGE)
        if is_array:
            GL.glTexImage3D(target, 0, GL.GL_DEPTH_COMPONENT24, self.width, self.height, self.array_size,
                            0, GL.GL_DEPTH_COMPONENT, GL.GL_UNSIGNED_INT, None)
        else:
            GL.glTexImage2D(target, 0, GL.GL_DEPTH_COMPONENT24, self.width, self.height,
                            0, GL.GL_DEPTH_COMPONENT, GL.GL_UNSIGNED_INT, None)
        return texture

    def destroy(self) -> None:
        for texture in self._fallback_depth_textures.values():
            GL.glDeleteTextures(1, [texture])
        self._fallback_depth_textures.clear()
