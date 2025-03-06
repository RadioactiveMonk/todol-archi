from gui.widgets.delete_button_delegate import DeleteButtonDelegate


class TaskTable(QTableView):
    """Tableau des tâches avec gestion des actions."""

    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        self.database = DatabaseManager()
        self.table_model = TaskTableModel(self, self.database)
        self.setModel(self.table_model)

        # ✅ Appliquer le délégué pour la colonne "Actions"
        self.setItemDelegateForColumn(
            self.table_model.columnCount() - 1, DeleteButtonDelegate(self)
        )

        self.setup_ui()
