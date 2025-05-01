# src/utils/path_utils.py

from pathlib import Path

from core.log_manager import logger

# =====================================
# PATH CONSTANTS
# =====================================

BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
SRC_DIR: Path = BASE_DIR / "src"
DATA_DIR: Path = BASE_DIR / "data"
LOG_DIR: Path = BASE_DIR / "logs"
RESOURCES_DIR: Path = SRC_DIR / "ui" / "resources"
ICONS_DIR: Path = RESOURCES_DIR / "icons"
STYLESHEETS_DIR: Path = RESOURCES_DIR / "stylesheets"

# =====================================
# FILES CONSTANTS
# =====================================

SETTINGS_FILE: Path = DATA_DIR / "settings.json"
DB_FILE: Path = DATA_DIR / "tasks.db"
APP_LOG_FILE: Path = LOG_DIR / "app.log"

# =====================================
# DISPATCH TABLE
# =====================================

_PATHS: dict[str, Path] = {
    "base": BASE_DIR,
    "data": DATA_DIR,
    "log_dir": LOG_DIR,
    "log_file": APP_LOG_FILE,
    "db": DB_FILE,
    "settings": SETTINGS_FILE,
    "icons": ICONS_DIR,
    "stylesheets": STYLESHEETS_DIR,
}

# =====================================
# ACCESS FUNCTIONS
# =====================================


def get_path(key: str, default: Path | None = None) -> Path:
    """Return a Path from the dispatch table, or a default if provided."""
    if key not in _PATHS:
        if default is not None:
            logger.warning(f"Path key '{key}' not found, returning fallback.")
            return default
        logger.error(f"Invalid path key: '{key}'")
        raise

    path = _PATHS[key]
    logger.debug(f"Accessing path: {key} → {path}")
    return path


def get_all_paths() -> dict[str, Path]:
    """Return a copy of all known paths."""
    logger.debug("Getting all paths")
    return _PATHS.copy()
