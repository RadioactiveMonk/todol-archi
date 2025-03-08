from PyQt6.QtWidgets import QStyledItemDelegate
from PyQt6.QtCore import QRect, pyqtSignal, QEvent
from PyQt6.QtGui import QIcon, QPainter, QMouseEvent


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

        icon_size = option.rect.height() - 4
        spacing = 6
        positions = ["check", "edit", "delete"]

        for i, icon_name in enumerate(positions):
            x_offset = option.rect.left() + spacing + (icon_size + spacing) * i
            icon_rect = QRect(x_offset, option.rect.top() + 2, icon_size, icon_size)
            self.icons[icon_name].paint(painter, icon_rect)

    from PyQt6.QtGui import QMouseEvent


    def editorEvent(self, event, model, option, index):
        """Gère le clic sur les icônes"""

        if not isinstance(event, QMouseEvent):
            return False  # ✅ Évite les erreurs si ce n'est pas un événement souris

        if event.type() == QEvent.Type.MouseButtonRelease:
            mouse_pos = event.position().toPoint()  # ✅ Utilisation correcte en PyQt6
            icon_size = option.rect.height() - 4
            spacing = 6
            positions = ["check", "edit", "delete"]
            signals = [self.checkClicked, self.editClicked, self.deleteClicked]

            for i, signal in enumerate(signals):
                x_offset = option.rect.left() + spacing + (icon_size + spacing) * i
                icon_rect = QRect(x_offset, option.rect.top() + 2, icon_size, icon_size)

                if icon_rect.contains(mouse_pos):
                    signal.emit(index.row())
                    return True  # ✅ Stoppe dès qu'un clic est détecté

        return super().editorEvent(event, model, option, index)
