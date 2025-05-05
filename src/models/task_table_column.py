from dataclasses import dataclass
from typing import Optional

from PySide6.QtCore import Qt


@dataclass(frozen=True)
class TaskTableColumn:
    """Representation of task table columns"""

    name: str
    field: str
    width: int = 150
    editable: bool = True
    alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignLeft
    flags: Optional[Qt.ItemFlag] = None
    visible: bool = True
    tooltip: Optional[str] = None
    delegate: Optional[type] = None
