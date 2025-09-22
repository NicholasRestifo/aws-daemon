from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtGui import QKeyEvent


class CommonSignals(QObject):
    key_press_signal = pyqtSignal(QKeyEvent)
    key_release_signal = pyqtSignal(QKeyEvent)

    def key_press_event(self, event: QKeyEvent):
        # if event.key() == Qt.Key.Key_Return:
        #     return
        self.key_press_signal.emit(event)

    def key_release_event(self, event: QKeyEvent):
        # if event.key() == Qt.Key.Key_Return:
        #     self.return_pressed()
        #     return
        self.key_release_signal.emit(event)