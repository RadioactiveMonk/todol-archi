from dataclasses import dataclass, field
from datetime import datetime
import uuid
from collections import namedtuple
from backend.validators import BaseValidator, DateValidator, validate_fields
from typing import Optional

# Creation d'un namedtuple pour les priorités de tâches.
Priority = namedtuple("Priority", ["urgent", "important", "secondary"])
PRIORITY = Priority(urgent="Urgent", important="Important", secondary="Secondaire")


@dataclass
class Task:
    """Modèle de tâche avec validation automatique."""

    title: str = field(metadata={"validator": BaseValidator(str, "")})
    task_uuid: str = field(default_factory=lambda: str(uuid.uuid4()), init=False)
    created_at: datetime = field(default_factory=datetime.now, init=False)

    # Valeurs optionnelles

    status: bool = field(
        default=False,
        metadata={
            "validator": BaseValidator(bool, False)
        },  # Attend un bool False par défaut.
    )
    priority: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)
    expiration: Optional[datetime] = field(
        default=None,
        metadata={"validator": DateValidator(allow_past=False)},
    )

    def to_dict(self) -> dict:
        """Convertit une instance de Task en dictionnaire pour la sauvegarde JSON."""
        return {
            "title": self.title,
            "status": self.status,
            "priority": self.priority,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "expiration": (
                self.expiration.isoformat() if self.expiration else None
            ),  # Si expiration n'est pas renseigné, isoformat ne fonctionne pas sur None.
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
            expiration=(
                datetime.fromisoformat(data["expiration"])
                if data.get("expiration")
                else None  # Si expiration n'est pas renseigné fromisoformat ne fonctionne pas, on ajoute une condition
            ),
        )

        # Mise à jour des champs non initialisés (init=False)
        instance.task_uuid = data.get("task_uuid", str(uuid.uuid4()))
        instance.created_at = datetime.fromisoformat(
            data.get("created_ad", datetime.now().isoformat())
        )

        return instance

    def validate(self) -> bool:
        """Valide les champs en appelant validate_fields (validation.py)"""
        return validate_fields(self)
