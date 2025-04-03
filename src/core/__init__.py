from helpers.cached_utils import get_available_themes, get_categories
from helpers.log_utils import logger
from ui.theme.style_loader import load_stylesheet, reload_theme

from .app_constants import APP_NAME
from .config import AUTO_SAVE_INTERVAL, DEBUG
from .database_config import (
    SQL_DELETE_TASK_BY_ID,
    SQL_INSERT_TASK,
    SQL_SELECT_TASK_BY_ID,
    SQL_SELECT_TASKS,
    SQL_UPDATE_TASK_BY_ID,
)
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
from .sql_schema import SQL_CREATE_TASKS_TABLE, SQL_DROP_TASKS_TABLE

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
    "SQL_INSERT_TASK",
    "SQL_SELECT_TASKS",
    "SQL_SELECT_TASK_BY_ID",
    "SQL_UPDATE_TASK_BY_ID",
    "SQL_DELETE_TASK_BY_ID",
    # DB schema
    "SQL_CREATE_TASKS_TABLE",
    "SQL_DROP_TASKS_TABLE",
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
