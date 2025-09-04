import xr


def test_structure_type():
    # Basic access
    ep_type = xr.StructureType.EXTENSION_PROPERTIES
    assert ep_type.name == "EXTENSION_PROPERTIES"
    assert ep_type.value == 2
    # Strings
    # assert repr(ep_type) == "xr.StructureType.EXTENSION_PROPERTIES"
    # assert str(ep_type) == "xr.StructureType.EXTENSION_PROPERTIES"
    # Equality
    assert xr.StructureType.EXTENSION_PROPERTIES == ep_type
    assert xr.StructureType.EXTENSION_PROPERTIES == xr.StructureType.EXTENSION_PROPERTIES
    assert xr.StructureType.EXTENSION_PROPERTIES != xr.StructureType.UNKNOWN
    # Iteration
    assert len(xr.StructureType) > 1
    for foo in xr.StructureType:
        pass
    print(dir(xr.StructureType))


if __name__ == "__main__":
    import pytest
    import os
    # Run pytest on this file
    pytest.main([os.path.abspath(__file__)])
