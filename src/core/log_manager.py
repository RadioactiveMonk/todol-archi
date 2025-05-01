# src/utils/log_utils.py

import sys

from loguru import logger

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

# Defer the APP_LOG_FILE import here to avoid circular import
try:
    from utils.path_utils import APP_LOG_FILE

    logger.add(
        APP_LOG_FILE,
        rotation="500 KB",
        retention="10 days",
        level="DEBUG",
        format=log_format,
    )
except ImportError:
    # Optional: you can log a warning or ignore silently during certain startup phases
    logger.warning("APP_LOG_FILE could not be imported at log setup time.")

__all__ = ["logger"]
