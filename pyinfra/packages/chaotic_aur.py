from pyinfra.operations import pacman
from pyinfra.operations import server
from pyinfra.operations import files

packages = [
    "paru",
    # "epson-inkjet-printer-escpr2",
]


def _summarize(result):
    # don’t assume stdout/stderr attributes exist
    attrs = [
        a
        for a in ("stdout", "stderr", "command", "commands", "return_code", "rc")
        if hasattr(result, a)
    ]
    out = {a: getattr(result, a, None) for a in attrs}
    # truncate any long strings
    for k, v in list(out.items()):
        if isinstance(v, str) and len(v) > 2000:
            out[k] = v[:2000] + "…[truncated]"
    return out


def get_primary_key() -> None:
    server.shell(
        name="Import Chaotic-AUR primary key",
        commands=[
            "printf 'y\n' | pacman-key --recv-key 3056513887B78AEB --keyserver keyserver.ubuntu.com",
            "printf 'y\n' | pacman-key --lsign-key 3056513887B78AEB",
        ],
    )


def install_keyring_mirror() -> None:

    server.shell(
        name="Install Chaotic-AUR keyring and mirrorlist",
        commands=[
            "pacman -U --noconfirm 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst'",
            "pacman -U --noconfirm 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'",
        ],
    )


def install():

    # 1. Import key
    get_primary_key()

    # 2. Install keyring + mirrorlist
    install_keyring_mirror()

    # 3. Add [chaotic-aur] to pacman.conf BEFORE syncing
    files.block(
        path="/etc/pacman.conf",
        present=True,
        backup=True,
        content=[
            "[chaotic-aur]",
            "Include = /etc/pacman.d/chaotic-mirrorlist",
        ],
        marker="## {mark} Chaotic AUR ##",
    )

    # 4. Now sync and update (includes chaotic-aur)
    pacman.update()
    pacman.upgrade()

    # 5. Update keyring packages
    pacman.packages(
        name="Update keyrings",
        present=True,
        packages=[
            "archlinux-keyring",
            "cachyos-keyring",
        ],
    )

    # 6. Import TNE's key (chaotic-keyring is stale)
    server.shell(
        name="Import TNE key",
        commands=[
            "pacman-key --recv-key D6C9442437365605 --keyserver keyserver.ubuntu.com",
            "printf 'y\\n' | pacman-key --lsign-key D6C9442437365605",
        ],
    )

    # 7. Final sync after key imports
    pacman.update()

    # 8. Install packages from chaotic-aur
    pacman.packages(
        name="Install Chaotic-AUR packages",
        packages=packages,
        present=True,
    )


def remove() -> None:

    pacman.packages(
        name="Remove packages installed from chaotic aur",
        packages=packages,
        present=False,
        update=True,
    )

    pacman.packages(
        name="Remove chaotic aur keyring & mirror",
        packages=[
            "chaotic-keyring",
            "chaotic-mirrorlist",
        ],
        present=False,
        update=True,
    )

    files.block(
        path="/etc/pacman.conf",
        present=True,
        backup=True,
        content=[
            "[chaotic-aur]",
            "Include = /etc/pacman.d/chaotic-mirrorlist",
        ],
        marker="## {mark} Chaotic AUR ##",
    )
    server.shell(
        name="Remove key-ring",
        commands=[
            "pacman-key --delete 3056513887B78AEB",
        ],
    )

    files.file(
        name="Delete chaotic-aur.db",
        path="/var/lib/pacman/sync/chaotic-aur.db",
        present="False",
    )

    files.file(
        name="Delete chaotic-aur.files",
        path="/var/lib/pacman/sync/chaotic-aur.files",
        present="False",
    )

    files.file(
        name="Delete chaotic-aur.sig",
        path="/var/lib/pacman/sync/chaotic-aur.sig",
        present="False",
    )
