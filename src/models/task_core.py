from dataclasses import asdict, dataclass
from typing import Any, Dict, Optional

from core.defaults import (
    DEFAULT_CATEGORY,
    DEFAULT_EXPIRATION,
    DEFAULT_NOTES,
    DEFAULT_STATUS,
    DEFAULT_TITLE,
)


@dataclass
class TaskCore:
    """Represents a base task object with core attributes only."""

    id: Optional[int] = None
    title: str = DEFAULT_TITLE
    category: str = DEFAULT_CATEGORY
    completed: bool = DEFAULT_STATUS
    expiration: str = DEFAULT_EXPIRATION
    notes: str = DEFAULT_NOTES

    def __eq__(self, other: object) -> bool:
        """Check equality based on the 'id' attribute.

        Args:
            other (object): Object to compare.

        Returns:
            bool: True if both objects are TaskCore with the same ID, else False.
        """
        if not isinstance(other, TaskCore):
            return NotImplemented
        return self.id == other.id

    @classmethod
    def from_dict(cls, data: dict) -> "TaskCore":
        """Create a TaskCore instance from a dictionary.

        Args:
            data (dict): Task data with fields matching TaskCore.

        Returns:
            TaskCore: An instance built from the provided data.
        """
        return cls(**data)

    def to_dict(self) -> Dict[str, Any]:
        """Convert the TaskCore instance to a dictionary.

        Returns:
            Dict[str, Any]: Dictionary representation of the task.
        """
        return asdict(self)
