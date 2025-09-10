import random
import string
import threading
import time

from model.notification.emitting_property import EmittingProperty


class SessionInfo:
    def __init__(self):
        self.region = EmittingProperty()
        self.output = EmittingProperty()
