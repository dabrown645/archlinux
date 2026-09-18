# Encrypt Storage Partition + TPM2 Auto-Unlock

> **Scope:** LUKS2 encryption of the `storage` partition with TPM2-based auto-unlock on CachyOS.
> **Prerequisite:** This is for a **fresh install only**. The partition will be wiped during encryption.
> **Mount strategy:** Systemd mount units (no fstab for Storage).
> **Owner:** Rex (Senior Administrator)

## Overview

The Storage partition (`PARTLABEL=storage`) holds user data bind-mounted to `/Storage/dabrown/` and `/Storage/Backups/`. This procedure encrypts it with LUKS2 and enrolls TPM2 for automatic passphrase-free unlock on boot.

All mounts use systemd units. The dependency chain is:

```
LUKS unlock (cryptsetup)
  → /dev/mapper/storage available
    → Storage-dabrown.mount (subvol=@dabrown)
    → Storage-Backups.mount (subvol=@backup)
      → home-dabrown-*.mount (bind mounts)
```

## Procedure

### Step 1: Backup existing data

If there is data on the Storage partition you need to keep, copy it off before proceeding. The partition gets wiped.

```bash
# Check what's currently on Storage
lsblk /dev/disk/by-partlabel/storage
```

### Step 2: Encrypt the partition

```bash
# Wipe and encrypt with LUKS2
cryptsetup luksFormat \
  --type luks2 \
  --cipher aes-xts-plain64 \
  --key-size 512 \
  --hash sha256 \
  /dev/disk/by-partlabel/storage

# Open it (prompts for the passphrase you just set)
cryptsetup open /dev/disk/by-partlabel/storage storage

# Create BTRFS filesystem
mkfs.btrfs -L Storage /dev/mapper/storage
```

### Step 3: Create subvolumes

```bash
# Mount the encrypted volume
mount --mkdir /dev/mapper/storage /mnt/storage

# Create subvolumes matching the existing layout
btrfs subvolume create /mnt/storage/@dabrown
btrfs subvolume create /mnt/storage/@backup

# Unmount
umount /mnt/storage
```

### Step 4: Generate auto-unlock keyfile

```bash
# Create the keyfile directory
mkdir -p /etc/cryptsetup-keys.d

# Generate a random 4096-byte keyfile
dd if=/dev/urandom of=/etc/cryptsetup-keys.d/storage.key \
  bs=4096 count=1 mode=0400

# Add the keyfile as a LUKS key
cryptsetup luksAddKey \
  /dev/disk/by-partlabel/storage \
  /etc/cryptsetup-keys.d/storage.key
```

### Step 5: Enroll with TPM2

```bash
# Register with TPM2 for auto-unlock
# PCR 7 = Secure Boot state (same as root volume)
systemd-cryptenroll \
  --tpm2-device=auto \
  --tpm2-pcrs=7 \
  /dev/disk/by-partlabel/storage
```

> **Warning:** If you toggle Secure Boot mode (Standard ↔ Custom), TPM2 will refuse to auto-unlock. Use the recovery passphrase to unlock, then re-enroll.

### Step 6: Configure /etc/crypttab.initramfs

```bash
# Add Storage to crypttab for early boot unlock
echo "storage  /dev/disk/by-partlabel/storage  /etc/cryptsetup-keys.d/storage.key  tpm2-device=auto" \
  >> /etc/crypttab.initramfs
```

### Step 7: Update systemd mount units

Update the existing mount units to use the LUKS mapper device instead of the raw partition.

**Storage-dabrown.mount** — update `What=` and add device dependency:

```ini
[Unit]
Description=Mount encrypted Storage partition (dabrown)
After=dev-mapper-storage.device
Requires=dev-mapper-storage.device

[Mount]
What=/dev/mapper/storage
Where=/Storage/dabrown
Type=btrfs
Options=subvol=@dabrown,defaults,noatime,compress=zstd

[Install]
WantedBy=multi-user.target
```

**Storage-Backups.mount** — same pattern:

```ini
[Unit]
Description=Mount encrypted Storage partition (backups)
After=dev-mapper-storage.device
Requires=dev-mapper-storage.device

[Mount]
What=/dev/mapper/storage
Where=/Storage/Backups
Type=btrfs
Options=subvol=@backup,defaults,noatime,compress=zstd

[Install]
WantedBy=multi-user.target
```

**home-dabrown-*.mount** — no changes needed. They already depend on `Storage-dabrown.mount`:

```ini
[Unit]
Description=Bind /Storage/dabrown/<DIR> to /home/dabrown/<DIR>
After=Storage-dabrown.mount
Requires=Storage-dabrown.mount
```

The dependency chain ensures:
1. LUKS unlocks → `/dev/mapper/storage` appears
2. `Storage-dabrown.mount` and `Storage-Backups.mount` mount the subvolumes
3. `home-dabrown-*.mount` bind-mounts into `/home/dabrown/`

### Step 8: Regenerate initramfs and reboot

```bash
mkinitcpio -P
reboot
```

## Verification

```bash
# Confirm LUKS is active and auto-unlock worked
lsblk -f /dev/disk/by-partlabel/storage

# Confirm mapper device is open
ls /dev/mapper/storage

# Confirm mounts via systemd
systemctl list-units --type=mount | grep Storage

# Confirm bind mounts
systemctl list-units --type=mount | grep home-dabrown

# Confirm TPM2 enrollment
systemd-cryptenroll /dev/disk/by-partlabel/storage
```

## Rollback

If auto-unlock fails on boot:

```bash
# Boot from live USB, then:
cryptsetup open /dev/disk/by-partlabel/storage storage
mount --mkdir /dev/mapper/storage /Storage/dabrown
```

## References

- Root volume LUKS + TPM2: follows same PCR 7 pattern as base install
- Systemd mount units: `systemd/system/`
