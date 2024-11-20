disk=/dev/vda

# Partition the disk drive

sgdisk -Z ${disk}

sgdisk --new=0:0:+1G --change-name=0:EFI --typecode=0:ef00 ${disk}          # setup efi partition
sgdisk --new=0:0:+10G --change-name=0:swap --typecode=0:8200 ${disk}        # setup swap partion
sgdisk --largest-new=0 --change-name=0:archlinux --typecode=0:8303 ${disk}  # setup root partition


# Encrypt the disk drive

rootdevice=/dev/disk/by-partlabel/archlinux

cryptsetup luksFormat --type luks2 ${rootdevice}
cryptsetup luksOpen ${rootdevice} root

# make file systems
rootcrypt=/dev/mapper/root

mkswap /dev/disk/by-partlabel/swap
swapon /dev/disk/by-partlabel/swap

mkfs.vfat -F32 -n EFI /dev/disk/by-partlabel/EFI
mkfs.btrfs -f -L archlinux ${rootcrypt}

mount ${rootcrypt} /mnt

btrfs subvolume create /mnt/@
btrfs subvolume create /mnt/@home
btrfs subvolume create /mnt/@root
btrfs subvolume create /mnt/@srv
btrfs subvolume create /mnt/@cache
btrfs subvolume create /mnt/@log
btrfs subvolume create /mnt/@tmp
btrfs subvolume create /mnt/@image
btrfs subvolume create /mnt/@.snapshots

umount -R /mnt

mount --options subvol=/@,defaults,noatime,compress=zstd ${rootcrypt} /mnt
mount --mkdir --options subvol=/@home,defaults,noatime,compress=zstd ${rootcrypt} /mnt/home
mount --mkdir --options subvol=/@.snapshots,defaults,noatime,compress=zstd ${rootcrypt} /mnt/.snapshots
mount --mkdir --options subvol=/@root,defaults,noatime,compress=zstd ${rootcrypt} /mnt/root
mount --mkdir --options subvol=/@srv,defaults,noatime,compress=zstd ${rootcrypt} /mnt/srv
mount --mkdir --options subvol=/@cache,defaults,noatime,compress=zstd ${rootcrypt} /mnt/var/cache
mount --mkdir --options subvol=/@log,defaults,noatime,compress=zstd ${rootcrypt} /mnt/var/log
mount --mkdir --options subvol=/@tmp,defaults,noatime,compress=zstd ${rootcrypt} /mnt/var/tmp
mount --mkdir --options subvol=/@images,defaults,noatime,compress=zstd ${rootcrypt} /mnt/var/lib/libvirt/images

mount --mkdir --options defaults,umask=0077 /dev/disk/by-partlabel/EFI /mnt/efi


