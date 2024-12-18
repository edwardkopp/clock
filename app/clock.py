from tkinter import Misc as _Misc, BOTH as _BOTH
from tkinter.ttk import Frame as _Frame, Label as _Label
from tkinter.font import Font as _Font
from time import time as _time
from datetime import datetime as _datetime


class Clock(_Frame):

    def __init__(self, master: _Misc):
        _Frame.__init__(self, master)
        inner_frame = _Frame(self)
        self._timezone = _Label(inner_frame, font=_Font(size=12, weight="bold"))
        self._timezone.pack(padx=16, pady=16)
        self._time = _Label(inner_frame, font=_Font(size=32, weight="bold"))
        self._time.pack(padx=16)
        self._date = _Label(inner_frame, font=_Font(size=12, weight="bold"))
        self._date.pack(padx=16, pady=16)
        self.set_time_loop()
        inner_frame.pack(expand=True)

    def set_time_loop(self, now: _datetime | None = None) -> None:
        if not isinstance(now, _datetime):
            now = _datetime.now()
        timezone = now.astimezone().tzname()
        if timezone is not None:
            # Mac and Linux show three character code, but Windows does not
            self._timezone.config(text="".join(filter(lambda x: not x.islower(), timezone)).replace(" ", ""))
        self._time.config(text=now.strftime("%H:%M:%S"))
        self._date.config(text=now.strftime("%a %b %d %Y\n"))
        # noinspection PyTypeChecker
        self.after(int((((_time() + 1) // 1) - _time()) * 1000) + 10, self.set_time_loop)

    def pack(self, **kwargs) -> None:
        _Frame.pack(self, expand=True, fill=_BOTH, **kwargs)
