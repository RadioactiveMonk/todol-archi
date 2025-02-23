from PyQt6.QtCore import Qt, QAbstractTableModel
from typing import List, Dict, Any, Optional, Union


class TaskTableModel(QAbstractTableModel):
    """Modèle de données pour afficher les tâches dans un QTableView"""

    HEADERS = [
        "Status",
        "Priority",
        "Category",
        "Expiration",
        "Title",
        "Notes",
    ]  # Titres des sections

    def __init__(self, tasks: Optional[List[Dict[str, Any]]] = None) -> None:
        """
        Initialise une liste de tâches sous forme de dict ou une liste vide si aucune tâche

        Parameters
        ----------
        self, tasks : List
            Une liste de tâches
        """

        super().__init__()
        self.tasks: List[Dict[str, Any]] = tasks or []  # Les tâches ou une liste vide

    def rowCount(self, parent=None) -> int:
        """
        Retourne le nombre de lignes.
        """
        return len(self.tasks)

    def columnCount(self, parent=None) -> int:
        """
        Retourne le nombre de colonnes (sections)
        """
        return len(self.HEADERS)

    def data(self, index: int, role: Qt.ItemDataRole) -> Optional[str]:
        """
        Retourne la donnée à afficher selon l'index et le rôle.

        Parameters
        ----------
        index : int
            Index de la tâche
        role : Qt.ItemDataRole
            Le rôle de l'objet (un status, une date ...)


        Returns
        -------
        role OR None: bool
            Si le role est précisé -> Role, sinon -> None
        """

        if not index.isValid():
            return None
        
