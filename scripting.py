from pathlib import Path
from PyQt6.QtWidgets import QApplication
from backend.config.configs import STYLESHEET_PATH
from backend.settings_manager import SettingsManager
from backend.logger import logger


def load_stylesheet(app: QApplication):
    """Charge et applique un fichier de style .QSS"""
    try:
        settings = SettingsManager.load_settings()
        theme = settings.get("theme", "default")  # Lecture propre
    except Exception as e:
        logger.error(f"Erreur lors du chargement du thème: {e}")
        theme = "default"

    stylesheet_file = Path(STYLESHEET_PATH) / f"{theme}.qss"
    if not stylesheet_file.exists():
        logger.warning(f"Stylesheet {theme}.qss introuvable, fallback sur default.qss")
        stylesheet_file = Path(STYLESHEET_PATH) / "default.qss"

    return stylesheet_file
