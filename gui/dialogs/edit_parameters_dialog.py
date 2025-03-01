from PyQt6.QtWidgets import (
    QDialog,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QFormLayout,
    QLineEdit,
    QHBoxLayout,
)
from gui.selectors import CategorySelector, ThemeSelector
from backend.config import EDIT_PARAMETERS_DIALOG_GEOMETRY, EDIT_PARAMETERS_DIALOG_TITLE
from backend.constants import CATEGORIES


class EditParametersDialog(QDialog):
    """Fenêtre d'édition des paramètres"""

    def __init__(self, parent: QWidget) -> None:
        """
        Layouts de la fenêtre de paramètres

         Parameters
         ----------
         parent : QWidget
             De quelle fenêtre dépend la boite de dialogue

        """

        super().__init__(parent)
        self.setWindowTitle(EDIT_PARAMETERS_DIALOG_TITLE)
        self.setGeometry(*EDIT_PARAMETERS_DIALOG_GEOMETRY)

        # Layout principal vertical
        main_layout = QVBoxLayout(self)

        # Layout pour aligner les éléments
        form_layout = QFormLayout(self)

        # Instanciation des sélécteurs

        self.category_selector = CategorySelector()
        self.theme_selector = ThemeSelector()

        add_category_layout = QHBoxLayout(self)  # Layout pour add_category()
        self.add_category_input = QLineEdit(self)
        self.add_category_input.setPlaceholderText("Category name ...")

        self.add_category_button = QPushButton("➕ Add", self)
        self.add_category_button.clicked.connect(self.add_category)

        add_category_layout.addWidget(self.add_category_input)
        add_category_layout.addWidget(self.add_category_button)

        remove_category_layout = QHBoxLayout()  # Layout pour remove_category()
        self.remove_category_button = QPushButton("❌ Remove", self)
        self.remove_category_button.clicked.connect(self.remove_category)

        remove_category_layout.addWidget(self.category_selector)
        remove_category_layout.addWidget(self.remove_category_button)

        # Affichage par ligne

        form_layout.addRow("Add new category: ", add_category_layout)

        form_layout.addRow("Categories: ", remove_category_layout)

        form_layout.addRow("Theme: ", self.theme_selector)

        # Ajout des lignes au layout principal

        main_layout.addLayout(form_layout)

        self.ok_button = QPushButton("Apply", self)
        self.ok_button.clicked.connect(self.accept)
        main_layout.addWidget(self.ok_button)

        self.setLayout(main_layout)

    def add_category(self) -> None:
        """Ajoute une catégorie et met à jour le sélecteur."""

        category_name = self.add_category_input.text().strip()

        if category_name and category_name not in CATEGORIES:
            CATEGORIES.append(category_name)  # Ajout dans les constantes
            self.category_selector.addItem(category_name)  # Mise à jour UI
            self.add_category_input.clear()  # Réinitialise le champ après ajout

    def remove_category(self) -> None:
        """Supprime une catégorie."""

        category_name = self.category_selector.currentText()

        if category_name in CATEGORIES:
            index = CATEGORIES.index(category_name)
            del CATEGORIES[index]
