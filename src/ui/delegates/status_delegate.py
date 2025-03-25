from typing import Any

from src.core.logger import logger
from PyQt6.QtCore import QEvent, QModelIndex, Qt
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem


class StatusEditDelegate(QStyledItemDelegate):
    """Délégué pour gérer le clic sur la colonne 'Status' sans passer par un éditeur."""

    def editorEvent(
        self,
        event: QEvent,
        model: Any,
        option: QStyleOptionViewItem,
        index: QModelIndex,
    ) -> bool:
        """Déclenche setData() sur clic gauche."""
        if event.type() == QEvent.Type.MouseButtonRelease and isinstance(
            event, QMouseEvent
        ):
            logger.debug("Click detected")
            model.setData(index, None, Qt.ItemDataRole.EditRole)
        return True
