from pathlib import Path
from PyQt6.QtWidgets import QApplication
from backend import settings_manager
from backend.config.configs import STYLESHEET_PATH
from backend.settings_manager import SettingsManager
from backend.logger import logger


def load_stylesheet(app: QApplication):
    """Charge et applique un fichier de style .QSS"""
    settings_manager = SettingsManager()

    try:
        settings = settings_manager.get_all()
        theme = settings.get("theme", "default")
    except Exception as e:
        logger.error(f"THEME ERROR (load_settings()): {e}")
        theme = "default"

    stylesheet_file = Path(STYLESHEET_PATH) / f"{theme}.qss"
    if not stylesheet_file.exists():
        logger.warning(f"{theme}.qss introuvable. Fallback sur default.qss")
        stylesheet_file = Path(STYLESHEET_PATH) / "default.qss"

    try:
        with stylesheet_file.open("r", encoding="utf-8") as f:
            stylesheet = f.read()
            app.setStyleSheet(stylesheet)  # Applique le style
            logger.info(f"Theme {theme} appliqué avec succès !")
    except Exception as e:
        logger.error(f"Erreur lors de l'application du thème {theme}: {e}")

    return stylesheet_file  # Utile si on veut vérifier ailleurs
