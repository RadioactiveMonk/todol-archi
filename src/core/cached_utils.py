import json
from functools import lru_cache

from core.app_constants import DEFAULT_THEME, SETTINGS_FILE, STYLESHEET_PATH


@lru_cache
def get_categories() -> list[str]:
    """Return the list of categories from the settings file (cached)"""
    with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("categories", [])


@lru_cache
def get_stylesheet(theme: str = DEFAULT_THEME) -> str:
    """Return the content of the .qss file corresponding to the theme"""
    qss_path = STYLESHEET_PATH / f"{theme}.qss"
    return qss_path.read_text(encoding="utf-8")


@lru_cache
def get_available_themes() -> list[str]:
    """Return the list of available themes"""
    return [
        file.stem for file in STYLESHEET_PATH.glob("*.qss") if file.is_file()
    ]  # .stem = supprime l'extension | .glob: parcours le dossier | .is_file: si c'est un fichier
