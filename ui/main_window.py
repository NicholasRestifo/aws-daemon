from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from ui.console.console_widget import ConsoleWidget
from ui.services.service_tab_widget import ServiceTabWidget
from ui.session.session_widget import SessionWidget


class MainWindow(QMainWindow):
    def __init__(self, aws):
        super().__init__()
        self.setWindowTitle("AWS Daemon")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(SessionWidget(aws.session_info, central_widget))
        vertical_layout.addWidget(ServiceTabWidget(aws, central_widget))
        vertical_layout.addWidget(ConsoleWidget(aws.console, central_widget))
        central_widget.setLayout(vertical_layout)