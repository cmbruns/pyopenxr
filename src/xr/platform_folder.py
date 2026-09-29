import platform
import sys


def platform_folder() -> tuple[str, str]:
    """
    :return: Folder name and shared library suffix for the current platform
    """

    # Windows?
    if platform.system() == "Windows":
        return "windows_x86_64", "dll"

    # Android?
    try:
        sys.getandroidapilevel()
        return "android_arm_v8a", "so"
    except AttributeError:
        pass

    # ARM64 Linux?
    if platform.machine() == "aarch64":
        return "linux_aarch64", "so"

    # Regular Linux?
    if platform.machine() == "x86_64":
        return "linux_x86_64", "so"

    print(f"platform.system() = '{platform.system()}'; platform.machine() = '{platform.machine()}'")
    raise NotImplementedError


__all__ = [
    "platform_folder",
]
