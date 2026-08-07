from pyinfra.operations import pacman

packages = [
    "distrobox",
    "podman",
    "qemu-full",
    "quickemu-git",
]


def install() -> None:
    global packages
    pacman.packages(
        name="Install Virtualization",
        packages=packages,
        present=True,
        update=True,
    )


def remove() -> None:
    global packages
    pacman.packages(
        name="Remove Virtualization",
        packages=packages,
        present=False,
        update=True,
    )
