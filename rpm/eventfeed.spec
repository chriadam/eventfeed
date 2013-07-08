# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       eventfeed

# >> macros
# << macros

Summary:    Event feed subsystem
Version:    0.2.0
Release:    0
Group:      System/GUI/Other
License:    BSD License
URL:        https://github.com/nemomobile/eventfeed
Source0:    %{name}-%{version}.tar.bz2
Source100:  eventfeed.yaml
BuildRequires:  pkgconfig(QtCore) >= 4.6.0
BuildRequires:  pkgconfig(QtDBus)
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  qt-devel-tools
BuildRequires:  doxygen
Obsoletes:   eventfeed-qmlapi

%description
This package provides a D-Bus service and a QML component needed to show |
event items.


%package -n libeventfeed
Summary:    D-Bus interface for MeegoTouch Events
Group:      Applications/System
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description -n libeventfeed
This library provides D-Bus interface to MeegoTouch Events.


%package -n libeventfeed-devel
Summary:    Development files for libeventfeed
License:    BSD License
Group:      Development/Libraries
Requires:   libeventfeed = %{version}
Provides:   eventfeed-devel = %{version}
Obsoletes:  eventfeed-devel < %{version}

%description -n libeventfeed-devel
This package contains development files for libeventfeed.


%package -n libeventfeed-tests
Summary:    Test suite for libeventfeed
License:    BSD License
Group:      Development/Libraries
Requires:   libeventfeed = %{version}

%description -n libeventfeed-tests
This package contains test suite for libeventfeed.


%package -n libmeegotouchevents
Summary:    D-Bus interface for MeegoTouch Events
Group:      Applications/System
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description -n libmeegotouchevents
This library provides D-Bus interface to MeegoTouch Events.


%package -n libmeegotouchevents-devel
Summary:    Development files for libmeegotouchevents
Group:      Development/Libraries
Requires:   libmeegotouchevents = %{version}

%description -n libmeegotouchevents-devel
This package contains development files for libmeegotouchevents.


%package -n libmeegotouchevents-doc
Summary:    Documentation for libmeegotouchevents
Group:      Documentation

%description -n libmeegotouchevents-doc
This package contains documentation for libmeegotouchevents.


%package -n fakefeeder
Summary:    Utility creating fake events with libmeegotouchevents
Group:      Applications/System
Requires:   %{name} = %{version}-%{release}

%description -n fakefeeder
This utility creates fake events that might be useful when |
developing event views.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake 

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake_install

# >> install post
# << install post

%post -n libeventfeed -p /sbin/ldconfig

%postun -n libeventfeed -p /sbin/ldconfig

%post -n libmeegotouchevents -p /sbin/ldconfig

%postun -n libmeegotouchevents -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_usr}/bin/eventfeedd
%{_datadir}/dbus-1/*
# >> files
# << files

%files -n libeventfeed
%defattr(-,root,root,-)
%{_libdir}/qt4/imports/org/nemomobile/events/*
%{_libdir}/libeventfeed.so.*
# >> files libeventfeed
# << files libeventfeed

%files -n libeventfeed-devel
%defattr(-,root,root,-)
%{_includedir}/eventfeed/*.h
%{_datadir}/qt4/mkspecs/features/eventfeed.prf
%{_libdir}/libeventfeed.so
# >> files libeventfeed-devel
# << files libeventfeed-devel

%files -n libeventfeed-tests
%defattr(-,root,root,-)
/opt/tests/libeventfeed/*
# >> files libeventfeed-tests
# << files libeventfeed-tests

%files -n libmeegotouchevents
%defattr(-,root,root,-)
%{_libdir}/libmeegotouchevents.so.*
# >> files libmeegotouchevents
# << files libmeegotouchevents

%files -n libmeegotouchevents-devel
%defattr(-,root,root,-)
%{_libdir}/libmeegotouchevents.so
%{_includedir}/meegotouchevents/*.h
%{_datadir}/qt4/mkspecs/features/meegotouchevents.prf
# >> files libmeegotouchevents-devel
# << files libmeegotouchevents-devel

%files -n libmeegotouchevents-doc
%defattr(-,root,root,-)
%{_datadir}/doc/libmeegotouchevents/*
# >> files libmeegotouchevents-doc
# << files libmeegotouchevents-doc

%files -n fakefeeder
%defattr(-,root,root,-)
%{_usr}/bin/fakefeeder
# >> files fakefeeder
# << files fakefeeder
