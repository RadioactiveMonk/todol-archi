from functools import lru_cache

from utils.log_utils import logger
from utils.path_utils import STYLESHEETS_DIR


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
