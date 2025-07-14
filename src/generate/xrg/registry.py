from importlib.resources import files
from xml.etree import ElementTree

registry_file = files("xrg") / "headers" / "xr.xml"
try:
    # open the resource as a binary stream
    with registry_file.open("rb") as stream:
        xr_registry = ElementTree.parse(stream).getroot()
except FileNotFoundError:
    xr_registry = None

__all__ = [
    "xr_registry",
]
