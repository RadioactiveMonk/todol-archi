import json
from typing import Any

from core.default_values import CATEGORIES
from helpers.log_utils import logger
from core.path import SETTINGS_FILE
from ui.ui_constants import DEFAULT_THEME


def load_settings() -> dict[str, Any]:
    """Load settings file 'settings.json'"""
    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            logger.info(f"{SETTINGS_FILE} loaded successfully")
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Failed to load settings: {e}")
        return {}


def save_settings(data: dict[str, Any]) -> bool:
    """Write settings into 'settings.json'"""
    try:
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
            logger.info(f"{SETTINGS_FILE} saved successfully: {data}")
            return True
    except Exception as e:
        logger.error(f"Failed to save settings: {e}")
        return False


def get_setting(key: str, default: Any = None) -> Any:
    """Retrieve a settings value from 'settings.json'"""
    settings = load_settings()

    # Respecte le default fourni, sinon fallback automatique
    if default is None:
        default = DEFAULT_THEME if key == "theme" else CATEGORIES

    try:
        return settings.get(key, default)
    except Exception as e:
        logger.warning(f"Failed to get setting '{key}': {e}")
        return default


def set_setting(key: str, value: Any) -> bool:
    """Update a settings value in 'settings.json'"""
    settings = load_settings()

    try:
        settings[key] = value
        success = save_settings(settings)

        if success:
            logger.info(f"Setting updated successfully: {key} = {value}")
        return success
    except Exception as e:
        logger.error(f"Failed to update setting '{key}': {e}")
        return False
