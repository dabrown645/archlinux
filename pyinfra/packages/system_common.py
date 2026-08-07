from pyinfra.operations import pacman

packages = [
    "7zip",
    "bc",
    "cachy-update",
    "cdrtools",
    # "dislocker",
    "downgrade",
    "epson-inkjet-printer-escpr2",
    "ffmpegthumbs",
    "fwupd",
    "gptfdisk",
    "mokutil",
    "pax",
    "tpm2-tools",
    "zsync",
]


def install() -> None:
    global packages
    pacman.packages(
        name="Install Common System",
        packages=packages,
        present=True,
        update=True,
    )


def remove() -> None:
    global packages
    pacman.packages(
        name="Remove Common System",
        packages=packages,
        present=False,
        update=True,
    )
