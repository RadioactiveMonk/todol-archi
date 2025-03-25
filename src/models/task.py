from dataclasses import dataclass, field

from src.core.settings.constants import (
    DEFAULT_CATEGORY,
    DEFAULT_DATETIME,
    DEFAULT_NOTES,
    DEFAULT_STATUS,
    DEFAULT_TITLE,
)


@dataclass
class Task:
    """Represent a task"""

    tid: int | None = None
    completed: bool = field(default=DEFAULT_STATUS)
    category: str = field(default=DEFAULT_CATEGORY)
    expiration: str = field(
        default_factory=lambda: DEFAULT_DATETIME.toString("yyyy-MM-dd HH:mm")
    )
    title: str = field(default=DEFAULT_TITLE)
    notes: str = field(default=DEFAULT_NOTES)
