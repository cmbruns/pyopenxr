import sys
import typing

import xr

from .session_manager import FrameManager, SessionManager


class XrContext(object):
    """
    High level api2 pyopenxr class used to automatically initialize the
    session, state, system, etc., and run the frame loop.
    """
    def __init__(
            self,
            instance_create_info: xr.InstanceCreateInfo,
            system_get_info: xr.SystemGetInfo = None,
            session_create_info: xr.SessionCreateInfo = None,
            reference_space_type: xr.ReferenceSpaceType = xr.ReferenceSpaceType.STAGE,
    ) -> None:
        # TODO: take arguments for optional create_info objects
        if instance_create_info is None:
            instance_create_info = xr.InstanceCreateInfo(
                enabled_extension_names=[xr.KHR_OPENGL_ENABLE_EXTENSION_NAME],
            )
        enabled = [n.decode() for n in instance_create_info.enabled_extension_names]
        if xr.KHR_OPENGL_ENABLE_EXTENSION_NAME in enabled:
            self.graphics_extension = xr.KHR_OPENGL_ENABLE_EXTENSION_NAME
        elif xr.MND_HEADLESS_EXTENSION_NAME in enabled:
            self.graphics_extension = xr.MND_HEADLESS_EXTENSION_NAME
        else:
            raise NotImplementedError
        self.instance_create_info = instance_create_info
        if system_get_info is None:
            system_get_info = xr.SystemGetInfo()
        self.system_get_info = system_get_info
        if session_create_info is None:
            session_create_info = xr.SessionCreateInfo()
        self.reference_space_type = reference_space_type
        self.session_create_info = session_create_info
        self.instance = None
        self.system_id = None
        self.graphics_context = None
        self.session = None
        self.reference_space = None
        self.swapchains = None
        self.session_manager = None

    def __enter__(self):
        try:
            # Chain many dependent context managers
            self.instance = xr.Instance(self.instance_create_info).__enter__()
            self.system_id = xr.get_system(self.instance, self.system_get_info)
            if self.graphics_extension == xr.MND_HEADLESS_EXTENSION_NAME:
                graphics_binding_pointer = None
            elif self.graphics_extension == xr.KHR_OPENGL_ENABLE_EXTENSION_NAME:
                self.graphics_context = xr.api2.GLFWContext(
                    instance=self.instance,
                    system_id=self.system_id,
                ).__enter__()
                graphics_binding_pointer = self.graphics_context.graphics_binding_pointer
            else:
                raise NotImplementedError  # More graphics contexts!
            self.session_create_info.system_id = self.system_id
            self.session_create_info.next = graphics_binding_pointer
            self.session = xr.Session(
                instance=self.instance,
                create_info=self.session_create_info,
            ).__enter__()
            self.reference_space = xr.create_reference_space(
                session=self.session,
                create_info=xr.ReferenceSpaceCreateInfo(
                    reference_space_type=self.reference_space_type,
                ),
            )
            if self.graphics_extension == xr.MND_HEADLESS_EXTENSION_NAME:
                self.swapchains = None
            elif self.graphics_extension == xr.KHR_OPENGL_ENABLE_EXTENSION_NAME:
                self.swapchains = xr.api2.XrSwapchains(
                    instance=self.instance,
                    system_id=self.system_id,
                    session=self.session,
                    context=self.graphics_context,
                    view_configuration_type=xr.ViewConfigurationType.PRIMARY_STEREO,
                    reference_space=self.reference_space,
                ).__enter__()
            else:
                raise NotImplementedError  # More graphics contexts!
            self.session_manager = SessionManager(
                instance=self.instance,
                system_id=self.system_id,
                session=self.session,
                is_headless=self.graphics_extension == xr.MND_HEADLESS_EXTENSION_NAME,
                swapchains=self.swapchains,
            ).__enter__()
            return self
        except BaseException:
            # Clean up partially constructed context manager chain
            self.__exit__(*sys.exc_info())
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Unwind chained context managers in reverse order of creation
        if self.session_manager is not None:
            self.session_manager.__exit__(exc_type, exc_val, exc_tb)
            self.session_manager = None
        if self.swapchains is not None:
            self.swapchains.__exit__(exc_type, exc_val, exc_tb)
            self.swapchains = None
        if self.reference_space is not None:
            xr.destroy_space(space=self.reference_space)
            self.reference_space = None
        if self.session is not None:
            self.session.__exit__(exc_type, exc_val, exc_tb)
            self.session = None
        if self.graphics_context is not None:
            self.graphics_context.__exit__(exc_type, exc_val, exc_tb)
            self.graphics_context = None
        self.system_id = None
        if self.instance is not None:
            self.instance.__exit__(exc_type, exc_val, exc_tb)
            self.instance = None

    def frames(self) -> typing.Generator[FrameManager, None, None]:
        """
        The OpenXR frame loop.
        """
        if self.instance is None:  # Called in non-context manager context
            with self:
                for frame in self.session_manager.frames():
                    yield frame
        else:
            for frame in self.session_manager.frames():
                yield frame


__all__ = [
    "XrContext",
]
