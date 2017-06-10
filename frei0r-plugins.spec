%define	oname frei0r

Summary:	A minimalistic plugin API for video effects
Name:		%{oname}-plugins
Version:	1.6.1
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.piksel.org/frei0r
Source0:	http://www.piksel.no/frei0r/releases/%{name}-%{version}.tar.gz
Patch0:		frei0r-1.3-doc-destdir-support.patch
Patch1:		frei0r-1.3-build-docs-by-default.patch
BuildRequires:	autoconf
BuildRequires:	cmake
BuildRequires:	doxygen
Buildrequires:	pkgconfig(cairo)
Buildrequires:	pkgconfig(gavl)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(opencv)
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
%doc AUTHORS README ChangeLog
%exclude %{_docdir}/%{name}/html
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
%doc %{_docdir}/%{name}/html
%{_includedir}/frei0r.h
%{_libdir}/pkgconfig/frei0r.pc

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1 -b .destdir~
%patch1 -p1 -b .doc~
autoreconf -fiv

%build
%configure
%make

%install
%makeinstall_std

