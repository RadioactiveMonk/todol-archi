from dataclasses import dataclass
from typing import Optional

from PySide6.QtCore import Qt

from ui.delegates.edit_delegate import EditDelegate
from ui.delegates.status_delegate import StatusEditDelegate
from utils.log_utils import logger


def flags_editable() -> Qt.ItemFlag:
    """Return flags to make column editable"""
    return (
        Qt.ItemFlag.ItemIsEnabled
        | Qt.ItemFlag.ItemIsEditable
        | Qt.ItemFlag.ItemIsSelectable
    )


def flags_selectable() -> Qt.ItemFlag:
    """Return flags to make column selectable"""
    return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable


def flags_checkbox() -> Qt.ItemFlag:
    """Return flags to make column checkable"""
    return (
        Qt.ItemFlag.ItemIsEnabled
        | Qt.ItemFlag.ItemIsSelectable
        | Qt.ItemFlag.ItemIsUserCheckable
    )


def text_alignment(position: str) -> Qt.AlignmentFlag:
    """Returns text alignment for columns"""
    options = {
        "left": Qt.AlignmentFlag.AlignLeft,
        "center": Qt.AlignmentFlag.AlignCenter,
        "right": Qt.AlignmentFlag.AlignRight,
    }
    if position in options:
        return options[position]

    logger.error(f"Unknown alignment position '{position}', falling back to center.")
    return Qt.AlignmentFlag.AlignCenter


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
        delegate=StatusEditDelegate,
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


def get_column_by_name(name: str) -> TaskTableColumn:
    """Returns column name or raise an error if not found"""
    for column in TASK_TABLE_COLUMNS:
        if column.name == name:
            return column
    logger.error(f"Column '{name}' not found.")
    raise


def get_column_index(field: str) -> Optional[int]:
    """
    Return the index of the column with the given field name.
    Return None if no column found.
    """
    for index, column in enumerate(TASK_TABLE_COLUMNS):
        if column.field == field:
            return index
    return None


def get_all_column_names() -> list[str]:
    """Returns a list of all columns names"""
    return [col.name for col in TASK_TABLE_COLUMNS]


def get_flags_for_column(name: str) -> Qt.ItemFlag:
    """Return the flags for the given column, with fallback if not explicitly set."""
    column = get_column_by_name(name)
    if column.flags is not None:
        return column.flags
    return flags_editable() if column.editable else flags_selectable()
