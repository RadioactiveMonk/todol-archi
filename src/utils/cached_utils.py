import json
from functools import lru_cache

from core.path import SETTINGS_FILE, STYLESHEETS_DIR


@lru_cache
def get_categories() -> list[str]:
    """Return the list of categories from the settings file (cached)"""
    with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("categories", [])


@lru_cache
def get_available_themes() -> list[str]:
    """Return the list of available themes"""
    return [
        file.stem for file in STYLESHEETS_DIR.glob("*.qss") if file.is_file()
    ]  # .stem = supprime l'extension | .glob: parcours le dossier | .is_file: si c'est un fichier
