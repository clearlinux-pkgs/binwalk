#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : binwalk
Version  : 2.3.3
Release  : 25
URL      : https://github.com/ReFirmLabs/binwalk/archive/v2.3.3/binwalk-2.3.3.tar.gz
Source0  : https://github.com/ReFirmLabs/binwalk/archive/v2.3.3/binwalk-2.3.3.tar.gz
Summary  : Firmware analysis tool
Group    : Development/Tools
License  : MIT
Requires: binwalk-bin = %{version}-%{release}
Requires: binwalk-license = %{version}-%{release}
Requires: binwalk-python = %{version}-%{release}
Requires: binwalk-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# Binwalk
[![Build Status](https://travis-ci.org/ReFirmLabs/binwalk.svg?branch=master)](https://travis-ci.org/ReFirmLabs/binwalk)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/ReFirmLabs/binwalk/graphs/commit-activity)
[![GitHub license](https://img.shields.io/github/license/ReFirmLabs/binwalk.svg)](https://github.com/ReFirmLabs/binwalk/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/badges/shields.svg?style=social&label=Stars)](https://github.com/ReFirmLabs/binwalk/stargazers)

%package bin
Summary: bin components for the binwalk package.
Group: Binaries
Requires: binwalk-license = %{version}-%{release}

%description bin
bin components for the binwalk package.


%package license
Summary: license components for the binwalk package.
Group: Default

%description license
license components for the binwalk package.


%package python
Summary: python components for the binwalk package.
Group: Default
Requires: binwalk-python3 = %{version}-%{release}

%description python
python components for the binwalk package.


%package python3
Summary: python3 components for the binwalk package.
Group: Default
Requires: python3-core
Provides: pypi(binwalk)

%description python3
python3 components for the binwalk package.


%prep
%setup -q -n binwalk-2.3.3
cd %{_builddir}/binwalk-2.3.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635706854
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/binwalk
cp %{_builddir}/binwalk-2.3.3/LICENSE %{buildroot}/usr/share/package-licenses/binwalk/ef53b2a881493ff495032066771aed6ceae431b8
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/binwalk

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/binwalk/ef53b2a881493ff495032066771aed6ceae431b8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
