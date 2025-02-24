from dataclasses import dataclass, field
import uuid
from backend.validators import Validators
from typing import Optional
from PyQt6.QtCore import QDate


@dataclass
class Task:
    """Modèle de tâche avec validation automatique."""

    title: str
    task_uuid: str = field(default_factory=lambda: str(uuid.uuid4()), init=False)
    due_date: Optional[QDate] = None  # ✅ Stocké directement en `QDate`
    status: Optional[bool] = False
    priority: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self):
        """Valide automatiquement les champs après l'initialisation."""
        Validators.validate_title(self.title)

        if isinstance(self.due_date, QDate):  # ✅ Vérifie si c'est bien un `QDate`
            Validators.validate_due_date(self.due_date)

        if self.priority:
            Validators.validate_priority(self.priority)

    def to_dict(self) -> dict:
        """Convertit une instance de Task en dictionnaire pour la sauvegarde JSON."""
        return {
            "title": self.title,
            "status": self.status,
            "priority": self.priority,
            "description": self.description,
            "due_date": (
                self.due_date.toString("yyyy-MM-dd")
                if isinstance(self.due_date, QDate)
                else None
            ),  # ✅ Plus propre
            "task_uuid": self.task_uuid,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Crée une instance de Task à partir d'un dictionnaire JSON."""
        instance = cls(
            title=data["title"],
            status=data.get("status", False),
            priority=data.get("priority"),
            description=data.get("description"),
            due_date=(
                QDate.fromString(data["due_date"], "yyyy-MM-dd")
                if data.get("due_date")
                else None
            ),  # ✅ QDate directement
        )

        # ✅ Mise à jour des champs non initialisés (init=False)
        instance.task_uuid = data.get("task_uuid", str(uuid.uuid4()))
        return instance
