from dataclasses import dataclass
from typing import Optional


@dataclass
class TaskCore:
    """Représente une tâche de l'application."""

    id: Optional[int] = None
    title: str = ""
    category: str = ""
    completed: bool = False
    expiration: str = "2025-08-08 00:00"
    notes: str = ""

