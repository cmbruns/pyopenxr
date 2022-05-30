import abc


class IPlatformPlugin(abc.ABC):
    @abc.abstractmethod
    def get_instance_extensions(self):
        pass


class Win32PlatformPlugin(IPlatformPlugin):
    def get_instance_extensions(self):
        return []
