import json
from pathlib import Path
from typing import Dict, List, Any
from backend.config.configs import SETTINGS_FILE, DEFAULT_THEME, CATEGORIES
from backend.logger import logger


class SettingsManager:
    """Gestionnaire de paramètres"""

    SETTINGS = SETTINGS_FILE

    @classmethod
    def load_settings(cls) -> Dict:
        if cls.SETTINGS.exists():
            try:
                with cls.SETTINGS.open("r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                logger.error(f"JSON ERROR: {e}")
                return cls.reset()
        return cls.default_settings()

    @classmethod
    def save_settings(cls, settings: dict) -> None:
        pass

    @classmethod
    def update_settings(cls, key: str, value: Any) -> None:
        pass

    @classmethod
    def reset(cls) -> dict:
        default = cls.default_settings()
        cls.save_settings(default)
        return default

    @staticmethod
    def default_settings() -> dict:
        DEFAULT_CATEGORIES = ["General", "Work", "Hobbies"]
        return {"theme": DEFAULT_THEME, "categories": DEFAULT_CATEGORIES}
