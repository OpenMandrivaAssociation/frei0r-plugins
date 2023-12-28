%define	oname frei0r

Summary:	A minimalistic plugin API for video effects
Name:		%{oname}-plugins
Version:	2.3.2
Release:	2
License:	GPLv2+
Group:		System/Libraries
Url:		http://frei0r.dyne.org/
# See also https://github.com/dyne/frei0r
Source0:	https://github.com/dyne/frei0r/archive/refs/tags/v%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gavl)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(opencv4)
%rename		%{oname}

%description
frei0r - a minimalistic plugin API for video effects.

It is a minimalistic plugin API for video sources and filters.
The behaviour of the effects can be controlled from the host by
simple parameters. The intent is to solve the recurring
reimplementation or adaptation issue of standard effects.

It is not meant as a generic API for all kinds of video
applications.

There is no support for the requirements of special application
areas like non linear editors, hardware accelerated shader effects,
and high precision video processing. These advanced issues are not
even solved satisfactory for non cross application plugin apis and
are still an evolving field.

The frei0r API is not meant to be a competing standard to more
ambitious efforts.

%files
%dir %{_libdir}/frei0r-1
%{_libdir}/frei0r-1/*.so

#----------------------------------------------------------------------------

%package	devel
Summary:	Development files for frei0r-plugins
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description	devel
The fri0r-plugins-devel package contains header files for developing
applications that use frei0r-plugins.

%files devel
#doc #{_docdir}/%{name}
%{_includedir}/frei0r.h
%{_libdir}/pkgconfig/frei0r.pc

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n frei0r-%{version}
%cmake \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
