# This script creates an updated version of xr/version.py

import re
import inspect

from clang.cindex import CursorKind

# These variables are filled in by cmake's configure_file process
# TODO: replace with symbolic file path
openxr_header = "C:/Program Files/OPENXR/include/openxr/openxr_loader.h"
# openxr_header = "@OPENXR_INCLUDE_FILE@"

with open(openxr_header) as f:
    file_string = f.read()
