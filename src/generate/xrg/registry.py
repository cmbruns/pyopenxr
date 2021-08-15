from pkg_resources import resource_exists, resource_stream
from xml.etree import ElementTree

xr_registry = None
if resource_exists("xrg", "headers/xr.xml"):
    with resource_stream("xrg", "headers/xr.xml") as stream:
        xr_registry = ElementTree.parse(stream).getroot()

__all__ = [
    "xr_registry",
]
