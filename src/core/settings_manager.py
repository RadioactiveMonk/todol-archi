from typing import Optional
from pydantic import BaseModel
import json
from pathlib import Path

from core.log_manager import logger
from utils.path_utils import SETTINGS_FILE


class SettingsModel(BaseModel):
    theme: str = "default"
    categories: list = DEFAULT_CATEGORIES
    autosave: bool = True
    


class SettingsManager:
    """Manage settings using a Pydantic model and JSON file."""

    def __init__(self, path: Optional[Path] = None):
        self._path = Path(path) if path else SETTINGS_FILE
        self._settings = self._load()

    def _load(self) -> SettingsModel:
        try:
            with self._path.open("r", encoding="utf-8") as f:
                data = json.load(f)
            settings = SettingsModel(**data)
            logger.info(f"{self._path} loaded successfully")
            return settings
        except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
            logger.error(f"Failed to load settings, falling back to defaults: {e}")
            return SettingsModel()

    def _save(self) -> bool:
        try:
            with self._path.open("w", encoding="utf-8") as f:
                json.dump(self._settings.dict(), f, indent=4)
            logger.info(f"{self._path} saved successfully: {self._settings.dict()}")
            return True
        except Exception as e:
            logger.error(f"Failed to save settings: {e}")
            return False

    def get(self, key: str):
        return getattr(self._settings, key, None)

    def set(self, key: str, value) -> bool:
        if not hasattr(self._settings, key):
            logger.warning(f"Attempted to set unknown key: {key}")
            return False
        setattr(self._settings, key, value)
        return self._save()

    def all(self) -> dict:
        return self._settings.dict()

    def reset(self) -> None:
        self._settings = SettingsModel()
        self._save()