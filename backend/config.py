# =====================================
# CONFIGURATION DE L'APPLICATION
# =====================================


# Mode débug
# =====================================
DEBUG = True

# Fenêtre principale
# =====================================
MAIN_WINDOW_TITLE = "Todol Pro"
MAIN_WINDOW_GEOMETRY = (100, 100, 800, 600)

# Boite d'ajout de tâche
# =====================================
TASK_DIALOG_TITLE = "New task"
TASK_DIALOG_GEOMETRY = (130, 130, 400, 350)



# Fichiers et stockage
# =====================================
DATA_FILE = "data/tasks.json"
DB_FILE = "data/tasks.db"
LOG_FILE = "logs/app.log"

# Thèmes
# =====================================
APP_THEMES = ["Default", "Dark", "Night blue"]
DEFAULT_THEME = APP_THEMES[0]

# Autres paramètres
# =====================================
AUTO_SAVE_INTERVAL = 5
