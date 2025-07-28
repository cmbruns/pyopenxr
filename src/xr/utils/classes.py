import ctypes
from ctypes import Array
import enum
from typing import Sequence

# TODO: separate package for opengl stuff
import xr

import glfw

from xr.enums import *
from xr.typedefs import *
from xr.functions import *
from xr.platform import *
from xr.version import *
from xr.exception import *

from .gl import create_graphics_binding


class Eye(enum.IntEnum):
    LEFT = 0
    RIGHT = 1


class InstanceObject(object):
    def __init__(
            self,
            enabled_extensions: Sequence[str] = None,
            application_name: str = None,
            application_version: Version = None,
            engine_name: str = None,
            engine_version: Version = None,
            api_version=Version(1, 0, XR_VERSION_PATCH),
            next=None,
    ) -> None:
        if enabled_extensions is None:
            discovered_extensions = enumerate_instance_extension_properties()
            # Use the most reasonable default
            if KHR_OPENGL_ENABLE_EXTENSION_NAME in discovered_extensions:
                enabled_extensions = [KHR_OPENGL_ENABLE_EXTENSION_NAME, ]
            else:
                enabled_extensions = []
        if application_name is None:
            application_name = "Unknown application"
        self.application_name = application_name
        if application_version is None:
            application_version = Version()
        if engine_name is None:
            engine_name = "pyopenxr"
            engine_version = PYOPENXR_CURRENT_API_VERSION
        if engine_version is None:
            engine_version = Version()
        if application_version is None:
            application_version = xr.Version(0, 0, 0)
        application_info = ApplicationInfo(
            application_name=application_name,
            application_version=application_version,
            engine_name=engine_name,
            engine_version=engine_version,
            api_version=api_version,
        )
        instance_create_info = InstanceCreateInfo(
            create_flags=InstanceCreateFlags(),
            application_info=application_info,
            enabled_api_layer_names=[],
            enabled_extension_names=enabled_extensions,
            next=next,
        )
        self.handle = create_instance(instance_create_info)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, value, traceback):
        self.destroy()

    def destroy(self):
        if self.handle is not None:
            destroy_instance(self.handle)
            self.handle = None

    def get_properties(self) -> InstanceProperties:
        return xr.get_instance_properties(instance=self.handle)


class SystemObject(object):
    def __init__(
            self,
            instance: InstanceObject,
            form_factor: FormFactor = FormFactor.HEAD_MOUNTED_DISPLAY,
    ) -> None:
        # TODO: default managed value for instance
        system_get_info = SystemGetInfo(
            form_factor=form_factor,
        )
        self.id = get_system(instance.handle, system_get_info)
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
            raise XrException("GLFW initialization failed")
        if mirror_window:
            self.window_size = [s // 4 for s in system.render_target_size]
        else:
            self.window_size = (64, 64)
            glfw.window_hint(glfw.VISIBLE, False)
        self.system = system
        self.pxrGetOpenGLGraphicsRequirementsKHR = ctypes.cast(
            get_instance_proc_addr(
                self.system.instance.handle,
                "xrGetOpenGLGraphicsRequirementsKHR",
            ),
            PFN_xrGetOpenGLGraphicsRequirementsKHR
        )
        self.graphics_requirements = GraphicsRequirementsOpenGLKHR()  # TODO: others
        result = self.pxrGetOpenGLGraphicsRequirementsKHR(
            self.system.instance.handle,
            self.system.id,
            ctypes.byref(self.graphics_requirements))  # TODO: pythonic wrapper
        result = check_result(Result(result))
        if result.is_exception():
            raise result
        glfw.window_hint(glfw.DOUBLEBUFFER, False)
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 5)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        self.window = glfw.create_window(*self.window_size, title, None, None)
        if self.window is None:
            raise XrException("Failed to create GLFW window")
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
        session_create_info = SessionCreateInfo(
            next=graphics_binding.pointer,
            create_flags=SessionCreateFlags(),
            system_id=system.id,
        )
        self.handle = create_session(
            system.instance.handle,
            session_create_info
        )
        self.state = SessionState.IDLE
        self.frame_state = FrameState()
        self.system = system
        self.space = SpaceObject(self)
        self.view_configuration_type = ViewConfigurationType.PRIMARY_STEREO

    def __enter__(self):
        return self

    def __exit__(self, type_, value, traceback):
        self.destroy()

    def begin_frame(self):
        begin_frame(self.handle)

    def destroy(self):
        if self.handle is None:
            return
        try:
            destroy_session(self.handle)
        finally:
            self.handle = None

    def end_frame(self, layers=None):
        frame_end_info = FrameEndInfo(
            display_time=self.frame_state.predicted_display_time,
            environment_blend_mode=EnvironmentBlendMode.OPAQUE,
            layers=layers,
        )
        end_frame(self.handle, frame_end_info)

    def locate_views(self) -> (ViewState, Array):
        view_configuration_type = self.view_configuration_type
        # TODO: put this someplace else
        # TODO: if self.state....
        display_time = self.frame_state.predicted_display_time
        #
        view_locate_info = ViewLocateInfo(
            view_configuration_type,
            display_time,
            self.space.handle,
        )
        return locate_views(self.handle, view_locate_info)

    def on_state_changed(self, session_state_changed_event):
        if self.handle is None:
            return
        if not StructureType(session_state_changed_event.type) == StructureType.EVENT_DATA_SESSION_STATE_CHANGED:
            return
        event = ctypes.cast(
            ctypes.byref(session_state_changed_event),
            ctypes.POINTER(EventDataSessionStateChanged)).contents
        self.state = SessionState(event.state)
        if self.state == SessionState.READY:
            if self.handle is not None:
                sbi = SessionBeginInfo(self.view_configuration_type)
                begin_session(self.handle, sbi)
        elif self.state == SessionState.STOPPING:
            self.destroy()

    def poll_xr_events(self):
        while True:
            try:
                event_buffer = poll_event(self.system.instance.handle)
                event_type = StructureType(event_buffer.type)
                if event_type == StructureType.EVENT_DATA_SESSION_STATE_CHANGED:
                    self.on_state_changed(event_buffer)
            except EventUnavailable:
                break

    def wait_frame(self):
        self.frame_state = wait_frame(self.handle)


class SpaceObject(object):
    def __init__(
            self,
            session: SessionObject,
            reference_space_type: ReferenceSpaceType = ReferenceSpaceType.STAGE,
            pose_in_reference_space: Posef = None,
    ):
        if pose_in_reference_space is None:
            pose_in_reference_space = Posef()
        reference_space_create_info = ReferenceSpaceCreateInfo(
            reference_space_type=reference_space_type,
            pose_in_reference_space=pose_in_reference_space,
        )
        self.handle = create_reference_space(session.handle, reference_space_create_info)


__all__ = [
    "Eye",
    "GlfwWindow",
    "InstanceObject",
    "SessionObject",
    "SpaceObject",
    "SystemObject",
]
