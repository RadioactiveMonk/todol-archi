# Constantes du tableau des tâches
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
    5: 100,  # Edit section
}
