from PyQt6.QtCore import QAbstractTableModel, QModelIndex, QObject, Qt


class TaskTableModel(QAbstractTableModel):
    ...

    def setData(self, index: QModelIndex, value, role: int) -> bool:
        """Supprime une tâche lorsqu'on clique sur le bouton 'Supprimer'."""
        if role == Qt.ItemDataRole.EditRole and index.column() == len(
            TASK_TABLE_HEADERS
        ):
            task = self.tasks[index.row()]
            self.database.del_task(task.tid)  # Suppression dans la DB
            self.tasks.pop(index.row())  # Suppression dans le modèle
            self.layoutChanged.emit()  # 🔥 Mise à jour de l'affichage
            return True
        return False
