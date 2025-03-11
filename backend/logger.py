import logging
import os
from backend.config.configs import LOG_PATH
from backend.config.configs import DEBUG


# Création du dossier si inexistant
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

# Gestion du logger pour le DEBUG si DEBUG = TRUE (désactivé en production)
top_level = logging.DEBUG if DEBUG else logging.INFO

# Logger pour les erreurs
error_handler = logging.FileHandler(os.path.join(LOG_PATH, "errors.log"))
error_handler.setLevel(logging.ERROR)

# Config du logger
logging.basicConfig(
    filename=os.path.join(LOG_PATH, "app.log"),
    level=top_level,  # Log en fonction du mode DEBUG (true or false)
    format="%(asctime)s - %(levelname)s - %(message)s",  # format des logs
)

logger = logging.getLogger("ToDoLogger")  # Instance
logger.addHandler(error_handler)
