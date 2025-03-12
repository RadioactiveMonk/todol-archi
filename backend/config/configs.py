import os

# =====================================
# CONFIGURATION DE L'APPLICATION
# =====================================


# Mode débug
# =====================================
DEBUG = False

# Fichiers et stockage
# =====================================
BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../")
)  # Dossier Todol-pro
CONFIG_DIR = os.path.join(BASE_DIR, "backend", "config")
SETTINGS_PATH = os.path.join(CONFIG_DIR, "settings.json")  # ✅ Fichier complet
DB_PATH = os.path.join(BASE_DIR, "data", "tasks.db")
LOG_PATH = os.path.join(BASE_DIR, "logs")
STYLESHEET_PATH = os.path.join(BASE_DIR, "resources", "stylesheets")

for path in [os.path.dirname(DB_PATH), LOG_PATH, STYLESHEET_PATH]:
    os.makedirs(path, exist_ok=True)


# Thèmes
# =====================================
APP_THEMES = ["Default", "Dark"]
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
