Name:           ffr-brcmfmac
Version:        VERSIONSTRING
Release:        1
Summary:        Broadcom wireless firmware for FfR
ExclusiveArch:	aarch64

License:        Proprietary
Source0:        %{name}-%{version}.tar.gz

Requires:	dracut
Requires:	systemd
Requires:	util-linux
Requires:	bash
Requires:	iw
Requires:	brcmfmac-firmware
Requires:	xz
Requires:	findutils
Requires:	NetworkManager

%global debug_package %{nil}

%description
Broadcom/Cypress firmware to boot non-supported distributions on the Raspberry Pi 4/5.

%prep
%setup -q

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{sbin,usr/lib/systemd/system}
cp -r sbin/* $RPM_BUILD_ROOT/sbin/
cp -r usr/lib/systemd/system/* $RPM_BUILD_ROOT/usr/lib/systemd/system/

%files
/usr/lib/systemd/system/*
/sbin/*

%post
systemctl mask network-online.target
systemctl mask rfkill.socket
iw reg set US
iw dev wlan0 set power_save off
ffr-brcmfmac-extract
modprobe -r brcmfmac
modprobe brcmfmac
systemctl enable ffr-brcmfixup.service
