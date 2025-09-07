from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

UI_FILE_PATH = "ui/services/iam_form.ui"


class IamWidget(QWidget):
    def __init__(self, console):
        super().__init__()
        uic.loadUi(UI_FILE_PATH, self)
        self.console = console