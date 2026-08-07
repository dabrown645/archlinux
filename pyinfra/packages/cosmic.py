from pyinfra.operations import pacman

packages = [
    "cosmic-comp",
    "cosmic-files",
    "cosmic-greeter",
    "cosmic-icon-theme",
    "cosmic-idle",
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
    "cosmic-sound-theme",
    "cosmic-store",
    "cosmic-terminal",
    "cosmic-text-editor",
    "cosmic-wallpapers",
    "cosmic-workspaces",
]


def install() -> None:
    global packages
    pacman.packages(
        name="Install Cosmic",
        packages=packages,
        present=True,
        update=True,
    )


def remove() -> None:
    global packages
    pacman.packages(
        name="Remove Cosmic",
        packages=packages,
        present=False,
        update=True,
    )


# cosmic-app-library 1:1.4.0-1.1 (cosmic) Cosmic App Library
# cosmic-applets 1:1.4.0-1.1 (cosmic) Applets for COSMIC Panel
# cosmic-bg 1:1.4.0-1.1 (cosmic) COSMIC session service which applies backgrounds to displays
# cosmic-comp 1:1.4.0-1.1 (cosmic) Compositor for the COSMIC desktop environment
# cosmic-files 1:1.4.0-1.1 (cosmic) File manager for the COSMIC desktop environment
# cosmic-greeter 1:1.4.0-1.1 (cosmic) COSMIC greeter for greetd
# cosmic-icon-theme 1:1.4.0-1 Cosmic icon theme
# cosmic-idle 1:1.4.0-1.1 (cosmic) Cosmic idle daemon
# cosmic-launcher 1:1.4.0-1.1 (cosmic) Layer Shell frontend for Pop Launcher
# cosmic-monitor 1:1.4.0-1.1 (cosmic) COSMIC System Monitor
# cosmic-notifications 1:1.4.0-1.1 (cosmic) Layer Shell notifications daemon which integrates with COSMIC
# cosmic-osd 1:1.4.0-1.1 (cosmic) COSMIC On-Screen Display
# cosmic-panel 1:1.4.0-1.1 (cosmic) XDG Shell Wrapper Panel for Cosmic
# cosmic-player 1:1.4.0-1.1 (cosmic) WIP COSMIC media player
# cosmic-randr 1:1.4.0-1.1 (cosmic) Library and utility for displaying and configuring Wayland outputs
# cosmic-screenshot 1:1.4.0-1.1 (cosmic) Utility for capturing screenshots via XDG Desktop Portal
# cosmic-session 1:1.4.0-1.1 (cosmic) Session manager for the COSMIC desktop environment
# cosmic-settings 1:1.4.0-1.1 (cosmic) The settings application for the COSMIC desktop environment
# cosmic-settings-daemon 1:1.4.0-2.1 (cosmic) Cosmic settings daemon
# cosmic-sound-theme 1.4.0-1 (cosmic) Sound theme for the COSMIC desktop environment
# /cosmic-store 1:1.5.0-1.1 (cosmic) [installed] Cosmic App Store
# cosmic-terminal 1:1.4.0-1.1 (cosmic) Cosmic Terminal Emulator
# cosmic-text-editor 1:1.4.0-1.1 (cosmic) Text editor for the COSMIC desktop
# cosmic-wallpapers 2:1.4.0-1 (cosmic) Wallpapers for the COSMIC Desktop Environment
# cosmic-workspaces 2:1.4.0-1.1 (cosmic) Cosmic workspaces
# xdg-desktop-portal-cosmic 1:1.4.0-1.1 (cosmic) A backend implementation for xdg-desktop-portal for the COSMIC desktop environment
#
#
#
