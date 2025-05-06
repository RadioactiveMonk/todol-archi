from PySide6.QtCore import QAbstractItemModel, QEvent, QModelIndex, QRect, Signal
from PySide6.QtGui import QIcon, QMouseEvent, QPainter
from PySide6.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem, QWidget

from ui.constants.geometry import (
    EDIT_ICON_SIZE,
    EDIT_ICON_SPACING,
    EDIT_SECTION_POSITIONS,
)
from utils.path_utils import ICONS_DIR


class EditDelegate(QStyledItemDelegate):
    """
    Délégué personnalisé pour la colonne 'Edit'.
    Affiche des icônes (ex: edit, delete) et gère les clics dessus.
    """

    editClicked = Signal(int)  # row index
    deleteClicked = Signal(int)  # row index

    def __init__(self, parent: QWidget | None = None):
        """Initialise les icônes"""
        super().__init__(parent)
        self.icons = {
            "edit": QIcon(str(ICONS_DIR / "edit_task.png")),
            "delete": QIcon(str(ICONS_DIR / "delete_task.png")),
        }

        self.signal_map = {"edit": self.editClicked, "delete": self.deleteClicked}

    def paint(
        self, painter: QPainter | None, option: QStyleOptionViewItem, index: QModelIndex
    ):
        """Affiche les icônes centrées dans la cellule."""

        cell_center_x = option.rect.center().x()  # Centre de la cellule
        total_width = (EDIT_ICON_SIZE + EDIT_ICON_SPACING) * len(
            EDIT_SECTION_POSITIONS
        ) - EDIT_ICON_SPACING
        start_x = cell_center_x - (total_width // 2)  # Alignement centré

        for i, icon_name in enumerate(EDIT_SECTION_POSITIONS):
            x_offset = start_x + (EDIT_ICON_SIZE + EDIT_ICON_SPACING) * i
            icon_rect = QRect(
                x_offset,
                option.rect.center().y()
                - (EDIT_ICON_SIZE // 2),  # Centre verticalement
                EDIT_ICON_SIZE,
                EDIT_ICON_SIZE,
            )
            self.icons[icon_name].paint(painter, icon_rect)

    def editorEvent(
        self,
        event: QEvent | None,
        model: QAbstractItemModel | None,
        option: QStyleOptionViewItem,
        index: QModelIndex,
    ):
        """Gère les clics sur les icônes et émet le signal correspondant."""

        if (
            not isinstance(event, QMouseEvent)
            or event.type() != QEvent.Type.MouseButtonRelease
        ):
            return False  # On s'assure que c'est bien un clic souris

        mouse_pos = (
            event.position().toPoint()
        )  # PyQt6 utilise `.position()` à convertir en QPoint
        cell_center_x = option.rect.center().x()
        total_width = (EDIT_ICON_SIZE + EDIT_ICON_SPACING) * len(
            EDIT_SECTION_POSITIONS
        ) - EDIT_ICON_SPACING
        start_x = cell_center_x - (total_width // 2)  # Départ aligné au centre

        for i, icon_name in enumerate(EDIT_SECTION_POSITIONS):
            x_offset = start_x + (EDIT_ICON_SIZE + EDIT_ICON_SPACING) * i
            icon_rect = QRect(
                x_offset,
                option.rect.center().y() - (EDIT_ICON_SIZE // 2),
                EDIT_ICON_SIZE,
                EDIT_ICON_SIZE,
            )

            if icon_rect.contains(mouse_pos):  # Vérifie si la souris est dans l'icône
                self.signal_map[icon_name].emit(index.row())
                return True

        return super().editorEvent(event, model, option, index)
