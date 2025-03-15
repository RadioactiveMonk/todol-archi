def test_load_settings(settings_manager, clean_settings):
    """Test si les paramètres sont bien chargés"""
    settings = settings_manager.get_all()
    assert settings["theme"] == "dark"
    assert settings["categories"] == ["Work", "Personal"]


def test_update_theme(settings_manager):
    """Test si le thème est bien mis à jour"""
    settings_manager.update("theme", "system")
    assert settings_manager.get("theme") == "system"


def test_update_categories(settings_manager):
    """Test si les catégories sont bien mises à jour"""
    settings_manager.update("categories", ["Work", "Pets"])
    assert settings_manager.get("categories") == ["Work", "Pets"]


def test_invalid_key(settings_manager):
    """Vérifie que mettre à jour une clé invalide ne casse pas le code"""
    settings_manager.update("clock", "time")
    assert settings_manager.get("clock") is None
