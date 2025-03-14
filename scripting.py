import pytest
import json
from pathlib import Path
from backend.settings_manager import SettingsManager, SETTINGS_FILE


@pytest.fixture
def settings_manager():
    """Fixture pour instancier un SettingsManager propre pour chaque test"""
    SETTINGS_FILE.write_text(
        json.dumps({"theme": "light", "categories": ["Work", "Personal"]})
    )
    return SettingsManager()


def test_load_settings(settings_manager):
    """Teste si les paramètres sont bien chargés"""
    settings = settings_manager.get_all()
    assert settings["theme"] == "light"
    assert settings["categories"] == ["Work", "Personal"]


def test_update_theme(settings_manager):
    """Teste si la mise à jour du thème fonctionne"""
    settings_manager.update("theme", "dark")
    assert settings_manager.get("theme") == "dark"


def test_update_categories(settings_manager):
    """Teste si les catégories sont bien mises à jour"""
    settings_manager.update("categories", ["New Category"])
    assert settings_manager.get("categories") == ["New Category"]


def test_invalid_key(settings_manager):
    """Vérifie que mettre à jour une clé invalide ne casse pas le code"""
    settings_manager.update("invalid_key", "value")
    assert (
        settings_manager.get("invalid_key") is None
    )  # Clé inconnue, donc pas d'ajout inattendu
