from PyQt6 import uic

from ui.services.services_widget import ServicesWidget

UI_FILE_PATH = "ui/services/iam_form.ui"


class IamWidget(ServicesWidget):
    def __init__(self, iam_services):
        super().__init__()
        uic.loadUi(UI_FILE_PATH, self)
        self.iam_services = iam_services
        self.button_1.clicked.connect(self.button_1_clicked)
        self.button_2.clicked.connect(self.button_2_clicked)
        self.button_3.clicked.connect(self.button_3_clicked)

    @property
    def name(self):
        return self.iam_services.name

    def button_1_clicked(self):
        self.iam_services._console.handle_console_input("dir")

    def button_2_clicked(self):
        self.iam_services._console.handle_console_input("ls")

    def button_3_clicked(self):
        self.iam_services._console.handle_console_input("where")