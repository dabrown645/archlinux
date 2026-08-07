#!/usr/bin/bash
from=${1}
master=${2}
while read -r pkg; do
  for req in $(pacman -Qi "${pkg}" | rg "Depends" | cut -f2 -d":"); do
    # echo ${req}
    req=${req//=*/}
    sed -i "/${req}/d" ${master}
  done
done <${from}
