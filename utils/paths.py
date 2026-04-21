import os
import sys
from pathlib import Path

APP_NAME = "March7thAssistant"


def runtime_root() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent.parent


ROOT_DIR = runtime_root()
ASSETS_DIR = ROOT_DIR / "assets"
IS_SOURCE_CHECKOUT = (ROOT_DIR / ".git").exists()


def _user_base_dir(env_var: str, fallback: Path) -> Path:
    return Path(os.environ.get(env_var) or fallback).expanduser()


def user_config_dir() -> Path:
    if sys.platform == "win32":
        base = _user_base_dir("APPDATA", Path.home() / "AppData" / "Roaming")
    elif sys.platform == "darwin":
        base = Path.home() / "Library" / "Application Support"
    else:
        base = _user_base_dir("XDG_CONFIG_HOME", Path.home() / ".config")

    path = base / APP_NAME
    path.mkdir(parents=True, exist_ok=True)
    return path


def user_data_dir() -> Path:
    if sys.platform == "win32":
        base = _user_base_dir("LOCALAPPDATA", Path.home() / "AppData" / "Local")
    elif sys.platform == "darwin":
        base = Path.home() / "Library" / "Application Support"
    else:
        base = _user_base_dir("XDG_DATA_HOME", Path.home() / ".local" / "share")

    path = base / APP_NAME
    path.mkdir(parents=True, exist_ok=True)
    return path


CONFIG_DIR = ROOT_DIR if IS_SOURCE_CHECKOUT else user_config_dir()
DATA_DIR = ROOT_DIR if IS_SOURCE_CHECKOUT else user_data_dir()


def root_path(*parts: str) -> str:
    return str(ROOT_DIR.joinpath(*parts))


def asset_path(*parts: str) -> str:
    return str(ASSETS_DIR.joinpath(*parts))


def config_path(filename: str = "config.yaml") -> str:
    path = CONFIG_DIR.joinpath(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    return str(path)


def data_path(*parts: str) -> str:
    path = DATA_DIR.joinpath(*parts)
    path.parent.mkdir(parents=True, exist_ok=True)
    return str(path)


def settings_path(*parts: str) -> str:
    return data_path("settings", *parts)


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
