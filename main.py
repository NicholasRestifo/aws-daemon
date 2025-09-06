import sys

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout
)

from services.services_widget import ServicesWidget
from session.session_widget import SessionWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AWS Daemon")

        session_widget = SessionWidget()
        services_widget = ServicesWidget()

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(session_widget)
        vertical_layout.addWidget(services_widget)

        self.setLayout(vertical_layout)


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.resize(360, 420)   # optional: give it a comfortable default size
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()