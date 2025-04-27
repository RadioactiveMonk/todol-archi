from PySide6.QtCore import Qt

from ui.containers.task_table_view import TaskTableView
from utils.task_table_column_utils import TaskTableColumn


def apply_column_config(view: TaskTableView, columns: list[TaskTableColumn]) -> None:
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
        
