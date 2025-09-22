from model.cloud_watch_services import CloudWatchServices
from model.iam_services import IamServices


class Aws:
    def __init__(self, console, session_info):
        super().__init__()
        self.session_info = session_info
        self.console = console
        self.iam_services = IamServices(console)
        self.cloud_watch_services = CloudWatchServices(console)