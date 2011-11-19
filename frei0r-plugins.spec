%define date	%(echo `LC_ALL="C" date +"%a %b %d %Y"`)

%define split 1

#%define snapshot 20110220

Summary:        A minimalistic plugin API for video effects
Name:           frei0r-plugins
#Version:        1.1.22_git%{snapshot}
Version:        1.3
Release:        %mkrel 1
License:        GPLv2+
Group:          System/Libraries
URL:		http://www.piksel.org/frei0r
Source0:	http://www.piksel.no/frei0r/releases/frei0r-plugins-%{version}.tar.gz
## git clone --depth=1 git://code.dyne.org/frei0r.git
#Source0:        frei0r-%{snapshot}.tar.bz2
Patch0:         %{name}-no-return-in-nonvoid-function.patch
Patch1:         %{name}-sequence-point.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc-c++
BuildRequires:  gavl-devel >= 0.2.3
BuildRequires:  doxygen
#%if %suse_version >= 1110
BuildRequires:  opencv-devel >= 1.0.0
#%endif
BuildRequires:  pkgconfig >= 0.9.0
%if !%{split}
Provides:       %{name}-devel = %{version}
%endif

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

%if %{split}
%package devel
Summary:        Development files for frei0r-plugins
Group:          Development/Other
Requires:       %{name} = %{version}
Requires:       gavl-devel
Requires:       opencv-devel

%description devel
The fri0r-plugins-devel package contains header files for developing
applications that use frei0r-plugins.
%endif #split

%prep
%setup -q -n frei0r-%{version}
#%setup -q -n "frei0r-%{snapshot}"
#%setup -q -n "frei0r"
%patch0 -p1
%patch1 -p1

%build
[ -e ./configure ] || ./autogen.sh
%configure \
    --disable-static
%__make %{?_smp_flags}

%install
%makeinstall_std \
    plugindir=%{_libdir}/frei0r-1

%__rm -f doc/html/Makefile*
%__rm -rf "%{buildroot}%{_datadir}/doc/%{name}-1.1"
%__rm -rf "%{buildroot}%{_datadir}/doc/frei0r-plugins"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README ChangeLog
%dir %{_libdir}/frei0r-1
%{_libdir}/frei0r-1/*.so

%if %{split}
%files devel
%defattr(-,root,root,-)
%endif
#doc doc/html/*
%{_includedir}/*.h
%{_libdir}/pkgconfig/frei0r.pc

