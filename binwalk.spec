#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : binwalk
Version  : 2.1.0
Release  : 2
URL      : https://files.pythonhosted.org/packages/6e/a8/b52eb5fb66f4b582aa21f3b236bcd479bb2d2f602b639d5632a1b080e747/binwalk-2.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/6e/a8/b52eb5fb66f4b582aa21f3b236bcd479bb2d2f602b639d5632a1b080e747/binwalk-2.1.0.tar.gz
Summary  : A tool for searching a given binary image for embedded files
Group    : Development/Tools
License  : MIT
Requires: binwalk-bin = %{version}-%{release}
Requires: binwalk-python = %{version}-%{release}
Requires: binwalk-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
No detailed description available

%package bin
Summary: bin components for the binwalk package.
Group: Binaries

%description bin
bin components for the binwalk package.


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

%description python3
python3 components for the binwalk package.


%prep
%setup -q -n binwalk-2.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1550586531
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/binwalk

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
