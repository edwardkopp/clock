from PyInstaller.__main__ import run


APP_NAME = "Clock"
MAIN_PY = "main.py"


def package() -> None:
    run([
        "--clean", "-y", "-w"
        "-n", APP_NAME,
        MAIN_PY
    ])


if __name__ == "__main__":
    package()