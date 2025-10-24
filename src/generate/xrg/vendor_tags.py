from .registry import xr_registry

vendor_tags = []
for tags in xr_registry.findall("tags"):
    for tag in tags.findall("tag"):
        vendor_tags.append(tag.attrib["name"])
vendor_tags.append("EXTX")
vendor_tags.append("MNDX")
