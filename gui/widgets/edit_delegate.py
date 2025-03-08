from PyQt6.QtWidgets import QStyledItemDelegate
from PyQt6.QtCore import QRect, pyqtSignal, QEvent
from PyQt6.QtGui import QIcon, QPainter, QMouseEvent
from backend.config.constants import (
    EDIT_ICON_SIZE,
    EDIT_ICON_SPACING,
    EDIT_ICON_TOP_OFFSET,
    EDIT_SECTION_POSITIONS,
)


class EditDelegate(QStyledItemDelegate):
    """Délégué pour afficher et gérer les icônes dans la colonne 'edit'"""

    checkClicked = pyqtSignal(int)
    editClicked = pyqtSignal(int)
    deleteClicked = pyqtSignal(int)

    def __init__(self, parent=None):
        """Initialise les icônes"""
        super().__init__(parent)
        self.icons = {
            "check": QIcon("resources/icons/check_task.png"),
            "edit": QIcon("resources/icons/edit_task.png"),
            "delete": QIcon("resources/icons/delete_task.png"),
        }

    def paint(self, painter: QPainter, option, index):
        """Affiche les icônes dans la colonne 'edit'"""

        for i, icon_name in enumerate(EDIT_SECTION_POSITIONS):
            x_offset = (
                option.rect.left()
                + EDIT_ICON_SPACING
                + (EDIT_ICON_SIZE + EDIT_ICON_SPACING) * i
            )
            icon_rect = QRect(
                x_offset,
                option.rect.top() + EDIT_ICON_TOP_OFFSET,
                EDIT_ICON_SIZE,
                EDIT_ICON_SIZE,
            )

            self.icons[icon_name].paint(painter, icon_rect)

    def editorEvent(self, event, model, option, index):
        """Gère le clic sur les icônes"""

        if not isinstance(event, QMouseEvent):
            return False  # ✅ Ignore les événements non liés à la souris

        if event.type() == QEvent.Type.MouseButtonRelease:
            mouse_pos = event.position().toPoint()  # ✅ Utilisation correcte en PyQt6
            signals = [self.deleteClicked, self.editClicked, self.checkClicked]

            for i, signal in enumerate(signals):
                x_offset = option.rect.left() + EDIT_ICON_SPACING + (EDIT_ICON_SIZE + EDIT_ICON_SPACING) * i
                icon_rect = QRect(x_offset, option.rect.top() + EDIT_ICON_TOP_OFFSET, EDIT_ICON_SIZE, EDIT_ICON_SIZE)

                if icon_rect.contains(mouse_pos):
                    signal.emit(index.row())
                    return True  # ✅ Stoppe dès qu'un clic est détecté

        return super().editorEvent(event, model, option, index)

