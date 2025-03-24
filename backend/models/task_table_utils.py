# Constantes du tableau des tâches
# =====================================
TASK_TABLE_HEADERS = ["Status", "Category", "Expiration", "Title", "Notes", "Edit"]
COLUMN_MAPPING = {
    "Status": "completed",
    "Category": "category",
    "Expiration": "expiration",
    "Title": "title",
    "Notes": "notes",
}  # Edit n'est pas mappé, ne fait pas partie des attributs de tâche
EDIT_COLUMN = TASK_TABLE_HEADERS[-1]
STATUS_COLUMN = TASK_TABLE_HEADERS[0]
COLUMN_WIDTHS = {
    0: 100,  # Status
    1: 100,  # Category
    2: 150,  # Expiration
    3: 250,  # Title
    4: 370,  # Notes
    5: 80,  # Edit section (stretched to content)
}
STATUS_DONE_UI = "[ROCKED]"
STATUS_PENDING_UI = "[PENDING]"
