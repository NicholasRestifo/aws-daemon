from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from model.session_info import SessionInfo

UI_FILE_PATH = "ui/session/session_form.ui"


class SessionWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        uic.loadUi(UI_FILE_PATH, self)
        self.model = SessionInfo()
