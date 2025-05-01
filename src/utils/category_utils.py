from functools import lru_cache
from typing import List

from helpers.contextmanagers import open_settings
from core.log_manager import logger


@lru_cache
def get_categories() -> List[str]:
    """Return the list of categories from the settings file (cached)"""

    logger.debug("Accessing task categories")
    with open_settings() as settings:
        categories = settings.get("categories", [])
        return categories if isinstance(categories, list) else []
