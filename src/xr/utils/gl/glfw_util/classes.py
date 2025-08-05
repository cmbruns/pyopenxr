import ctypes
from ctypes import Array
from typing import Sequence

# TODO: separate package for opengl stuff
import xr

import glfw

from .. import create_graphics_binding


class InstanceObject(object):
    def __init__(
            self,
            enabled_extensions: Sequence[str] = None,
            application_name: str = None,
            application_version: xr.Version = None,
            engine_name: str = None,
            engine_version: xr.Version = None,
            api_version=xr.Version(1, 0, xr.XR_VERSION_PATCH),
            next=None,
    ) -> None:
        if enabled_extensions is None:
            discovered_extensions = xr.enumerate_instance_extension_properties()
            # Use the most reasonable default
            if xr.KHR_OPENGL_ENABLE_EXTENSION_NAME in discovered_extensions:
                enabled_extensions = [xr.KHR_OPENGL_ENABLE_EXTENSION_NAME, ]
            else:
                enabled_extensions = []
        if application_name is None:
            application_name = "Unknown application"
        self.application_name = application_name
        if application_version is None:
            application_version = xr.Version()
        if engine_name is None:
            engine_name = "pyopenxr"
            engine_version = xr.PYOPENXR_CURRENT_API_VERSION
        if engine_version is None:
            engine_version = xr.Version()
        if application_version is None:
            application_version = xr.Version(0, 0, 0)
        application_info = xr.ApplicationInfo(
            application_name=application_name,
            application_version=application_version,
            engine_name=engine_name,
            engine_version=engine_version,
            api_version=api_version,
        )
        instance_create_info = xr.InstanceCreateInfo(
            create_flags=xr.InstanceCreateFlags(),
            application_info=application_info,
            enabled_api_layer_names=[],
            enabled_extension_names=enabled_extensions,
            next=next,
        )
        self.handle = xr.create_instance(instance_create_info)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, value, traceback):
        self.destroy()

    def destroy(self):
        if self.handle is not None:
            xr.destroy_instance(self.handle)
            self.handle = None

    def get_properties(self) -> xr.InstanceProperties:
        return xr.get_instance_properties(instance=self.handle)


class SystemObject(object):
    def __init__(
            self,
            instance: InstanceObject,
            form_factor: xr.FormFactor = xr.FormFactor.HEAD_MOUNTED_DISPLAY,
    ) -> None:
        # TODO: default managed value for instance
        system_get_info = xr.SystemGetInfo(
            form_factor=form_factor,
        )
        self.id = xr.get_system(instance.handle, system_get_info)
        self.instance = instance

    def __enter__(self):
        return self

    def __exit__(self, exception_type, value, traceback):
        self.id = None


class GlfwWindow(object):
    def __init__(
            self,
            system: SystemObject,
            title: str = None,
            mirror_window: bool = False
    ) -> None:
        if title is None:
            title = system.instance.application_name
        if not glfw.init():
            raise xr.XrException("GLFW initialization failed")
        if mirror_window:
            self.window_size = [s // 4 for s in system.render_target_size]
        else:
            self.window_size = (64, 64)
            glfw.window_hint(glfw.VISIBLE, False)
        self.system = system
        self.pxrGetOpenGLGraphicsRequirementsKHR = ctypes.cast(
            xr.get_instance_proc_addr(
                self.system.instance.handle,
                "xrGetOpenGLGraphicsRequirementsKHR",
            ),
            xr.PFN_xrGetOpenGLGraphicsRequirementsKHR
        )
        self.graphics_requirements = xr.GraphicsRequirementsOpenGLKHR()  # TODO: others
        result = self.pxrGetOpenGLGraphicsRequirementsKHR(
            self.system.instance.handle,
            self.system.id,
            ctypes.byref(self.graphics_requirements))  # TODO: pythonic wrapper
        result = xr.check_result(xr.Result(result))
        if result.is_exception():
            raise result
        glfw.window_hint(glfw.DOUBLEBUFFER, False)
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 5)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        self.window = glfw.create_window(*self.window_size, title, None, None)
        if self.window is None:
            raise xr.XrException("Failed to create GLFW window")
        glfw.make_context_current(self.window)
        # Attempt to disable vsync on the desktop window, or
        # it will interfere with the OpenXR frame loop timing
        glfw.swap_interval(0)
        offscreen_context = xr.utils.gl.glfw_util.GLFWSharedOffscreenContextProvider(self.window)
        self.graphics_binding = create_graphics_binding(offscreen_context)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, value, traceback):
        glfw.terminate()


class SessionObject(object):
    def __init__(self, system: SystemObject, graphics_binding):
        session_create_info = xr.SessionCreateInfo(
            next=graphics_binding.pointer,
            create_flags=xr.SessionCreateFlags(),
            system_id=system.id,
        )
        self.handle = xr.create_session(
            system.instance.handle,
            session_create_info
        )
        self.state = xr.SessionState.IDLE
        self.frame_state = xr.FrameState()
        self.system = system
        self.space = SpaceObject(self)
        self.view_configuration_type = xr.ViewConfigurationType.PRIMARY_STEREO

    def __enter__(self):
        return self

    def __exit__(self, type_, value, traceback):
        self.destroy()

    def begin_frame(self):
        xr.begin_frame(self.handle)

    def destroy(self):
        if self.handle is None:
            return
        try:
            xr.destroy_session(self.handle)
        finally:
            self.handle = None

    def end_frame(self, layers=None):
        frame_end_info = xr.FrameEndInfo(
            display_time=self.frame_state.predicted_display_time,
            environment_blend_mode=xr.EnvironmentBlendMode.OPAQUE,
            layers=layers,
        )
        xr.end_frame(self.handle, frame_end_info)

    def locate_views(self) -> (xr.ViewState, Array):
        view_configuration_type = self.view_configuration_type
        # TODO: put this someplace else
        # TODO: if self.state....
        display_time = self.frame_state.predicted_display_time
        #
        view_locate_info = xr.ViewLocateInfo(
            view_configuration_type,
            display_time,
            self.space.handle,
        )
        return xr.locate_views(self.handle, view_locate_info)

    def on_state_changed(self, session_state_changed_event):
        if self.handle is None:
            return
        if not xr.StructureType(session_state_changed_event.type) == xr.StructureType.EVENT_DATA_SESSION_STATE_CHANGED:
            return
        event = ctypes.cast(
            ctypes.byref(session_state_changed_event),
            ctypes.POINTER(xr.EventDataSessionStateChanged)).contents
        self.state = xr.SessionState(event.state)
        if self.state == xr.SessionState.READY:
            if self.handle is not None:
                sbi = xr.SessionBeginInfo(self.view_configuration_type)
                xr.begin_session(self.handle, sbi)
        elif self.state == xr.SessionState.STOPPING:
            self.destroy()

    def poll_xr_events(self):
        while True:
            try:
                event_buffer = xr.poll_event(self.system.instance.handle)
                event_type = xr.StructureType(event_buffer.type)
                if event_type == xr.StructureType.EVENT_DATA_SESSION_STATE_CHANGED:
                    self.on_state_changed(event_buffer)
            except xr.EventUnavailable:
                break

    def wait_frame(self):
        self.frame_state = xr.wait_frame(self.handle)


class SpaceObject(object):
    def __init__(
            self,
            session: SessionObject,
            reference_space_type: xr.ReferenceSpaceType = xr.ReferenceSpaceType.STAGE,
            pose_in_reference_space: xr.Posef = None,
    ):
        if pose_in_reference_space is None:
            pose_in_reference_space = xr.Posef()
        reference_space_create_info = xr.ReferenceSpaceCreateInfo(
            reference_space_type=reference_space_type,
            pose_in_reference_space=pose_in_reference_space,
        )
        self.handle = xr.create_reference_space(session.handle, reference_space_create_info)


__all__ = [
    "GlfwWindow",
    "InstanceObject",
    "SessionObject",
    "SpaceObject",
    "SystemObject",
]
