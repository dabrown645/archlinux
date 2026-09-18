from pyinfra.operations import pacman

packages = [
    "cachyos-hypr-noctalia",
    "dolphin",
    "hyprland",
    "kitty",
    "sddm",
]


def install() -> None:
    pacman.packages(
        name="Install Hyprland",
        packages=packages,
        present=True,
        update=True,
    )


def remove() -> None:
    pacman.packages(
        name="Remove Hyprland",
        packages=packages,
        present=False,
        update=True,
    )
