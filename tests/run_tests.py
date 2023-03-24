# Programmatically run as if "pytest" on command line
# NOTE: run this from the top level pyopenxr folder, *NOT* from this "tests" folder.

import pytest

retcode = pytest.main()
