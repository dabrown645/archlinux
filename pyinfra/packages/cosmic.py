from pyinfra.operations import pacman

packages = [
    "cosmic-applets",
    "cosmic-app-library",
    "cosmic-bg",
    "cosmic-comp",
    "cosmic-files",
    "cosmic-greeter",
    "cosmic-icon-theme",
    "cosmic-launcher",
    "cosmic-monitor",
    "cosmic-notifications",
    "cosmic-osd",
    "cosmic-panel",
    "cosmic-player",
    "cosmic-randr",
    "cosmic-screenshot",
    "cosmic-session",
    "cosmic-settings",
    "cosmic-settings-daemon",
    "cosmic-terminal",
    "cosmic-text-editor",
    "cosmic-wallpapers",
    "cosmic-workspaces",
    "device-mapper",
    "gnome-keyring",
    "gst-libav",
    "gst-plugins-bad",
    "gst-plugins-ugly",
    "lvm2",
    "notification-daemon",
    "xdg-desktop-portal-cosmic",
    "xdg-desktop-portal-gtk",
    "xorg-xwayland",
]


def install() -> None:
    pacman.packages(
        name="Install Cosmic",
        packages=packages,
        present=True,
        update=True,
    )


def remove() -> None:
    pacman.packages(
        name="Remove Cosmic",
        packages=packages,
        present=False,
        update=True,
    )
