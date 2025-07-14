"""
Implement pkg_resources functions using importlib
"""

import atexit
import contextlib
import importlib.resources

_exit_stack = contextlib.ExitStack()
atexit.register(_exit_stack.close)


def resource_exists(package: str, resource_name: str) -> bool:
    return (importlib.resources.files(package) / resource_name).exists()


def resource_filename(package: str, resource_name: str) -> str:
    """Replacement for pkg_resources.resource_filename"""
    ref = importlib.resources.files(package) / resource_name
    path = _exit_stack.enter_context(importlib.resources.as_file(ref))
    return str(path)


def resource_stream(package: str, resource_name: str):
    return importlib.resources.open_binary(package, resource_name)


def resource_string(package: str, resource_name: str) -> bytes:
    """Replacement for pkg_resources.resource_string"""
    ref = importlib.resources.files(package).joinpath(resource_name)
    return ref.read_bytes()


__all__ = [
    "resource_exists",
    "resource_filename",
    "resource_stream",
    "resource_string",
]
