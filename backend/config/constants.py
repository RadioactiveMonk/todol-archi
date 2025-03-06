from PyQt6.QtCore import QDateTime


# Headers du tableau des tâches
# =====================================
TASK_TABLE_HEADERS = ["Status", "Category", "Expiration", "Title", "Notes"]
COLUMN_MAPPING = {
    "Status": "status",
    "Category": "category",
    "Expiration": "expiration",
    "Title": "title",
    "Notes": "notes",
}


# Status des tâches
# =====================================
STATUS_DONE = True
STATUS_PENDING = False

# Tailles et positions de boutons
# =====================================


# Valeurs par défaut
# =====================================
DEFAULT_DATETIME = QDateTime.currentDateTime().addDays(1)
DEFAULT_TITLE = "TASK"
DEFAULT_NOTES = ""
DEFAULT_STATUS = False
NO_ID = -1
