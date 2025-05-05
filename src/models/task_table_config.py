from dataclasses import dataclass
from typing import Optional

from PySide6.QtCore import Qt

from helpers.ui_helpers import (
    flags_checkbox,
    flags_selectable,
    text_alignment,
)
from ui.delegates import EditDelegate


@dataclass(frozen=True)
class TaskTableColumn:
    """Representation of task table columns"""

    name: str
    field: str
    width: int = 150
    editable: bool = True
    alignment: Qt.AlignmentFlag = text_alignment("center")
    flags: Optional[Qt.ItemFlag] = None
    visible: bool = True
    tooltip: Optional[str] = None
    delegate: Optional[type] = None


TASK_TABLE_COLUMNS = [
    TaskTableColumn(
        name="ID",
        field="id",
        width=50,
        editable=False,
        flags=flags_selectable(),
    ),
    TaskTableColumn(name="Title", field="title", width=250, tooltip="Task title"),
    TaskTableColumn(name="Category", field="category"),
    TaskTableColumn(
        name="Status",
        field="completed",
        flags=flags_checkbox(),
    ),
    TaskTableColumn(name="Expiration", field="expiration"),
    TaskTableColumn(name="Notes", field="notes"),
    TaskTableColumn(
        name="Edit",
        field="edit",
        width=100,
        editable=False,
        flags=flags_selectable(),
        delegate=EditDelegate,
    ),
]



