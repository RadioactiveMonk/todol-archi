# utils/status_utils.py

"""
Logique de représentation visuelle des statuts de tâche :
association entre un booléen de complétion et son label + couleur.
"""

from utils.log_utils import logger

STATUS_PENDING: bool = False
STATUS_DONE: bool = True

STATUS_UI: dict[bool, dict[str, str]] = {
    STATUS_DONE: {
        "label": "ROCKED!",
        "color": "green",
    },
    STATUS_PENDING: {
        "label": "PENDING",
        "color": "orange",
    },
}

DEFAULT_UI = {
    "label": "UNKNOWN",
    "color": "grey",
}


def get_status_ui(completed: bool) -> dict[str, str]:
    """
    Retourne un dictionnaire contenant le label et la couleur d’un statut donné.

    Args:
        completed: bool indiquant l'état de complétion

    Returns:
        dict avec les clés 'label' et 'color'
    """
    logger.debug("Accessing status datas")
    return STATUS_UI.get(completed, DEFAULT_UI)


def status_label(completed: bool) -> str:
    """Alias pour accéder uniquement au label."""
    return get_status_ui(completed)["label"]


def status_color(completed: bool) -> str:
    """Alias pour accéder uniquement à la couleur."""
    return get_status_ui(completed)["color"]
