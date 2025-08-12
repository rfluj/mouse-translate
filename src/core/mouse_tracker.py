from pynput import mouse
import threading
import time
from utils import get_text_under_mouse
from .translator import Translate

translator = Translate()

class MouseTracker:
    def __init__(self, window):
        self._running = False
        self._thread = None
        self._mouse = mouse.Controller()
        self._window = window
        self.text = ""
        self.new_text = ""

    def _track(self):
        while self._running:
            pos = self._mouse.position
            self.new_text = get_text_under_mouse(x=pos[0], y=pos[1])
            if self.new_text == self.text:
                pass
            else:
                self.text = self.new_text
                translated_text = translator._translate_text(self.text, "fa")
                self._window.show(translated_text, pos)  # تغییر UI از طریق window.show که امن است
            # print(f"موقعیت موس: {pos} و متن زیر آن : {text}")
            time.sleep(0.2)

    def start(self):
        if not self._running:
            self._running = True
            self._thread = threading.Thread(target=self._track, daemon=True)
            self._thread.start()

    def stop(self):
        if self._running:
            self._running = False
            if self._thread:
                self._thread.join()

    @property
    def is_running(self):
        return self._running
