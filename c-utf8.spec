Summary:	UTF-8 Handling in Standard ISO-C11
Name:		c-utf8
Version:	1.1.0
Release:	1
License:	Apache 2.0 or LGPL v2.1+
Group:		Libraries
Source0:	https://github.com/c-util/c-utf8/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a52961128ca3a479a60d8dfb766157d0
URL:		https://c-util.github.io/c-utf8/
BuildRequires:	c-stdaux-devel >= 1.5.0
BuildRequires:	meson >= 0.60.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The c-utf8 project implements utility functions around handling UTF-8
in standard ISO C11.

%package devel
Summary:	Header files for c-utf8 library
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for c-utf8 library.

%package static
Summary:	Static c-utf8 library
Group:		Development/Libraries
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static c-utf8 library.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS.md README.md
%attr(755,root,root) %{_libdir}/libcutf8-1.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcutf8-1.so
%{_includedir}/c-utf8.h
%{_pkgconfigdir}/libcutf8-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcutf8-1.a
