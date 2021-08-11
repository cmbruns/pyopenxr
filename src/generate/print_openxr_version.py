# This script prints the current version of the OpenXR API

import re
import xrg

file_string = xrg.get_header_as_string()

# We expect a line in openxr.h like
#   "#define XR_CURRENT_API_VERSION XR_MAKE_VERSION(1, 0, 17)"
version_match = re.search(
    r"define XR_CURRENT_API_VERSION XR_MAKE_VERSION\((\d+), (\d+), (\d+)\)", file_string
)

major = int(version_match.group(1))
minor = int(version_match.group(2))
patch = int(version_match.group(3))

print(f"{major}.{minor}.{patch}")
