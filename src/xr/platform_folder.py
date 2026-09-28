import platform


def platform_folder() -> tuple[str, str]:
    if platform.system() == "Windows":
        return "windows_x86_64", "dll"
    if platform.machine() == "x86_64":
        return "x86_64", "so"
    elif platform.machine() == "aarch64":
        return "aarch64", "so"
    else:
        print(f"platform.system() = '{platform.system()}'; platform.machine() = '{platform.machine()}'")
        raise NotImplementedError


__all__ = [
    "platform_folder",
]
