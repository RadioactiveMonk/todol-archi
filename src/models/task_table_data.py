from helpers.ui_helpers import flags_checkbox, flags_selectable
from models.task_table_column import TaskTableColumn

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
    ),
]
