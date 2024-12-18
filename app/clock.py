from tkinter import Misc as _Misc, StringVar as _StringVar, BOTH as _BOTH
from tkinter.ttk import Frame as _Frame, Label as _Label
from tkinter.font import Font as _Font
from time import sleep as _sleep, time as _time
from datetime import datetime as _datetime
from threading import Thread as _Thread, current_thread as _current_thread


class Clock(_Frame):

    def __init__(self, master: _Misc):
        _Frame.__init__(self, master)
        inner_frame = _Frame(self)
        self._timezone = _StringVar(inner_frame)
        self._time = _StringVar(inner_frame)
        self._date = _StringVar(inner_frame)
        self.set_time()
        _Label(inner_frame, textvariable=self._timezone, font=_Font(size=12, weight="bold")).pack(padx=16, pady=16)
        _Label(inner_frame, textvariable=self._time, font=_Font(size=32, weight="bold")).pack(padx=16)
        _Label(inner_frame, textvariable=self._date, font=_Font(size=12, weight="bold")).pack(padx=16, pady=16)
        inner_frame.pack(expand=True)
        self._thread: _Thread | None = None

    def set_time(self, now: _datetime | None = None) -> None:
        if not isinstance(now, _datetime):
            now = _datetime.now()
        timezone = now.astimezone().tzname()
        if timezone is not None:
            # Mac and Linux show three character code, but Windows does not
            self._timezone.set("".join(filter(lambda x: not x.islower(), timezone)).replace(" ", ""))
        self._time.set(now.strftime("%H:%M:%S"))
        self._date.set(now.strftime("%a %b %d %Y\n"))

    def time_thread(self) -> None:
        thread = _current_thread()

        def get_state() -> bool:
            return getattr(thread, "active", True)

        while get_state():
            _sleep(max(0.5, ((_time() + 1) // 1) - _time()))
            if get_state():
                self.set_time()
            else:
                break

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
