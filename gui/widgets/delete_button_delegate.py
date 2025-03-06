from PyQt6.QtWidgets import QStyledItemDelegate, QPushButton
from PyQt6.QtCore import QModelIndex, Qt, QEvent
from backend.config.constants import DELETE_BUTTON_DELEGATE_SIZE


class DeleteButtonDelegate(QStyledItemDelegate):
    """Délégué pour afficher un bouton '🗑️ Supprimer' dans la colonne 'Actions'."""

    def createEditor(self, parent, option, index: QModelIndex = QModelIndex()):
        """Crée un bouton 'Supprimer' et le lie à l'action de suppression."""
        btn: QPushButton = QPushButton("🗑️", parent)
        btn.setFixedSize(*DELETE_BUTTON_DELEGATE_SIZE)

        if index.isValid():
            # 🔥 Correction : On récupère explicitement `task_model` à partir de `index.model()`
            task_model = (
                index.model()
            )  # ✅ On évite `model` pour ne pas entrer en conflit avec PyQt6
            btn.clicked.connect(lambda: self.delete_task(task_model, index.row()))

        return btn

    def delete_task(self, task_model, row: int):
        """Supprime une tâche via 'TaskTableModel'."""
        if task_model:  # ✅ Vérifie que le modèle existe
            task_model.delete_task(row)  # ✅ Appelle `delete_task()` correctement
