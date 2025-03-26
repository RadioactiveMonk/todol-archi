from PyQt6.QtWidgets import QApplication
from src.core.cached_utils import get_stylesheet
from src.core.logger import logger
from src.core.settings_manager import get_setting

from core.app_constants import DEFAULT_THEME


def load_stylesheet(app: QApplication, theme: str = DEFAULT_THEME) -> None:
    """Apply a theme to the application

    Parameters
    ----------
    app : QApplication
        The application to apply the theme to
    theme : str, optional
        by default DEFAULT_THEME
    """

    try:
        qss = get_stylesheet(theme)
        app.setStyleSheet(qss)
        logger.info(f"🎨 Theme '{theme}' appliqué avec succès !")
    except Exception as e:
        logger.warning(f"⚠️ Impossible de charger le thème '{theme}' : {e}")


def reload_theme(app: QApplication) -> None:
    """Reload the current theme"""
    get_stylesheet.cache_clear()
    theme = get_setting("theme")
    app.setStyleSheet(get_stylesheet(theme))
