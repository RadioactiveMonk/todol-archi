# src/helpers/log_utils.py
import sys

from loguru import logger

from core.path import LOG_DIR

LOG_FILE = LOG_DIR / "app.log"

logger.remove()  # Supprime le logger par défaut
logger.add(
    sys.stderr,
    level="DEBUG",
    format="<green>{time:HH:mm:ss}</green> | <level>{level}</level> | <cyan>{message}</cyan>",
)
logger.add(LOG_FILE, rotation="500 KB", retention="10 days", level="DEBUG")

__all__ = ["logger"]
