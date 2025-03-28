from .app_constants import APP_NAME
from .cached_utils import get_available_themes, get_categories, get_stylesheet
from .config import AUTO_SAVE_INTERVAL, DEBUG
from .database_config import (
    SQL_CREATE_TABLE,
    SQL_DELETE_TASK,
    SQL_DROP_TABLE,
    SQL_INSERT_TASK,
    SQL_SELECT_TASKS,
)
from .logger import logger
from .path import (
    BASE_DIR,
    DATA_DIR,
    DB_FILE,
    ICONS_DIR,
    LOG_DIR,
    SETTINGS_FILE,
    SRC_DIR,
    STYLESHEETS_DIR,
)
from .settings_manager import get_setting, load_settings, save_settings, set_setting
from .style_loader import load_stylesheet, reload_theme

__all__ = [
    # App constants
    "APP_NAME",
    # Settings access
    "get_setting",
    "set_setting",
    "load_settings",
    "save_settings",
    # Cache utils
    "get_categories",
    "get_stylesheet",
    "get_available_themes",
    # Style
    "load_stylesheet",
    "reload_theme",
    # Paths
    "BASE_DIR",
    "SRC_DIR",
    "DATA_DIR",
    "LOG_DIR",
    "ICONS_DIR",
    "STYLESHEETS_DIR",
    "DB_FILE",
    "SETTINGS_FILE",
    # DB config
    "SQL_CREATE_TABLE",
    "SQL_DELETE_TASK",
    "SQL_DROP_TABLE",
    "SQL_INSERT_TASK",
    "SQL_SELECT_TASKS",
    # Dev tools
    "logger",
    # Misc
    "AUTO_SAVE_INTERVAL",
    "DEBUG",
]

# This module imports and re-exports various constants, utility functions, and
# configuration settings related to the application. It serves as a centralized
# location for accessing important paths, database configurations, settings
# management, and other application-wide constants.
