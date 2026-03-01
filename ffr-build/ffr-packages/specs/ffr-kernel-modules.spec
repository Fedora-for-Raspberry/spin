Name:           ffr-kernel-modules
Version:        VERSIONSTRING
Release:        1
Summary:        Kernel modules for FfR
ExclusiveArch:	aarch64

License:        GPL
Source0:        %{name}-%{version}.tar.gz

Obsoletes:	kernel-modules

%global debug_package %{nil}

%description
Kernel modules for Raspberry Pi4/5

%prep
%setup -q

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/lib
cp -r lib/* $RPM_BUILD_ROOT/lib/

%files
/lib/*
