from typing import Optional

from PySide6.QtCore import Qt

from models.task_table_column import TaskTableColumn


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
    return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsUserCheckable


def text_alignment(align: str) -> Qt.AlignmentFlag:
    """Returns text alignment for columns"""
    return {
        "left": Qt.AlignmentFlag.AlignLeft,
        "center": Qt.AlignmentFlag.AlignCenter,
        "right": Qt.AlignmentFlag.AlignRight,
    }.get(align, Qt.AlignmentFlag.AlignLeft)


def get_flags_for_column(
    field: str, columns: list[TaskTableColumn]
) -> Optional[Qt.ItemFlag]:
    """Return the flags for the given column, with fallback if not explicitly set."""
    return next((c.flags for c in columns if c.field == field), None)


def get_column_by_field(
    field: str, columns: list[TaskTableColumn]
) -> Optional[TaskTableColumn]:
    return next((c for c in columns if c.field == field), None)


def get_column_index(name: str, columns: list[TaskTableColumn]) -> Optional[int]:
    """
    Return the index of the column with the given field name.
    Return None if no column found.
    """
    return next((i for i, col in enumerate(columns) if col.name == name), None)


def get_all_column_names(columns: list[TaskTableColumn]) -> list[str]:
    """Returns a list of all columns names"""
    return [c.name for c in columns]
