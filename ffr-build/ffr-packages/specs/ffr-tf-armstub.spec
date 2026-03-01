Name:           ffr-tf-armstub
Version:        VERSIONSTRING
Release:        1
Summary:        TF-A for FfR
ExclusiveArch:	aarch64

License:        Unknown
Source0:        %{name}-%{version}.tar.gz

%global debug_package %{nil}

%description
PSCI TF-A armstubs for the Raspberry Pi 4/5.

%prep
%setup -q

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/boot
cp -r boot/* $RPM_BUILD_ROOT/boot/

%files
/boot/*
