from tkinter import Tk as _Tk
from .clock import Clock as _Clock


class App(_Tk):

    def __init__(self):
        _Tk.__init__(self)
        self.title("Clock")
        self.geometry("240x180")
        self.attributes("-topmost", True)
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.destroy)
        _Clock(self).pack()
