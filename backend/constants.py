from PyQt6.QtCore import QDate

# ==================== CATEGORIES DES TÂCHES ====================

CATEGORIES = ["General", "Work", "Home", "Personnal", "Family", "Pets",]

# ==================== HEADERS DU TABLEAU DES TÂCHES ====================

TASK_HEADERS = ["Status", "Category", "Expiration", "Title", "Notes"]

# ==================== STATUTS DES TÂCHES ====================

STATUS_DONE = "✅"
STATUS_PENDING = "⏳"

# ==================== VALEURS PAR DEFAUT ====================

DEFAULT_EXPIRATION = QDate.currentDate().addDays(1)
DEFAULT_TITLE = "TASK"
DEFAULT_NOTES = ""
DEFAULT_STATUS = STATUS_PENDING
DEFAULT_CATEGORY = CATEGORIES[0]
