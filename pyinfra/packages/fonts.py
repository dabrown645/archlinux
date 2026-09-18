from pyinfra.operations import pacman

packages = [
    "ttf-droid",
    "ttf-fira-code",
    "ttf-jetbrains-mono",
    "ttf-jetbrains-mono-nerd",
]


def install() -> None:
    pacman.packages(
        name="Install Fonts",
        packages=packages,
        present=True,
        update=True,
    )


def remove() -> None:
    pacman.packages(
        name="Remove Fonts",
        packages=packages,
        present=False,
        update=True,
    )
