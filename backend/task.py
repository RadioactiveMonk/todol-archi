from dataclasses import dataclass, field
from backend.config.constants import (
    DEFAULT_STATUS,
    DEFAULT_DATETIME,
    DEFAULT_TITLE,
    DEFAULT_NOTES,
    NO_ID
)
from backend.config.configs import DEFAULT_CATEGORY


@dataclass
class Task:
    """Représente une tâche"""

    tid: int = field(default=NO_ID) 
    status: bool = field(default=DEFAULT_STATUS)
    category: str = field(default=DEFAULT_CATEGORY)
    title: str = field(default=DEFAULT_TITLE)
    notes: str = field(default=DEFAULT_NOTES)
    expiration: str = field(
        default_factory=lambda: DEFAULT_DATETIME.toString("yyyy-MM-dd HH:mm")
    )
