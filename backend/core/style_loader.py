from PyQt6.QtWidgets import QApplication
from configuration.constants import DEFAULT_THEME
from backend.core.cached_utils import get_stylesheet
from backend.core.logger import logger


def load_stylesheet(app: QApplication, theme: str = DEFAULT_THEME) -> None:
    """Applique le thème QSS à l'application (cache activé)."""
    try:
        qss = get_stylesheet(theme)
        app.setStyleSheet(qss)
        logger.info(f"🎨 Theme '{theme}' appliqué avec succès !")
    except Exception as e:
        logger.warning(f"⚠️ Impossible de charger le thème '{theme}' : {e}")
