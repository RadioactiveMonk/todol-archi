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

    editClicked = pyqtSignal(int)
    deleteClicked = pyqtSignal(int)

    def __init__(self, parent=None):
        """Initialise les icônes"""
        super().__init__(parent)
        self.icons = {
            "edit": QIcon("resources/icons/edit_task.png"),
            "delete": QIcon("resources/icons/delete_task.png"),
        }

    def paint(self, painter: QPainter, option, index):
        """Affiche les icônes dans la colonne 'edit'"""

        cell_center_x = option.rect.center().x()  # ✅ Centre de la cellule
        total_width = (EDIT_ICON_SIZE + EDIT_ICON_SPACING) * len(
            self.icons
        ) - EDIT_ICON_SPACING
        start_x = cell_center_x - (total_width // 2)  # ✅ Alignement centré

        for i, icon_name in enumerate(EDIT_SECTION_POSITIONS):
            x_offset = start_x + (EDIT_ICON_SIZE + EDIT_ICON_SPACING) * i

            icon_rect = QRect(
                x_offset,
                option.rect.center().y()
                - (EDIT_ICON_SIZE // 2),  # ✅ Centre verticalement
                EDIT_ICON_SIZE,
                EDIT_ICON_SIZE,
            )
            self.icons[icon_name].paint(painter, icon_rect)

    def editorEvent(self, event, model, option, index):
        """Gère les clics sur les icônes d'édition."""

        SIGNAL_MAPPING = {
            "edit": "editClicked",
            "delete": "deleteClicked",
        }

        if (
            not isinstance(event, QMouseEvent)
            or event.type() != QEvent.Type.MouseButtonRelease
        ):
            return False  # ✅ On s'assure que c'est bien un clic souris

        mouse_pos = (
            event.position().toPoint()
        )  # ✅ PyQt6 utilise `.position()` à convertir en QPoint
        cell_center_x = option.rect.center().x()
        total_width = (EDIT_ICON_SIZE + EDIT_ICON_SPACING) * len(
            self.icons
        ) - EDIT_ICON_SPACING
        start_x = cell_center_x - (total_width // 2)  # ✅ Départ aligné au centre

        for i, icon_name in enumerate(EDIT_SECTION_POSITIONS):
            x_offset = start_x + (EDIT_ICON_SIZE + EDIT_ICON_SPACING) * i
            icon_rect = QRect(
                x_offset,
                option.rect.center().y() - (EDIT_ICON_SIZE // 2),
                EDIT_ICON_SIZE,
                EDIT_ICON_SIZE,
            )

            if icon_rect.contains(
                mouse_pos
            ):  # ✅ Vérifie si la souris est dans l'icône
                getattr(self, SIGNAL_MAPPING[icon_name]).emit(
                    index.row()
                )  # ✅ Récupère le bon signal dynamiquement
                return True

        return super().editorEvent(event, model, option, index)
