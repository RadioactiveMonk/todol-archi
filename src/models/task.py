from dataclasses import dataclass, field
from typing import Optional

from core.default_values import (
    DEFAULT_CATEGORY,
    DEFAULT_NOTES,
    DEFAULT_STATUS,
    DEFAULT_TITLE,
)


@dataclass
class Task:
    """Représente une tâche de l'application."""

    id: Optional[int] = None
    title: str = field(default=DEFAULT_TITLE)
    category: str = field(default=DEFAULT_CATEGORY)
    expiration: str = "2025-01-01 00:00"
    completed: bool = field(default=DEFAULT_STATUS)
    notes: str = field(default=DEFAULT_NOTES)

