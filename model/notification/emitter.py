class Emitter:
    def __init__(self):
        self._listeners = []

    def connect(self, listener):
        self._listeners.append(listener)

    def disconnect(self, listener):
        self._listeners.remove(listener)

    def emit(self, *args, **kwargs):
        for listener in self._listeners:
            listener(*args, **kwargs)