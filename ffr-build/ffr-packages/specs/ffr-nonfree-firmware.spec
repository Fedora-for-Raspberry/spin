Name:           ffr-nonfree-firmware
Version:        VERSIONSTRING
Release:        1
Summary:        Nonfree firmware for FfR
ExclusiveArch:	aarch64

License:        GPL
Source0:        %{name}-%{version}.tar.gz

%global debug_package %{nil}

%description
Nonfree firmware to boot non-supported distributions on the Raspberry Pi 4/5.

%prep
%setup -q

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/boot
cp -r boot/* $RPM_BUILD_ROOT/boot/

%files
/boot/*
