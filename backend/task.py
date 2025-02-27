from dataclasses import dataclass, field
import uuid
from PyQt6.QtCore import QDateTime
from backend.constants import (
    DEFAULT_CATEGORY,
    DEFAULT_STATUS,
    DEFAULT_DATETIME,
    DEFAULT_TITLE,
    DEFAULT_NOTES,
)


@dataclass
class Task:
    """Représente une tâche dans la To-Do List."""

    status: str = field(default=DEFAULT_STATUS)
    category: str = field(default=DEFAULT_CATEGORY)
    title: str = field(default=DEFAULT_TITLE)
    notes: str = field(default=DEFAULT_NOTES)
    expiration: QDateTime = field(default=DEFAULT_DATETIME)
    task_id: str = field(default_factory=lambda: str(uuid.uuid4()), init=False)

    def to_dict(self) -> dict:
        """Convertit une instance de Task en dictionnaire pour la sauvegarde JSON."""
        return {
            "status": self.status,
            "category": self.category,
            "title": self.title,
            "notes": self.notes,
            "expiration": self.expiration.toString("yyyy-MM-dd HH:mm"),
            "task_id": self.task_id,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Crée une instance de Task à partir d'un dictionnaire JSON."""

        instance = cls(
            status=data.get("status", DEFAULT_STATUS),
            category=data.get("category", DEFAULT_CATEGORY),
            title=data.get("title", DEFAULT_TITLE),
            notes=data.get("notes", DEFAULT_NOTES),
            expiration=QDateTime.fromString(data.get("expiration"), "yyyy-MM-dd HH:mm"),
        )
        # Mise à jour des champs non initialisés (init=False)
        instance.task_id = data.get("task_id", str(uuid.uuid4()))

        return instance
