from model.console_model import ConsoleModel
from ui.ui_file_widget import UiFileWidget


class ConsoleWidget(UiFileWidget):
    def __init__(self, ui_path, parent=None):
        super().__init__(ui_path, parent)
        self.model = ConsoleModel()
        self.console_in_widget.model = self.model
        self.model.subscribe_out_text(lambda out_text: self.write(out_text)) # can just pass self.write?

    def write(self, text):
        self.console_out_widget.append(text)
        self.scroll_to_bottom()

    def scroll_to_bottom(self):
        (self.console_out_widget.verticalScrollBar()
        .setValue(
            self.console_out_widget.verticalScrollBar().maximum()))
