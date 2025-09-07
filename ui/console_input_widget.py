from PyQt6.QtCore import Qt, QEvent
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import QTextEdit


class ConsoleInputWidget(QTextEdit):
    def __init__(self, parent=...):
        super().__init__(parent)
        self.model = None

    def keyReleaseEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Return:
            self.return_pressed()

        super().keyPressEvent(event)

    def return_pressed(self):
        input_text = self.toPlainText()[:-1]
        self.clear()
        self.model.handle_console_input(input_text)