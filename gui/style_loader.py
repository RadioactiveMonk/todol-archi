import os
from PyQt6.QtWidgets import QApplication
from backend.config.configs import STYLESHEET_PATH
from backend.logger import logger


def load_stylesheet(app: QApplication, theme: str = "default"):
    """Charge et applique un fichier de style .QSS"""

    qss_file = os.path.join(STYLESHEET_PATH, f"{theme}.qss")

    if os.path.exists(qss_file):
        with open(qss_file, "r") as f:
            app.setStyleSheet(f.read())
            logger.info(f"THEME UPDATE: {qss_file}")
    else:
        logger.error(f"Thème introuvable: {qss_file}")
