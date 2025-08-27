import copy
import importlib
import inspect
import pkgutil
from typing import Optional

import sys
import textwrap

import requests

import xr
import xr.ext
from class_docstring_data import class_docstrings
from function_docstring_data import function_docstrings


def get_instance_docstring():
    doc = inspect.getdoc(xr.Instance)
    return inspect.cleandoc(doc) if doc else ""


def compare_docstrings(live: str, stored: str) -> bool:
    return live.strip() == stored.strip()


def check_spec_url(url: str) -> bool:
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False


def check_instance_docstring():
    qualified_name = "xr.Instance"
    live_doc = get_instance_docstring()
    stored_entry = class_docstrings.get(qualified_name)

    if not stored_entry:
        print(f"❌ No stored docstring for {qualified_name}")
        return

    stored_doc = stored_entry["docstring"]
    spec_url = stored_entry.get("spec_url", "")

    if compare_docstrings(live_doc, stored_doc):
        print(f"✅ Docstring for {qualified_name} matches stored version.")
    else:
        print(f"⚠️ Docstring mismatch for {qualified_name}")
        print("Live:\n", live_doc)
        print("Stored:\n", stored_doc)

    if spec_url:
        if check_spec_url(spec_url):
            print(f"🔗 Spec URL reachable: {spec_url}")
        else:
            print(f"❌ Spec URL unreachable: {spec_url}")


def is_relevant(obj):
    return inspect.isclass(obj) or inspect.isfunction(obj) or inspect.ismodule(obj)


def has_docstring(obj):
    doc = inspect.getdoc(obj)
    return bool(doc and doc.strip())


def has_explicit_docstring(obj):
    doc = getattr(obj, "__doc__", None)
    if not isinstance(doc, str):
        return False
    doc = doc.strip()
    # Filter out generic or placeholder strings
    if not doc or doc in {"An enumeration."}:
        return False
    return True


def count_xr_docstrings():
    total = 0
    with_doc = 0
    docstring_items = []

    for name in dir(xr):
        if name.startswith("_"):
            continue

        try:
            obj = getattr(xr, name)
        except Exception:
            continue  # Skip problematic attributes

        if not is_relevant(obj):
            continue

        total += 1
        if has_explicit_docstring(obj):
            with_doc += 1
            docstring_items.append(f"{name}: ✅")

    print(f"🔍 Scanned {total} items in xr namespace")
    print(f"📘 Found {with_doc} with non-empty docstrings")
    print("\nSample with docstrings:")
    for item in docstring_items[:10]:
        print("  ", item)


def write_docstrings(entries: dict[str, dict[str, str]], label="class", file=sys.stdout):
    file.write(inspect.cleandoc(f"""
        import inspect
        
        {label}_docstrings = {{
    """))
    file.write("\n")
    for item_name in sorted(entries):
        entry = entries[item_name]
        file.write(f'{4 * " "}"{item_name}": {{\n')  # "xr.Instance": {
        for key in sorted(entry):
            value = entry[key]
            if '"""' in value:
                raise ValueError(f'Docstring for {item_name}.{key} contains unescaped triple quotes')
            file.write(f'{8 * " "}"{key}": ')  # "docstring":
            if key == "docstring":
                file.write('inspect.cleandoc("""\n')
                file.write(textwrap.indent(value, 12 * " "))
                file.write(f'\n{8 * " "}"""),\n')
            else:
                file.write(f'"{value}",\n')
        file.write(f'{4 * " "}}},\n')
    file.write(inspect.cleandoc(f"""
        }}
        
        __all__ = [
            "{label}_docstrings",
        ]
    """))
    file.write("\n")


def get_doc(obj) -> Optional[str]:
    doc = getattr(obj, "__doc__", None)
    if not doc:
        return None
    if doc in {"An enumeration."}:
        return None
    return doc


def enumerate_class_docstrings(clazz):
    for member_name, member in inspect.getmembers(clazz):
        if not hasattr(member, "__name__"):
            continue
        if member_name.startswith("_") and member_name != "__init__":
            continue
        doc = get_doc(member)
        if doc is not None:
            yield doc, (clazz, member)
        if inspect.isclass(member):
            for doc, path in enumerate_class_docstrings(member):
                print(path)
                yield doc, (clazz, *path)


def enumerate_docstrings(modules=(xr, xr.ext)):
    for module in modules:
        if not hasattr(module, "__name__"):
            continue
        for name in dir(module):
            obj = getattr(module, name)
            if not hasattr(obj, "__name__"):
                continue
            doc = get_doc(obj)
            if doc is not None:
                yield doc, (module, obj)
            if inspect.isclass(obj):
                for doc, path in enumerate_class_docstrings(obj):
                    yield doc, (module, *path)


def get_class_url(class_) -> Optional[str]:
    if issubclass(class_, xr.ResultException):
        return "https://registry.khronos.org/OpenXR/specs/1.1/man/html/XrResult.html"
    else:
        c_name = f"Xr{class_.__name__}"  # TODO: cases
        return check_url(f"https://registry.khronos.org/OpenXR/specs/1.1/man/html/{c_name}.html")


def camelize_function_name(snake_str: str) -> str:
    # Trick to help with type_format_exceptions below
    pass1 = snake_str.replace("opengl_es", "opengles")
    parts = pass1.strip("_").split("_")
    if not parts:
        return ""
    type_format_exceptions = {
        # Section 2.9.6 of OpenXR spec
        "opengl": "OpenGL",
        "opengles": "OpenGLES",
        "egl": "EGL",
        "d3d": "D3D",
    }
    camelled = []
    for part in parts:
        if part in type_format_exceptions:
            camelled.append(type_format_exceptions[part])
        else:
            camelled.append(part.capitalize())
    return "".join(camelled)


def check_url(url: str) -> Optional[str]:
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        if response.status_code == 200:
            return url
    except requests.RequestException:
        pass
    return None


def store_class_docstrings():
    updated_class_docstrings = copy.deepcopy(class_docstrings)
    for doc, path in enumerate_docstrings():
        clazz = path[-1]
        if not inspect.isclass(clazz):
            continue
        url = get_class_url(clazz)
        qualified_name = ".".join([x.__name__ for x in path])
        updated_class_docstrings[qualified_name] = {}
        entry = updated_class_docstrings[qualified_name]
        if url is not None:
            entry["spec_url"] = url
        entry["docstring"] = doc
    with open("class_docstring_data.py", "w", encoding="utf-8") as file:
        write_docstrings(updated_class_docstrings, label="class", file=file)


def store_function_docstrings():
    updated_function_docstrings = copy.deepcopy(function_docstrings)
    for doc, path in enumerate_docstrings():
        func = path[-1]
        if not inspect.isfunction(func):
            continue
        n = func.__name__
        if n.startswith("_") and n != "__init__":
            continue
        qualified_name = ".".join([x.__name__ for x in path])
        vendor_prefix = ""
        extension = path[-2]
        if inspect.isclass(extension) and issubclass(extension, xr.ext.InstanceExtension):
            extension_name = getattr(extension, "NAME")
            parts = extension_name.split("_")
            if len(parts) > 1:
                vendor_prefix = parts[1]
        if hasattr(extension, "VENDOR_PREFIX"):
            vendor_prefix = extension.VENDOR_PREFIX
        c_name = f"xr{camelize_function_name(func.__name__)}{vendor_prefix}"
        url = check_url(f"https://registry.khronos.org/OpenXR/specs/1.1/man/html/{c_name}.html")
        updated_function_docstrings[qualified_name] = {}
        entry = updated_function_docstrings[qualified_name]
        if url is not None:
            entry["spec_url"] = url
        entry["docstring"] = doc
        print(qualified_name, entry)
    with open("function_docstring_data.py", "w", encoding="utf-8") as file:
        write_docstrings(updated_function_docstrings, label="function", file=file)


def find_extension_modules():
    xr_ext = importlib.import_module("xr.ext")
    for finder, name, is_pkg in pkgutil.iter_modules(xr_ext.__path__, "xr.ext" + "."):
        try:
            submod = importlib.import_module(name)
            if hasattr(submod, '__path__'):  # It's a package
                for _, subname, _ in pkgutil.iter_modules(submod.__path__, name + "."):
                    yield subname
        except Exception as e:
            print(f"Skipping {name}: {e}")


if __name__ == "__main__":
    # check_instance_docstring()
    # count_xr_docstrings()
    # write_docstrings(class_docstrings)
    # store_class_docstrings()
    # store_function_docstrings()
    for module in find_extension_modules():
        print(module)
