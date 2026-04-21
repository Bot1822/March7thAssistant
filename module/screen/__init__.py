from module.logger import log
from module.screen.screen import Screen
from utils.paths import asset_path

SCREENS_PATH = asset_path("config", "screens.json")

screen = Screen(SCREENS_PATH, log)
