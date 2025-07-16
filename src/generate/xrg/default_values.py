
# These default values override others
default_values = {
    "Function": {
        "get_system": {
            "Parameter": {
                "get_info": "SystemGetInfo()",
            },
        },
    },
    "Structure": {
        "ApplicationInfo": {
            "Field": {
                "application_name": "os.path.basename(sys.argv[0])",
                "engine_name": '"pyopenxr"',
                "engine_version": "PYOPENXR_CURRENT_API_VERSION",
                "api_version": "Version(1, 0, XR_VERSION_PATCH)",
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
