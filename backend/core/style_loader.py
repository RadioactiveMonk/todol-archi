from PyQt6.QtWidgets import QApplication
from configuration.constants import DEFAULT_THEME
from backend.core.cached_utils import get_stylesheet
from configuration.settings_manager import get_setting
from backend.core.logger import logger


def load_stylesheet(app, theme: str = DEFAULT_THEME) -> None:
    """Applique le thème QSS à l'application (cache activé)."""
    try:
        qss = get_stylesheet(theme)
        app.setStyleSheet(qss)
        logger.info(f"🎨 Theme '{theme}' appliqué avec succès !")
    except Exception as e:
        logger.warning(f"⚠️ Impossible de charger le thème '{theme}' : {e}")


def reload_theme(app) -> None:
    """Reload the active theme (cache)"""
    get_stylesheet.cache_clear()
    theme = get_setting("theme")
    app.setStyleSheet(get_stylesheet(theme))
