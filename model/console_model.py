from PyQt6.QtCore import QProcess


def process_data_to_text(data):
    return data.data().decode('utf-8').strip()


class ConsoleModel:
    def __init__(self):
        self.out_subscribers = []
        self.process = QProcess()

        self.process.readyReadStandardOutput.connect(self._print_process_output)
        self.process.readyReadStandardError.connect(self._print_process_output)

    def subscribe_out_text(self, out_text_consumer):
        self.out_subscribers.append(out_text_consumer)

    def _post_out_text(self, out_text):
        for subscriber in self.out_subscribers:
            subscriber(out_text)

    def _print_process_output(self):
        self._post_out_text(
            process_data_to_text(
                self.process.readAllStandardOutput()))
        self._post_out_text(
            process_data_to_text(
                self.process.readAllStandardError()))

    def input_text(self, input_text):
        self._post_out_text(input_text)
        self.process.start(input_text)
