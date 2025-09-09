from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

UI_FILE_PATH = "ui/session/session_form.ui"


class SessionWidget(QWidget):
    def __init__(self, session_info, parent):
        super().__init__(parent)
        uic.loadUi(UI_FILE_PATH, self)

        self.user_input.setCurrentText(session_info.user_name.value)
        self.user_input.currentTextChanged.connect(session_info.user_name.set_value)

        self.region_input.setCurrentText(session_info.region.value)
        self.region_input.currentTextChanged.connect(session_info.region.set_value)

        self.auth_token_label.setText(session_info.auth_token.value)
        session_info.auth_token.changed.connect(self.update_auth_token)

    def update_auth_token(self, auth_token):
        self.auth_token_label.setText(auth_token)
