from PyQt6.QtWidgets import QTabWidget

from ui.services.could_watch_widget import CloudWatchWidget
from ui.services.iam_widget import IamWidget

UI_FILE_PATH = "ui/services/services_form.ui"


class ServiceTabWidget(QTabWidget):
    def __init__(self, aws, parent):
        super().__init__(parent)

        self.add_tab(
            IamWidget(
                aws.iam_services))

        self.add_tab(
            CloudWatchWidget(
                aws.cloud_watch_services))

    def add_tab(self, services_widget):
        self.addTab(
            services_widget,
            services_widget.name)