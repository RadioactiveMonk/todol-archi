import json
from typing import Dict, Any
from dataclasses import dataclass, field
from configuration.constants import DEFAULT_THEME, CATEGORIES, SETTINGS_FILE
from backend.core.logger import logger
from backend.core.cached_utils import get_categories


@dataclass
class Settings:
    """Représente la configuration chargée depuis le .json"""

    theme: str = DEFAULT_THEME
    categories: list[str] = field(default_factory=lambda: CATEGORIES)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Settings":
        return cls(
            theme=data.get("theme", DEFAULT_THEME),
            categories=data.get("categories", CATEGORIES),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "theme": self.theme,
            "categories": self.categories,
        }


class SettingsManager:
    def __init__(self) -> None:
        self.settings: Settings = self._load_settings()

    def _load_settings(self) -> Settings:
        try:
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return Settings.from_dict(data)
        except (FileNotFoundError, json.JSONDecodeError):
            return Settings()  # retourne la config par défaut

    def get(self, key: str, default=None):
        return getattr(self.settings, key, default)

    def set(self, key: str, value) -> None:
        if hasattr(self.settings, key):
            setattr(self.settings, key, value)
            with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
                json.dump(self.settings.to_dict(), f, indent=4)

    def get_categories(self) -> list[str]:
        return get_categories()

    def get_all(self) -> Dict[str, Any]:
        return self.settings.to_dict()
