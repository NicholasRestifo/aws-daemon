from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from ui.services.services_widget import ServicesWidget

UI_FILE_PATH = "ui/services/cloud_watch_form.ui"


class CloudWatchWidget(ServicesWidget):
    def __init__(self, cloud_watch_services):
        super().__init__()
        uic.loadUi(UI_FILE_PATH, self)
        self.cloud_watch_services = cloud_watch_services
        self.button_1.clicked.connect(self.button_1_clicked)
        self.button_2.clicked.connect(self.button_2_clicked)
        self.button_3.clicked.connect(self.button_3_clicked)

    @property
    def name(self):
        return self.cloud_watch_services.name

    def button_1_clicked(self):
        self.cloud_watch_services._console.handle_console_input("systeminfo")

    def button_2_clicked(self):
        self.cloud_watch_services._console.handle_console_input("tasklist")

    def button_3_clicked(self):
        self.cloud_watch_services._console.handle_console_input("help")