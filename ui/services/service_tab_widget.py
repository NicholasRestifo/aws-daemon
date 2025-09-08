from PyQt6.QtWidgets import QTabWidget

from model.cloud_watch_services import CloudWatchServices
from model.iam_services import IamServices
from ui.services.could_watch_widget import CloudWatchWidget
from ui.services.iam_widget import IamWidget

UI_FILE_PATH = "ui/services/services_form.ui"


class ServiceTabWidget(QTabWidget):
    def __init__(self, console, parent):
        super().__init__(parent)

        self.add_tab(
            IamWidget(
                IamServices(
                    console)))

        self.add_tab(
            CloudWatchWidget(
                CloudWatchServices(
                    console)))

    def add_tab(self, services_widget):
        self.addTab(
            services_widget,
            services_widget.name)