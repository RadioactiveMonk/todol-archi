import json
from typing import Any

from core.log_manager import logger
from utils.default_values import DEFAULT_SETTINGS
from utils.path_utils import SETTINGS_FILE


class SettingsManager:
    """Manage settings values from the settings.json file in data/"""

    def __init__(self):
        """Initialize SettingsManager.

        Loads the settings from a JSON file located at the given path, 
        falling back to default values if loading fails.
        """
        self._path = SETTINGS_FILE
        self._defaults = DEFAULT_SETTINGS.copy()
        self._settings = self._load()

    def _load(self) -> dict:
        """Load the settings from the JSON file.

        Returns
        -------
        dict
            Dictionary of loaded settings, or a copy of defaults if the file cannot be read.
        """
        try:
            with open(self._path, "r", encoding="utf-8") as f:
                settings = json.load(f)
                logger.info(f"{self._path} loaded successfully")
                return settings
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logger.error(f"Failed to load settings from {self._path}, falling back to defaults: {e}")
            return self._defaults.copy()

    def _save(self) -> bool:
        """Save the current settings to the JSON file.

        Returns
        -------
        bool
            True if the settings were saved successfully, False otherwise.
        """
        try:
            with open(self._path, "w", encoding="utf-8") as f:
                json.dump(self._settings, f, indent=4)
                logger.info(f"{self._path} saved successfully: {self._settings}")
                return True
        except Exception as e:
            logger.error(f"Failed to save settings: {e}")
            return False

    def get(self, key: str) -> Any:
        """Get a setting value by key.

        Parameters
        ----------
        key : str
            The setting key to retrieve.

        Returns
        -------
        Any
            The value associated with the key, or a default value if not found.
        """
        return self._settings.get(key, self._defaults.get(key))

    def set(self, key: str, value: Any) -> bool:
        """Set a value for a setting key.

        Parameters
        ----------
        key : str
            The key to update.
        value : Any
            The new value to assign.

        Returns
        -------
        bool
            True if the key is valid and the setting is saved successfully, False otherwise.
        """
        if not key or key not in self._defaults:
            logger.warning(f"Attempted to set invalid or unknown key: '{key}'.")
            return False
        self._settings[key] = value
        return self._save()

    def all(self) -> dict:
        """Get a dictionary of all settings, merged with defaults.

        Returns
        -------
        dict
            A copy of the default settings with current settings overrides.
        """
        merged = self._defaults.copy()
        merged.update(self._settings)
        return merged

    def reset(self) -> None:
        """Reset all settings to default values and save to file.

        Returns
        -------
        None
        """
        self._settings = self._defaults.copy()
        self._save()
