import runpy

from utils.paths import set_working_directory


def main() -> None:
    set_working_directory()
    runpy.run_module("app", run_name="__main__")
