import xr


class InstanceManager(object):
    def __init__(self, create_info: xr.InstanceCreateInfo):
        self.instance = xr.create_instance(create_info=create_info)

    def __enter__(self):
        return self.instance

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.instance is not None:
            xr.destroy_instance(self.instance)
            self.instance = None


__all__ = [
    "InstanceManager",
]
