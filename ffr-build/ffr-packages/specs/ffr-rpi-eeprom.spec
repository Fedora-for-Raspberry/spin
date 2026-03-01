Name:           ffr-rpi-eeprom
Version:        VERSIONSTRING
Release:        1
Summary:        EEPROM updater for FfR
ExclusiveArch:	aarch64

License:        Proprietary
Source0:        %{name}-%{version}.tar.gz

Requires:	python3
Requires:	bash
Requires:	flashrom

%global debug_package %{nil}

%description
EEPROM updater for the Raspberry Pi 4/5.

%prep
%setup -q

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/rpi-eeprom
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/etc/default
cp -r usr/share/rpi-eeprom/* $RPM_BUILD_ROOT/usr/share/rpi-eeprom/
cp -r usr/sbin/* $RPM_BUILD_ROOT/usr/sbin/
cp -r etc/default/* $RPM_BUILD_ROOT/etc/default/

%files
/usr/share/rpi-eeprom/*
/usr/sbin/*
/etc/default/*
