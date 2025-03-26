from pathlib import Path

# =====================================
# PATHS CENTRALISED FOR THE PROJECT
# =====================================

# Absolute path to the current file (core/path.py)
CURRENT_FILE = Path(__file__).resolve()

# src/ directory
SRC_DIR = CURRENT_FILE.parent.parent  # = src/core/..

# Project root (one level above src/)
BASE_DIR = SRC_DIR.parent

# Core directories
CONFIG_DIR = SRC_DIR / "core"
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"
RESOURCES_DIR = SRC_DIR / "ui" / "resources"
ICONS_DIR = RESOURCES_DIR / "icons"
STYLESHEETS_DIR = RESOURCES_DIR / "stylesheets"

# Files
SETTINGS_FILE = DATA_DIR / "settings.json"
DB_FILE = DATA_DIR / "tasks.db"

# Ensure needed directories exist
for directory in [DATA_DIR, LOG_DIR, STYLESHEETS_DIR, ICONS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)
