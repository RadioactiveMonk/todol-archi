import json
from typing import Any

from core.log_manager import logger
from utils.default_values import DEFAULT_SETTINGS
from utils.path_utils import SETTINGS_FILE


class SettingsManager:
    """Manage settings values from the settings.json file in data/"""

    def __init__(self):
        """Initialize path to settings and default settings values. Load the file when instantiated."""
        self._path = SETTINGS_FILE
        self._defaults = DEFAULT_SETTINGS.copy()  # Ensure immutability
        self._settings = self._load()

    def _load(self) -> dict:
        """Load the JSON file and its values and store them into '_settings'."""
        try:
            with open(self._path, "r", encoding="utf-8") as f:
                settings = json.load(f)
                logger.info(f"{self._path} loaded successfully")
                return settings
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logger.error(f"Failed to load settings from {self._path}, falling back to defaults: {e}")
            return self._defaults.copy()

    def _save(self) -> bool:
       """Save the settings to the JSON file. Returns True if successful, False otherwise."""
        try:
            with open(self._path, "w", encoding="utf-8") as f:
                json.dump(self._settings, f, indent=4)
                logger.info(f"{self._path} saved successfully: {self._settings}")
                return True
        except Exception as e:
            logger.error(f"Failed to save settings: {e}")
            return False

    def get(self, key: str) -> Any:
        """Get the value for the given setting key."""
        return self._settings.get(key, self._defaults.get(key))

    def set(self, key: str, value: Any) -> bool:
       """Set a value for the given setting key. Returns False if key is invalid. Saves the file."""
        if not key or key not in self._defaults:
            logger.warning(f"Attempted to set invalid or unknown key: '{key}'.")
            return False
        self._settings[key] = value
        return self._save()

    def all(self) -> dict:
       """Return a copy of all settings, combining defaults and overrides."""
        merged = self._defaults.copy()
        merged.update(self._settings)
        return merged

    def reset(self) -> None:
        """Reset all settings to default values and save."""
        self._settings = self._defaults.copy()
        self._save()
