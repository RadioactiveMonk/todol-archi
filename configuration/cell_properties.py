from PyQt6.QtCore import QModelIndex, Qt
from backend.models.task_table_utils import TASK_TABLE_HEADERS, EDIT_COLUMN_INDEX, STATUS_COLUMN_INDEX


def get_flags(
    index: QModelIndex,
    edit_section: int = EDIT_COLUMN_INDEX,
    status_section: int = STATUS_COLUMN_INDEX,
) -> Qt.ItemFlag:
    """
    Retourne les propriétés (flags) associées à une cellule du tableau.

    - Colonne Status : sélectionnable + éditable (permet le toggle)
    - Colonne Edit   : activée uniquement (clic sur bouton)
    - Autres colonnes : désactivées par défaut ici (gérées ailleurs)

    Args:
        index (QModelIndex): index de la cellule
        edit_section (int): index de la colonne d'édition (par défaut la dernière)
        status_section (int): index de la colonne de statut (par défaut 0)

    Returns:
        Qt.ItemFlags: combinaisons de flags Qt pour la cellule
    """
    if not index.isValid():
        return Qt.ItemFlag.NoItemFlags

    if index.column() == edit_section:
        return Qt.ItemFlag.ItemIsEnabled

    if index.column() == status_section:
        return (
            Qt.ItemFlag.ItemIsEnabled
            | Qt.ItemFlag.ItemIsEditable
            | Qt.ItemFlag.ItemIsSelectable
        )

    return Qt.ItemFlag.NoItemFlags


def get_alignment(column: int) -> Qt.AlignmentFlag:
    """
    Retourne l'alignement du texte pour une colonne donnée.
    Actuellement : tout est centré, mais cette fonction permet d’adapter colonne par colonne.
    """
    return Qt.AlignmentFlag.AlignCenter
