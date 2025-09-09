import random
import string
import threading
import time

from model.notification.emitting_property import EmittingProperty


class SessionInfo:
    def __init__(self):
        self.user_name = EmittingProperty()
        self.region = EmittingProperty()
        self.auth_token = DumbAuthToken()

class DumbAuthToken(EmittingProperty):
    def __init__(self):
        super().__init__()

        self.generate_auth_token()
        # TODO something about the threading here causes a huge error when the application is closed
        thread_instance = threading.Thread(target=self.update_loop, args=())
        thread_instance.start()

    def update_loop(self):
        while True:
            time.sleep(1)
            self.generate_auth_token()

    def generate_auth_token(self):
        self.value = ''.join(random.choices(string.ascii_letters, k=50))