Name:           ffr-bootutils
Version:        VERSIONSTRING
Release:        1
Summary:        Tools for FfR
ExclusiveArch:	aarch64

License:        GPL
Source0:        %{name}-%{version}.tar.gz

Requires:	dracut
Requires:	systemd
Requires:	mtools
Requires:	util-linux
Requires:	bash
Requires:	e2fsprogs
Requires:	sed
Requires:	NetworkManager
Requires:	NetworkManager-wifi
Requires:	NetworkManager-tui
Requires:	iw
Requires:	cloud-utils-growpart

%global debug_package %{nil}

%description
Utilities to boot non-supported distributions on the Raspberry Pi 4/5.

%prep
%setup -q

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{sbin,usr/lib/systemd/system,etc/dracut.conf.d}
cp -r sbin/* $RPM_BUILD_ROOT/sbin/
cp -r usr/lib/systemd/system/* $RPM_BUILD_ROOT/usr/lib/systemd/system/
cp -r etc/dracut.conf.d/* $RPM_BUILD_ROOT/etc/dracut.conf.d/

%files
/sbin/*
/etc/dracut.conf.d/*
/usr/lib/systemd/system/*

%post
systemctl mask network-online.target
systemctl mask rfkill.socket
iw reg set US
systemctl enable ffr-firstboot.service
