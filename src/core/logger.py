import logging
from pathlib import Path
from configuration.constants import LOG_PATH
from core.config import DEBUG

# Création du dossier logs/ s'il n'existe pas
log_path = Path(LOG_PATH)
log_path.mkdir(parents=True, exist_ok=True)
log_file = Path(LOG_PATH) / "app.log"
log_file.touch(exist_ok=True)
errors_file = Path(LOG_PATH) / "errors.log"
errors_file.touch(exist_ok=True)

# Niveau du logger en fonction de DEBUG (True = DEBUG, False = INFO)
top_level = logging.DEBUG if DEBUG else logging.INFO

# Création de l'instance du logger
logger = logging.getLogger("ToDoLogger")
logger.setLevel(top_level)

# Handler pour le fichier général (app.log)
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(top_level)

# Handler pour les erreurs (errors.log) - Ne capture que les erreurs
error_handler = logging.FileHandler(errors_file)
error_handler.setLevel(logging.ERROR)

# Format des logs
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Appliquer le format aux handlers
file_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)

# Ajouter les handlers au logger
logger.addHandler(file_handler)
logger.addHandler(error_handler)
