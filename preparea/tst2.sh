#!/usr/bin/bash

while read -r pkg; do
  echo "${pkg}" : $(yay -Qi "${pkg}" | rg Description | cut -f2 -d":")
done <need
