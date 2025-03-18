fix_pacmanconf() {
  pacmanconf=${1:-/etc/pacman.conf}

  sed -i -e 's/#Parallel.*/ParallelDownloads = 20/' \
    -e 's/#Color/Color/' \
    -e 's/#VerbosePkgLists/VerbosePkgLists/' \
    -e 's/#CheckSpace/CheckSpace/' \
    ${pacmanconf}
  sed -i '/Parallel/a ILoveCandy' ${pacmanconf}
}

box_me() {
  local s="MyArch: ${*}"
  tput setaf 3
  echo "╔══${s//?/═}╗"
  echo "║ ${s} ║" # U+2550-255f
  echo "╚══${s//?/═}╝"
  tput sgr0
  # 0 1 2 3 4 5 6 7 8 9 0 a b c d e f
  # ═ ║ ╒ ╓ ╔ ╕ ╖ ╗ ╘ ╙ ═ ╚ ╛ ╜ ╝ ≞ ╟
}

mylsblk() {
  lsblkopt="-o NAME,FSTYPE,PARTLABEL,MOUNTPOINTS"
  lsblk ${lsblkopt} ${1}
}
