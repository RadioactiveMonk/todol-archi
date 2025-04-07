from typing import Any

from helpers.log_utils import logger

# =====================================
# DOMAIN DEFAULTS
# =====================================

# Category
CATEGORIES: list[str] = ["Général", "Work", "Hobbies"]

# Task values
DEFAULT_TITLE: str = "Nouvelle tâche"
DEFAULT_CATEGORY: str = CATEGORIES[0]
DEFAULT_STATUS: bool = False
DEFAULT_EXPIRATION: str = "2025-01-01 00:00"
DEFAULT_NOTES: str = ""

_DEFAULTS: dict = {
    "title": DEFAULT_TITLE,
    "category": DEFAULT_CATEGORY,
    "completed": DEFAULT_STATUS,
    "expiration": DEFAULT_EXPIRATION,
    "notes": DEFAULT_NOTES,
}


def get_default(key: str) -> Any:
    """Return default values for a task"""
    try:
        logger.debug(f"Accessing default values: {key}")
        return _DEFAULTS[key]
    except KeyError:
        logger.error(f"Couldn't access {key} in _DEFAULTS")
        raise


# Fallback
NO_ID: int = -1
