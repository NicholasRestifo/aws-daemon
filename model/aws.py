from model.console import Console


class Aws:
    def __init__(self, session_info):
        super().__init__()
        self.session_info = session_info
        self.console = Console()