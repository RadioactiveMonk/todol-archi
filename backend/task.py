from dataclasses import dataclass, field
from typing import Optional
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

    tid: Optional[int] = None  # maintenant géré par SQL
    status: bool= field(default=DEFAULT_STATUS)
    category: str = field(default=DEFAULT_CATEGORY)
    title: str = field(default=DEFAULT_TITLE)
    notes: str = field(default=DEFAULT_NOTES)
    expiration: str = field(default_factory=lambda: DEFAULT_DATETIME.toString("yyyy-MM-dd HH:mm"))
