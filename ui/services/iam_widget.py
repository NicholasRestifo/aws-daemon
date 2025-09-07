from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

UI_FILE_PATH = "ui/services/iam_form.ui"


class IamWidget(QWidget):
    def __init__(self, console):
        super().__init__()
        uic.loadUi(UI_FILE_PATH, self)
        self.console = console
        self.button_1.clicked.connect(self.button_1_clicked)
        self.button_2.clicked.connect(self.button_2_clicked)
        self.button_3.clicked.connect(self.button_3_clicked)

    def button_1_clicked(self):
        self.console.handle_console_input("dir")

    def button_2_clicked(self):
        self.console.handle_console_input("ls")

    def button_3_clicked(self):
        self.console.handle_console_input("where")