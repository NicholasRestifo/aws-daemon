from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from ui.console_widget import ConsoleWidget
from ui.services_widget import ServicesWidget
from ui.session_widget import SessionWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AWS Daemon")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(SessionWidget("ui/session_form.ui", central_widget))
        vertical_layout.addWidget(ServicesWidget("ui/services_form.ui", central_widget))
        vertical_layout.addWidget(ConsoleWidget("ui/console_form.ui", central_widget))

        central_widget.setLayout(vertical_layout)