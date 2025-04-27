# src/helpers/log_utils.py
import sys

from loguru import logger

from utils.path_utils import APP_LOG_FILE


# Improved log format
log_format = (
    "<white>{time:YYYY-MM-DD HH:mm:ss.SSS}</white> | "
    "<level>{level: <8}</level> | "
    "<cyan>{module}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
    "<magenta>{process.id}</magenta> - "
    "<level>{message}</level>"
)

# Remove the default logger
logger.remove()

# Console (terminal) logger
logger.add(
    sys.stderr,
    level="DEBUG",
    format=log_format,
)

# File logger with rotation and retention
logger.add(
    APP_LOG_FILE,
    rotation="500 KB",
    retention="10 days",
    level="DEBUG",
    format=log_format,
)

__all__ = ["logger"]
