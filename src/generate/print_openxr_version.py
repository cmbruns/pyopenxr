# This script prints the current version of the OpenXR API

import re

# These variables are filled in by cmake's configure_file process
openxr_header = "@OPENXR_INCLUDE_FILE@"

with open(openxr_header) as f:
    file_string = f.read()

# We expect a line in openxr.h like
#   "#define XR_CURRENT_API_VERSION XR_MAKE_VERSION(1, 0, 17)"
version_match = re.search(
    r"define XR_CURRENT_API_VERSION XR_MAKE_VERSION\((\d+), (\d+), (\d+)\)",
    file_string
)

major = int(version_match.group(1))
minor = int(version_match.group(2))
patch = int(version_match.group(3))

print(f"{major}.{minor}.{patch}")
