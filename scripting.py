import pytest
import json
from PyQt6.QtWidgets import QApplication
from backend.settings_manager import SettingsManager, SETTINGS_FILE
from gui.dialogs.edit_parameters_dialog import EditParametersDialog


# Initialiser une application Qt pour les tests
@pytest.fixture(scope="session", autouse=True)
def app():
    """Crée une instance de QApplication pour les tests PyQt6"""
    app = QApplication([])
    yield app
    app.quit()


@pytest.fixture
def settings_manager():
    """Fixture pour instancier un SettingsManager propre aux tests"""
    SETTINGS_FILE.write_text(
        json.dumps({"theme": "light", "categories": ["Work", "Home"]})
    )
    return SettingsManager()


@pytest.fixture
def edit_parameters_dialog(qtbot):
    """Fixture pour instancier la boîte de dialogue avec un qtbot"""
    dialog = EditParametersDialog()
    qtbot.addWidget(dialog)
    return dialog


def test_add_category(edit_parameters_dialog, settings_manager, qtbot):
    """Teste l'ajout d'une catégorie via CategorySelector"""
    edit_parameters_dialog.add_category_input.setText("Fitness")
    qtbot.mouseClick(edit_parameters_dialog.add_category_button, 1)  # Simule un clic

    assert "Fitness" in settings_manager.get(
        "categories"
    )  # Vérifie que c'est bien enregistré
    assert (
        edit_parameters_dialog.category_selector.findText("Fitness") != -1
    )  # Vérifie que l'UI est mise à jour


def test_remove_category(edit_parameters_dialog, settings_manager, qtbot):
    """Teste la suppression d'une catégorie via CategorySelector"""
    edit_parameters_dialog.category_selector.setCurrentText("Work")
    qtbot.mouseClick(edit_parameters_dialog.remove_category_button, 1)  # Simule un clic

    assert "Work" not in settings_manager.get("categories")  # Vérifie que c'
