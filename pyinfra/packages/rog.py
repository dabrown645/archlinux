from pyinfra.operations import pacman

packages = [
    "asusctl",
    "rog-control-center",
    "supergfxctl",
]


def install() -> None:
    global packages
    pacman.packages(
        name="Install rog software",
        packages=packages,
        present=True,
        update=True,
    )


def remove() -> None:
    global packages
    pacman.packages(
        name="Remove rog software",
        packages=packages,
        present=False,
        update=True,
    )
