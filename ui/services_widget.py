from model.services_model import ServicesModel
from ui.ui_file_widget import UiFileWidget


class ServicesWidget(UiFileWidget):
    def __init__(self, ui_path, parent=None):
        super().__init__(ui_path, parent)
        self.model = ServicesModel()