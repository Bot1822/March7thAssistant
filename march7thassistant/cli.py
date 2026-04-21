import runpy

from utils.paths import set_working_directory


def main() -> None:
    set_working_directory()
    runpy.run_module("main", run_name="__main__")
