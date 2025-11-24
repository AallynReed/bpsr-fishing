import subprocess
import sys
from pathlib import Path

from cx_Freeze import setup, Executable

python_path = Path(sys.executable).parent.parent

version = "1.0.0"

instructions = [
    ("--set-version-string", "CompanyName", "Aallyn"),
    ("--set-version-string", "FileDescription", "BPSR Fishing"),
    ("--set-version-string", "ProductName", "BPSR Fishing"),
    (
        "--set-version-string",
        "OriginalFilename",
        f"BPSR-Fishing-{version}.exe",
    ),
    ("--set-version-string", "LegalCopyright", "2025-present"),
    ("--set-version-string", "CompanyName", "Aallyn"),
    ("--set-version-string", "InternalName", "BPSR-Fishing"),
    ("--set-file-version", version, ""),
    ("--set-product-version", version, ""),
    ("--set-icon", "assets/x256.ico", ""),
]

build_exe_options = {
    "packages": [
        "ok",
        "src",
    ],
    "includes": [
        "uuid",
        "src",
    ],
    "excludes": [
        "wheel",
        "cx_Freeze",
    ],
    "include_files": [
        ("assets/", "assets/"),
        ("icons/", "icons/"),
        ("src/", "src/"),
    ],
    "optimize": 2,
    "include_msvcr": True,
}

bdist_msi_options = {
    "initial_target_dir": f"[AppDataFolder]BPSR-Fishing",
    "target_name": "BPSR-Fishing",
    "upgrade_code": "{680027cc-0e73-40a1-ace8-9c108fd5c850}",
    "add_to_path": True,
    "install_icon": "assets\\favicon.ico",
    "all_users": True,
}

options = {"build_exe": build_exe_options, "bdist_msi": bdist_msi_options}

setup(
    name="BPSR Fishing",
    version=version,
    author="Aallyn",
    url=f"https://github.com/AallynReed/bpsr-fishing",
    description="A Fishing assistance tool for disabled players.",
    options=options,
    license="MIT",
    license_file="LICENSE",
    keywords="blueprotocol,fishing,python,ok-script",
    executables=[
        Executable(
            "main.py",
            target_name=f"BPSR-Fishing.exe",
            icon="assets\\favicon.ico",
            base="Win32GUI",
            copyright=f"Aallyn 2025-present",
            shortcut_name="BPSR Fishing",
            shortcut_dir="DesktopFolder",
        )
    ],
)
