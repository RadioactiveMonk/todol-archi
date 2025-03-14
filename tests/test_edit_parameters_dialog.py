import pytest
import json
from PyQt6.QtWidgets import QApplication
from gui.dialogs.edit_parameters_dialog import EditParametersDialog
from backend.settings_manager import SettingsManager, SETTINGS_FILE


@pytest.fixture(scope="session", autouse=True)
def app():
    pass
