#!/bin/bash
mount -o remount,rw /
BOOTDEV=/dev/`$(lsblk -no PKNAME '$(findmnt -rno SOURCE /)"`
BOOTPART=/dev/$(lsblk -Jno NAME,TYPE $BOOTDEV | jq -r ".blockdevices[0].children[0].name")
ROOTPART=/dev/$(lsblk -Jno NAME,TYPE $BOOTDEV | jq -r ".blockdevices[0].children[1].name")
UUID_BOOT=$(uuidgen | cut -d "-" -f1)
UUID_ROOT=$(uuidgen)
umount $BOOTPART
growpart $BOOTDEV 2
resize2fs $ROOTPART
sleep 3
udevadm settle
mv /etc/mtools.conf /etc/mtools.conf.bak
echo "drive c: file=\"$BOOTPART\"" > /etc/mtools.conf
mlabel -N $UUID_BOOT c:
rm -fr /etc/mtools.conf
mv /etc/mtools.conf.bak /etc/mtools.conf
tune2fs -U $UUID_ROOT $ROOTPART
mount $BOOTPART /boot
ffr-genfstab -p -U / | grep -A2 $BOOTDEV > /etc/fstab
ffr-gencmdline | sed "s/ROOTSPEC/root=UUID=$UUID_ROOT/g" > /boot/cmdline.txt
echo $UUID_BOOT > /boot/uuid_boot
echo $UUID_ROOT > /boot/uuid_root
systemctl mask ffr-firstboot.service
dracut -f
