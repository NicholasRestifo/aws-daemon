import sys

from PyQt6.QtWidgets import QApplication

from model.session_info import SessionInfo
from ui.main_window import MainWindow


def run():
    app = QApplication(sys.argv)

    main_window = MainWindow(SessionInfo())
    main_window.resize(800, 600)
    main_window.show()

    return app.exec()
