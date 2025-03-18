#!/usr/bin/env bash

umount /.snapshots

rmdir /.snapshots

snapper -c root create /

btrfs subvol delete .snapshots

mkdir /.snapshots

mount -a
