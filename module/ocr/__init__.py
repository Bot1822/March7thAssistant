from module.logger import log
from module.ocr.ocr import OCR
import json
from utils.paths import asset_path

# 读取 OCR 替换配置
with open(asset_path("config", "ocr_replacements.json"), 'r', encoding='utf-8') as file:
    replacements = json.load(file)
# 初始化 OCR 对象
ocr = OCR(log, replacements)
