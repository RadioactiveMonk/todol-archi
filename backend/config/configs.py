# =====================================
# CONFIGURATION DE L'APPLICATION
# =====================================


# Mode débug
# =====================================
DEBUG = True

# Fichiers et stockage
# =====================================
CFG_PATH = "data/config.json"
DB_PATH = "data/tasks.db"
LOG_PATH = "logs"

# Thèmes
# =====================================
APP_THEMES = ["Default", "Dark", "Night blue"]
DEFAULT_THEME = APP_THEMES[0]

# Catégories des tâches
# =====================================
CATEGORIES = [
    "General",
    "Home",
    "Health",
    "Personnal",
    "Family",
    "Pets",
    "Education",
]

# Autres paramètres
# =====================================
AUTO_SAVE_INTERVAL = 5
