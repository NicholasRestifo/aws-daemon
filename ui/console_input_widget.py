from PyQt6.QtCore import Qt, QSizeF
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import QTextEdit


class ConsoleInputWidget(QTextEdit):
    # TODO some kind of widget subclass with a key press/release signal...
    def __init__(self, parent=...):
        super().__init__(parent)
        self.model = None
        self.document().documentLayout().documentSizeChanged.connect(self.adjust_height)

    def adjust_height(self, size: QSizeF):
        # Adding a small margin to prevent scrollbars appearing prematurely
        self.setMaximumHeight(int(size.height()) + int(self.document().documentMargin() * 2))

    def keyReleaseEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Return:
            self.return_pressed()

        super().keyPressEvent(event)

    def return_pressed(self):
        input_text = self.toPlainText().strip()
        self.clear()
        self.model.handle_console_input(input_text)