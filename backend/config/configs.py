# =====================================
# CONFIGURATION DE L'APPLICATION
# =====================================


# Mode débug
# =====================================
DEBUG = True

# Fenêtre principale
# =====================================
MAIN_WINDOW_TITLE = "Todol Pro"
MAIN_WINDOW_GEOMETRY = (100, 100, 640, 480)

# Boite d'ajout de tâche
# =====================================
TASK_DIALOG_TITLE = "New task"
TASK_DIALOG_GEOMETRY = (130, 130, 400, 350)

# Boite de paramètres
# =====================================
EDIT_PARAMETERS_DIALOG_TITLE = "Parameters"
EDIT_PARAMETERS_DIALOG_GEOMETRY = (200, 200, 400, 250)

# Fichiers et stockage
# =====================================
CFG_PATH = "data/config.json"
DB_PATH = "data/tasks.db"
LOG_PATH = "logs/app.log"

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
    "Pets"
]
DEFAULT_CATEGORY = CATEGORIES[0]

# Autres paramètres
# =====================================
AUTO_SAVE_INTERVAL = 5
