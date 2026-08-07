from pyinfra.operations import pacman

packages = [
    "betterbird-bin",
    "brave-origin-bin",
    "libreoffice-fresh",
    "hunspell-en_us",
    "zoom",
]


def install() -> None:
    global packages
    pacman.packages(
        name="Install Office Products",
        packages=packages,
        present=True,
        update=True,
    )


def remove() -> None:
    global packages
    pacman.packages(
        name="Remove Office Products",
        packages=packages,
        present=False,
        update=True,
    )
