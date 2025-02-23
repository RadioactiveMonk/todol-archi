from dataclasses import dataclass, field
from datetime import datetime
import uuid
from backend.validators import Validators
from typing import Optional
from PyQt6.QtCore import QDate


@dataclass
class Task:
    """Modèle de tâche avec validation automatique."""

    title: str
    task_uuid: str = field(default_factory=lambda: str(uuid.uuid4()), init=False)
    created_at: datetime = field(default_factory=datetime.now, init=False)

    # Valeurs optionnelles
    status: bool = False
    priority: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None

    def __post_init__(self):
        """Valide automatiquement les champs après l'initialisation."""
        Validators.validate_title(self.title)

        if self.due_date:
            qdate_due = QDate(
                self.due_date.year, self.due_date.month, self.due_date.day
            )  # ✅ Conversion
            Validators.validate_due_date(qdate_due)  # ✅ Maintenant `QDate` est valide

        if self.priority:  # ✅ Vérifie la priorité si elle est définie
            Validators.validate_priority(self.priority)

    def to_dict(self) -> dict:
        """Convertit une instance de Task en dictionnaire pour la sauvegarde JSON."""
        return {
            "title": self.title,
            "status": self.status,
            "priority": self.priority,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "due_date": self.due_date.isoformat() if self.due_date else None,
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
                datetime.fromisoformat(data["due_date"])
                if data.get("due_date")
                else None
            ),
        )

        # Mise à jour des champs non initialisés (init=False)
        instance.task_uuid = data.get("task_uuid", str(uuid.uuid4()))
        instance.created_at = datetime.fromisoformat(
            data.get("created_at", datetime.now().isoformat())
        )

        return instance
