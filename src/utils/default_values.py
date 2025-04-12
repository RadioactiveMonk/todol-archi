from typing import Any

from utils.log_utils import logger

# =====================================
# DOMAIN DEFAULTS
# =====================================
NO_ID: int = -1

# Category
CATEGORIES: list[str] = ["General", "Work", "Hobbies"]

# Task values
DEFAULT_TITLE: str = "New task"
DEFAULT_CATEGORY: str = CATEGORIES[0]
DEFAULT_STATUS: bool = False
DEFAULT_EXPIRATION: str = "2023-10-31 08:30"
DEFAULT_NOTES: str = ""

_DEFAULTS: dict = {
    "title": DEFAULT_TITLE,
    "category": DEFAULT_CATEGORY,
    "completed": DEFAULT_STATUS,
    "expiration": DEFAULT_EXPIRATION,
    "notes": DEFAULT_NOTES,
}


def get_default(key: str) -> Any:
    """Retourne une valeur par défaut via une clé dict"""
    try:
        logger.debug(f"Accessing default values: {key}")
        return _DEFAULTS[key]
    except KeyError:
        logger.error(f"Couldn't access {key} in _DEFAULTS")
        raise


def get_all_defaults() -> dict:
    """Retourne une copie du dictionnaire de toutes les valeurs par défaut."""
    logger.debug("Accessing all default values.")
    return _DEFAULTS.copy()
