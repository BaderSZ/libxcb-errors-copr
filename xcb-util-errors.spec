Name: xcb-util-errors
Version: 1.0
Release: 0%{%dist}
License: MIT
Summary: Errors library for the C protocol C-language Binding.
Url: https://xcb.freedesktop.org/

# 7752a722e580efdbada30632cb23aed35c18757399ac3b547b59fd7257cf5e33  xcb-util-errors-1.0.tar.gz
# Sources can be obtained by:
#   wget -c https://xcb.freedesktop.org/dist/xcb-util-errors-1.0.tar.gz

Source0: https://xcb.freedesktop.org/dist/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: m4
BuildRequires: libxcb-devel
BuildRequires: xcb-proto
BuildRequires: xorg-x11-util-macros

%description
%summary

%package devel
Summary:	Development and header files for xcb-util-errors
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
Development files for xcb-util-errors.

%prep
%setup -q

%build
%{configure}
make %{?_smp_mflags}

%install
export DESTDIR=%{buildroot}
make install

%ldconfig_post

%ldconfig_postun

%files
/usr/include/xcb/xcb_errors.h
/usr/lib64/libxcb-errors.a
/usr/lib64/libxcb-errors.so
/usr/lib64/libxcb-errors.so.0
/usr/lib64/libxcb-errors.so.0.0.0
/usr/lib64/pkgconfig/xcb-errors.pc

%changelog
* Tue Jul 12 2022 Bader Zaidan <bader@zaidan.pw> 1.0-0%{}
- new package built with tito

