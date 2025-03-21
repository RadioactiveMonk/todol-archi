import json
from typing import Dict, Any
from dataclasses import dataclass, field
from backend.config.constants import DEFAULT_THEME, CATEGORIES, SETTINGS_FILE
from backend.logger import logger


@dataclass
class Settings:
    """Represent the configuration loaded in memory (.json)"""

    theme: str = DEFAULT_THEME
    categories: list[str] = field(default_factory=lambda: CATEGORIES)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Settings":
        """Create an instance of settings from the json.

        Parameters
        ----------
        data : Dict[str, Any]


        Returns
        -------
        Settings
            instance of class 'Settings'
        """
        return cls(
            theme=data.get("theme", DEFAULT_THEME),
            categories=data.get("categories", CATEGORIES),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert an instance of 'Settings' to a dictionnary for the .json"""
        return {"theme": self.theme, "categories": self.categories}


class SettingsManager:
    """Manages the global settings"""

    _instance = None
    _settings: Settings = Settings()

    def __new__(cls):
        """Creates a singleton

        Returns
        -------
        SettingsManager
            a unique instance of 'SettingsManager'
        """
        if cls._instance is None:
            cls._instance = super(SettingsManager, cls).__new__(cls)
            cls._settings = cls._load()
        return cls._instance

    @classmethod
    def _load(cls) -> Settings:
        """Load global settings (once)

        Returns
        -------
        Settings
            instance of 'Settings'
        """

        if SETTINGS_FILE.exists():
            try:
                with SETTINGS_FILE.open("r", encoding="utf-8") as fhand:
                    data = json.load(fhand)
                return Settings.from_dict(data)

            except (json.JSONDecodeError, IOError) as e:
                logger.error(f"ERROR: couldn't load 'settings.json: {e}")
                return Settings()  # 👁️‍🗨️ retourne la dataclass de base si erreur
        return Settings()

    def save(self) -> None:
        """Saves to .json"""
        try:
            with SETTINGS_FILE.open("w", encoding="utf-8") as fhand:
                json.dump(self._settings.to_dict(), fhand, indent=4, ensure_ascii=False)
        except IOError as e:
            logger.error(f"ERROR: couldn't save settings.json: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        """Get settings from the .json"""
        return getattr(self._settings, key, default)

    def update(self, key: str, value: Any) -> None:
        if hasattr(self._settings, key):
            setattr(self._settings, key, value)
            self.save()  # 👁️‍🗨️ Une seule sauvegarde
        else:
            logger.warning(f"WARNING: couldn't load parameter -- {key}")

    def get_all(self) -> Dict[str, Any]:
        """Return settings as a dictionnary"""
        return self._settings.to_dict()
