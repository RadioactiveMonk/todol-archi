from functools import lru_cache
from typing import List

from core.log_manager import logger
from helpers.contextmanagers import open_settings
from utils.path_utils import STYLESHEETS_DIR


@lru_cache
def get_categories() -> List[str]:
    """Return the list of categories from the settings file (cached)"""

    logger.debug("Accessing task categories")
    with open_settings() as settings:
        categories = settings.get("categories", [])
        return categories if isinstance(categories, list) else []


@lru_cache
def get_available_themes() -> list[str]:
    """
    Return the list of available theme names (without extension),
    found in the stylesheets directory.
    """
    logger.debug(f"Accessing themes folder: {STYLESHEETS_DIR}")
    themes = [
        file.stem for file in STYLESHEETS_DIR.glob("*.qss") if file.is_file()
    ]  # .stem = supprime l'extension | .glob: parcours le dossier | .is_file: si c'est un fichier
    return sorted(themes)


def is_theme_available(name: str) -> bool:
    """Check if a theme is available."""
    return name in get_available_themes()
