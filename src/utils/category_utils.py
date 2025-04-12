from functools import lru_cache

@lru_cache
def get_categories() -> list[str]:
    """Return the list of categories from the settings file (cached)"""
    with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("categories", [])
