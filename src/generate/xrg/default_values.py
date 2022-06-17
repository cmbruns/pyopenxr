
# These default values override others
default_values = {
    "Structure": {
        "ApplicationInfo": {
            "Field": {
                "application_name": "sys.argv[0]",
                "application_version": "Version(0)",  # it's an int
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
        "ReferenceSpaceCreateInfo": {
            "Field": {
                "reference_space_type": "ReferenceSpaceType.STAGE",
            }
        },
    }
}

__all__ = [
    "default_values"
]
