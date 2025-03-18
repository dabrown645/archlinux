#!/usr/bin/bash

if [[ ${dryrun} == true ]]; then
  cmd="echo "
else
  cmd=""
fi

source utils.sh

# mountpoint=$(jq -r .disk_config.mountpoint user_configuration.json)
mountpoint=$(grep mountpoint user_configuration.json | cut -f 4 -d '"')
echo "mountpoint=${mountpoint}"

box_me "Install arch specific micro-code and snapper packages"
packages="${packages} $(./info.py snapper)"
${cmd} arch-chroot ${mountpoint} pacman -S --needed --noconfirm ${packages}
${cmd} arch-chroot ${mountpoint} umount /.snapshots
sleep 5
${cmd} arch-chroot ${mountpoint} rmdir /.snapshots
${cmd} arch-chroot ${mountpoint} snapper -c root create-config /
${cmd} arch-chroot ${mountpoint} btrfs subvol delete .snapshots
${cmd} arch-chroot ${mountpoint} mkdir /.snapshots
${cmd} arch-chroot ${mountpoint} mount -a
${cmd} arch-chroot ${mountpoint} systemctl daemon-reload
${cmd} arch-chroot ${mountpoint} systemctl enable --now grub-btrfsd
${cmd} arch-chroot ${mountpoint} ln -sf /boot/efi/grub /boot/grub
${cmd} arch-chroot ${mountpoint} grub-mkconfig -o /boot/grub/grub.cfg
