from PyQt6.QtCore import Qt

from utils.log_utils import logger

_COLUMN_FLAGS = {
    "Edit": Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable,
    "Status": Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsUserCheckable,
}

DEFAULT_FLAGS = Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable


def get_column_flags(column: str) -> Qt.ItemFlag:
    """
    Retourne les Qt.ItemFlags associés à une colonne du tableau.
    """
    if column in _COLUMN_FLAGS:
        return _COLUMN_FLAGS[column]

    logger.debug(f"No specific flags set for column '{column}', using default.")
    return DEFAULT_FLAGS
    


def get_alignment(column: int) -> Qt.AlignmentFlag:
    """
    Retourne l'alignement du texte pour une colonne donnée.
    Actuellement : tout est centré, mais cette fonction permet d’adapter colonne par colonne.
    """
    return Qt.AlignmentFlag.AlignCenter
