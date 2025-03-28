from typing import Any

from PyQt6.QtCore import QEvent, QModelIndex, Qt
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem

from core.logger import logger


class StatusEditDelegate(QStyledItemDelegate):
    """Délégué pour gérer le clic sur la colonne 'Status' sans passer par un éditeur."""

    def editorEvent(
        self,
        event: QEvent | None,
        model: Any,
        option: QStyleOptionViewItem,
        index: QModelIndex,
    ) -> bool:
        """Déclenche setData() sur clic gauche."""
        if (
            event is not None
            and event.type() == QEvent.Type.MouseButtonRelease
            and isinstance(event, QMouseEvent)
        ):
            logger.debug("Click detected")
            model.setData(index, None, Qt.ItemDataRole.EditRole)
        return True
