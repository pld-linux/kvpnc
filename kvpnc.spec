Summary:	GUI for VPN Client for various servers
Summary(pl.UTF-8):	GUI dla klienta dla różnych serwerów VPN
Name:		kvpnc
Version:	0.8.9
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.gna.org/kvpnc/%{name}-%{version}.tar.bz2
# Source0-md5:	08cc09eef44da7f14e3a4c3fd73b17ff
Patch0:		%{name}-bash.patch
URL:		http://home.gna.org/kvpnc/en/index.html
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2
BuildRequires:	libgcrypt-devel
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
Requires:	bash
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KVpnc is a KDE frontend for various VPN clients. It supports Cisco VPN
(vpnc) and IPSec (FreeS/WAN, racoon). vpnc is a replacement for the
Cisco VPN client, and is used as client for the cisco3000 VPN
Concentrator. FreeS/WAN (OpenS/WAN) is a IPSec client for Linux 2.4.x,
and raccoon is a IPSec client for Linux 2.6.x and *BSD. It also
supports PPTP (pptpclient) and OpenVPN.

%description -l pl.UTF-8
KVpnc to nakładka na klienta vpnc działajaca w środowisku KDE. Wspiera
Cisco VPN, IPSec (FreeS/WAN, racoon). vpnc jest zamiennikiem dla
klienta VPN Cisco, i jest używany jako klient dla koncentratorów VPN
cisco3000. FreeS/WAN (OpenS/WAN) jest klientem ipsecowym dla Linux
2.4.x oraz racoon w wersji 2.6.x oraz *BSD. Wspiera również protokół
PPTP (pptpclient) oraz OpenVPN.

%prep
%setup -q
%patch0 -p1

cp -f /usr/share/automake/config.* admin

%build
#%{__sed} -i 's,<UI version="3.1",<UI version="3.2",' src/*.ui
#%{__make} -f admin/Makefile.common
%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/config,%{_desktopdir},%{_sbindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/%{name}.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
mv -f $RPM_BUILD_ROOT%{_bindir}/%{name} \
	$RPM_BUILD_ROOT%{_sbindir}/%{name}

echo "Categories=Qt;KDE;System;X-Administration;" >> \
	$RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
echo "Comment[pl]=Klient vpnc dla KDE" >> \
	$RPM_BUILD_ROOT%{_datadir}/apps/kvpnc/eventsrc

install src/%{name}ui.rc $RPM_BUILD_ROOT%{_datadir}/config

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_sbindir}/*
%{_datadir}/apps/kvpnc
%{_datadir}/config/*
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/*/*
# shouldn't be as regular %doc?
%{_kdedocdir}/kvpnc
