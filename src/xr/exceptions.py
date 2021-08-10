from typing import Union


class XrSuccess(object):
    """Class representing a successful OpenXR function call result."""
    def __init__(self, message: str = None):
        pass


class XrException(Exception):
    """Base class for all OpenXR exceptions."""


class XrError(XrException):
    """OpenXR error exception."""


class XrQualifiedSuccess(XrException):
    """An OpenXR function returned a non-error status other than SUCCESS"""


# TODO: specific exceptions for every result type


def check_result(xr_result: int, message: str = None) -> Union[XrException, XrSuccess]:
    if xr_result < 0:
        result = XrException
    elif xr_result > 1:
        result = XrQualifiedSuccess
    else:
        result = XrSuccess
    if message is None:
        return result()
    else:
        return result(message)


def is_exception(exception: Union[XrException, XrSuccess]) -> bool:
    return isinstance(exception, XrException)


__all__ = [
    "check_result",
    "is_exception",
    "XrError",
    "XrException",
    "XrQualifiedSuccess",
]
