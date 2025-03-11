import logging
import os
from backend.config.configs import LOG_PATH


# Création du dossier si inexistant
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

# Config du logger
logging.basicConfig(
    filename=os.path.join(LOG_PATH, "app.log"),
    level=logging.DEBUG,  # Log tout: DEBUG, INFO, WARNING...
    format="%(asctime)s - %(levelname)s - %(message)s",  # format des logs
)

logger = logging.getLogger("ToDoLogger")  # Instance
