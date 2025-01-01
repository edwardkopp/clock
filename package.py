from PyInstaller.__main__ import run
from sys import platform
from os.path import join
from shutil import rmtree


APP_NAME = "Clock"
MAIN_PY = "main.py"


def package() -> None:
    run([
        "--clean", "-y",
        "-n", APP_NAME,
        "-w", MAIN_PY
    ])
    if platform == "darwin":
        rmtree(join(".", "dist", APP_NAME))


if __name__ == "__main__":
    package()
