from __future__ import annotations

import queue
import threading
import time

import pyttsx3


class AudioFeedback:
    def __init__(self, cooldown_seconds: int = 4) -> None:
        self.cooldown_seconds = cooldown_seconds
        self._last_spoken_at: dict[str, float] = {}
        self._queue: queue.Queue[str] = queue.Queue()
        self._engine = pyttsx3.init()
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def speak_detection(self, label: str) -> None:
        now = time.time()
        previous = self._last_spoken_at.get(label, 0.0)
        if now - previous < self.cooldown_seconds:
            return
        self._last_spoken_at[label] = now
        self._queue.put(f"Caution. {label} detected ahead.")

    def _run(self) -> None:
        while True:
            text = self._queue.get()
            self._engine.say(text)
            self._engine.runAndWait()
