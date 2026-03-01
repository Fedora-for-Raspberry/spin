Name:           ffr-kernel
Version:        VERSIONSTRING
Release:        1
Summary:        Linux Kernel for FfR
ExclusiveArch:	aarch64

License:        GPL
Source0:        %{name}-%{version}.tar.gz

Obsoletes:	kernel

%global debug_package %{nil}

%description
Linux Kernel to boot non-supported distributions on the Raspberry Pi 4/5.

%prep
%setup -q

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/boot
cp -r boot/* $RPM_BUILD_ROOT/boot/

%files
/boot/*
