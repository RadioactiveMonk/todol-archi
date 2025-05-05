from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableView

from models.task_table_column import TaskTableColumn


def apply_delegate_for_column(view: QTableView, columns: list[TaskTableColumn]) -> None:
    """
    Apply delegates dynamically to a QTableView based on provided TaskTableColumn list.

    Parameters
    ----------
    view : QTableView
        the task table view
    columns : list[TaskTableColumn]
        list of columns and their properties
    """

    for index, column in enumerate(columns):
        if column.delegate:
            delegate_instance = column.delegate(view)
            view.setItemDelegateForColumn(index, delegate_instance)

            if hasattr(view, "column_delegates"):
                view.column_delegates[index] = delegate_instance


def apply_column_config(view: QTableView, columns: list[TaskTableColumn]) -> None:
    """
    Apply column configuration to a QTableView based on provided TaskTableColumn list.
    """
    for index, column in enumerate(columns):
        view.setColumnHidden(index, not column.visible)
        view.model().setHeaderData(index, Qt.Orientation.Horizontal, column.name)

        if column.tooltip:
            view.model().setHeaderData(
                index,
                Qt.Orientation.Horizontal,
                column.tooltip,
                role=Qt.ItemDataRole.ToolTipRole,
            )
