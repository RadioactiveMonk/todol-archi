from dataclasses import dataclass, field
from typing import Any

from core.default_values import (
    DEFAULT_CATEGORY,
    DEFAULT_DATETIME,
    DEFAULT_NOTES,
    DEFAULT_TITLE,
)
from core.status_constants import DEFAULT_STATUS
from helpers.converters import dataclass_to_dict


@dataclass
class Task:
    """Représente une tâche de l'application."""

    id: int | None = None
    completed: bool = field(default=DEFAULT_STATUS)
    category: str = field(default=DEFAULT_CATEGORY)
    expiration: str = field(
        default_factory=lambda: DEFAULT_DATETIME.toString("yyyy-MM-dd HH:mm")
    )
    title: str = field(default=DEFAULT_TITLE)
    notes: str = field(default=DEFAULT_NOTES)

    # --------- Propriétés utiles ---------

    @property
    def is_done(self) -> bool:
        """Renvoie l'état de complétion (alias plus lisible)."""
        return self.completed

    @is_done.setter
    def is_done(self, value: bool) -> None:
        """Permet de modifier completed via l'alias."""
        self.completed = bool(value)

    # --------- Conversions ---------

    def to_dict(self, exclude: set[str] | None = None) -> dict[str, Any]:
        """Retourne la tâche sous forme de dictionnaire."""
        return dataclass_to_dict(self, exclude=exclude)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Task":
        """Crée une instance de Task à partir d’un dictionnaire."""
        return cls(**data)

    # --------- Représentation ---------

    def __str__(self) -> str:
        return f"[{'✔' if self.completed else ' '}] {self.title} ({self.category})"

    def __repr__(self) -> str:
        return (
            f"Task(id={self.id}, title={self.title!r}, "
            f"done={self.completed}, expiration={self.expiration})"
        )
