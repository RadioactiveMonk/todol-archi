import sys
from rich.traceback import install
from PyQt6.QtWidgets import QApplication
from gui.main_window import MainWindow
from backend.core.style_loader import load_stylesheet


def main():
    """Application entry point"""

    app = QApplication(sys.argv)  # Convention: initialisation de QApplication
    load_stylesheet(app)
    window = MainWindow()  # Récupération de la fenêtre principale
    window.show()  # A la manière de 'plot', la fenêtre est crée mais doit être affichée

    sys.exit(app.exec())  # Convention: boucle principale de l'application


if __name__ == "__main__":
    install()  # Active les tracebacks améliorés avec rich
    main()
