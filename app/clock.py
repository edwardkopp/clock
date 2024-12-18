from tkinter import Misc as _Misc, StringVar as _StringVar
from customtkinter import CTkFrame as _Frame, CTkLabel as _Label, CTkFont as _Font, BOTH as _BOTH
from time import sleep as _sleep, time as _time
from datetime import datetime as _datetime
from threading import Thread as _Thread, current_thread as _current_thread


class Clock(_Frame):

    def __init__(self, master: _Misc):
        _Frame.__init__(self, master)
        self._timezone = _StringVar(self)
        self._time = _StringVar(self)
        self._date = _StringVar(self)
        self.set_time()
        _Label(self, textvariable=self._timezone, font=_Font(size=20)).pack(padx=16, pady=16)
        _Label(self, textvariable=self._time, font=_Font(size=64)).pack(padx=16)
        _Label(self, textvariable=self._date, font=_Font(size=24)).pack(padx=16, pady=16)
        self._thread: _Thread | None = None

    def set_time(self, now: _datetime | None = None) -> None:
        if not isinstance(now, _datetime):
            now = _datetime.now()
        timezone = now.astimezone().tzname()
        if timezone is not None:
            # Mac and Linux show three character code, but Windows does not
            self._timezone.set("".join(filter(lambda x: not x.islower(), timezone)).replace(" ", ""))
        self._time.set(now.strftime("%H:%M:%S"))
        self._date.set(now.strftime("%A\n%Y %b %d"))

    def time_thread(self) -> None:
        thread = _current_thread()

        def get_state() -> bool:
            return getattr(thread, "active", True)

        cycle = 0
        while get_state():
            _sleep(min(0.5, ((_time() + 1) // 1) - _time()))
            if not get_state():
                return
            self.set_time()
            cycle += 1

    def pack(self, **kwargs) -> None:
        if isinstance(self._thread, _Thread):
            return
        self._thread = _Thread(target=self.time_thread)
        self._thread.start()
        _Frame.pack(self, expand=True, fill=_BOTH, **kwargs)

    def stop(self) -> None:
        if not isinstance(self._thread, _Thread):
            return
        self._thread.active = False
        self._thread.join()
        self._thread = None
