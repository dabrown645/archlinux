from pyinfra.operations import pacman

packages = [
    "ark",
    "bluedevil",
    "breeze-gtk",
    "cachyos-emerald-kde-theme-git",
    "cachyos-iridescent-kde",
    "cachyos-kde-settings",
    "cachyos-nord-kde-theme-git",
    "cachy-update",
    "char-white",
    "device-mapper",
    "dolphin",
    "ffmpegthumbs",
    "filelight",
    "fwupd",
    "gst-libav",
    "gst-plugins-bad",
    "gst-plugins-ugly",
    "gwenview",
    "haruna",
    "kate",
    "kcalc",
    "kdeconnect",
    "kdegraphics-thumbnailers",
    "kde-gtk-config",
    "kdeplasma-addons",
    "kdialog",
    "kinfocenter",
    "kio-admin",
    "konsole",
    "kscreen",
    "kwalletmanager",
    "kwallet-pam",
    "lvm2",
    "partitionmanager",
    "phonon-qt6-vlc",
    "plasma-browser-integration",
    "plasma-desktop",
    "plasma-firewall",
    "plasma-login-manager",
    "plasma-nm",
    "plasma-pa",
    "plasma-systemmonitor",
    "plasma-thunderbolt",
    "plymouth-kcm",
    "powerdevil",
    "spectacle",
    "tesseract-data-eng",
    "xsettingsd",
]


def install() -> None:
    pacman.packages(
        name="Install Plasma/KDE",
        packages=packages,
        present=True,
        update=True,
    )


def remove() -> None:
    pacman.packages(
        name="Remove Plasma/KDE",
        packages=packages,
        present=False,
        update=True,
    )
