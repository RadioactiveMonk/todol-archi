from PyQt6.QtWidgets import QStyledItemDelegate, QStyleOptionButton, QApplication
from PyQt6.QtCore import QRect, pyqtSignal, QEvent
from PyQt6.QtGui import QIcon, QPainter


class EditDelegate(QStyledItemDelegate):
    """Délégué pour afficher et gérer les icônes interactives dans la colonne Edit."""

    editClicked = pyqtSignal(int)
    deleteClicked = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.icons = {
            "edit": QIcon("resources/icons/edit_task.png"),
            "delete": QIcon("resources/icons/delete_task.png"),
        }

    def paint(self, painter: QPainter, option, index):
        """Affiche les icônes dans la cellule Edit."""
        icon_size = option.rect.height() - 4
        spacing = 6
        edit_rect = QRect(
            option.rect.left() + spacing, option.rect.top() + 2, icon_size, icon_size
        )
        delete_rect = QRect(
            option.rect.left() + icon_size + spacing * 2,
            option.rect.top() + 2,
            icon_size,
            icon_size,
        )

        self.icons["edit"].paint(painter, edit_rect)
        self.icons["delete"].paint(painter, delete_rect)

    def editorEvent(self, event, model, option, index):
        """Gère le clic sur les icônes."""
        if event.type() == QEvent.Type.MouseButtonRelease:
            mouse_pos = event.pos()
            icon_size = option.rect.height() - 4
            spacing = 6
            edit_rect = QRect(
                option.rect.left() + spacing,
                option.rect.top() + 2,
                icon_size,
                icon_size,
            )
            delete_rect = QRect(
                option.rect.left() + icon_size + spacing * 2,
                option.rect.top() + 2,
                icon_size,
                icon_size,
            )

            if edit_rect.contains(mouse_pos):
                self.editClicked.emit(index.row())
            elif delete_rect.contains(mouse_pos):
                self.deleteClicked.emit(index.row())

        return super().editorEvent(event, model, option, index)
