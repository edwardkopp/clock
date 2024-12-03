from customtkinter import CTk as _Tk
from .clock import Clock as _Clock


class App(_Tk):

    def __init__(self):
        _Tk.__init__(self)
        self.title("Clock")
        self.attributes("-topmost", True)
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.quit)
        self.clock = _Clock(self)
        self.clock.pack()

    def run(self):
        self.mainloop()

    def quit(self) -> None:
        self.destroy()
        self.clock.stop()
        _Tk.quit(self)
