# src/helpers/log_utils.py
import sys

from loguru import logger

from core.path import LOG_DIR

LOG_FILE = LOG_DIR / "app.log"

log_format = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>"
)

logger.remove()  # Supprime le logger par défaut

# Console (terminal)
logger.add(
    sys.stderr,
    level="DEBUG",
    format=log_format,
)

# Fichier avec rotation et rétention
logger.add(
    LOG_FILE,
    rotation="500 KB",
    retention="10 days",
    level="DEBUG",
    format=log_format,
)

__all__ = ["logger"]
