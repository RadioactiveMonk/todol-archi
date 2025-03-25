# task_table_utils.py

from typing import Dict, List

# 🌟 Noms affichés dans l'entête du tableau
TASK_TABLE_HEADERS: List[str] = [
    "Status",
    "Category",
    "Expiration",
    "Title",
    "Notes",
    "Edit",
]

# 🔁 Mapping entre les noms affichés et les clés de données dans les tâches
COLUMN_MAPPING: Dict[str, str] = {
    "Status": "completed",
    "Category": "category",
    "Expiration": "expiration",
    "Title": "title",
    "Notes": "notes",
}

# 🖱️ Colonnes spécifiques pour interactions (non mappées à des attributs)
EDIT_COLUMN: str = TASK_TABLE_HEADERS[-1]
STATUS_COLUMN: str = TASK_TABLE_HEADERS[0]
EDIT_COLUMN_INDEX: int = len(TASK_TABLE_HEADERS)
STATUS_COLUMN_INDEX: int = TASK_TABLE_HEADERS.index("Status")


# 📐 Largeurs personnalisées des colonnes
COLUMN_WIDTHS: Dict[int, int] = {
    0: 100,  # Status
    1: 100,  # Category
    2: 150,  # Expiration
    3: 250,  # Title
    4: 370,  # Notes
    5: 80,  # Edit
}

# ✅ Statuts UI (affichage visuel)
STATUS_DONE_UI: str = "[ROCKED]"
STATUS_PENDING_UI: str = "[PENDING]"
