from typing import Optional, Union
from .enums import Result

# raise_on_qualified_success is a module setting to control whether positive non-SUCCESS result
# trigger exceptions.
raise_on_qualified_success = True


class XrException(Exception):
    """Base class for all OpenXR exceptions."""

    @staticmethod
    def is_exception() -> bool:
        return True


class ResultException(XrException):
    """Exception related to return value of and OpenXR function."""

    @staticmethod
    def get_result_enum() -> Optional[Result]:
        return None


class ResultError(ResultException):
    """Error during OpenXR function call."""


class QualifiedSuccessResult(ResultException):
    """An OpenXR function returned a non-error status other than SUCCESS"""

    @staticmethod
    def is_exception() -> bool:
        return raise_on_qualified_success


class SuccessResult(ResultException):
    """An OpenXR function call completed successfully."""

    @staticmethod
    def is_exception() -> bool:
        return False

    @staticmethod
    def get_result_enum() -> Result:
        return Result.SUCCESS


class TimeoutExpired(QualifiedSuccessResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.TIMEOUT_EXPIRED


class EventUnavailable(QualifiedSuccessResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.EVENT_UNAVAILABLE


class ValidationFailureError(ResultError):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_VALIDATION_FAILURE


# TODO: specific exceptions for every result type


_exception_map = {
    Result.SUCCESS: SuccessResult,
    Result.TIMEOUT_EXPIRED: TimeoutExpired,
    Result.ERROR_VALIDATION_FAILURE: ValidationFailureError,
    Result.EVENT_UNAVAILABLE: EventUnavailable,
}


def check_result(
    xr_result: Result, message: str = None
) -> Union[XrException, SuccessResult]:
    if xr_result in _exception_map:
        xr_result_exception = _exception_map[xr_result]
    else:
        if xr_result.value < 0:
            xr_result_exception = ResultError
        elif xr_result.value > 1:
            xr_result_exception = QualifiedSuccessResult
        else:
            xr_result_exception = SuccessResult
    if message is None:
        # TODO: I see a message in the logging...
        return xr_result_exception()
    else:
        return xr_result_exception(message)


__all__ = [
    "check_result",
    "raise_on_qualified_success",
    "EventUnavailable",
    "ResultError",
    "XrException",
    "ResultException",
    "QualifiedSuccessResult",
]
