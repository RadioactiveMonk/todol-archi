from typing import List, Dict, Any, Optional, Union
from PyQt6.QtCore import QAbstractTableModel, QModelIndex, QObject, Qt


class TaskTableModel(QAbstractTableModel):
    """Modèle de donnée a afficher dans TaskTable (widgets.py)"""

    def __init__(self, parent: QObject) -> None:
        super().__init__(parent)

    def rowCount(self, parent: QModelIndex) -> int:
        return super().rowCount(parent)
    
    def columnCount(self, parent: QModelIndex) -> int:
        return super().columnCount(parent)
    
    def headerData(self, section: int, orientation: Qt.Orientation, role: int) -> Any:
        return super().headerData(section, orientation, role)
    
    def data(self, index: QModelIndex, role: int) -> Any:
        return super().data(index, role)

    pass
