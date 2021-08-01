import typing

from clang.cindex import Config, CursorKind, Index
import clang.cindex


def generate_ast_elements(
    file_name, file_string
) -> typing.Generator[clang.cindex.Cursor, None, None]:
    index = Index.create()
    tu = index.parse(
        path=file_name,
        unsaved_files=((file_name, file_string),),
        args=[
            "-fparse-all-comments",  # Alas to no avail; these lame openxr headers contain no docstrings.
        ],
        options=clang.cindex.TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD,
    )
    tu_file_name = str(tu.cursor.spelling)
    for child in tu.cursor.get_children():
        if not str(child.location.file) == tu_file_name:
            continue  # Please don't leave this file
        yield child
        continue


def pysymbol_from_csymbol(csymbol: str):
    if csymbol.startswith("XR_"):
        csymbol = csymbol[3:]
    return csymbol


def pyvalue_from_cvalue(cvalue: str):
    try:
        result = int(cvalue)
        return result
    except ValueError:
        pass
    if "(" in cvalue:
        return None
    return cvalue


def constant_parser(
    cursor: clang.cindex.Cursor, lines: typing.List[str]
) -> typing.Tuple[str]:
    if cursor.kind == CursorKind.MACRO_DEFINITION:
        if str(cursor.spelling).endswith("_"):  # e.g. "OPENXR_H_" header guard
            return None
        line = cursor.extent.start.line
        if line != cursor.extent.end.line:
            return None  # Ignore multiline #defines
        column = cursor.extent.start.column
        column2 = cursor.extent.end.column
        this_line = lines[line - 1]
        value = str(this_line[column + len(cursor.spelling) - 1 : column2]).strip()
        name = pysymbol_from_csymbol(cursor.spelling)
        value = pyvalue_from_cvalue(value)
        if value is None:
            return None
        # TODO: return a constant object, name, value, cursor
        return (f"{name} = {value}",)


def main():
    # TODO: configure header location using CMAKE
    file_name = "C:/Program Files/OPENXR/include/openxr/openxr.h"
    with open(file_name) as f:
        file_string = f.read()
    lines = file_string.split("\n")
    Config.set_library_file("C:/Program Files/LLVM/bin/libclang.dll")
    for cursor in generate_ast_elements(file_name, file_string):
        result = constant_parser(cursor, lines)
        if result is not None:
            print("\n".join(result), "\n")


if __name__ == "__main__":
    main()
