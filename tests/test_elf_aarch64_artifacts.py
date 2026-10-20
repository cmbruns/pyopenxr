"""
test_elf_page_alignment.py -- unit tests for the aarch64 artifacts (issue #147).

On 16KB-page kernels (e.g. the stock 64-bit Raspberry Pi 5 OS, and Android
15+ devices), the dynamic loader cannot map a shared library whose PT_LOAD
segments are aligned to less than 16KB. Every native artifact pyopenxr ships
or loads for aarch64 must therefore be linked with
-Wl,-z,max-page-size=16384 (-Wl,-z,common-page-size=16384 is the usual
companion).

These tests enforce the aarch64 build principles directly on the bundled
artifacts. They run on ANY host -- the host platform is irrelevant, because
ELF files are just bytes to parse -- and check every .so bundled in the
installed xr package under xr/library/<aarch64>/ and xr/api_layer/<aarch64>/,
for both the Linux and Android targets:

1. Bitness/architecture: every file is a 64-bit (ELFCLASS64) little-endian
   ELF with e_machine == EM_AARCH64. Guards against accidentally packaging
   32-bit (or wrong-architecture) libraries in the aarch64 folders.
2. Page alignment: every PT_LOAD segment has p_align >= 16384.

ELF parsing uses only the stdlib (struct): no new dependencies, and no
assumption that binutils/readelf exists on the test machine.

If no aarch64 .so files are bundled in this installation (e.g. a source
checkout where the native binaries were never built), the tests skip with
a visible message rather than passing vacuously.
"""
import os
import struct
import unittest

import xr

_PAGE_SIZE_16K = 16384
_PT_LOAD = 1
_EM_AARCH64 = 183

# (subpackage, target folder) pairs whose shared libraries must be checked.
# Both aarch64 targets: Linux (Pi 5 16KB-page kernel) and Android (15+).
_AARCH64_TARGETS = (
    ("library", "linux_aarch64"),
    ("library", "android_arm_v8a"),
    ("api_layer", "linux_aarch64"),
    ("api_layer", "android_arm_v8a"),
)

# ELF64 program header, little-endian (aarch64 is always LE):
#   u32 p_type, p_flags; u64 p_offset, p_vaddr, p_paddr,
#   p_filesz, p_memsz, p_align
_PHDR64_FMT = "<IIQQQQQQ"
_PHDR64_SIZE = struct.calcsize(_PHDR64_FMT)


def _elf_header(path):
    """Return (ei_class, e_machine, phoff, phentsize, phnum) for an ELF file.

    Raises ValueError if the file is not a little-endian ELF.
    """
    with open(path, "rb") as f:
        ident = f.read(16)
        if ident[:4] != b"\x7fELF":
            raise ValueError(f"{path}: not an ELF file")
        if ident[5] != 1:  # EI_DATA: ELFDATA2LSB
            raise ValueError(f"{path}: expected little-endian ELF, EI_DATA={ident[5]}")
        f.seek(18)  # e_machine
        (e_machine,) = struct.unpack("<H", f.read(2))
        f.seek(0x20)  # e_phoff
        (phoff,) = struct.unpack("<Q", f.read(8))
        f.seek(0x36)  # e_phentsize, e_phnum
        (phentsize, phnum) = struct.unpack("<HH", f.read(4))
    return ident[4], e_machine, phoff, phentsize, phnum


def _load_segment_alignments(path):
    """Return the p_align of every PT_LOAD segment in a 64-bit LE ELF file."""
    ei_class, _, phoff, phentsize, phnum = _elf_header(path)
    if ei_class != 2:  # EI_CLASS: ELFCLASS64
        raise ValueError(f"{path}: expected 64-bit ELF, EI_CLASS={ei_class}")
    if phentsize < _PHDR64_SIZE:
        raise ValueError(f"{path}: program header size {phentsize} < {_PHDR64_SIZE}")
    aligns = []
    with open(path, "rb") as f:
        for i in range(phnum):
            f.seek(phoff + i * phentsize)
            fields = struct.unpack(_PHDR64_FMT, f.read(_PHDR64_SIZE))
            p_type, p_align = fields[0], fields[7]
            if p_type == _PT_LOAD:
                aligns.append(p_align)
    if not aligns:
        raise ValueError(f"{path}: no PT_LOAD segments found")
    return aligns


def _aarch64_shared_libraries():
    """Yield paths of every bundled aarch64 .so in the installed xr package."""
    xr_dir = os.path.dirname(xr.__file__)
    for sub, folder in _AARCH64_TARGETS:
        d = os.path.join(xr_dir, sub, folder)
        if not os.path.isdir(d):
            continue
        for name in sorted(os.listdir(d)):
            if name.endswith(".so"):
                yield os.path.join(d, name)


class TestElfPageAlignment(unittest.TestCase):
    def _libs_or_skip(self):
        libs = list(_aarch64_shared_libraries())
        if not libs:
            self.skipTest(
                "no bundled aarch64 .so files in this installation; "
                "nothing to check (issue #147)"
            )
        return libs

    def test_all_aarch64_libraries_are_64_bit_aarch64(self):
        wrong = {}
        for lib in self._libs_or_skip():
            ei_class, e_machine, *_ = _elf_header(lib)
            problems = []
            if ei_class != 2:
                problems.append(f"EI_CLASS={ei_class} (expected 2, ELFCLASS64)")
            if e_machine != _EM_AARCH64:
                problems.append(
                    f"e_machine={e_machine} (expected {_EM_AARCH64}, EM_AARCH64)"
                )
            if problems:
                wrong[lib] = problems
        self.assertFalse(
            wrong,
            "aarch64 libraries with wrong bitness or architecture:\n"
            + "\n".join(f"  {lib}: {p}" for lib, p in wrong.items()),
        )

    def test_all_aarch64_libraries_are_16k_page_clean(self):
        bad = {}
        for lib in self._libs_or_skip():
            aligns = _load_segment_alignments(lib)
            too_small = [a for a in aligns if a < _PAGE_SIZE_16K]
            if too_small:
                bad[lib] = too_small
        self.assertFalse(
            bad,
            "aarch64 shared libraries with PT_LOAD segments aligned below "
            "16KB (rebuild with -Wl,-z,max-page-size=16384):\n"
            + "\n".join(f"  {lib}: p_align={a}" for lib, a in bad.items()),
        )


if __name__ == "__main__":
    unittest.main()
