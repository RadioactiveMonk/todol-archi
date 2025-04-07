from dataclasses import asdict, dataclass
from typing import Any, Dict, Optional


@dataclass
class TaskCore:
    """Représente une tâche de l'application."""

    id: Optional[int] = None
    title: str = ""
    category: str = ""
    completed: bool = False
    expiration: str = "2025-08-08 00:00"
    notes: str = ""

    @classmethod
    def from_dict(cls, data: dict) -> "TaskCore":
        """
        Convert a task in dict format to a class instance 'TaskCore'

        Parameters
        ----------
        data : dict
            task datas (id, title, ...)

        Returns
        -------
        TaskCore
            an instance of the class TaskCore from 'data'
        """
        return cls(**data)
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the class instance to a dictionnary

        Returns
        -------
        Dict[str, Any]
            the task in a dict format
        """
        return asdict(self)

