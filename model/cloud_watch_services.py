from model.services import Services


class CloudWatchServices(Services):
    def __init__(self, console):
        super().__init__()
        self.name = "Cloud Watch"
        self._console = console
