import logging
import os
from backend.config.configs import LOG_PATH, DEBUG

# 🔥 Création du dossier logs/ s'il n'existe pas
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

# 🔥 Niveau du logger en fonction de DEBUG (True = DEBUG, False = INFO)
top_level = logging.DEBUG if DEBUG else logging.INFO

# 🔥 Création de l'instance du logger
logger = logging.getLogger("ToDoLogger")
logger.setLevel(top_level)

# 🔥 Handler pour le fichier général (app.log)
file_handler = logging.FileHandler(os.path.join(LOG_PATH, "app.log"))
file_handler.setLevel(top_level)

# 🔥 Handler pour les erreurs (errors.log) - Ne capture que les erreurs
error_handler = logging.FileHandler(os.path.join(LOG_PATH, "errors.log"))
error_handler.setLevel(logging.ERROR)

# 🔥 Format des logs
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# 🔥 Appliquer le format aux handlers
file_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)

# 🔥 Ajouter les handlers au logger
logger.addHandler(file_handler)
logger.addHandler(error_handler)
