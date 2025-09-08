from model.services import Services


class IamServices(Services):
    def __init__(self, console):
        super().__init__()
        self.name = "IAM"
        self._console = console
