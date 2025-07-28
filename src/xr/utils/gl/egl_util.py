from _ctypes import pointer
from ctypes import cast, c_void_p

from OpenGL import EGL
import xr

from . import GraphicsBinding
from .. import GraphicsContextProvider


class EGLOffscreenContextProvider(GraphicsContextProvider):
    def __init__(self):
        self.display = EGL.eglGetDisplay(EGL.EGL_DEFAULT_DISPLAY)
        if self.display == EGL.EGL_NO_DISPLAY:
            raise RuntimeError("Failed to get EGL display")
        if not EGL.eglInitialize(self.display, None, None):
            raise RuntimeError("EGL initialization failed")
        config_attributes = [
            EGL.EGL_RED_SIZE, 8,
            EGL.EGL_GREEN_SIZE, 8,
            EGL.EGL_BLUE_SIZE, 8,
            EGL.EGL_ALPHA_SIZE, 8,
            EGL.EGL_DEPTH_SIZE, 24,
            EGL.EGL_RENDERABLE_TYPE, EGL.EGL_OPENGL_BIT,
            EGL.EGL_SURFACE_TYPE, EGL.EGL_PBUFFER_BIT,
            EGL.EGL_NONE
        ]
        configs = (EGL.EGLConfig * 1)()
        num_configs = EGL.EGLint()
        if not EGL.eglChooseConfig(self.display, config_attributes, configs, 1, num_configs):
            raise RuntimeError("Failed to choose EGL config")
        self.config = configs[0]
        # Set the pixel buffer configuration
        width, height = 1, 1
        pixel_buffer_attributes = [
            EGL.EGL_WIDTH, width,
            EGL.EGL_HEIGHT, height,
            EGL.EGL_NONE
        ]
        self.surface = EGL.eglCreatePbufferSurface(self.display, self.config, pixel_buffer_attributes)
        if self.surface == EGL.EGL_NO_SURFACE:
            raise RuntimeError("Failed to create pixel buffer surface")
        # Step 5: Bind API and create context
        EGL.eglBindAPI(EGL.EGL_OPENGL_API)
        self.context = EGL.eglCreateContext(self.display, self.config, EGL.EGL_NO_CONTEXT, None)
        if self.context == EGL.EGL_NO_CONTEXT:
            raise RuntimeError("Failed to create EGL context")

    def destroy(self):
        # Unbind context if it’s currently bound
        self.done_current()
        # Destroy EGL surface if it exists
        if self.surface:
            result = EGL.eglDestroySurface(self.display, self.surface)
            if not result:
                raise RuntimeError("Failed to destroy EGL surface")
            self.surface = None
        # Destroy EGL context if it exists
        if self.context:
            result = EGL.eglDestroyContext(self.display, self.context)
            if not result:
                raise RuntimeError("Failed to destroy EGL context")
            self.context = None
        # Terminate display
        if self.display:
            result = EGL.eglTerminate(self.display)
            if not result:
                raise RuntimeError("Failed to terminate EGL display")
            self.display = None

    def done_current(self) -> None:
        result = EGL.eglMakeCurrent(
            self.display,
            EGL.EGL_NO_SURFACE,
            EGL.EGL_NO_SURFACE,
            EGL.EGL_NO_CONTEXT
        )
        if not result:
            raise RuntimeError("Failed to release EGL context")

    def make_current(self):
        if not EGL.eglMakeCurrent(self.display, self.surface, self.surface, self.context):
            raise RuntimeError("Failed to create EGL context")


class EGLGraphicsBinding(GraphicsBinding):
    def __init__(self, context_provider: EGLOffscreenContextProvider):
        self.graphics_binding = xr.GraphicsBindingEGLMNDX()
        display = context_provider.display
        context = context_provider.context
        self.graphics_binding.display = display
        self.graphics_binding.context = context
        self.graphics_binding.get_proc_address = cast(
            EGL.eglGetProcAddress.load(), xr.PFN_xrEglGetProcAddressMNDX)
        self.graphics_binding.config = context_provider.config
        self._pointer = cast(pointer(self.graphics_binding), c_void_p)

    @property
    def pointer(self):
        return self._pointer
