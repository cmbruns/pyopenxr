"""
Implement pkg_resources functions using importlib
"""

import atexit
import contextlib
import importlib.resources

_exit_stack = None


def resource_filename(package: str, filename: str) -> str:
    """Replacement for pkg_resources.resource_filename"""
    global _exit_stack
    if _exit_stack is None:
        _exit_stack = contextlib.ExitStack()
        atexit.register(_exit_stack.close)
    ref = importlib.resources.files(package) / filename
    path = _exit_stack.enter_context(importlib.resources.as_file(ref))
    return str(path)


def resource_string(package: str, filename: str) -> bytes:
    """Replacement for pkg_resources.resource_string"""
    ref = importlib.resources.files(package).joinpath(filename)
    contents = ref.read_bytes()
    return contents
