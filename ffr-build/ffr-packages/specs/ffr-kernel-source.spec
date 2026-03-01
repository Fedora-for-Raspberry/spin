Name:           ffr-kernel-source
Version:        VERSIONSTRING
Release:        1
Summary:        Linux Kernel Source for FfR
ExclusiveArch:	aarch64

License:        GPL
Source0:        %{name}-%{version}.tar.gz

Obsoletes:	kernel-devel

%global debug_package %{nil}

%description
Linux Kernel source for FfR

%prep
%setup -q

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/src
cp -r usr/src/* $RPM_BUILD_ROOT/usr/src/

%files
/usr/src/*
