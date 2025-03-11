from PyQt6.QtCore import QDateTime


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
# TASKS_ROWS = ??


# Status des tâches
# =====================================
STATUS_DONE = 1
STATUS_PENDING = 0

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
NO_ID = -1
