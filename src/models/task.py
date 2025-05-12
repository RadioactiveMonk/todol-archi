from dataclasses import dataclass
from typing import Any, Optional

from core.log_manager import logger
from helpers.converters import dataclass_to_dict
from models.task_core import TaskCore


@dataclass
class Task(TaskCore):
    """Représente une tâche complète avec affichage, helpers et validations."""

    # --------- Validations ---------

    def __setattr__(self, name: str, value: Any) -> None:
        IMMUTABLE_FIELDS = {"id", "created_at"}
        if name in IMMUTABLE_FIELDS and hasattr(self, name):
            raise AttributeError(f"Field '{name}' is read-only after creation")
        super().__setattr__(name, value)

    # --------- Méthodes métier ---------

    def toggle_status(self) -> None:
        """
        Toggles the completion status of the task.
        """
        self.completed = not self.completed

    def update_fields(self, updates: dict[str, Any]) -> None:
        """Update the task with provided attribute and value in dict format"""
        for key, value in updates.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                logger.warning(f"Ignored unknown field for task: {key}")

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
