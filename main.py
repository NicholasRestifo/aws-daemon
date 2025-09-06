import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QLabel, QPushButton, QListWidget
)
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide Quick Start")

        # ---- central widget & layout
        central = QWidget(self)
        layout = QVBoxLayout()
        central.setLayout(layout)
        self.setCentralWidget(central)

        # ---- UI elements
        self.label = QLabel("Hello, world!")
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.button = QPushButton("Add item")
        self.list_widget = QListWidget()

        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(self.list_widget)

        # simple counter so items are unique
        self._count = 0

        # ---- connect signals
        self.button.clicked.connect(self.add_item)

    def add_item(self):
        self._count += 1
        self.list_widget.addItem(f"Item {self._count}")


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.resize(360, 420)   # optional: give it a comfortable default size
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()