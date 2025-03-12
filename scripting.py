import os

# ✅ Définition du dossier principal du projet
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ✅ Répertoire de configuration
CONFIG_DIR = os.path.join(BASE_DIR, "backend", "config")

# ✅ Chemin des fichiers spécifiques
SETTINGS_PATH = os.path.join(CONFIG_DIR, "settings.json")
STYLESHEET_PATH = os.path.join(BASE_DIR, "resources", "stylesheets")

# ✅ Paramètres dynamiques
DEBUG = True  # Peut être chargé dynamiquement plus tard

# ✅ Fichiers spécifiques aux styles
DEFAULT_THEME = "default"  # Thème par défaut si settings.json est absent
DARK_THEME = "dark"  # Option de thème sombre
