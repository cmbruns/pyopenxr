
# These default values override others
default_values = {
    "Structure": {
        "ApplicationInfo": {
            "Field": {
                "application_name": "sys.argv[0]",
                "application_version": "Version(0)",
                "engine_name": '"pyopenxr"',
                "engine_version": "PYOPENXR_CURRENT_API_VERSION",
                "api_version": "XR_CURRENT_API_VERSION",
            }
        },
        "InstanceCreateInfo": {
            "Field": {
                "application_info": "ApplicationInfo()",
            }
        },
    }
}

__all__ = [
    "default_values"
]
