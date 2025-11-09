from ctypes import Structure
from typing import Optional

import android  # I'm inventing this module in a separate project

import xr
from .platform_plugin import IPlatformPlugin


class AndroidPlatformPlugin(IPlatformPlugin):
    def __init__(self):
        super().__init__()
        self.instance_create_info_android = xr.InstanceCreateInfoAndroidKHR(
            application_vm=android.get_vm(),
            application_activity=android.get_activity(),
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @property
    def instance_create_extension(self) -> Optional[Structure]:
        return self.instance_create_info_android

    @property
    def instance_extensions(self):
        return [xr.KHR_ANDROID_CREATE_INSTANCE_EXTENSION_NAME]

    def update_options(self, options) -> None:
        pass
