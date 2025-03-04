# Importing packages and modules
import atexit
import sys
from rich.traceback import install
from PyQt6.QtWidgets import QApplication
from gui.main_window import MainWindow
from backend.database import DatabaseManager


def main():
    """Point d'entrée principal de l'application"""

    app = QApplication(sys.argv)  # Convention: initialisation de QApplication
    window = MainWindow()  # Récupération de la fenêtre principale
    window.show()  # A la manière de 'plot', la fenêtre est crée mais doit être affichée
    db = DatabaseManager()
    atexit.register(db.close_connection)

    sys.exit(app.exec())  # Convention: boucle principale de l'application


if __name__ == "__main__":
    install()  # Active les tracebacks améliorés avec rich
    main()

    
