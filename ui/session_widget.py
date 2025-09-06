from model.session_model import SessionModel
from ui.ui_file_widget import UiFileWidget


class SessionWidget(UiFileWidget):
    def __init__(self, ui_path, parent=None):
        super().__init__(ui_path, parent)
        self.model = SessionModel()
