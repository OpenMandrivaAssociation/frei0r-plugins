%define	oname	frei0r
Summary:	A minimalistic plugin API for video effects
Name:		%{oname}-plugins
Version:	1.3
Release:	2
License:	GPLv2+
Group:		System/Libraries
URL:		http://www.piksel.org/frei0r
Source0:	http://www.piksel.no/frei0r/releases/%{name}-%{version}.tar.gz
Patch0:		frei0r-plugins-no-return-in-nonvoid-function.patch
Patch1:		frei0r-plugins-sequence-point.patch
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	pkgconfig(opencv)
Buildrequires:	pkgconfig(gavl)
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

%package	devel
Summary:	Development files for frei0r-plugins
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description	devel
The fri0r-plugins-devel package contains header files for developing
applications that use frei0r-plugins.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1
%patch1 -p1

%build
%configure
%make

%install
%makeinstall_std

%files
%doc AUTHORS README ChangeLog
%dir %{_libdir}/frei0r-1
%{_libdir}/frei0r-1/*.so

%files devel
#doc doc/html/*
%{_includedir}/frei0r.h
%{_libdir}/pkgconfig/frei0r.pc
