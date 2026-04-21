import runpy

from utils.paths import root_path, set_working_directory


def main() -> None:
    set_working_directory()
    runpy.run_path(root_path("main.py"), run_name="__main__")
