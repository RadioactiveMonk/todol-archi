from functools import lru_cache


@lru_cache
def get_available_themes() -> list[str]:
    """Return the list of available themes"""
    return [
        file.stem for file in STYLESHEETS_DIR.glob("*.qss") if file.is_file()
    ]  # .stem = supprime l'extension | .glob: parcours le dossier | .is_file: si c'est un fichier
