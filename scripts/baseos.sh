
reflector --country US --age 24 --protocol http,https --sort rate --save /etc/pacman.d/mirrorlist

pacstrap -K /mnt base base-devel linux linux-firmware intel-ucode cryptsetup btrfs-progs neovim dosfstools util-linux git unzip sbctl wezterm networkmanager sudo

### bad signatures
# pacman -Sy archlinux-keyring
# pacman-key --populate archlinux
# pacman-key --refresh-keys
###

sed -i -e "s/^#en_US.UTF-8/en_US.UTF-8/" /mnt/etc/locale.gen

systemd-firstboot --root /mnt --prompt

arch-chroot /mnt locale-gen

arch-chroot /mnt useradd -G wheel -m dabrown
arch-chroot /mnt passwd dabrown

#sed -i -e '/^# %wheel ALL=(ALL:ALL) NOPASSWD: ALL/s/^# //' /mnt/etc/sudoers
sed -i -e '/^# %wheel ALL=(ALL:ALL) ALL/s/^# //' /mnt/etc/sudoers

#Unified kernel

echo "quiet rw" > /mnt/etc/kernel/cmdline

mkdir -p /mnt/efi/EFI/Linux

sed -i -e 's/^HOOKS=.*/HOOKS=(base systemd autodetect modconf kms keyboard sd-vconsole sd-encrypt block filesystems fsck)/' /mnt/etc/mkinitcpio.conf

sed -i -e 's/^#ALL_config/ALL_config/' /mnt/etc/mkinitcpio.d/linux.preset
sed -i -e 's/^default_image/#default_image/' /mnt/etc/mkinitcpio.d/linux.preset
sed -i -e 's/^#default_uki/default_uki/' /mnt/etc/mkinitcpio.d/linux.preset
sed -i -e 's/^#default_options/default_options/' /mnt/etc/mkinitcpio.d/linux.preset
sed -i -e 's/^fallback_config/#fallback_config/' /mnt/etc/mkinitcpio.d/linux.preset
sed -i -e 's/^fallback_image/#fallback_image/' /mnt/etc/mkinitcpio.d/linux.preset
sed -i -e 's/^#fallback_uki/fallback_uki/' /mnt/etc/mkinitcpio.d/linux.preset
sed -i -e 's/^#fallback_options/fallback_options/' /mnt/etc/mkinitcpio.d/linux.preset
sed -i '/^ALL_kver/a ALL_microcode=(/boot/*-ucode.img)/fallback_options/' /mnt/etc/mkinitcpio.d/linux.preset


arch-chroot /mnt mkinitcpio -P

systemctl --root /mnt enable systemd-resolved systemd-timesyncd NetworkManager
systemctl --root /mnt mask systemd-networkd
arch-chroot /mnt bootctl install --esp-path=/efi

sync
systemctl reboot --firmware-setup
