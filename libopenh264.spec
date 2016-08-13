Name:           libopenh264
Version:        1.6.0
Release:        1%{?dist}
Summary:        Open Source H.264 Codec

License:        BSD
URL:            http://www.openh264.org
Source0:        https://github.com/cisco/openh264/archive/v1.6.0.tar.gz
Patch0:         libdir.patch

BuildRequires:  nasm

%description
OpenH264 is a free software library for real-time encoding and decoding video
streams in the H.264/MPEG-4 AVC format. It is released under the terms of the
Simplified BSD License.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n openh264-%{version}
%patch0 -p1

echo '#!/bin/sh' > ./configure
chmod +x ./configure


%build
%configure
make %{?_smp_mflags} PREFIX=%{_prefix} LIBDIR_NAME=%{_lib}


%install
rm -rf %{buildroot}
%make_install PREFIX=%{_prefix} LIBDIR_NAME=%{_lib}
find %{buildroot} -name '*.a' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc
%{_libdir}/*.so.*

%files devel
%doc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Sat Aug 13 2016 Jajauma's Packages <jajauma@yandex.ru> - 1.6.0-1
- Public release
