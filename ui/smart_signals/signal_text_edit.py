from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import QTextEdit

from ui.smart_signals.common_signals import CommonSignals


class SignalTextEdit(QTextEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.common_signals = CommonSignals(self)

    def keyPressEvent(self, event: QKeyEvent):
        super().keyPressEvent(event)
        self.common_signals.key_press_event(event)

    def keyReleaseEvent(self, event: QKeyEvent):
        super().keyReleaseEvent(event)
        self.common_signals.key_release_event(event)
