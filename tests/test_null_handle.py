import xr


def test_null_handle():
    assert not xr.NULL_HANDLE
    assert bool(xr.NULL_HANDLE) == False
    assert "fish" != xr.NULL_HANDLE
    assert xr.NULL_HANDLE != "fish"
    assert xr.NULL_HANDLE is None
    assert None is xr.NULL_HANDLE
    assert xr.NULL_HANDLE == None
    assert None == xr.NULL_HANDLE
    uninitialized_instance = xr.Instance()
    assert uninitialized_instance == xr.NULL_HANDLE
    assert xr.NULL_HANDLE == uninitialized_instance
    assert uninitialized_instance != "fish"
    # Certain functions can be retrieved without a valid instance
    xr.get_instance_proc_addr(None, "xrEnumerateInstanceExtensionProperties")
    xr.get_instance_proc_addr(xr.NULL_HANDLE, "xrEnumerateInstanceExtensionProperties")
    try:
        # Other functions require a valid instance
        pfn = xr.get_instance_proc_addr(xr.NULL_HANDLE, "xrGetSystem")
        assert False
    except xr.HandleInvalidError:
        pass  # expected error
    try:
        # Other functions require a valid instance
        pfn = xr.get_instance_proc_addr(uninitialized_instance, "xrGetSystem")
        assert False
    except xr.HandleInvalidError:
        pass  # expected error


if __name__ == "__main__":
    test_null_handle()
