import subprocess


class Console:
    def __init__(self):
        self.out_subscribers = []

    def subscribe_out_text(self, out_text_consumer):
        self.out_subscribers.append(out_text_consumer)

    def _post_out_text(self, out_text):
        for subscriber in self.out_subscribers:
            subscriber(out_text)

    def handle_console_input(self, console_input):
        self._post_out_text(console_input)
        self._run_process(console_input)

    def _run_process(self, console_input):
        completed_process = subprocess.run(
            console_input,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding='utf-8')
        self._post_out_text(str(completed_process.stdout).strip())
        self._post_out_text(str(completed_process.stderr).strip())
