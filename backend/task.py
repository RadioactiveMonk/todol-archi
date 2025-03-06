from dataclasses import dataclass, field
from backend.constants import (
    DEFAULT_STATUS,
    DEFAULT_DATETIME,
    DEFAULT_TITLE,
    DEFAULT_NOTES,
)
from backend.config import DEFAULT_CATEGORY
from backend.constants import NO_ID


@dataclass
class Task:
    """Représente une tâche dans la To-Do List."""

    tid: int = field(default=NO_ID)  # maintenant géré par SQL (None est remplacé par -1)
    status: bool = field(default=DEFAULT_STATUS)
    category: str = field(default=DEFAULT_CATEGORY)
    title: str = field(default=DEFAULT_TITLE)
    notes: str = field(default=DEFAULT_NOTES)
    expiration: str = field(
        default_factory=lambda: DEFAULT_DATETIME.toString("yyyy-MM-dd HH:mm")
    )
