from pathlib import Path
from PyQt6.QtWidgets import QApplication
from configuration.constants import STYLESHEET_PATH, DEFAULT_THEME
from backend.core.settings_manager import SettingsManager
from backend.core.logger import logger


def load_stylesheet(app: QApplication):
    """Charge et applique un fichier de style .QSS"""
    settings_manager = SettingsManager()

    try:
        settings = settings_manager.get_all()
        theme = settings.get("theme", DEFAULT_THEME)
    except Exception as e:
        logger.error(f"THEME ERROR (load_settings()): {e}")
        theme = DEFAULT_THEME

    stylesheet_file = Path(STYLESHEET_PATH) / f"{theme}.qss"
    if not stylesheet_file.exists():
        logger.warning(f"{theme}.qss introuvable. Fallback sur {DEFAULT_THEME}.qss")
        stylesheet_file = Path(STYLESHEET_PATH) / f"{DEFAULT_THEME}.qss"

    try:
        with stylesheet_file.open("r", encoding="utf-8") as f:
            stylesheet = f.read()
            app.setStyleSheet(stylesheet)  # Applique le style
            logger.info(f"Theme {theme} appliqué avec succès !")
    except Exception as e:
        logger.error(f"Erreur lors de l'application du thème {theme}: {e}")

    return stylesheet_file  # Utile si on veut vérifier ailleurs
