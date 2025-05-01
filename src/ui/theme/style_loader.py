# src/ui/theme/style_loader.py


from functools import lru_cache
from pathlib import Path

from PySide6.QtWidgets import QApplication

from core.settings_manager import get_setting
from utils.path_utils import STYLESHEETS_DIR
from utils.ui_geometry_utils import DEFAULT_THEME


def apply_stylesheet(app: QApplication, qss: str) -> None:
    """
    Apply the .qss file to the app
    """
    app.setStyleSheet(qss)


@lru_cache
def get_stylesheet(theme: str) -> str:
    """
    Get the stylesheet path

    Parameters
    ----------
    theme : str
        the name of the theme without extension

    Returns
    -------
    str: the path to the .qss stylesheet

    """

    from core.log_manager import logger

    qss_file = Path(STYLESHEETS_DIR) / f"{theme}.qss"
    try:
        qss = qss_file.read_text()
        logger.info(f"Stylesheet retrieved: {qss_file}")
        return qss
    except FileNotFoundError:
        logger.error(f"Stylesheet file not found: {qss_file}")
        return ""


def load_stylesheet(app: QApplication, theme: str = DEFAULT_THEME) -> None:
    """Apply a theme to the application

    Parameters
    ----------
    app : QApplication
        The application to apply the theme to
    theme : str, optional
        by default DEFAULT_THEME
    """

    from core.log_manager import logger

    try:
        qss = get_stylesheet(theme)
        apply_stylesheet(app, qss)
        logger.info(f"🎨 Theme '{theme}' appliqué avec succès !")
    except Exception as e:
        logger.warning(f"⚠️ Impossible de charger le thème '{theme}' : {e}")


def reload_theme(app: QApplication) -> None:
    """
    Reload the current theme
    """

    get_stylesheet.cache_clear()
    theme = get_setting("theme")
    app.setStyleSheet(get_stylesheet(theme))
