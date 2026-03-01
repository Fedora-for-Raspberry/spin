Name:           ffr-kernel-overlays
Version:        VERSIONSTRING
Release:        1
Summary:        Overlays for FfR
ExclusiveArch:	aarch64

License:        GPL
Source0:        %{name}-%{version}.tar.gz

Requires:	ffr-kernel-devicetree

%global debug_package %{nil}

%description
Device trees for Raspberry Pi4/5

%prep
%setup -q

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/boot/overlays/
cp -r boot/overlays/* $RPM_BUILD_ROOT/boot/overlays/

%files
/boot/overlays/*
