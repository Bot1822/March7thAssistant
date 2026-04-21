import os
import sys
from pathlib import Path


def runtime_root() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent.parent


ROOT_DIR = runtime_root()
ASSETS_DIR = ROOT_DIR / "assets"


def root_path(*parts: str) -> str:
    return str(ROOT_DIR.joinpath(*parts))


def asset_path(*parts: str) -> str:
    return str(ASSETS_DIR.joinpath(*parts))


def config_path(filename: str = "config.yaml") -> str:
    return root_path(filename)


def from_root(path: str) -> str:
    candidate = Path(path)
    if candidate.is_absolute():
        return str(candidate)

    normalized = path.replace("\\", "/")
    while normalized.startswith("./"):
        normalized = normalized[2:]

    return str(ROOT_DIR / Path(normalized))


def set_working_directory() -> None:
    os.chdir(ROOT_DIR)
