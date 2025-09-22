import sys

from PyQt6.QtWidgets import QApplication

from model.aws import Aws
from model.console import Console
from model.session_info import SessionInfo
from ui.main_window import MainWindow


def run():
    app = QApplication(sys.argv)

    aws = Aws(Console(), SessionInfo())
    main_window = MainWindow(aws)
    main_window.resize(800, 600)
    main_window.show()

    return app.exec()
