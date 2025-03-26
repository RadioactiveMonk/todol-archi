import sys

from PyQt6.QtWidgets import QApplication
from rich.traceback import install

from factory.mainwindow_factory import MainWindowFactory


def main():
    """Application entry point"""

    app = QApplication(sys.argv)
    main_window = MainWindowFactory.create()
    main_window.show()

    sys.exit(app.exec())  # Convention: boucle principale de l'application


if __name__ == "__main__":
    install()  # Active les tracebacks améliorés avec rich
    main()
