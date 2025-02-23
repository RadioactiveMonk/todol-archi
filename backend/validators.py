from typing import Optional
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QMessageBox
from backend.constants import task_priorities


class Validators:
    """Regroupe les règles de validation"""

    @staticmethod
    def validate_title(title: str, parent=None) -> bool:
        """Vérifie que le titre d'une tâche est valide"""
        if not isinstance(title, str) or not title.strip():
            QMessageBox.warning(parent, "Erreur", "Le titre ne peut pas être vide.")
            return False
        return True

    @staticmethod
    def validate_due_date(due_date: Optional[QDate], parent=None) -> bool:
        """Vérifie que la date d'expiration est valide et n'est pas dans le passé."""
        if not isinstance(due_date, QDate):
            QMessageBox.warning(parent, "Erreur", "Date invalide.")
            return False

        if due_date < QDate.currentDate():
            QMessageBox.warning(
                parent,
                "Erreur",
                "La date d'expiration doit être aujourd'hui ou plus tard.",
            )
            return False

        return True  # ✅ Si la date est valide

    @staticmethod
    def validate_priority(priority: str, parent=None) -> bool:
        """Vérifie que la priorité est valide"""
        if priority not in task_priorities:
            QMessageBox.warning(
                parent, "Erreur", "Veuillez choisir une priorité valide."
            )
            return False
        return True

    @staticmethod
    def validate_category(category: Optional[str], parent=None) -> bool:
        """Vérifie que la catégorie existe"""
        if category is not None and (
            not isinstance(category, str) or not category.strip()
        ):
            QMessageBox.warning(parent, "Erreur", "Catégorie invalide")
            return False
        return True
