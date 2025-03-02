import sqlite3
from typing import List, Dict, Any, Optional, Union
from backend.task import Task


class DatabaseManager:
    """Gestion de la base de donnée."""

    def __init__(self) -> None:
        pass

    def _connect(self):
        pass

    def _create_table(self):
        pass

    def add_task(self, title: str):
        pass

    def update_task(self, task_id: str):
        pass

    def del_task(self, task_id: str) -> None:
        pass

    def get_tasks(self) -> List[Task]:
        return []
