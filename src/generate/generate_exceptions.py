# This script creates an updated version of xr/exceptions.py

import inspect
import re

from clang.cindex import CursorKind

import xrg
from xrg import Api
from xrg.registry import xr_registry


def camel_word(word: re.Match) -> str:
    s = word.group(1) + word.group(2)
    if s in ("FB", "KHR", "MSFT", ):  # TODO more vendor tags
        return s
    result = word.group(1).upper() + word.group(2).lower()
    return result


def main():
    cg = xrg.CodeGenerator(
        [
            CursorKind.ENUM_DECL,
        ]
    )

    all_exceptions = set()

    print(inspect.cleandoc('''
        from typing import Optional
        from xr.enums import Result
        
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
    '''))

    all_exceptions.update([
        "XrException",
        "ResultException",
        "ErrorResult",
        "QualifiedSuccessResult",
    ])

    exception_map = {}

    result_reg = xr_registry.find(f'enums[@name="XrResult"]')

    for enum in cg.items:
        if enum.name() != "Result":
            continue
        for result_item in enum.values:
            if result_item.name() == "_MAX_ENUM":
                continue
            name = result_item.name()
            name = re.sub(r"(?:\b|_)([^_])([^_]*)", camel_word, name)
            if name.startswith("Error"):
                name = name[5:] + name[:5]
            # Each result value type gets its own exception
            if result_item.value < 0:
                base = "ErrorResult"
            elif result_item.value > 0:
                base = "QualifiedSuccessResult"
            elif result_item.value == 0:
                base = "ResultException"  # Success
            else:
                assert False
            doc = None
            val_reg = result_reg.find(f'enum[@name="{result_item.name(api=Api.C)}"]')
            if val_reg is not None:
                doc = val_reg.attrib.get("comment", None)
            code = "\n\n"
            if doc is None:
                code += inspect.cleandoc(f'''
                    class {name}({base}):
                        @staticmethod
                        def get_result_enum() -> Result:
                            return Result.{result_item.name()}
                ''')
            else:
                code += inspect.cleandoc(f'''
                    class {name}({base}):
                        """{doc}"""

                        def __init__(self, message=None):
                            if message is None:
                                super().__init__(
                                    "{doc}"
                                )
                            else:
                                super().__init__(message)

                        @staticmethod
                        def get_result_enum() -> Result:
                            return Result.{result_item.name()}
                ''')
            all_exceptions.add(name)
            exception_map[result_item.name()] = name
            print(code)

    print("\n\n_exception_map = {")
    for k, v in exception_map.items():
        print(f"    Result.{k}: {v},")
    print("}\n\n")

    print(inspect.cleandoc('''
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
    '''))

    print("\n\n__all__ = [")
    for t in sorted(all_exceptions):
        print(f'    "{t}",')
    print("]")


if __name__ == "__main__":
    main()
