from dataclasses import dataclass, field
import uuid
from PyQt6.QtCore import QDateTime
from backend.constants import (
    DEFAULT_STATUS,
    DEFAULT_DATETIME,
    DEFAULT_TITLE,
    DEFAULT_NOTES,
)
from backend.config import DEFAULT_CATEGORY


@dataclass
class Task:
    """Représente une tâche dans la To-Do List."""

    status: str = field(default=DEFAULT_STATUS)
    category: str = field(default=DEFAULT_CATEGORY)
    title: str = field(default=DEFAULT_TITLE)
    notes: str = field(default=DEFAULT_NOTES)
    expiration: QDateTime = field(default=DEFAULT_DATETIME)
    task_id: str = field(default_factory=lambda: str(uuid.uuid4()), init=False)

   