import abc
from ctypes import c_void_p, cast, sizeof, Structure
import inspect
import logging
import platform

from OpenGL import GL
if platform.system() == "Windows":
    from OpenGL import WGL
elif platform.system() == "Linux":
    from OpenGL import GLX
import glfw

import xr

from hello_xr.geometry import c_cubeVertices, c_cubeIndices, Vertex

logger = logging.getLogger("hello_xr.graphics_plugins")


class Cube(Structure):
    _fields_ = [
        ("Pose", xr.Posef),
        ("Scale", xr.Vector3f),
    ]


class IGraphicsPlugin(abc.ABC):
    @abc.abstractmethod
    def __enter__(self):
        pass

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @abc.abstractmethod
    def get_instance_extensions(self):
        pass

    @abc.abstractmethod
    def get_supported_swapchain_sample_count(xr_view_configuration_view):
        pass

    @property
    @abc.abstractmethod
    def graphics_binding(self):
        pass

    @abc.abstractmethod
    def initialize_device(self, instance_handle, system_id):
        pass

    @abc.abstractmethod
    def select_color_swapchain_format(self, runtime_formats):
        pass


class OpenGLGraphicsPlugin(IGraphicsPlugin):
    def __init__(self):
        self.dark_slate_gray = (0.184313729, 0.309803933, 0.309803933, 1.0)
        # Map color buffer to associated depth buffer. This map is populated on demand.
        self.color_to_depth_map = {}
        self.window = None
        if platform.system() == "Windows":
            self._graphics_binding = xr.GraphicsBindingOpenGLWin32KHR()
        elif platform.system() == "Linux":
            # TODO more nuance on Linux: Xlib, Xcb, Wayland
            self._graphics_binding = xr.GraphicsBindingOpenGLXlibKHR()
        self.swapchain_image_buffers = None
        self.swapchain_framebuffer = None
        self.program = None
        self.vao = None
        self.cube_vertex_buffer = None
        self.cube_index_buffer = None
        self.model_view_projection_uniform_location = 0
        self.vertex_attrib_coords = 0
        self.vertex_attrib_color = 0
        self.debug_message_proc = None
        self.vertex_shader_glsl = inspect.cleandoc("""
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
        self.fragment_shader_glsl = inspect.cleandoc("""
            #version 410
        
            in vec3 PSVertexColor;
            out vec4 FragColor;
        
            void main() {
               FragColor = vec4(PSVertexColor, 1);
            }
        """)

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
        for color, depth in self.color_to_depth_map.items():
            if depth is not None:
                GL.glDeleteTextures(1, depth)
        self.color_to_depth_map = {}
        glfw.terminate()

    @staticmethod
    def debug_message_callback(source, msg_type, msg_id, severity, length, raw, user):
        """Redirect OpenGL debug messages"""
        msg = raw[0:length]
        logger.info(f"GL Debug: {msg.decode()}")

    def focus_window(self):
        glfw.focus_window(self.window)
        glfw.make_context_current(self.window)

    def get_instance_extensions(self):
        return [xr.KHR_OPENGL_ENABLE_EXTENSION_NAME]

    @staticmethod
    def get_swapchain_image_type():
        return xr.SwapchainImageOpenGLKHR

    @property
    def graphics_binding(self):
        return self._graphics_binding

    def initialize_device(self, instance_handle, system_id):
        # extension function must be loaded by name
        pfnGetOpenGLGraphicsRequirementsKHR = cast(
            xr.get_instance_proc_addr(
                instance_handle,
                "xrGetOpenGLGraphicsRequirementsKHR",
            ),
            xr.PFN_xrGetOpenGLGraphicsRequirementsKHR
        )
        graphics_requirements = xr.GraphicsRequirementsOpenGLKHR()
        result = pfnGetOpenGLGraphicsRequirementsKHR(instance_handle, system_id, graphics_requirements)
        result = xr.check_result(xr.Result(result))
        if result.is_exception():
            raise result
        if not glfw.init():
            raise xr.XrException("GLFW initialization failed")
        # glfw.window_hint(glfw.VISIBLE, False)
        # glfw.window_hint(glfw.DOUBLEBUFFER, False)
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 5)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        self.window = glfw.create_window(64, 64, "GLFW Window", None, None)
        if self.window is None:
            raise xr.XrException("Failed to create GLFW window")
        glfw.make_context_current(self.window)
        glfw.swap_interval(0)
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
        self.debug_message_proc = GL.GLDEBUGPROC(self.debug_message_callback)
        GL.glDebugMessageCallback(self.debug_message_proc, None)
        self.initialize_resources()

    def initialize_resources(self):
        self.swapchain_framebuffer = GL.glGenFramebuffers(1)
        vertex_shader = GL.glCreateShader(GL.GL_VERTEX_SHADER)
        GL.glShaderSource(vertex_shader, self.vertex_shader_glsl)
        GL.glCompileShader(vertex_shader)
        self.check_shader(vertex_shader)
        fragment_shader = GL.glCreateShader(GL.GL_FRAGMENT_SHADER)
        GL.glShaderSource(fragment_shader, self.fragment_shader_glsl)
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

    def select_color_swapchain_format(self, runtime_formats):
        # List of supported color swapchain formats.
        supported_color_swapchain_formats = [
            GL.GL_RGB10_A2,
            GL.GL_RGBA16F,
            # The two below should only be used as a fallback, as they are linear color formats without enough bits for color
            # depth, thus leading to banding.
            GL.GL_RGBA8,
            GL.GL_RGBA8_SNORM,
        ]
        for rf in runtime_formats:
            for sf in supported_color_swapchain_formats:
                if rf == sf:
                    return sf
        raise RuntimeError("No runtime swapchain format supported for color swapchain")

    """

    const XrBaseInStructure* GetGraphicsBinding() const:
        return reinterpret_cast<const XrBaseInStructure*>(self.graphicsBinding)
    

    std::vector<XrSwapchainImageBaseHeader*> AllocateSwapchainImageStructs(
        uint32_t capacity, const XrSwapchainCreateInfo /*swapchainCreateInfo*/):
        # Allocate and initialize the buffer of image structs (must be sequential in memory for xrEnumerateSwapchainImages).
        # Return back an array of pointers to each swapchain image struct so the consumer doesn't need to know the type/size.
        std::vector<XrSwapchainImageOpenGLKHR> swapchainImageBuffer(capacity)
        std::vector<XrSwapchainImageBaseHeader*> swapchainImageBase
        for (XrSwapchainImageOpenGLKHR image : swapchainImageBuffer):
            image.type = XR_TYPE_SWAPCHAIN_IMAGE_OPENGL_KHR
            swapchainImageBase.push_back(reinterpret_cast<XrSwapchainImageBaseHeader*>(image))
        

        # Keep the buffer alive by moving it into the list of buffers.
        self.swapchainImageBuffers.push_back(std::move(swapchainImageBuffer))

        return swapchainImageBase
    

    uint32_t GetDepthTexture(uint32_t colorTexture):
        # If a depth-stencil view has already been created for this back-buffer, use it.
        auto depthBufferIt = self.color_to_depth_map.find(colorTexture)
        if depthBufferIt != self.color_to_depth_map.end()):
            return depthBufferIt->second
        

        # This back-buffer has no corresponding depth-stencil texture, so create one with matching dimensions.

        GLint width
        GLint height
        GL.glBindTexture(GL.GL_TEXTURE_2D, colorTexture)
        GL.glGetTexLevelParameteriv(GL.GL_TEXTURE_2D, 0, GL.GL_TEXTURE_WIDTH, width)
        GL.glGetTexLevelParameteriv(GL.GL_TEXTURE_2D, 0, GL.GL_TEXTURE_HEIGHT, height)

        uint32_t depthTexture
        depthTexture = GL.glGenTextures(1)
        GL.glBindTexture(GL.GL_TEXTURE_2D, depthTexture)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_NEAREST)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_NEAREST)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_CLAMP_TO_EDGE)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_CLAMP_TO_EDGE)
        GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_DEPTH_COMPONENT32, width, height, 0, GL.GL_DEPTH_COMPONENT, GL.GL_FLOAT, None)

        self.color_to_depth_map.insert(std::make_pair(colorTexture, depthTexture))

        return depthTexture
    

    void RenderView(const XrCompositionLayerProjectionView layerView, const XrSwapchainImageBaseHeader* swapchainImage,
                    int64_t swapchainFormat, const std::vector<Cube> cubes):
        CHECK(layerView.subImage.imageArrayIndex == 0)  # exture arrays not supported.
        UNUSED_PARM(swapchainFormat)                    # ot used in this function for now.

        GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, self.swapchain_framebuffer)

        const uint32_t colorTexture = reinterpret_cast<const XrSwapchainImageOpenGLKHR*>(swapchainImage)->image

        GL.glViewport(static_cast<GLint>(layerView.subImage.imageRect.offset.x),
                   static_cast<GLint>(layerView.subImage.imageRect.offset.y),
                   static_cast<GLsizei>(layerView.subImage.imageRect.extent.width),
                   static_cast<GLsizei>(layerView.subImage.imageRect.extent.height))

        GL.glFrontFace(GL.GL_CW)
        GL.glCullFace(GL.GL_BACK)
        GL.glEnable(GL.GL_CULL_FACE)
        GL.glEnable(GL.GL_DEPTH_TEST)

        const uint32_t depthTexture = GetDepthTexture(colorTexture)

        GL.glFramebufferTexture2D(GL.GL_FRAMEBUFFER, GL.GL_COLOR_ATTACHMENT0, GL.GL_TEXTURE_2D, colorTexture, 0)
        GL.glFramebufferTexture2D(GL.GL_FRAMEBUFFER, GL.GL_DEPTH_ATTACHMENT, GL.GL_TEXTURE_2D, depthTexture, 0)

        # Clear swapchain and depth buffer.
        GL.glClearColor(dark_slate_gray[0], dark_slate_gray[1], dark_slate_gray[2], dark_slate_gray[3])
        GL.glClearDepth(1.0)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT | GL.GL_STENCIL_BUFFER_BIT)

        # Set shaders and uniform variables.
        GL.glUseProgram(self.program)

        const auto pose = layerView.pose
        XrMatrix4x4f proj
        XrMatrix4x4f_CreateProjectionFov(proj, GRAPHICS_OPENGL, layerView.fov, 0.05, 100.0)
        XrMatrix4x4f toView
        XrVector3f scale{1.f, 1.f, 1.f}
        XrMatrix4x4f_CreateTranslationRotationScale(toView, pose.position, pose.orientation, scale)
        XrMatrix4x4f view
        XrMatrix4x4f_InvertRigidBody(view, toView)
        XrMatrix4x4f vp
        XrMatrix4x4f_Multiply(vp, proj, view)

        # Set cube primitive data.
        GL.glBindVertexArray(self.vao)

        # Render each cube
        for (const Cube cube : cubes):
            # ompute the model-view-projection transform and set it..
            XrMatrix4x4f model
            XrMatrix4x4f_CreateTranslationRotationScale(model, cube.Pose.position, cube.Pose.orientation, cube.Scale)
            XrMatrix4x4f mvp
            XrMatrix4x4f_Multiply(mvp, vp, model)
            GL.glUniformMatrix4fv(self.model_view_projection_uniform_location, 1, False, reinterpret_cast<const GLfloat*>(mvp))

            # Draw the cube.
            GL.glDrawElements(GL.GL_TRIANGLES, static_cast<GLsizei>(ArraySize(Geometry::c_cubeIndices)), GL.GL_UNSIGNED_SHORT, None)
        

        GL.glBindVertexArray(0)
        GL.glUseProgram(0)
        GL.glBindFramebuffer(GL.GL_FRAMEBUFFER, 0)

        # Swap our window every other eye for RenderDoc
        static int everyOther = 0
        if (everyOther++  1) is not None:
            ksGpuWindow_SwapBuffers(window)
    """

    @staticmethod
    def get_supported_swapchain_sample_count(xr_view_configuration_view):
        return 1
