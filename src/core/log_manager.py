import sys

from loguru import logger

from models.task_core import TaskCore
from utils.path_utils import APP_LOG_FILE

# Format
LOG_FORMAT = (
    "<white>{time:YYYY-MM-DD HH:mm:ss.SSS}</white> | "
    "<level>{level: <8}</level> | "
    "<cyan>{module}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
    "<magenta>{process.id}</magenta> - "
    "<level>{message}</level>"
)

# Suppression du logger d'origine
logger.remove()

# Console
logger.add(
    sys.stderr,
    level="DEBUG",
    format=LOG_FORMAT,
)

# Fichier (rotation 500 KB, rétention 10 jours)
logger.add(
    APP_LOG_FILE,
    rotation="500 KB",
    retention="10 days",
    level="DEBUG",
    format=LOG_FORMAT,
)


def log_task(task: TaskCore, action: str = "saved") -> None:
    """Log special actions for in app tasks manipulation"""
    logger.info(f"[TASK] {action.upper()} – {task}")


__all__ = ["logger"]
