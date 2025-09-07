from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

UI_FILE_PATH = "ui//console/console_form.ui"


class ConsoleWidget(QWidget):
    def __init__(self, console, parent):
        super().__init__(parent)
        uic.loadUi(UI_FILE_PATH, self)
        self.model = console
        self.console_in_widget.model = self.model
        self.model.subscribe_out_text(lambda out_text: self.write(out_text)) # can just pass self.write?

    def write(self, text):
        if len(text) == 0:
            return

        self.console_out_widget.append(text)
        self.scroll_to_bottom()

    def scroll_to_bottom(self):
        (self.console_out_widget.verticalScrollBar()
        .setValue(
            self.console_out_widget.verticalScrollBar().maximum()))
