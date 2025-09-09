from model.notification.emitter import Emitter


class EmittingProperty:
    def __init__(self, value=None):
        super().__init__()
        self.changed = Emitter()
        self._value = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self.changed.emit(value)

