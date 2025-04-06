# helpers/status_constants.py

"""
Contient la logique de conversion entre état de complétion et labels/textes pour affichage.
Utile pour l'UI, les exports, les logs, etc.
"""

STATUS_LABELS = {
    True: "ROCKED",
    False: "PENDING",
}

STATUS_COLORS = {
    True: "green",
    False: "orange",
}


def status_label(completed: bool) -> str:
    """
    Retourne un label lisible selon l'état de complétion.

    Args:
        completed: booléen indiquant si la tâche est faite.

    Returns:
        Une chaîne comme "ROCKED" ou "PENDING"
    """
    return STATUS_LABELS.get(completed, "UNKNOWN")


def status_color(completed: bool) -> str:
    """
    Retourne une couleur indicative pour un statut (ex: UI).

    Args:
        completed: booléen indiquant si la tâche est faite.

    Returns:
        Une couleur sous forme de chaîne (ex: "green")
    """
    return STATUS_COLORS.get(completed, "grey")
