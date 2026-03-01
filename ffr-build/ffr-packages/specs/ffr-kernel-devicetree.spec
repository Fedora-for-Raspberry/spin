Name:           ffr-kernel-devicetree
Version:        VERSIONSTRING
Release:        1
Summary:        Device trees for FfR
ExclusiveArch:	aarch64

License:        GPL
Source0:        %{name}-%{version}.tar.gz

%global debug_package %{nil}

%description
Device trees for Raspberry Pi4/5

%prep
%setup -q

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/boot
cp -r boot/* $RPM_BUILD_ROOT/boot/

%files
/boot/*
