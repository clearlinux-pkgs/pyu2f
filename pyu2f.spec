#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyu2f
Version  : 0.1.5
Release  : 18
URL      : https://files.pythonhosted.org/packages/29/b5/c1209e6cb77647bc2c9a6a1a953355720f34f3b006b725e303c70f3c0786/pyu2f-0.1.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/29/b5/c1209e6cb77647bc2c9a6a1a953355720f34f3b006b725e303c70f3c0786/pyu2f-0.1.5.tar.gz
Summary  : U2F host library for interacting with a U2F device over USB.
Group    : Development/Tools
License  : Apache-2.0
Requires: pyu2f-license = %{version}-%{release}
Requires: pyu2f-python = %{version}-%{release}
Requires: pyu2f-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : six

%description
# pyu2f
[![Build Status](https://travis-ci.org/google/pyu2f.svg?branch=master)](https://travis-ci.org/google/pyu2f)

%package license
Summary: license components for the pyu2f package.
Group: Default

%description license
license components for the pyu2f package.


%package python
Summary: python components for the pyu2f package.
Group: Default
Requires: pyu2f-python3 = %{version}-%{release}

%description python
python components for the pyu2f package.


%package python3
Summary: python3 components for the pyu2f package.
Group: Default
Requires: python3-core
Provides: pypi(pyu2f)
Requires: pypi(six)

%description python3
python3 components for the pyu2f package.


%prep
%setup -q -n pyu2f-0.1.5
cd %{_builddir}/pyu2f-0.1.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604339692
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyu2f
cp %{_builddir}/pyu2f-0.1.5/LICENSE %{buildroot}/usr/share/package-licenses/pyu2f/2b8b815229aa8a61e483fb4ba0588b8b6c491890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyu2f/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
