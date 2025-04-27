import json
from typing import Any, Dict

from core.default_values import CATEGORIES
from utils.path_utils import SETTINGS_FILE
from utils.log_utils import logger
from utils.ui_geometry_utils import DEFAULT_THEME


def load_settings() -> Dict[str, Any]:
    """
    Load settings from the 'settings.json' file.

    Returns:
        A dictionary containing the settings.
    """
    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            settings = json.load(f)
            logger.info(f"{SETTINGS_FILE} loaded successfully")
            return settings
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Failed to load settings: {e}")
        return {}


def save_settings(data: Dict[str, Any]) -> bool:
    """
    Save settings to the 'settings.json' file.

    Args:
        data: A dictionary containing the settings to save.

    Returns:
        True if settings were saved successfully, False otherwise.
    """
    try:
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
            logger.info(f"{SETTINGS_FILE} saved successfully: {data}")
            return True
    except Exception as e:
        logger.error(f"Failed to save settings: {e}")
        return False


def get_setting(key: str, default: Any = None) -> Any:
    """
    Retrieve a setting value from 'settings.json'.

    Args:
        key: The key of the setting to retrieve.
        default: The default value to return if the setting is not found.

    Returns:
        The value of the setting, or the default value if the setting is not found.
    """
    settings = load_settings()

    if default is None:
        default = DEFAULT_THEME if key == "theme" else CATEGORIES

    return settings.get(key, default)


def set_setting(key: str, value: Any) -> bool:
    """
    Update a setting value in 'settings.json'.

    Args:
        key: The key of the setting to update.
        value: The new value of the setting.

    Returns:
        True if the setting was updated and saved successfully, False otherwise.
    """
    settings = load_settings()
    settings[key] = value

    success = save_settings(settings)
    if success:
        logger.info(f"Setting updated successfully: {key} = {value}")
    return success
