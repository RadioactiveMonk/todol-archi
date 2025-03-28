from PyQt6.QtCore import QDateTime

# =====================================
# DOMAIN DEFAULTS
# =====================================

# Status
STATUS_DONE: bool = True
STATUS_PENDING: bool = False
DEFAULT_STATUS: bool = STATUS_PENDING

# Task values
DEFAULT_TITLE: str = "TASK"
DEFAULT_NOTES: str = ""

# Category
CATEGORIES: list[str] = ["General", "Work", "Hobbies"]
DEFAULT_CATEGORY: str = CATEGORIES[0]

# Expiration
DEFAULT_DATETIME: QDateTime = QDateTime.currentDateTime().addDays(1)

# Fallback
NO_ID: int = -1
