from PyInstaller.__main__ import run


APP_NAME = "Clock"
MAIN_PY = "main.py"


def main() -> None:
    run([
        "--clean", "-y",
        "-n", APP_NAME,
        "-w",
        MAIN_PY
    ])


if __name__ == "__main__":
    main()