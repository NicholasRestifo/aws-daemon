from PyQt6 import uic
from PyQt6.QtWidgets import QWidget


class UiFileWidget(QWidget):
    def __init__(self, ui_path, parent=None):
        super().__init__(parent)
        uic.loadUi(ui_path, self)