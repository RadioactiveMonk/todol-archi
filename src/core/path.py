from pathlib import Path

# =====================================
# CENTRALIZED PATHS FOR THE PROJECT
# =====================================

# Absolute path to the current file (core/path.py)
CURRENT_FILE = Path(__file__).resolve()

# src/ directory (parent of the current file's directory)
SRC_DIR = CURRENT_FILE.parent.parent

# Project root (one level above src/)
BASE_DIR = SRC_DIR.parent

# Core directories
CONFIG_DIR = SRC_DIR / "core"  # Directory for core configuration files
DATA_DIR = BASE_DIR / "data"   # Directory for data storage
LOG_DIR = BASE_DIR / "logs"    # Directory for log files
RESOURCES_DIR = SRC_DIR / "ui" / "resources"  # Directory for UI resources
ICONS_DIR = RESOURCES_DIR / "icons"  # Directory for icon files
STYLESHEETS_DIR = RESOURCES_DIR / "stylesheets"  # Directory for stylesheet files

# Specific files
SETTINGS_FILE = DATA_DIR / "settings.json"  # Settings file path
DB_FILE = DATA_DIR / "tasks.db"  # Database file path

# Ensure needed directories exist
for directory in [DATA_DIR, LOG_DIR, STYLESHEETS_DIR, ICONS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)