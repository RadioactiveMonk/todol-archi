import os
import json
from PyQt6.QtWidgets import QApplication
from backend.config.configs import CONFIG_DIR, SETTINGS_PATH, STYLESHEET_PATH
from backend.logger import logger


def load_stylesheet(app: QApplication, theme: str):
    """Charge et applique un fichier de style .QSS"""

    theme = "default"

    if os.path.exists(SETTINGS_PATH):
        try:
            with open(SETTINGS_PATH, "r") as file:
                settings = json.load(file)
                theme = settings.get("theme", "default")
        except json.JSONDecodeError as e:
            logger.error(f"JSON ERROR (settings.json): {e}")

    qss_file = os.path.join(STYLESHEET_PATH, f"{theme}.qss")

