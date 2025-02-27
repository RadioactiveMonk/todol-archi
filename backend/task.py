from dataclasses import dataclass, field
from datetime import datetime
import uuid
from PyQt6.QtCore import QDate


@dataclass
class Task:
    """Représente une tâche dans la To-Do List."""

    status: bool = False
    category: str = ""
    title: str = ""
    notes: str = ""
    expiration: QDate = field(default_factory=lambda: QDate.currentDate().addDays(1))
    task_id: str = field(default_factory=lambda: str(uuid.uuid4()), init=False)

    def to_dict(self) -> dict:
        """Convertit une instance de Task en dictionnaire pour la sauvegarde JSON."""
        return {
            "task_id": self.task_id,
            "status": self.status,
            "category": self.category,
            "title": self.title,
            "notes": self.notes,
            "expiration": self.expiration,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Crée une instance de Task à partir d'un dictionnaire JSON."""

        instance = cls(
            task_id=data.get("task_id"),
            title=data.get("title", "Task title not found."),
            status=data.get("status", False),
            notes=data.get("notes"),
            expiration=data.get("expiration"),
        )
    

        # Mise à jour des champs non initialisés (init=False)
        instance.task_id = data.get("task_id", str(uuid.uuid4()))

        return instance
