Name:           ffr-kernel-headers
Version:        VERSIONSTRING
Release:        1
Summary:        Kernel headers for FfR
ExclusiveArch:	aarch64

License:        GPL
Source0:        %{name}-%{version}.tar.gz

Obsoletes:	kernel-headers

%global debug_package %{nil}

%description
Kernel headers for Raspberry Pi4/5

%prep
%setup -q

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/include
cp -r /usr/include/* $RPM_BUILD_ROOT/usr/include

%files
/usr/include/*
