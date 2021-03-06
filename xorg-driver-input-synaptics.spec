Summary:	XOrg/XFree86 input driver for Synaptics and ALPS touchpads
Name:		xorg-driver-input-synaptics
Version:	1.8.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/archive/individual/driver/xf86-input-synaptics-%{version}.tar.bz2
# Source0-md5:	8ed68e8cc674dd61adb280704764aafb
Source1:	%{name}.conf
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libtool
BuildRequires:	mtdev-devel
BuildRequires:	perl-base
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXi-devel >= 1.7
BuildRequires:	xorg-xserver-server-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xorg/XFree86 input driver for Synaptics touchpad.

%prep
%setup -qn xf86-input-synaptics-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d/50-synaptics.conf
rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/input/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/xorg/modules/input/*.so
%{_datadir}/X11/xorg.conf.d/50-synaptics.conf
%{_mandir}/man?/*

