from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from model.console import Console
from ui.console.console_widget import ConsoleWidget
from ui.services.services_widget import ServicesWidget
from ui.session_widget import SessionWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AWS Daemon")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        vertical_layout = QVBoxLayout()

        console = Console()

        vertical_layout.addWidget(SessionWidget(central_widget))
        vertical_layout.addWidget(ServicesWidget(console, central_widget))
        vertical_layout.addWidget(ConsoleWidget(console, central_widget))

        central_widget.setLayout(vertical_layout)