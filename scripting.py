class TaskTable(QTableView):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        self.database = DatabaseManager()
        self.table_model = TaskTableModel(self, self.database)
        self.setModel(self.table_model)

        # 🔥 Ajout du délégué pour la colonne "Actions"
        self.setItemDelegateForColumn(
            len(TASK_TABLE_HEADERS), DeleteButtonDelegate(self)
        )
