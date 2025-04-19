from dataclasses import dataclass

from utils.log_utils import logger


@dataclass(frozen=True)
class TaskTableColumn:
    """Manages the comportment of columns"""

    name: str
    field: str
    width: int = 150
    editable: bool = False
    

