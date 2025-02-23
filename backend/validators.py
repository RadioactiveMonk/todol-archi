from typing import List, Dict, Any, Optional, Union
from PyQt6.QtCore import QDate  # Gestion de dates de PyQt6
from backend.constants import task_priorities


class Validators:
    """Regroupe les règles de validation"""

    @staticmethod  # pourquoi ? Eviter self ?
    def validate_title(title: str) -> None:
        """Vérifie que le titre d'une tâche est valide"""
        if not title.strip() or not isinstance(
            title, str
        ):  # Si y a rien à enlever c'est que c'est vide ..
            raise ValueError("Titre invalide")

    @staticmethod
    def validate_due_date(due_date: Optional[QDate]) -> None:
        """Vérifie que la date d'expiration est valide et n'est pas dans le passé"""
        if not isinstance(due_date, QDate):  # ✅ Vérifie que c'est bien un objet QDate
            raise ValueError("Date invalide")

        if due_date < QDate.currentDate():  # ✅ Comparaison valide maintenant
            raise ValueError("La date d'expiration doit être aujourd'hui ou plus tard.")

    @staticmethod
    def validate_priority(priority: str) -> None:
        """Vérifie que la priorité est valide"""
        if priority not in task_priorities:
            raise ValueError("Veuillez choisir une priorité valide.")

    @staticmethod
    def validate_category(category: Optional[str]) -> None:
        """Vérifie que la catégorie existe"""
        if category != None and (not isinstance(category, str) or not category.strip()):
            raise ValueError("Catégorie invalide")
