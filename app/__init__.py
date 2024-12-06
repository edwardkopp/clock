from customtkinter import CTk as _Tk, set_appearance_mode as _set_mode
from .clock import Clock as _Clock


class App(_Tk):

    def __init__(self):
        _Tk.__init__(self)
        self.title("Clock")
        self.attributes("-topmost", True)
        self.attributes("-alpha", 0.7)
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.quit)
        self.clock = _Clock(self)
        self.clock.pack()

    def run(self):
        _set_mode("dark")
        self.mainloop()

    def quit(self) -> None:
        self.destroy()
        self.clock.stop()
        _Tk.quit(self)
