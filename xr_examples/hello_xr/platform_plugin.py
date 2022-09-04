import abc
from ctypes import Structure
from typing import List, Optional


class IPlatformPlugin(abc.ABC):
    """Wraps platform-specific implementation so the main openxr program can be platform-independent."""

    @abc.abstractmethod
    def __enter__(self):
        pass

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Clean up platform resources."""

    @property
    @abc.abstractmethod
    def instance_create_extension(self) -> Optional[Structure]:
        """OpenXR instance-level extensions required by this platform."""

    @property
    @abc.abstractmethod
    def instance_extensions(self) -> List[str]:
        """OpenXR instance-level extensions required by this platform."""

    @abc.abstractmethod
    def update_options(self, options) -> None:
        pass
