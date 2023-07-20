import xr


class SessionManager(object):
    """
    Context manager that automatically destroys an OpenXR session after use
    """
    def __init__(self, instance: xr.Instance, create_info: xr.SessionCreateInfo) -> None:
        self.session = xr.create_session(instance=instance, create_info=create_info)

    def __enter__(self) -> xr.Session:
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if self.session is not None:
            xr.destroy_session(self.session)
            self.session = None


__all__ = [
    "SessionManager",
]
