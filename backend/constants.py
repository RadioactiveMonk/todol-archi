from PyQt6.QtCore import QDateTime


# Headers du tableau des tâches
# =====================================
TASK_HEADERS = ["Status", "Category", "Expiration", "Title", "Notes"]

# Status des tâches
# =====================================
STATUS_DONE = "✅"
STATUS_PENDING = "⏳"

# Valeurs par défaut
# =====================================
DEFAULT_DATETIME = QDateTime.currentDateTime().addDays(1)
DEFAULT_TITLE = "TASK"
DEFAULT_NOTES = ""
DEFAULT_STATUS = STATUS_PENDING

