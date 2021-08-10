from typing import Union
from .enums import Result

raise_on_qualified_success = True


class XrException(Exception):
    """Base class for all OpenXR exceptions."""

    @staticmethod
    def is_exception():
        return True


class XrErrorResult(XrException):
    """Error during OpenXR function call."""


class XrQualifiedSuccessResult(XrException):
    """An OpenXR function returned a non-error status other than SUCCESS"""

    @staticmethod
    def is_exception():
        return raise_on_qualified_success


class XrSuccessResult(object):
    """An OpenXR function call completed successfully."""
    def __init__(self, _unused: str = None):
        pass

    @staticmethod
    def is_exception():
        return False


# TODO: specific exceptions for every result type


_exception_map = {
    Result.SUCCESS: XrSuccessResult,
}


def check_result(xr_result_int: int, message: str = None) -> Union[XrException, XrSuccessResult]:
    xr_result_enum = Result(xr_result_int)
    if xr_result_enum in _exception_map:
        xr_result_exception = _exception_map[xr_result_enum]
    else:
        if xr_result_int < 0:
            xr_result_exception = XrErrorResult
        elif xr_result_int > 1:
            xr_result_exception = XrQualifiedSuccessResult
        else:
            xr_result_exception = XrSuccessResult
    if message is None:
        return xr_result_exception()
    else:
        return xr_result_exception(message)


__all__ = [
    "check_result",
    "raise_on_qualified_success",
    "XrErrorResult",
    "XrException",
    "XrQualifiedSuccessResult",
]
