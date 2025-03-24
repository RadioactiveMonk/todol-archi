from PyQt6.QtCore import QModelIndex, Qt
from backend.models.task_table_utils import TASK_TABLE_HEADERS


def get_flags(index: QModelIndex, edit_section: int = len(TASK_TABLE_HEADERS), status_section: int = 0) -> Qt.ItemFlag:
    """Définit les propriétés des cellules (éditables, sélectionnables)"""

    if not index.isValid():
        return Qt.ItemFlag.NoItemFlags  # Empeche d'interagir avec une cellule invalide

    if index.column() == edit_section:
        return Qt.ItemFlag.ItemIsEnabled

    if index.column() == status_section:  # Colonne status
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsSelectable

    return Qt.ItemFlag.NoItemFlags
