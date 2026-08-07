from pyinfra.operations import pacman

packages = [
    "age",
    "chezmoi",
    "gdu",
    "opencode",
    "restic",
    "sddm-astronaut-theme",
    "shellcheck",
    "shfmt",
    "starship",
    "ventoy-bin",
    "yazi",
    "zoxide",
]


def install() -> None:
    global packages
    pacman.packages(
        name="Install My Tools",
        packages=packages,
        present=True,
        update=True,
    )


def remove() -> None:
    global packages
    pacman.packages(
        name="Remove My Tools",
        packages=packages,
        present=False,
        update=True,
    )
