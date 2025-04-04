#!/usr/bin/env bash
fix_pacmanconf() {
  pacmanconf=${1:-/etc/pacman.conf}

  sed -i -e 's/#*Parallel.*/ParallelDownloads = 20/' \
    -e 's/#Color/Color/' \
    -e 's/#VerbosePkgLists/VerbosePkgLists/' \
    -e 's/#CheckSpace/CheckSpace/' \
    "${pacmanconf}"
  sed -i '/Parallel/a ILoveCandy' "${pacmanconf}"
}

fix_grub-btrfs() {
  grub_btrfs_config=${1:-/etc/default/grub-btrfs/config}

  cp "${grub_btrfs_config}" "${grub_btrfs_config}.$(date +%y%m%d)"
  sed -i -e 's/#*GRUB_BTRFS_GRUB_DIRNAME.*/GRUB_BTRFS_GRUB_DIRNAME=\"\/efi\/grub\"/' \
    -e 's/#*GRUB_BTRFS_GBTRFS_DIRNAME.*/GRUB_BTRFS_GBTRFS_DIRNAME=\"\/efi\/grub\"/' \
    "${grub_btrfs_config}"
}

fix_locale_gen() {
  locale_gen=${1:-/etc/locale.gen}

  sed -i -e 's/#en_US.UTF-8/en_US.UTF-8/' ${locale_gen}
}

fix_locale_conf() {
  locale_conf=${1:-/etc/locale.conf}

  {
    echo "LANG=en_US.UTF-8"
    echo "LC_ADDRESS=en_US.UTF-8"
    echo "LC_IDENTIFICATION=en_US.UTF-8"
    echo "LC_MEASUREMENT=en_US.UTF-8"
    echo "LC_MONETARY=en_US.UTF-8"
    echo "LC_NAME=en_US.UTF-8"
    echo "LC_NUMERIC=en_US.UTF-8"
    echo "LC_PAPER=en_US.UTF-8"
    echo "LC_TELEPHONE=en_US.UTF-8"
    echo "LC_TIME=en_US.UTF-8"
  } >"${locale_conf}"
}

fix_fstab() {
  set -x
  prefix=${1:- }

  for dir in $(grep subvol ./fstab | cut -f 2 -d ' '); do
    mkdir -p ${prefix}/${dir}
  done

  for dir in $(grep bind ./fstab | cut -f4 -d'/'); do
    mkdir -p ${prefix}/home/dabrown/${dir}
  done

  cat ./fstab >>${prefix}/etc/fstab
  set +x

}

fix_locale_conf() {
  locale_conf=${1:-/etc/locale.conf}

  {
    echo "LANG=en_US.UTF-8"
    echo "LC_ADDRESS=en_US.UTF-8"
    echo "LC_IDENTIFICATION=en_US.UTF-8"
    echo "LC_MEASUREMENT=en_US.UTF-8"
    echo "LC_MONETARY=en_US.UTF-8"
    echo "LC_NAME=en_US.UTF-8"
    echo "LC_NUMERIC=en_US.UTF-8"
    echo "LC_PAPER=en_US.UTF-8"
    echo "LC_TELEPHONE=en_US.UTF-8"
    echo "LC_TIME=en_US.UTF-8"
  } >"${locale_conf}"
}

fix_vconsole_conf() {
  vsconsole_conf=${1:-/etc/vconsole.conf}
  {
    echo "FONT=ter-220n"
    echo "KEYMAP=us"
  } >"${vsconsole_conf}"
}

fix_hostname() {
  hostname=${1:-/etc/hostname}

  {
    echo "rog1"
  } >"${hostname}"
}

fix_localtime() {
  localtime=${1:-/etc/localtime}
  timezone="America/Los_Angles"

  ln -sf /usr/share/zoneinfo/${timezone} "${localtime}"
}

fix_sudoers_wheel() {
  sudoers=${1:-/etc/sudoers}
  sed -i -e 's/# *%wheel  *ALL=(ALL:ALL)  *ALL/%wheel ALL=(ALL:ALL) ALL/' "${sudoers}"
}

box_me() {
  local s="MyArch: ${*}"
  tput setaf 3
  echo "╔══${s//?/═}╗"
  echo "║ ${s} ║" # U+2550-255f
  echo "╚══${s//?/═}╝"
  tput sgr0
  sleep 3
  # 0 1 2 3 4 5 6 7 8 9 0 a b c d e f
  # ═ ║ ╒ ╓ ╔ ╕ ╖ ╗ ╘ ╙ ═ ╚ ╛ ╜ ╝ ≞ ╟
}

mylsblk() {
  lsblkopt="NAME,FSTYPE,PARTLABEL,MOUNTPOINTS,UUID"
  # shellcheck disable=SC2086
  lsblk -o "${lsblkopt}" ${1}
}
