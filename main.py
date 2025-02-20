# Importing packages and modules
import sys
from PyQt6.QtWidgets import QApplication
from gui.main_window import MainWindow


def main():
    """Point d'entrée principal de l'application"""

    app = QApplication(sys.argv)  # Convention: initialisation de QApplication
    window = MainWindow()  # Récupération de la fenêtre principale
    window.show()  # A la manière de 'plot', la fenêtre est crée mais doit être affichée

    sys.exit(app.exec())  # Convention: boucle principale de l'application

if __name__ == "__main__":
    main()