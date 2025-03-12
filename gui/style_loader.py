import os
import json
from PyQt6.QtWidgets import QApplication
from backend.config.configs import SETTINGS_PATH, STYLESHEET_PATH, DEFAULT_THEME
from backend.logger import logger


def load_stylesheet(app: QApplication):
    """Charge et applique un fichier de style .QSS"""

    theme = DEFAULT_THEME

    if os.path.exists(SETTINGS_PATH):
        try:
            with open(SETTINGS_PATH, "r") as file:
                settings = json.load(file)
                theme = settings.get("theme", DEFAULT_THEME)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            logger.error(f"JSON ERROR (settings.json): {e}")

    qss_file = os.path.join(STYLESHEET_PATH, f"{theme}.qss")

    if os.path.exists(qss_file):
        with open(qss_file, "r") as f:
            app.setStyleSheet(f.read())
            logger.info(f"THEME UPDATE: {qss_file}")
    else:
        logger.error(f"FILENOTFOUND: {qss_file}")
