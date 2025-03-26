from PyQt6.QtCore import QDateTime

# Fenêtre principale
# =====================================
MAIN_WINDOW_TITLE = "Todol Pro"
MAIN_WINDOW_GEOMETRY = (250, 100, 1080, 600)

# Boite d'ajout de tâche
# =====================================
TASK_DIALOG_TITLE = "New task"
EDIT_TASK_DIALOG_TITLE = "Edit task"
TASK_DIALOG_GEOMETRY = (1150, 200, 400, 350)

# Boite de paramètres
# =====================================
EDIT_PARAMETERS_DIALOG_TITLE = "Parameters"
EDIT_PARAMETERS_DIALOG_GEOMETRY = (1150, 200, 400, 200)


# Status des tâches (voir task_table_utils.py)
# =====================================
STATUS_DONE = True
STATUS_PENDING = False

# Tailles et positions de boutons
# =====================================

# Icônes de tâches
EDIT_ICON_SIZE = 18
EDIT_ICON_SPACING = 4
EDIT_ICON_TOP_OFFSET = 2
EDIT_SECTION_POSITIONS = ["delete", "edit"]


# Valeurs par défaut
# =====================================
DEFAULT_DATETIME = QDateTime.currentDateTime().addDays(1)
DEFAULT_TITLE = "TASK"
DEFAULT_NOTES = ""
DEFAULT_STATUS = STATUS_PENDING
CATEGORIES = ["General", "Work", "Hobbies"]  # default categories
DEFAULT_CATEGORY = CATEGORIES[0]  # 'Général'
NO_ID = -1

# Thèmes
# =====================================
APP_THEMES = ["default", "dark", "system"]
DEFAULT_THEME = APP_THEMES[0]
