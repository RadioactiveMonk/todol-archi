from PyQt6.QtCore import QDateTime
from backend.config.configs import CATEGORIES

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

# Tableau des tâches
# =====================================
TASK_TABLE_HEADERS = ["Status", "Category", "Expiration", "Title", "Notes"]
COLUMN_MAPPING = {
    "Status": "status",
    "Category": "category",
    "Expiration": "expiration",
    "Title": "title",
    "Notes": "notes",
}
EDIT_COLUMN_INDEX = len(TASK_TABLE_HEADERS)
COLUMN_WIDTHS = {
    0: 80,  # Status
    1: 100,  # Category
    2: 150,  # Expiration
    3: 250,  # Title
    4: 370,  # Notes
    5: 100,  # Edit
}
# TASKS_ROWS = ??


# Status des tâches
# =====================================
STATUS_DONE = True
STATUS_PENDING = False

# Tailles et positions de boutons
# =====================================

# Icônes de tâches
EDIT_ICON_SIZE = 18
EDIT_ICON_SPACING = 4
EDIT_ICON_TOP_OFFSET = 2
EDIT_SECTION_POSITIONS = ["delete", "edit", "check"]


# Valeurs par défaut
# =====================================
DEFAULT_DATETIME = QDateTime.currentDateTime().addDays(1)
DEFAULT_TITLE = "TASK"
DEFAULT_NOTES = ""
DEFAULT_STATUS = STATUS_PENDING
DEFAULT_CATEGORY = CATEGORIES[0]  # 'Général'
NO_ID = -1
