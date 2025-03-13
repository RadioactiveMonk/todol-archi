from pathlib import Path

# =====================================
# CONFIGURATION DE L'APPLICATION
# =====================================


# Mode débug
# =====================================
DEBUG = True

# Fichiers et stockage
# =====================================
BASE_DIR = Path(__file__).resolve().parent.parent.parent
CONFIG_DIR = BASE_DIR / "backend" / "config"
SETTINGS_FILE = CONFIG_DIR / "settings.json"
DB_PATH = BASE_DIR / "data" / "tasks.db"
LOG_PATH = BASE_DIR / "logs"
STYLESHEET_PATH = BASE_DIR / "resources" / "stylesheets"

for p in [DB_PATH.parent, LOG_PATH, STYLESHEET_PATH]:
    p.mkdir(parents=True, exist_ok=True)


# Thèmes
# =====================================
APP_THEMES = ["default", "dark", "system"]
DEFAULT_THEME = APP_THEMES[0]

# Catégories des tâches
# =====================================
CATEGORIES = [
    "General",
    "Work",
    "Hobbies",
]

# Autres paramètres
# =====================================
AUTO_SAVE_INTERVAL = 5
