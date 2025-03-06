from PyQt6.QtWidgets import QStyledItemDelegate, QPushButton
from PyQt6.QtCore import QModelIndex, Qt
from backend.config.constants import DELETE_BUTTON_DELEGATE_SIZE


class DeleteButtonDelegate(QStyledItemDelegate):
    """Délégué pour afficher un boutton 'supprimer' dans la colone 'actions'"""

    def createEditor(self, parent, option, index: QModelIndex | None = QModelIndex()):
        """Crée un bouton et le lie à la suppression"""

        btn: QPushButton = QPushButton("🗑️", parent)
        btn.setFixedSize(*DELETE_BUTTON_DELEGATE_SIZE)
        btn.clicked.connect(lambda: self.delete_task(index.model(), index.row()))
        return btn
                            
    def delete_task(self, model, row: int):
        """Supprime une tâche via 'TaskTableModel'"""
        model.delete_task(row)
    
    
