from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeyEvent, QTextCursor
from PyQt6.QtWidgets import QWidget

from ui import widget_util

UI_FILE_PATH = "ui//console/console_form.ui"


class ConsoleWidget(QWidget):
    def __init__(self, console, parent):
        super().__init__(parent)
        uic.loadUi(UI_FILE_PATH, self)
        self.console = console
        self.console.out_text_emitter.connect(self.write)
        widget_util.bind_height_to_document(self.console_in_widget)
        self.console_in_widget.common_signals.key_press_signal.connect(self.input_enter_press_event)
        self.console_in_widget.common_signals.key_press_signal.connect(self.input_enter_release_event)

    def write(self, text):
        if len(text) == 0:
            return

        self.console_out_widget.append(text)
        self.scroll_to_bottom()

    def scroll_to_bottom(self):
        (self.console_out_widget.verticalScrollBar()
        .setValue(
            self.console_out_widget.verticalScrollBar().maximum()))

    def input_enter_press_event(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Return:
            self.console_in_widget.textCursor().deletePreviousChar()

    def input_enter_release_event(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Return:
            self.process_input()

    def process_input(self):
        input_text = self.console_in_widget.toPlainText().strip()
        self.console_in_widget.clear()
        self.console.handle_console_input(input_text)
