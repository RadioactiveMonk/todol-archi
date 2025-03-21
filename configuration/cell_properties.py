from PyQt6.QtCore import QModelIndex, Qt
from backend.models.task_table_utils import TASK_TABLE_HEADERS


def get_flags(index: QModelIndex, total_columns: int = len(TASK_TABLE_HEADERS)) -> Qt.ItemFlag:
    """Définit les propriétés des cellules (éditables, sélectionnables)"""

    if not index.isValid():
        return Qt.ItemFlag.NoItemFlags  # Empeche d'interagir avec une cellule invalide

    if index.column() == total_columns:
        return Qt.ItemFlag.ItemIsEnabled

    return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable
