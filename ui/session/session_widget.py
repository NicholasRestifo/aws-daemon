from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

UI_FILE_PATH = "ui/session/session_form.ui"


class SessionWidget(QWidget):
    def __init__(self, session_info, parent):
        super().__init__(parent)
        uic.loadUi(UI_FILE_PATH, self)

        self.region.setCurrentText(session_info.region.value)
        self.region.currentTextChanged.connect(session_info.region.set_value)

        self.output.setCurrentText(session_info.output.value)
        self.output.currentTextChanged.connect(session_info.output.set_value)
