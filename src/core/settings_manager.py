import json
from typing import Any

from core.log_manager import logger
from utils.default_values import DEFAULT_SETTINGS
from utils.path_utils import SETTINGS_FILE


class SettingsManager:
    """Manage settings values from the settings.json file in data/"""

    def __init__(self):
        """Initializing path to settings, default settings values. Load the file when called."""
        self._path = SETTINGS_FILE
        self._defaults = DEFAULT_SETTINGS
        self._settings = self._load()

    def _load(self) -> dict:
        """Loads the json file and its values and stores it into 'settings'"""
        try:
            with open(self._path, "r", encoding="utf-8") as f:
                settings = json.load(f)
                logger.info(f"{self._path} loaded successfully")
                return settings
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logger.error(
                f"Failed to load settings with {self._path}, falling back to default: {e}"
            )
            return self._defaults

    def _save(self) -> bool:
        """Saves the json file. Return true if data are stored, otherwise returns false"""
        try:
            with open(self._path, "w", encoding="utf-8") as f:
                json.dump(
                    self._settings, f, indent=4
                )  # dumps what stored in self._settings (self._load) into the file
                logger.info(f"{self._path} saved successfully: {self._settings}")
                return True
        except Exception as e:
            logger.error(f"Failed to save settings: {e}")
            return False

    def get(self, key: str) -> Any:
        """Get the value for the given setting key"""
        return self._settings.get(key, self._defaults.get(key, None))  # Fallback

    def set(self, key: str, value: Any) -> bool:
        """Set a value for the given setting key. Returns false if key doesn't exist. Saves the file."""
        if not key:
            logger.warning("Attempted to set setting with empty key.")
            return False
        self._settings[key] = value
        return self._save()

    def all(self) -> dict:
        """Returns a copy of all settings keys and values (defaults if no changes)"""
        merged = self._defaults.copy()
        merged.update(self._settings)
        return merged

    def reset(self) -> None:
        """Reset all settings to default values and save."""
        self._settings = DEFAULT_SETTINGS
        self._save()
