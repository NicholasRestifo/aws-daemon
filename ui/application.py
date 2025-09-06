import sys

from PyQt6.QtWidgets import QApplication

from ui.main_window import MainWindow


def run():
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.resize(800, 600)
    main_window.show()

    return app.exec()
