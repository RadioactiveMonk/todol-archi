from functools import lru_cache
from configuration.constants import SETTINGS_FILE, STYLESHEET_PATH, DEFAULT_THEME
import json


@lru_cache
def get_categories() -> list[str]:
    """Retourne les catégories stockées dans le fichier settings.json (cache activé)"""
    with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("categories", [])


@lru_cache
def get_stylesheet(theme: str = DEFAULT_THEME) -> str:
    """Retourne le contenu QSS du thème donné (cache activé)"""
    qss_path = STYLESHEET_PATH / f"{theme}.qss"
    return qss_path.read_text(encoding="utf-8")


@lru_cache
def get_available_themes() -> list[str]:
    """Retourne la liste des thèmes disponibles (.qss sans extension)"""
    return [
        file.stem for file in STYLESHEET_PATH.glob("*.qss") if file.is_file()
    ]  # .stem = supprime l'extension | .glob: parcours le dossier | .is_file: si c'est un fichier
