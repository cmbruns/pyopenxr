import platform
import sys
import os
import struct

# Basic platform info
print(f"platform.system(): {platform.system()}")
print(f"platform.machine(): {platform.machine()}")
print(f"platform.architecture(): {platform.architecture()}")
# print(f"platform.platform(): {platform.platform()}")
print(f"platform.version(): {platform.version()}")
print(f"platform.release(): {platform.release()}")

# Detailed uname
uname = platform.uname()
for field in uname._fields:
    print(f"platform.uname['{field}']: {getattr(uname, field)}")

# sys module info
print(f"sys.platform: {sys.platform}")
print(f"sys.byteorder: {sys.byteorder}")
print(f"sys.maxsize: 0x{sys.maxsize:0X}")
print(f"sys.executable: {sys.executable}")
try:
    print(f"sys.get_androidapilevel(): {sys.getandroidapilevel()}")
except AttributeError:
    print(f"sys.get_androidapilevel(): <unknown attribute>")


# OS environment
for key in sorted(os.environ.keys()):
    if False and key not in [
        "ANDROID_ROOT",  # Android
        "ANDROID_DATA",  # Android
        "BOOTCLASSPATH",  # Android
        "OS",  # Windows
        "PROCESSOR_ARCHITECTURE",
        "SNAP_ARCH",  # Ubuntu
        "STEAMOS_VERSION",  # Steam Frame?
        "STEAM_RUNTIME",  # Steam Frame?
    ]:
        continue
    print(f"os.environ['{key}']={os.environ[key]}")

# Check ELF vs non‑ELF (Android uses Bionic libc)
try:
    with open("/lib/libc.so", "rb") as f:
        magic = f.read(4)
        print("/lib/libc.so magic:", magic)
except Exception as e:
    print("Could not read /lib/libc.so:", e)

try:
    with open("/system/lib64/libc.so", "rb") as f:
        magic = f.read(4)
        print("/system/lib64/libc.so magic:", magic)
except Exception as e:
    print("Could not read Android libc:", e)

# Pointer size (32 vs 64 bit)
print("struct.calcsize('P'):", struct.calcsize("P"))
