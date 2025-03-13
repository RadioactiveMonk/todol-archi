import os
from pathlib import Path
import json
from PyQt6.QtWidgets import QApplication
from backend.config.configs import STYLESHEET_PATH
from backend.settings_manager import SettingsManager
from backend.logger import logger


def load_stylesheet(app: QApplication):
    """Charge et applique un fichier de style .QSS"""

    try:
        settings = SettingsManager.load_settings()
        theme = settings.get("theme", "default")
    except Exception as e:
        logger.error(f"THEME ERROR: {e}")
        theme = "default"

    stylesheet_file = Path(STYLESHEET_PATH) / f"{theme}.qss"
    if not stylesheet_file.exists():
        logger.warning(f"{theme}.qss introuvable. Fallback sur default.qss")
        stylesheet_file = Path(STYLESHEET_PATH) / "default.qss"
