from PyQt6.QtWidgets import QTabWidget

from ui.services.could_watch_widget import CloudWatchWidget
from ui.services.iam_widget import IamWidget

UI_FILE_PATH = "ui/services/services_form.ui"


class ServicesWidget(QTabWidget):
    def __init__(self, console, parent):
        super().__init__(parent)
        #todo pull names from data structure? move all this logic to a ui file?
        self.addTab(IamWidget(console), "IAM")
        self.addTab(CloudWatchWidget(console), "CloudWatch")
