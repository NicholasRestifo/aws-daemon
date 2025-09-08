from PyQt6.QtWidgets import QWidget


class ServicesWidget(QWidget):
    def __init__(self):
        super().__init__()

    @property
    def name(self):
        return "unnamed services"