from dataclasses import dataclass
from typing import Any, Optional

from core.log_manager import logger
from helpers.converters import dataclass_to_dict
from models.task_core import TaskCore


@dataclass
class Task(TaskCore):
    """Représente une tâche complète avec affichage, helpers et validations."""

    # --------- Propriétés utiles ---------

    @property
    def is_completed(self) -> bool:
        """Alias plus lisible pour completed."""
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
