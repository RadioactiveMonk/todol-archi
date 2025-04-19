from dataclasses import dataclass

from utils.log_utils import logger


@dataclass(frozen=True)
class TaskTableColumn:
    """Manages the comportment of columns"""

    name: str
    field: str
    width: int = 150
    editable: bool = True

TASK_TABLE_COLUMNS = [
    TaskTableColumn(name="ID", field="id", width=50, editable=False),
    TaskTableColumn(name="Title", field="title", width=250),
    TaskTableColumn(name="Category", field="category"),
    TaskTableColumn(name="Completed", field="completed"),
    TaskTableColumn(name="Expiration", field="expiration"),
    TaskTableColumn(name="Notes", field="notes"),
    TaskTableColumn(name="Edit", field="edit", width=100, editable=False),
]

def get_column_by_name(name: str) -> TaskTableColumn:
    for column in TASK_TABLE_COLUMNS:
        if column.name == name:
            return column
    logger.error(f"Column '{name}' not found.")
    raise

def get_all_column_names() -> list[str]:
    return [col.name for col in TASK_TABLE_COLUMNS]
