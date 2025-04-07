from dataclasses import dataclass, field
from typing import Any, Optional

from core.default_values import (
    DEFAULT_CATEGORY,
    DEFAULT_NOTES,
    DEFAULT_STATUS,
    DEFAULT_TITLE,
)
from helpers.converters import dataclass_to_dict
from helpers.log_utils import logger


@dataclass
class Task:
    """Représente une tâche de l'application."""

    id: Optional[int] = None
    title: str = field(default=DEFAULT_TITLE)
    category: str = field(default=DEFAULT_CATEGORY)
    expiration: str = "2025-01-01 00:00"
    completed: bool = field(default=DEFAULT_STATUS)
    notes: str = field(default=DEFAULT_NOTES)

    # --------- Propriétés utiles ---------

    @property
    def is_completed(self) -> bool:
        """Renvoie l'état de complétion (alias plus lisible)."""
        return self.completed

    @is_completed.setter
    def is_completed(self, value: bool) -> None:
        """Permet de modifier completed via l'alias."""
        self.completed = bool(value)

    # --------- Conversions ---------

    def to_dict(self, exclude: Optional[set[str]] = None) -> dict[str, Any]:
        """Retourne la tâche sous forme de dictionnaire."""
        return dataclass_to_dict(self, exclude=exclude)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Task":
        """Crée une instance de Task à partir d’un dictionnaire."""
        try:
            return cls(**data)
        except TypeError as e:
            logger.error(f"Failed to create Task from dict: {e}")
            raise

    # --------- Représentation ---------

    def __str__(self) -> str:
        return f"[{'ROCKED' if self.completed else 'PENDING'}] {self.title} ({self.category})"

    def __repr__(self) -> str:
        return (
            f"Task(id={self.id}, title={self.title!r}, "
            f"done={self.completed}, expiration={self.expiration})"
        )
