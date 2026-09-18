from pyinfra.operations import pacman

packages = [
        "cmake",
        "neovim",
        "uv",
        "worktrunk",
    ]


def install() -> None:
    pacman.packages(
        name="Install Common Development",
        packages=packages,
        present=True,
        update=True,
    )


def remove() -> None:
    pacman.packages(
        name="Remove Common Development",
        packages=packages,
        present=False,
        update=True,
    )
