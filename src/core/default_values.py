from PyQt6.QtCore import QDateTime

# =====================================
# DOMAIN DEFAULTS
# =====================================


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
