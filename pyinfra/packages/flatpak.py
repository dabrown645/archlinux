from pyinfra.operations import pacman
from pyinfra.operations import flatpak

packages = [
    "flatpak",
]

flatpaks = [
    "com.microsoft.Edge",
    "net.epson.epsonscan2",
]


def install() -> None:

    pacman.packages(
        name="Install flatpak",
        packages=packages,
        present=True,
        update=True,
    )

    flatpak.packages(
        name="Install flatpack packages",
        packages=flatpaks,
        present=True,
    )


def remove() -> None:

    pacman.packages(
        name="Remove flatpak",
        packages=packages,
        present=False,
        update=True,
    )

    flatpak.packages(
        name="Remove flatpack packages",
        packages=flatpaks,
        present=False,
    )
