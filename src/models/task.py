from dataclasses import dataclass
from typing import Any, Optional

from core.log_manager import logger
from helpers.converters import dataclass_to_dict
from models.task_core import TaskCore


@dataclass
class Task(TaskCore):
    """Represents a complete task with additional helpers and validations."""

    def toggle_status(self) -> None:
        """Toggle the completion status of the task."""
        self.completed = not self.completed

    def update_fields(self, updates: dict[str, Any]) -> None:
        """Update the task with provided attribute and value in dict format.

        Args:
            updates (dict[str, Any]): Dictionary with attribute names and their new values.
        """
        for key, value in updates.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                logger.warning(f"Ignored unknown field for task: {key}")

    def to_dict(self, exclude: Optional[set[str]] = None) -> dict[str, Any]:
        """Return the task as a dictionary.

        Args:
            exclude (Optional[set[str]]): Set of field names to exclude from the result.

        Returns:
            dict[str, Any]: Dictionary representation of the task.
        """
        return dataclass_to_dict(self, exclude=exclude)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Task":
        """Create a Task instance from a dictionary.

        Args:
            data (dict[str, Any]): Dictionary with task data.

        Returns:
            Task: A new Task instance.

        Raises:
            TypeError: If the dictionary doesn't match expected fields.
        """
        try:
            return cls(**data)
        except TypeError as e:
            logger.error(f"Failed to create Task from dict: {e}")
            raise

    def __str__(self) -> str:
        """Return a user-friendly string representation of the task."""
        return f"[{'ROCKED' if self.completed else 'PENDING'}] {self.title} ({self.category})"

    def __repr__(self) -> str:
        """Return a developer-friendly representation of the task."""
        return (
            f"Task(id={self.id}, title={self.title!r}, "
            f"done={self.completed}, expiration={self.expiration})"
        )
