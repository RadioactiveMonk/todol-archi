from backend.style_loader import load_stylesheet


def accept(self) -> None:
    """Applique immédiatement les paramètres et ferme la boîte de dialogue."""
    new_theme = self.theme_selector.currentText()  # 🔥 Récupère le thème sélectionné
    SettingsManager.update_settings("theme", new_theme)  # 🔥 Sauvegarde

    # 🔥 Applique immédiatement le thème
    load_stylesheet(self.parent())

    # 🔥 Notifie que les settings ont changé
    self.settings_updated.emit(SettingsManager.load_settings())

    self.close()
