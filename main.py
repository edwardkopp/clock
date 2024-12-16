from app import App
from app.clock import Clock


def main() -> None:
    app = App()
    clock = Clock(app)
    clock.pack()
    app.mainloop()
    clock.stop()


if __name__ == '__main__':
    main()
