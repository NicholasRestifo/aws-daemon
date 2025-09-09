import subprocess

from model.notification.emitter import Emitter


class Console:
    def __init__(self):
        self.out_text_emitter = Emitter()

    def _post_out_text(self, out_text):
        self.out_text_emitter.emit(out_text)

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
