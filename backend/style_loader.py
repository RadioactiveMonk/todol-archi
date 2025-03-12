import os
from pathlib import Path
import json
from PyQt6.QtWidgets import QApplication
from backend.config.configs import STYLESHEET_PATH, DEFAULT_THEME, SETTINGS_FILE
from backend.logger import logger


def load_stylesheet(app: QApplication):
    """Charge et applique un fichier de style .QSS"""

    with SETTINGS_FILE.open("r", encoding="utf-8") as f:
        theme = f.readlines.get("theme", DEFAULT_THEME)
