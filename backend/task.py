from dataclasses import dataclass, field
import uuid
from PyQt6.QtCore import QDate
from typing import Optional
from backend.constants import DEFAULT_CATEGORY, DEFAULT_STATUS


@dataclass
class Task:
    """Représente une tâche dans la To-Do List."""

    status: Optional[str] = DEFAULT_STATUS
    category: Optional[str] = DEFAULT_CATEGORY
    title: str = ""
    notes: Optional[str] = ""
    expiration: QDate = field(default_factory=lambda: QDate.currentDate().addDays(1))
    task_id: str = field(default_factory=lambda: str(uuid.uuid4()), init=False)

    def to_dict(self) -> dict:
        """Convertit une instance de Task en dictionnaire pour la sauvegarde JSON."""
        return {
            "status": self.status,
            "category": self.category,
            "title": self.title,
            "notes": self.notes,
            "expiration": QDate.toString(self.expiration),
            "task_id": self.task_id,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Crée une instance de Task à partir d'un dictionnaire JSON."""

        instance = cls(
            status=data.get("status", DEFAULT_STATUS),
            category=data.get("category", DEFAULT_CATEGORY),
            title=data.get("title", ""),
            notes=data.get("notes", ""),
            expiration=data.get("expiration", ""),
        )
        # Mise à jour des champs non initialisés (init=False)
        instance.task_id = data.get("task_id", str(uuid.uuid4()))

        return instance
