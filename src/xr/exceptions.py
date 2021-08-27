from typing import Optional
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

    @staticmethod
    def is_exception() -> bool:
        return False


class ErrorResult(ResultException):
    """Error during OpenXR function call."""

    @staticmethod
    def is_exception() -> bool:
        return True


class QualifiedSuccessResult(ResultException):
    """An OpenXR function returned a non-error status other than SUCCESS"""

    @staticmethod
    def is_exception() -> bool:
        return raise_on_qualified_success


class Success(ResultException):
    """Function successfully completed."""

    def __init__(self, message=None):
        if message is None:
            super().__init__("Function successfully completed.")
        else:
            super().__init__(message)

    @staticmethod
    def is_exception() -> bool:
        return False

    @staticmethod
    def get_result_enum() -> Result:
        return Result.SUCCESS


class TimeoutExpired(QualifiedSuccessResult):
    """The specified timeout time occurred before the operation could complete."""

    def __init__(self, message=None):
        if message is None:
            super().__init__("The specified timeout time occurred before the operation could complete.")
        else:
            super().__init__(message)

    @staticmethod
    def get_result_enum() -> Result:
        return Result.TIMEOUT_EXPIRED


class EventUnavailable(QualifiedSuccessResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.EVENT_UNAVAILABLE


class ValidationFailureError(ErrorResult):
    @staticmethod
    def get_result_enum() -> Result:
        return Result.ERROR_VALIDATION_FAILURE


# TODO: specific exceptions for every result type


_exception_map = {
    Result.SUCCESS: Success,
    Result.TIMEOUT_EXPIRED: TimeoutExpired,
    Result.ERROR_VALIDATION_FAILURE: ValidationFailureError,
    Result.EVENT_UNAVAILABLE: EventUnavailable,
}


def check_result(
    xr_result: Result, message: str = None
) -> XrException:
    if xr_result in _exception_map:
        xr_result_exception = _exception_map[xr_result]
    else:
        if xr_result.value < 0:
            xr_result_exception = ErrorResult
        elif xr_result.value > 1:
            xr_result_exception = QualifiedSuccessResult
        else:
            xr_result_exception = Success
    if message is None:
        # TODO: I see a message in the logging...
        return xr_result_exception()
    else:
        return xr_result_exception(message)


__all__ = [
    "check_result",
    "raise_on_qualified_success",
    "EventUnavailable",
    "ErrorResult",
    "XrException",
    "ResultException",
    "QualifiedSuccessResult",
    "Success",
    "TimeoutExpired",
]
