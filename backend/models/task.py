from dataclasses import dataclass, field
from configuration.constants import (
    DEFAULT_STATUS,
    DEFAULT_DATETIME,
    DEFAULT_TITLE,
    DEFAULT_NOTES,
    DEFAULT_CATEGORY,
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
