from ctypes import Structure
from typing import Optional

from xr_examples.hello_xr.platform_plugin import IPlatformPlugin


class XlibPlatformPlugin(IPlatformPlugin):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @property
    def instance_create_extension(self) -> Optional[Structure]:
        return None

    @property
    def instance_extensions(self):
        return []

    def update_options(self, options) -> None:
        pass
