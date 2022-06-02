import abc


class IPlatformPlugin(abc.ABC):
    @property
    @abc.abstractmethod
    def instance_extensions(self):
        pass


class Win32PlatformPlugin(IPlatformPlugin):
    @property
    def instance_extensions(self):
        return []
