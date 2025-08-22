import copy
import inspect
import sys
import textwrap

import requests

import xr
import xr.ext
from class_docstring_data import class_docstrings


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


def exercise_docstring_roundtrip():
    updated_class_docstrings = copy.deepcopy(class_docstrings)

    for module in [xr, xr.ext]:
        for name in dir(module):
            obj = getattr(module, name)
            doc = getattr(obj, "__doc__", None)
            if not doc or doc in {"An enumeration."}:
                continue
            if not inspect.isclass(obj):
                continue
            qualified_name = f"{module.__name__}.{name}"

            c_name = f"Xr{name}"  # TODO: cases
            url = f"https://registry.khronos.org/OpenXR/specs/1.1/man/html/{c_name}.html"
            try:
                response = requests.head(url, allow_redirects=True, timeout=5)
                if response.status_code != 200:
                    url = None
            except requests.RequestException:
                url = None
            
            updated_class_docstrings[qualified_name] = {}
            if url is not None:
                updated_class_docstrings[qualified_name]["spec_url"] = url
            updated_class_docstrings[qualified_name]["docstring"] = doc

    with open("class_docstring_data.py", "w") as file:
        write_docstrings(updated_class_docstrings, label="class", file=file)


if __name__ == "__main__":
    # check_instance_docstring()
    # count_xr_docstrings()
    # write_docstrings(class_docstrings)
    exercise_docstring_roundtrip()
